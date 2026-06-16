---
name: resources-to-notion-technical-design
description: Create or update Notion technical design documents from mixed resources such as PRDs, prompts, Notion/Jira/Confluence pages, architecture docs, local files, URLs, screenshots, transcripts, raw notes, external docs, and mandatory codebase analysis when a repository is available. Use when Codex must act as a senior/staff engineer or architect to synthesize resources, inspect the current repository, compare implementation options, choose enterprise-grade dependencies and infrastructure, record RFC/ADR-style decisions, include Terraform/IaC plans when infra changes are needed, and publish an implementation-ready production design in Notion for later engineering work or Jira planning.
---

# Resources To Notion Technical Design

## Overview

Create a production-grade technical design document in Notion from heterogeneous resources and repository evidence. The document should read like a practical RFC plus ADR: it explains the problem, compares credible options, chooses a recommended architecture, records decisions and tradeoffs, and gives engineering enough detail to implement safely.

Assume the team may not have a staff engineer, architect, SRE, security reviewer, or domain expert available to turn ambiguous inputs into implementation direction. Do not merely organize the user's input. Convert vague intent, PRDs, tickets, docs, and codebase evidence into a defensible production design with explicit assumptions, recommended decisions, and validation paths.

Do not stop at an outline unless the user explicitly asks for one. Publish the actual Notion document.

## Workflow

1. **Classify** the request type and combine modes when needed.
2. **Clarify** only blocking inputs.
3. **Fetch** every provided resource.
4. **Normalize** source facts, product decisions, technical claims, assumptions, conflicts, and gaps.
5. **Analyze** the current codebase before choosing architecture, dependencies, story boundaries, or infrastructure.
6. **Discover** the technical domain, production environment, constraints, and integration behavior when knowledge is weak or missing.
7. **Research** external systems, platform limits, legal/compliance constraints, enterprise-grade services, libraries, vendor APIs, and cloud-native alternatives when they materially affect the design.
8. **Frame** goals, non-goals, functional requirements, non-functional requirements, and enterprise constraints.
9. **Generate** credible implementation options, including a conservative repo-native option.
10. **Compare** options by correctness, maintainability, modularity, risk, delivery cost, operations, security, performance, and future extensibility.
11. **Decide** the recommended approach and record ADR-style decision rationale.
12. **Design** implementation details: boundaries, contracts, data model, APIs, jobs, state transitions, failure modes, rollout, migration, and tests.
13. **Draft** the technical design with traceable requirements, decisions, and codebase evidence.
14. **Publish** the technical design document to Notion.
15. **Report** the Notion location, recommended approach, critical tradeoffs, open questions, and suggested next step, such as Jira planning.

Do not implement application code, infrastructure, migrations, or tests while using this skill unless the user explicitly asks for implementation after the design work.

## 0. Classify

Identify the primary mode and combine modes when needed:

- **New system or service:** define ownership, boundaries, data flow, contracts, infrastructure, operations, and rollout.
- **Feature implementation:** translate PRD/user goals into repo-aligned architecture, contracts, data changes, failure behavior, and tests.
- **Feature enhancement:** analyze current behavior, compatibility, regressions, rollout, migration, and incremental delivery.
- **Refactor or modularization:** preserve behavior while improving boundaries, dependency direction, testability, and migration safety.
- **External integration:** cover auth, scopes, token lifecycle, webhooks, pagination, rate limits, retries, idempotency, sandbox validation, and vendor drift.
- **Migration or data change:** cover schema/data ownership, backfills, consistency, compatibility, rollback, verification, and operational readiness.
- **Reliability or incident-driven redesign:** start from failure modes, blast radius, SLOs, observability, runbooks, rollout gates, and recovery.
- **AI or automation:** cover model/prompt ownership, grounding, evals, guardrails, human review, latency/cost budgets, retention, and abuse prevention.
- **Data or analytics:** cover definitions, lineage, freshness, reconciliation, permissions, exports, data quality, and alerting.
- **Security, privacy, or compliance:** cover threat model, least privilege, auditability, retention, approvals, tenant boundaries, and evidence capture.

For vague prompts such as "build the backend", "add AI", "integrate X", "make reporting production-ready", or "improve reliability", proceed through repository discovery and make recommended architecture decisions instead of asking the user to become the architect.

## Clarify

Infer reasonable defaults from the resources and workspace. Ask the user only when a missing answer would materially change the design or risk writing to the wrong Notion location. Ask at most three concise blocker questions at the start.

Blocking questions are limited to:

- Target Notion parent page, existing page, database, or workspace location is missing and cannot be inferred.
- The product goal, user segment, system boundary, or source of truth is ambiguous and competing interpretations would produce different architecture.
- The design involves regulated data, production mutations, money movement, access control, security posture, or compliance obligations that are unclear.
- The requested external platform, vendor, library, or deployment environment cannot be identified.
- Notion write access is unavailable or the destination is ambiguous.

Always treat Notion as the destination. If the user provides a non-Notion destination, treat it as a source or export preference unless they explicitly override this skill's normal behavior.

When information is missing but not blocking, proceed with a recommended assumption, confidence level, impact if wrong, and validation path. Do not fill the design with `TBD`.

## Fetch Resources

Collect all material the user provided:

- **Notion pages or target locations:** use Notion tools when available. If tools are not loaded and tool discovery is available, search for Notion tools first.
- **PRDs or product docs:** extract goals, users, requirements, non-goals, metrics, rollout, and unresolved product decisions.
- **Jira or Confluence:** use Atlassian tools when available. Treat issues as source evidence unless the user asks to update Jira.
- **URLs:** browse or fetch the page, especially for current vendor docs, API limits, pricing, security, legal, and platform behavior.
- **Local files:** read directly, including architecture docs, README files, schemas, tests, diagrams, screenshots, prompts, transcripts, and logs.
- **Raw text or prompts:** extract explicit requirements, implied constraints, assumptions, and ambiguity.
- **Repository context:** inspect the current codebase whenever a repo is available.

Maintain a source ledger with:

- Source name and link/path.
- Resource type.
- Date accessed or source date when known.
- Key claims and decisions.
- Product constraint, platform limit, vendor behavior, dependency, infrastructure, security, or operational evidence when relevant.
- Confidence: validated fact, sourced claim, inference, assumption, or open question.
- Conflicts with other resources.

Do not invent source-backed facts. Label inferences explicitly.

## Codebase Analysis

Treat codebase analysis as required when a repository is available. This is not optional for repo-backed requests: do not design only from a PRD, prompt, or external doc. Use `rg`, `rg --files`, package manifests, tests, config, migrations, and targeted file reads.

Validate:

- Repo instructions and local engineering rules such as `AGENTS.md`, `CLAUDE.md`, README files, architecture notes, and nested guidance files that apply to the touched areas.
- Existing architecture, modules, layers, domain boundaries, service/client patterns, dependency direction, and naming.
- Relevant entities, migrations, data ownership, retention, indexes, transactions, and backfills.
- API routes, GraphQL schemas, RPC boundaries, contracts, DTOs, validation, auth, and permissions.
- Background jobs, event buses, queues, schedulers, retries, idempotency, and dead-letter handling.
- Existing logging, metrics, tracing, error handling, alerting, runbooks, feature flags, and rollout gates.
- Security, privacy, secrets, tenant isolation, audit logs, rate limits, and abuse controls.
- Infrastructure-as-code, Terraform modules, environment layout, IAM, secrets, DNS, alarms, dashboards, tags, remote state, and deployment pipelines when infra may change.
- Nearby tests, fixtures, mocks, integration harnesses, contract tests, and CI commands.
- Existing implementations that should be reused instead of inventing a new abstraction.

The design must separate:

- **Repo-validated facts:** confirmed in code or tests.
- **Source claims:** stated in docs or tickets but not yet validated.
- **Inferences:** reasoned from patterns.
- **Assumptions:** plausible but unproven decisions.
- **Gaps:** unknowns that require spikes, stakeholder decisions, or vendor validation.

If the codebase contradicts a resource, prefer the code for implementation reality and call out the discrepancy.

## Technical And Domain Framing

Think like the senior/staff engineer or architect for the specified product domain. If a PRD exists, preserve its product intent while translating it into implementation constraints and technical requirements. If product intent is unclear enough that architecture would be speculative, use `resources-to-notion-prd` first or ask only the blocking product question.

Define:

- Product/user goal, business objective, and target launch phase.
- System boundary, owning team, upstream/downstream dependencies, and source of truth.
- Current workflow and current system behavior.
- Technical thesis: why this architecture is the best current implementation path.
- Enterprise constraints: cloud provider, deployment model, Terraform/IaC, security, compliance, cost, latency, operational maturity, staffing, and release timing.
- Compatibility constraints: API versions, data migration windows, backwards compatibility, tenant isolation, support workflows, and rollback expectations.
- Confidence level, impact if wrong, and validation path for major assumptions.

Use the domain lens to add technical design details teams often miss:

- **B2B SaaS or internal operations:** account/tenant boundaries, roles, approvals, audit logs, admin controls, SLAs, support tooling, integrations, and change management.
- **Consumer products:** abuse controls, privacy, accessibility, notifications, offline/error states, experimentation, and rollout safety.
- **AI or automation:** model/prompt ownership, grounding, eval datasets, confidence thresholds, guardrails, human review, fallback behavior, latency/cost budgets, retention, and abuse prevention.
- **Platform products:** product contracts, versioning, compatibility, rate limits, sandbox needs, developer documentation, observability, and deprecation policy.
- **Marketplaces:** matching/ranking integrity, fraud controls, payments/disputes, incentive abuse, reconciliation, and operational tooling.
- **Regulated domains:** consent, least privilege, auditability, data residency, retention, evidence capture, approvals, and compliance review.
- **Data and analytics products:** metric definitions, lineage, freshness, reconciliation, access control, exports, confidence, backfills, and alerting.

## Technical Discovery And Benchmarking

Run technical discovery whenever the implementation depends on unfamiliar systems, vendor behavior, platform limits, compliance posture, enterprise dependency choices, or ambiguous architecture. Do not limit evaluation to the user's first suggested dependency.

Compare relevant alternatives:

- **Repo-native implementation:** reuse existing modules, services, jobs, clients, and infrastructure patterns.
- **Cloud-native managed services:** especially when the repo or organization already uses that cloud provider.
- **Enterprise SaaS or vendor APIs:** evaluate only when they create clear product, compliance, delivery, support, or operational value.
- **Open-source or self-hosted dependencies:** include only when they are realistic for this repo's runtime, security posture, operations, and team capacity.
- **Manual, temporary, or phased alternatives:** include when they reduce delivery risk or validate assumptions before deeper investment.

Translate findings into design decisions:

- Mark platform or dependency parity as required only when it is necessary for correctness, compliance, operational support, procurement, or workflow completeness.
- Prefer the smallest production-safe design that proves the product value and preserves a path to scale.
- Avoid choosing a wrapper or new abstraction merely because it is convenient.
- Add validation tasks for low-confidence vendor claims, limits, pricing signals, compliance evidence, or operational behavior.

If current research access is unavailable, provide a model-informed alternative map, clearly label it as assumptions, and include the exact validation searches or primary sources to check later.

## Design Quality Bar

The best technical design documents are decision instruments, not documentation theater. They make the safest high-leverage implementation obvious, while preserving enough context for future engineers to understand why alternatives were rejected.

A strong design:

- Starts from product/user goals and maps them to technical requirements.
- Is grounded in the actual codebase and production environment.
- Reuses local patterns unless a new pattern clearly reduces complexity or risk.
- Treats dependency and service selection as architecture, preferring production-grade enterprise dependencies that fit the existing cloud, security, observability, and deployment model.
- Defines crisp module boundaries, ownership, contracts, and dependency direction.
- Keeps concerns separated: domain logic, transport, persistence, orchestration, policy, UI, observability, and vendor adapters.
- Compares real options, including the cost of doing nothing or deferring.
- Records decisions with rationale, alternatives, consequences, and revisit triggers.
- Designs failure behavior intentionally: validation, typed errors, user-safe messaging, retries, timeouts, idempotency, rollback, and partial success.
- Specifies observability that answers operational questions, not noisy logs.
- Handles security, privacy, permissions, compliance, auditability, and abuse cases.
- Plans migration, rollout, feature flags, compatibility, and rollback.
- Defines test strategy across unit, integration, contract, e2e, load/performance, security, and AI evals where relevant.
- Makes dependencies, sequencing, ownership, and risks visible enough for Jira planning.

## Synthesize Technical Scope

Turn the resources and repository evidence into a coherent technical plan:

- Define the technical thesis: why this design should exist now and why this approach is the safest high-value path.
- Separate product goals, technical requirements, non-goals, constraints, assumptions, risks, future ideas, and open questions.
- Resolve conflicts explicitly. Prefer current code for implementation reality, newer authoritative docs for product intent, and the user's current brief for active decisions; label unresolved disagreements.
- Convert vague feature requests into implementation boundaries, contracts, data changes, failure handling, operational behavior, rollout, and testable acceptance signals.
- Select a recommended implementation option when resources contain several plausible directions. Explain the decision and defer weaker options.
- Preserve product intent while removing unsupported implementation speculation from PRDs, tickets, or stakeholder notes.
- Keep future architecture visible without letting it blur MVP or first-phase implementation commitments.

When updating an existing Notion technical design, treat the page as a **single current source of truth**:

- Integrate improvements into the relevant existing sections.
- Replace or rewrite stale/conflicting sections so the document reads as one coherent current design.
- Do not append "improvement pass", "revision", "delta", "current correction", "v2", or version-log sections unless the user explicitly asks for a changelog.
- Do not preserve old wording merely to avoid changing a prior decision. If the current architecture decision has changed, update the canonical section directly and capture uncertainty in assumptions or open questions.
- Keep work notes, rationale for edits, and version history in the final response, not inside the canonical technical design.

When the prompt is ambiguous, make the design explicitly assumption-driven:

- **Recommended decision:** the choice the team should use unless new evidence appears.
- **Confidence:** High, Medium, or Low.
- **Why this is the best current call:** codebase evidence, source evidence, reasoning, and tradeoffs.
- **Validation path:** fastest way to confirm or correct the assumption.
- **Impact if wrong:** technical, product, launch, customer, operations, security, or cost risk.

## Options And Decisions

Generate at least two credible options unless the solution is constrained by an explicit requirement. Prefer three when useful:

- Conservative repo-native implementation.
- More modular or scalable implementation.
- Minimal/temporary implementation or phased variant.

For each option, compare:

- Fit with product goals and requirements.
- Fit with existing architecture and team patterns.
- Modularity and separation of concerns.
- Complexity, delivery effort, and migration burden.
- Reliability, scalability, latency, and cost.
- Security, privacy, compliance, and permissions risk.
- Operational burden, observability, and supportability.
- Testability and maintainability.
- Future extensibility and lock-in.

Choose one recommended option. Record rejected options honestly; do not create strawmen. Include explicit revisit triggers that would justify changing the decision later.

## Enterprise Dependencies And Infrastructure

Prefer enterprise-ready services and dependencies that are durable under production scale, security review, procurement, compliance, observability, support, and incident response. The existing codebase, cloud provider, and infrastructure patterns are the source of truth.

Dependency decisions must cover:

- Why the dependency or service belongs in the architecture.
- Whether it fits the repo's existing stack, language, runtime, deployment, auth, logging, metrics, and testing patterns.
- Security posture, data residency, PII handling, compliance evidence, auditability, SLA, support model, rate limits, quotas, and vendor lock-in.
- Failure modes, retries, timeouts, idempotency, cost controls, alerting, runbooks, and rollback.
- Whether a direct cloud-native implementation is a better enterprise fit than a convenience wrapper.

When the organization already runs on AWS or the repo clearly uses AWS patterns, prefer AWS-native building blocks over wrapper SaaS unless there is a strong product, compliance, delivery, or operational reason not to. For example, for email delivery, evaluate direct AWS SES with IAM, DKIM/SPF/DMARC, bounce and complaint handling through SNS/SQS/EventBridge, suppression handling, CloudWatch metrics/alarms, redaction, and Terraform before recommending a wrapper such as Resend.

If infrastructure is introduced or changed:

- Include Terraform or the repo's existing IaC tool as part of the design. If no IaC pattern exists and AWS is the target, recommend Terraform as the default unless the user or repo establishes another standard.
- Identify Terraform modules, resources, variables, outputs, providers, environments, state, IAM policies, KMS/secrets, tags, alarms, dashboards, DNS, networking, queues, topics, buckets, and deployment pipeline changes.
- Separate application code, infrastructure code, and operational configuration workstreams.
- Include plan/apply ownership, review gates, environment promotion, rollback, drift detection, and secret rotation considerations.
- Add infra-specific tests or validation such as `terraform fmt`, `terraform validate`, plan review, policy checks, and sandbox deployment evidence when applicable.

## Technical Requirement Quality Bar

Write technical requirements so engineering, QA, SRE, security, support, and downstream Jira planning can act on them:

- Use stable IDs such as `FR-001`, `NFR-001`, `API-001`, `DATA-001`, `SEC-001`, `OPS-001`, `OBS-001`, `INFRA-001`, `AI-001`, and `TEST-001`.
- Use precise nouns from the repo and domain.
- Prefer observable behavior, contracts, and validation signals over broad intent.
- Include negative requirements where unsafe behavior must not happen.
- Include permissions, failure states, partial-success behavior, retries, and rollback, not only happy paths.
- Make acceptance signals concrete and verifiable.
- Include source/confidence so downstream planning can preserve or resolve assumptions.
- Avoid "nice to have" language in committed first-phase scope. Move uncertain ideas to future scope or open questions.
- Ensure every non-functional target has an owner, measurement method, expected threshold or direction, and validation approach when inferable.
- Use Must/Should/Could/Won't or P0/P1/P2 consistently.
- Keep future architecture ideas outside committed implementation requirements.

Example requirement row:

| ID | Priority | Phase | Area | Requirement | Acceptance Signal | Source/Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| API-001 | Must | MVP | Booking API | Reservation creation must be idempotent for retried client requests. | Duplicate requests with the same idempotency key return the original reservation result, emit one audit event, and do not create extra rows. | Codebase inference / Medium |

## Production Readiness Checklist

Cover every relevant item in the Notion doc:

- **Contracts:** API shape, request/response schemas, event schemas, validation, versioning, compatibility, and deprecation.
- **Data:** ownership, migrations, backfills, indexes, consistency, retention, lineage, freshness, PII, tenancy, and deletion.
- **Reliability:** timeouts, retries, backoff, circuit breakers, idempotency keys, rate limits, quotas, concurrency, partial failure, and recovery.
- **Errors:** typed failure taxonomy, user-facing behavior, operator-facing diagnostics, retryable vs non-retryable errors, and safe fallbacks.
- **Observability:** metrics, logs, traces, audit events, dashboards, alerts, SLOs, correlation IDs, sampling, and redaction.
- **Security:** authn/authz, least privilege, secret handling, encryption, tenant boundaries, abuse cases, auditability, and threat model.
- **Operations:** feature flags, rollout, rollback, runbooks, support tooling, admin controls, migrations, incident response, and post-launch review.
- **Infrastructure:** Terraform/IaC changes, IAM, networking, secrets, DNS, queues/topics, alarms, dashboards, environment promotion, drift detection, and rollback.
- **Testing:** unit, integration, contract, e2e, migration, regression, load, chaos/failure, security, accessibility, and AI evals where relevant.
- **AI systems:** model/prompt ownership, eval datasets, guardrails, grounding, hallucination/fallback behavior, cost/latency budget, data retention, human review, and abuse prevention.
- **External integrations:** scopes, token lifecycle, webhooks, sandbox validation, vendor limits, retries, pagination, idempotency, schema drift, and fallback behavior.

Logging must provide operational value. Specify what question each important log/metric answers, such as "which tenant is affected?", "which vendor request failed?", "is this retryable?", "did the rollout increase errors?", or "which downstream dependency is slow?" Do not require logs merely to say that a method was entered.

## Notion Document

Read `references/notion-technical-design-template.md` before drafting the final page or when the user asks for a reusable template. Adapt section names to the user's template if provided, but keep the decision quality bar, source ledger, options comparison, production readiness, and validation plan.

Always treat Notion as the destination unless the user explicitly asks for another output. If the user also requests a local draft, create it only as an intermediate artifact and still publish to Notion.

Publish the technical design to Notion:

- Create or update the target Notion page/database when Notion tools are available. If needed, discover Notion tools first.
- If the user provides an existing Notion page, update that page unless they ask for a new child page.
- If the user provides a Notion database, create a database item with a clear design title, status, product/system area, request mode, and confidence when properties are available.
- If the user provides a parent page, create a child page named `Technical Design: <feature or system name>`.
- Preserve hierarchy with Notion headings, tables, callouts, and source links.
- Put a short **Read First** section at the top with recommendation, status, confidence, top risks, next decision, and links.
- Use Notion tables for requirements, source ledger, options comparison, decision records, dependencies, infrastructure plan, risks, assumptions, open questions, validation plan, and delivery workstreams when the tools support them.
- When updating an existing page, rewrite it into a coherent current technical design. Do not append versioned addenda or contradictory correction sections.
- If a parent page or database is ambiguous, ask before writing.

If Notion tools cannot access the requested Notion target, produce the technical design in Markdown as a fallback artifact and clearly state what blocked direct Notion publishing. Do not silently store the canonical design somewhere else.

## Workflow Composition

This skill can run independently from raw resources, or as the middle step in a larger workflow:

- Use `resources-to-notion-prd` first when the product problem, user value, MVP, or requirements are unclear.
- Use this skill when implementation architecture, tradeoffs, risks, and production readiness need to be decided.
- Use `resources-to-jira` after this skill when the team is ready to turn the design into an epic, stories, dependencies, and acceptance criteria.

Do not require an upstream PRD or downstream Jira workflow. If the user provides enough context, produce the technical design directly. If an upstream PRD exists, treat it as product context and a product decision source, but validate implementation claims against the current codebase before treating them as technical reality.

## Finish

Before finishing, verify:

- All provided resources were considered or explicitly marked inaccessible.
- Repository analysis was completed when a repo is available, including applicable local instructions.
- The design distinguishes repo-validated facts, source claims, inferences, assumptions, and gaps.
- The Notion page exists at the intended location.
- Codebase findings and source conflicts are reflected in the recommended design.
- Major decisions include alternatives, rationale, consequences, and revisit triggers.
- Enterprise dependency choices are justified against direct cloud-native or repo-native alternatives.
- Any infra changes include Terraform/IaC scope, ownership, validation, rollout, and rollback.
- Production readiness sections are concrete, not generic.
- Requirements have stable IDs, priorities, acceptance signals, and source/confidence.
- MVP/first phase, future scope, and non-goals are distinct.
- Risks and open questions have owners or validation paths when inferable.
- The Notion document reads as one current source of truth, not as layered revisions or appended correction passes.
- The Notion document is structured enough for Jira planning without re-discovering product intent or current system reality.
- The user receives a concise summary with the Notion link, recommended approach, critical risks, unresolved blockers, and suggested next workflow step.

Perform a final self-review as architect, domain engineer, SRE, security reviewer, QA lead, support lead, and delivery lead:

- Would an engineer know what modules, contracts, data changes, infra changes, and tests to build?
- Would SRE/support know what can fail, how to detect it, and how to recover?
- Would security/privacy reviewers know what data, permissions, secrets, audit trails, and abuse cases matter?
- Would QA know how to validate behavior, edge cases, regressions, migrations, and failure modes?
- Are assumptions explicit enough to prevent false certainty?
- Is the recommended option justified against credible alternatives, including repo-native and cloud-native options?
- Are dependencies, sequencing, ownership, and risks visible enough for Jira planning?

Finish with a concise note containing the Notion technical design location, recommended approach, strongest assumptions, unresolved blockers, and recommended next workflow step.
