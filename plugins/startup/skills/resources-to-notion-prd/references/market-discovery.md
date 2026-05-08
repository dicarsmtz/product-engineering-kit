# Market And Feature Discovery

Use this reference when the user has weak domain knowledge, provides an ambiguous idea, asks what features would be useful, or asks how to enhance an existing feature.

## Discovery Questions To Answer Internally

- What market category does this fit into?
- Who is the buyer, economic customer, daily user, admin, operator, and support owner?
- What urgent job-to-be-done creates willingness to adopt or pay?
- What workflow exists today, and where does it break?
- What alternatives do users already use, including spreadsheets, manual work, agencies, internal tools, and competitors?
- Which direct competitors, adjacent products, platform-native features, open-source tools, or cross-market analogs would users compare against?
- What table-stakes capabilities would users expect in this market?
- What competitor capabilities are only parity, and which gaps create real differentiation?
- What could differentiate the product in a credible first version and create better value than doing nothing or buying an alternative?
- What pricing, packaging, onboarding, procurement, or switching-cost signals shape perceived value?
- What data, integrations, permissions, or compliance rules shape the solution?
- What would make the feature fail after launch: low adoption, missing data, support burden, trust risk, latency, cost, poor fit, or unclear ownership?

## Competitive And Similar-Solution Scan

Build a scan broad enough to avoid tunnel vision:

- Direct competitors in the same category and segment.
- Adjacent workflow tools that may already own part of the user journey.
- Similar solutions in other markets whose patterns could transfer.
- Manual substitutes: spreadsheets, email, chat, documents, agencies, consultants, or internal tools.
- Platform-native alternatives inside products the user already uses.
- Open-source or self-hosted alternatives only when buyers/users would evaluate them as product alternatives; do not inspect code.

For each meaningful alternative, capture:

- Target segment and core promise.
- Table-stakes features users likely expect.
- Strengths worth learning from.
- Gaps, complaints, constraints, or adoption friction.
- Pricing, packaging, onboarding, procurement, or switching-cost signal.
- Evidence quality: primary source, customer evidence, review signal, market inference, or assumption.

Use this table when the PRD needs competitive evidence:

| Alternative | Type | Target Segment | Core Promise | Table-Stakes Features | Strengths | Gaps Or Limits | Pricing/Packaging Signal | Differentiation Opportunity | Evidence/Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Convert the scan into product decisions:

- Keep parity features only when they unlock adoption, trust, procurement, or workflow completeness.
- Prioritize the smallest wedge where the product can be meaningfully better for the target segment.
- Prefer value claims tied to a workflow, metric, risk reduction, cost reduction, speed, trust, or switching pain.
- Add validation tasks for competitor claims that came from weak or unavailable research.

## Feature Opportunity Inputs

Generate candidate features from:

- User lifecycle: discover, onboard, configure, perform core work, collaborate, review, recover, report, renew.
- Workflow stages: intake, triage, planning, execution, approval, audit, analytics, support.
- Pain categories: speed, accuracy, visibility, compliance, coordination, trust, cost, manual effort, missing context.
- Product surfaces: dashboard, list/detail views, notifications, admin settings, exports, imports, integrations, automation, analytics.
- Operational needs: product observability, permissions, rate-limit expectations, failure recovery, support diagnostics, rollout controls.
- Competitive gaps: missing workflow depth, poor setup, weak integrations, high price, limited permissions, poor reporting, slow support, weak compliance, shallow automation, underserved segment.
- Value wedges: faster time-to-value, lower total cost, higher trust, better data quality, deeper workflow fit, stronger ecosystem integration, clearer analytics, safer automation.

## Prioritization Heuristics

Prefer features that:

- Solve a frequent or painful job for a clearly identifiable user.
- Create measurable business value or reduce material risk.
- Produce better value than credible alternatives for the chosen segment.
- Are feasible with available data and platform constraints.
- Produce learning quickly.
- Fit a narrow MVP without blocking future expansion.
- Avoid high compliance, trust, or operational risk unless that risk is the core value proposition.

Defer features that:

- Depend on unvalidated demand.
- Require large platform changes before any user value is visible.
- Add surface area without a clear workflow.
- Create support or compliance obligations the team cannot operate.
- Are mostly competitor parity without adoption evidence.
- Copy competitor behavior without a clear user-value reason.

## Enhancement Analysis

For an existing feature, structure thinking as:

1. Current workflow and user expectations.
2. Current pain points and failure modes.
3. Desired outcome and measurable improvement.
4. Enhancement options, including UX, workflow, performance, data quality, permissions, automation, analytics, reliability, and support.
5. MVP enhancement and phased rollout.
6. Backwards compatibility, change-management, and regression risk.
7. Instrumentation needed to prove improvement.

## Evidence Labels

Use these labels in PRDs:

- **Validated fact:** confirmed in source material, tools, user-provided evidence, or current product documentation.
- **Sourced claim:** stated by a provided resource but not independently verified.
- **Market inference:** reasoned from market/domain patterns or current research.
- **Product recommendation:** decision made by the skill acting as PM.
- **Assumption:** plausible but unverified.
- **Open question:** answer needed before commitment, launch, or downstream planning.
