"""Decides which lots a given driver is allowed to use.

Covers ORD 5.1.1.2 (accept customer ID), 5.1.1.4 (accept customer records)
and 5.1.4.1 (provide access to an authorized customer). In the UC.1 flow this
is action UC.1.2, and it runs again before a reservation is recorded
(UC.1.8), because a permit or a rule can change between the two.

Nothing here is implemented yet. The signatures exist so the walking skeleton
has something to call.
"""


def eligible_lots(permit_profile, candidate_lots):
    """Return the subset of candidate_lots the permit actually covers.

    permit_profile comes from the Campus Identity & Permit System.
    candidate_lots comes from administrator-maintained lot rules.
    """
    raise NotImplementedError


def is_still_eligible(permit_profile, lot, arrival_time):
    """Second check, run at reservation time rather than at search time."""
    raise NotImplementedError
