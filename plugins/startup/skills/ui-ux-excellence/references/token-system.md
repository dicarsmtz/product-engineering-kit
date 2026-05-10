# Token System

## Table Of Contents

- Three-file contract
- Required token categories
- CSS and mixin patterns
- Framework theme overrides
- Anti-pattern scans

## Three-File Contract

A serious frontend keeps design tokens in lockstep:

1. `tokens/*.ts`, `tokens.ts`, or equivalent exported constants.
2. `_tokens.scss`, CSS variables, theme CSS, or equivalent runtime styling source.
3. `DESIGN_FOUNDATIONS.md`, design-system docs, or equivalent human-readable contract.

When a token changes, update all three in the same change. If the project uses a design-system package or generated tokens, update the source of truth and generated artifacts according to that system. Document this rule in frontend `AGENTS.md` when missing.

## Required Token Categories

Cover these categories before building one-off values:

- **Color:** surface ladder, borders, text, accent/brand, complement, AI/special, semantic status.
- **Typography:** family, weights, scale, line-height, and tokenized letter spacing if the project uses it.
- **Spacing:** 4px base scale such as 1=4, 2=8, 3=12, 4=16, 5=20, 6=24, 8=32, 12=48, 16=64, 24=96.
- **Radii:** chip, control, card, panel, and pill.
- **Shadow:** card, lift, panel/dialog, glow, focus. Elevated cards should include an inner-top highlight unless the design contract says otherwise.
- **Motion:** fast, base, slow durations and standard, entrance, exit easings.
- **Z-index:** sticky, topbar, drawer, overlay, modal, popover, toast.
- **Breakpoints:** mobile-first thresholds such as sm, md, lg, xl.

Do not use literal spacing >= 4px in component code when a token exists. Do not put hex colors in `.tsx`, `sx` props, component SCSS, or styled leaf components.

## CSS And Mixin Patterns

Mirror TypeScript tokens into CSS variables per theme mode. Keep token names semantic at the component boundary:

```scss
:root,
[data-theme="dark"] {
  --color-canvas: #0f1a17;
  --color-surface: #162824;
  --color-surface-hi: #1a302b;
  --color-border-subtle: rgba(255, 255, 255, 0.08);
  --color-border-focus: #3fbf7f;
  --shadow-card: 0 1px 0 rgba(255, 255, 255, 0.04) inset, 0 12px 32px rgba(0, 0, 0, 0.32);
  --duration-fast: 140ms;
  --duration-base: 200ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
}
```

Useful mixins:

```scss
@mixin focus-ring {
  outline: 0;
  box-shadow: 0 0 0 2px var(--color-canvas), 0 0 0 4px var(--color-border-focus);
}

@mixin card-surface {
  background: var(--color-surface);
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card);
}

@mixin glass-surface {
  background: color-mix(in srgb, var(--color-canvas) 72%, transparent);
  backdrop-filter: blur(18px) saturate(140%);
}

@mixin status-dot {
  position: relative;
  display: inline-block;
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
  background: currentColor;

  &::after {
    content: "";
    position: absolute;
    inset: -0.1875rem;
    border-radius: 50%;
    background: currentColor;
    opacity: 0.42;
    filter: blur(0.1875rem);
  }
}
```

Treat the concrete values above as examples. Replace them with project tokens.

## Framework Theme Overrides

When a project uses Material UI, override every customer-facing surface in the theme: `Button`, `IconButton`, `OutlinedInput`, `Alert`, `LinearProgress`, `ToggleButtonGroup`, `ToggleButton`, `Menu`, `MenuItem`, `Paper`, and `Tooltip`. Set `Paper.backgroundImage = "none"` so Material's default gradient does not leak into the design.

When a project uses shadcn, Radix, Bootstrap, Chakra, Mantine, or another kit, map kit primitives to the project token contract. Do not accept the starter theme as the finished product.

## Anti-Pattern Scans

Run targeted searches before finishing:

```bash
rg -n "#[0-9a-fA-F]{3,8}" src
rg -n "rgba?\\(|hsla?\\(" src
rg -n "margin|padding|gap|border-radius|box-shadow" src
rg -n "setTimeout\\(|duration|transition" src
```

Do not blindly remove every literal. Some token files, resets, or vendor overrides need literals. The goal is to catch leaf-component drift and move repeated values into tokens.
