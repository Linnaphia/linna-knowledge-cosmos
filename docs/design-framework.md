# Linna Design Framework & Vision

> Last updated: 2026-05-27 (Depth Design Complete)
> 6 core modules + AI engine architecture finalized. Ready for development.

---

## Product Vision

**Linna is not a note-taking tool. It is a carrier platform for the AI era.**

The core differentiation: every AI assistant today has "amnesia" — it doesn't remember its user. Linna's AI has the **Book of the Universe** as its knowledge foundation. The AI draws answers from the user's personal structured knowledge, not from generic internet training data.

**The user is the creator and ruler of their personal cosmos.** The AI assistant is the guardian and steward.

---

## Five Key Design Decisions

### Decision 1: Primary Interface Mode → Hybrid
**3D cosmos = knowledge dashboard** (overview, discovery, emotional attachment). **Search/list = efficiency path** (quick retrieval, precise editing). Both coexist.

*Research*: Hubenschmid et al. (2025); Li et al. (2024) — 3D reduces cognitive load when paired with 2D efficiency paths.

### Decision 2: Spatial Metaphor → Universe (Restructured Mapping)
Retain the universe visual metaphor. Restructure internal mapping — category ≠ galaxy. Dynamic, flexible spatial organization.

*Research*: Lee & Lee (2025) — spatial memory improves 14-day retention. Wang et al. (2025) — media attachment is strongest retention anchor.

### Decision 3: First-Time Experience → Lightweight Question + AI Generation
One simple question on first open. AI generates a personalized initial cosmos. Lighter than a 3-step wizard, more guided than a blank canvas.

*Research*: UC Berkeley iSchool (2025); Forsey & Leahy — layered interfaces improve learnability.

### Decision 4: Alternative Views → 3D + Card/List Coexistence
3D cosmos and card/list views coexist side by side. The spatial view serves browsing and discovery, the list view serves efficient retrieval and editing.

*Research*: Hubenschmid et al. (2025) — avoid disruptive modality switching.

### Decision 5: Connection Line Visibility → Under Discussion
Direction: hover-highlight with persistent hint lines (progressive disclosure).

*Research*: Chu & Chen (2025) — connector cues increase cognitive load in cluttered layouts.

---

## Eight Assumptions — Critical Review

| # | Assumption | Status | Change Required |
|---|-----------|--------|-----------------|
| 1 | 3D > 2D as default interface | Partially validated | Must pair with 2D efficiency path |
| 2 | Category = Galaxy mapping natural | Questioned | Flexible dynamic mapping needed |
| 3 | Users spontaneously explore 3D | Needs guidance | Add clear affordances, progressive cues |
| 4 | Spiral galaxy as visual metaphor | Valid | Form adjustable |
| 5 | Connection lines convey relationships | Needs disclosure | Hover-reveal with persistent hints |
| 6 | Camera flight maintains continuity | Conditional | Keep <1.2s; add spatial anchors |
| 7 | 4-layer architecture appropriate | Too deep for mobile | Compress to 3 layers |
| 8 | 3-step wizard sufficient onboarding | Redesign | Lightweight question + AI generation |

---

## Unified Operation Flow (Cross-Platform)

```
Layer 1 — Universe Overview (3D Cosmos)
    │  Rotate/zoom. See all knowledge at a glance.
    │  Desktop: mouse orbit. Mobile: single-finger rotate, pinch-zoom.
    │  Click/tap a planet → Layer 2
    │
Layer 2 — Planet Directory (Structured List)
    │  Title + summary + timestamp + tags.
    │  Click/tap entry → Layer 3
    │  Swipe/back → Layer 1
    │
Layer 3 — Content Reading/Editing
    │  Full text. Collapsible table of contents.
    │  Back → Layer 2

Global Paths (identical across desktop/mobile):
    Search: Ctrl+K / top bar
    AI Assistant: bottom-right orb / FAB button
```

---

## Phased Roadmap

| Phase | Timeline | Goal |
|-------|----------|------|
| 1. Foundation | Now – 3 months | Reliable knowledge storage. Users *want* to return. |
| 2. Book of the Universe | 3–12 months | RAG-powered AI answers from personal knowledge with citations |
| 3. Platform | 1–3 years | Plugins, mobile, knowledge marketplace |
| 4. Carrier | 3–10 years | Full ecosystem: life services, knowledge sharing, AI agents |

---

## Research Foundation

See [research-references.md](research-references.md) for complete bibliography with findings and Linna applications.

---

## Prior Art Declaration

**Date of first public disclosure**: May 27, 2026  
**Author**: Filinna  
**License**: Apache 2.0
