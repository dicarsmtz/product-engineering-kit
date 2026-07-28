# Jira Fields & Lean Templates (Developer-First)

Use this reference when creating Jira issues from a validated PRD or design plan. All epics and stories must remain concise, actionable, and free of enterprise fluff.

---

## Common Fields

Story custom fields commonly required in `BFAI`:

| Field | Key | Type | Value |
|---|---|---|---|
| Product Area | `customfield_10134` | Select option | `{"id": "OPTION_ID"}` |
| Testing Needed? | `customfield_10095` | Multi-checkbox array | `[{"id": "10162"}]` for Yes |
| Acceptance Criteria | `customfield_10132` | ADF document | Use `scripts/adf_acceptance.py` |

Product Area option IDs commonly used:

| Value | ID |
|---|---|
| Connections | `10231` |
| Chat | `10180` |
| Blueprints | `10174` |
| API | `10592` |
| Authentication | `10591` |
| Agent V2 | `12056` |
| Activity | `10491` |

Testing Needed option IDs:

| Value | ID |
|---|---|
| Yes | `10162` |
| No | `10163` |

*Note: Always query field metadata before relying on these IDs. Field availability can differ by issue type.*

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
