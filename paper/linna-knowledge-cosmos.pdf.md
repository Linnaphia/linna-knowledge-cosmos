# Linna: A Personal Knowledge Cosmos — 3D Spatial Knowledge Organization with AI-Driven Personal Memory

**Filinna**  
*May 27, 2026*

---

## Abstract

Current AI assistants suffer from a fundamental limitation: they do not remember their users. Each conversation begins from zero, requiring users to re-establish context and re-explain their background. Meanwhile, personal knowledge management tools remain rooted in flat document-folder paradigms that fail to reflect how human memory actually works—spatially, associatively, and emotionally. This paper presents **Linna**, a personal knowledge management system that combines (1) a 3D spatial universe as the organizing metaphor for personal knowledge, (2) a personal knowledge base called the *Book of the Universe* that grows with the user over time, and (3) an AI assistant that retrieves answers from this personal knowledge base rather than from generic internet training data. We describe the system architecture, the design principles grounded in HCI research, and the long-term vision of Linna as an extensible carrier platform—evolving from a personal knowledge tool into a comprehensive ecosystem. This paper serves as a public declaration of prior art and a call for the research community to explore the intersection of spatial cognition, personal knowledge management, and persistent AI memory.

---

## 1. Introduction

The year is 2026. Large language models have become ubiquitous. Yet every AI conversation remains fundamentally anonymous—the AI does not know who you are, what you know, or what you have previously discussed. This is not a technical limitation; it is a design choice. Mainstream AI assistants are optimized for general-purpose question answering, not for building a persistent model of an individual user's knowledge, preferences, and intellectual history.

Meanwhile, personal knowledge management (PKM) has become a thriving category. A variety of tools help users capture and organize information. However, research shows that approximately 50% of saved content is never reopened (UC Berkeley iSchool, 2025). The problem is not capture—it is retrieval, relevance, and emotional connection.

**Linna** proposes a unified solution: a personal knowledge system where every piece of saved information becomes part of a 3D spatial universe, and where an AI assistant answers questions by drawing from this personal knowledge base rather than from generic training data. The result is an AI that genuinely knows its user.

### 1.1 Core Innovations

Linna combines three innovations that, to our knowledge, have not been combined before in a single system:

1. **3D Spatial Universe as Organizing Metaphor**: Knowledge is organized as stars, galaxies, and constellations in a navigable 3D cosmos. This leverages human spatial memory—the same cognitive systems that enable the Method of Loci (memory palace) technique, which has been validated to improve long-term memory retention by 14+ days (Lee & Lee, 2025).

2. **The Book of the Universe**: A personal knowledge base that serves as the sole source of truth for the AI assistant. Unlike generic AI assistants that draw from internet-scale training data, Linna's AI retrieves information from the user's own structured knowledge repository, with source attribution.

3. **Platform Carrier Vision**: Linna is architected not as a single-purpose tool but as an extensible platform that can integrate multiple AI models, support plugins, and eventually expand into a comprehensive ecosystem including services, scheduling, and knowledge sharing—an approach of gradual platform evolution.

### 1.2 Paper Structure

Section 2 reviews related work across HCI, AI memory, and knowledge management. Section 3 presents the system design and architecture. Section 4 describes the design principles grounded in empirical research. Section 5 discusses the phased roadmap. Section 6 concludes with the long-term vision.

---

## 2. Related Work

### 2.1 3D Spatial Interfaces and Cognitive Load

Li et al. (2024) conducted a 40-participant eye-tracking experiment comparing 2D and 3D user interfaces for repetitive tasks in augmented reality. They found that well-designed 3D interfaces significantly reduced cognitive load—measured through shorter eye-blink durations, shorter fixation durations, less dispersed gaze areas, and lower NASA-TLX subjective workload scores. Critically, there was no significant difference in learnability between 2D and 3D interfaces.

Sudár & Csapó (2024) extended this finding to desktop environments, comparing 2D Web 2.0 layouts with two different 3D virtual reality dashboards. Their key finding: 3D environments can reduce cognitive load while maintaining equal task performance, but only when designed to minimize physical locomotion. Camera rotation, they found, imposes less cognitive cost than translation-based navigation.

Hubenschmid et al. (2025) argued for hybrid 2D/3D systems, proposing that users should "stay in the optimal modality for each subtask" without disruptive context switches, combining the spatial overview advantages of 3D with the precision of 2D list/text interfaces.

These findings directly inform Linna's hybrid-mode design (Section 3.4): the 3D cosmos serves as a dashboard for spatial overview and discovery, while search and list views provide efficiency paths for targeted retrieval.

### 2.2 Spatial Memory and Knowledge Retention

The Method of Loci (memory palace technique) has been empirically validated across multiple studies. Lee & Lee (2025) demonstrated that a virtual memory palace with a Worlds-in-Miniature (WIM) interface significantly improved recognition memory, with benefits persisting at 14-day follow-up. Participants who used spatial organization showed better both immediate recall and long-term retention compared to flat-list controls.

This cognitive science foundation justifies Linna's core design metaphor: knowledge organized in 3D space is not merely aesthetic—it leverages innate human spatial memory systems (hippocampal place cells and grid cells) to improve knowledge discovery and retention.

### 2.3 User Retention and Emotional Attachment

Wang et al. (2025) applied the Push-Pull-Mooring (PPM) framework to study user switching intentions on knowledge sharing platforms in China (N=330). Their structural equation model revealed that **mooring effects**—particularly switching cost and media attachment—were the strongest moderators of user retention. Media attachment (emotional connection to a platform) significantly moderated the relationship between push effects (dissatisfaction) and switching intention.

This finding has profound implications for PKM tool design: features that create emotional connection are more effective retention mechanisms than feature completeness alone. For Linna, the spatial universe metaphor—where the user is the "creator and ruler" of their personal cosmos—is designed explicitly to build this emotional mooring effect.

### 2.4 AI Personal Memory Systems

The AI memory space has attracted significant venture capital in 2024-2025. Multiple startups have raised substantial funding for AI memory infrastructure, with the sector attracting over $65M in disclosed funding across seed and Series A rounds in 2025 alone. These investments signal strong market validation for the thesis that AI needs persistent, personalized memory—moving beyond single-session context to truly knowing a user over time.

However, existing systems operate as either infrastructure APIs or 2D document/knowledge-graph interfaces. **None** combines 3D spatial organization with personal knowledge-driven AI in a consumer-facing application with a platform carrier vision.

### 2.5 Visual Metaphor Design for Knowledge

Chu & Chen (2025) studied 2D vs. 3D interactive labeling with connector cues (N=32), finding that 3D modes reduced frustration from constant view-switching in spatial labeling tasks. However, they also found that connector line cues could increase cognitive load in cluttered layouts—a finding that directly informs Linna's progressive disclosure strategy for knowledge connection lines (Decision 5 in our design framework).

---

## 3. System Design

### 3.1 The Book of the Universe: Core Concept

The *Book of the Universe* is Linna's central organizing principle. It consists of:

- **Planets**: Individual knowledge topics. Each planet is a collection of related notes, ideas, and information fragments. Visually, a planet is a sphere whose surface is composed of text lines from its contents—conveying at a glance whether it is "full" or "empty."
- **Galaxies**: Groups of related planets. The mapping between categories and galaxies is flexible and dynamic, not rigid 1:1 (unlike traditional folder hierarchies).
- **Connection Lines**: Knowledge relationships between planets. Four semantic types: causal (red), thematic (cyan), reference (yellow), and temporal (purple). These follow progressive disclosure principles to avoid visual clutter (Chu & Chen, 2025).
- **Lifecycle States**: Each planet evolves through five stages—newborn (blue), active (green), stable (yellow), dormant (purple), archived (gray)—providing visual feedback on knowledge engagement.

### 3.2 Three-Layer Information Architecture

After design review and mobile-platform constraints analysis, the original four-layer architecture was compressed to three layers, ensuring consistent operation flow across desktop and mobile:

```
Layer 1 — Universe Overview
    │  Navigable 3D cosmos showing all planets and galaxies.
    │  Desktop: mouse orbit/zoom; Mobile: single-finger rotate, pinch-zoom.
    │  Click/tap a planet → enter Layer 2.
    │
Layer 2 — Planet Directory
    │  Structured list: title + summary + timestamp + tags.
    │  Click/tap an entry → enter Layer 3.
    │  Swipe down / back button → return to Layer 1.
    │
Layer 3 — Content Reading/Editing
    │  Full-screen text with collapsible table of contents.
    │  Edit, tag, and connect operations available.
    │  Back → return to Layer 2.
```

### 3.3 Two Global Paths (Always Accessible)

Regardless of which layer the user is in, two paths remain universally accessible with identical entry points across desktop and mobile:

| Path | Desktop | Mobile |
|------|---------|--------|
| **Search** | `Ctrl+K` | Top search bar |
| **AI Assistant** | Bottom-right floating orb | Bottom-right FAB button |

This ensures that efficiency-seeking users never need to navigate through 3D space to find what they need (addressing the Sudár & Csapó 2024 finding that excessive 3D locomotion impairs usability).

### 3.4 Hybrid Mode: 3D + 2D Coexistence

Following the Hubenschmid et al. (2025) hybrid interface principle, Linna provides both:

- **3D Cosmos View**: For spatial browsing, knowledge discovery, and emotional engagement. This is the default home screen, establishing the "my world" anchoring effect (Wang et al., 2025).
- **Card/List View**: For efficient scanning, sorting, and editing. Toggleable from the 3D view.

Users naturally stay in the modality that suits their current task, without disruptive switching costs.

### 3.5 AI Assistant Architecture

The AI assistant differs fundamentally from general-purpose chatbots:

1. **Knowledge Source**: Retrieves from the user's Book of the Universe via RAG (Retrieval-Augmented Generation), not from internet training data.
2. **Source Attribution**: Every answer cites specific notes/planets in the user's knowledge base ("This recommendation is based on your March 2026 note on React performance optimization").
3. **Multi-Model Support**: Open architecture supporting DeepSeek (default), GPT, Claude, and any OpenAI-compatible API endpoint. Users can bring their own API keys.
4. **Knowledge Discovery**: Proactively identifies knowledge gaps and suggests connections between planets.

### 3.6 Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | React 19 + TypeScript 5 + Vite 6 | Modern component architecture, type safety |
| 3D Rendering | Three.js + @react-three/fiber | Mature WebGL ecosystem, React integration |
| UI Animation | Framer Motion 11 | Declarative React component transitions |
| 3D Animation | GSAP (planned) | Direct Three.js object manipulation, Timeline |
| State Management | Zustand 4 | Minimal API, no Provider wrapper |
| Backend | FastAPI (Python) | Async-native, auto OpenAPI docs |
| Database | SQLite (WAL + FTS5) | Zero-ops, single-file, built-in full-text search |
| AI Default | DeepSeek API | Strong Chinese language support, low cost |

---

## 4. Design Principles

### 4.1 Research-Grounded Principles

All design decisions are grounded in empirical HCI and cognitive science research rather than aesthetic preference:

1. **Respect Human Operating Habits**: No novel interaction paradigms. All operations follow established user expectations from existing tools (file managers, notes apps, search interfaces).

2. **Efficiency, Simplicity, Durability**: The design framework must scale to accommodate decades of accumulated knowledge without degradation in usability.

3. **Cross-Platform Consistency**: Desktop and mobile share identical operation flows. The only differences are input methods (mouse vs. touch).

4. **Progressive Disclosure**: Advanced features and connections are revealed on demand, not displayed by default. Following Chu & Chen (2025), visual complexity scales with user engagement.

5. **Emotional Anchoring**: The spatial universe metaphor creates media attachment (Wang et al., 2025)—the user is not managing files but ruling a personal cosmos.

### 4.2 Five Key Design Decisions

Our design review process identified five critical architectural decisions, each evaluated against published research:

| # | Decision | Resolution | Research Basis |
|---|----------|-----------|----------------|
| 1 | Primary interface task | **Hybrid mode**: 3D cosmos = dashboard; search = efficiency path | Hubenschmid et al. (2025); Li et al. (2024) |
| 2 | Spatial metaphor | **Universe retained; internal mapping restructured** | Lee & Lee (2025); Wang et al. (2025) |
| 3 | First-time user experience | **Lightweight question + AI-generated initial cosmos** | UC Berkeley iSchool (2025); Forsey & Leahy |
| 4 | Alternative views | **3D + card/list view coexistence** | Hubenschmid et al. (2025) |
| 5 | Connection line visibility | **Under discussion** (hover-highlight direction) | Chu & Chen (2025) |

### 4.3 Eight Design Assumptions — Critical Examination

Each assumption underlying the current implementation was systematically deconstructed and validated or revised:

| Assumption | Status | Required Change |
|------------|--------|-----------------|
| 3D > 2D for main interface | Partially validated | Must pair with 2D efficiency path |
| Category = Galaxy mapping | Questioned | Restructure to flexible dynamic mapping |
| Users will spontaneously explore 3D | Needs guidance | Add clear affordances and progressive cues |
| Spiral galaxy as visual metaphor | Valid direction | Specific form adjustable |
| Connection lines alone convey relationships | Needs progressive disclosure | Add hint lines; hover to reveal |
| Camera flight maintains spatial continuity | Conditional | Keep flights short (<1.2s); add spatial anchors |
| 4-layer architecture | Too deep for mobile | Compress to 3 layers |
| 3-step wizard for onboarding | Redesign | Replace with lightweight question + AI generation |

---

## 5. Phased Roadmap

Linna's development follows a four-phase roadmap spanning from immediate execution to a decade-scale vision.

### Phase 1: Knowledge Storage Foundation (Now – 3 months)

**Goal**: Users can store, organize, find, and want to reopen their knowledge.

- Complete planet/entry CRUD operations
- Full-text search (FTS5)
- 3D cosmos overview (minimal viable version)
- AI-powered text import and auto-categorization
- Tag system + timeline view
- Card/list view alongside 3D
- Desktop complete application

### Phase 2: Book of the Universe + AI Assistant (3–12 months)

**Goal**: AI answers questions using the user's personal knowledge, with source attribution.

- RAG retrieval from user knowledge base
- Source citation in AI responses
- Multi-model API integration
- Connection line 3D visualization (progressive disclosure)
- AI-suggested knowledge connections

### Phase 3: Platformization (1–3 years)

**Goal**: From personal tool to extensible platform.

- Plugin system and third-party integrations
- Knowledge marketplace (share planet/galaxy templates)
- Full mobile applications (iOS + Android)
- Collaboration features
- Public API for external applications

### Phase 4: Universal Carrier (3–10 years)

**Goal**: An indispensable daily AI companion and comprehensive ecosystem platform.

- Life services integration (payment, scheduling, commerce)
- Social knowledge networking
- Enterprise edition (team cosmos)
- AR/VR interfaces
- Autonomous AI agent capabilities

---

## 6. Conclusion

Linna proposes an alternative paradigm for personal knowledge management: one where knowledge is not stored in folders but organized as a living cosmos, and where the AI assistant does not merely chat—it genuinely knows its user through the accumulation of personal knowledge over time.

The core insight is simple but has been overlooked by the current generation of AI products: **a personal AI must have personal knowledge**. The Book of the Universe provides this foundation, and the 3D spatial metaphor transforms knowledge management from a chore into an experience of ownership, discovery, and emotional connection.

This paper serves as a public declaration of prior art. The complete design framework, system architecture, and implementation roadmap are available in the accompanying GitHub repository.

---

## References

1. Li, X., et al. (2024). Comparative Study on 2D and 3D User Interface for Eliminating Cognitive Loads in Augmented Reality Repetitive Tasks. *International Journal of Human-Computer Interaction*, 40(23).

2. Sudár, A. & Csapó, B. (2024). Comparing Desktop 3D Virtual Reality with Web 2.0 Interfaces: Identifying Key Factors Behind Enhanced User Capabilities. *Heliyon*.

3. Hubenschmid, S., et al. (2025). Revisiting Hybrid Input Devices for Immersive Analytics. *Workshop on Human Factors in Immersive Analytics*.

4. Lee, J. & Lee, S. (2025). Enhancing Recognition Memory in Virtual Memory Palaces Using Worlds-in-Miniature. *Applied Sciences*, 15(5), 2304.

5. Wang, R., Ye, D., Jia, Z., & Cho, D. (2025). Knowledge Sharing Platform Users' Switching Intention from the Perspective of the Push-Pull-Mooring Framework. *International Journal of Mobile Communications*, 25(3), 339-368.

6. Chu, Y. & Chen, W. (2025). Investigating 2D and 3D Interactive Labeling with Connector Cues for Symptom-Assisted Appointment Scheduling in mHealth. *HCI International 2025*, Springer LNCS.

7. UC Berkeley School of Information. (2025). ScrollWise: A Personal Knowledge Management Tool. Product Report.

8. Forsey, J. & Leahy, M. Designing for Learnability: Improvement Through Layered Interfaces.

---

## 8. Design Status (Addendum, May 27, 2026)

As of the date of this public disclosure, the Phase 2.5 depth design for Linna has been completed. Six core functional modules have been fully specified: Import Panel, Timeline, AI Chat Panel, Search Panel, Card List View, and Content Editor (L3). The AI engine architecture has been designed with function-calling capability, multi-layered retrieval strategy, and streaming response generation. All design decisions are grounded in the research foundation described in Sections 2–4.

Detailed design documents and implementation specifications are maintained in the private development repository.

---

## Prior Art Declaration

**Date of first public disclosure**: May 27, 2026  
**Repository**: [github.com/Linnaphia/linna-knowledge-cosmos](https://github.com/Linnaphia/linna-knowledge-cosmos)  
**Preprint DOI**: [to be assigned by OSF Preprints]  
**Author**: Filinna  
**License**: Apache 2.0

This document, together with the accompanying GitHub repository and OSF Preprints record, establishes public prior art for the Linna Knowledge Cosmos system. Any subsequent patent applications, product launches, or commercial implementations of substantially similar systems incorporating the combination of (a) 3D spatial universe metaphor for personal knowledge organization, (b) personal knowledge-base-driven AI assistant with source attribution, and (c) carrier platform architecture with multi-model AI integration, are preceded by this disclosure.
