# Design Standards

## Table Of Contents

- Aesthetic direction
- Density by context
- Color and depth
- Motion and states
- Editorial copy
- Floating-label inputs
- Naming and brand

## Aesthetic Direction

Every interface needs a point of view. Choose one direction that fits the audience and execute it consistently:

- **Brutalist:** raw, sparse, monospace, hard edges.
- **Editorial:** strong hierarchy, generous whitespace, asymmetric composition.
- **Operations console:** dense, signal-first, status-coded, dark-canvas friendly. Roampler Trail fits here.
- **Refined or luxury:** restrained palette, precise spacing, elevated typography.
- **Organic or natural:** warm tones, tactile materials, irregular accents.
- **Retro-futuristic:** high contrast, glow, scan-line or terminal influences.

Avoid generic AI styling: purple-on-white gradients, unstyled default cards, lavender dashboards, or framework-default component kits. Match the direction to the product. A tourism operations workspace, developer console, consumer habit app, and public marketing page should not look identical.

## Density By Context

Use the project's spacing and typography scale, then tune density to the surface:

- **Marketing/public:** spacious, hero-led, body text usually 16-18px.
- **Operations workspace:** dense but calm, body around 14px, meta around 12px, tight scanning layouts.
- **Developer console:** denser still, often 13px body and monospace for data or commands.
- **Consumer app:** medium density, more whitespace than operations, less than marketing.

Do not default to a generic 16px body plus large whitespace. Density is only calm when the spacing scale stays honest.

## Color And Depth

Color must carry meaning before decoration:

- Put brand accent in one role per visual region: CTA, active navigation, focus ring, AI affordance, or another explicit role.
- Reserve status colors for status: success/active, warning/at-risk, error/stuck, neutral/inactive.
- Use a secondary accent only to differentiate the brand or domain, not as a default surface paint.
- Check the screen in grayscale mentally: hierarchy should still read without hue.

For dark surfaces, build depth with a surface ladder: void -> canvas -> surface -> surface-hi -> tint -> tint-hi. Elevated surfaces need an inner-top highlight, often described as a ridge of light. For light themes, invert depth with white surfaces, subtle highlights, and soft shadows tinted by the deepest brand color.

Use glass effects sparingly for top bars, command palettes, drawers, and overlays: translucent canvas, blur, and saturation. Use mesh or radial gradients only for hero/auth backgrounds where the project direction supports it.

## Motion And States

Use a tiny motion vocabulary:

- Fast for hover micro-interactions.
- Base for card lifts and sidebar changes.
- Slow for drawer or modal entry.

Use project motion tokens for duration and easing. Do not put magic durations in component code.

Every interactive element needs hover, `:focus-visible`, active, and disabled states. Focus should use a double-ring pattern: an inner ring matching the canvas plus an outer ring using the focus/accent token. Page transitions should be quiet; reserve animation for hover, focus, and meaningful loading feedback.

## Editorial Copy

Apply this filter to every visible string:

1. Cut strings that are too long.
2. Remove text that explains what the user already knows from layout or context.
3. Rewrite vague, formal, or cold language.
4. Remove repeated context.

Common rewrites:

| Current | Better |
| --- | --- |
| Click here to continue | Continue |
| This field is required. | Required |
| Please enter a valid email address. | Invalid email |
| Sign in with your email | Sign in |
| Account created {{date}} | Created {{date}} |
| {{count}} of {{total}} foundation steps complete. | {{count}} of {{total}} done. |

Keep section descriptions to one sentence. Adapt copy per language instead of literal-translating. B2B operations Spanish, consumer Spanish, German, and Japanese have different concision and register norms.

## Floating-Label Inputs

Use this decision tree:

1. Add a floating label. It is the primary identifier and should be concise.
2. Add a placeholder only when it provides a format hint or example, such as `MM/DD/YYYY`, `you@company.com`, or `acme.com`.
3. Add helper text only for actionable context: optionality, max length, or a security note.
4. Replace helper text with validation error text when invalid.

Do not place a static external label next to a floating label. Do not use a placeholder as the only label. Do not write helpers that restate the label.

## Naming And Brand

Show the product name, not the repository name. Users should see "Roampler", "Stripe", or the product brand, not "Helm", "stripe-monorepo", or internal codenames.

Internal identifiers may keep repository names in HTTP headers, localStorage keys, file names, debug logs, and code. The rule is for rendered text.

Use operational surface names for product areas: Inbox, Analytics, Operations, Settings. Avoid compound wordmarks like "Product Helm" unless the brand contract explicitly says so.
