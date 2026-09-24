# CampusPark specification

What this file is for: the build takes its instructions from here, and
everything here comes from the model rather than from a product idea. Each
item cites the requirement or use case action it came from, so a reviewer can
go the other way and check that nothing was invented on the way into the code.

Sources are the Airport Kiosk style Operational Requirements Document imported
into Innoslate (cited as ORD 5.x) and use case UC.1 Driver Finds and Reserves
Campus Parking (cited as UC.1.n).

This version covers the primary path only. Failed permit checks, no capacity,
cancellations and interface outages are real cases and they are not specified
yet, for the same reason UC.1 does not model them: the stakeholder
requirements that govern them are due October 4.

## Scope of this version

In: one driver, one trip, one reservation, along the normal success path.

Out: sensors, cameras, plate readers, gates, payment, enforcement, rule
changes, campus-wide rollout. Those are excluded in the BMA report and stay
excluded here.

## The path the system implements

| Step | What happens | From |
| --- | --- | --- |
| 1 | Driver submits identity, destination, arrival time, parking duration | UC.1.1, ORD 5.1.1.1, 5.1.1.3 |
| 2 | System requests identity and permit validation | UC.1.2, ORD 5.1.2.2 |
| 3 | Permit system returns identity and permit eligibility | UC.1.3, ORD 5.1.1.2 |
| 4 | System requests lot locations and routes | UC.1.4, ORD 5.1.2.4 |
| 5 | Map service returns locations and routes | UC.1.5, ORD 5.1.1.4 |
| 6 | System applies rules, permit limits, location and capacity, returns eligible options | UC.1.6, ORD 5.1.4.2, 5.1.4.3 |
| 7 | Driver selects an option and requests a reservation | UC.1.7 |
| 8 | System rechecks eligibility and capacity, records the reservation | UC.1.8, ORD 5.1.4.4 |
| 9 | System returns confirmation and navigation guidance | UC.1.9, ORD 5.1.2.5, 5.1.2.16 |
| 10 | Driver reviews the confirmation | UC.1.10 |

Step 8 repeats the checks from steps 2 and 6 on purpose. Conditions change
between browsing and committing, and a reservation that was valid at search
time is not necessarily valid a minute later.

## Components and what each one owes

### api/eligibility.py

Given a permit profile and a set of candidate lots, return the lots the permit
covers. Returns the same answer for the same inputs; no ranking, no capacity
logic. Called twice per session, once at step 2 and once at step 8.

Comes from ORD 5.1.4.1 and 5.1.1.2.

### api/ranking.py

Given eligible lots, destination, arrival time and capacity figures, return
the lots in the order the driver should see them. Distance to destination and
expected availability are the two factors the model already commits to. How
they are weighted is open until the stakeholder requirements are written, and
that gap should stay visible here rather than be filled in by a guess.

Comes from UC.1.6 and the Campus Driver need in section 3 of the BMA report.

### api/reservations.py

Record a reservation against a lot for a time window, and report remaining
reservable capacity. Remaining capacity is configured capacity minus
reservations already held for that window. Refuses the reservation and returns
nothing when eligibility or capacity fails the recheck.

Comes from UC.1.8, UC.1.9 and ORD 5.1.2.6.

### integrations/permit/client.py

One call: given a driver identity, return the permit profile. Owned by the
Campus Identity & Permit System, which we read and never write. Stubbed with
fixture data until access is arranged, which is open assumption A2 in the
report.

### integrations/map/client.py

Two calls: candidate lots near a destination, and a route to a chosen lot.
Also read-only, also stubbed.

### web/

One screen: the trip form, the option list, the confirmation. Fields follow
the requirements rather than a sketch of a nice looking form, so this waits
for the October 4 work.

## What the system has to be judged on

These are the two measures already drafted in the BMA report, carried here so
the build has the same targets as the model.

| Measure | Target | How it gets checked |
| --- | --- | --- |
| Recommendation accuracy | 90 percent or better of displayed options are actually usable by that driver | Audit a sample of recommendations against permit rules, posted restrictions, configured capacity and the requested trip |
| Parking search time | Reduced by 20 percent or more against the current process | Timed matched tasks, current process as baseline |

The first measure is about the correctness of the information, not about
whether a physical space is free on arrival. Nothing in this version can claim
the second thing, and the spec should not pretend otherwise.

## Known limits of this version

Availability is calculated, not measured. Both external services are stubs.
Only the success path exists. Anything a reader finds in the code that is not
traceable to a line above should be treated as a defect in this document, not
as a feature.
