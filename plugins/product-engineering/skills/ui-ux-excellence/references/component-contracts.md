# Component Contracts

## Table Of Contents

- Card
- Button and IconButton
- Badge and StatusDot
- Sidebar and TopBar
- Form fields
- Empty, error, loading
- Toasts
- Sample patterns

## Card

Use card primitives for repeated or framed content, not for every page section.

- Background: surface token.
- Border: subtle border token.
- Radius: large card radius token.
- Shadow: card shadow with inner-top highlight.
- Padding: named scale such as sm, md, lg.
- Elevated variant: stronger shadow ladder.
- Interactive variant: render as a button or link, include hover lift and double-ring focus.

## Button And IconButton

Button:

- Intents: primary, secondary, ghost.
- `glow` or equivalent is reserved for the screen's most important CTA only.
- `full` stretches to the row width.
- States: hover with slight lift/brightness, focus-visible double ring, active reset, disabled with clear affordance.
- Use icons for tool actions when a known icon exists.

IconButton:

- Require an accessible label and tooltip.
- Use a stable square size, commonly 36px when the design contract does not specify.
- Transparent at rest, tint on hover, focus ring on keyboard focus.
- Accent variant only for status-related or high-signal actions.

## Badge And StatusDot

Badge:

- Tones: neutral, success, warning, error, info, AI/special, and one project-specific complement when needed.
- Use soft background plus full-color text.
- Prefer pill shape and concise labels.
- `withDot` uses a luminescent dot in the tone color.

StatusDot:

- 6-8px circle with a blurred halo.
- Tones map to real states, not decoration.
- Add an accessible label when not adjacent to descriptive text.

## Sidebar And TopBar

Sidebar:

- Use the deepest surface for the rail in dark operations layouts.
- Keep expanded/collapsed widths tokenized and stable.
- Section labels use overline/meta treatment.
- Nav rows have fixed height, active state, hover state, and `aria-current` through `NavLink` or framework equivalent.

TopBar:

- Use a glass surface when the design direction supports it.
- Sticky top bar height should be stable.
- Put status/context on the left and utilities on the right.
- Separate utility groups with subtle dividers.

## Form Fields

- Use the framework's floating-label field when available.
- Override focus border and add a soft glow or double-ring focus treatment.
- Keep desktop input height consistent across a form.
- Error text replaces helper text.
- Use `aria-invalid`, `aria-describedby`, and `role="alert"` or equivalent for errors.
- Preserve autocomplete, input type, name, and browser semantics.

## Empty, Error, Loading

All three states are designed surfaces:

- Icon or brand mark tile.
- Short heading.
- One body line.
- Optional single action.

Loading should use the brand mark or a project-native progress pattern. Avoid default spinners as the final shipped loading state unless the design contract specifically uses them. Provide a `bare` mode when the state nests inside an existing surface.

## Toasts

- Slide in from a corner or project-standard toast region.
- Stack predictably.
- Use semantic soft fills.
- Auto-dismiss in 4-6 seconds unless user action is required.
- Never block primary content unless the event is modal by nature.

## Sample Patterns

Polished card:

```tsx
<Card padding="md" elevated>
  <div className="card__heading">
    <div className="card__title-block">
      <h2>{t("setup.progressTitle")}</h2>
      <p>{t("setup.progressSummary", { count: 3, total: 5 })}</p>
    </div>
    <Badge tone="success" withDot size="lg">
      {t("status.inProgress")}
    </Badge>
  </div>
  <div className="card__progress-row">
    <LinearProgress variant="determinate" value={60} />
    <span className="card__progress-value">60%</span>
  </div>
  <p className="card__meta">{t("setup.createdAgo", { days: 3 })}</p>
</Card>
```

Auth surface:

```tsx
<form className="auth-flow__form" onSubmit={handleSubmit}>
  <TextInput
    name="email"
    control={control}
    type="email"
    label={t("auth.emailLabel")}
    placeholder={t("auth.emailPlaceholder")}
    autoComplete="email"
  />
  <Button type="submit" full glow startIcon={<Mail size={16} />}>
    {t("auth.sendLink")}
  </Button>
</form>
```

These samples show structure and copy discipline. Replace component names, translation keys, and token classes with the project's conventions.
