---
name: Cognitive Clarity
colors:
  surface: '#f9f9ff'
  surface-dim: '#d3daef'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3ff'
  surface-container: '#e9edff'
  surface-container-high: '#e1e8fd'
  surface-container-highest: '#dce2f7'
  on-surface: '#141b2b'
  on-surface-variant: '#464555'
  inverse-surface: '#293040'
  inverse-on-surface: '#edf0ff'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#684000'
  on-tertiary: '#ffffff'
  tertiary-container: '#885500'
  on-tertiary-container: '#ffd4a4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#ffb95f'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#653e00'
  background: '#f9f9ff'
  on-background: '#141b2b'
  surface-variant: '#dce2f7'
  danger: '#EF4444'
  primary-muted: '#EEF2FF'
  surface-bg: '#F9FAFB'
  border-subtle: '#E5E7EB'
  text-secondary: '#4B5563'
typography:
  hero:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h1:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  h2:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  h3:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.5'
  body:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
  label:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.01em
  mono:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is engineered to foster a **professional, calm, and trustworthy** environment for both high-stakes candidates and data-driven recruiters. The aesthetic leans into **Corporate Modernism**, prioritizing functional clarity over decorative elements to reduce cognitive load and user anxiety during evaluation.

The style utilizes a high-contrast, structured approach with generous whitespace and a rigorous layout grid. It borrows elements from **Minimalism** to ensure density doesn't compromise readability, and uses **Progressive Disclosure** to present data in manageable tiers. The emotional response should be one of "reliable intelligence"—a platform that is precise, accessible, and supportive.

## Colors

The palette is anchored by a deep Indigo primary, signaling authority and modern tech. Success, Warning, and Danger colors are functionally mapped to score ranges and system feedback, ensuring immediate semantic understanding.

- **Primary (#4F46E5):** Reserved for core actions (CTAs), focus states, and active navigation indicators.
- **Semantic Ranges:** Green (#10B981) for scores ≥ 75, Amber (#F59E0B) for 50–74, and Red (#EF4444) for < 50.
- **Neutrals:** A grayscale spectrum optimized for WCAG 2.1 AA compliance. `#F9FAFB` provides a soft, non-clinical background for pure white cards.
- **Contrast:** High-contrast text (`#111827`) against clean backgrounds ensures legibility across all lighting conditions.

## Typography

The system uses **Inter** for all UI elements to maintain a clean, humanist feel that is highly legible at small sizes. **JetBrains Mono** is introduced specifically for technical feedback, code snippets, or monospaced data comparisons, providing a distinct visual "anchor" for technical content.

### Hierarchy Rules
- **Headlines:** Use tighter letter spacing and bold weights to establish clear section entry points.
- **Body:** Standardized at 14px to balance data density with readability. 
- **Labels:** Used for captions and metadata, utilizing medium weights to maintain visibility despite smaller scale.
- **Monospace:** Applied to technical scores or raw data outputs to differentiate AI-generated insights from human-readable prose.

## Layout & Spacing

The system employs a **12-column fluid grid** for desktop and a single-column layout for mobile. A strict 4px baseline grid ensures vertical rhythm across all components.

- **Desktop (>1024px):** Fixed sidebar (280px) with fluid main content area. Grids are 3-column for metric cards and 1-column for data tables.
- **Tablet (768–1024px):** Sidebar collapses to icons or a hamburger menu. Grids reflow to 2-columns.
- **Mobile (<768px):** Bottom navigation for accessibility. Full-width cards with 16px horizontal margins.

Spacing is primarily handled via the `md (16px)` unit for internal card padding and `lg (24px)` for gutters between major layout blocks.

## Elevation & Depth

This design system uses **Tonal Layering** combined with **Ambient Shadows** to create a structured hierarchy without overwhelming the user with depth cues.

- **Base Layer:** The page background uses `#F9FAFB`.
- **Surface Layer:** All primary content containers (Cards, Modals) use `#FFFFFF`.
- **Shadow Scale:**
  - `sm`: Used for static cards and input fields to provide a subtle "lift" from the background.
  - `md`: Reserved for hover states on interactive cards or candidate rows.
  - `lg`: Used exclusively for overlays, dropdowns, and modals to focus user attention.
- **Depth via Borders:** In high-density views (like the Recruiter Table), elevation is minimized in favor of subtle `#E5E7EB` borders to maximize screen real estate.

## Shapes

The shape language is "Soft-Modern," using varying radii to distinguish between layout containers and interactive elements.

- **Cards:** 12px radius to feel approachable and modern.
- **Interactive Elements:** Buttons and Input fields use a 8px radius to signify clickability while maintaining a clean, professional edge.
- **Data Pills & Badges:** Use 999px (full-round) for status indicators and score badges, making them instantly recognizable as distinct from functional buttons.
- **Avatars:** Strictly circular (50%) to soften the UI.

## Components

### Buttons & Inputs
- **Primary Button:** Indigo background, white text, 8px radius. Height: 40px (md) / 48px (lg).
- **Secondary Button:** White background, Indigo border/text.
- **Inputs:** 8px radius, 1px border (`--neutral-200`). Focus state uses a 2px Indigo ring with `0.15` opacity.

### Score Badges
- **Circular Badge:** A 48px or 64px circle. The border-thickness represents the score via a circular progress stroke.
- **Color Logic:** Use Success Green for 75+, Warning Amber for 50-74, and Danger Red for <50.

### Progress Bars
- **Track:** 8px height, rounded ends, `--neutral-200` background.
- **Fill:** Animated from left-to-right. Multi-colored based on the same logic as the Score Badge.

### Cards
- **Metric Card:** 16px padding, shadow-sm, contains a 24px icon in the top-left, followed by a label (`caption`) and value (`h2`).
- **Question Card:** Features a structured header with metadata (Progress, Difficulty, Timer) separated by a thin divider from the main question text.

### Candidate Rows
- **Table Design:** 12px vertical padding per row. On hover, apply a slight background shift to `--neutral-50` and `shadow-md` to indicate selectability.