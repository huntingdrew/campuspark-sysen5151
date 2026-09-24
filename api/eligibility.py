"""Which lots this driver's permit actually covers.

UC.1.2, and again at UC.1.8 before the reservation is recorded. ORD 5.1.4.1.
"""


def eligible_lots(profile, candidate_lots):
    """Keep only the lots this permit type is allowed to use."""
    permit = profile["permit"]
    return [lot for lot in candidate_lots if permit in lot["permits"]]


def is_still_eligible(profile, lot):
    """Same check, run again at reservation time.

    Rules can change between the search and the moment the driver commits, so
    we don't trust the earlier result.
    """
    return profile["permit"] in lot["permits"]
