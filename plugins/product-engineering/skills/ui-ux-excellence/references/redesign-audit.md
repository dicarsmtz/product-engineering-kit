# Redesign Audit And Verification

## Table Of Contents

- Redesign audit
- Audit report format
- Verification gates
- Good PR bar
- Tracker and docs sync

## Redesign Audit

Before broad redesign work, inspect and report:

1. **Token audit:** Do tokens exist? Are modes consistent? Are colors or spacing literalized in components?
2. **Component audit:** Which primitives are reusable? Which one-offs should collapse into shared components?
3. **Copy audit:** Apply the editorial filter to every visible string. Produce current -> proposed changes per language when copy changes are material.
4. **Input audit:** Check floating labels, placeholders as format hints only, concise helpers, error replacement, autocomplete, and semantics.
5. **A11y audit:** Check focus rings on every background, keyboard order, skip links, `aria-current`, form errors, and semantic controls.
6. **Naming audit:** Remove repository names, codenames, and internal jargon from rendered text.
7. **State audit:** Empty, loading, and error states must be designed surfaces, not text fallbacks.
8. **Dependency audit:** Confirm the existing stack can support the redesign without new packages.

For a small polish request, keep this audit lightweight and proceed. For a full redesign, show the punch list and direction before making broad edits unless the user has already told you to proceed.

## Audit Report Format

Use a concise punch list:

```markdown
**Direction**
Operations-dense, dark-first dashboard using the existing token ladder and current component catalog.

**Findings**
- Token drift: hardcoded focus color in `src/components/Button.tsx`; move to `--color-border-focus`.
- Copy: sign-in helper repeats the email label; shorten to "We'll send a single-use link."
- Inputs: placeholder is acting as a label in `InviteUserForm`; add floating label and keep placeholder as example only.
- A11y: active sidebar row lacks `aria-current`; use `NavLink`.

**Proposed Change**
Consolidate cards/buttons/badges to existing primitives, refresh auth and dashboard states, update i18n, then run lint/typecheck/test/build plus browser checks at mobile and desktop.
```

## Verification Gates

Run all project equivalents before declaring done:

```bash
yarn lint
yarn typecheck
yarn test
yarn build
```

For UI changes, also start the dev server and test:

- Golden path for the changed surface.
- Mobile <= 600px and desktop >= 1200px.
- Tablet when the layout shifts at the medium breakpoint.
- Dark and light themes when both exist.
- Every supported language touched by changed copy.
- Keyboard navigation and focus-visible rings.

Do not claim the UI works because typecheck passed. If visual verification is blocked, state it explicitly.

## Good PR Bar

A strong UI/UX change should have:

1. Zero hex colors in leaf components, `sx` props, or component CSS.
2. Zero magic spacing values >= 4px in leaf components when tokens exist.
3. All four verification gates passing or a clear blocker note.
4. Token code, CSS/theme tokens, and design documentation updated together when tokens change.
5. Frontend `AGENTS.md` updated when a new pattern or rule was introduced.
6. New visible strings added to every supported language.
7. Manual browser-pass notes listing viewports, themes, languages, and any unverified areas.
8. Cross-links to Notion, Jira, Linear, or design docs when the change ships a foundation contract.

## Tracker And Docs Sync

Sync external sources when requested or when the UI change alters a durable contract:

- Notion/design docs: update token, component, layout, and copy decisions.
- Jira/Linear: update story scope, acceptance criteria, screenshots, verification notes, and follow-up bugs.
- `AGENTS.md`: add concise rules for new frontend patterns.
- Design-system docs: document new primitives and anti-patterns.

Keep sync factual. Do not create version-log sections unless the user asks; update the canonical sections so the next contributor finds one current source of truth.
