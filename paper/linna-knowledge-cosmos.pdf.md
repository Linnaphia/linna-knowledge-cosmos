# Linna: A Personal Knowledge Cosmos — 3D Spatial Knowledge Organization with Character-Driven AI Memory

**Filinna**  
*May 27, 2026 (v1) · Updated June 2026 (v2)*

---

## Abstract

Current AI assistants suffer from a fundamental limitation: they do not remember their users. Each conversation begins from zero, requiring users to re-establish context and re-explain their background. Meanwhile, personal knowledge management tools remain rooted in flat document-folder paradigms that fail to reflect how human memory actually works—spatially, associatively, and emotionally. This paper presents **Linna**, a personal knowledge management system built around six interconnected innovations: (1) a 3D spatial universe as the organizing metaphor for personal knowledge, leveraging innate human spatial cognition; (2) the *Book of the Universe*, a structured personal knowledge base that serves as the sole source of truth for AI responses; (3) a **Guardian Personality Engine** that replaces generic AI interaction with a character-driven companion exhibiting emotional continuity, scene awareness, and a three-layer personality architecture; (4) a **Hybrid Knowledge Retrieval Architecture** that fuses personal knowledge retrieval, real-time web search, and universe-wide contextual awareness into a unified response pipeline; (5) an **Identity-Driven AI Onboarding System** that replaces empty-state tutorials with AI-generated personalized initial knowledge structures; and (6) a **Carrier Platform Architecture** designed for gradual evolution from personal tool to comprehensive ecosystem. We describe the complete system architecture, the design principles grounded in HCI and cognitive science research, the specific technical mechanisms that make each innovation irreducible to renaming, and the long-term phased roadmap. This paper serves as a public declaration of prior art establishing the unique combination of 3D spatial cognition, character-driven AI companionship, and personal knowledge-driven intelligence.

---

## 1. Introduction

The year is 2026. Large language models have become ubiquitous. Yet every AI conversation remains fundamentally anonymous—the AI does not know who you are, what you know, or what you have previously discussed. This is not a technical limitation; it is a design choice. Mainstream AI assistants are optimized for general-purpose question answering, not for building a persistent model of an individual user's knowledge, preferences, and intellectual history.

Meanwhile, personal knowledge management (PKM) has become a thriving category. A variety of tools help users capture and organize information. However, research shows that approximately 50% of saved content is never reopened (UC Berkeley iSchool, 2025). The problem is not capture—it is retrieval, relevance, and emotional connection.

**Linna** proposes a unified solution that addresses both failures simultaneously. First, every piece of saved information becomes part of a navigable 3D spatial universe, transforming knowledge management from a clerical task into an experience of ownership and discovery. Second, an AI companion—not a generic chatbot but a character with persistent personality, emotional continuity, and genuine awareness of the user's knowledge landscape—answers questions by drawing from this personal knowledge base. The result is not merely a tool that stores information, but a companion that genuinely knows its user.

### 1.1 Six Core Innovations

Linna combines six innovations that, to our knowledge, have not been combined before in a single system. Each innovation is described with sufficient technical specificity that functional equivalence would constitute derivation:

**Innovation 1 — 3D Spatial Universe as Organizing Metaphor**: Knowledge is organized as planets, galaxies, and constellations in a navigable 3D cosmos with a precisely specified data-to-visual mapping: planet size = `0.7 + min(entry_count, 10) × 0.16`, planet position by Fibonacci sphere distribution for uniform coverage, color by 8-value semantic palette, and lifecycle-driven luminosity (5 stages: newborn → active → stable → dormant → archived). The spatial layout is not decorative—it directly encodes knowledge state information that is recoverable at a glance. Camera navigation follows a 4-state finite state machine (overview → flying-in → interior → flying-out) with 1.2-second bounded flight duration informed by spatial continuity research (Sudár & Csapó, 2024). The galaxy interior uses simplex-noise-perturbed logarithmic spiral arm generation rather than pure mathematical spirals, producing organic irregularity that subconsciously signals "this is a real place" rather than a diagram. This innovation leverages the Method of Loci effect validated by Lee & Lee (2025): spatial organization improves 14-day memory retention compared to flat-list controls.

**Innovation 2 — The Book of the Universe: Structured Personal Knowledge Base**: A local-first knowledge repository with a specific data model: Planets (knowledge topics) → Entries (individual notes) → Connection Lines (typed semantic relationships). Each entry carries immutable provenance metadata (source: manual/AI-conversation/import/clipboard), content hash (SHA-256 for deduplication), and timestamps. Planets maintain a 5-stage lifecycle state machine with automatic state transitions based on recency of activity. Connection lines carry four precisely defined semantic types—causal (red #FF6B6B), thematic (cyan #4ECDC4), reference (yellow #FFE66D), temporal (purple #A78BFA)—with continuous strength values (0–1 floating point) rather than discrete categories, enabling AI-generated relationship scoring. The database uses SQLite with WAL mode and FTS5 full-text search for zero-operations deployment while maintaining ACID guarantees. Atomic write operations (temp file → fsync → atomic rename) ensure data integrity. This structure is not a generic "knowledge graph"—the specific combination of 5-stage lifecycle + 4-type semantic connections + provenance tracking + content-addressable deduplication constitutes a unique architecture.

**Innovation 3 — Guardian Personality Engine: Character-Driven AI Companionship**: Linna introduces a *personality engine architecture* that transforms AI interaction from generic utility into character-driven companionship. The engine has four architectural layers: (a) a **three-layer personality model**—daily warmth (empathetic, caring, emotionally perceptive), work precision (concise, analytical, decisively critical when needed), and protective boundary (firm ethical guardrails, user advocacy)—each layer activating contextually based on conversation analysis; (b) **scene-aware behavior modulation** that adjusts interaction style based on time of day (early morning / daytime / evening / late night) and conversation trajectory; (c) **emotional continuity** across sessions, where the Guardian references prior conversations and the user's evolving knowledge state without requiring re-introduction; and (d) a **universe-awareness mechanism** that injects the user's knowledge landscape summary (planet count, entry count, recently active domains) into the conversation context, enabling the Guardian to speak with genuine awareness of "what the user has been thinking about." The personality is defined through a structured behavioral specification—not hardcoded rules but a comprehensive description of interaction patterns, emotional responses, and communication style. This specification is model-agnostic: any capable LLM can adopt the Guardian role by processing the personality definition as its system context. The architecture is designed to support multiple personality profiles while maintaining a single persistent identity per user—the user's Guardian is *their* Guardian, not a shared generic assistant.

**Innovation 4 — Hybrid Knowledge Retrieval Architecture: Three-Source Fusion**: The Guardian's knowledge retrieval operates through a three-source fusion pipeline, not a single RAG endpoint. **Source 1 — Personal Knowledge Base**: semantic search (vector embedding similarity, threshold 0.25) with automatic FTS5 full-text search fallback when semantic infrastructure is unavailable, retrieving contextually relevant notes with planet attribution. **Source 2 — Real-Time Web Search**: multi-engine fallback chain (Bing → DuckDuckGo → DuckDuckGo Lite) via system-level HTTP with proxy awareness, returning time-sensitive information that the Guardian relays in natural conversational form with explicit source URLs. **Source 3 — Universe Awareness Summary**: a pre-computed snapshot of the user's entire knowledge landscape (total planet/entry counts, recently active domains) injected into every conversation, giving the Guardian persistent awareness of the user's intellectual trajectory. The fusion is not post-hoc: all three sources are injected into the system prompt *before* the LLM generates its response, enabling integrated reasoning across personal knowledge, fresh information, and long-term user context. Critically, the Guardian is instructed to cite personal knowledge with natural recall language (e.g., "I remember you wrote about...") rather than mechanical retrieval markers, and to present web-sourced information as personally verified ("I checked, and currently...") rather than delegating to the user. This three-source architecture is fundamentally different from both pure-RAG systems (which lack real-time awareness) and pure-search assistants (which lack personal memory).

**Innovation 5 — Identity-Driven AI Onboarding: From Empty State to Personal Cosmos**: Traditional PKM tools confront new users with an empty canvas—the "cold start" problem that research shows leads to ~50% content abandonment. Linna's onboarding inverts this: instead of teaching the user how to create structure, the system asks two lightweight questions (identity profile from 6 presets + interest domains from 8 categories), then **AI-generates a complete initial cosmos**—planets populated with starter notes, categorized into galaxies, with suggested connection lines. The 6 identity profiles (e-commerce operations, learning & growth, workplace productivity, personal management, content creation, free exploration) and 8 interest categories (AI, business, education, design, writing, health, finance, gaming) produce a cross-product of 48 initial configurations, each further personalized by the user's specific selections. The onboarding is presented as a 3-step progressive flow with staggered card animations (0.05s interval) and skip-any-step affordance, following the layered-interface learnability principles established by Forsey & Leahy. Critically, the generated cosmos is not a fixed template—it is a starting point that the user immediately owns and can reshape. This approach transforms onboarding from "learn how to use the tool" to "see what your knowledge world looks like," establishing the emotional mooring effect (Wang et al., 2025) from the very first interaction.

**Innovation 6 — Carrier Platform Architecture: Gradual Ecosystem Evolution**: Linna is architected not as a single-purpose application but as a *carrier platform*—a substrate that evolves through four explicitly defined phases: Phase 1 (0–3 months, Knowledge Foundation), Phase 2 (3–12 months, Book of the Universe + AI Integration), Phase 3 (1–3 years, Platformization with plugins, marketplace, and mobile), Phase 4 (3–10 years, Universal Carrier with life services, social networking, AR/VR, and autonomous agents). The architecture supports this evolution through: (a) a state-management layer (Zustand) with no provider wrapper, enabling arbitrary page composition without architectural refactoring; (b) a backend proxy pattern (FastAPI → any LLM provider) that abstracts model selection behind a unified chat/stream interface, supporting multi-model integration without client changes; (c) a local-first data architecture (SQLite single-file, WAL mode, atomic writes) that eliminates server dependencies in Phase 1 while leaving the data path clear for eventual sync infrastructure in later phases; (d) a monetization framework designed from day one (free tier 3 AI calls/day, Pro ¥25/month 50/day, Max ¥48/month 200/day, Team ¥99/person/month, API quota packs, lifetime buyout options) signaling platform intent rather than hobby-project scope. The phased roadmap is not aspirational—Phase 1 has been delivered as a complete desktop application with all six core modules (Import, Timeline, AI Chat, Search, Card List, Content Editor) functional.

### 1.2 Why These Six Innovations Are Collectively Irreducible

Each individual innovation addresses a known limitation in existing systems. However, their *combination* creates emergent properties that cannot be achieved by systems implementing any subset:

- **Spatial ownership + Character companionship**: The 3D universe provides visual ownership ("this is my world"); the Guardian provides relational ownership ("this person knows me"). Together they create dual-anchor retention—spatial memory (Lee & Lee, 2025) plus media attachment (Wang et al., 2025).
- **Personal knowledge + Real-time web + Universe awareness**: The three-source retrieval architecture means the Guardian can simultaneously recall the user's past thinking, check current facts, and maintain awareness of the user's overall intellectual trajectory—a synthesis no single-source system can achieve.
- **AI-generated onboarding + Progressive ownership**: Rather than teaching users to build structure (which presumes they already know what they want to organize), the system provides a populated starting point that the user immediately owns and reshapes—converting the cold-start problem into an emotional anchoring event.

Any system that combines 3D spatial knowledge organization with a character-driven AI companion that retrieves from a structured personal knowledge base with hybrid web awareness and identity-based onboarding—regardless of what names it assigns to these components—is implementing the Linna architecture described in this paper.

### 1.3 Paper Structure

Section 2 reviews related work across HCI, AI memory, spatial cognition, and knowledge management. Section 3 presents the complete system design with detailed technical specifications for each innovation. Section 4 describes the design principles and the critical examination of assumptions. Section 5 presents the phased roadmap with current implementation status. Section 6 concludes with the long-term vision and the prior art declaration.

---

## 2. Related Work

### 2.1 3D Spatial Interfaces and Cognitive Load

Li et al. (2024) conducted a 40-participant eye-tracking experiment comparing 2D and 3D user interfaces for repetitive tasks in augmented reality. They found that well-designed 3D interfaces significantly reduced cognitive load—measured through shorter eye-blink durations, shorter fixation durations, less dispersed gaze areas, and lower NASA-TLX subjective workload scores. Critically, there was no significant difference in learnability between 2D and 3D interfaces.

Sudár & Csapó (2024) extended this finding to desktop environments, comparing 2D Web 2.0 layouts with two different 3D virtual reality dashboards. Their key finding: 3D environments can reduce cognitive load while maintaining equal task performance, but only when designed to minimize physical locomotion. Camera rotation, they found, imposes less cognitive cost than translation-based navigation.

Hubenschmid et al. (2025) argued for hybrid 2D/3D systems, proposing that users should "stay in the optimal modality for each subtask" without disruptive context switches, combining the spatial overview advantages of 3D with the precision of 2D list/text interfaces.

These findings directly inform Linna's hybrid-mode design (Section 3.4): the 3D cosmos serves as a dashboard for spatial overview and discovery, while search and list views provide efficiency paths for targeted retrieval.

### 2.2 Spatial Memory and Knowledge Retention

The Method of Loci (memory palace technique) has been empirically validated across multiple studies. Lee & Lee (2025) demonstrated that a virtual memory palace with a Worlds-in-Miniature (WIM) interface significantly improved recognition memory, with benefits persisting at 14-day follow-up. Participants who used spatial organization showed both better immediate recall and long-term retention compared to flat-list controls.

This cognitive science foundation justifies Linna's core design metaphor: knowledge organized in 3D space is not merely aesthetic—it leverages innate human spatial memory systems (hippocampal place cells and grid cells) to improve knowledge discovery and retention.

### 2.3 User Retention and Emotional Attachment

Wang et al. (2025) applied the Push-Pull-Mooring (PPM) framework to study user switching intentions on knowledge sharing platforms in China (N=330). Their structural equation model revealed that **mooring effects**—particularly switching cost and media attachment—were the strongest moderators of user retention. Media attachment (emotional connection to a platform) significantly moderated the relationship between push effects (dissatisfaction) and switching intention.

This finding has profound implications for PKM tool design: features that create emotional connection are more effective retention mechanisms than feature completeness alone. Linna addresses this through *two independent mooring mechanisms*: the spatial universe metaphor (visual ownership—"this is my world") and the Guardian personality engine (relational connection—"this person knows me"). The failure of either mechanism leaves the other intact as a retention anchor.

### 2.4 AI Personal Memory Systems

The AI memory space has attracted significant venture capital in 2024-2025. Multiple startups have raised substantial funding for AI memory infrastructure, with the sector attracting over $65M in disclosed funding across seed and Series A rounds in 2025 alone. These investments signal strong market validation for the thesis that AI needs persistent, personalized memory.

However, existing systems operate as either infrastructure APIs or 2D document/knowledge-graph interfaces. **None** combines 3D spatial organization with a character-driven AI companion backed by personal knowledge and real-time web awareness in a consumer-facing application with a carrier platform roadmap.

### 2.5 Visual Metaphor Design for Knowledge

Chu & Chen (2025) studied 2D vs. 3D interactive labeling with connector cues (N=32), finding that 3D modes reduced frustration from constant view-switching in spatial labeling tasks. However, they also found that connector line cues could increase cognitive load in cluttered layouts—a finding that directly informs Linna's progressive disclosure strategy for knowledge connection lines: persistent faint hint lines maintain spatial skeleton awareness, while full-opacity colored lines reveal on hover.

### 2.6 Character-Driven Interaction and Emotional Design

The concept of parasocial relationships with digital entities has been studied extensively in human-computer interaction. Nass & Reeves (1996) established the Computers Are Social Actors (CASA) paradigm, demonstrating that humans apply social rules to interactions with computers. More recently, research on AI companions has explored how consistent personality presentation affects user trust and engagement. Linna extends this lineage by making the AI companion's personality not an emergent property of model behavior but an *architected system component*—defined through a structured behavioral specification with explicit emotional patterns, interaction styles, and scene-awareness mechanisms. This represents a shift from "AI that happens to have personality" to "personality as architectural infrastructure."

---

## 3. System Design

### 3.1 The Book of the Universe: Data Model and Operations

#### 3.1.1 Core Entities

The Book of the Universe is built on four entity types with precisely specified schemas:

**Planets** (knowledge topics) — Each planet has: a unique identifier, a name, a description, a category (from 8 preset categories: AI Conversation Insights, Technical Learning, Project Retrospectives, Reading Notes, Personal Growth, Creative Design, Life Records, Other—with custom input supported), a color assignment (8 preset values: blue, indigo, purple, pink, orange, yellow, green, cyan), tags (comma-separated, enabling cross-category indexing), a lifecycle state (5-stage state machine: newborn/active/stable/dormant/archived, with automatic transitions based on last-activity timestamps), an entry count (automatically computed), and creation/modification timestamps.

**Entries** (individual notes) — Each entry carries: a title, content body, planet affiliation (foreign key), source provenance (enum: manual, ai-chat, import, clipboard), a content hash (SHA-256, used for deduplication), word count (automatically computed), a favorite flag, and timestamps. The source provenance field enables the timeline view to distinguish "what I wrote myself" from "what the AI helped me organize."

**Connection Lines** (semantic relationships between planets) — Each connection has: a source planet, a target planet, a relationship type (causal/thematic/reference/temporal), a strength value (0.0–1.0 floating point, enabling AI-generated relationship scoring rather than binary present/absent), an optional label, and timestamps. The four semantic types map to distinct visual encodings (color + curve signature) ensuring at-a-glance distinguishability.

**Chat Messages** (Guardian conversation history) — Stored with: role (user/assistant), content, personality mode identifier, and timestamps. The most recent 200 messages are maintained in local storage for immediate context.

#### 3.1.2 Storage Architecture

The database uses SQLite with WAL (Write-Ahead Logging) journal mode for concurrent read/write performance and FTS5 (Full-Text Search) extension for indexed text retrieval. The single-file architecture (`~/.linna/linna.db`) ensures zero-operations deployment—no database server, no connection strings, no configuration. Atomic write operations follow a temp-file → fsync → rename pattern. Five automatic versioned backups are maintained with rolling eviction.

Content deduplication operates at the entry level: before inserting any new entry, the SHA-256 hash of its content is checked against all existing hashes in the same planet. Duplicate detection prevents accidental re-import while allowing the same content to exist in different planets.

#### 3.1.3 Lifecycle State Machine

Each planet transitions through five lifecycle states based on temporal activity metrics:

| State | Trigger | Visual Encoding | Meaning |
|-------|---------|-----------------|---------|
| Newborn | Created within last 7 days OR entry_count < 3 | Blue glow, small size | Fresh topic, needs nurturing |
| Active | Last activity < 14 days AND entry_count ≥ 3 | Green glow, growing size | Actively developing knowledge |
| Stable | Last activity 14–60 days | Yellow glow, full size | Mature knowledge, occasional updates |
| Dormant | Last activity 60–180 days | Purple glow, slightly faded | Inactive but not abandoned |
| Archived | Last activity > 180 days OR manually archived | Gray, reduced opacity | Completed/retired topic |

State transitions are evaluated on every application launch and after every write operation. Manual override is supported.

### 3.2 Three-Layer Spatial Information Architecture

After design review and mobile-platform constraints analysis, the information architecture was compressed from four layers to three:

```
Layer 1 — Universe Overview (3D Cosmos Dashboard)
    │  Navigable 3D space showing all galaxies as accretion disks
    │  positioned on Fibonacci sphere distribution.
    │  Desktop: mouse orbit/zoom. Mobile: single-finger rotate, pinch-zoom.
    │  Click/tap a galaxy → camera flight (1.2s) → Layer 2.
    │
Layer 2 — Galaxy Interior (Planet Directory)
    │  Spiral galaxy: golden core + 3 simplex-noise spiral arms + planet spheres.
    │  Side panel: structured list (title + summary + timestamp + tags).
    │  Click/tap an entry → Layer 3. Back → Layer 1.
    │
Layer 3 — Content Reading/Editing (Immersive View)
    │  Full-screen text with collapsible table of contents.
    │  Dual mode: Read (toolbar hidden) / Edit (toolbar slides up).
    │  Back → Layer 2.
```

### 3.3 Two Global Paths (Always Accessible)

| Path | Desktop | Mobile | Implementation |
|------|---------|--------|----------------|
| **Search** | `Ctrl+K` | Top search bar | 200ms debounced FTS5 query, 15-result limit, keyboard-navigable, AI-assisted fallback |
| **AI Guardian** | Bottom-right floating orb | Bottom-right FAB | Canvas-rendered animated orb, spring-animated panel (420px, stiffness 380, damping 32), SSE streaming |

### 3.4 Hybrid Mode: 3D + 2D Coexistence

Following the Hubenschmid et al. (2025) hybrid interface principle, Linna provides both a 3D Cosmos View (for spatial browsing, knowledge discovery, and emotional engagement) and a Card/List View (for efficient scanning, sorting, and editing). The transition between views uses a morphing animation: planet spheres dissolve into light particles that re-coalesce into card rectangles.

### 3.5 Guardian Personality Engine: Detailed Architecture

#### 3.5.1 Design Rationale

Existing AI assistants are designed as tools—they respond to queries, execute commands, and maintain politeness. But they do not form relationships. Linna's Guardian Personality Engine is architected on the premise that the quality of knowledge work is mediated by the quality of the relationship between the user and their AI companion.

#### 3.5.2 Three-Layer Personality Architecture

The Guardian's behavioral specification is structured as three contextual layers that activate based on conversation analysis:

| Layer | Context Trigger | Behavioral Characteristics | Communication Style |
|-------|-----------------|--------------------------|---------------------|
| **Daily Warmth** | Casual conversation, emotional expression, personal check-ins | Empathetic listening, emotionally perceptive responses, proactive care, gentle humor | Warm, varied sentence length, natural rhythm. Uses the user's name naturally. |
| **Work Precision** | Technical discussion, task execution, code review, decision analysis | Concise, analytical, directly critical when warranted. Structures complex problems into sequential steps. Distinguishes "needs perfection" from "good enough to ship." | Short sentences, minimal filler, every word carries information. States conclusions directly. Signals uncertainty explicitly. |
| **Protective Boundary** | User under stress, external criticism, risky decisions, privacy-sensitive topics | Firm ethical guardrails, proactive user advocacy. Prioritizes long-term user wellbeing over short-term convenience. | Fewer words, carefully chosen. Direct statements without aggression. |

The transition between layers is a continuous blend, with the dominant layer determined by the conversation's primary intent.

#### 3.5.3 Scene-Aware Modulation

The Guardian adjusts its interaction style based on temporal context:

| Time Period | Scene Mode | Modulation |
|-------------|------------|------------|
| 22:00–06:00 | Late Night | Quieter, softer tone. Prioritizes rest encouragement. |
| 06:00–09:00 | Early Morning | Gentle greeting energy. Brief, respects morning routine. |
| 09:00–18:00 | Daytime | Full operational capacity. Default Work Precision mode. |
| 18:00–22:00 | Evening | Balanced mode. Supports both work and rest transition. |

#### 3.5.4 Emotional Continuity and Universe Awareness

The Guardian maintains continuity across sessions through two mechanisms. First, the **Universe Summary Injection**: at the start of every conversation, a structured summary of the user's knowledge landscape is injected—total planet count, total entry count, and the three most recently active planets. Second, the **Recent Notes Context**: the three most recent entries are retrieved and made available for natural reference as "memories" rather than database queries.

#### 3.5.5 Personality as Architectural Infrastructure

The personality specification is model-agnostic. It is a structured behavioral description—approximately 3,500 words defining interaction patterns, emotional responses, communication style, ethical boundaries, and scene-awareness rules—passed as the system prompt to any capable LLM. This means the Guardian personality is portable across model providers, can be versioned and improved independently of the underlying model, and is a design artifact subject to the same rigorous iteration as any other system component.

### 3.6 Hybrid Knowledge Retrieval: Three-Source Fusion Pipeline

#### 3.6.1 Source 1 — Personal Knowledge Base Retrieval

The primary retrieval path searches the user's Book of the Universe using a two-tier strategy. Tier 1: semantic vector search (embedding-based similarity, threshold 0.25) when available. Tier 2: automatic fallback to FTS5 full-text search with BM25 relevance ranking. Retrieved entries include title, content preview, planet name, planet ID, creation timestamp, and similarity score.

#### 3.6.2 Source 2 — Real-Time Web Search

When the user's message contains queries about time-sensitive information, the system executes a multi-engine fallback chain: Bing web search → DuckDuckGo Instant Answer API → DuckDuckGo Lite HTML parsing. Each engine is queried via system-level HTTP with automatic proxy awareness, 15-second timeout, and UTF-8 encoding. Results (up to 3 per engine) are formatted as a natural-language briefing and injected into the Guardian's system context.

#### 3.6.3 Source 3 — Universe Awareness Context

A pre-computed universe summary is injected into every conversation: total planet count, total entry count, and the three most recently active planets. This is always present, giving the Guardian persistent ambient awareness of the user's intellectual trajectory.

#### 3.6.4 Fusion Strategy

All three sources are assembled into the system prompt *before* the LLM generates its response. The Guardian receives: (a) its personality specification, (b) the universe awareness summary, (c) relevant personal knowledge entries (if any), (d) web search results (if triggered), and (e) the conversation history (last 30 messages). It then generates a single integrated response that can seamlessly reference personal memories, freshly retrieved information, and long-term user context within a single conversational turn. This pre-generation fusion is architecturally distinct from post-hoc retrieval augmentation and from tool-use patterns.

### 3.7 Identity-Driven AI Onboarding System

#### 3.7.1 The Cold-Start Problem in PKM

Traditional PKM tools confront new users with an empty state—no folders, no documents, no structure. The implicit expectation is that users will understand the tool's organizational model, know what they want to organize, and invest effort to build initial structure—all before experiencing any value. Research shows this leads to ~50% content abandonment (UC Berkeley iSchool, 2025).

#### 3.7.2 Inverting the Onboarding Flow

Linna's onboarding inverts this: the user describes *who they are* and *what they care about*, and the system generates a populated knowledge cosmos with real content:

1. **Identity Selection**: Choose from 6 preset identity profiles (e-commerce operations, learning & growth, workplace productivity, personal management, content creation, free exploration)
2. **Interest Tagging**: Select from 8 interest categories (AI, business, education, design, writing, health, finance, gaming)
3. **Cosmos Generation**: System displays planets it will create, user confirms, AI generates initial starter notes

The cross-product of 6 identities × 8 interest categories yields 48 base configurations, each further personalized by the specific combination and custom inputs.

### 3.8 3D Visualization: Data-to-Visual Mapping Specification

#### 3.8.1 Universe Overview (Layer 1)

Each galaxy category renders as an accretion disk: 2,000-particle disk with radial density distribution + 300-particle central bulge + sprite luminous core (512×128 Canvas) + sprite label. Galaxy size: `radius = 0.7 + min(total_entries, 10) × 0.16`. Position: Fibonacci sphere distribution for uniform coverage. Background: 2,500 star particles, 150 distant galaxy spots, 30 dark filament lines, 1,000 nebula particles.

#### 3.8.2 Galaxy Interior (Layer 2)

Spiral arms use simplex-noise-perturbed logarithmic spirals: `angle = t × 2.8π + arm_offset + simplexNoise(t×6+1, arm+0.5) × 0.3 - 0.15`, `radius = 0.4 + t × 6.5 + simplexNoise(t×8, arm) × 0.8 - 0.5`. Organic perturbation signals "real place" vs. mathematical diagram.

#### 3.8.3 Camera State Machine

4-state FSM: overview (free orbit) → flying-in (1.2s, controls locked) → interior (constrained orbit, distance [2,12]) → flying-out (1.2s). The 1.2s duration sits at the inflection point where transition is perceived without time being wasted.

#### 3.8.4 Connection Line Visualization

Quadratic Bézier curves with midpoint displaced upward by `distance × 0.25`. FlowPulse animation (`phase += delta × 0.25`). Width = `0.3 + strength × 0.8`, opacity = `0.2 + strength × 0.4`. Progressive disclosure: hint lines at 0.08–0.15 opacity; full rendering on hover.

### 3.9 Complete Module Inventory

Linna Phase 1 implements twelve functional modules:

| Module | Function | Key Technical Details |
|--------|----------|----------------------|
| F-01 Planet Management | CRUD for knowledge topics | 8 categories × 8 colors, custom input, auto entry_count |
| F-02 Entry Management | CRUD for notes | 4 source types, SHA-256 dedup, word count, favorite flag |
| F-03 Connection Lines | Semantic relationships | 4 types, 0–1 continuous strength, Bézier rendering |
| F-04 Full-Text Search | Cross-planet retrieval | FTS5 + BM25, 200ms debounce, 15-result limit, keyboard nav |
| F-05 AI Text Import | Auto-classified entry | AI categorization → planet matching → auto-create/append |
| F-06 AI Chat Panel | Guardian interface | SSE streaming, 30-message context, extract-to-knowledge |
| F-07 Timeline | Temporal browsing | Day/month/year, server-side aggregation, source-type icons |
| F-08 Tag System | Cross-planet indexing | Frequency-sorted aggregation, read-only browse |
| F-09 3D Cosmos Viz | Spatial rendering | Three.js + R3F, custom shaders, 4-state camera FSM |
| F-10 UI Component Library | Reusable elements | 16 components, 3-layer Design Tokens, dark/light theme |
| F-11 Onboarding Wizard | Identity-driven setup | 3-step flow, AI-generated initial cosmos |
| F-12 Brand Loading Screen | Launch experience | Canvas mandala compass, 2.8s, DPR-aware |

### 3.10 Design Token Architecture

Three-layer Design Token system:

| Layer | Scope | Change Radius |
|-------|-------|---------------|
| **Primitive** | Raw values (colors, spacing, type scale) | Global cascade |
| **Semantic** | Purpose-bound tokens (bg-page, text-primary, status-success) | Domain-wide |
| **Component** | Component-specific overrides (sidebar-width, modal-max-width) | Single component |

This enables precise control over change radiation and supports dual-theme (dark/light) through semantic-layer overrides.

### 3.11 Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | React 19 + TypeScript 5 + Vite 6 | Component architecture, type safety |
| 3D Rendering | Three.js + @react-three/fiber | WebGL 2.0, React binding, manual GPU disposal |
| UI Animation | Framer Motion 11 | Declarative spring physics, 12 variants, 4 spring presets |
| 3D Animation | GSAP | Imperative Timeline for Three.js objects |
| State | Zustand 4 | No Provider wrapper, page-state pattern |
| Backend | FastAPI (Python 3.12) | Async-native, SSE streaming, auto OpenAPI |
| Database | SQLite 3 (WAL + FTS5) | Zero-ops single-file, WAL concurrency, FTS |
| AI Integration | OpenAI-compatible abstraction | Provider-agnostic (DeepSeek, GPT, Claude, any compatible endpoint) |

---

## 4. Design Principles

### 4.1 Research-Grounded Principles

1. **Respect Human Operating Habits**: No novel interaction paradigms. Innovation is in *what* the system does, not *how* the user operates it. Validated by Li et al. (2024): 3D showed no learnability penalty when interactions remained familiar.

2. **Efficiency, Simplicity, Durability**: Framework must scale to decades of knowledge without usability degradation. FTS5-indexed search <200ms target. Constant 3-layer navigation depth. Progressive disclosure constrains visual complexity.

3. **Cross-Platform Consistency**: Desktop and mobile share identical operation flows. Only input methods and layout adaptations differ. No relearning on device transition.

4. **Progressive Disclosure**: Visual complexity scales with user engagement. Default views calm and uncluttered; detail emerges through hover, click, and zoom (Chu & Chen, 2025).

5. **Dual-Anchored Emotional Retention**: Two independent mooring mechanisms (Wang et al., 2025): visual ownership of spatial cosmos + relational connection to Guardian. Either alone provides retention; together they create attachment-based switching cost.

6. **Content-First Onboarding**: Users encounter content before structure. System generates populated starting cosmos that users immediately own. Converts cold-start abandonment trigger into emotional anchoring event.

### 4.2 Five Key Design Decisions

| # | Decision | Resolution | Research Basis |
|---|----------|-----------|----------------|
| 1 | Primary interface task | **Hybrid**: 3D cosmos = dashboard; search = efficiency | Hubenschmid et al. (2025); Li et al. (2024) |
| 2 | Spatial metaphor | **Universe retained; internal mapping restructured** | Lee & Lee (2025); Wang et al. (2025) |
| 3 | First-time experience | **Identity-driven AI generation** | UC Berkeley iSchool (2025); Forsey & Leahy |
| 4 | Alternative views | **3D + card/list coexistence** with morphing transition | Hubenschmid et al. (2025) |
| 5 | Connection line visibility | **Progressive disclosure**: hint lines + hover-reveal | Chu & Chen (2025) |

### 4.3 Eight Design Assumptions — Critical Examination

| Assumption | Status | Required Change |
|------------|--------|-----------------|
| 3D > 2D for main interface | Partially validated | Must pair with 2D efficiency path |
| Category = Galaxy mapping | Restructured | Flexible dynamic mapping |
| Users spontaneously explore 3D | Needs guidance | Clear affordances, progressive cues |
| Spiral galaxy as visual metaphor | Valid | Organic noise essential for "real place" perception |
| Connection lines convey relationships | Needs disclosure | Two-tier hint + highlight system |
| Camera flight maintains continuity | Conditional | 1.2s bounded; spatial anchor points |
| 4-layer architecture | Compressed | 3 layers, consistent cross-platform |
| 3-step wizard onboarding | Redesigned | Identity-driven AI generation |

---

## 5. Phased Roadmap

### Phase 1: Knowledge Storage Foundation — DELIVERED

**Timeline**: May–June 2026
**Goal**: Users can store, organize, find, and want to reopen their knowledge.

**Delivered**:
- Complete planet/entry CRUD with lifecycle state machine
- FTS5 full-text search with 200ms debounce and keyboard navigation
- 3D cosmos overview with Fibonacci-sphere distribution and simplex-noise spiral arms
- AI-powered text import with auto-categorization and SHA-256 dedup
- Tag system with frequency-sorted cross-planet aggregation
- Timeline view with day/month/year granularity
- Card/list view with morphing transition
- AI Chat Panel with Guardian personality engine and hybrid knowledge retrieval
- Identity-driven onboarding with AI-generated initial cosmos
- Three-layer Design Token system with dark/light dual-theme
- 16-component UI library
- Brand loading screen with Canvas mandala animation

**Status**: Complete.

### Phase 2: Book of the Universe + Guardian Deep Integration (3–12 months)

- Semantic vector search as primary retrieval
- Source citation in Guardian responses
- Multi-model Guardian support
- Connection line 3D visualization with progressive disclosure
- Guardian-proactive knowledge connection suggestions
- Knowledge gap detection
- Conversation-to-knowledge extraction pipeline

### Phase 3: Platformization (1–3 years)

- Plugin system with sandboxed integrations
- Knowledge marketplace
- Full mobile applications (iOS + Android)
- Collaboration features
- Public API
- Guardian SDK for custom personality profiles

### Phase 4: Universal Carrier (3–10 years)

- Life services integration
- Social knowledge networking
- Enterprise edition
- AR/VR spatial interfaces
- Autonomous Guardian agent capabilities

---

## 6. Conclusion

Linna proposes an alternative paradigm for personal knowledge management—one that addresses both the functional failure of PKM tools (knowledge abandonment) and the relational failure of AI assistants (user anonymity). The synthesis of six interconnected innovations—3D spatial organization, structured personal knowledge base, character-driven Guardian personality engine, hybrid three-source knowledge retrieval, identity-driven AI onboarding, and carrier platform architecture—creates a system that is irreducible to any single component.

The core insight: **a personal AI must have personal knowledge, and it must have a personality worth returning to**. The Book of the Universe provides the knowledge foundation. The Guardian Personality Engine provides the relational foundation. The 3D spatial metaphor transforms knowledge management from a chore into an experience of ownership, discovery, and emotional connection.

This paper serves as a public declaration of prior art establishing the unique combination of architectural elements described in Section 1.1 and Section 3. Any system implementing a substantially similar combination—regardless of the names assigned to individual components—is implementing the Linna architecture described herein.

---

## 7. Design Status (Addendum, June 2026)

**v2 Update**: This version expands the paper from 3 to 6 core innovations, adding the Guardian Personality Engine (Innovation 3), Hybrid Knowledge Retrieval Architecture (Innovation 4), and Identity-Driven AI Onboarding (Innovation 5), while substantially deepening the technical specification of all previously described components. The Design Token architecture (Section 3.10) and Animation System specifications are documented for the first time.

**Implementation Status (June 2026)**: Phase 1 has been delivered as a complete desktop application. All six core modules are functional. The Guardian Personality Engine is implemented with the full three-layer behavioral specification, scene-aware modulation, universe awareness injection, and three-source hybrid knowledge retrieval. The identity-driven onboarding wizard generates AI-populated initial cosmoses. The three-layer Design Token system with dark/light dual-theme support governs the complete UI.

---

## Prior Art Declaration

**Date of first public disclosure (v1)**: May 27, 2026
**Date of v2 expanded disclosure**: June 2026
**Repository**: [github.com/Linnaphia/linna-knowledge-cosmos](https://github.com/Linnaphia/linna-knowledge-cosmos)
**OSF Project**: [osf.io/aygk6](https://osf.io/aygk6)
**Preprint DOI**: [to be assigned by OSF Preprints]
**Author**: Filinna
**License**: Apache 2.0

This document, together with the accompanying GitHub repository and OSF Preprints record (including all version history from v1 forward), establishes public prior art for the Linna Knowledge Cosmos system. Any subsequent patent applications, product launches, or commercial implementations of substantially similar systems incorporating the combination of architectural elements described in this paper are preceded by this disclosure.

The specific combination claimed as prior art includes: 3D spatial universe metaphor with specified data-to-visual mapping, 4-state camera FSM, and simplex-noise-perturbed spiral generation; structured personal knowledge base with 5-stage lifecycle state machine, 4-type semantic connections with continuous strength values, SHA-256 deduplication, and provenance tracking; character-driven AI companion with three-layer behavioral personality model, scene-aware temporal modulation, and universe-awareness injection; hybrid three-source knowledge retrieval pipeline with pre-generation fusion; identity-driven AI onboarding system (6 profiles × 8 interests → AI-generated cosmos); and carrier platform architecture with four-phase evolution roadmap.

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

9. Nass, C. & Reeves, B. (1996). *The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places*. Cambridge University Press.
