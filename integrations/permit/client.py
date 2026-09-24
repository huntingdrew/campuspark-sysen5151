"""Campus Identity & Permit System.

Outside our boundary, we only read from it. Real access still has to go
through Campus IT (assumption A2 in the report), so for now this returns
fixture data.
"""

# Three permit types, enough to show that eligibility actually filters.
FIXTURE_PROFILES = {
    "student01": {"driver_id": "student01", "name": "Student driver", "permit": "student"},
    "staff01": {"driver_id": "staff01", "name": "Staff driver", "permit": "staff"},
    "visitor01": {"driver_id": "visitor01", "name": "Visitor", "permit": "visitor"},
}

DEFAULT_PROFILE = FIXTURE_PROFILES["student01"]


def validate(driver_id):
    """Return the driver's permit profile, or None if we don't know them.

    UC.1.3. The real call will be a request to the permit system.
    """
    if not driver_id:
        return DEFAULT_PROFILE
    return FIXTURE_PROFILES.get(driver_id.strip().lower())
