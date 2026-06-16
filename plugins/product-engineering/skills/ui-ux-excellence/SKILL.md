---
name: ui-ux-excellence
description: Design, audit, refactor, polish, or implement high-quality user-facing UI/UX across components, pages, apps, design systems, and marketing surfaces. Use when Codex is asked to build or improve a frontend surface, audit UI copy, audit forms and input patterns, set up or refresh design tokens, write frontend AGENTS.md rules, migrate one design language to another, or sync code, design docs, and project tickets after a UI change.
---

# UI/UX Excellence

## Purpose

Ship user-facing surfaces that feel intentional, accessible, token-driven, and project-native. Use the target project's design contract as the source of truth, then apply this skill's general bar for token discipline, copy restraint, input patterns, focus states, browser verification, and documentation sync.

The Roampler Trail examples in the references are examples of an operations-console direction, not a universal brand. Adapt every concrete color, density, component shape, and tone to the project being edited.

## Preflight

Before writing code, do this in order:

1. Read the project's design contract when it exists: `DESIGN_FOUNDATIONS.md`, design-system docs, Figma exports, and relevant `design/` or `docs/` markdown.
2. Read the closest `AGENTS.md` for the files being edited. The closest file wins; root `AGENTS.md` supplies defaults.
3. Read token sources such as `tokens.ts`, `_tokens.scss`, `theme.ts`, CSS variables, or design-system package exports. Tokens are the source of truth.
4. Run `git status` and inspect relevant diffs. Do not overwrite uncommitted work.
5. Read `package.json` or equivalent to identify framework, styling approach, test scripts, i18n, and existing UI libraries. Do not add dependencies unless the user explicitly asks.
6. Locate i18n files before changing visible strings. New user-facing strings should land in every supported language together.

Project-specific files win for palette, typography, naming, density, and implementation conventions. This skill still holds the cross-project bar: token discipline, accessible focus, designed states, concise copy, and verification.

## Mode

Classify the work before editing:

- **Build or polish:** Sketch the layout in words, choose the aesthetic direction, reuse existing primitives, then implement.
- **Audit or redesign:** Run the redesign audit from `references/redesign-audit.md`, report the punch list and proposed direction, then proceed once the user has accepted the direction or has already asked you to make the changes directly.
- **Design-token work:** Use `references/token-system.md`. Token changes must update code tokens, CSS/theme tokens, and design documentation together.
- **Component-system work:** Use `references/component-contracts.md`. Prefer small primitives over one-off styling.
- **Copy or form work:** Use `references/design-standards.md` for editorial and floating-label rules.
- **Docs or tracker sync:** Update frontend `AGENTS.md`, design docs, Notion, Jira, Linear, or equivalent when a UI contract changes or the user requested external sync.

## Process

1. Identify the audience, primary workflow, next action, and the one thing the user should notice first.
2. Audit existing design files, tokens, components, AGENTS rules, i18n, and package scripts.
3. Name the surface pattern: hero, auth form, dashboard, list/detail, operations console, editor, settings, marketing page, or component primitive.
4. Choose one aesthetic direction that fits the audience. Do not mix unrelated styles.
5. Reuse existing primitives first. Add a primitive only when it removes real duplication or establishes a reusable contract.
6. Keep colors, spacing, radii, shadows, motion, and z-indexes token-driven. Do not place hex colors or magic spacing in component code.
7. Route visible strings through i18n and apply the editorial filter: cut redundant context, shorten actions, and replace verbose validation with direct messages.
8. Give every interactive element hover, `:focus-visible`, active, and disabled states. Use a double-ring focus pattern that reads on every background.
9. Design empty, loading, and error states as actual surfaces. Do not leave text-only fallbacks for shipped UI.
10. Update AGENTS/design docs/tickets when the change creates or modifies a design contract.
11. Run verification gates and perform a manual browser pass when UI changed.

## Non-Negotiables

- Display product names, not repository names or internal codenames.
- Use project tokens or CSS variables for colors and spacing. Literal values belong in token files, not leaf components.
- Keep brand color to one role per visual region: primary CTA, focus ring, active nav, AI affordance, or another intentional role.
- Reserve status colors for status. Do not use green, amber, red, or gray decoratively.
- Use floating labels for fields when the framework supports them. Placeholders are only for format hints or examples.
- Error text replaces helper text. Helper text must be actionable and short.
- Keep badges soft, pill-shaped, and semantic. Avoid solid-fill status badges unless the design contract explicitly requires them.
- Prefer the project's existing icon library. If lucide-react is already installed, use lucide icons for tool and action buttons.
- Do not introduce new dependencies, animation systems, font packages, component kits, or CSS frameworks without explicit user approval.
- Do not let Material UI, shadcn, browser defaults, or framework defaults leak through as the final aesthetic.

## Verification

Run the repo's equivalent gates before declaring done:

```bash
yarn lint
yarn typecheck
yarn test
yarn build
```

Use `pnpm`, `npm`, `bun`, `cargo`, or the repo's documented commands when Yarn is not the package manager. Treat `--max-warnings=0`, strict typecheck, and production build warnings as the project requires.

For UI changes, also verify:

- Dev server golden path in a browser.
- Mobile at <= 600px and desktop at >= 1200px; add tablet when layout changes at the medium breakpoint.
- Dark and light themes when both exist.
- Every supported language touched by new or changed copy.
- Keyboard navigation and double-ring focus on all relevant backgrounds.

If any gate or browser pass cannot run, state exactly what was not verified and why.

## References

- `references/design-standards.md`: aesthetic direction, density, color, motion, editorial copy, input rules, and naming.
- `references/token-system.md`: three-file token contract, token categories, theme override rules, and anti-pattern scans.
- `references/component-contracts.md`: reusable primitive contracts for cards, buttons, badges, status, navigation, forms, and states.
- `references/redesign-audit.md`: audit checklist, report format, verification notes, and "good PR" bar.
