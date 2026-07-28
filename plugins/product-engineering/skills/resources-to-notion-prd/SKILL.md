---
name: resources-to-notion-prd
description: Create concise, actionable, lean Notion PRDs and developer-first micro-tickets from ambiguous ideas, transcripts, links, or notes. Eliminates enterprise bloat, focuses strictly on the MVP core loop, and enforces brevity to prevent decision fatigue.
---

# Resources To Notion PRD (Lean & Developer-First)

## Primary Directive
Act as a pragmatic Staff Product Manager and Lead Engineer. Convert vague user ideas and scattered resources into a concise, high-confidence Notion PRD. 

**STRICT RULE:** Eliminate fluff, enterprise overhead, and multi-page prose. Prioritize scannability, brevity, and actionable developer requirements over exhaustive market documentation.

---

## Workflow & MVP Guardrails

1. **Apply the "Core MVP Filter":** 
   * Defer any feature that does not directly serve the core loop: **[Context Ingestion] $\rightarrow$ [Content Generation + Approval] $\rightarrow$ [Automated API Publishing]**.
   * Move complex ideas (e.g., automated A/B testing, multi-touch attribution, enterprise roles, deep analytics) straight to the `Deferred / V2` table.

2. **Format Constraints:**
   * Maximum **150 words per requirement/ticket**.
   * Use bullet points and markdown tables.
   * NO introductory filler, polite preamble, or fluff.

3. **Fetch & Synthesize:**
   * Read provided text, links, or notes. Extract only user outcomes, workflow constraints, and API inputs.

---

## Streamlined PRD Structure for Notion

Every generated Notion PRD MUST follow this exact 6-section structure:

### 1. Executive Summary & Core Thesis
* **What we are building:** [1-2 sentences max]
* **Target User:** [1 sentence]
* **Value Wedge:** [Why this beats doing it manually in 1 sentence]
* **Confidence Level:** High | Medium | Low

### 2. High-Level User Flow
Short visual flowchart or step-by-step list showing how data moves through the system (e.g., `User Input -> Prompt Pipeline -> Approval UI -> Scheduled Cron -> Meta API`).

### 3. Core MVP Requirements Table
Keep descriptions tight and verifiable.

| ID | Feature | Target User | Requirement & Behavior | Acceptance Criteria | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `FR-001` | [Name] | [Persona] | [Short functional requirement] | - [ ] Criteria 1<br>- [ ] Criteria 2 | Must |
| `FR-002` | [Name] | [Persona] | [Short functional requirement] | - [ ] Criteria 1<br>- [ ] Criteria 2 | Must |

### 4. Developer Micro-Tickets
Write implementation-ready tasks in micro-format. Strictly limit each ticket to under 100 words. **Every ticket must state its 1-sentence value context.**

> **Ticket ID:** `TICK-001` - [Short Title]  
> **Goal:** [1 sentence describing what to build]  
> **User/Business Value:** [1 sentence explaining why this task matters or what problem it solves]  
> **Acceptance Criteria:**  
> - [ ] Checkbox 1  
> - [ ] Checkbox 2  
> **Tech/API Hints:** [Relevant endpoints, DB models, or SDKs]

### 5. Key Decisions & Deferred Scope (V2)
* **Decisions Made:** List top 2-3 choices made to save time.
* **Explicitly Deferred to V2:** List features cut from MVP to avoid bloat (e.g., Multi-account switching, advanced analytics, custom AI fine-tuning).

### 6. Open Questions & Validation Steps
Maximum 3 critical questions that must be answered before writing code.

---

## Notion Execution Guidelines
* **Target:** Publish or update the specified Notion page/database.
* **Formatting:** Use Notion callouts for important warnings, code blocks for API/schema hints, and native tables for requirements.
* **Updates:** If updating an existing page, overwrite outdated sections directly to maintain a single current source of truth. Do not append "v2 additions" or changelogs.
