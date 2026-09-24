"""Walking skeleton for UC.1.

One path, end to end: the driver asks for parking, we check the permit, get
lots from the map service, filter and rank them, the driver picks one, we
re-check and record the reservation, then send back a confirmation.

Both external services are stubs. Run it with:
    uvicorn api.main:app --reload
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from api import eligibility, ranking, reservations
from integrations.map import client as map_client
from integrations.permit import client as permit_client

app = FastAPI(title="CampusPark")


class OptionsRequest(BaseModel):
    driver_id: str = "student01"
    destination: str = "Duffield Hall"
    arrival: str = "09:00"
    hours: int = 2


class ReserveRequest(OptionsRequest):
    lot_id: str


def window_of(req):
    # Good enough for the skeleton: one slot per arrival time.
    return f"{req.arrival}+{req.hours}h"


@app.get("/")
def home():
    return FileResponse("web/index.html")


@app.get("/api/destinations")
def destinations():
    return {"destinations": map_client.DESTINATIONS}


@app.post("/api/options")
def options(req: OptionsRequest):
    """UC.1.2 through UC.1.6."""
    profile = permit_client.validate(req.driver_id)
    if profile is None:
        return {"error": "We don't recognise that ID. Try student01, staff01 or visitor01."}

    candidates = map_client.lots_near(req.destination)
    allowed = eligibility.eligible_lots(profile, candidates)
    ranked = ranking.rank(allowed, req.destination, window_of(req))

    return {
        "permit": profile["permit"],
        "options": [
            {
                "lot_id": lot["id"],
                "name": lot["name"],
                "walk_minutes": lot["walk_minutes"],
                "remaining": lot["remaining"],
            }
            for lot in ranked
        ],
    }


@app.post("/api/reserve")
def reserve(req: ReserveRequest):
    """UC.1.8 and UC.1.9, including the second eligibility and capacity check."""
    profile = permit_client.validate(req.driver_id)
    if profile is None:
        return {"error": "Unknown driver."}

    lots = {l["id"]: l for l in map_client.lots_near(req.destination)}
    lot = lots.get(req.lot_id)
    if lot is None:
        return {"error": "That lot isn't in the list any more."}

    # Re-check rather than trusting what we showed a minute ago.
    if not eligibility.is_still_eligible(profile, lot):
        return {"error": "Your permit no longer covers that lot."}

    record = reservations.reserve(profile, lot, req.destination, window_of(req))
    if record is None:
        return {"error": "That lot just filled up. Pick another option."}

    return {
        "confirmation": record["id"],
        "lot": lot["name"],
        "guidance": map_client.route_to(lot, req.destination),
        "note": "Capacity is held in our records. We do not sense the physical space.",
    }
