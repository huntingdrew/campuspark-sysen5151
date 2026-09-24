"""Talks to the Campus Map & Navigation Service.

Also outside our boundary. We send a location and route request, it returns
lot locations and route information. Two calls in the UC.1 flow depend on it:
building the option list (UC.1.4 and UC.1.5) and returning guidance after the
reservation is recorded (UC.1.9).

Stubbed, same reason as the permit client.
"""


def lots_near(destination):
    """Return candidate lots with their locations, nearest first."""
    raise NotImplementedError


def route_to(lot, origin=None):
    """Return navigation guidance for a reserved lot."""
    raise NotImplementedError
