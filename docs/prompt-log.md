# Prompt and provenance log

Required by the course: any work done with generative AI gets recorded here,
with enough detail that a reader can tell what was asked for and what came
back. The course also rules out generating the whole project from one broad
prompt, so the entries below are scoped to a single file or a single question
each.

Format: date, who, tool, what was asked, what was produced, what the human
checked or changed.

---

### 2026-09-24 · Hangting Zhu · Claude (Opus 5)

**Asked for:** a README written from our approved OpsCon and system context,
covering the problem, the UC.1 flow, the four external participants, and the
in and out of scope lists from the BMA report.

**Produced:** `README.md`.

**Inputs given to the tool:** our submitted Business or Mission Analysis
report, the Milestone Check 1 criteria document.

**Checked:** external participants and the seven step flow match section 4 and
section 5 of the report. Scope list matches section 1.1 and 9.2. No feature
appears that is not in the report.

---

### 2026-09-24 · Hangting Zhu · Claude (Opus 5)

**Asked for:** a package layout that mirrors the system context diagram rather
than a generic framework starter, with stub modules whose docstrings cite the
requirement or use case action each one serves.

**Produced:** `api/eligibility.py`, `api/ranking.py`, `api/reservations.py`,
`integrations/permit/client.py`, `integrations/map/client.py`,
`web/README.md`. All function bodies raise NotImplementedError.

**Checked:** one top level folder per element of the system context. Each
module cites ORD numbers and UC.1 actions. No implementation was requested or
accepted at this stage, since the ranking rules and error handling depend on
the stakeholder requirements due October 4.

---

### 2026-09-24 · Hangting Zhu · Claude (Opus 5)

**Asked for:** a specification file derived from the ORD requirements and the
UC.1 flow, covering the primary path only, with the gaps left visible.

**Produced:** `docs/SPEC.md`.

**Checked:** every step in the path table cites a UC.1 action and, where one
exists, an ORD requirement number. The two measures match the ones in the BMA
report. Off nominal cases are listed as not specified rather than filled in.

---

### 2026-09-24 · Hangting Zhu · Claude (Opus 5)

**Asked for:** a walking skeleton covering UC.1 only, with the permit system
and the map service returning fixture data, and the second eligibility and
capacity check kept as a real step rather than skipped.

**Produced:** implementations in `api/eligibility.py`, `api/ranking.py`,
`api/reservations.py`, both integration clients, `api/main.py` with
`/api/options` and `/api/reserve`, and `web/index.html`.

**Checked by running it:** a student permit and a visitor permit get different
lots back, remaining capacity drops from 15 to 14 after a reservation, a
student trying to reserve the visitor garage is refused by the recheck at step
8, and an unknown driver ID returns a message instead of an error page. The
browser flow completes from the form through to a confirmation number.

**Left deliberately undone:** ranking weights, error handling for a downed
external service, persistence. Those depend on the stakeholder requirements
due October 4, and filling them in now would put behaviour in the code that no
requirement asks for.

---

### Template for future entries

```
### YYYY-MM-DD · name · tool

**Asked for:**

**Produced:**

**Inputs given to the tool:**

**Checked:**
```


### 2026-09-30 Chapter 3 specification and acceptance work

**Requested by:** the Team 25 project user. No individual name is assigned to this entry.

**Tool:** Codex.

**Asked for:** complete the remaining Chapter 3.5 specification, data and AI response contracts, named failing tests, commit, and automatic checks in the existing CampusPark repository.

**Inputs:** the saved CampusPark Chapter 3 report draft; Innoslate project 13360 with 13 needs, 18 stakeholder requirements, and 20 source links; the current Canvas assignment and rubric screenshots; Lab Manual Chapter 3; the existing specification and walking skeleton.

**Produced:** an updated `docs/SPEC.md`; `tests/acceptance_cases.json`; 20 named tests in `tests/test_spec_acceptance.py`; one trace check in `tests/test_spec_coverage.py`; `requirements-dev.txt`; `.github/workflows/chapter3-acceptance.yml`; updated README instructions.

**Assistant work:** copied the current draft need statements, requirement statements, MOEs, and validation criteria without changing their targets. Added repository criterion IDs and test names. Described current fixture fields and planned contract behavior separately. Flagged the earlier 20%/90% targets and the newer Chapter 3 proposals for review. This was drafting and technical review, not a claim that the team wrote these criteria without assistant help.

**Technical checks run:** the local pytest run collected 21 tests. The trace check passed and all 20 acceptance placeholders failed with their named assertion messages. The process returned exit code 1. No syntax, collection, or dependency error caused those 20 failures. A separate review checked that all source statements, MOEs, and validation criteria matched the saved Chapter 3 data.

**Human review:** the user authorized this repository work and confirmed the repository URL. Team adoption of the criteria, owner approval, and real user or field validation remain pending. No completed human review or stakeholder approval is claimed.

**Build limits:** application code was not changed for this increment. The existing fixture services, time-window limits, and in-memory records remain. The named red suite follows the manual's Chapter 3 example. The AI contract is specified for later implementation; no live model service was called.

