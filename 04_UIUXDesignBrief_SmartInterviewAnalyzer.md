# UI/UX Design Brief
## Smart Interview Analyzer

**Version:** 1.0  
**Date:** June 2026

---

## 1. Design Philosophy

The platform must feel **professional, calm, and trustworthy** — not clinical or cold. Candidates are in a high-stress situation (being evaluated); the UI should reduce anxiety. Recruiters need dense data to be quickly scannable.

**Core Principles:**
- **Clarity over cleverness** — every element must communicate a clear purpose
- **Progressive disclosure** — show simple views first, details on demand
- **Feedback at every step** — users always know what's happening and what's next
- **Accessible by default** — WCAG 2.1 AA compliance, high contrast, keyboard navigation

---

## 2. Brand & Visual Identity

### 2.1 Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--primary` | `#4F46E5` | Indigo — CTAs, active states, brand accent |
| `--primary-light` | `#EEF2FF` | Hover backgrounds, subtle highlights |
| `--success` | `#10B981` | Scores > 75, positive feedback |
| `--warning` | `#F59E0B` | Scores 50–75, caution states |
| `--danger` | `#EF4444` | Scores < 50, errors |
| `--neutral-900` | `#111827` | Primary text |
| `--neutral-600` | `#4B5563` | Secondary text |
| `--neutral-200` | `#E5E7EB` | Borders, dividers |
| `--neutral-50` | `#F9FAFB` | Page background |
| `--white` | `#FFFFFF` | Card backgrounds |

### 2.2 Typography

| Role | Font | Size | Weight |
|------|------|------|--------|
| Display (hero) | Inter | 32px | 700 |
| H1 | Inter | 24px | 700 |
| H2 | Inter | 20px | 600 |
| H3 | Inter | 16px | 600 |
| Body | Inter | 14px | 400 |
| Caption / Label | Inter | 12px | 500 |
| Code / Monospace | JetBrains Mono | 13px | 400 |

### 2.3 Spacing System
Base unit: `4px`  
Spacing scale: `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64px`

### 2.4 Border Radius
- Cards: `12px`
- Buttons: `8px`
- Inputs: `8px`
- Badges / Pills: `999px`
- Avatar: `50%`

### 2.5 Elevation / Shadows
```css
--shadow-sm:  0 1px 2px rgba(0,0,0,0.05);
--shadow-md:  0 4px 6px rgba(0,0,0,0.07);
--shadow-lg:  0 10px 15px rgba(0,0,0,0.10);
```

---

## 3. Component Design Specs

### 3.1 Score Badge
Circular badge displaying numeric score (0–100).  
Color changes based on score range:
```
≥ 75 → success green
50–74 → warning amber
< 50 → danger red
```

### 3.2 Progress Bar
Height: `8px`, rounded pill, animated fill on load.  
Used for: keyword coverage, grammar score, communication score.

### 3.3 Metric Card
White card with shadow-sm, 16px padding.  
Contains: icon (24px), label (caption), value (H2), optional trend arrow.

### 3.4 Question Card (during interview)
```
┌─────────────────────────────────────────────────┐
│  Q3 of 10            [ MEDIUM ]    ⏱ 01:45      │
├─────────────────────────────────────────────────┤
│                                                 │
│  Explain the difference between authentication │
│  and authorization in a REST API.              │
│                                                 │
├─────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────┐  │
│  │  Your answer...                           │  │
│  │                                           │  │
│  └───────────────────────────────────────────┘  │
│                            [ Submit Answer →]   │
└─────────────────────────────────────────────────┘
```

### 3.5 Candidate Row (Recruiter Table)
```
| Avatar | Name + Role  | Final Score | Technical | Comm. | Confidence | Date | Actions |
| ●      | Riya Sharma  |    [92]     |   88%     | 90%   |    87%     | Jun 1| View PDF|
```
Score colored by range. Rows sortable.

---

## 4. Page-by-Page Screens

### 4.1 Landing Page
- Hero: "AI-Powered Interview Analysis for Smarter Hiring"
- Sub-headline: feature highlights (3 columns: Record → Analyze → Hire)
- CTA buttons: "I'm a Candidate" / "I'm a Recruiter"
- Social proof: stats (interviews analyzed, companies using)
- Footer: links, legal

### 4.2 Candidate Dashboard
**Layout:** Sidebar (nav) + main content area
```
Sidebar:
  - Logo
  - Dashboard (home)
  - Start Interview
  - My Reports
  - Resume Analysis
  - Progress
  - Settings

Main Area:
  - Welcome banner with name
  - Quick stats row: [Interviews taken] [Avg Score] [Best Score] [Streak]
  - Recent interviews list (card per interview)
  - Resume ATS score widget
  - CTA: "Start New Interview"
```

### 4.3 Interview Screen
- **Pre-interview:** Review job role, question count, mode, instructions → "Begin"
- **During interview:**
  - Top bar: progress (Q3/10), timer countdown, mode indicator
  - Center: question card (see spec above)
  - Audio mode: waveform visualizer during recording
  - Video mode: live camera preview + recording indicator
- **Post-submit:** "Processing your responses…" loader with status updates

### 4.4 Report Screen (Candidate View)
```
┌──────────────────────────────────────────────────────┐
│  Interview Report — Backend Developer · June 2, 2026 │
│                                              [Download PDF] │
├──────────────┬───────────────────────────────────────┤
│  FINAL SCORE │  SCORE BREAKDOWN                      │
│    [ 81 ]    │  Technical    ████████░░  80%          │
│   out of 100 │  Communication████████░░  85%          │
│              │  Confidence   ███████░░░  70%          │
│              │  Keywords     █████████░  90%          │
├──────────────┴───────────────────────────────────────┤
│  AI FEEDBACK                                         │
│  ✅ Strengths: Good understanding of REST, JWT auth  │
│  ⚠️  Weaknesses: Missing caching concepts, SQL gaps  │
│  💡 Suggestions: Study Redis, practice SQL indexes   │
├──────────────────────────────────────────────────────┤
│  PER-QUESTION BREAKDOWN                              │
│  [accordion list of Q1–Q10 with scores + feedback]   │
└──────────────────────────────────────────────────────┘
```

### 4.5 Recruiter Dashboard
```
Layout: Top nav + main grid

Tabs:
  [Candidates] [Job Roles] [Analytics] [Question Bank]

Candidates Tab:
  - Filter by: Job Role, Score Range, Date
  - Sortable ranking table
  - "Compare" button (select 2 candidates)

Analytics Tab:
  - Avg score card, total interviews card
  - Line chart: score trend over time
  - Bar chart: skill distribution (Python / Java / SQL / React)
  - Donut chart: confidence level distribution
```

### 4.6 Comparison Screen (Recruiter)
```
┌──────────────────────────────────────────────────┐
│  Candidate A: Arjun Mehta  vs  Candidate B: Riya │
├──────────────┬───────────────────────────────────┤
│  Metric       │    Arjun       │    Riya          │
│  Final Score  │     [87]       │     [92]         │
│  Technical    │     84%        │     90%          │
│  Communication│     86%        │     88%          │
│  Confidence   │     80%        │     94%          │
│  Keywords     │     88%        │     92%          │
├──────────────┴───────────────────────────────────┤
│  SKILL HEATMAP  [Python] [Java] [SQL] [API Design]│
│  Arjun:        ████     ███    █████  ████        │
│  Riya:         █████    ████   ████   ████        │
└──────────────────────────────────────────────────┘
```

---

## 5. Responsive Design

| Breakpoint | Width | Layout |
|-----------|-------|--------|
| Mobile | < 768px | Single column, bottom nav |
| Tablet | 768–1024px | Sidebar collapsible, 2-col grids |
| Desktop | > 1024px | Full sidebar, 3-col grids |

Interview screen is **desktop-only recommended** for video mode. Mobile support for text-based only.

---

## 6. Key Interaction Patterns

### 6.1 Recording UI (Voice/Video)
- Red pulsing dot when recording
- Live waveform animation (audio)
- Camera feed preview in corner (video)
- Countdown before recording starts (3, 2, 1…)

### 6.2 Score Reveal Animation
- Circular score badge animates fill from 0 to final value (0.8s ease-out)
- Progress bars fill left-to-right with a 0.5s delay

### 6.3 Loading States
- Skeleton loaders on all data tables and cards
- Processing screen post-interview: step-by-step status (Transcribing → Analyzing → Generating Feedback → Done)

### 6.4 Empty States
- Illustrated placeholder for no interviews yet: "No interviews yet. Start your first one!"
- Friendly illustration (not just blank text)

---

## 7. Accessibility

- All interactive elements keyboard-navigable
- ARIA labels on icon buttons and form fields
- Minimum contrast ratio: 4.5:1 for body text, 3:1 for large text
- Focus ring visible on all focusable elements
- Audio transcripts available for all voice/video content
- Error messages appear as inline text (not only color-coded)
