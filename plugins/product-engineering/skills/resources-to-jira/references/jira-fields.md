# Jira Fields & Lean Templates (Developer-First)

Use this reference when creating Jira issues from a validated PRD or design plan[cite: 4]. All epics and stories must remain concise, actionable, and free of enterprise fluff.

---

## BlueFlame BFAI Common Fields

Story custom fields commonly required in `BFAI`[cite: 4]:

| Field | Key | Type | Value |
|---|---|---|---|
| Product Area | `customfield_10134` | Select option | `{"id": "OPTION_ID"}` |
| Testing Needed? | `customfield_10095` | Multi-checkbox array | `[{"id": "10162"}]` for Yes |
| Acceptance Criteria | `customfield_10132` | ADF document | Use `scripts/adf_acceptance.py` |

Product Area option IDs commonly used[cite: 4]:

| Value | ID |
|---|---|
| Connections | `10231` |
| Chat | `10180` |
| Blueprints | `10174` |
| API | `10592` |
| Authentication | `10591` |
| Agent V2 | `12056` |
| Activity | `10491` |

Testing Needed option IDs[cite: 4]:

| Value | ID |
|---|---|
| Yes | `10162` |
| No | `10163` |

*Note: Always query field metadata before relying on these IDs. Field availability can differ by issue type[cite: 4].*

---

## Epic Description Template

```markdown
# Epic: [Feature Name]

## Overview & Value
- **Goal:** [1-2 sentences max on what is being built]
- **User/Business Value:** [1 sentence explaining why this matters or what problem it solves]

## Core Technical Scope
- **API / Protocol:** [e.g., REST, GraphQL, Webhook]
- **Auth Strategy:** [e.g., OAuth2, API Key, JWT]
- **Key Files/Modules:** [List primary codebase touchpoints]

## Out of Scope (V2)
- [Explicitly cut feature 1]
- [Explicitly cut feature 2]

## Dependency & Execution Order
1. `[Phase 0 Foundation]` -> 2. `[Phase 1 MVP]` -> 3. `[Phase 2 Endgame]`
```

---

## Story Description Template (<100 Words)

```markdown
# Story: [Title]

**Phase:** [Phase N] | **Effort:** [S / M / L] | **Type:** [Feature / Bug / Task]

---

## Goal & Value
* **Goal:** [1 sentence describing what to build]
* **User/Business Value:** [1 sentence explaining why this task matters]

## Implementation Approach
* **Files to Touch:** `path/to/file.py` (Create / Modify)
* **Pattern / Helper to Follow:** [Existing pattern or helper to reuse]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Dependencies & Blocks
* **Depends on:** [Story Key or None]
* **Blocks:** [Story Key or None]
```

---

## Story Creation Pattern & API Example

Story summaries must include the phase prefix and any sequencing keyword determined during planning[cite: 4]:

```text
[Phase 0 Foundation] Feature: Setup Database Models
[Phase 1 MVP] Feature: Build API Endpoint
[Phase 2 ENDGAME] Feature: Logging & Observability
```

Use this execution pattern when calling the Jira API tool[cite: 4]:

```python
createJiraIssue(
    cloudId="<cloud-id>",
    projectKey="BFAI",
    issueTypeName="Story",
    summary="[Phase 1 MVP] Feature: Build API Endpoint",
    description="<full markdown description filled out using the Story Description Template above>",
    parent="<EPIC-KEY>",
    additional_fields={
        "customfield_10134": {"id": "10231"},
        "customfield_10095": [{"id": "10162"}],
        "customfield_10132": <ADF JSON object>,
        "labels": ["connections", "feature-name"],
    },
)
```

---

## Common Pitfalls

- Acceptance Criteria must be ADF (`customfield_10132`), not a string[cite: 4].
- Product Area may not exist on Epic issue type; check metadata[cite: 4].
- Do not create Jira issues from unvalidated design assumptions[cite: 4].
- Prefer synchronous implementation patterns unless the codebase clearly uses async in that area[cite: 4].
- Keep tickets functional and PR-sized; avoid enum-only or entity-only stories unless they are subtasks[cite: 4].
