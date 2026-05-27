# Linna · Knowledge Cosmos

> **The Book of the Universe** — A personal knowledge cosmos where AI truly knows you.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![OSF](https://img.shields.io/badge/OSF-Registration-green.svg)](https://osf.io/aygk6)
[![Phase](https://img.shields.io/badge/phase-depth%20design%20complete-blue.svg)]()

---

## The Problem

Every AI assistant you use today suffers from the same flaw: **it doesn't remember you**.

Today's AI assistants are brilliant. But every conversation starts from zero. They don't know what you've learned, what you care about, or what you've previously discussed. The AI that is supposed to be *your* assistant has no memory of *you*.

Meanwhile, ~50% of everything you save is never reopened (UC Berkeley iSchool, 2025). Your knowledge is scattered across notes, bookmarks, chat histories, and files — stored but not living.

## The Solution

**Linna** combines three things that have never been combined before:

### 1. A 3D Spatial Universe
Your knowledge isn't a folder tree. It's a cosmos. Each topic is a **planet**. Related topics form **galaxies**. Knowledge connections are glowing **constellation lines**. You are the creator and ruler of your personal universe.

> *Research basis*: 3D spatial interfaces reduce cognitive load (Li et al., 2024). Spatial memory organization improves retention by 14+ days (Lee & Lee, 2025).

### 2. The Book of the Universe
A personal knowledge base that grows with you. Every idea, note, and insight you save becomes part of a structured, searchable, living knowledge system — not a forgotten bookmark.

### 3. An AI That Knows You
The AI assistant doesn't search the internet for answers. It searches **your** Book of the Universe. Every answer comes with a source: "Based on your March 2026 note on React performance..."

> This is not a chatbot. This is *your* AI, built on *your* knowledge.

---

## Core Design Principles

1. **Respect human habits** — No novel interaction paradigms. Operations follow established user expectations.
2. **Efficient, simple, durable** — Designed to scale across decades of accumulated knowledge.
3. **Cross-platform consistent** — Desktop and mobile share identical operation flows.
4. **Progressive** — Build indispensable core features first. Expand gradually.
5. **Zero-barrier access** — Every core operation works for users of any age and background.
6. **AI differentiation first** — Every AI feature must be grounded in the user's Book of the Universe with source attribution.

---

## Architecture

```
Layer 1 — Universe Overview (3D Cosmos)
    │  Navigable starfield. See all your knowledge at a glance.
    │  Click a planet → Layer 2
    │
Layer 2 — Planet Directory (Structured List)
    │  Title + summary + timestamp + tags.
    │  Click an entry → Layer 3
    │
Layer 3 — Content Reading/Editing
    │  Full text with table of contents.
    │  Edit, tag, connect.

Global Paths (always available, every page):
    Search: Ctrl+K (desktop) / top bar (mobile)
    AI Assistant: bottom-right orb (desktop) / FAB (mobile)
```

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19 · TypeScript 5 · Vite 6 |
| 3D | Three.js · @react-three/fiber · GSAP (planned) |
| UI Animation | Framer Motion 11 |
| State | Zustand 4 |
| Backend | FastAPI (Python) |
| Database | SQLite (WAL + FTS5) |
| AI | DeepSeek (default) · GPT · Claude · OpenAI-compatible |

---

## Roadmap

| Phase | Timeline | Goal |
|-------|----------|------|
| **1. Foundation** | Now – 3 months | Store, organize, find. Users *want* to come back. |
| **2. Book of the Universe** | 3–12 months | AI answers from personal knowledge with source citations |
| **3. Platform** | 1–3 years | Plugins, mobile apps, knowledge marketplace |
| **4. Carrier** | 3–10 years | Full ecosystem — life services, knowledge sharing, AI agents |

---

## Prior Art & Intellectual Property

This repository and the accompanying [OSF Preprint](https://osf.io/) serve as **public prior art declaration** for the Linna Knowledge Cosmos system.

- **Date of first public disclosure**: May 27, 2026
- **Author**: Filinna
- **License**: Apache 2.0

The specific combination of (a) 3D spatial universe metaphor for personal knowledge, (b) personal knowledge-base-driven AI with source attribution, and (c) multi-model carrier platform architecture represents an approach we believe has not been fully explored in a consumer-facing application.

---

## Documentation

- [Design Framework & Vision (English)](docs/design-framework.md)
- [设计框架与愿景（中文）](docs/design-framework_CN.md)
- [Academic Paper (Preprint)](paper/linna-knowledge-cosmos.pdf.md)
- [Full Research References](docs/research-references.md)

---

## Contact

- **Creator**: Filinna
- **Domain**: [filinna.top](https://filinna.top)
- **OSF Registration**: [osf.io/aygk6](https://osf.io/aygk6) — May 27, 2026 (DOI pending)

---

## Core Modules

Depth design (Phase 2.5) completed with 6 core functional modules:

- **Import Panel** — Unified entry for external knowledge. Drag-and-drop, batch folder import, AI-powered classification.
- **Timeline** — Global vertical timeline. Browse knowledge across all planets by day/month/year.
- **AI Chat Panel** — Right-side slide-out panel. AI guardian searches your Book of the Universe, not the internet.
- **Search** — Ctrl+K global search. Results grouped by planet, keyboard-navigable. AI steps in when no results are found.
- **Card List** — Alternative planet view. Compact rows with sort, pin, and a morphing transition from 3D cosmos to cards.
- **Editor (L3)** — Read/Edit dual mode. Immersive reading by default, toolbar slides up when editing.

## Current Status

**May 27, 2026**: Phase 2.5 depth design complete. 6 core modules + AI engine architecture finalized. Ready for development.

---

*"Your knowledge is not a folder. It's a universe."*
