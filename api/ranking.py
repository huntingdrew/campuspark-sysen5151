"""Orders the eligible lots into the list the driver actually sees.

This is UC.1.6 in the model, the step that turns raw eligibility into a
recommendation. The inputs are the eligible lots, the driver's destination
and arrival time, and the capacity figures the Parking Administrator
maintains.

Ranking rules are not settled yet. They belong to the stakeholder
requirements work due October 4, so this file holds the shape of the call and
nothing more.
"""


def rank(eligible_lots, destination, arrival_time, capacity_by_lot):
    """Return eligible lots ordered best first.

    Distance to destination and expected availability are the two factors we
    know we need. Weighting is open until the requirements are written.
    """
    raise NotImplementedError
