"""Hold a space and remember that we held it (UC.1.8, UC.1.9).

Everything lives in memory for now, so restarting the server clears the
reservations. A database is fine to add later; it isn't what the milestone is
checking.

Worth repeating because it drives the whole design: remaining capacity is
configured capacity minus reservations we recorded. It is not a measurement.
A confirmation means we set capacity aside, not that a space is empty.
"""

import uuid

# reservation records, newest last
_RESERVATIONS = []


def remaining_capacity(lot, window):
    taken = sum(
        1 for r in _RESERVATIONS
        if r["lot_id"] == lot["id"] and r["window"] == window
    )
    return lot["capacity"] - taken


def reserve(profile, lot, destination, window):
    """Record a reservation. Returns None if the lot filled up in the meantime."""
    if remaining_capacity(lot, window) <= 0:
        return None
    record = {
        "id": uuid.uuid4().hex[:8],
        "driver_id": profile["driver_id"],
        "lot_id": lot["id"],
        "lot_name": lot["name"],
        "destination": destination,
        "window": window,
    }
    _RESERVATIONS.append(record)
    return record


def all_reservations():
    return list(_RESERVATIONS)
