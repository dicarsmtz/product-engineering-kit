---
name: jira-from-design
description: Gather context from resources such as PRDs, technical design docs, architecture plans, Notion pages, URLs, local files, prompts, or existing Jira epics; validate claims against the actual current codebase; review risks and corrections; plan dependencies, blockers, parallel lanes, same-owner bundles, enterprise dependency choices, and Terraform/IaC work when infra changes are needed; then create or extend a Jira epic and functional technical stories with rich Markdown descriptions. Use when Codex is asked to turn resources to Jira, resources into Jira work, or a design doc, PRD, technical plan, integration plan, Notion page, or existing Jira into actionable Jira issues, especially for BlueFlame engineering tickets.
---

# Jira From Design / Resources To Jira

## Overview

Turn heterogeneous resources into build-ready Jira work. Act like a delivery lead who can preserve product intent from PRDs, preserve architecture decisions from technical designs, validate both against the current repository, and shape the work into functional stories that real engineers can own.

Do not merely copy sections from a PRD or technical design. Convert product outcomes, technical decisions, assumptions, risks, codebase evidence, and rollout constraints into a coherent Jira epic with sequenced stories, acceptance criteria, dependencies, ownership guidance, and explicit validation gates.

## Workflow

1. **Classify** the request and determine whether to create a new epic, extend an existing epic, draft a plan, or recommend more discovery first.
2. **Clarify** only blocking inputs.
3. **Fetch** every source and maintain a lightweight source ledger.
4. **Normalize** product facts, technical claims, decisions, assumptions, conflicts, gaps, and out-of-scope work.
5. **Validate** claims against the current codebase when a repository is available.
6. **Review** risks, corrections, and evidence quality before ticketing unless the user asked for direct creation only.
7. **Plan** phased, functional stories with dependency and collaboration sequencing.
8. **Create or extend** the Jira epic and child stories.

Always treat the codebase validation step as required when a repository is available. Design docs often contain stale file paths, wrong base classes, incorrect config patterns, wrong infrastructure assumptions, or async assumptions that will make tickets misleading. Do not create implementation tickets from documents alone when current repo validation is possible.

When the user provides an existing epic, inspect its description, comments, children, labels, and links before creating or changing anything. Preserve the existing scope and add only missing work; do not duplicate already-ticketed phases.

This skill can run independently from mixed resources, or after `resources-to-notion-prd` and `resources-to-notion-technical-design`. Do not require an upstream PRD or technical design, but preserve their decisions when provided. If the sources are too ambiguous for build-ready Jira stories, create explicit spike stories or recommend a technical design pass before broad implementation ticketing.

## 0. Classify And Clarify

Classify the primary mode and combine modes when needed:

- **New delivery plan:** create a new epic and child stories from resources.
- **Existing epic extension:** add missing stories, comments, links, or acceptance criteria without duplicating existing work.
- **PRD-to-Jira:** preserve product outcomes, users, MVP scope, non-goals, success metrics, edge states, and product risks; do not invent architecture before code/design validation.
- **Technical-design-to-Jira:** preserve recommended architecture, ADR decisions, rejected options, rollout, tests, observability, and infra scope while validating against the repo.
- **Ambiguous resources-to-Jira:** infer a delivery path when feasible, but use spikes or recommend `resources-to-notion-prd` / `resources-to-notion-technical-design` when product or architecture is too uncertain for build-ready tickets.
- **Delivery rescue:** reconcile stale tickets, conflicting docs, or partially implemented work into a corrected epic plan.

Ask the user at most three concise blocker questions, only when a missing answer would cause incorrect Jira writes or materially different work:

- Jira project, destination epic, or permission target is missing and cannot be inferred.
- Product objective, launch phase, user segment, or system boundary has competing interpretations.
- Regulated data, production mutations, money movement, access control, security posture, or compliance obligations are unclear.
- External platform, vendor, dependency, or deployment environment cannot be identified.
- The user asks for direct Jira creation but required Jira metadata or access is unavailable.

When information is missing but not blocking, proceed with a recommended assumption, confidence level, impact if wrong, and validation path. Do not fill Jira issues with `TBD`.

## 1. Fetch

Collect every artifact the user provided:

- Notion URL: use the Notion fetch tool.
- PRD or technical design doc: extract goals, requirements, architecture decisions, options rejected, rollout plan, risks, dependencies, and open questions.
- Web URL: browse/fetch the page and cite the source.
- Local file path: read it directly.
- Jira/Confluence link: use Atlassian tools. For a Jira epic, fetch the epic, comments, linked issues, and child stories with JQL.

Extract scope, architecture layers, phases, dependencies, risks, non-goals, rollout constraints, ownership boundaries, handoff points, and named implementation details such as files, classes, flags, tools, endpoints, and entities.

Maintain a lightweight source ledger while working:

- Source name and link/path.
- Resource type and date accessed or source date when known.
- Key product claims, requirements, architecture decisions, constraints, and open questions.
- Evidence type: validated fact, source claim, inference, assumption, gap, or conflict.
- Product confidence and technical confidence when they differ.
- Conflicts with other sources and the decision used for ticketing.

When PRD and technical design sources disagree, prefer the PRD for product intent, the technical design for implementation decisions, the current codebase for implementation reality, and the user's current brief for active scope. Call out unresolved conflicts before creating tickets.

## 2. Validate Against Code

Check the design against the current repository before writing tickets:

- Applicable repo instructions such as `AGENTS.md`, `CLAUDE.md`, README files, architecture notes, and nested guidance files.
- Do referenced files, folders, classes, commands, entities, and config names exist?
- Which nearby implementation is the best pattern to follow?
- Does the design match sync/async execution in the repo?
- Does auth extend the correct base class?
- Does config follow the real local pattern?
- Are there existing helpers, clients, caches, prompts, workers, or tests to reuse?
- Are there existing enterprise-approved dependencies, cloud services, AWS patterns, Terraform/IaC modules, IAM policies, deployment pipelines, alarms, dashboards, or secrets patterns to reuse?
- Which files/modules are likely to be touched by multiple stories and therefore need owner grouping or serialized work?
- Which requirements are verified product commitments, which are implementation assumptions, and which are fallback triggers that need validation before becoming scope?
- Which existing tests, fixtures, CI commands, mocks, contract tests, or sandbox harnesses should be referenced in acceptance criteria?

When subagents are available and the user has explicitly allowed delegation, use an `explorer` subagent for a focused validation pass. Otherwise validate locally with `rg`, `rg --files`, and targeted file reads.

For BlueFlame repos, specifically verify:

- `ThirdPartyIntegration` and related attributes in `blueflame-common`.
- Command registration and `AbstractCommand`/`MCPCommand` patterns in `blueflame-integrations`.
- OAuth storage in `AccountIntegration`, `AccountSecret`, and `UserIntegration`.
- `bf_defaults` shape before proposing feature flags.
- Existing integrations similar to the requested work, such as Salesforce, DealCloud, O365, FactSet, or existing MCP commands.

For permission-sensitive integrations, validate cache boundaries explicitly. Metadata or schema caches often need account, user, environment, and version/fingerprint inputs; do not assume account-only caching is safe unless the code or platform proves permission equivalence.

For infrastructure or external dependency work, validate the repo's cloud and IaC patterns before ticketing:

- Prefer enterprise-grade repo-native or cloud-native services over convenience wrappers when they fit the architecture. For AWS-backed systems, evaluate direct AWS services before wrapper SaaS such as Resend.
- If new infrastructure is required, create explicit Terraform/IaC tickets or acceptance criteria for modules, resources, variables, outputs, IAM, secrets, alarms, dashboards, DNS/networking, queues/topics, deployment pipeline changes, validation, rollout, and rollback.
- Do not hide Terraform or cloud setup inside an application story when the infra work needs separate ownership, review, apply permissions, or environment promotion.

## 3. Review

Before creating Jira issues, summarize findings for the user unless they asked for direct creation only:

- **Critical issues:** implementation blockers or wrong assumptions.
- **Moderate issues:** unresolved design gaps, scaling limits, unclear ownership, missing permissions, weak failure modes.
- **Minor issues:** polish, naming, ticket-shaping, observability improvements.
- **Strong points:** design choices worth preserving.

Incorporate every correction into the ticket descriptions. Do not create tickets that repeat known-bad assumptions from the design doc.

Keep the review precise about evidence:

- **Validated facts:** confirmed in the repo, docs, sandbox, or existing Jira.
- **Source claims:** stated in PRDs, technical designs, tickets, docs, or vendor pages but not independently verified.
- **Inferences:** reasoned from repo patterns, source material, or architecture constraints.
- **Assumptions:** plausible but unproven choices that need acceptance criteria or spikes.
- **Gaps:** missing facts that require a stakeholder decision, repo investigation, sandbox validation, vendor confirmation, or spike.
- **Fallback triggers:** conditions that justify a narrower alternate implementation later.
- **Out of scope:** related capabilities that should remain in epic notes unless the user explicitly asks for future tickets.

If a PRD is present, verify that the plan preserves:

- Target users, buyers, admins, operators, and support roles.
- MVP scope, non-goals, deferred ideas, and launch gates.
- Key workflows, edge states, permission behavior, analytics, support, and risk requirements.
- Success metrics and product assumptions that downstream engineering should not silently discard.

If a technical design is present, verify that the plan preserves:

- Recommended architecture, alternatives rejected, consequences, and revisit triggers.
- Contracts, data model changes, migrations, API/event shapes, jobs, failure modes, rollout, rollback, and test strategy.
- Security, privacy, observability, operations, external integration, and infrastructure decisions.
- Explicit Terraform/IaC scope and validation when infra changes are needed.

## 4. Plan Stories

Order work by dependency chain:

1. Foundation: auth, shared clients, integration registration, account config.
2. Core infrastructure: Terraform/IaC, IAM/secrets, discovery, schema/config cache, constants, policy layer.
3. Product contracts: stable API/event/DTO shapes, UX or product-surface contracts, analytics events, permission policy, and support workflows.
4. Functional features: user-visible reads, writes, creation, bulk flows, admin/operator flows, and edge states.
5. Integration layer: command routing, prompts, orchestrators, product surfaces, webhooks, background jobs, and external adapters.
6. Validation and rollout: tests, evals, observability, support tooling, docs, runbooks, rollout gates, and rollback.

Prefer 7-12 meaningful stories over many thin tickets. A story should be a functional delivery that can land as a useful PR, even if it includes enums, entities, prompts, tests, and UI/API glue.

Shape tickets by user outcome and production boundary, not by document section. Avoid creating separate thin tickets for every enum, model, helper, or prompt unless the repo or ownership model requires it.

Analyze phase and sequencing explicitly before creating tickets. Every child story Jira summary must start with a bracketed phase prefix, for example `[Phase 0 Foundation]`, `[Phase 1 MVP]`, or `[Phase 2 Rollout]`. Add a sequencing keyword inside the bracket when the story has special timing or dependency behavior:

- `SPIKE` for research/validation that must happen before implementation assumptions can be trusted.
- `SPIKE+BUILD` when the same story validates an integration uncertainty and then implements the adapter if the expected path is not viable.
- `GATED` when work must wait for earlier stories or a feature flag/rollout gate before it can be safely exposed.
- `ENDGAME` for final hardening, observability, sandbox validation, docs, support tooling, or launch-readiness work that should happen near the end.
- `FUTURE` only when the user explicitly asks to create future-scope tickets; otherwise keep future/out-of-scope work in epic notes and do not create child stories for it.

Use the prefix in the Jira summary automatically, not only in the description. Keep the rest of the title concise and functional, for example `[Phase 1 GATED] Dynamics MCP: Wire read-only data into product surfaces`.

Use this sizing guide:

- **XS:** 1-2 hours, config/constants/simple additions.
- **S:** 3-4 hours, one straightforward module.
- **M:** about 1 day, multiple related functions.
- **L:** 2-3 days, complex feature across several files.
- **XL:** 3-5 days; break down if possible.

Use these shaping patterns when they fit the design:

- For uncertain external APIs or MCP/tool integrations, create a capability matrix: primary path, fallback candidate, explicit trigger, and out-of-scope future work.
- Keep one user-facing product boundary when possible. If an implementation may need multiple internal clients or token audiences, ticket that behind one service/integration contract instead of separate product flows.
- Use `SPIKE` stories to classify behavior as supported, unsupported, or unknown with mitigation. Include sandbox evidence, sanitized request/response examples, failure modes, and a decision on whether implementation can stay on the primary path, reduce scope, or needs future fallback work.
- Use `SPIKE+BUILD` only when the likely happy path can be implemented in the same story after validation; do not hide unrelated fallback implementation inside it.
- For writes, creates, deletes, permissions, or other high-risk behavior, sequence work as: read-only foundation, validation spike, gated policy/feature flags, deterministic planning/confirmation, audit and recovery, then operational hardening.
- For launch readiness, add explicit `ENDGAME` work for diagnostics, redaction-safe traces or replay fixtures, alerts/dashboards, golden evals, quotas/rate controls, runbooks, and rollout checklists instead of burying these in feature tickets.
- For infra changes, add explicit Terraform/IaC work with validation and rollout acceptance criteria instead of burying cloud resources inside feature tickets.
- For AI or automation work, include prompt/model ownership, grounding, eval datasets, guardrails, latency/cost budgets, fallback behavior, auditability, and human review when relevant.
- For data or analytics work, include metric definitions, lineage, freshness, permissions, exports, reconciliation, backfills, and alerting when relevant.
- For external integrations, include scopes, token lifecycle, sandbox validation, vendor limits, retries, pagination, idempotency, schema drift, and user-safe fallback behavior.

## Dependency And Collaboration Planning

Before creating issues, build a lightweight dependency graph and collaboration plan from the validated code paths:

- **Hard dependencies:** stories that cannot start until another story lands, such as auth before commands, schema before reads, or persisted model changes before UI/product wiring.
- **Soft dependencies:** stories that can start from agreed interfaces or mocks but need a short integration checkpoint before merge.
- **Parallel lanes:** stories with disjoint files, ownership boundaries, and acceptance criteria that can be assigned to different people at the same time.
- **Conflict sets:** stories that touch the same files, migrations, prompts, config, routing, or shared tests; recommend same-owner sequencing or explicit merge order.
- **Same-owner bundles:** tickets that should go to the same person because they share context, require tight back-and-forth, or would otherwise create avoidable review churn. Same-owner bundles are not counted as parallel capacity unless the work is explicitly staged.
- **Handoff points:** contracts, fixtures, feature flags, or API shapes that must be agreed before another lane can proceed safely.
- **Infra lanes:** Terraform/IaC, IAM, secrets, alarms, dashboards, DNS/networking, and deployment changes that may need separate ownership or apply permissions.

For each story, include these coordination fields in the description:

- **Depends on:** exact story titles or "None".
- **Blocks:** downstream stories delayed by this story.
- **Can run in parallel with:** story titles that are safe to work at the same time.
- **Avoid concurrent edits with:** story titles that touch overlapping files or contracts.
- **Suggested ownership:** same owner as Story X, separate owner from Story Y, or any owner.
- **Merge/review order:** when sequencing matters to avoid conflicts or broken intermediate states.

Prefer plans that minimize cross-branch conflicts and back-and-forth:

- Keep one person on a cluster when tickets share the same core files, migration, command registration, prompt surface, or test fixtures.
- Split across people only when the stories have clear contracts and low overlap.
- Create a spike or contract-setting foundation story before parallel implementation when the integration shape is uncertain.
- Use handoff points for concrete contracts: normalized endpoint resolver, token/scope model, schema DTO, write-plan shape, failure taxonomy, metric names, fixture format, or rollout gate.
- Mark truly blocked stories as `GATED`; do not present them as parallel-ready.
- Add Jira issue links for hard dependencies after creating issues, using the available `Blocks` link type when present.

## 5. Create Jira Issues

First discover Jira configuration:

1. Get accessible Atlassian resources and choose the correct `cloudId`.
2. Get visible Jira projects and confirm the project key, usually `BFAI` for BlueFlame.
3. Get issue type metadata and required fields for both Epic and Story.

Always check required fields. They vary by project and issue type.

Use rich Markdown in the `description` field. For BlueFlame `BFAI` stories, Acceptance Criteria usually must also be sent to `customfield_10132` as Atlassian Document Format (ADF), not plain text. Use `scripts/adf_acceptance.py` to convert bullet criteria into an ADF JSON object.

After creating stories, use `getIssueLinkTypes` and `createIssueLink` to link hard blockers when the project exposes a suitable dependency link type, usually `Blocks`.

Read `references/jira-fields.md` for the BlueFlame field IDs, Jira templates, and story creation pattern.

When extending an existing epic, add a concise epic comment with validation notes, newly added stories, and anything deliberately kept future/out of scope.

## Epic Requirements

The epic description must include:

- Overview.
- Business value.
- Product intent summary: users, MVP outcome, non-goals, success signals, launch gates, and source confidence.
- Explicit PRD/design coverage decision when source docs disagree or exceed the proposed phase.
- Capability mapping: primary implementation path, fallback candidates, and explicit out-of-scope capabilities.
- Enterprise dependency decision: repo-native or cloud-native services considered, wrappers rejected or justified, and operational/compliance rationale.
- Technical architecture.
- Technical scope.
- Terraform/IaC and infrastructure scope when resources, IAM, alarms, dashboards, secrets, DNS/networking, queues/topics, or deployment pipelines are affected.
- Auth/product boundary decisions, especially when one user-facing connection hides multiple internal mechanisms.
- Validated codebase findings that materially changed the plan.
- Out of scope.
- Key risks and mitigations.
- Dependency graph and parallelization plan.
- Suggested owner lanes or same-owner bundles.
- Source ledger summary and evidence classes used for ticketing.
- Design reference links.
- Stories breakdown by phase.

Add consistent labels, for example `connections` and a short feature label.

## Story Requirements

Each story description must include:

- Story type, phase, and effort.
- Jira summary/title with the phase prefix and any required sequencing keyword.
- Product outcome and user/operator value.
- Description and implementation approach.
- Files to create or modify, after codebase validation.
- Terraform/IaC resources, modules, variables, outputs, IAM policies, secrets, alarms, dashboards, or deployment pipeline changes when applicable.
- Validated codebase context for risky or architecture-setting stories.
- Source evidence: PRD requirement IDs, technical requirement IDs, design decisions, repo facts, assumptions, and gaps.
- Dependencies on earlier stories.
- Blocks, parallel-safe stories, avoid-concurrent stories, suggested ownership, and merge/review order.
- Acceptance criteria in the description for readability.
- Test and validation expectations: unit, integration, contract, migration, e2e, sandbox, load, security, accessibility, or AI evals when relevant.
- Observability and support expectations when the story changes production behavior.
- Technical notes, risks, and non-obvious local patterns.

The canonical acceptance criteria must be populated in the Jira Acceptance Criteria custom field when required by the project.

Acceptance criteria must be concrete and verifiable. Include happy path, edge or permission cases, failure behavior, tests, rollout/rollback signals, and negative scope where unsafe behavior must not happen. Reference stable requirement IDs from the PRD or technical design when available.

For spike stories, acceptance criteria must force a decision output, not only research activity: state the validated behavior, classify unsupported/unknown semantics, document user-safe failure handling, and recommend primary-path, reduced-scope, or future-fallback next steps.

For high-risk integration stories, include negative scope and safety language: no second auth UX unless approved, no production mutation flag until gated, no direct API fallback unless a trigger is proven, no sensitive payloads in diagnostics, and no future capability hidden inside the current phase.

## Finish

Before finishing, verify:

- Corrections from codebase validation are reflected in stories.
- Epic exists and links to the design doc.
- Stories are children of the epic.
- Hard dependencies are captured in descriptions and Jira issue links when link types are available.
- Parallel lanes, conflict sets, and same-owner bundles are summarized for the user.
- Existing epic comments are updated when work was added to an existing epic.
- Product Area, Testing Needed, Acceptance Criteria, and labels are set where required.
- Total effort estimate is summarized.
- The user gets a concise table of all created Jira keys and titles.

Perform a final self-review as product manager, architect, delivery lead, QA lead, SRE, security reviewer, and support lead:

- Would an engineer know what modules, contracts, data changes, infra changes, and tests to build?
- Would QA know how to validate behavior, edge cases, regressions, migrations, and failure modes?
- Would SRE/support know what can fail, how to detect it, and how to recover?
- Would security/privacy reviewers know what data, permissions, secrets, audit trails, and abuse cases matter?
- Are product assumptions, technical assumptions, source claims, repo-validated facts, and gaps explicit enough to prevent false certainty?
- Is the critical path, parallelization plan, conflict set, and same-owner grouping realistic?
