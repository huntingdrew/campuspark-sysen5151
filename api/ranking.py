"""Order the eligible lots into the list the driver sees (UC.1.6).

Walk time first, remaining capacity as the tie breaker. That ordering is a
placeholder: how to weigh distance against the chance of a space is a
stakeholder requirements question, and those are due Oct 4. Leaving it simple
and obvious until then beats inventing a score nobody asked for.
"""

from api import reservations


def rank(lots, destination, window):
    scored = []
    for lot in lots:
        free = reservations.remaining_capacity(lot, window)
        if free <= 0:
            continue  # nothing to offer, don't show it
        scored.append({**lot, "remaining": free})
    return sorted(scored, key=lambda l: (l["walk_minutes"], -l["remaining"]))
