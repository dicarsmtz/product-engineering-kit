---
name: resources-to-notion-prd
description: Create or update product-only Notion PRDs from ambiguous user ideas and mixed product resources such as links, Notion pages, Jira/Confluence pages, local docs, screenshots, transcripts, raw text, market context, customer evidence, or business constraints. Use when Codex must act as the product manager/owner to discover the market/domain, investigate competitors and similar solutions, identify useful features, improve an existing feature, choose best-value MVP scope, and publish a single-source-of-truth Notion PRD for design, QA, stakeholder alignment, and later downstream planning.
---

# Resources To Notion PRD

## Overview

Create a complete product PRD in Notion from heterogeneous resources, with product-manager judgment for the specified domain or market. The output should be useful to stakeholders now and structured enough for later design, QA, stakeholder review, and delivery planning without turning the PRD itself into technical work.

Assume the team may not have a product manager, product owner, domain expert, or market expert. Do not merely organize the user's input. Convert vague intent and scattered resources into a defensible product direction, scoped requirements, and a Notion artifact that can drive product, design, QA, launch, stakeholder alignment, and later planning.

**Product-only boundary:** This skill must not inspect local repositories, validate implementation against code, read `AGENTS.md` or `CLAUDE.md`, infer architecture, choose dependencies, design APIs, plan migrations, or create codebase-validated facts. If the user provides code or technical docs as resources, use them only for product implications and business constraints; do not turn the PRD into a technical design.

## Workflow

1. **Classify** the request type: new feature, feature enhancement, market/domain discovery, resource synthesis, or product concept derived from business resources.
2. **Clarify** only blocking inputs.
3. **Fetch** every provided resource.
4. **Normalize** source facts, assumptions, conflicts, and gaps.
5. **Discover** the market/domain, users, workflows, constraints, and feature opportunities when knowledge is weak or missing.
6. **Benchmark** direct competitors, adjacent tools, similar solutions, manual substitutes, and platform-native alternatives to find table-stakes expectations, unmet needs, and credible differentiation.
7. **Frame** the product opportunity through the target domain, market, users, business model, competitive landscape, and best-value positioning.
8. **Shape** scope, requirements, success metrics, UX flows, risks, and delivery phases.
9. **Prioritize** MVP, next phases, deferred ideas, and out-of-scope work.
10. **Draft** the PRD with traceable requirements and explicit decisions.
11. **Publish** the PRD to Notion.
12. **Report** the Notion location, recommended MVP, major assumptions, open questions, and product handoff notes.

Do not stop at a high-level outline unless the user explicitly asks for an outline. Produce the actual PRD.

## 0. Classify

Identify the primary mode and combine modes when needed:

- **New feature or solution:** define the problem, users, scope, requirements, launch plan, and handoff details.
- **Feature enhancement:** analyze current state, target outcome, gaps, options, change management, regressions, and incremental rollout.
- **Market/domain feature discovery:** research the domain, infer user needs, propose useful feature opportunities, prioritize the best concept, then write the PRD for the recommended scope.
- **Resource synthesis:** reconcile many documents into one product direction and PRD.
- **Product concept from business resources:** convert business, market, or stakeholder inputs into user outcomes, product requirements, rollout, and product risks without specifying architecture or implementation.

For vague prompts such as "build reporting", "improve onboarding", "add AI", "make X better", or "what should we build for this market", proceed through discovery and make recommended decisions instead of asking the user to become the product manager.

## 1. Clarify

Infer reasonable defaults from the resources and the workspace. Ask the user only when a missing answer would materially change the PRD or risk writing to the wrong Notion location. Ask at most three concise blocker questions at the start.

Blocker questions are limited to:

- The target Notion parent page, existing page, database, or workspace location is missing and cannot be inferred.
- Target domain, market, or customer segment is ambiguous and competing interpretations change scope.
- The resources conflict on launch phase, user segment, compliance boundary, or business objective.
- Notion write access is unavailable or the target Notion location is ambiguous.
- A hard business constraint is missing, such as launch timing, enterprise readiness, regulated data, legal review, launch geography, pricing boundary, or required channel/platform policy.

Always treat Notion as the destination. If the user provides a non-Notion destination, treat it as a source or export preference unless they explicitly override this skill's normal behavior.

When information is missing but not blocking, proceed with:

- Recommended assumption.
- Confidence: High, Medium, or Low.
- Impact if wrong.
- How to validate later.

Do not fill the PRD with `TBD`. Use a recommended decision plus a validation note unless the item is genuinely blocked.

## 2. Fetch Resources

Collect all material the user provided:

- Notion URL or requested Notion target: use Notion tools when available. If Notion tools are not loaded but tool discovery is available, search for the Notion tools before falling back.
- Jira or Confluence link: use Atlassian tools when available, but use the content as source material rather than a publishing target.
- Web URL: browse or fetch the page, especially for current market, pricing, legal, competitor, similar-solution, or vendor information.
- Local file path: read it directly.
- Raw text, pasted notes, transcripts, screenshots, or images: extract decisions, requirements, evidence, and unresolved questions.

Do **not** inspect repository context for this PRD skill. Do not read local source code, package manifests, tests, implementation docs, or repo instructions merely because a repo exists. If the user explicitly provides a technical file as a resource, extract only product-facing implications such as existing user behavior, business constraints, constraints from a platform policy, or terminology the PRD should use.

Create a lightweight source ledger while working:

- Source name and link/path.
- Resource type.
- Date accessed or document date when known.
- Key claims and decisions.
- Competitor, substitute, pricing, positioning, feature, or value evidence when relevant.
- Confidence: validated fact, sourced claim, inference, assumption, or open question.
- Conflicts with other resources.

Do not invent source-backed facts. When a conclusion is inferred, label it as an inference.

## 3. Product And Market Framing

Think like the product manager or product owner for the specified domain. If the user provides a market, domain, customer segment, buyer, or business model, make that the lens for prioritization. If not, infer it from the resources and state the assumption.

Define:

- Target market and customer segment.
- Primary users, buyers, admins, operators, and support roles.
- Current pain, jobs-to-be-done, alternatives, and switching constraints.
- Business objective: acquisition, activation, retention, monetization, efficiency, risk reduction, expansion, or strategic enablement.
- Market maturity and adoption constraints.
- Competitive landscape, differentiation, and why this solution should exist now.
- Best-value position: what the product should do better, cheaper, faster, safer, simpler, or more completely than alternatives for the target segment.
- Constraints: compliance, privacy, data availability, platform policies, cost, response-time expectations, operational support, change management, or release timing.

Use the domain lens to add product requirements teams often miss:

- **B2B SaaS or internal operations:** roles, permissions, approval workflows, audit logs, admin controls, SLAs, integrations, change management, support workflows.
- **Consumer products:** onboarding, activation, retention loops, trust and safety, privacy, accessibility, notifications, offline/error states, experimentation.
- **AI or automation:** human review, evals, guardrails, behavior ownership, explainability, confidence thresholds, fallback behavior, response-time expectations, usage/cost guardrails, data retention, abuse prevention.
- **Platform products:** roles, permissions, product contracts, docs, version expectations, rate-limit expectations, sandbox needs, backwards compatibility, product observability needs.
- **Marketplaces:** supply-demand liquidity, matching/ranking, incentives, payments, disputes, fraud controls, marketplace integrity.
- **Regulated domains:** consent, auditability, data residency, retention, risk approvals, legal/compliance review, least-privilege access, evidence capture.
- **Data and analytics products:** metric definitions, lineage, freshness, access control, exports, confidence, reconciliation, alerting, explainability.

When market or domain knowledge is weak, discover before writing requirements:

- Market category, target segment, buyer, user, and economic customer.
- Common workflows, jobs-to-be-done, pain points, switching costs, and alternatives.
- Competitors, adjacent tools, similar products, manual workarounds, and platform-native alternatives, including what users likely expect as table-stakes.
- Domain constraints: compliance, privacy, data sensitivity, permissions, data quality, integrations, workflow approvals, seasonality, support burden, and operational risk.
- Common pricing, packaging, procurement, onboarding, and adoption constraints when relevant.
- Product maturity: MVP, wedge feature, parity feature, expansion feature, or operational hardening.

Use current web research for market, competitor, pricing, legal, platform, and vendor claims when tools are available. Prefer primary sources, official docs, product pages, public pricing pages, customer evidence, standards, and regulatory sources. If research access is unavailable, state that market conclusions are model-informed assumptions and include validation tasks.

## 3A. Competitive And Similar-Solution Investigation

Run this investigation whenever the PRD depends on market/domain judgment, the team lacks domain knowledge, the prompt is vague, or the feature must beat or improve on existing solutions. Do not limit research to obvious direct competitors.

Include:

- **Direct competitors:** products solving the same core problem for the same segment.
- **Adjacent tools:** products in nearby workflows that users may already use.
- **Similar solutions in other markets:** patterns from other domains that could transfer.
- **Manual and services substitutes:** spreadsheets, agencies, consultants, internal tools, email, Slack, documents, or offline workflows.
- **Platform-native alternatives:** built-in features from ecosystems the target users already rely on.
- **Open-source or self-hosted alternatives:** include only when the buyer/user would evaluate them as product alternatives; do not inspect their code.

Answer internally:

- What alternatives would the target user compare against during evaluation or procurement?
- Which capabilities are table-stakes and should not be treated as differentiators?
- Where do alternatives appear strong: workflow fit, UX, integrations, compliance, price, trust, speed, automation, reporting, support, or ecosystem?
- Where do alternatives appear weak: setup effort, missing roles/permissions, poor data quality, limited automation, expensive pricing, weak reporting, support gaps, privacy risk, rigidity, or poor fit for this segment?
- What pricing, packaging, onboarding, procurement, and adoption patterns affect perceived value?
- What competitor claims should be verified before product commitment or go-to-market?
- Which value wedge is most defensible for the user's product: lower friction, better workflow depth, better integrations, better trust/compliance, faster time-to-value, lower total cost, better AI/automation, or underserved segment focus?

Create a competitive landscape table when meaningful:

| Alternative | Type | Target Segment | Core Promise | Table-Stakes Features | Strengths | Gaps Or Limits | Pricing/Packaging Signal | Differentiation Opportunity | Evidence/Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Translate the findings into PRD decisions:

- Mark competitor parity as MVP only when it is required for adoption, trust, procurement, or workflow completeness.
- Prefer differentiation that matters to the target segment over adding a broad feature checklist.
- Avoid copying competitors without a user-value reason.
- Identify the smallest MVP wedge that proves better value than alternatives.
- Include "better than alternatives because..." in the executive summary, solution overview, and key decisions.
- Add validation tasks for low-confidence competitor claims, pricing signals, or market gaps.

If current research access is unavailable, still provide a model-informed competitor/substitute map, clearly label it as assumptions, and include the exact validation searches or sources to check later.

## 3B. Feature Discovery And Enhancement Thinking

For "what should we build", "what features would be useful", "how do we improve X", or vague feature ideas, generate product options before choosing scope.

Build a feature opportunity map:

| Opportunity | User/Persona | Pain Solved | Why Now | Business Value | Competitive Gap Or Value Wedge | Evidence | Effort | Risk | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Score or qualitatively rank opportunities using:

- User impact and urgency.
- Strategic fit.
- Differentiation or table-stakes necessity.
- Competitive gap or best-value potential versus alternatives.
- Revenue, retention, activation, efficiency, or risk-reduction potential.
- Feasibility with available data, business constraints, integrations at a product level, and team capacity.
- Risk from privacy, compliance, support, reliability, or user trust.
- Time-to-learning: how fast the team can validate the idea.

Select a recommended MVP and explain why alternatives were deferred.

For enhancement requests, include:

- Current state and current user journey.
- Pain points and failure modes.
- Enhancement goals and non-goals.
- Candidate improvements across UX, workflow, performance, permissions, analytics, automation, reliability, and support.
- Backwards compatibility, adoption, change-management, and rollout risks.
- Regression risks and success metrics.

## 4. Synthesize Scope

Turn the resources into a coherent product plan:

- Define the product thesis: why this feature should exist now.
- Define the value thesis: why the target user should choose this over competitors, substitutes, or doing nothing.
- Identify users, buyers, admins, operators, support roles, and other stakeholders.
- Distinguish problem, solution, workflow, requirements, assumptions, and product constraints.
- Resolve conflicts explicitly. Prefer newer, authoritative, or user-specified sources; label unresolved disagreements.
- Separate goals, non-goals, requirements, constraints, assumptions, risks, and future ideas.
- Define MVP and subsequent phases. Keep future scope visible without letting it blur MVP commitments.
- Convert vague feature requests into user outcomes, workflows, and testable requirements.
- Select a recommended scope when resources contain several plausible directions. Explain the decision and defer weaker options.
- Preserve product intent while removing implementation speculation that is not supported by the resources.
- Keep technical context out of the PRD unless it is a product-facing constraint explicitly provided by the user or source material.
- Do not produce codebase-validated facts, architecture notes, API contracts, implementation dependencies, migrations, feature-flag plans, or engineering validation tasks in this skill.

When updating an existing Notion PRD, treat the page as a **single current source of truth**:

- Integrate improvements into the relevant existing sections.
- Replace or rewrite stale/conflicting sections so the document reads as one coherent current PRD.
- Do not append "improvement pass", "revision", "delta", "current correction", "v2", or version-log sections unless the user explicitly asks for a changelog.
- Do not preserve old wording merely to avoid changing a prior decision. If the current product decision has changed, update the canonical section directly and capture uncertainty in assumptions or open questions.
- Keep work notes, rationale for edits, and version history in the final response, not inside the canonical PRD.

When the prompt is ambiguous, make the PRD explicitly assumption-driven:

- **Recommended decision:** the choice the team should use unless new evidence appears.
- **Confidence:** High, Medium, or Low.
- **Why this is the best current call:** evidence, reasoning, and tradeoffs.
- **Validation path:** fastest way to confirm or correct the assumption.
- **Impact if wrong:** product, technical, launch, customer, or support risk.

## 5. PRD Structure

Use this structure unless the user provides a different template. Keep the original PRD sections below, and enrich them with market discovery, feature opportunity, assumption, and decision content when the input is ambiguous or the domain is unfamiliar.

1. **Title And Metadata**
   - Feature or solution name.
   - Status, date, author/preparer, owners, stakeholders, Notion location, source links.
   - Target domain/market and customer segment.

2. **Executive Summary**
   - What is being built, for whom, why now, expected business/user impact, recommended MVP, and confidence level.

3. **Context And Opportunity**
   - Background, current pain, market/domain forces, customer evidence, existing alternatives, strategic fit.
   - Product thesis: the strategic bet and why this scope is the right first version.
   - Competitive landscape and similar-solution findings: direct competitors, adjacent tools, substitutes, table-stakes expectations, value gaps, and evidence confidence.
   - Value thesis: why the recommended MVP should beat alternatives for the target segment.
   - Source and evidence summary: key source claims, market findings, assumptions, conflicts, and confidence.

4. **Users And Personas**
   - Primary and secondary users.
   - Buyer/admin/operator/support roles when relevant.
   - Jobs-to-be-done and top use cases.

5. **Problem Statement**
   - Clear problem framing.
   - Current workflow and failure modes.
   - Why existing solutions are insufficient.

6. **Goals, Non-Goals, And Success Metrics**
   - Product goals.
   - Business goals.
   - Non-goals and explicit exclusions.
   - North-star and guardrail metrics.
   - Launch, adoption, quality, reliability, and support metrics.

7. **Solution Overview**
   - Proposed capability set.
   - Key user journeys or workflows.
   - Domain-specific behavior.
   - Best-value position and how the solution is meaningfully better than competitors, substitutes, or current manual workflows.
   - Major product decisions and rationale.
   - Feature opportunity map and rationale when multiple useful features or enhancements were considered.

8. **Scope And Phasing**
   - MVP / Phase 0 / Phase 1 / Phase 2 as appropriate.
   - In scope, out of scope, deferred ideas.
   - Dependencies and sequencing.
   - Validation checkpoints for low-confidence assumptions.

9. **Requirements**
   - Use stable IDs such as `FR-001`, `NFR-001`, `DATA-001`, `AN-001`, `OPS-001`, `SEC-001`, `AI-001`, `UX-001`.
   - Include priority, user/persona, requirement, rationale, acceptance criteria, and source/confidence.
   - Make every requirement testable.

10. **UX And Interaction Requirements**
    - Primary flows.
    - Empty, loading, error, permission-denied, partial-success, and recovery states.
    - Notifications, confirmations, accessibility, localization, and responsive behavior when relevant.

11. **Data, Integrations, And Permissions**
    - Product-level data objects, sources, retention expectations, freshness expectations, ownership, permissions, auditability, external systems, and data quality constraints.

12. **Analytics, Experimentation, And Evaluation**
    - Events, funnels, dashboards, experiment plan, AI evals when relevant, operational metrics, and decision thresholds.

13. **Security, Privacy, Compliance, And Risk**
    - Threats, abuse cases, privacy posture, compliance obligations, approvals, operational risks, mitigations, and rollback plan.

14. **Product Handoff Notes**
    - Product constraints and dependencies.
    - Critical user journeys and product decisions downstream teams must preserve.
    - Launch gates, rollout expectations, support readiness, and policy/compliance constraints.
    - Suggested product workstreams by user outcome when useful.
    - Inputs downstream implementation-planning workflows should receive as product context, without specifying architecture or implementation.

15. **Launch And Operations**
    - Rollout plan, beta criteria, enablement, support playbooks, documentation, monitoring, alerting, and post-launch review.

16. **Open Questions And Decisions**
    - Decisions made.
    - Open questions with owner, deadline, and impact if unanswered.
    - Assumptions that downstream planning must preserve or resolve.
    - Recommended decisions for unresolved product choices, with confidence and validation path.

17. **Appendix**
    - Source ledger.
    - Glossary.
    - Research notes, competitive notes, diagrams, or raw artifacts summaries.

## 6. Requirement Quality Bar

Write requirements so product, design, QA, support, and downstream planning can act on them:

- Use precise nouns from the product/domain.
- Prefer observable behavior over broad intent.
- Include negative requirements where unsafe behavior must not happen.
- Include permissions and failure states, not only happy paths.
- Make acceptance criteria concrete and verifiable.
- Include source/confidence so downstream planning can preserve assumptions.
- Avoid "nice to have" language in committed MVP scope. Move uncertain ideas to future scope or open questions.
- Ensure every success metric has an owner, measurement method, and expected direction.
- Include edge states, support/operations needs, analytics, and launch gates when they affect delivery.
- Avoid broad phrases such as "make it easy" unless paired with observable criteria.
- Use Must/Should/Could/Won't or P0/P1/P2 consistently.
- Keep future ideas outside committed MVP requirements.

Example requirement row:

| ID | Priority | Phase | User | Requirement | Acceptance Criteria | Source/Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | Must | MVP | Account admin | Admins can invite teammates by email and assign roles before sending invites. | Invite form validates email, requires one role, sends invitation, records actor and timestamp, and shows recoverable errors. | Customer interview / Medium |

## 7. Notion Publishing

Publish the PRD to Notion:

- Create or update the target Notion page/database when Notion tools are available. If needed, discover Notion tools first.
- If the user provides an existing Notion page, update that page unless they ask for a new child page.
- If the user provides a Notion database, create a database item with a clear feature title, PRD status, domain, and confidence when properties are available.
- If the user provides a parent page, create a child page named `PRD: <feature or solution name>`.
- Preserve hierarchy with Notion headings, tables, callouts, and source links.
- Put a short **Read First** section at the top with executive summary, recommended MVP, confidence, top risks, and next decision.
- Use Notion tables for requirements, competitive landscape, feature opportunity map, assumptions, open questions, decisions, risks, and source ledger when the tools support them.
- When updating an existing page, rewrite it into a coherent current PRD. Do not append versioned addenda or contradictory correction sections.
- If a parent page or database is ambiguous, ask before writing.

If Notion tools cannot access the requested Notion target, produce the PRD in Markdown as a fallback artifact and clearly state what blocked direct Notion publishing. Do not silently store the canonical PRD somewhere else.

## 8. Handoff Readiness

Before finishing, check:

- All provided resources were considered or explicitly marked inaccessible.
- The PRD contains domain/market-specific requirements.
- Market/domain assumptions are explicit when the team lacks domain expertise.
- Competitors, adjacent tools, similar solutions, manual substitutes, and platform-native alternatives were investigated or explicitly marked as unvalidated assumptions.
- The PRD distinguishes table-stakes parity from true differentiation.
- The recommended MVP explains why it provides better value than credible alternatives.
- Useful feature opportunities or enhancement options were considered, not only the user's first phrasing.
- The recommended MVP is justified against alternatives.
- MVP, future scope, and non-goals are distinct.
- Requirements have stable IDs and acceptance criteria.
- Assumptions, decisions, conflicts, and open questions are explicit.
- Product handoff notes are useful and do not contain codebase, architecture, API, migration, or dependency decisions.
- The source ledger supports later review.
- The Notion document reads as one current source of truth, not as layered revisions or appended correction passes.
- The Notion document is structured enough for downstream planning to use as product context without re-discovering product intent.

Perform a final self-review as product manager, domain analyst, designer, QA, and support lead:

- Would a downstream design/delivery team understand the product outcomes and priorities?
- Would a designer know the primary workflows and edge states?
- Would QA know how to test requirements?
- Would support/operators know what changes and what can fail?
- Are assumptions explicit enough to prevent false certainty?
- Does MVP maximize learning and value while minimizing scope risk?
- Are market/domain constraints represented?
- Is the value proposition stronger than direct competitors, substitutes, and doing nothing?

Finish with a concise note containing the Notion PRD location, strongest assumptions, unresolved blockers, and recommended product next step. Mention downstream delivery planning only when the user asks or when it is clearly the next product handoff; keep it out of the PRD body.

## References

Load bundled references only when they materially improve the run:

- `references/market-discovery.md`: use when the domain/market is unfamiliar, the prompt is vague, competitor/similar-solution investigation is needed, the user asks what features would be useful, or an existing feature needs enhancement strategy.
- `references/notion-prd-template.md`: use when drafting the final Notion page structure or when a consistent PRD table set is needed.
