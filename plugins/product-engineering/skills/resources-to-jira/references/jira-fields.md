# Jira Fields And Templates

Use this reference when creating Jira issues from a validated design plan.

## BlueFlame BFAI Common Fields

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

Always query field metadata before relying on these IDs. Field availability can differ by issue type.

## Epic Description Template

```markdown
# Epic: [Feature Name]

## Overview
[2-3 sentences: what and why]

## Business Value
- [Benefit 1]
- [Benefit 2]

## Technical Architecture
- **API**: [type]
- **Auth**: [mechanism]
- **Key components**: [list]

## Technical Scope
- [Component 1]
- [Component 2]

## Out of Scope
- [Explicitly excluded item 1]

## Key Risks
1. [Risk + mitigation]

## Design Reference
- [Link to design doc]

## Stories Breakdown
1. [Story title] (Phase N)
2. [Story title] (Phase N)

## Dependency And Collaboration Plan
- **Critical path:** [Story A -> Story B -> Story C]
- **Parallel lanes:** [Lane 1], [Lane 2]
- **Same-owner bundles:** [Stories that should be assigned together]
- **Conflict sets:** [Stories that should not be edited concurrently]
- **Handoff points:** [Contracts, interfaces, fixtures, or flags to agree first]
```

## Story Description Template

```markdown
# Story N: [Title]

**Story Type:** Technical Task | **Phase:** N - [Name] | **Effort:** [Size]

---

## Description
[2-3 sentences: what needs to be done and why]

## Technical Details

### Implementation Approach
- [Key design decisions]
- [Validated codebase pattern to follow]

### Files to Create/Modify
- **Create**: `path/to/new_file.py`
- **Modify**: `path/to/existing_file.py`

### Dependencies
- Story N: [dependency description]

### Collaboration Plan
- **Blocks:** [downstream stories or None]
- **Can run in parallel with:** [story titles or None]
- **Avoid concurrent edits with:** [story titles or None]
- **Suggested ownership:** [same owner as Story N, separate owner from Story N, or any owner]
- **Merge/review order:** [required order or None]

## Acceptance Criteria
- Criterion 1
- Criterion 2

## Technical Notes
- [Non-obvious implementation details]
- [Caveats, gotchas, decisions]
```

## Story Creation Pattern

Story summaries must include the phase prefix and any sequencing keyword determined during planning:

```text
[Phase 0 Foundation] Feature: Story Title
[Phase 0 SPIKE+BUILD] Feature: Validate and implement uncertain adapter
[Phase 1 MVP] Feature: User-visible read path
[Phase 1 GATED] Feature: Product surface wiring
[Phase 2 ENDGAME] Feature: Observability, validation, and runbooks
```

```python
createJiraIssue(
    cloudId="<cloud-id>",
    projectKey="BFAI",
    issueTypeName="Story",
    summary="[Phase N Keyword] Feature: Story Title",
    description="<full markdown description>",
    parent="<EPIC-KEY>",
    additional_fields={
        "customfield_10134": {"id": "10231"},
        "customfield_10095": [{"id": "10162"}],
        "customfield_10132": <ADF JSON object>,
        "labels": ["connections", "feature-name"],
    },
)
```

## Common Pitfalls

- Acceptance Criteria must be ADF, not a string.
- Product Area may not exist on Epic issue type; check metadata.
- Do not create Jira issues from unvalidated design assumptions.
- Do not count same-owner serial bundles as parallel capacity; they are assignment guidance, not extra throughput.
- BlueFlame `bf_defaults` uses tuple-style defaults; verify the current file before proposing flags.
- Prefer synchronous implementation patterns unless the codebase clearly uses async in that area.
- Keep tickets functional and PR-sized; avoid enum-only or entity-only stories unless they are subtasks.
