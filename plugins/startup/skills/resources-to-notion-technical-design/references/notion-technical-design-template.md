# Notion Technical Design Template

Use this reference when creating the final Notion page. Adapt headings to the user's template if one is provided, but preserve the substance of the sections below.

## Top Section

Start every technical design with a short **Read First** section:

- Recommendation: one paragraph naming the chosen approach and why.
- Status: Draft, In Review, Approved, Implementing, Superseded, or Deprecated.
- Confidence: High, Medium, or Low.
- Top risks: 3 to 5 bullets.
- Next decision: the most important unresolved choice.
- Links: PRD, source resources, related Jira epic, diagrams, code references, Terraform/IaC references, and external docs.

## Metadata

Include:

- Title.
- Date.
- Preparer.
- Owners and reviewers when known.
- Product or system area.
- Request mode: new feature, enhancement, refactor, integration, migration, reliability, data, AI, security, or incident follow-up.
- Target release or phase when known.
- Notion location.
- Source links.

## 1. Executive Summary

Explain what will be built, why now, which option is recommended, expected user/business value, main implementation boundaries, and the confidence level.

## 2. Context And Goals

Include:

- Product/user problem and business objective.
- Current system behavior.
- Functional goals.
- Non-functional goals.
- Non-goals.
- Success metrics and operational targets.
- Constraints from PRD, stakeholders, codebase, infrastructure, cloud provider, Terraform/IaC, compliance, vendors, cost, latency, staffing, or release timing.

## 3. Source Ledger

| Source | Type | Date | Key Claims | Confidence | Conflicts Or Gaps |
| --- | --- | --- | --- | --- | --- |

Confidence values: validated fact, sourced claim, inference, assumption, or open question.

## 4. Existing System Analysis

Document codebase evidence:

- Relevant modules, services, routes, jobs, schemas, migrations, clients, prompts, UI surfaces, tests, and config.
- Existing patterns to reuse.
- Existing cloud, Terraform/IaC modules, deployment pipelines, environment config, IAM, secrets, alarms, dashboards, and operational tooling when infra may change.
- Current limitations and failure modes.
- Code/doc mismatches.
- Ownership boundaries and likely files to touch.

Use file paths, class/function names, or command names where useful.

## 5. Requirements And Constraints

### Functional Requirements

| ID | Priority | Requirement | Source/Confidence | Acceptance Signal |
| --- | --- | --- | --- | --- |

### Non-Functional Requirements

| ID | Category | Target | Rationale | Validation |
| --- | --- | --- | --- | --- |

Categories may include reliability, latency, throughput, scale, security, privacy, compliance, accessibility, operability, maintainability, cost, data quality, and supportability.

## 6. Options Considered

| Option | Summary | Pros | Cons | Risks | Effort | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |

Include at least:

- Conservative repo-native option.
- More scalable or modular option.
- Minimal or phased option when useful.

Also include "do nothing" or "defer" when it is a real product/engineering alternative.

## 7. Decision Record

Use ADR-style entries for major decisions:

| Decision | Chosen Approach | Rationale | Alternatives Rejected | Consequences | Revisit Trigger |
| --- | --- | --- | --- | --- | --- |

## 8. Enterprise Dependency And Infrastructure Plan

### Dependency Decisions

| Capability | Recommended Service/Library | Why Enterprise-Ready | Alternatives Rejected | Security/Ops Notes |
| --- | --- | --- | --- | --- |

Prefer repo-native and cloud-native services when they fit the existing enterprise platform. For AWS-backed systems, evaluate direct AWS services before wrapper SaaS. Example: for email, compare AWS SES plus SNS/SQS/EventBridge, IAM, DKIM/SPF/DMARC, suppression handling, CloudWatch, and Terraform against wrappers such as Resend.

### Infrastructure Plan

| Infra Area | Terraform/IaC Change | Environment Impact | Owner | Validation |
| --- | --- | --- | --- | --- |

Cover modules/resources, variables, outputs, providers, remote state, IAM, KMS/secrets, DNS, networking, queues/topics, buckets, alarms, dashboards, tags, deployment pipeline changes, plan/apply workflow, rollback, drift detection, and secret rotation when relevant.

## 9. Target Architecture

Cover the relevant design:

- Component/module boundaries.
- Dependency direction.
- Domain model and service ownership.
- API, RPC, or event contracts.
- Data model, migrations, indexes, retention, lineage, and ownership.
- UI state and interaction contracts when applicable.
- Background jobs, queues, schedulers, and workflows.
- External systems, vendors, scopes, auth, webhooks, limits, and sandbox behavior.
- AI prompts, models, tools, evals, guardrails, and human review when applicable.

Add diagrams when useful. Use text diagrams if visual tooling is unavailable.

## 10. Failure Handling And Reliability

Define:

- Failure taxonomy.
- Retryable and non-retryable errors.
- Timeouts, backoff, circuit breakers, rate limits, and quotas.
- Idempotency, deduplication, concurrency, and ordering.
- Partial success behavior.
- Fallbacks and degraded modes.
- User-facing recovery and operator-facing diagnostics.
- Dead-letter, replay, reconciliation, and repair flows when relevant.

## 11. Observability And Operations

Specify:

- Logs that answer concrete diagnostic questions.
- Metrics and dimensions.
- Traces and correlation IDs.
- Audit events.
- Dashboards.
- Alerts and thresholds.
- SLOs or launch health checks.
- Redaction and sampling rules.
- Runbooks, support tooling, admin controls, and escalation paths.

Avoid generic "add logging" language. State the operational question each important signal answers.

## 12. Security, Privacy, And Compliance

Include:

- Authn/authz model.
- Permission checks and tenant boundaries.
- Least-privilege scopes.
- Secret handling.
- PII and sensitive data handling.
- Encryption and data retention.
- Auditability.
- Abuse cases and threat model.
- Compliance obligations and required approvals.

## 13. Rollout, Migration, And Rollback

Define:

- Feature flags and rollout gates.
- Environment strategy.
- Migration and backfill steps.
- Compatibility and versioning.
- Monitoring checkpoints.
- Rollback plan.
- Data repair plan.
- Customer, support, or documentation readiness.

## 14. Test And Validation Plan

Cover:

- Unit tests.
- Integration tests.
- Contract tests.
- End-to-end tests.
- Migration tests.
- Regression tests.
- Failure-mode tests.
- Load/performance tests.
- Security/privacy tests.
- Terraform/IaC validation such as format, validate, plan review, policy checks, sandbox deployment, and drift checks when infra changes are included.
- Accessibility tests when UI is involved.
- AI evals, golden sets, adversarial tests, and human review when AI is involved.
- Manual validation or sandbox evidence for external integrations.

## 15. Delivery Plan

Include:

| Workstream | Scope | Dependencies | Parallelizable With | Owner Suggestion | Notes |
| --- | --- | --- | --- | --- | --- |

Also include:

- Suggested story boundaries.
- Hard dependencies.
- Soft dependencies.
- Conflict sets.
- Same-owner bundles.
- Handoff contracts.
- Spikes needed before build work.

## 16. Risks, Assumptions, And Open Questions

### Risks

| Risk | Impact | Likelihood | Mitigation | Owner |
| --- | --- | --- | --- | --- |

### Assumptions

| Assumption | Confidence | Impact If Wrong | Validation Path | Owner |
| --- | --- | --- | --- | --- |

### Open Questions

| Question | Impact | Recommended Default | Owner | Deadline |
| --- | --- | --- | --- | --- |

## 17. Appendices

Use appendices for detailed API examples, schema drafts, source excerpts, benchmark data, vendor notes, threat-model details, or rejected ideas that would distract from the main design.
