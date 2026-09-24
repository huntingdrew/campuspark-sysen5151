"""Holds a space for a driver and records what was held.

UC.1.8 and UC.1.9 in the model. ORD 5.1.2.6 (provide transactions to the
Reservation System) and 5.1.2.16 (provide a boarding-pass equivalent, here the
reservation confirmation) sit behind this file.

One thing worth being explicit about, because it shapes everything in here:
availability is derived from configured capacity and existing reservations,
not measured. A confirmed reservation means CampusPark has set capacity aside
in its own records. It does not mean a sensor has seen an empty space. That
limitation is documented in the BMA report and carries into the requirements.
"""


def reserve(driver_id, lot, arrival_time, duration):
    """Record a reservation and return a confirmation.

    Re-checks eligibility and remaining capacity first. Returns None when the
    option is no longer available so the caller can send the driver back to
    the option list.
    """
    raise NotImplementedError


def remaining_capacity(lot, window):
    """Reservable capacity for a lot over a time window.

    Configured capacity minus reservations already recorded in that window.
    """
    raise NotImplementedError
