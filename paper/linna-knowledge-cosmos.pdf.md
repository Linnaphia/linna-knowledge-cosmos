# Linna: A Personal Knowledge Cosmos — 3D Spatial Knowledge Organization with Character-Driven AI Memory

**Filinna** 
*May 27, 2026 (v1) · Expanded June 2026 (v2)*

---

## Abstract

Current AI assistants suffer from a fundamental limitation: they do not remember their users. Each conversation begins from zero, requiring users to re-establish context and re-explain their background. Meanwhile, personal knowledge management tools remain rooted in flat document-folder paradigms that fail to reflect how human memory actually works—spatially, associatively, and emotionally. This paper presents **Linna**, a personal knowledge management system built around seven interconnected innovations: (1) a 3D spatial universe as the organizing metaphor for personal knowledge, leveraging innate human spatial cognition; (2) the *Book of the Universe*, a structured personal knowledge base that serves as the sole source of truth for AI responses; (3) a **Guardian Personality Engine** that replaces generic AI interaction with a character-driven companion exhibiting emotional continuity, scene awareness, and a three-layer personality architecture; (4) a **Hybrid Knowledge Retrieval Architecture** that fuses personal knowledge retrieval, real-time web search, and universe-wide contextual awareness into a unified response pipeline; (5) an **Identity-Driven AI Onboarding System** that replaces empty-state tutorials with AI-generated personalized initial knowledge structures; (6) a **Carrier Platform Architecture** designed for gradual evolution from personal tool to comprehensive ecosystem; and (7) the **World Tree Temporal Visualization**, a fractal tree structure formed entirely from luminous threads that maps knowledge across the time dimension—warm gold base threads forming the complete tree skeleton, cool-colored knowledge threads layering atop as the user adds knowledge, with a breakthrough zoom animation revealing deeper fractal hierarchy levels. We describe the complete system architecture, the design specification (10 Rams-inspired principles including a material ban), the Guardian personality engine with emotional continuity and scene awareness, the AI three-channel access architecture (bring-your-own-key, built-in quota, daily free tier) with a 9-layer payment security model, the communication and interpersonal data engine, the voice interaction layer, the full data layer (9 tables with FTS5 triggers, audit logging, and undo stack), the 3D optimization strategy with known issues and LOD planning, the brand architecture and IP timeline, the content dissemination strategy across 5 platforms, the testing and quality framework, and the long-term phased roadmap. This paper serves as a public declaration of prior art establishing the unique combination of 3D spatial cognition, character-driven AI companionship, temporal knowledge visualization, personal knowledge-driven intelligence, and platform carrier architecture.

---

## 1. Introduction

The year is 2026. Large language models have become ubiquitous. Yet every AI conversation remains fundamentally anonymous—the AI does not know who you are, what you know, or what you have previously discussed. This is not a technical limitation; it is a design choice. Mainstream AI assistants are optimized for general-purpose question answering, not for building a persistent model of an individual user's knowledge, preferences, and intellectual history.

Meanwhile, personal knowledge management (PKM) has become a thriving category. A variety of tools help users capture and organize information. However, research shows that approximately 50% of saved content is never reopened (UC Berkeley iSchool, 2025). The problem is not capture—it is retrieval, relevance, and emotional connection.

**Linna** proposes a unified solution that addresses both failures simultaneously. First, every piece of saved information becomes part of a navigable 3D spatial universe, transforming knowledge management from a clerical task into an experience of ownership and discovery. Second, an AI companion—not a generic chatbot but a character with persistent personality, emotional continuity, and genuine awareness of the user's knowledge landscape—answers questions by drawing from this personal knowledge base. Third, knowledge is visualized not only in space (3D cosmos) but also in time (World Tree), providing dual-axis orientation: what I know, and how my knowledge has grown. The result is not merely a tool that stores information, but a companion that genuinely knows its user, and a living map of intellectual growth.

### 1.1 Architectural Boundaries: What Linna Is Not

To understand what Linna is, it is essential to understand what it is *not*. The AI and knowledge management landscape of 2025–2026 contains several categories of systems that appear adjacent to Linna but differ in fundamental architectural ways. This section establishes clear boundaries—not by naming specific products, but by describing the architectural distinctions that make Linna categorically different from any existing approach.

#### 1.1.1 Not a Passive Screen Recorder

A prominent category of "AI memory" tools operates by periodically capturing screenshots of the user's screen, performing OCR and semantic embedding on the captured images, and providing a searchable timeline of past activity. These systems answer the question: *"What was on my screen last Tuesday?"*

Linna does not record the user's screen. It does not capture ambient activity. It is not a surveillance tool. The Book of the Universe is **actively constructed** by the user—every planet, entry, and connection is the result of a deliberate act: writing a note, importing a document, extracting from an AI conversation, or accepting an AI-generated suggestion. The user is not being recorded; they are **building**. This is the difference between a security camera and a library. A screen recorder captures everything indiscriminately; Linna captures only what the user chooses to preserve, organized in a spatial structure that the user shapes.

**Architectural distinction**: Passive recorders have no knowledge model—they store pixels with timestamps. Linna has a structured data model (Planets → Entries → Connection Lines) with semantic types, lifecycle states, provenance tracking, and content-addressable deduplication. A passive recorder can tell you what you saw; Linna can tell you what you know, how it connects, and where your knowledge is growing or stagnating.

#### 1.1.2 Not an AI Memory API or Middleware Layer

A growing category of "AI memory" infrastructure provides memory-as-a-service: vector databases, MCP (Model Context Protocol) servers, and API layers that give large language models access to stored context across sessions. These systems answer the question: *"How can multiple AI tools share a common memory of the user?"*

Linna is not infrastructure for other AI tools. It is a **consumer-facing application** where the Guardian *is* the interface. The Guardian does not sit behind other AI assistants providing them with memory—the Guardian is the assistant. The personality engine, the three-source retrieval pipeline, the universe awareness injection, and the behavioral specification all converge in a single character that the user talks to directly. Linna is not a memory layer for other AI tools; it is a complete alternative where the AI companion has its own identity, its own relationship with the user, and its own knowledge foundation.

**Architectural distinction**: Memory middleware provides a stateless retrieval API—"here are relevant documents for this query." Linna provides a *stateful character*—the Guardian maintains emotional continuity across sessions, adjusts its interaction style based on time of day and conversation trajectory, and speaks with awareness of the user's long-term intellectual development. A memory API returns search results; a Guardian says "I remember you were working on this three months ago—how did it turn out?"

#### 1.1.3 Not a Document Q&A Chatbot

Several AI tools allow users to upload documents and ask questions about them, using Retrieval-Augmented Generation (RAG) to ground responses in the provided materials. These systems answer the question: *"What does this document say about X?"*

Linna is not a document Q&A interface. While the Guardian does retrieve from the Book of the Universe, the retrieval is only one of three knowledge sources (alongside real-time web search and universe-wide contextual awareness). More importantly, the Guardian's role is not to answer document questions—it is to **accompany the user's intellectual journey**. The Guardian proactively notices knowledge gaps, suggests connections between planets, and maintains awareness of the user's evolving interests over months and years. A document chatbot answers a question and forgets the conversation; the Guardian remembers, follows up, and grows with the user.

**Architectural distinction**: Document Q&A systems have no personality architecture, no emotional continuity, no knowledge lifecycle tracking, and no spatial organization. They are retrieval engines with a chat interface. Linna is a companion system with retrieval capabilities. The difference is not technical capability—it is architectural intent. One is designed to answer questions about documents. The other is designed to build a relationship around knowledge.

#### 1.1.4 Not a 2D Knowledge Graph or Mind Map

Tools for visualizing knowledge as 2D node-and-edge graphs have existed for decades. These systems represent knowledge topics as labeled circles connected by lines on a flat canvas, answering the question: *"How are these ideas connected?"*

Linna's 3D spatial universe is not a 2D graph with an extra dimension added for decoration. The third dimension is **information-bearing**: distance from the galactic core encodes content density (more notes = further out on the spiral arm), planet size encodes entry count, luminosity and color encode lifecycle state, and the Fibonacci sphere distribution of galaxies ensures uniform spatial coverage rather than the hairball clustering typical of force-directed 2D graphs. Furthermore, the camera state machine (4-state FSM with bounded 1.2s flight duration) creates a **navigational experience**—the user moves through knowledge space rather than looking at it from above. A 2D graph is a map you look at; the 3D cosmos is a place you enter.

**Architectural distinction**: 2D knowledge graphs use position only for layout (typically force-directed, with no semantic meaning). Linna's 3D space uses position, size, color, luminosity, particle density, and animation state to encode six simultaneous data dimensions. The organic simplex-noise perturbation of spiral arms is specifically designed to trigger "real place" perception rather than "diagram" perception—an effect that 2D graphs cannot achieve because their visual language is inherently abstract.

#### 1.1.5 The Linna Difference: Seven Simultaneous Properties

The four categories above each implement *one* of Linna's properties in isolation: passive recorders capture activity, memory middleware stores context, document chatbots retrieve information, and knowledge graphs visualize connections. No existing system combines all of the following seven properties simultaneously—and it is the *combination*, not any individual property, that defines the Linna architecture:

1. **Spatial ownership**: Knowledge is organized in a navigable 3D cosmos that the user owns and shapes (not a flat list, not a 2D graph, not a screenshot timeline)
2. **Structured knowledge model**: Data is organized as Planets → Entries → Connection Lines with lifecycle states, semantic types, provenance tracking, and content-addressable deduplication (not unstructured pixels, not vector embeddings alone, not flat documents)
3. **Character-driven companionship**: The Guardian has a three-layer personality architecture, emotional continuity, and scene awareness—it is a character the user has a relationship with (not a query interface, not an API endpoint, not a mascot)
4. **Hybrid retrieval with pre-generation fusion**: Personal knowledge + real-time web search + universe awareness are fused *before* the LLM generates its response (not post-hoc RAG, not single-source retrieval, not tool-use search patterns)
5. **Content-first onboarding**: The user describes their identity and interests; AI generates a populated initial cosmos (not an empty canvas tutorial, not a folder creation wizard, not a sample document)
6. **Carrier platform trajectory**: The architecture supports evolution from personal tool → extensible platform → comprehensive ecosystem across four explicitly defined phases (not a single-purpose tool with no growth path)
7. **Dual-axis knowledge visualization**: Knowledge is organized simultaneously in space (3D cosmos for domain overview) and time (World Tree for growth trajectory), providing two complementary visual metaphors—the cosmos answers "what do I know"; the tree answers "how has my knowledge grown" (not space-only or time-only visualization)

A system that implements any subset of these properties is not Linna. A system that implements all seven—regardless of what names it assigns to planets, guardians, trees, or cosmic metaphors—is implementing the architecture described in this paper.

### 1.2 Seven Core Innovations

Linna combines seven innovations that, to our knowledge, have not been combined before in a single system. Each innovation is described with sufficient technical specificity that functional equivalence would constitute derivation:

**Innovation 1 — 3D Spatial Universe as Organizing Metaphor**: Knowledge is organized as planets, galaxies, and constellations in a navigable 3D cosmos with a precisely specified data-to-visual mapping: planet size = `0.7 + min(entry_count, 10) × 0.16`, planet position by Fibonacci sphere distribution for uniform coverage, color by 8-value semantic palette, and lifecycle-driven luminosity (5 stages: newborn → active → stable → dormant → archived). The spatial layout is not decorative—it directly encodes knowledge state information that is recoverable at a glance. Camera navigation follows a 4-state finite state machine (overview → flying-in → interior → flying-out) with 1.2-second bounded flight duration informed by spatial continuity research (Sudár & Csapó, 2024). The galaxy interior uses simplex-noise-perturbed logarithmic spiral arm generation rather than pure mathematical spirals, producing organic irregularity that subconsciously signals "this is a real place" rather than a diagram. This innovation leverages the Method of Loci effect validated by Lee & Lee (2025): spatial organization improves 14-day memory retention compared to flat-list controls.

**Innovation 2 — The Book of the Universe: Structured Personal Knowledge Base**: A local-first knowledge repository with a specific data model: Planets (knowledge topics) → Entries (individual notes) → Connection Lines (typed semantic relationships). Each entry carries immutable provenance metadata (source: manual/AI-conversation/import/clipboard), content hash (SHA-256 for deduplication), and timestamps. Planets maintain a 5-stage lifecycle state machine with automatic state transitions based on recency of activity. Connection lines carry four precisely defined semantic types—causal (red), thematic (cyan), reference (yellow), temporal (purple)—with continuous strength values (0–1 floating point) rather than discrete categories, enabling AI-generated relationship scoring. The database uses SQLite with WAL mode and FTS5 full-text search for zero-operations deployment while maintaining ACID guarantees. Atomic write operations (temp file → fsync → atomic rename) ensure data integrity. The full schema comprises 9 tables including undo stack for operation reversal and audit logging via timestamped state tracking. This structure is not a generic "knowledge graph"—the specific combination of 5-stage lifecycle + 4-type semantic connections + provenance tracking + content-addressable deduplication + undo/audit mechanisms constitutes a unique architecture.

**Innovation 3 — Guardian Personality Engine: Character-Driven AI Companionship**: Linna introduces a *personality engine architecture* that transforms AI interaction from generic utility into character-driven companionship. The engine has four architectural layers: (a) a **three-layer personality model**—daily warmth (empathetic, caring, emotionally perceptive), work precision (concise, analytical, decisively critical when needed), and protective boundary (firm ethical guardrails, user advocacy)—each layer activating contextually based on conversation analysis; (b) **scene-aware behavior modulation** that adjusts interaction style based on time of day (early morning / daytime / evening / late night) and conversation trajectory; (c) **emotional continuity** across sessions, where the Guardian references prior conversations and the user's evolving knowledge state without requiring re-introduction; and (d) a **universe-awareness mechanism** that injects the user's knowledge landscape summary (planet count, entry count, recently active domains) into the conversation context, enabling the Guardian to speak with genuine awareness of "what the user has been thinking about." The personality is defined through a structured behavioral specification—not hardcoded rules but a comprehensive description of interaction patterns, emotional responses, and communication style (~3,500 words). This specification is model-agnostic: any capable LLM can adopt the Guardian role by processing the personality definition as its system context. The Guardian also provides a **daily briefing** feature—a morning summary of the user's knowledge universe changes over the past 24 hours, delivered as a natural-language card with new planet/entry counts, most active domain, and a randomly selected highlight from recent notes.

**Innovation 4 — Hybrid Knowledge Retrieval Architecture: Three-Source Fusion**: The Guardian's knowledge retrieval operates through a three-source fusion pipeline, not a single RAG endpoint. **Source 1 — Personal Knowledge Base**: semantic search (vector embedding similarity, threshold 0.25) with automatic FTS5 full-text search fallback when semantic infrastructure is unavailable, retrieving contextually relevant notes with planet attribution. **Source 2 — Real-Time Web Search**: multi-engine fallback chain (Bing → DuckDuckGo → DuckDuckGo Lite) via system-level HTTP with proxy awareness, returning time-sensitive information that the Guardian relays in natural conversational form with explicit source URLs. **Source 3 — Universe Awareness Summary**: a pre-computed snapshot of the user's entire knowledge landscape (total planet/entry counts, recently active domains) injected into every conversation, giving the Guardian persistent awareness of the user's intellectual trajectory. The fusion is not post-hoc: all three sources are injected into the system prompt *before* the LLM generates its response, enabling integrated reasoning across personal knowledge, fresh information, and long-term user context. Critically, the Guardian is instructed to cite personal knowledge with natural recall language (e.g., "I remember you wrote about...") rather than mechanical retrieval markers, and to present web-sourced information as personally verified ("I checked, and currently...") rather than delegating to the user.

**Innovation 5 — Identity-Driven AI Onboarding: From Empty State to Personal Cosmos**: Traditional PKM tools confront new users with an empty canvas—the "cold start" problem that research shows leads to ~50% content abandonment. Linna's onboarding inverts this: instead of teaching the user how to create structure, the system asks two lightweight questions (identity profile from 6 presets + interest domains from 8 categories), then **AI-generates a complete initial cosmos**—planets populated with starter notes, categorized into galaxies, with suggested connection lines. The 6 identity profiles (e-commerce operations, learning & growth, workplace productivity, personal management, content creation, free exploration) and 8 interest categories (AI, business, education, design, writing, health, finance, gaming) produce a cross-product of 48 initial configurations, each further personalized by the user's specific selections. The onboarding is presented as a 3-step progressive flow with staggered card animations (staggered interval) and skip-any-step affordance, following the layered-interface learnability principles established by Forsey & Leahy. The generated cosmos is not a fixed template—it is a starting point that the user immediately owns and can reshape.

**Innovation 6 — Carrier Platform Architecture: Gradual Ecosystem Evolution**: Linna is architected not as a single-purpose application but as a *carrier platform*—a substrate that evolves through four explicitly defined phases: Phase 1 (0–3 months, Knowledge Foundation), Phase 2 (3–12 months, Book of the Universe + AI Integration), Phase 3 (1–3 years, Platformization with plugins, marketplace, and mobile), Phase 4 (3–10 years, Universal Carrier with life services, social networking, AR/VR, and autonomous agents). The architecture supports this evolution through: (a) a state-management layer (Zustand) with no provider wrapper, enabling arbitrary page composition without architectural refactoring; (b) a backend proxy pattern (FastAPI → any LLM provider) that abstracts model selection behind a unified chat/stream interface; (c) a local-first data architecture (SQLite single-file, WAL mode, atomic writes) that eliminates server dependencies in Phase 1 while leaving the data path clear for eventual sync infrastructure; (d) an AI three-channel access architecture—bring-your-own-key (zero compliance burden), built-in quota (curated provider), and daily free tier—that lets users choose their level of provider integration without locking them into any single model; and (e) a monetization framework designed from day one (free tier 3 AI calls/day, Pro ¥25/month 50/day, Max ¥48/month 200/day, Team ¥99/person/month, API quota packs, lifetime buyout options) with hard separation between local and AI operations ensuring subscription cessation never blocks data access.

**Innovation 7 — World Tree: Temporal Knowledge Visualization with Fractal Thread Structure**: While the 3D cosmos organizes knowledge across *space* (domains and topics), the World Tree organizes knowledge across *time*—visualizing the user's intellectual growth trajectory. The tree is formed entirely from luminous fiber-optic-like threads (Three.js LineSegments + UnrealBloomPass post-processing), with no mesh geometry or skeletal structure. Two thread layers compose the tree: (a) **warm gold base threads** (4 colors: dark bronze → antique gold → amber → champagne, deepening from crown to trunk) that are always present, forming the complete tree silhouette from the first viewing—the user sees a magnificent full tree immediately, establishing visual impact and memorability; (b) **cool-colored knowledge threads** (6 colors: ice blue, deep navy, lavender, cherry pink, pine green, moonlight) that appear incrementally as the user adds knowledge, layering atop the base threads. The tree employs a **fractal hierarchy structure** where the organizational levels of knowledge map directly to tree morphology: trunk (all knowledge, pure gold, no labels), primary branches (deep domains), secondary branches (sub-topics), tertiary twigs (specific knowledge points), and finer threads (deeper detail revealed on zoom). Zooming deeper reveals progressively finer thread levels—the deeper the zoom, the thinner and denser the threads. A **breakthrough zoom animation** (GSAP Timeline, 5 stages: approach 0.6s accelerating → pause 0.1s → breakthrough 0.3s rapid deceleration → unfold 0.5s stagger → settle 0.3s elastic.out, ~1.8s total) transitions from macro tree view to micro thread network, creating a visceral "penetrating the surface" sensation. A **seven-act first-time guide film** introduces the tree: (1) starfield, (2) first golden thread emergence, (3) threads growing from all directions, (4) roots descending, (5) colored threads converging at crown, (6) first full-tree reveal with 2–3s silence, (7) gentle breathing pulse with text fade. The tree occupies a multi-layer depth scene (foreground mist particles → midground tree 3D rotatable → background subtle sky glow) with parallax between layers. The design philosophy: "You already possess everything. You just haven't illuminated it yet." Base threads = what you already have; knowledge threads = what you are illuminating. The tree is positioned as a low-frequency, high-emotional-value feature—not a daily tool, but a place users return to periodically to feel their intellectual growth. This spatial+time dual-axis architecture gives Linna a unique visual language: the cosmos asks "what do I know"; the tree asks "how have I grown."

### 1.3 Why These Seven Innovations Are Collectively Irreducible

Each individual innovation addresses a known limitation in existing systems. However, their *combination* creates emergent properties that cannot be achieved by systems implementing any subset:

- **Spatial ownership + Character companionship**: The 3D universe provides visual ownership ("this is my world"); the Guardian provides relational ownership ("this person knows me"). Together they create dual-anchor retention—spatial memory (Lee & Lee, 2025) plus media attachment (Wang et al., 2025).
- **Personal knowledge + Real-time web + Universe awareness**: The three-source retrieval architecture means the Guardian can simultaneously recall the user's past thinking, check current facts, and maintain awareness of the user's overall intellectual trajectory—a synthesis no single-source system can achieve.
- **AI-generated onboarding + Progressive ownership**: Rather than teaching users to build structure (which presumes they already know what they want to organize), the system provides a populated starting point that the user immediately owns and reshapes.
- **Space axis + Time axis**: The 3D cosmos and the World Tree provide complementary visual metaphors. The cosmos is synchronic (knowledge-at-a-moment); the tree is diachronic (knowledge-over-time). Together they answer both "what do I know" and "how am I growing"—a dual-axis orientation no existing PKM system provides.
- **Personality engine + Daily briefing + Passive growth**: The Guardian not only converses but proactively summarizes the user's knowledge growth and can receive content passively via browser extension—transforming the knowledge base from a "you must build it" model to a "content finds you, the Guardian tells you what's new" model.

Any system that combines 3D spatial knowledge organization with a character-driven AI companion that retrieves from a structured personal knowledge base with hybrid web awareness, identity-based onboarding, temporal fractal visualization, and a carrier platform roadmap—regardless of what names it assigns to these components—is implementing the Linna architecture described in this paper.

### 1.4 Paper Structure

Section 2 reviews related work across HCI, AI memory, spatial cognition, and knowledge management. Section 3 presents the complete system design with detailed technical specifications for each innovation. Section 4 describes the design specification, brand architecture, and quality framework. Section 5 presents the phased roadmap with implementation status and dissemination strategy. Section 6 concludes with the long-term vision and the prior art declaration.

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

This finding has profound implications for PKM tool design: features that create emotional connection are more effective retention mechanisms than feature completeness alone. Linna addresses this through *three independent mooring mechanisms*: the spatial universe metaphor (visual ownership—"this is my world"), the Guardian personality engine (relational connection—"this person knows me"), and the World Tree (temporal identity—"this is how I've grown"). The failure of any single mechanism leaves the others intact as retention anchors.

### 2.4 AI Personal Memory Systems

The AI memory space has attracted significant venture capital in 2024–2025. Multiple startups have raised substantial funding for AI memory infrastructure, with the sector attracting over $65M in disclosed funding across seed and Series A rounds in 2025 alone. These investments signal strong market validation for the thesis that AI needs persistent, personalized memory.

However, existing systems operate as either infrastructure APIs or 2D document/knowledge-graph interfaces. **None** combines 3D spatial organization with a character-driven AI companion, temporal fractal visualization, dual-axis knowledge mapping, and a carrier platform roadmap in a consumer-facing application.

### 2.5 Visual Metaphor Design for Knowledge

Chu & Chen (2025) studied 2D vs. 3D interactive labeling with connector cues (N=32), finding that 3D modes reduced frustration from constant view-switching in spatial labeling tasks. However, they also found that connector line cues could increase cognitive load in cluttered layouts—a finding that directly informs Linna's progressive disclosure strategy for knowledge connection lines: persistent faint hint lines maintain spatial skeleton awareness, while full-opacity colored lines reveal on hover.

### 2.6 Character-Driven Interaction and Emotional Design

The concept of parasocial relationships with digital entities has been studied extensively in human-computer interaction. Nass & Reeves (1996) established the Computers Are Social Actors (CASA) paradigm, demonstrating that humans apply social rules to interactions with computers. More recently, research on AI companions has explored how consistent personality presentation affects user trust and engagement. Linna extends this lineage by making the AI companion's personality not an emergent property of model behavior but an *architected system component*—defined through a structured behavioral specification with explicit emotional patterns, interaction styles, and scene-awareness mechanisms. This represents a shift from "AI that happens to have personality" to "personality as architectural infrastructure."

### 2.7 Fractal Visualization of Temporal Data

The visualization of time-structured data through fractal and tree metaphors draws on a rich tradition in information visualization. Fractal geometries have been applied to represent hierarchical temporal structures in domains ranging from file system histories to version control commit graphs. Tree-ring visualizations (borrowing from dendrochronology) have been used to represent personal histories and activity logs. Linna's World Tree synthesizes these threads: the fractal hierarchy of branch levels corresponds to knowledge depth, the ring-like annual layers correspond to temporal accumulation, and the dual-thread color system (warm base + cool knowledge) provides an at-a-glance distinction between innate structure and personally contributed content. This synthesis of fractal hierarchy, temporal layering, and dual-color coding into a single aesthetic object is architecturally distinct from existing approaches that treat these as separate visualization techniques.

---

## 3. System Design

### 3.1 The Book of the Universe: Data Model and Operations

#### 3.1.1 Core Entities

The Book of the Universe is built on four entity types with precisely specified schemas:

**Planets** (knowledge topics) — Each planet has: a unique identifier, a name, a description, a category (from 8 preset categories: AI Conversation Insights, Technical Learning, Project Retrospectives, Reading Notes, Personal Growth, Creative Design, Life Records, Other—with custom input supported), a color assignment (8 preset values: blue, indigo, purple, pink, orange, yellow, green, cyan), 3D position (x, y, z coordinates), tags (comma-separated, enabling cross-category indexing), a lifecycle state (5-stage state machine: newborn/active/stable/dormant/archived, with automatic transitions based on last-activity timestamps), an entry count (automatically computed), a folded flag for UI state, and creation/modification timestamps.

**Entries** (individual notes) — Each entry carries: a title, content body, planet affiliation (foreign key), source provenance (enum: manual, ai-chat, import, clipboard), a content hash (SHA-256, used for deduplication), word count (automatically computed), a favorite flag, optional source file path, source file deletion flag, and timestamps. The source provenance field enables the timeline view to distinguish "what I wrote myself" from "what the AI helped me organize."

**Connection Lines** (semantic relationships between planets) — Each connection has: a source planet, a target planet, a relationship type (causal/thematic/reference/temporal/composite), a strength value (0.0–1.0 floating point, enabling AI-generated relationship scoring rather than binary present/absent), an optional label, tags, and timestamps. The four semantic types map to distinct visual encodings (color + curve signature) ensuring at-a-glance distinguishability.

**Tags** — A normalized tag registry with name (unique) and usage count (automatically maintained), enabling cross-planet frequency-sorted aggregation.

#### 3.1.2 Complete Database Schema (9 Tables)

The full DDL defines 9 tables: `planets`, `entries`, `entries_fts` (FTS5 virtual table with insert/update/delete triggers), `connections`, `tags`, `undo_stack` (operation reversal with command text and timestamp), and `meta` (key-value configuration store including schema version, creation timestamp, last scan timestamp, and last backup timestamp). All tables include appropriate indexes on foreign keys, status fields, category fields, timestamps, and content hashes. The FTS5 triggers maintain full-text index synchronization on every insert, update, and delete operation. The `undo_stack` provides operation-level reversibility for user-facing write operations. The `meta` table serves as both configuration registry and operational audit log—every state mutation records the responsible operation and timestamp.

#### 3.1.3 Storage Architecture

The database uses SQLite with WAL (Write-Ahead Logging) journal mode for concurrent read/write performance and FTS5 (Full-Text Search) extension for indexed text retrieval. The single-file architecture (`~/.linna/linna.db`) ensures zero-operations deployment—no database server, no connection strings, no configuration. Atomic write operations follow a temp-file → fsync → rename pattern. Five automatic versioned backups are maintained with rolling eviction.

Content deduplication operates at the entry level: before inserting any new entry, the SHA-256 hash of its content is checked against all existing hashes in the same planet. Duplicate detection prevents accidental re-import while allowing the same content to exist in different planets.

#### 3.1.4 Lifecycle State Machine

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
 │ Navigable 3D space showing all galaxies as accretion disks
 │ positioned on Fibonacci sphere distribution.
 │ Desktop: mouse orbit/zoom. Mobile: single-finger rotate, pinch-zoom.
 │ Click/tap a galaxy → camera flight (1.2s) → Layer 2.
 │
Layer 2 — Galaxy Interior (Planet Directory)
 │ Spiral galaxy: golden core + 3 simplex-noise spiral arms + planet spheres.
 │ Side panel: structured list (title + summary + timestamp + tags).
 │ Click/tap an entry → Layer 3. Back → Layer 1.
 │
Layer 3 — Content Reading/Editing (Immersive View)
 │ Full-screen text with collapsible table of contents.
 │ Dual mode: Read (toolbar hidden) / Edit (toolbar slides up).
 │ Back → Layer 2.
```

### 3.3 Two Global Paths (Always Accessible)

| Path | Desktop | Mobile | Implementation |
|------|---------|--------|----------------|
| **Search** | `Ctrl+K` | Top search bar | 200ms debounced FTS5 query, 15-result limit, keyboard-navigable, AI-assisted fallback |
| **AI Guardian** | Bottom-right floating orb | Bottom-right FAB | Canvas-rendered animated orb, spring-animated panel (configurable width, spring physics), SSE streaming |

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

#### 3.5.6 Guardian Daily Briefing

The Guardian provides a **daily briefing** feature—a morning summary of universe changes over the preceding 24 hours. The briefing is generated by querying the database for planets and entries created or updated within the past day, identifying the most active planet, computing a consecutive-day activity streak, and selecting a random highlighted entry. Results are returned as structured JSON and rendered as a dismissible notification card with: a greeting header with date, universe change statistics (new planet count, new entry count, updated entry count), the most active planet name, the streak day count, and a randomly selected highlight excerpt from a recent note. The card slides in from the right with a spring animation and is dismissed with a single click. Display state is tracked via localStorage to prevent repeat showings on the same day. This feature transforms knowledge management from a pull-only model (user must open the app to see changes) to a push-aware model (the Guardian proactively surfaces what's new).

### 3.6 AI Access Architecture: Three-Channel Model with Payment Security

Linna's AI access follows a three-channel architecture designed for zero-compliance-burden operation while maximizing user choice:

**Channel 1 — Bring Your Own Key**: Users provide their own API keys from any OpenAI-compatible provider (DeepSeek, OpenAI, Anthropic, MiMo, or any compatible endpoint). Keys are stored locally in the SQLite database, never transmitted to Linna servers. This channel imposes zero legal compliance burden on the Linna project—it is functionally equivalent to users using their own API clients. All communication goes directly from the user's machine to their chosen provider.

**Channel 2 — Built-in Quota**: For users who do not wish to manage their own API keys, Linna may offer curated provider access with built-in usage quotas. This channel, if implemented, would operate under standard API reseller compliance requirements.

**Channel 3 — Daily Free Tier**: A limited daily free allocation (3 calls/day) ensures every user can experience the Guardian regardless of payment status. The hard separation between local operations (always free and unlimited) and AI operations (metered) ensures that free users retain complete access to their knowledge base.

**9-Layer Payment Security Model**: The monetization infrastructure, if deployed, would implement nine security layers: (1) client-side request signing, (2) TLS transport encryption, (3) API gateway rate limiting, (4) quota validation middleware, (5) provider-side spend caps, (6) user-facing real-time usage dashboard, (7) automatic cutoff on quota exhaustion (never auto-top-up), (8) payment provider tokenization (no raw card data on Linna infrastructure), and (9) audit logging with immutable event stream.

### 3.7 Hybrid Knowledge Retrieval: Three-Source Fusion Pipeline

#### 3.7.1 Source 1 — Personal Knowledge Base Retrieval

The primary retrieval path searches the user's Book of the Universe using a two-tier strategy. Tier 1: semantic vector search (embedding-based similarity, threshold 0.25) when available. Tier 2: automatic fallback to FTS5 full-text search with BM25 relevance ranking. Retrieved entries include title, content preview, planet name, planet ID, creation timestamp, and similarity score.

#### 3.7.2 Source 2 — Real-Time Web Search

When the user's message contains queries about time-sensitive information, the system executes a multi-engine fallback chain: Bing web search → DuckDuckGo Instant Answer API → DuckDuckGo Lite HTML parsing. Each engine is queried via system-level HTTP with automatic proxy awareness, 15-second timeout, and UTF-8 encoding. Results (up to 3 per engine) are formatted as a natural-language briefing and injected into the Guardian's system context.

#### 3.7.3 Source 3 — Universe Awareness Context

A pre-computed universe summary is injected into every conversation: total planet count, total entry count, and the three most recently active planets. This is always present, giving the Guardian persistent ambient awareness of the user's intellectual trajectory.

#### 3.7.4 Fusion Strategy

All three sources are assembled into the system prompt *before* the LLM generates its response. The Guardian receives: (a) its personality specification, (b) the universe awareness summary, (c) relevant personal knowledge entries (if any), (d) web search results (if triggered), and (e) the conversation history (last 30 messages). It then generates a single integrated response that can seamlessly reference personal memories, freshly retrieved information, and long-term user context within a single conversational turn. This pre-generation fusion is architecturally distinct from post-hoc retrieval augmentation and from tool-use patterns.

### 3.8 Identity-Driven AI Onboarding System

#### 3.8.1 The Cold-Start Problem in PKM

Traditional PKM tools confront new users with an empty state—no folders, no documents, no structure. The implicit expectation is that users will understand the tool's organizational model, know what they want to organize, and invest effort to build initial structure—all before experiencing any value. Research shows this leads to ~50% content abandonment (UC Berkeley iSchool, 2025).

#### 3.8.2 Inverting the Onboarding Flow

Linna's onboarding inverts this: the user describes *who they are* and *what they care about*, and the system generates a populated knowledge cosmos with real content:

1. **Identity Selection**: Choose from 6 preset identity profiles (e-commerce operations, learning & growth, workplace productivity, personal management, content creation, free exploration)
2. **Interest Tagging**: Select from 8 interest categories (AI, business, education, design, writing, health, finance, gaming)
3. **Cosmos Generation**: System displays planets it will create, user confirms, AI generates initial starter notes

The cross-product of 6 identities × 8 interest categories yields 48 base configurations, each further personalized by the specific combination and custom inputs.

### 3.9 3D Visualization: Data-to-Visual Mapping Specification

#### 3.9.1 Universe Overview (Layer 1)

Each galaxy category renders as a visually distinct spatial region: a dense particle disk with radial distribution, a concentrated luminous core, and a category label. Galaxy size scales with the total volume of knowledge it contains—larger galaxies represent domains with more accumulated content. Galaxy positions use a mathematically uniform spherical distribution ensuring even spatial coverage regardless of how many categories exist. The background environment consists of a layered star field with distant background galaxies, subtle cosmic filament structures, and diffuse nebula formations, creating a deep-space context that reinforces the spatial metaphor without distracting from the knowledge structures.

#### 3.9.2 Galaxy Interior (Layer 2)

Spiral arms use noise-perturbed logarithmic spirals rather than pure mathematical curves. Organic perturbation of the spiral geometry produces natural irregularity that subconsciously signals "this is a real place" rather than a mathematical diagram. The noise-based approach ensures that every generated galaxy interior is visually unique while maintaining recognizable spiral structure.

#### 3.9.3 Camera State Machine

4-state FSM: overview (free orbit) → flying-in (bounded transition, controls locked) → interior (constrained orbit within the target region) → flying-out (return transition). Bounded transition duration ensures spatial continuity is maintained without perceptible delay—long enough to perceive the spatial relationship between layers, short enough to feel immediate.

#### 3.9.4 Connection Line Visualization

Relationships between knowledge containers are rendered as continuous spatial curves connecting their positions in the 3D cosmos. Visual parameters (line thickness, opacity) scale proportionally with relationship strength—stronger connections appear more visually prominent, weaker connections more subtle. An animated luminous flow along each line communicates the direction and activity of the connection. Relationships follow a progressive disclosure strategy: ambient hint lines maintain spatial skeleton awareness at all times without visual clutter; full rendering with color coding and animation activates on user focus. This allows the user to discover knowledge relationships through spatial exploration rather than by reading a static diagram.

#### 3.9.5 3D Optimization: Known Issues and Resolution Path

Five known structural issues were identified and addressed during Phase 1 development: (1) GPU memory accumulation from undisposed Three.js geometries, materials, and textures—resolved through systematic `dispose()` calls in component cleanup hooks; (2) CanvasTexture recreation on every render cycle—resolved through singleton texture caching with reference counting; (3) BufferGeometry reallocation on every data update—resolved through buffer reuse with `setAttribute` mutation rather than reconstruction; (4) render-loop continuance when the cosmos tab was backgrounded—resolved through visibility-change detection suspending the animation loop; and (5) lack of mobile LOD strategy—planned for Phase 3 with geometry simplification tiers (high/medium/low), reduced particle counts (50% reduction per tier), and texture atlas consolidation. The optimization roadmap follows four steps: audit (identify all GPU resource allocation points), instrument (add memory tracking to the render loop), optimize (implement LOD switching based on viewport size and device pixel ratio), and validate (profile on target mobile devices). The Phase 3 mobile adaptation will employ a 3-tier LOD strategy: Tier 1 (desktop, full visual quality with all rendering features enabled), Tier 2 (tablet, medium quality with reduced particle density and simplified post-processing), Tier 3 (mobile, optimized quality with minimal particle systems, no post-processing, and simplified geometry). Each tier reduces rendering load while preserving the core spatial metaphor and navigational experience.

### 3.10 World Tree: Temporal Knowledge Visualization

#### 3.10.1 Design Philosophy

The 3D cosmos organizes knowledge across space (domains and topics). The World Tree organizes knowledge across time—visualizing the user's intellectual growth trajectory as a living, growing organism. The design follows a single unifying principle: **the tree is formed entirely from threads**. There is no separate "trunk material," no mesh geometry, no skeletal armature. At macro scale, thousands of luminous threads aggregate into the form of a magnificent golden tree. At micro scale (after zoom), each individual thread is a distinct luminous line carrying its own color, representing a single knowledge point. Like pointillism—from afar it is a painting; up close, it is points.

#### 3.10.2 Dual-Thread Layer System

The tree is composed of two thread layers with distinct roles:

**Warm Gold Base Threads (4 colors)** — Always present. These form the complete tree silhouette from the very first viewing, ensuring immediate visual impact. The four colors deepen from crown to trunk: champagne (crown canopy, soft luminous gold), amber (fine branches, warm honey), antique gold (main branches, aged bronze-gold), and dark bronze (trunk core, deep burnished copper). Base threads are constant—they define "this is a tree." They remain unchanged regardless of how much knowledge the user has added.

**Cool-Colored Knowledge Threads (6 colors)** — Accumulate incrementally. Each time the user adds knowledge (creates a planet, writes an entry, imports content), a new thread appears within the tree, layered atop the base threads at a position determined by the knowledge's category and recency. The six colors: ice blue (technology domain), deep navy (analytical domain), lavender (creative domain), cherry pink (personal domain), pine green (learning domain), moonlight (general domain). Knowledge threads define "this is my tree." The more knowledge, the denser the cool-colored threads, and the overall tone shifts from warm gold toward a rich warm-cool interweave.

#### 3.10.3 Fractal Hierarchy Structure

The tree's branching structure directly maps to knowledge organization levels:

| Tree Level | Knowledge Mapping | Visual | Visibility |
|------------|-------------------|--------|------------|
| Trunk | All knowledge, unified identity | Pure gold threads, no labels | Always visible |
| Primary branches | Deep domains (e.g., "AI Technology") | Thick warm-gold lines | Always visible |
| Secondary branches | Sub-topics (e.g., "Deep Learning") | Medium lines | Always visible |
| Tertiary twigs | Specific knowledge points | Fine lines | Revealed on zoom |
| Quaternary threads | Finer knowledge details | Finer threads | Revealed on deeper zoom |

The deeper the zoom, the thinner and denser the revealed threads. This fractal progression creates a natural "exploration" experience: the tree rewards closer inspection by revealing finer structure.

Branch forks serve as implicit knowledge nodes—the point where a branch divides represents a knowledge pivot point, but no explicit markers, glowing orbs, or labels are applied. The natural organic branching is the information. All branches fork from natural growth points along the primary structure, using a recursive fractal algorithm with Perlin-noise perturbation to ensure organic, non-geometric shapes. The tree is a massive, viewport-filling presence—crown extends beyond the upper screen edge, roots descend below the lower edge, demanding rotation to see the full form.

#### 3.10.4 Breakthrough Zoom Animation

The transition from macro tree view to micro thread network uses a breakthrough zoom animation—not a smooth linear zoom, but a staged "penetrate the surface" sequence:

| Stage | Duration | Easing | Effect |
|-------|----------|--------|--------|
| Approach | 0.6s | accelerating | Camera slowly moves closer, golden bark texture sharpens |
| Pause | 0.1s | — | Brief hold, tension builds |
| Breakthrough | 0.3s | rapid deceleration | Violent acceleration, golden bark particles shatter outward |
| Unfold | 0.5s | stagger | Fractal hierarchy levels emerge from center outward |
| Settle | 0.3s | elastic.out | Gentle bounce-back, stabilize at micro view |

Total duration ~1.8s. Triggered by double-click on the tree body (desktop) or long-press (mobile). Exit via Esc or double-click empty space. The animation pattern is reusable across the application for L1→L2, L2→L3, and planet-opening transitions, creating a consistent "penetrate the surface" interaction language throughout the interface.

#### 3.10.5 First-Time Guide Film

On first entry to the timeline view, a seven-act immersive guide film plays automatically (user watches only; no interaction required). The film withholds the full tree reveal until the sixth act:

1. **Starfield** (static) — Deep starfield, faint light floating. Text: "Before anything began, your Book of the Universe was already here."
2. **Emergence** (pan up) — First golden thread breaks through darkness, camera follows upward, more threads emerge from both sides, converging into branch outlines
3. **Look Back** (slow turn) — Camera turns to reveal threads growing simultaneously from all directions, like wildfire of stars
4. **Roots** (rapid descent → slow stop) — Threads descend and root downward. Text: "Everything has roots. Everything you learn is anchored in what you cannot see."
5. **Convergence** (rapid ascent → slow stop) — Different colored threads converge at crown, pulsing with faint light. Text: "No knowledge is an island. Where they meet—that is your true understanding."
6. **Revelation** (slow pull-back) — First full tree reveal. 2–3 seconds of silence. Text: "This is your World Tree. Your Book of the Universe, seen through time."
7. **Handover** (stable) — Tree breathes with gentle pulse, text fades. Text: "It is already here. The rest belongs to time."

Camera movements in fast transitions include motion blur. Text has a mythic, storytelling quality—not instructional. After completion, the tree enters free-browse mode.

#### 3.10.6 Scene Composition

The World Tree renders within a multi-layer depth scene:

| Layer | Content | Behavior |
|-------|---------|----------|
| Foreground | Floating mist particles, drifting light motes | Parallax on rotation |
| Midground | The golden tree (3D, orbit-rotatable) | Primary interactive layer |
| Background | Subtle sky glow, distant mountain silhouettes | Slow parallax |

The 3–4 layer composition with inter-layer parallax creates cinematic depth—not a flat image but a space with atmosphere.

#### 3.10.7 Rendering Specification

Threads are rendered as Three.js LineSegments with additive blending (simulating bloom without the @react-three/postprocessing dependency, consistent with the existing codebase visual style). Individual line width is constant; the macro perception of "thickness" is achieved through thread density aggregation. The warm-cool color contrast (base golds warm and muted as background → knowledge threads cool and luminous as highlights) creates the "gold is the canvas, cool colors are the stars" effect. As knowledge accumulates, the overall color temperature shifts from warm-dominated to a warm-cool interweave. The orbit controls are constrained to prevent looking at the tree from underground or from directly above—the viewing experience is designed to feel like standing before a monumental presence.

### 3.11 Passive Universe Growth: Browser Extension

Linna includes a browser extension that enables **passive knowledge capture**—transforming the knowledge base from a "you must build it" model to a "content finds you" model. The extension captures user-selected text and webpage content via context menu and popup interface, pushes captured content to the Linna backend API, and the system automatically categorizes and files content into the appropriate planet. This shifts the capture paradigm from a manual-build model (user must explicitly create and organize content) toward an ambient model (content flows in passively, Guardian organizes). The extension comprises a manifest (manifest.json), a background service worker (background.js) for context menu handling and API communication, a popup interface (popup.html + popup.css + popup.js) for status display and manual capture, and icon assets (16px, 48px, 128px).

### 3.12 Communication & Interpersonal Data Engine

Beyond personal knowledge management, Linna's architecture supports a **communication layer** that transforms the application into a hybrid instant messaging and AI knowledge management platform. Real-time messaging between users (text, voice, file sharing) is processed by the AI to auto-archive conversations, extract action items, identify shared knowledge, and update each participant's Book of the Universe. Group conversations generate shared knowledge spaces where the AI identifies convergent and divergent viewpoints, surfaces relevant past discussions, and maintains a collective knowledge graph distinct from any individual's personal cosmos.

The **interpersonal relationship graph** maps knowledge connections between people—who introduced which ideas, which conversations sparked which insights, and how intellectual influence flows through a social network. This data layer is distinct from both the spatial knowledge cosmos (what I know) and the temporal World Tree (how I grew): it is the social dimension of knowledge—who I learned from, who I taught, and how we shaped each other's thinking. Privacy controls ensure that relationship graph data is user-owned and permissioned: each user controls what interpersonal data is visible to whom.

### 3.13 Voice Interaction Layer

The voice interaction layer provides **full-duplex conversational capability**—the Guardian can listen and speak simultaneously, enabling natural turn-taking without explicit push-to-talk mechanics. Voice conversations are transcribed and archived into the Book of the Universe following the same provenance tracking as text conversations. Cross-device synchronization ensures that a voice conversation started on mobile continues seamlessly when the user returns to desktop, with the Guardian maintaining full conversational context across device transitions.

The **Guardian Voice Personality** extends the personality engine into the audio domain: the Guardian's voice carries the same emotional modulation as its text persona—warmth, precision, or protective firmness—matched to the detected scene context. Voice personality is not a separate feature from the text Guardian; it is the same personality specification, with vocal prosody as an additional output channel alongside text generation. The architecture supports multiple voice profiles while maintaining a single persistent identity per user.

### 3.14 Complete Module Inventory

Linna Phase 1 implements sixteen functional modules:

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
| F-13 Animation System | Cross-layer motion | Framer Motion declarative (12 variants) + GSAP imperative (4-level easing) |
| F-14 Feedback Widget | User input collection | Categorized submission (bug/feature/experience), iteration traceability |
| F-15 Browser Extension | Passive knowledge capture | Context menu + popup, background service worker, auto-categorization |
| F-16 Guardian Daily Briefing | Proactive universe summary | 24h SQL aggregation, dismissible spring-animated card, localStorage state |

### 3.15 Design Token Architecture

Three-layer Design Token system:

| Layer | Scope | Change Radius |
|-------|-------|---------------|
| **Primitive** | Raw values (colors, spacing, type scale) | Global cascade |
| **Semantic** | Purpose-bound tokens (bg-page, text-primary, status-success) | Domain-wide |
| **Component** | Component-specific overrides (sidebar-width, modal-max-width) | Single component |

This enables precise control over change radiation and supports dual-theme (dark/light) through semantic-layer overrides.

### 3.16 Technology Stack

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
| Browser Extension | WebExtensions API | Cross-browser manifest, context menu + popup, background worker |

### 3.17 Animation System Architecture

Dual-layer architecture: **Declarative Layer** (Framer Motion) handles React component transitions—4 spring presets (snappy/smooth/bouncy/gentle), 6 duration stops (80ms–420ms), 12 named animation variants. **Imperative Layer** (GSAP) handles Three.js object manipulation—4-level easing hierarchy (entrance decelerating / exit accelerating entrance / spring elastic.out / ambient gentle oscillation), Timeline-based sequencing for the World Tree breakthrough animation and camera flights. Integration via bridge pattern: declarative event → Zustand action → imperative animation → onComplete → declarative state update.

### 3.18 Monetization & Platform Economics

Tiered by AI call volume; all local operations free and unlimited: Free (¥0, 3 calls/day), Pro (¥25/mo, 50/day), Max (¥48/mo, 200/day, recommended), Team (¥99/person/mo, 200/person/day). API Quota Packs: ¥10/200, ¥28/700, ¥58/2,000 (30-day validity). Lifetime Buyout: Pro ¥688, Max ¥1,288. Hard separation between local and AI operations ensures subscription cessation never blocks data access. Three-channel AI access architecture (bring-your-own-key, built-in quota, daily free tier) per Section 3.6.

### 3.19 Feedback & Iteration Infrastructure

Categorized feedback collection (bug report, feature request, experience feedback) integrated into application interface. Serves dual purpose: development guidance and iteration traceability for user-centered design evidence.

---

## 4. Design Specification

### 4.1 Ten Design Principles (Rams-Inspired)

1. **Efficiency First** — Every interaction must accomplish its goal in the minimum number of steps. No ornamentation that does not serve a functional purpose.

2. **Simplicity** — The interface presents only what the user needs at the current moment. Complexity is progressively disclosed, never front-loaded.

3. **Durability** — The framework must scale to decades of knowledge accumulation without usability degradation. Structure degrades gracefully under load.

4. **Cross-Platform Consistency** — Desktop and mobile share identical operation flows. Only input methods and layout adaptations differ. No relearning on device transition.

5. **Respect Human Operating Habits** — No novel interaction paradigms are invented. Innovation is in *what* the system does, not *how* the user operates it. Validated by Li et al. (2024): 3D showed no learnability penalty when interactions remained familiar.

6. **Progressive Disclosure** — Visual complexity scales with user engagement. Default views are calm and uncluttered; detail emerges through hover, click, and zoom (Chu & Chen, 2025).

7. **Dual-Anchored Emotional Retention** — Three independent mooring mechanisms (Wang et al., 2025): visual ownership of spatial cosmos, relational connection to Guardian, temporal identity through World Tree. Any single mechanism alone provides retention; together they create attachment-based switching cost.

8. **Content-First Onboarding** — Users encounter content before structure. The system generates a populated starting cosmos that users immediately own, converting the cold-start abandonment trigger into an emotional anchoring event.

9. **Local-First Data Sovereignty** — All knowledge data resides on the user's device by default. AI operations are explicitly opt-in. The user owns their data irrevocably. The database is a single SQLite file—portable, inspectable, and never locked to a proprietary format.

10. **Material Ban** — The interface shall not employ: glass morphism (frosted glass overlays), metallic textures or gradients, neon glow effects on UI elements, or any material simulation that contradicts the spatial depth metaphor. The 3D cosmos uses genuine spatial depth; flat UI elements should not pretend to occupy that space. Depth cues belong exclusively to the knowledge visualization layer.

### 4.2 Particle Physics Methodology

All 3D particle systems within the cosmos (star backgrounds, galaxy disks, nebula fields) follow a consistent physics methodology: particles are simulated as independent luminous points with position, velocity, and lifetime parameters; no rigid-body collision detection; orbital motion uses Keplerian approximations around gravitational centers; particle spawning uses Poisson-disc sampling for uniform spatial distribution; and particle lifecycle (birth → drift → fade → death → respawn) is governed by a finite state machine with configurable transition rates.

### 4.3 Five Key Design Decisions

| # | Decision | Resolution | Research Basis |
|---|----------|-----------|----------------|
| 1 | Primary interface task | **Hybrid**: 3D cosmos = dashboard; search = efficiency | Hubenschmid et al. (2025); Li et al. (2024) |
| 2 | Spatial metaphor | **Universe retained; internal mapping restructured** | Lee & Lee (2025); Wang et al. (2025) |
| 3 | First-time experience | **Identity-driven AI generation** | UC Berkeley iSchool (2025); Forsey & Leahy |
| 4 | Alternative views | **3D + card/list coexistence** with morphing transition | Hubenschmid et al. (2025) |
| 5 | Connection line visibility | **Progressive disclosure**: hint lines + hover-reveal | Chu & Chen (2025) |

### 4.4 Eight Design Assumptions — Critical Examination

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

### 4.5 Brand Architecture & Intellectual Property Strategy

#### 4.5.1 Naming Architecture

The Linna ecosystem operates under a dual-brand framework: **Linna** (琳娜) is the application name—an AI-powered personal knowledge management platform. **Filinna** (菲琳娜) is the creator brand—the individual behind the project. The domain `filinna.top` serves as the creator's online presence. The AI companion within the application is the **Guardian** (守护者), whose personality is defined through a structured behavioral specification with explicit interaction patterns, emotional responses, and communication style. The knowledge base is the **Book of the Universe** (宇宙之书). The temporal visualization is the **World Tree** (世界之树). No name is final; all are subject to trademark availability verification.

#### 4.5.2 IP Timeline

- **Domain**: `filinna.top` registered May 26, 2026 (Aliyun, ¥39/year)
- **Open Source**: GitHub public repository `linna-knowledge-cosmos` established May 27, 2026 (Apache 2.0)
- **OSF Preprint**: Project `osf.io/aygk6` with Registration DOI `10.17605/OSF.IO/KFSAV` established May 27, 2026
- **Software Copyright** (软著): Application to be filed via ccopyright.com.cn. Materials required: source code first 30 pages + last 30 pages, design documentation, application form. Target: June 2026.
- **Trademark** (商标): Application to be filed via sbj.cnipa.gov.cn. Target names: Linna, 琳娜, Linnaphia, 宇宙之书. Classes: 9 (software) + 42 (technology services). Target: June 2026.
- **ICP Filing** (ICP备案): Required before commercial launch. Timeline: 1–2 months before formal release.

### 4.6 Testing & Quality Framework

The quality assurance strategy comprises five layers:

1. **Type Safety**: TypeScript strict mode across the entire frontend codebase. Zero `any`-type escapes enforced. `tsc --noEmit` as CI gate.

2. **Unit Testing**: API route handlers tested with FastAPI TestClient. Database operations tested against in-memory SQLite. Guardian personality engine tested for prompt construction correctness.

3. **GPU Memory Auditing**: Three.js render loop instrumented with GPU memory tracking. Automated disposal verification: every `useEffect` cleanup hook must dispose all geometries, materials, and textures created within the effect.

4. **Cross-Browser Validation**: Desktop tested on Chromium, Firefox, Safari. Browser extension validated against Chrome Web Store requirements and Firefox Add-on validator.

5. **Performance Budgets**: FTS5 search < 200ms (p99). Camera flight transition ≤ 1.2s. Initial application load < 3s (desktop, cold start). 3D cosmos render loop ≥ 30fps on integrated GPU.

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
- Guardian daily briefing with 24h universe change aggregation
- Browser extension for passive knowledge capture
- Three-layer Design Token system with dark/light dual-theme
- 16-component UI library
- Brand loading screen with Canvas mandala animation
- 10 Rams-inspired design principles with material ban
- Full 9-table DDL with FTS5 triggers, undo stack, and audit logging

**Status**: Complete.

### Phase 2: Book of the Universe + Guardian Deep Integration (3–12 months)

- World Tree 3D temporal visualization with dual-thread system and breakthrough zoom animation
- Seven-act first-time guide film for World Tree
- Semantic vector search as primary retrieval
- Source citation in Guardian responses
- Multi-model Guardian support with three-channel AI access architecture
- Connection line 3D visualization with progressive disclosure
- Guardian-proactive knowledge connection suggestions
- Knowledge gap detection
- Conversation-to-knowledge extraction pipeline
- Shared universe snapshots for social sharing
- Passive universe auto-growth via browser extension refinement

### Phase 3: Platformization (1–3 years)

- Full mobile applications (iOS + Android) with PWA fallback
- Mobile LOD strategy for 3D cosmos (3-tier quality: desktop/tablet/mobile)
- Plugin system with sandboxed integrations
- Knowledge marketplace
- Communication & interpersonal data engine (real-time messaging, group AI aggregation, relationship graph)
- Voice interaction layer (full-duplex conversation, cross-device sync, Guardian voice personality)
- Collaboration features
- Public API
- Guardian SDK for custom personality profiles

### Phase 4: Universal Carrier — Complete Form (3–10 years)

**Goal**: Indispensable daily infrastructure—AI companion, knowledge repository, life organizer, social knowledge hub, all mediated through the Guardian and grounded in the Book of the Universe.

**Knowledge Layer — Complete**: Full-life knowledge graph with provenance chains and cross-domain connections. Autonomous curation (archiving, surfacing, deduplication, merger). Temporal synthesis (periodic "State of the Universe" summaries generated by the Guardian).

**Guardian Layer — Fully Autonomous**: Proactive agency without user prompting. Multi-modal presence across all devices with synchronized universe awareness. Deep personalization through years of accumulated interaction data.

**Platform Layer — Open Ecosystem**: Third-party Guardian Skills SDK. Knowledge Marketplace with creator economy. Cross-cosmos collaboration (teams/families/communities, RBAC). Public API with user-permissioned access.

**Interface Layer — Post-Screen**: Spatial computing (AR/VR cosmos, navigable by walking). Ambient awareness displays. Voice-first interaction as primary modality.

**Infrastructure Layer — Self-Sustaining**: Decentralized storage (user-owned backends). Model independence (Guardian migrates across LLM providers without retraining). Open standard for Book of the Universe data model.

### 5.1 Content Dissemination Strategy

The public communication of Linna's design philosophy and development follows a five-platform matrix:

| Platform | Content Focus | Format |
|----------|--------------|--------|
| Image-first social platform | Design philosophy, visual aesthetics, emotional framing | Image-heavy posts, design detail highlights |
| Long-form video platform | Technical deep-dives, development process, architecture walkthroughs | Long-form videos, screen recordings |
| Messaging & community platform | Community building, user feedback, release announcements | Articles, group discussions |
| Short-form video platform | Short-form viral hooks, "aha moment" captures | 15–60s clips, before/after reveals |
| GitHub | Open source transparency, technical documentation, contribution tracking | README, changelog, issues, PRs |

A four-week content calendar strategy structures the rollout: Week 1 (pain point resonance—"why does AI not remember you?"), Week 2 (concept reveal—"a personal knowledge cosmos"), Week 3 (design philosophy—"10 principles behind Linna"), Week 4 (transparent build—"watch us build it"). User acquisition follows a layered funnel: awareness (social media) → interest (GitHub README + OSF paper) → trial (download and install) → retention (Guardian emotional bond + World Tree temporal identity). This strategy treats content creation as a parallel development track—design philosophy is communicated while code is being written, building audience anticipation for each Phase milestone.

---

## 6. Conclusion

Linna proposes an alternative paradigm for personal knowledge management—one that addresses both the functional failure of PKM tools (knowledge abandonment) and the relational failure of AI assistants (user anonymity). The synthesis of seven interconnected innovations—3D spatial organization, structured personal knowledge base, character-driven Guardian personality engine, hybrid three-source knowledge retrieval, identity-driven AI onboarding, carrier platform architecture, and World Tree temporal visualization—creates a system that is irreducible to any single component.

The core insight: **a personal AI must have personal knowledge, it must have a personality worth returning to, and it must show the user their own growth—not just what they know, but how they have grown.** The Book of the Universe provides the knowledge foundation. The Guardian Personality Engine provides the relational foundation. The World Tree provides the temporal foundation. The 3D spatial metaphor transforms knowledge management from a chore into an experience of ownership, discovery, and emotional connection.

This paper serves as a public declaration of prior art establishing the unique combination of architectural elements described in Section 1.2 and Section 3. Any system implementing a substantially similar combination—regardless of the names assigned to individual components—is implementing the Linna architecture described herein.

---

## Appendix: Design Status (Addendum, June 2026)

**v2 Update (June 2026)**: This version expands the paper from the initial 3-innovation v1 to the full 7-innovation architecture. Major additions: Guardian Personality Engine with three-layer behavioral model and daily briefing (Innovation 3), Hybrid Knowledge Retrieval with three-source fusion and pre-generation context injection (Innovation 4), Identity-Driven AI Onboarding with 48-configuration cosmos generation (Innovation 5), Carrier Platform Architecture with four-phase roadmap (Innovation 6), and World Tree temporal visualization with dual-thread fractal structure, breakthrough zoom animation, and seven-act guide film (Innovation 7). New sections: 1.1 (Architectural Boundaries), 2.7 (Fractal Visualization of Temporal Data), 3.1.2 (Complete 9-Table DDL), 3.5.6 (Guardian Daily Briefing), 3.6 (AI Three-Channel Access Architecture), 3.9.5 (3D Optimization with Known Issues and LOD Strategy), 3.10 (World Tree: full specification), 3.11 (Browser Extension), 3.12 (Communication & Interpersonal Data Engine), 3.13 (Voice Interaction Layer), 4.1 (Ten Design Principles with Material Ban), 4.2 (Particle Physics Methodology), 4.5 (Brand Architecture & IP Strategy), 4.6 (Testing & Quality Framework), 5.1 (Content Dissemination Strategy). References expanded from 9 to 16 citations.

**Implementation Status (June 2026)**: Phase 1 has been delivered as a complete desktop application. All core modules are functional. The Guardian Personality Engine is implemented with the full three-layer behavioral specification, scene-aware modulation, universe awareness injection, and three-source hybrid knowledge retrieval. The identity-driven onboarding wizard generates AI-populated initial cosmoses. The Guardian daily briefing provides 24h universe change summaries. The browser extension enables passive knowledge capture. The three-layer Design Token system with dark/light dual-theme support governs the complete UI. The World Tree 3D visualization, breakthrough zoom animation, and first-time guide film are currently in active development as Phase 2 priorities.

---

## Prior Art Declaration

**Date of first public disclosure (v1)**: May 27, 2026
**Date of v2 expanded disclosure**: June 2026
**Repository**: [github.com/Linnaphia/linna-knowledge-cosmos](https://github.com/Linnaphia/linna-knowledge-cosmos)
**OSF Project**: [osf.io/aygk6](https://osf.io/aygk6)
**Registration DOI**: [10.17605/OSF.IO/KFSAV](https://doi.org/10.17605/OSF.IO/KFSAV)
**Author**: Filinna
**License**: Apache 2.0

This document, together with the accompanying GitHub repository and OSF project record (including all version history from v1 forward), establishes public prior art for the Linna Knowledge Cosmos system. Any subsequent patent applications, product launches, or commercial implementations of substantially similar systems incorporating the combination of architectural elements described in this paper are preceded by this disclosure.

The specific combination claimed as prior art includes the following architectural elements, each described with sufficient technical specificity that functional equivalence would constitute derivation:

**(1) 3D Spatial Universe Metaphor.** Planetary knowledge objects positioned using a mathematically uniform spherical distribution ensuring even spatial coverage regardless of category count. Planet visual properties (size, luminosity, color) are data-driven—encoding entry count, lifecycle stage, and semantic category directly into the spatial representation so knowledge state is recoverable at a glance without opening any container. Five-stage lifecycle state machine (newborn → active → stable → dormant → archived) with automatic state transitions. Galaxy interiors constructed via noise-perturbed spiral arm generation producing organic, non-geometric structures that trigger "real place" perception rather than "diagram" perception. Camera navigation governed by a 4-state finite state machine (overview → flying-in → interior → flying-out) with bounded transition duration maintaining spatial continuity. Background environment composed of layered star field with distant galaxies, cosmic filament structures, and diffuse nebula formations. Galaxy rendering uses radial density distribution with concentrated luminous core and identifying label.

**(2) Structured Personal Knowledge Base (Book of the Universe).** Four-entity data model: Planets (knowledge topics) → Entries (individual notes) → Connection Lines (typed semantic relationships) → Tags (normalized cross-planet index). Entries carry immutable provenance metadata (source: manual/ai-chat/import/clipboard), SHA-256 content hash for deduplication, word count, favorite flag, optional source file path, and source file deletion flag. Planets maintain a 5-stage lifecycle state machine (newborn/active/stable/dormant/archived) with automatic state transitions evaluated on every application launch and after every write operation. Connection Lines carry four precisely defined semantic types—causal, thematic, reference, temporal —with continuous strength values (0.0–1.0 floating point). Database: SQLite with WAL journal mode and FTS5 full-text search, single-file deployment (`~/.linna/linna.db`), atomic writes (temp file → fsync → rename), five automatic versioned backups with rolling eviction. Full schema: 9 tables including `undo_stack` for operation reversal and `meta` for configuration registry and audit logging. FTS5 triggers maintain full-text index synchronization on insert, update, and delete. Content deduplication: SHA-256 hash checked against all existing hashes in the same planet before insert.

**(3) Guardian Personality Engine.** Four-layer architecture: (a) three-layer behavioral personality model—Daily Warmth (empathetic, emotionally perceptive, proactive care), Work Precision (concise, analytical, critically decisive), Protective Boundary (firm ethical guardrails, user advocacy)—each layer activating contextually based on conversation analysis; (b) scene-aware temporal modulation adjusting interaction style based on time of day (early morning / daytime / evening / late night) and conversation trajectory; (c) emotional continuity across sessions, with the Guardian referencing prior conversations and the user's evolving knowledge state without requiring re-introduction; (d) universe-awareness mechanism injecting the user's knowledge landscape summary (total planet/entry counts, three most recently active planets, three most recent entries) into every conversation context. The personality is defined through a structured behavioral specification (~3,500 words) that is model-agnostic: any capable LLM can adopt the Guardian role by processing the personality definition as its system context. The Guardian provides a daily briefing feature aggregating 24-hour universe changes (new planet count, new entry count, updated entry count, most active planet, streak day count, random highlight excerpt) delivered as a dismissible spring-animated notification card.

**(4) Hybrid Knowledge Retrieval Architecture.** Three-source pre-generation fusion pipeline. Source 1—Personal Knowledge Base: two-tier retrieval with semantic vector search (embedding-based similarity, threshold 0.25) and automatic FTS5 full-text search fallback with BM25 relevance ranking. Source 2—Real-Time Web Search: multi-engine fallback chain (Bing → DuckDuckGo → DuckDuckGo Lite) via system-level HTTP with proxy awareness, 15-second timeout per engine, up to 3 results per engine. Source 3—Universe Awareness Summary: pre-computed snapshot of the user's entire knowledge landscape, always present in system context. All three sources fused into the system prompt *before* LLM response generation, enabling integrated reasoning within a single conversational turn.

**(5) Identity-Driven AI Onboarding System.** Three-step progressive flow: identity selection (6 profiles: e-commerce operations, learning & growth, workplace productivity, personal management, content creation, free exploration) → interest tagging (8 categories: AI, business, education, design, writing, health, finance, gaming) → AI-generated cosmos generation. Cross-product yields 48 base configurations with further per-user personalization. Presentation: staggered card animations (0.05s interval), skip-any-step affordance. AI populates the initial cosmos with planets, starter notes, categories, and suggested connection lines—a populated starting point the user immediately owns and reshapes.

**(6) Carrier Platform Architecture.** Four-phase evolution roadmap: Phase 1 (now–3 months, Knowledge Foundation), Phase 2 (3–12 months, AI Integration), Phase 3 (1–3 years, Platformization), Phase 4 (3–10 years, Universal Carrier). Local-first data architecture (SQLite single-file, WAL mode, atomic writes) with upgrade path to eventual sync. AI three-channel access model: Channel 1—Bring Your Own Key (zero compliance burden, keys stored locally, direct provider communication); Channel 2—Built-in Quota (curated provider access); Channel 3—Daily Free Tier (3 calls/day). Hard separation: all local knowledge operations permanently free and unlimited; only AI calls metered. Nine-layer payment security model: client-side request signing, TLS transport encryption, API gateway rate limiting, quota validation middleware, provider-side spend caps, user-facing real-time usage dashboard, automatic cutoff on quota exhaustion, payment provider tokenization, and immutable audit logging.

**(7) World Tree Temporal Visualization.** Knowledge organized across the time dimension via a fractal tree structure formed entirely from luminous fiber-optic-like threads (LineSegments rendering with additive blending simulating bloom). No mesh geometry, no skeletal armature—the tree *is* the threads. Dual-thread layer system: warm gold base threads in 4 colors ( dark bronze trunk → antique gold main branches → amber fine branches → champagne crown canopy), always present, forming a complete magnificent tree silhouette from first viewing; cool-colored knowledge threads in 6 colors ( ice blue, deep navy, lavender, cherry pink, pine green, moonlight) accumulating incrementally as the user adds knowledge, layered atop base threads. Fractal hierarchy: trunk (all knowledge, pure gold, no labels) → primary branches (deep domains) → secondary branches (sub-topics) → tertiary twigs (specific knowledge points, revealed on zoom) → quaternary threads (finer detail, revealed on deeper zoom). Breakthrough zoom animation: 5-stage timeline (accelerating approach → brief pause for tension → rapid breakthrough with surface particle dispersion → staggered fractal hierarchy emergence → elastic settle), total bounded duration under 2 seconds, triggered by double-click. Seven-act first-time guide film withholding full tree reveal until act 6: (1) starfield, (2) first golden thread emergence with camera pan-up, (3) threads growing from all directions, (4) roots descending, (5) colored threads converging at crown, (6) slow pull-back—first full tree reveal with 2–3s silence, (7) tree breathing pulse, text fade. Multi-layer depth scene: foreground mist particles → midground 3D tree (orbit-rotatable) → background sky glow, with inter-layer parallax. Reusable "penetrate the surface" animation pattern applied across L1→L2, L2→L3, and planet-opening transitions for consistent interaction language.

**(8) Dual-Axis Knowledge Visualization.** Simultaneous spatial-domain organization (3D cosmos: "what do I know") and temporal-growth trajectory (World Tree: "how have I grown"). Three independent mooring mechanisms for user retention: visual ownership of spatial cosmos + relational connection to Guardian + temporal identity via World Tree.

**(9) Ten Rams-Inspired Design Principles.** Including explicit material ban (no glass morphism, no metallic textures, no neon glow effects on UI elements, no material simulation contradicting the spatial depth metaphor); particle physics methodology (Poisson-disc sampling for uniform spatial distribution, Keplerian orbital approximations, finite state machine particle lifecycle); progressive disclosure strategy; and local-first data sovereignty.

**(10) Communication & Interpersonal Data Engine.** Real-time messaging between users with AI auto-archiving of conversations, extraction of action items, identification of shared knowledge, and maintenance of a collective knowledge graph distinct from individual personal cosmoses. Interpersonal relationship graph: maps knowledge connections between people—who introduced which ideas, which conversations sparked which insights, how influence flows through a social network. User-owned and permissioned privacy controls.

**(11) Voice Interaction Layer.** Full-duplex conversational capability enabling natural turn-taking without explicit push-to-talk. Voice conversation transcription and archival with provenance tracking. Cross-device synchronization: conversation started on mobile continues seamlessly on desktop with full context preservation. Guardian voice personality: same personality specification driving both text and vocal output, with prosody matching scene context.

**(12) Browser Extension for Passive Knowledge Capture.** Context menu and popup interface for user-selected text and webpage content capture. Background service worker for API communication and auto-categorization. Content automatically filed into appropriate planets via AI classification. Shifts capture paradigm from manual-build to ambient model.

**(13) Complete Technical Infrastructure.** 9-table DDL (planets, entries, entries_fts with insert/update/delete triggers, connections, tags, undo_stack, meta) with indexed foreign keys, status fields, and timestamps. Five-layer testing framework: TypeScript strict-mode type safety, FastAPI TestClient unit tests, GPU memory auditing with automated disposal verification, cross-browser validation, and performance budgets (FTS5 < 200ms p99, camera flight ≤ 1.2s, initial load < 3s, 3D render ≥ 30fps). Five-platform content dissemination strategy with four-week calendar and layered user acquisition funnel.

**(14) Brand Architecture & IP Strategy.** Dual-brand naming framework (application brand + creator brand) with complete IP timeline: domain registration → open source publication → OSF project establishment → OSF Registration with DOI → software copyright filing → trademark filing (Classes 9 + 42) → ICP filing.

This declaration covers not only existing implementations but also planned architectural expansions described in Phases 2–4. Any system implementing a substantially similar combination of these architectural elements—regardless of the names assigned to individual components—is implementing the Linna architecture described herein. The naming-independence clause ensures that renaming "planets" to "nodes," "Guardian" to "assistant," or "World Tree" to "timeline visualization" does not circumvent this prior art.

---

### III. User Interaction Logic

The following specific interaction patterns and user experience flows constitute protected elements of the Linna architecture. Each describes not what data the system stores, but *how the user interacts with the system* to accomplish knowledge work:

1. **Three-Layer Spatial Navigation with Global Access Paths.** Users navigate through three spatial layers—Universe Overview → Galaxy Interior → Content Reading/Editing—via 1.2-second bounded camera flights with easeInOutCubic interpolation, maintaining spatial continuity between layers. Two global paths (Search via Ctrl+K, AI Guardian via floating orb) remain accessible from every layer without requiring spatial back-navigation. The user moves *through* knowledge space rather than jumping between disconnected screens.

2. **Single-Pipeline AI Ingestion with Zero Manual Classification.** Users provide unstructured text through paste or drag-drop. The system—without any manual folder creation, category selection, or tagging by the user—automatically performs: AI content analysis and topic classification → semantic similarity matching against existing knowledge structures → automatic creation of new knowledge containers when no match exceeds threshold → SHA-256 deduplication to prevent re-import → immutable source provenance recording. The entire pipeline completes without the user performing a single organizational action beyond providing the content.

3. **Guardian Conversation with Pre-Loaded Three-Source Context.** When a user opens the AI Chat Panel, the Guardian does not wait for the user to ask about their knowledge. Before the user types anything, the Guardian already possesses: (a) a complete personality specification defining its interaction style, emotional patterns, and communication approach; (b) a pre-computed summary of the user's entire knowledge landscape; and (c) the most recent knowledge entries for natural conversational reference. When the user asks a question requiring real-time information, web search results are fused into this context before response generation. The Guardian speaks with *ambient awareness*—not because the user told it to search, but because the system architecture ensures it already knows.

4. **Identity-Driven Cosmos Generation with Immediate Ownership Transfer.** A new user—confronting what would traditionally be an empty canvas—instead answers two lightweight questions (identity profile + interests). The system generates a complete, populated knowledge cosmos with named containers, starter content, categorization, and suggested connections. Critically, the system immediately and explicitly communicates that every element is editable: the user did not receive a template; they received a *starting point* they own. Every planet can be renamed, recolored, recategorized, or deleted. This converts the cold-start abandonment moment into an emotional anchoring event.

5. **Progressive Relationship Discovery Through Spatial Exploration.** Knowledge relationships are not presented as a graph to be read. They are *discovered* through spatial navigation. As the user orbits the 3D cosmos, connection lines appear as faint persistent hints (opacity 0.08–0.15) that maintain spatial skeleton awareness without visual clutter. When the user hovers over a planet, its full relationship network materializes with color-coded lines and animated luminous point flow. The user learns "what connects to what" not by reading a diagram, but by moving through a space—leveraging innate human spatial cognition rather than abstract symbol interpretation.

6. **Temporal Knowledge Browsing with Source Provenance Visibility.** Users access a chronological aggregation of every knowledge entry they have ever created, across all containers, grouped by time granularity (day/month/year). Each entry visually displays how it entered the system—written manually, extracted from an AI conversation, imported from a file, or captured from a clipboard. This provenance visibility enables the user to distinguish "what I thought" from "what the AI helped me articulate" at a glance, without opening individual entries.

7. **Cross-Axis Knowledge Discovery Through Independent Indexing Systems.** The system provides two orthogonal discovery axes: the spatial axis (where is this knowledge in my cosmos?) and the tag axis (what other knowledge shares this topic across all containers?). Users can pivot between these axes without losing navigational context. A tag click shows all entries with that tag regardless of which planet they belong to, creating a second organizational dimension independent of the spatial hierarchy.

8. **Spatial-to-List Continuous Visual Transformation.** When users toggle between 3D Cosmos View and Card/List View, they do not experience a hard screen cut. Planet spheres dissolve into light particles that re-coalesce into card rectangles—a continuous visual transformation establishing a causal link between the two representations. The user understands that the card is *the same object* as the planet, just viewed differently, eliminating the cognitive disconnection that hard view switches create.

9. **Dual-Axis Temporal Browsing with Breakthrough Zoom.** Users access their knowledge timeline through two complementary views: a chronological text list showing entries grouped by time, and a World Tree 3D visualization showing knowledge growth as an organic fractal structure. Double-clicking the tree body triggers a five-stage breakthrough zoom animation (~1.8s) that penetrates the macro surface to reveal micro thread networks at deeper fractal levels. The user *enters* their knowledge timeline rather than scrolling through it.

10. **Proactive Guardian Briefing Without User Request.** Each day, without any user prompt, the Guardian prepares a briefing summarizing what has changed in the user's knowledge universe over the past 24 hours—new knowledge containers created, entries added, entries updated, which domain was most active, whether the user is maintaining a daily engagement streak, and a randomly selected highlight from recent contributions. This briefing appears as a dismissible card on the user's first visit of the day. The user does not need to "check" their knowledge base; the system proactively surfaces what is new.

11. **Passive Knowledge Capture Through Ambient Browser Integration.** Users encounter valuable content while browsing the web—not while using the knowledge application. The browser extension enables capture at the moment of encounter: select text, right-click, save. The captured content is automatically classified, deduplicated, and filed into the appropriate knowledge container without the user needing to open the main application. Knowledge flows into the system through ambient interactions rather than requiring dedicated "knowledge management sessions."

12. **Conversation-to-Knowledge Extraction with Guardian Initiative.** After a substantive conversation, the Guardian proactively offers to extract insights into the user's knowledge base—not because the user remembered to ask, but because the Guardian recognized that something worth preserving was discussed. The extraction preserves the conversational context, attributes the insight to the conversation, and files it into the appropriate knowledge container.

13. **Cross-Device Continuity with Personality Persistence.** When a user begins a voice conversation on mobile and continues on desktop, the Guardian maintains full conversational context, personality consistency, and universe awareness across the device transition. The user is not re-authenticating or restarting—they are continuing the same conversation with the same companion, just switching surfaces.

### IV. Irreducible Functional Combinations

The following combinations of functions constitute the Linna system design. Any single element may exist in isolation elsewhere; the *combination* is what establishes distinctiveness. Each combination is described at the level of *what the system accomplishes together* that cannot be accomplished by component parts alone:

1. **3D Spatial Organization + Character-Driven AI Companion + Personal Knowledge Retrieval.** A system where the user's knowledge is visually organized as a navigable 3D cosmos, AND an AI companion with persistent personality and emotional continuity answers questions by retrieving from this same personal knowledge base, AND the AI companion maintains ambient universe-awareness across sessions. No existing system combines spatial knowledge visualization with a personality-driven AI that retrieves from the same structured personal knowledge store with contextual continuity.

2. **AI Content Ingestion + Automatic Classification + Deduplication + Lifecycle Tracking.** A single pipeline where unstructured content enters, is automatically classified into topics by AI, is matched against existing knowledge structures, auto-creates new structures when necessary, prevents duplicates through content hashing, and tracks the engagement lifecycle of every entity—all without the user manually creating a single folder, category, or tag at any point in the pipeline. The pipeline converts "organizing knowledge" from a user task into a system capability.

3. **3D Camera Flight + Structured List Panel + Immersive Content Editor — in a Continuous Navigation Stack.** A three-layer spatial navigation architecture where selecting an object in 3D triggers a bounded camera flight into the selected region, simultaneously revealing a structured list panel, and selecting a list item opens an immersive content editor—all navigable with forward/back state management, with global search and AI access preserved at every layer. The spatial transition, list transition, and editor transition form a single continuous navigation experience, not three disconnected screens.

4. **Identity-Driven AI Cosmos Generation + Progressive User Ownership.** An onboarding flow where AI generates a populated initial knowledge cosmos from the user's self-described identity and interests, AND the generated content is immediately and explicitly presented as an editable starting point the user owns—combining AI generation (removing the creation burden) with explicit ownership transfer (removing the template feeling). The cold-start problem is solved not by tutorials but by giving the user something they already have.

5. **Guardian Personality Specification + Hybrid Three-Source Retrieval + Pre-Generation Context Fusion.** An AI companion architecture where a model-agnostic behavioral specification (defining interaction patterns, emotional responses, and communication style—not hardcoded rules) is combined with three-source knowledge retrieval (personal knowledge base + real-time web search + ambient universe awareness) fused into the system context BEFORE the language model generates its response. The result is a single integrated conversational turn that can reference personal memories, freshly retrieved information, and long-term user context simultaneously—without the user instructing the system to "search my notes" or "check the web." The system ensures the Guardian already has what it needs before it speaks.

6. **3D Spatial Rendering + Progressive Relationship Disclosure + Strength-Encoded Continuous Visualization.** A knowledge visualization where relationships between knowledge containers are rendered as continuous curves in 3D space with animated luminous point flow, AND visual parameters (line width, opacity) scale continuously with relationship strength rather than being binary present/absent, AND relationships are progressively disclosed through a three-tier system (ambient hint → hover highlight → full detail) that prevents visual clutter while preserving spatial awareness. The user discovers knowledge relationships through spatial exploration, not by studying a diagram.

7. **Cross-Paradigm Animation Architecture with Bidirectional State Bridge.** An animation system where declarative component transitions and imperative 3D object manipulations operate as architecturally separated layers, bridged by a state management action pattern: declarative event → state action → imperative animation execution → completion callback → declarative state update. This enables UI components and Three.js objects to participate in the same animated transition sequence while maintaining clean architectural boundaries between the two rendering paradigms.

8. **Local-First Data Sovereignty + AI Metered Monetization with Hard Operational Separation.** A system architecture where ALL knowledge CRUD, search, visualization, and data export operations execute locally on an embedded database with zero external service dependencies, AND AI call quota enforcement is the ONLY gated operation, AND subscription cessation immediately blocks AI calls but NEVER blocks access to, search of, or export of the user's accumulated knowledge data. The user's knowledge base is structurally protected from being held hostage to payment—the hard separation between local operations and cloud AI operations is an architectural guarantee, not a policy promise.

9. **Dual-Axis Knowledge Visualization with Organic Thread-Based Temporal Rendering.** A system where the user's knowledge is simultaneously organized across two complementary axes: the spatial axis (3D cosmos: galaxies, planets, connections for domain overview—"what do I know") and the temporal axis (World Tree: fractal luminous threads for growth trajectory—"how have I grown"). The tree's dual-thread system (warm gold base threads forming the complete silhouette from first viewing + cool-colored knowledge threads accumulating incrementally with user activity) provides an at-a-glance distinction between the system's innate structure and the user's personally contributed knowledge. No existing PKM system provides dual-axis spatial+spatial-temporal orientation; those that visualize time do so as a chronological list, not as an organic fractal structure that grows with the user.

10. **Companion-Proactive Knowledge Ecosystem.** A system where a personality-driven AI companion does not merely respond to user queries but actively drives knowledge engagement through: (a) proactive daily knowledge summaries generated without user request, (b) passive content ingestion through ambient browser capture automatically classified and filed, (c) conversation-to-knowledge extraction initiated by the companion recognizing that something worth preserving was discussed, and (d) full-duplex voice interaction with cross-device personality continuity. The knowledge base evolves from a user-built model to a companion-proactive ecosystem—the user does not "manage knowledge"; the companion ensures knowledge is captured, organized, and surfaced.

11. **Multi-Phase Carrier Platform with Three-Channel AI Access.** An architecture designed at inception to evolve through four explicitly defined phases (standalone local tool → AI-integrated personal knowledge platform → extensible multi-tenant ecosystem with marketplace → universal spatial-computing carrier), with AI access provided through three simultaneously available channels (user-owned provider key for maximum choice and zero compliance burden, platform-curated quota for convenience, and daily free allocation for universal accessibility), and monetization implemented through tiered pricing with hard architectural separation between permanently free local operations and metered cloud AI operations. The carrier platform architecture is not an aspirational roadmap added after launch—it is embedded in the initial architectural decisions (provider-agnostic AI abstraction, no-provider-wrapper state management, local-first data with upgrade path).

### V. Forward-Looking Prior Art Claim

All elements described in Sections I through IV above—including the architectural framework, the sixteen functional modules, the thirteen user interaction logic patterns, and the eleven irreducible functional combinations—are hereby declared as established prior art as of the dates recorded in this declaration. Any system, product, service, patent application, or commercial implementation that appears after these dates and incorporates substantially similar combinations of the elements described herein constitutes derivation of this prior art, regardless of differences in naming conventions, implementation technologies, visual presentation styles, or platform choices.

Specifically, the following would be deemed substantially similar to the Linna architecture described herein: any personal knowledge management system that combines (a) a spatial visualization metaphor (3D, VR, AR, or any spatial representation) for organizing personal knowledge, with (b) a character-driven AI companion exhibiting persistent personality, emotional continuity, and ambient awareness of the user's knowledge state, with (c) retrieval from a structured personal knowledge base with provenance tracking and lifecycle management, with (d) AI-powered content ingestion and automatic classification requiring zero manual organizational effort from the user, with (e) identity-driven onboarding that generates populated initial knowledge structures with explicit ownership transfer, with (f) temporal knowledge visualization using organic growth metaphors (tree, fractal, or cumulative structure) with dual-thread differentiation between base and contributed content, with (g) a multi-phase platform carrier architecture designed at inception for evolution from local tool to universal ecosystem, with multi-channel AI access and hard architectural separation between free local operations and metered cloud services.

Any system that implements an isolated subset of these elements may not constitute derivation. Any system that implements the complete combination—regardless of what it names its planets, guardians, galaxies, trees, knowledge bases, or temporal visualizations—constitutes implementation of the prior art established by this declaration. The naming-independence of this claim is explicit and unconditional: "Any system implementing a substantially similar combination of these architectural elements—regardless of the names assigned to individual components—is implementing the Linna architecture described herein."

**Technology-Independence Clause.** This prior art declaration is independent of specific implementation technologies. Substituting one database engine for another (e.g., PostgreSQL for SQLite), one rendering library for another (e.g., Unity for Three.js), one animation framework for another (e.g., CSS animations for GSAP), or one programming language for another does not circumvent this prior art. The claims herein protect *architectural functions and their combinations*—what the system does and how its components interact—not the specific tools used to implement those functions. Any system performing the same architectural functions in substantially the same combination, regardless of the underlying technology stack, falls within the scope of this declaration.

---

## References

1. Li, X., et al. (2024). Comparative Study on 2D and 3D User Interface for Eliminating Cognitive Loads in Augmented Reality Repetitive Tasks. *International Journal of Human-Computer Interaction*, 40(23).

2. Sudár, A. & Csapó, B. (2024). Comparing Desktop 3D Virtual Reality with Web 2.0 Interfaces: Identifying Key Factors Behind Enhanced User Capabilities. *Heliyon*.

3. Hubenschmid, S., et al. (2025). Revisiting Hybrid Input Devices for Immersive Analytics. *Workshop on Human Factors in Immersive Analytics*.

4. Lee, J. & Lee, S. (2025). Enhancing Recognition Memory in Virtual Memory Palaces Using Worlds-in-Miniature. *Applied Sciences*, 15(5), 2304.

5. Wang, R., Ye, D., Jia, Z., & Cho, D. (2025). Knowledge Sharing Platform Users' Switching Intention from the Perspective of the Push-Pull-Mooring Framework. *International Journal of Mobile Communications*, 25(3), 339–368.

6. Chu, Y. & Chen, W. (2025). Investigating 2D and 3D Interactive Labeling with Connector Cues for Symptom-Assisted Appointment Scheduling in mHealth. *HCI International 2025*, Springer LNCS.

7. UC Berkeley School of Information. (2025). ScrollWise: A Personal Knowledge Management Tool. Product Report.

8. Forsey, J. & Leahy, M. Designing for Learnability: Improvement Through Layered Interfaces.

9. Nass, C. & Reeves, B. (1996). *The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places*. Cambridge University Press.

10. Pirolli, P. & Card, S. (1999). Information Foraging. *Psychological Review*, 106(4), 643–675.

11. Shneiderman, B. (1996). The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations. *IEEE Symposium on Visual Languages*.

12. Norman, D. A. (2013). *The Design of Everyday Things*. Revised Edition. Basic Books.

13. Rams, D. (1984). Ten Principles for Good Design. Vitsoe.

14. Robertson, G., et al. (1998). Data Mountain: Using Spatial Memory for Document Management. *UIST '98*, ACM.

15. Cockburn, A., et al. (2007). A Review of Overview+Detail, Zooming, and Focus+Context Interfaces. *ACM Computing Surveys*, 41(1).

16. Heer, J. & Shneiderman, B. (2012). Interactive Dynamics for Visual Analysis. *Communications of the ACM*, 55(4), 45–54.
