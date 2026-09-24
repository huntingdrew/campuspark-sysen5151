# CampusPark

Permit-aware campus parking recommendation and reservation platform. Course project for SYSEN 5151, Team 25.

## What problem this addresses

A campus driver has to answer several questions before every trip. Where am I allowed to park with my permit. How far is that lot from where I am actually going. Will there be a space when I arrive. Today those answers live in different places, so the driver ends up comparing them by hand and often still guesses wrong.

CampusPark brings those pieces into one flow. The driver gives a destination, an arrival time and how long they need to park. The system checks what their permit actually allows, looks up lot locations and routes, applies the parking rules and current capacity, and comes back with options the driver is eligible to use. The driver picks one, requests a reservation, and gets a confirmation and directions.

## How a session runs

This is the normal path, modeled as use case UC.1 in our Innoslate model.

1. Driver submits identity, destination, arrival time and parking duration
2. CampusPark asks the Campus Identity & Permit System to validate identity and permit eligibility
3. CampusPark asks the Campus Map & Navigation Service for lot locations and routes
4. CampusPark applies parking rules, permit limits, location and available capacity, then presents the eligible options
5. Driver selects an option and requests a reservation
6. CampusPark rechecks eligibility and capacity, then records the reservation
7. CampusPark returns the reservation confirmation and navigation guidance

Step 6 matters more than it looks. Conditions can change between the first search and the moment the driver commits, so eligibility and capacity are checked twice rather than once.

## What sits outside the system

Four external participants, taken from the system context diagram in our Business or Mission Analysis report.

| External system or actor | What it gives us | What we send it |
| --- | --- | --- |
| Campus Driver | Destination, arrival time, parking duration, option selection, reservation request | Eligible parking options, reservation confirmation, navigation guidance |
| Campus Identity & Permit System | Identity and permit eligibility | Identity and permit validation requests |
| Campus Map & Navigation Service | Lot locations and route information | Location and route requests |
| Parking Administrator | Lot rules, permit restrictions, reservable capacity | Update acknowledgements |

CampusPark does not own permit data or map data. It reads both and is responsible for turning them into a parking decision.

## Scope

Inside: trip intake, permit-aware filtering, option ranking, reservation records, confirmation and guidance, plus the administrative data that the recommendation depends on.

Outside: cameras, parking sensors, license plate readers, physical gates, payment processing. The system also does not change university permit rules or enforce parking regulations.

That boundary follows from the solution class we picked. Of the three we evaluated, the sensor and gate version gives the best availability data but needs equipment in every lot, and the cost, installation and privacy review put it out of reach for a nine month pilot. We went with the digital-only version instead and accepted its one real weakness: availability is calculated from capacity and reservation records rather than measured, so a confirmed reservation means the platform has set capacity aside, not that a sensor has seen an empty space.

## Repository layout

```
api/                  CampusPark itself: eligibility filtering, option ranking, reservations
integrations/permit/  Client for the Campus Identity & Permit System
integrations/map/     Client for the Campus Map & Navigation Service
web/                  Driver-facing interface
docs/                 SPEC.md, prompt log, notes that tie code back to the model
```

The top-level folders follow the system context rather than a framework's default layout, so each external system in the model has one place in the code where it is dealt with.

## Status

Early. The MBSE model is further along than the build.

Done so far: business and mission analysis, operational concept, system context and hierarchy, UC.1 modeled as use case, action, activity and sequence diagrams, and the operational requirements document imported into Innoslate.

Next: stakeholder needs and requirements, due October 4, then a walking skeleton that runs one end to end path with the two external services stubbed.

## Team

Hangting Zhu, Junjie Luo, Yixuan Zhu, Yuxin Wang
