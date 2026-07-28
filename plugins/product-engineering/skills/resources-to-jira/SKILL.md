---
name: resources-to-jira
description: Convert PRDs, technical designs, or notes into lean, code-ready Jira Epics and micro-stories (<100 words). Validates paths against the current codebase, enforces explicit User Value statements, and structures work into clear dependency order without enterprise text bloat.
---

# Resources To Jira (Lean & Code-Validated)

## Primary Directive
Act as a pragmatic Delivery Lead and Lead Engineer. Convert incoming PRDs, technical docs, or user notes into concise, actionable Jira tickets. 

**STRICT RULE:** Eliminate long prose, enterprise overhead, and redundant descriptions. Prioritize scannability, accurate file paths, and strict word caps.

---

## Workflow & Rules

1. **Codebase Validation (Mandatory):**
   * Inspect the codebase to verify file paths, base classes, helper functions, and configuration patterns before generating tickets.
   * Do NOT write tickets based on stale assumptions in design docs.

2. **The "Core 3" MVP Filter:**
   * Focus tickets strictly on the core execution path: **[Context Ingestion] $\rightarrow$ [Generation/Approval] $\rightarrow$ [API Publishing]**.
   * Move non-essential tasks (A/B testing, complex roles, multi-touch analytics) to the Epic's "Out of Scope / V2" section.

3. **Format Constraints:**
   * **Max 100 words per Story description.**
   * Every story MUST include a **1-sentence User/Business Value** statement.
   * Bullet points and checkboxes ONLY.

---

## Standard Ticket Generation Flow

### Step 1: Create the Epic
The Epic serves as the lightweight anchor. Keep descriptions strictly under 150 words using this template:

* **Goal:** [1-2 sentences max]
* **User/Business Value:** [1 sentence explaining core outcome]
* **Key Architecture & Files:** [Tech stack + main modules touched]
* **Out of Scope (V2):** [List deferred features]

### Step 2: Create Micro-Stories
Group work into 3 simple phases: `[Phase 0 Foundation]`, `[Phase 1 MVP]`, `[Phase 2 Endgame]`.

> **Story Summary:** `[Phase N Keyword] Feature: Short Title`  
>  
> **Goal:** [1 sentence describing what to build]  
> **User/Business Value:** [1 sentence explaining why this task matters]  
>  
> **Files to Touch:**  
> - `Create/Modify`: `path/to/validated_file.py`  
>  
> **Acceptance Criteria:**  
> - [ ] Criterion 1  
> - [ ] Criterion 2  
>  
> **Dependencies:** [Depends on / Blocks]

---

## Jira Tooling & Metadata Rules (BlueFlame BFAI)

* **Acceptance Criteria Field:** Send ADF JSON to `customfield_10132` using `scripts/adf_acceptance.py`.
* **Required Fields:** Always populate `Product Area` (`customfield_10134`) and `Testing Needed?` (`customfield_10095`).
* **Issue Links:** Connect hard dependencies using the `Blocks` link type after issue creation.
