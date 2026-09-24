"""Talks to the Campus Identity & Permit System.

That system sits outside our boundary. It owns permit data; we only read it.
The exchange is defined in section 4.5 of the BMA report: we send an identity
and permit validation request, it returns identity and permit eligibility.

Stubbed for the walking skeleton. Real access has to be arranged with Campus
IT, which is one of the open assumptions in the report (A2).
"""


def validate(driver_id):
    """Return the driver's permit profile.

    Until the real interface exists this returns fixture data so the rest of
    the path can run end to end.
    """
    raise NotImplementedError
