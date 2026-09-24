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

### Template for future entries

```
### YYYY-MM-DD · name · tool

**Asked for:**

**Produced:**

**Inputs given to the tool:**

**Checked:**
```
