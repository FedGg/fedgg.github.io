---
title: Setting Up Ontology In Tana And  Obsidian With Claude Code Pipeline
---

Now I have the full picture of Bri's OCP and how it shaped your system. Let me reflect on the philosophy before we get into specifics.

---

## What Bri's OCP gave you — and where you outgrew it

Bri's system rests on a beautifully simple premise: everything in your workspace is either an **objective** (something you're working toward), a **task** (an action that advances an objective), or an **input** (information that supports a task or objective). Three base tags, everything extends from one of them, and a single "Parent" field is the only required connection. The system works because of that radical simplicity — you can dump anything into your daily note and it self-organises.

You adopted this architecture. Your `#input` became the parent of `#note`, `#resource`, and `#update`. Your `#source` became a parallel to `#input` — a base tag for things you consume (articles, books, films, podcast episodes). And your `#objective` / `#task` side largely followed Bri's pattern.

But you needed something Bri explicitly didn't build: a **knowledge management layer** with real ontological structure. Bri treats PKM and productivity as separate systems (she says so directly). Her `#resource` tag is just "external sources or media" with a Parent field — she doesn't distinguish an article from a book from a podcast episode at the tag level. She doesn't need to, because her system is about getting things done, not about building a structured knowledge base.

You do need that distinction. You're not just tracking what you've read — you're building a library of interconnected references with authors, publishers, topics, and relationships between them. That's a fundamentally different problem, and it's why you ended up with 200 supertags instead of Bri's 6-8.

---

## The philosophical tension in your current system

Here's what I think is the core issue. You have two competing organisational logics:

**Logic 1 (from Bri/OCP): Everything relates to an objective through a Parent field.** This is a productivity logic. It answers "what is this *for*?" A book exists because you're reading it toward some goal. An article exists because it supports a task. The relationship is functional.

**Logic 2 (your PKM instinct): Things have intrinsic properties and relate to each other by what they *are*.** A book has an author, a publisher, a language, topics. An author wrote multiple books. A publication publishes multiple articles. These relationships exist regardless of whether you're pursuing any objective. The relationship is ontological.

Your `#source` and `#media` hierarchy is Logic 2. Your `#input` → Parent field is Logic 1. And right now they're entangled — `#article` *was* extending `#input`, `#book` still extends `#source`, and `#source` itself was originally an OCP concept (a type of input).

**The question of whether to sever `#book` from `#source` is really the question: should your reading/reference types inherit from a *functional* parent (what role does this play in my workflow?) or should they be *structurally independent* types that happen to share some properties?**

---

## My recommendation

Sever them all. Make `#article`, `#book`, `#film`, `#podcast episode` independent types with no shared parent tag.

Here's why:

**The shared fields are few and shallow.** What do all source types actually share? A URL (Media Source), Topics, and maybe a status (To Read / Reading / Read). That's it. Author means different things for a book vs an article vs a podcast. Publisher vs Publication vs Podcast are structurally similar relationships but point to different entity types. The inheritance buys you almost nothing — you're overriding most fields on each child tag anyway.

**Inheritance creates coupling you don't want.** If you add a field to `#source`, it appears on every child. If you change how `#source` works, everything downstream is affected. With 100+ book nodes and growing, that's a real risk. You already hit this with `#article` — severing `#input` was the right call, and you'd be doing the same thing to `#book` for the same reasons.

**Bri's own principle supports this.** Her rule is: figure out the minimum number of tags, and use extends only when the child truly behaves like the parent with additions. Your source types don't behave like each other — they share a vague family resemblance but have genuinely different field sets, different workflows, and different entity relationships.

**What you lose is trivial.** The only thing `#source` inheritance gives you is "find all sources" as a single search. You can achieve the same thing with a search across multiple tags (`#article OR #book OR #film OR #podcast episode`). That's a minor convenience, not a structural necessity.

---

## The hierarchy I'd propose instead

Rather than a tree of inheritance, think of it as **two parallel families of independent types connected by fields, not by extends**:

**Works** (things you consume or create — each an independent type):
- `#article` (with sub-tags: `/academic`, `/press`, `/web`) ✅ already done
- `#book` — sever from `#source`
- `#film`
- `#podcast episode`
- `#album`
- (future: `#show`, `#video`, etc.)

**Entities** (things that produce, distribute, or relate to works — also independent types):
- `#author` (or more broadly `#person` with role fields)
- `#publication` (newspaper, magazine, journal, blog)
- `#podcast` (the show, not the episode)
- `#publisher` (book publishers)
- `#organisation`
- (future: `#platform`, `#channel`, etc.)

**The connections between them are fields, not inheritance.** An article has a "Published in" field pointing to a `#publication`. A book has a "Publisher" field pointing to a `#publisher` (or `#organisation`). A podcast episode has a "Podcast" field pointing to a `#podcast`. These are all the same *kind* of relationship — "this work was produced/distributed by this entity" — but expressed through type-specific field names that make sense in context.

**Shared conventions, not shared parents.** Every work type has: a name, a Media Source (URL), Topics, and a status. But these are conventions you enforce through your schema documentation, not through tag inheritance. In practice this is what you're already doing — your `#article` and `#book` schemas are independently designed with parallel field patterns.

---

## What this means for the `#source` and `#media` base tags

`#source` becomes unnecessary as a parent tag. It can be retired (not deleted — Bri's own principle of keeping template references applies). Same for `#input` where it's still in use.

`#media` is more interesting. Your entity types (publication, podcast, newsletter, platform) do share more genuine structure than your work types do — they all have a name, a URL, a geography, a language, and they all serve as the "Published in" target for some work type. There's a stronger case for keeping `#media` as a parent here, *if* you find yourself wanting to search "all media entities" as a group. But I'd still lean toward independence for the same reasons — the coupling risk outweighs the search convenience.

---

The next question is: do you want to map this out as a concrete schema (fields per type, relationships between types) for the reading/writing workflow specifically? Or do you want to challenge any of the above first?

---

→ You are correct. My aim is to build my 'living' knowledge graph out of relations between ideas, concepts and stories.
I think of it in terms of ontological relationships. Happy to go with logic 2 as you called it. But I'd like to map it out conceptually.

My priority is to organise my creative workflow, connecting and being able to refer to and use ideas as I develop my writing. 

Currently I often fall into the 'collector's fallacy': I save lots of things I find, as they inspire thoughts and connections related to my philosophical, literary, political or creative enquiry. I want a way to manage that flow effectively so that those references are available as and when I need them, but they do not overwhelm my inbox.

My process goes like this: I read a book, article, blog post or listen to a podcast, and highlight (a lot), knowing I can access it later though Readwise, which syncs to both Tana and Obsidian. Sometimes I write a note about an idea which comes as I read, or watch a film, and so on for all the media I consume. These highlights and notes are saved in my graph — generally in Tana first, but for longer notes I tend write in markdown files which I save in my Obsidian AllNotes folder.

All of these highlights and notes would become much more accessible and useful once I tag them and connect them in Tana, Obsidian or both.

In Tana the 'ideas' ontology is fragmented in multiple supertags. I attach a snapshot:

The most important elements for my writing workflow are:

- `#writing inbox` – notes about things I am planning to write. these may be short or longer than fleeting notes
- `#fleeting notes` 

Also to note:

- I made `#thoughts` as a root tag for the above, which allows me to filter them without distinguishing between the two
- `#day notes` also extend `#thoughts` and was intended for journaling-type entries.
- `#ideas` is an older tag, based on the more generic `#note` tag from an earlier schema. 
- I also realise that `#note` extends `#input` which makes no sense for my own ideas and notes which are more of an output.

The other important set are the inputs, i.e. the reference notes from reading and other media consumption. e.g. `#article`, `#book`, `#film`, `#podcast episode` etc.

The reason I grouped them under a generic `#source` tag was to allow the 'options from tag' in some of the entities' fields to pick up on multiple types of objects. This is Tana specific, and does not have to complicate my overall ontology unnecessarily. Happy to look at an alternative solution and severe the parent relationship if that's cleaner/simpler.

I enclose a snapshot of some of these tags. You can see for instance there are multiple `#podcast` tags, although I only use one (the (★) helps me identify which).

I also attach a snapshot of the more complex Tanarian Brain system which I have used in part. Supertags or fields in my schema with (TB) or (★) are adaptations from there.

So I'm generally on board with your recommended hierarchy principles.

With these observations in mind, let us map this out for the reading and writing workflow.

---

Good — this is exactly the right level to work at. Let me synthesise what you've shown me and map it out.

From your screenshots I can see the current state clearly. In particular, the third screenshot confirms the inheritance chains: `#podcast episode` and `#podcast episode (★)` both extend `#source`, `#podcast (★)` extends `#publication`, `#film (★)` extends `#source`, `#book` is now independent (we severed it), and `#article` is independent (severed from `#input`). The Tanarian Brain template shows the maximalist version — 25+ source types, status tags for reading stages, publications as a separate branch, and source-specific fields (Title, Publication Date, Author).

Let me map out your actual reading and writing workflow as a unified ontology, incorporating what you've told me about how you actually work.Here's your reading and writing workflow mapped as an entity model. A few things to note about what this diagram represents and the decisions it embeds:

**The top half** is your reference library — works you consume on the left, the entities that produce them on the right. Each work type is independent (no `#source` parent). The arrows between them are *fields*, not inheritance — `Author(s)`, `Published in`, `Podcast`, `Publisher`. This is the pattern you've already proven with `#article` and `#book`.

**The middle band** is your thinking layer — where your own ideas live. I've grouped them into three types that map to your existing Obsidian categories: `#thoughts` (which covers your `#fleeting note`, `#writing inbox`, and `#day notes` — unified under one parent since you already use `#thoughts` as a root tag for this purpose), `#concept` (atomic ideas that mature toward evergreen), and `#reference note` (your synthesis of what you've read — distinct from the source itself). The status bar underneath shows the agreed progression.

**The bottom band** is the connective tissue — `#topic`, `#highlight`, and `#quote`. These aren't works or ideas in themselves; they're the links between them. Topics tag everything. Highlights flow from Readwise into both Tana and Obsidian, connecting to the source they came from. Quotes are specific passages you want to reference.

**What's deliberately missing:** the `#source` parent tag, the `#input` parent tag, the `#media` parent tag, and the Tanarian Brain hierarchy. Also missing: task management, CRM, and project types — those are a separate domain for later.

**Open questions this surfaces:**

Your `#thoughts` root tag currently groups `#fleeting note`, `#writing inbox`, and `#day notes`. Should these remain as sub-tags extending `#thoughts`, or should they collapse into one type with a field distinguishing them? Given Bri's principle of minimum tags, I'd lean toward one `#thought` type — the distinction between a fleeting note and a writing inbox entry is really about *intent*, which you know when you write it but doesn't need a structural separation.

Your `#person` vs `#author` distinction — in Tana you have `#person (★)`, `#author (★)`, `#host (★)`, `#editor (★)` as separate tags. Do these need to remain separate, or could `#person` be the one type with role fields? An author is a person who wrote something; the "author" role is expressed by the `Author(s)` field on `#book` or `#article` pointing to them.

The `#highlight` / `#quote` / `#Readwise` relationship — how do you want to handle the fact that Readwise creates its own nodes in a separate workspace? Are highlights a type in your ontology, or just a Readwise artifact you reference?

Click any box in the diagram to explore a specific type, or tell me which of these questions you want to tackle first.

---

→ Let's design the thoughts / fleeting notes schema

Good question to start with — this is where your own thinking lives, and it's the part of the system that most directly serves your writing.

Let me lay out what you currently have, then propose a clean design.

---

## Current state in Tana

From your screenshots and session files, you have:

- `#thoughts ★` — root tag, used as a filter to see all your thinking in one place
- `#fleeting note (★)` — extends `#thoughts`, for quick captures ("thoughts, ideas, comments" per Tanarian Brain)
- `#writing inbox` — extends `#thoughts`, for notes about things you're planning to write
- `#day notes` — extends `#thoughts`, intended for journaling-type entries
- `#ideas` — older tag, extends `#note` (which extends `#input`), from an earlier schema

And in Obsidian, the parallel categories are:

- `[[Concepts]]` — atomic ideas (50 notes)
- `[[Propositions]]` — claims, arguments (17 notes)
- `[[Fleeting Notes]]` — deprecated as a category, folded into `status: seed`
- `[[Drafts]]` — deprecated as a category, folded into `status: draft`

So the landscape is fragmented: Tana has multiple sub-tags under `#thoughts`, Obsidian moved away from type-based distinctions toward status-based ones, and `#ideas` sits orphaned under the old OCP `#input` chain.

---

## The design question

You said something important: `#note` extends `#input`, which makes no sense for your own ideas which are more of an output. That's exactly right. Your thoughts aren't inputs to an objective — they *are* the work. They're the raw material of your writing, not supporting information for a task.

So the question is: how many distinct types do you actually need for your own thinking?

I see three options, from simplest to most structured:

**Option A — One type, status does the work.** A single `#thought` tag. Whether it's a fleeting capture, a journaling entry, or a writing plan is expressed by how developed it is (status: seed → draft → active → evergreen) and what it links to (topics, sources). No sub-tags at all. This is the most Bri-like approach.

**Option B — One root type with two sub-types.** Keep `#thought` as the root, with `#thought/note` (fleeting captures, journal entries, quick ideas) and `#thought/writing` (things you intend to develop into publishable writing). The distinction is functional: a writing thought has a destination — it's going somewhere. A regular thought may or may not.

**Option C — Keep three sub-types as you have them.** `#thought/fleeting`, `#thought/writing`, `#thought/journal`. Each behaves slightly differently, each has its own fields.

My instinct is **Option A** for Tana, with a nuance. Here's why:

The difference between a fleeting note and a writing inbox entry is *intent at the moment of capture*. But intent changes. A fleeting thought about media ownership while reading might become the seed of an essay. A journaling entry about a conversation might surface an argument worth developing. If these are separate types, you have to reclassify them when their role changes. If they're one type with a status, the note just grows — seed becomes draft becomes active. The type doesn't change because the type was always "my thought."

The journaling case is the one exception worth considering. Journal entries are time-bound and personal in a way that ideas and writing plans aren't. But in Tana, journal-like entries naturally live in your daily note as child nodes — they don't need a separate type to be findable. They're findable by date.

---

## Proposed schema

```
#thought  ← single canonical type (replaces #thoughts ★, absorbs all sub-types)

  Fields:
  - Topics         instance of #topic, multi-value
  - Related        instance of #thought OR #article OR #book etc., multi-value
  - Source          instance of #article / #book / #podcast episode (what prompted this thought)
  - Status          options: seed · hypothesis · draft · active · evergreen
  - Media Source    url (optional — if this thought has a reference URL)
```

**What each field does:**

`Topics` connects the thought to your knowledge graph — same as on every other type. This is how you find it later.

`Related` is for lateral connections — other thoughts, concepts, or sources that relate to this one. This is the Zettelkasten link layer.

`Source` is specifically "what I was reading/watching when I had this thought." It's the provenance. A fleeting note while reading Mazzucato would point to `The Common Good Economy` here. This replaces the old OCP `Parent` field — instead of "what objective does this support," it's "what triggered this thinking."

`Status` does the work that sub-types used to do. A quick capture is `seed`. An idea you've started developing is `draft`. Something you've articulated clearly and want to keep is `active` or `evergreen`.

**What gets retired:**

- `#fleeting note (★)` — becomes `#thought` with `status: seed`
- `#writing inbox` — becomes `#thought` with `status: draft` (or seed, depending on how developed it is)
- `#day notes` — journal entries stay as plain child nodes in your daily note, no tag needed. If you want to tag some for retrieval, use `#thought` with a `Journal` topic.
- `#ideas` — absorbed into `#thought`, severed from `#note` → `#input`
- `#thoughts ★` — replaced by `#thought` (singular, cleaner)

**Obsidian mapping:**

In Obsidian, these become notes with `category: "[[Concepts]]"` (for ideas that reach atomic/evergreen status) or `category: "[[Propositions]]"` (for claims and arguments). The `status:` field tracks progression. Raw captures live in `AllNotes/` as seeds; developed thoughts move to `_Notes/` when they mature. No separate template needed for fleeting vs writing — the `Seed Template` handles initial capture, and the note grows from there.

---

Two things I'd like your input on before we finalise:

First, the `Source` field — is this useful to you in practice? When you capture a thought while reading, do you typically want to trace it back to the specific book or article, or is the topic connection sufficient?

Second, journaling — do you actually want to retrieve journal entries by type later, or are they more ephemeral? If ephemeral, they don't need a tag at all. If you browse them, a `#thought` with a `Journal` topic works. If they're a genuinely different activity for you (more reflective, less idea-oriented), then Option B might be worth it after all.


---


→ An important observation on Concepts:

`[[Concepts]]` in Obsidian (and in Tana) are not my atomic notes, although I might write some focused on a specific concept. They are separate cards (notes) generally holding a definition and primary sources for a concept. It extends `#term`. Some entries may be at once a concept, a term and a topic. This needs to be disticnt from a thought I may have about it. For instance "Brand" is both a `#concept` and a `#topic`. "Brand is a story connecting people" is my `#thought` (and an atomic idea). You could call that a concept too, but I need to differentiate the terms.

Of the three options, I appreciate the logic and the simplicity of A, but for my own clarity I would find it easier to set a tag in one step (e.g. option C) rather than having to set the tag and the status. Also B might work. The status might change for a writing note from seed to evergreen. A writing note at seed stage is still more than a fleeting thought.

There are also other notes I use for analytical and synoptical reading (Adler, Ahrens) such as `#reference` `#literature` notes and other Zettelkasten inspired versions (screenshot attached). This are important from my reading to writing workflow, where I produce atomic notes from reading, referencing, paraphrasing and rewriting, and generating my ideas. You should see the Obsidian taxonomy we are developing in the _Claude files I supplied, if not let me know.

To your questions: yes the `Source` field as defined is useful. Journal entries help me trace back the origins of an idea, although generally I would copy the relevant passages in a new note when I see potential. I still like the idea to be able to go back and review the journal entries though. I could do this in day pages, but that also contains a lot of other unrelated stuff.

---

This is really helpful — the screenshots clarify a lot. Let me work through what you've shown me.

---

## What I now understand better

**Concepts are not your ideas — they're reference objects.** `#concept` extends `#term`, and a term is defined as "a word or two used as the index and the rails to traverse the Zettelkasten." So "Brand" as a `#concept` is a card holding a definition, sources, and related terms. It's a building block of your knowledge graph — more like an encyclopedia entry than a personal thought. Your *thought* about Brand ("Brand is a story connecting people") is a separate entity — it's your atomic idea, your claim, your proposition. This is an important distinction that I conflated in the diagram.

**The Zettelkasten-inspired reading workflow has more structure than I mapped.** From your second screenshot I can see: `#evergreen (★)` for elaborated, synthesised atomic notes; `#permanent note` (from Zettelkasten tradition, not actively used); `#reference` which extends `#source` for notes about sources; `#literature note (★)` for your own thoughts responding to material; `#research` which extends `#z-note`. These all serve distinct roles in the Adler/Ahrens reading-to-writing pipeline.

**On Option A vs B vs C:** You're telling me that the *act of tagging* is a classification step you want to be meaningful in one move. Setting `#thought` plus `status: seed` is two decisions; setting `#fleeting note` is one. And a writing note at seed stage is qualitatively different from a fleeting thought — it already has direction, even if it's undeveloped. That's a real distinction, not just a status difference.

---

## Revised proposal — Option B, adapted

I think B is the right balance, but let me reframe it in light of everything:

```
#thought  ← root tag (for filtering all your thinking)

  ├── #thought/fleeting     ← quick captures, sparks, observations
  │     Default status: seed
  │
  ├── #thought/writing      ← notes about things you intend to write
  │     Default status: seed (but means more — has direction)
  │
  └── #thought/journal      ← reflective, time-bound entries
        Default status: seed
```

**Why this works for you:**

One tag per capture — you decide at the moment of writing whether this is a spark (`/fleeting`), a writing plan (`/writing`), or a journal reflection (`/journal`). No second step needed.

The root `#thought` gives you the filter you already built — see all your thinking in one search, regardless of sub-type. This is exactly what your current `#thoughts ★` does.

Journal entries become retrievable by type. You can search for all `#thought/journal` entries on a topic to trace the origin of an idea, without wading through task lists and other daily note clutter.

**Fields on the root `#thought` (inherited by all sub-types):**

```
- Topics         instance of #topic, multi-value
- Source          instance of #article / #book / #podcast episode etc.
                  (what prompted this thought — the provenance)
- Related         multi-value (other thoughts, concepts, terms)
- Status          seed · hypothesis · draft · active · evergreen
- Media Source    url (optional)
```

**No additional fields on the sub-types** unless you find you need them. The sub-types exist purely for classification and filtering, not for different field sets. This keeps it lean — Bri's principle of minimum fields still applies.

---

## Where this sits relative to the rest of your reading-to-writing pipeline

This is the part I got wrong in the diagram. Your pipeline isn't just "works → thoughts." It has a structured middle layer for analytical reading. Here's how the full chain looks:

**Sources** (what you consume): `#article`, `#book`, `#film`, `#podcast episode`
↓ *you read, highlight, annotate*
**Highlights**: `#highlight` / Readwise sync — passages you marked
↓ *you reflect, paraphrase, respond*
**Literature notes**: `#literature note` — your own words responding to the material
↓ *you synthesise, connect, abstract*
**Reference notes**: `#reference` — distilled knowledge from sources
↓ *you think, argue, create*
**Thoughts**: `#thought/fleeting`, `#thought/writing`, `#thought/journal` — your own ideas
↓ *you develop, refine, mature*
**Atomic notes**: `#evergreen` — elaborated, synthesised, stable ideas

**Concepts / Terms** (`#concept`, `#term`) sit alongside this pipeline, not in it. They're the index — the vocabulary you use to connect everything. "Brand" as a concept is a node that thoughts, literature notes, reference notes, and highlights all link *to*.

---

## The question this raises

Your `#evergreen (★)` and `#concept` currently serve different purposes — evergreens are your mature atomic ideas (like the ones in your screenshot: "It takes a lot more to change a culture than to devise a new strategy"), while concepts are definitional reference cards. But in Obsidian, you've been using `[[Concepts]]` as the category for atomic notes. 

Do you want to keep this separation in both systems? My suggestion: yes — they're genuinely different things. A concept/term is a *what* (a definition, a reference card). An evergreen is a *so what* (your synthesised position, your claim). In Obsidian terms, concepts could map to a `[[Terms]]` or `[[Concepts]]` category, while evergreens map to `[[Propositions]]` or stay as `[[Concepts]]` with `status: evergreen`. 

What's your instinct on this? And does the revised Option B feel right for the thoughts layer?

---

That's much better. 

A note on `#reference` notes. I have been using that to classify things I want to reference, but at a stage prior to my synthesis (in a corresponding `#literature` note), not after.

I forgot to include the `#garden card (★)` supertag I used to indicate in Tana the notes which were meant to get published (`#garden` tag in Obsidian). See screenshot.

Yes, definitely keep the separation between concepts and evergreens in both systems. I can use `[[ideas]]` rather than concepts in Obsidian too. I can use either the term 'ideas' or 'thoughts' in both places, I am using them interchangeably. I call the website where I publish my writings "Ideas Garden"

I really want to keep the two systems aligned. For as long as I use them both they need to feel interoperable.


---

This is coming together well. Let me integrate what you've just clarified and map the full picture.

---

## Key clarifications incorporated

**Reference notes come *before* literature notes**, not after. Your pipeline is: you read a source → you capture/distill what it says (`#reference`) → you write your own response to it (`#literature note`). This is the Ahrens sequence: reference notes are "what the author said," literature notes are "what I think about what the author said."

**`#garden card (★)`** is your Tana-side marker for notes intended for publication. It mirrors the `#garden` tag in Obsidian and connects to your "Ideas Garden" site. The garden card has rich fields: Growth stage, Related files, Motivation, Audience, Progress status, Topics, Parent (pointing to the Ideas Garden project). This is essentially your publishing metadata layer.

**Ideas = Thoughts = your atomic notes.** You use the terms interchangeably, and the site is called "Ideas Garden" — so `ideas` is the natural term for your own thinking. `#concept` / `#term` stays separate as reference cards for definitions.

**Interoperability is a hard requirement.** The same entity type should be recognisable in both systems, even if the implementation differs (supertag in Tana, category + frontmatter in Obsidian).

---

## The full reading-to-writing pipeline, corrected

Let me redraw this with the right sequence and the garden card layer:This is your reading-to-writing pipeline as a seven-stage flow, with the index layer (concepts, terms, topics) running alongside it.

A few things to note about the naming and cross-system alignment:

**I've switched from `#thought` to `#idea`** as the root tag. Since you use "ideas" and "thoughts" interchangeably, and your site is called "Ideas Garden," `#idea` creates a cleaner through-line: ideas grow into evergreens, evergreens become garden cards. The metaphor holds all the way through. In Tana, `#idea` replaces `#thoughts ★` as the root, with `/fleeting`, `/writing`, and `/journal` as sub-types.

**The Obsidian mapping for each stage:**

| Tana | Obsidian category | Obsidian folder |
|---|---|---|
| `#article`, `#book`, etc. | `[[Articles]]`, `[[Books]]`, etc. | `References/` |
| `#highlight` | (Readwise sync) | `Readwise/` |
| `#reference note` | `[[Reference Notes]]` | `AllNotes/` |
| `#literature note` | `[[Literature Notes]]` | `AllNotes/` |
| `#idea` (all sub-types) | `[[Ideas]]` | `AllNotes/` → `_Notes/` when mature |
| `#evergreen` | `[[Propositions]]` with `status: evergreen` | `_Notes/` |
| `#garden card` | `tags: [garden]` | `_Notes/` (published via sync-garden.py) |

**One open design question:** Should `#evergreen` be a separate type, or is it just `#idea` with `status: evergreen`? In your current Tana setup, `#evergreen (★)` is its own tag with its own list of nodes. But functionally, an evergreen *is* an idea that matured. The argument for keeping it separate: it marks a qualitative threshold — not every idea will become an evergreen, and evergreens have a specific role (they're your stable, citable claims). The argument for merging: you already have the status field to track this, and a separate tag means reclassification when an idea matures.

Given that you prefer one-step tagging, I'd suggest keeping `#evergreen` as a separate tag rather than a status on `#idea`. An idea that matures gets retagged — which is a deliberate, conscious act that says "I'm promoting this." That feels right for your workflow. The `status` field on `#idea` then tracks the *development* of ideas that haven't yet reached evergreen status.

**The garden card layer** sits on top — any evergreen (or occasionally a mature idea) can get the `#garden card` tag when you're ready to publish. In Obsidian, this is just `tags: [garden]` in frontmatter. The garden card fields (Growth stage, Audience, Motivation, Progress status) are publication metadata that only matters in Tana, not in Obsidian — the publishing script only looks for the garden tag.

Does this pipeline feel right? And does the `#idea` naming work for you, or do you prefer `#thought`?

---

→ Excellent. I like `#idea` better than `#thought`. 
In Obsidian I have been differentiating `[[Ideas]]` (currently `[[Concepts]]`) from `[[Propositions]]`. `evergreen` is really the status for any of them (in Tana too). But as you suggest a tag can help with deliberate 'promotion'.

The reason I created the `[[Concepts]]` caregory has to do with the published `#garden` notes. To differentiate Concept cards (e.g. 'Strategy') from `[[Propositions]]` (e.g. 'Culture eats Strategy for breakfast'). There are also other categories for published notes: `[[Methods]]`, `[[Frameworks]]` and `[[Stories]]`.

Not all of these need to exist in Tana as well (since I tend to work in Obsidian when I get closer to the evergreen stage), but it wouldn't hurt to have a single set of terms I can use consistently across both.

---

This clarifies the picture nicely. The distinction you're drawing is between *what kind of idea it is* and *how developed it is*. Status tracks development (seed → evergreen). Category tracks the nature of the idea — and that nature matters especially at the publishing stage, because your garden readers see different kinds of cards.

Let me map this out:

---

## Your idea types (categories)

These are the kinds of atomic notes you produce. Each can exist at any status level, but they become most visible when they reach evergreen and get published:

**`[[Ideas]]`** — your atomic claims, positions, opinions. "Brand is a story connecting people." "Culture eats strategy for breakfast." These are what you currently call `[[Propositions]]` in Obsidian and `#evergreen (★)` in Tana. They're the core output of your thinking.

**`[[Concepts]]`** — definitional reference cards. "Strategy" as a term with a definition, sources, and related concepts. These map to your `#concept` / `#term` tags in Tana. They're not claims — they're the vocabulary.

**`[[Methods]]`** — how-to notes, processes, approaches. Procedural knowledge rather than declarative.

**`[[Frameworks]]`** — structural models, mental models, analytical lenses. A framework organises other ideas — it's a way of seeing.

**`[[Stories]]`** — narratives, anecdotes, case studies. The concrete material that illustrates or grounds your abstract ideas.

---

## How this maps across both systems

| What it is | Obsidian category | Tana tag | Notes |
|---|---|---|---|
| A claim or position | `[[Ideas]]` | `#idea` (sub-types: `/fleeting`, `/writing`, `/journal`) | Replaces `[[Propositions]]` |
| A definition card | `[[Concepts]]` | `#concept` (extends `#term`) | Already exists in both |
| A process or approach | `[[Methods]]` | `#method` | New in Tana, or just use Obsidian |
| A structural model | `[[Frameworks]]` | `#framework` | New in Tana, or just use Obsidian |
| A narrative or case | `[[Stories]]` | `#story` | Already exists in Tana (2 nodes) |

**The status field works the same across all of them:** `seed → hypothesis → draft → active → evergreen`. Any idea, concept, method, framework, or story can be at any stage of development.

**The garden tag is orthogonal:** any of these categories can be published. A concept card gets `tags: [garden]` just like a proposition does. In Tana, the `#garden card (★)` tag adds the publishing metadata (Growth stage, Audience, etc.).

---

## Do Methods, Frameworks, and Stories need to exist in Tana?

Your instinct is right — they probably don't, at least not now. You work in Obsidian when things approach evergreen, and that's where these categories matter most (for the published garden). In Tana, a method or framework in development would just be `#idea/writing` until it moves to Obsidian for final development.

But having the vocabulary aligned costs nothing. If you create `#method`, `#framework`, and `#story` tags in Tana with no fields (or just Topics), they're available if you ever want them, and the terminology is consistent. You don't have to use them actively.

---

## One naming decision

You said you'd rename `[[Concepts]]` in Obsidian to `[[Ideas]]`, which makes sense given your site name. But then what do you call the definitional cards? They're currently `[[Concepts]]` in Obsidian and `#concept` in Tana. Options:

**Keep `[[Concepts]]` for definitional cards, use `[[Ideas]]` for your claims.** This is clean — a concept is a thing, an idea is your take on it. The garden shows both.

**Rename the definitional cards to `[[Terms]]`** to match the Tana `#term` tag. Then `[[Concepts]]` is freed up if you ever want it for something else.

I'd lean toward keeping `[[Concepts]]` for definitions and `[[Ideas]]` for your claims. The words carry the right connotations — a concept is something you define, an idea is something you argue. And it maps naturally to what your garden readers would expect to see.

Does this feel right? If so, I can produce an updated pipeline diagram that includes the category layer and the cross-system mapping as a reference document.

---

Sounds good. One more point of precision: I would separate `[[Ideas]]` from claims. An idea is something I may be exploring, abstract or creative, not necessarily provable. A `[[Claim]]` (or Proposition) can be backed (or refuted) by evidence.

I would keep all three: Concepts, Ideas and Claims.


That's a meaningful distinction — ideas are exploratory and creative, claims are assertable and evidential. Three types, each with a different epistemic character.The key change from the previous version is stage 6 — the atomic notes layer now has three distinct types with different epistemic characters:

**Ideas** (`[[Ideas]]`) — exploratory, creative, abstract. "What if brand is really a form of storytelling?" These don't need to be provable; they're generative.

**Claims** (`[[Claims]]`) — assertable, evidential. "Culture eats strategy for breakfast." These can be backed or refuted. This replaces your current `[[Propositions]]` (or you could keep that term if you prefer — "propositions" and "claims" carry similar weight).

**Concepts** (`[[Concepts]]`) — definitional, referential. "Strategy" as a card with a definition and sources. These are the index, not your own position.

Methods, Frameworks, and Stories sit alongside as additional published categories — available in both systems but primarily used in Obsidian near the publishing stage.

All of these can be at any status level (seed through evergreen), and any of them can become a garden card when ready to publish. The status tracks development; the category tracks what kind of thing it is.

Want me to save this updated version as a file too? And shall we move on to designing the schema for a specific type — perhaps `#idea` with its sub-types and fields — or do you want to refine the overall map further?

---

→ Yes save as markdown for working in Tana and Obsidian with Claude Code. Make sure to include the idea types for Obsidian too

---

(add link to the file)


This is ready to drop into your `_Claude/` folder. It covers the full pipeline (stages 1–7), all the Obsidian category mappings including Ideas, Claims, Concepts, Methods, Frameworks, Stories, and the additional types (Essays, MOC, Research Notes), the entity layer, the index layer, cross-system alignment, tags to retire, and open decisions still pending.

When you open a Claude Code session, you can load this alongside your `CLAUDE.md` and `HANDOFF.md` to give it the complete ontological context for any implementation work.


---


Looks great. A few more points before I move to implementation stage.


## Principles 

— ok

## Sources

there may be more source types in use. need to rationalise


## Stages 1-7

— ok

## Entities

`#Publisher` can extend (is a type of) `#organisation`

## Index layer

should a `[[terms]]` category exist in Obsidian to mirror `#term` in Tana?

## Cross-system alignment

A `#garden card` in Tana is not necessarily published (yet) but denotes the intention to publish. So it corresponds to the obsidian `garden` tag but is not functionally equivalent. When the content is published, I save a Hookmark link (in the relevant Tana field) to the corresponding Obsidian file.

I can remove the (★) from confirmed tags in Tana. Add tag description if missing (it should be clear which tags are part of my schema)

## Tags to retire

`#note` is used heavily in Projects and Areas (using a mix of OCP and PARA) ontology. Ok to sever from `#input` but not to retire it. I'll have to address those parts of the schema as well at some point.

## Open decisions

`#Publisher` extends `#organisation` so `Publisher` field can point to it (both are valid)

`[[Claims]]` = `[[Propositions]]` Let us just use Claims in both systems

I am tempted to merge `Media Source` and `Url` no need to dupliate. However caution is required for merging, there are many nodes using one or the other, sometimes both. Important to keep links clickable (so using the system `url` field when present. There may be multiple `Url` / `URL` fields in the schema. Avoid confusion and use the system field when available. A careful plan for doing this needs to be devised, running tests to validate the method. Also important to  minimize token use / maximise efficiency. 

`status:` legacy values may overlap OCP / PARA schemas, which require different values than read/write workflow.


---

Good — these are all precise refinements. Let me update the document with your decisions and notes.Now I'll apply all your refinements:Now update the Claims reference in stage 6:Updated with all your refinements:

- `#publisher` extends `#organisation` — resolved, moved out of open decisions
- `[[Claims]]` confirmed as the term in both systems — resolved
- `#note` kept alive (severed from `#input` but not retired — OCP/PARA usage in projects)
- `#garden card` clarified as intent-to-publish, not published; Hookmark link added when actually published
- `[[Terms]]` question added for Obsidian index layer
- Source type audit flagged — more types may exist beyond the five listed
- URL/Media Source consolidation expanded with your caution about migration complexity and clickability
- Status migration note updated — legacy values may belong to project/area schemas, not just read/write
- Tag hygiene note added — remove `(★)` from confirmed tags, add descriptions

Ready for implementation whenever you are. The document replaces the version in your project files and should go into `_Claude/` for Claude Code to reference.

(revised ontology reference file)

---

→ re: open questions. On the `#person` tag I need the system needs more development. At least some of them should be separate. These are not just roles. They have different fields I use some for CRM (contacts). An author can also be a contact. I attach a snapshot of some of the related tags in Tana. Some simplification may be good, but I don't think a single tag would do. Can you make a suggestion.

---

This is a rich screenshot. Let me map what I see:

**Current person-related tags in Tana:**

| Tag | Extends | Purpose | Rough count |
|---|---|---|---|
| `#person (★)` | — (base) | Base CRM tag | many |
| `#contact` | `#person (★)` | "A person who I can connect with" | many (with email) |
| `#contact +` | `#contact` | "A contact with more details" | ~20 (with email, org) |
| `#author (★)` | `#person (★)` | "General Author tag" — writers of works | 70+ |
| `#host (★)` | `#person (★)` | "Video or Podcast Host" | ~30 |
| `#designer (★)` | `#author (★)` | Designers specifically | ~20 |
| `#partner` | `#contact +` | Business partners (with "Current Organisation") | ~15 |
| `#family` | `#person (★)` | Family members | ~10 |

So you have two distinct branches growing from `#person (★)`:

**The knowledge branch** — `#author`, `#host`, `#designer` — people who create works you reference. These connect to your reading/writing pipeline via `Author(s)`, `Host`, `Guests` fields on sources.

**The CRM branch** — `#contact`, `#contact +`, `#partner`, `#family` — people you interact with. These have email addresses, organisations, relationship data. This is a different domain entirely.

And crucially: **some people are both.** An author you've read might also be a contact you've met at a conference. A designer whose work you reference might also be a business partner.

---

## My suggestion: keep two branches, allow stacking

Don't collapse these into one tag. The fields are genuinely different — an author needs works, topics, and a bibliography link; a contact needs email, organisation, and relationship context. Forcing both into one tag means either bloating every person with irrelevant fields, or using "hide when empty" so heavily that the tag becomes opaque.

Instead, keep `#person` as a lean base, and let the branches serve their domains:

```
#person  ← base tag (shared fields only)
  Fields: name, Topics, Media Source (website/profile)

  Knowledge branch (reading/writing workflow):
  ├── #author        ← people who create works you reference
  │     No extra fields needed — the connection is made
  │     via Author(s) field on #article, #book, etc.
  │
  └── #host          ← podcast/video hosts
        No extra fields needed — connected via Host field
        on #podcast episode

  CRM branch (contacts and relationships — defer for now):
  ├── #contact       ← people you can reach
  │     Fields: Email, Organisation, Role
  │
  ├── #contact +     ← contacts with richer data
  │     Extends #contact, additional fields
  │
  ├── #partner       ← business partners
  │     Extends #contact +, adds Current Organisation
  │
  └── #family        ← family members
        Extends #person directly
```

**When someone is both an author and a contact**, they get both tags — Tana supports multiple supertags on a single node. Mariana Mazzucato as an `#author` connects to her books; if you meet her at a conference and add her email, she also gets `#contact`. The node is the same person; the tags express different relationships you have with them.

**What to drop:** `#designer (★)` extending `#author` feels like over-classification. A designer who writes is an author. The fact that they're a designer is better expressed through Topics (link them to `#topic` Design) or through the nature of the works they've created, not through a sub-type of author. Unless you have designer-specific fields that authors don't need?

**Obsidian mapping:** In Obsidian, the person branch is simpler — you have `[[People]]` as a single category in `References/`. Whether someone is an author, host, contact, or family member is expressed through the note's content and links, not through separate categories. This is fine — the CRM-level distinction lives in Tana where it's useful for search nodes and filtering. Obsidian doesn't need to mirror every sub-type.

---

**For the reading/writing ontology specifically**, the only person tags that matter are `#author` and `#host` — they connect sources to the people who created them. The CRM branch is a separate workstream you've explicitly deferred. So in the reference document, I'd note `#person` and its knowledge-branch sub-types, and flag the CRM branch as out of scope.

Does this feel right? Want me to update the reference doc with this, or do you want to adjust the person hierarchy further?

---

→ Yes it feels right. I may have a (film) `#director` tag for reading/writing ontology as well, or is that the `#author` of the film? A film may have an Author, a Writer, a Producer, Actors...

---

Good question — and it reveals why the person/role design matters.

For films, the creative roles are genuinely distinct. The director shapes the vision, the writer creates the story, the producer funds and organises it, the actors perform. These aren't interchangeable the way "author" works for books and articles. You wouldn't say a film's producer "authored" it.

But here's the practical question: **how many of these roles do you actually track?** When you save a film node, do you record the director, the writer, the cast, and the producer? Or do you mostly just note the director and maybe a lead actor?

My suggestion: **keep `#author` as the tag for people, but use role-specific *fields* on the source types.** The person is always a `#person` (and optionally `#author` if they create works). The *role they play* is expressed by which field they're in, not by a sub-type of person.

So on `#film`:

```
#film
  Fields:
  - Director       instance of #person / #author
  - Writer         instance of #person / #author (optional)
  - Cast           instance of #person, multi-value (optional)
  - Producer       instance of #person (optional)
  - Topics, Status, Media Source, Year, Rating...
```

This means Martin Scorsese is tagged `#author` (he creates works). He appears in the `Director` field on his film nodes. He might also appear in the `Author(s)` field on a book he wrote. The tag says "this person creates things"; the field says "in what role."

You don't need `#director` as a separate tag because you'd never search for "all directors" — you'd search for "all films where Director = Scorsese" or just look at the person node and see what it's linked to. The search is on the field, not the tag.

Same logic applies to `#host` actually — you could argue that `Host` is just a field on `#podcast episode` pointing to a `#person` or `#author`, rather than needing its own tag. The only reason to keep `#host` as a tag is if hosts have host-specific fields that authors don't (like "show bio" or "interview style"). If they don't, `#author` covers both — they're people who create works.

So the simplified knowledge-branch would be:

```
#person  ← base
  └── #author  ← people who create works (books, articles, films, podcasts)
```

And the role specificity lives in the fields on each source type:

| Source type | Role fields |
|---|---|
| `#article` | Author(s) |
| `#book` | Author(s) |
| `#film` | Director, Writer, Cast, Producer |
| `#podcast episode` | Host, Guest(s) |
| `#album` | Artist(s) |

This keeps your person tags lean (just `#person` and `#author`) while giving you full role expressiveness through fields. Want me to update the reference doc with this approach?

→ yes

Updated. The entities section now has the resolved design: `#person` as base, `#author` as the single knowledge-branch sub-type, role specificity through fields on source types (Director/Writer/Cast/Producer on films, Host/Guests on podcast episodes, Artist on albums). CRM branch flagged as deferred. Person role tags removed from open decisions.

The reference doc is getting solid — the remaining open decisions are mostly implementation concerns (URL field consolidation, status migration, media hierarchy, source type audit) rather than conceptual ones. Good shape for moving to Claude Code.

---

→ Brilliant. I will move to Claude Code next. What are your recommendations for making all the changes with Claude Code? Are there any which would be better to do through Tana UI? Using Obsidian CLI? Using subagents? With a view to optimise usage.

---

Good question — the implementation approach matters as much as the schema design. Let me break this down by what each tool does well.

---

## What to do where

### Tana UI (manual, no token cost)

These tasks are either impossible via MCP or far more efficient done by hand:

- **Sever `#book` from `#source`** — removing an "extends" relationship is a UI-only action. Same for `#film`, `#podcast episode` when you get to them.
- **Create `#idea` root tag and sub-tags** (`/fleeting`, `/writing`, `/journal`) — creating new supertags with extends relationships is easier in the UI. Claude Code can add fields via MCP afterwards.
- **Bulk retag nodes** — when migrating `#thoughts ★` nodes to `#idea`, or `#fleeting note (★)` to `#idea/fleeting`, select all in a search view and retag in one action. MCP can't do bulk retags efficiently.
- **Remove `(★)` from tag names** — renaming supertags is UI-only.
- **Add tag descriptions** — quick text edits in the supertag config panel.
- **Set "extends" relationships** — e.g. `#publisher` extends `#organisation`, `#idea/fleeting` extends `#idea`.

### Claude Code + Tana MCP (automated, token-intensive)

Best for repetitive field-setting across many nodes, but requires careful token management:

- **Add fields to new tags** — once you've created `#idea` in the UI, Claude Code can add all the fields (Topics, Source, Related, Status, Media Source) via `set_tag_field`.
- **Populate fields on existing nodes** — e.g. setting Topics, Author(s), or Published in on batches of nodes. This is what the `#to-sort` processing session did.
- **Search and audit** — finding nodes that need migration, checking field values, identifying gaps.

**Efficiency rules from your March 27 session apply here:**
- Search by name + type, never by type alone
- Pre-resolve all node IDs in the plan before starting writes
- Delegate mechanical field-setting to a subagent when no decisions are needed
- Batch writes together — plan all changes for a set of nodes, then execute in one pass

### Claude Code + Obsidian CLI (automated, lower token cost)

Obsidian file operations are much cheaper than Tana MCP because files are small and local:

- **Update frontmatter schema** — add `category:`, fix `status:` values, normalise `topics:` across notes in bulk
- **Migrate `[[Propositions]]` → `[[Claims]]`** — find-and-replace in frontmatter across the vault
- **Create missing category notes** — `[[Claims]]`, `[[Ideas]]` in `Categories/`
- **Template updates** — update active templates with the new schema fields
- **`sync-garden.py` SOURCE_VAULT fix** — one-line change
- **Audit tasks** — find notes with legacy status values, missing frontmatter, inline `#garden` tags

The Obsidian CLI handles moves and renames safely (preserving wikilinks). Claude Code handles file reads and writes directly. Use CLI for moves, direct file operations for everything else.

### Subagents (for bulk mechanical work)

Use subagents when the task is:
- Fully specified (no decisions needed)
- Repetitive (same operation on many nodes)
- Read-heavy from MCP (search results burn context fast)

Good subagent tasks:
- "Set these 5 fields on these 13 nodes using these exact IDs" (like your `#to-sort` Pass 2)
- "For each of these 20 notes in AllNotes, add `status: seed` if status is missing"
- "Search for all notes with `category: [[Propositions]]` and change to `category: [[Claims]]`"

Bad subagent tasks:
- Anything requiring judgement ("should this note be a reference note or a literature note?")
- Discovery work ("find all nodes that might need migration")

---

## Recommended sequence

Here's how I'd order the work, grouped by tool:

**Phase 1 — Tana UI (do first, 30 minutes)**

1. Sever `#book` from `#source`
2. Create `#idea` tag (no extends, base type)
3. Create `#idea/fleeting`, `#idea/writing`, `#idea/journal` extending `#idea`
4. Create `#claim` tag
5. Remove `(★)` from confirmed tags: `#author`, `#podcast`, `#evergreen`, `#garden card`, `#host`, `#film`
6. Add descriptions to any tags missing them

**Phase 2 — Claude Code + Tana MCP (next session)**

7. Add fields to `#idea` via MCP (Topics, Source, Related, Status, Media Source)
8. Add fields to `#claim` if different from `#idea`
9. Add role fields to `#film` (Director, Writer, Cast, Producer) — prepare for when you rationalise it
10. Audit `#thoughts ★` / `#fleeting note (★)` / `#writing inbox` node counts to plan migration batches

**Phase 3 — Tana UI (after audit)**

11. Bulk retag `#thoughts ★` → `#idea` (or appropriate sub-type)
12. Bulk retag `#fleeting note (★)` → `#idea/fleeting`
13. Bulk retag `#writing inbox` → `#idea/writing`
14. Bulk retag `#day notes` → `#idea/journal`

**Phase 4 — Claude Code + Obsidian (separate session)**

15. Create `[[Claims]]` and `[[Ideas]]` category notes in `Categories/`
16. Migrate `[[Propositions]]` → `[[Claims]]` in frontmatter (subagent — mechanical)
17. Fix `sync-garden.py` SOURCE_VAULT (one-line edit)
18. Update active templates with new schema (continue from Task 4 in March 20 session)
19. Begin frontmatter normalisation — status values, missing fields (subagent for batches)

**Phase 5 — Deferred (when ready)**

20. Rationalise `#film`, `#podcast episode`, `#album` in Tana (same pattern as `#article` and `#book`)
21. URL / Media Source consolidation (needs careful test plan)
22. Resume Calibre sync (78/1,288 done)
23. `#media` hierarchy review
24. CRM branch (`#contact`, `#partner`, `#family`)

---

## For your next Claude Code session

Load these files at startup:

```
1. CLAUDE.md
2. _Claude/HANDOFF.md
3. _Claude/Reading and Writing Ontology — Reference.md  ← the new doc
```

Tell Claude Code: "Read these three files. The ontology reference is the authoritative schema. Summarise what phase we're in and what the next action is."

After Phase 1 (Tana UI work), update the HANDOFF.md to reflect what you did manually, so Claude Code knows the current state when it starts Phase 2.


---

Great, very helpful. Can you please check whether for Phase 2 it is necessary or better to use Claude Code + Tana MCP, or are those things easier or more efficient to do within Tana using Tana AI (https://outliner.tana.inc/docs/tana-ai) / AI Agents (https://outliner.tana.inc/docs/ai-agents)? I have a Pro plan.

---

Good — I've now read the Tana AI docs. Here's my assessment of Phase 2, comparing the three approaches:

---

## Phase 2 task-by-task: which tool is best?

### Task 7 — Add fields to `#idea` tag

**Claude Code + MCP wins.** You need to add specific fields with exact types (instance of `#topic`, instance of source types, options list for Status). MCP's `set_tag_field` does this precisely and programmatically. Tana AI can't modify supertag configurations — it operates on node content, not schema structure. And doing it in the UI manually is fine for 5 fields, but MCP is faster if Claude Code is already in a session doing other things.

**However:** if you're already in the Tana UI creating the tags (Phase 1), adding the fields by hand at the same time is probably more natural than switching to Claude Code just for this. Five fields takes about 2 minutes in the supertag config panel. My revised recommendation: **do this in Tana UI as part of Phase 1** — create the tag and add its fields in one pass.

### Task 8 — Add fields to `#claim`

Same analysis. **Tana UI, alongside Phase 1.** The fields are nearly identical to `#idea`.

### Task 9 — Add role fields to `#film`

Same. **Tana UI.** Director, Writer, Cast, Producer — four fields pointing to `#person`/`#author`. Quick to add in the config panel.

### Task 10 — Audit node counts for migration

This is where the tools diverge significantly.

**Tana AI / AI Chat:** You can ask Tana AI "How many nodes have the `#thoughts ★` tag?" directly in the AI chat panel. It has native access to your graph and can answer this without any API overhead. This is genuinely easier and cheaper than MCP for simple discovery queries. Use it for quick counts and spot checks.

**Claude Code + MCP:** Better if you need a structured audit across multiple tags in one pass (e.g. "give me the node count for `#thoughts ★`, `#fleeting note (★)`, `#writing inbox`, `#day notes`, `#ideas` and show me 3 example nodes from each"). MCP can do this systematically, but the token cost is real — each search returns large result sets.

**My recommendation: use Tana AI Chat for the audit.** Ask it to count nodes per tag and show a few examples. Copy the results into your session file for Claude Code to reference later. This saves MCP tokens for the actual migration work.

### What about Tana AI Agents and AI Commands?

These are powerful but serve a different purpose than what Phase 2 needs:

**AI Agents** are custom chat interfaces with system prompts and startup behaviours. Useful for *ongoing workflows* — like a "sort my inbox" agent you'd use repeatedly. Not useful for one-off schema configuration tasks. However, you could build a reusable agent later for `#to-sort` processing (which is an ongoing workflow).

**AI Command Nodes** can do things like autotag nodes, run prompts against node content, and set fields based on AI analysis. The **Text Processing Agent** and **Autotag** commands are particularly relevant for future migration work — for instance, you could build a command that looks at untagged nodes and suggests whether they should be `#idea/fleeting`, `#idea/writing`, or `#idea/journal`. But this requires building the command first, which is its own investment.

**AI Fields / Autofill** can auto-populate fields when a tag is applied — for example, auto-suggesting Topics based on the node's content. This could be valuable *after* the schema is set up, as an ongoing capture aid.

---

## Revised Phase 2 recommendation

Given all this, Phase 2 largely collapses into Phase 1 (Tana UI work):

**Do in Tana UI (extend Phase 1):**
- Add fields to `#idea` (Topics, Source, Related, Status, Media Source)
- Add fields to `#claim` (same set)
- Add role fields to `#film` (Director, Writer, Cast, Producer)

**Do in Tana AI Chat (quick, no token cost to you beyond your Pro plan):**
- Audit node counts for `#thoughts ★`, `#fleeting note (★)`, `#writing inbox`, `#day notes`, `#ideas`
- Check for edge cases (nodes with multiple tags, orphaned nodes)
- Save the results to your session file for Claude Code

**Reserve Claude Code + MCP for:**
- Cross-system work (Tana ↔ Obsidian sync, field mapping)
- Bulk field-setting on existing nodes (e.g. populating Topics, Authors on batches of unprocessed nodes — like the `#to-sort` workflow)
- Anything that needs to read/write both Tana and Obsidian in the same operation
- Resuming the Calibre sync

**Consider building (future, not now):**
- A Tana AI command for `#to-sort` processing — an autotag/classify command that suggests the right supertag for incoming links
- AI autofill on `#idea` for Topics — auto-suggest based on content when you tag something

This means your next Claude Code session can focus entirely on Phase 4 (Obsidian work) rather than spending tokens on Tana schema tasks you can do more efficiently in the Tana UI and AI Chat.


---


That is great. thank you. Look what I found about clickable url values:

## URL Field Pattern

**Use case**: Create a clickable URL node in a URL-type field (e.g. `Media Source`, `Url`).

`set_field_content` with a plain URL string creates plain text, NOT a clickable link.

### Correct approach

Use `import_tana_paste` with markdown URL syntax in the field:

```
Nodename #[[^tagID]]
[[^fieldID]]:: [Label](https://url)
```

Result: a node named "Label" with a child URL field — creates a real clickable URL node.

Can you tell me where to add this to the correct instructions file for Claude Code


---


## Tana MCP — Efficiency Rules

[...existing rules...]

- **Native URL field:** Do NOT trash the `Url` field child node when processing
  `#to-sort` nodes. Tana's native URL field makes the node name a clickable link —
  clearing it loses that behaviour. Set `Media Source` as well, but leave the URL
  field intact.
- **Clickable URL fields via MCP:** `set_field_content` with a plain URL string
  creates plain text, NOT a clickable link. To create a real clickable URL node,
  use `import_tana_paste` with markdown URL syntax:
  
```
  Nodename #[[^tagID]]
  [[^fieldID]]:: [Label](https://url)
```
This creates a node named "Label" with a child URL field that Tana renders as a clickable link. Use this pattern for `Media Source` and any URL-type field.


**2. `Reading and Writing Ontology — Reference.md`** — in the Open Decisions section under URL / Media Source consolidation, as a technical note. This way the implementation context is available when you plan the migration.

Add to the URL/Media Source row:
| URL / Media Source consolidation | ...existing text... 

**Technical note:** MCP's
  `set_field_content` writes plain text URLs (not clickable). Use `import_tana_paste` with markdown link syntax `[Label](url)` to create proper clickable URL nodes. |
  
  
---

(changes made)

→ Ah ok, you already did it. never mind. Now I want to set up the `#to-sort` processing workflow we did in `Claude Code Session — 2026-03-27` in Tana, rather than using MCP with Claude Code. Can you guide me through that?

---

Good idea — the `#to-sort` processing workflow is exactly the kind of repeatable task that Tana AI commands are built for. Let me think through what the workflow needs to do, then suggest how to build it.

---

## What the workflow does (from your March 27 session)

For each node in a `#to-sort` batch:

1. **Fetch the URL** to get the page title, author, description
2. **Rename the node** from raw URL to a clean title
3. **Apply the correct supertag** — `#article/press`, `#article/web`, `#article/academic`, `#book`, `#podcast episode`, `#publication`
4. **Set Media Source** — the URL in the correct field
5. **Write a summary** — 1-2 sentence description as child content
6. **Set Published in** — link to or create a `#publication` node
7. **Set Author(s)** — find or create `#author` nodes
8. **Suggest Topics** — from the content
9. **Leave a review flag** — so you can validate

---

## How to build this in Tana

The most powerful option is the **Text Processing Agent** AI command. It can read node content (including the URL), classify it, set tags, and populate fields — all natively within Tana. Here's my recommended approach:

### Option A — Text Processing Agent (recommended)

This is Tana's built-in agent that can classify nodes, apply tags, and set fields. You configure it once as a command, then run it on selected nodes.

**Step 1 — Create the command node**

In your workspace, create a new command node (Cmd+K → "Create command"). Set it up as:

- **Command type:** Text processing agent
- **Node filter:** Nodes with tag `#to-sort` (so it only appears on relevant nodes)
- **Tag choices:** `#article`, `#article/academic`, `#article/press`, `#article/web`, `#book`, `#podcast episode`, `#publication`
- **Prompts:** This is where you instruct the AI. Something like:

```
Analyze the URL in this node. Fetch or infer the content behind it.

1. Rename the node to the article/page title
2. Choose the most appropriate tag from the available options:
   - #article/academic for peer-reviewed papers (e.g. from ACM, IEEE, journals)
   - #article/press for newspaper/magazine journalism (Guardian, BBC, NYT)
   - #article/web for blog posts, newsletters, web-native content
   - #book for book product pages
   - #podcast episode for podcast episode pages
   - #publication for media outlet homepages (not specific articles)
3. Write a 1-2 sentence summary as the first child node
4. Set the Media Source field to the URL
5. If you can identify the author, set the Author(s) field
6. If you can identify the publication, set the Published in field
7. Suggest 2-3 topics from existing topics in the workspace
```

- **Fields to set:** Media Source, Author(s), Published in, Topics (map these to your field IDs)

**Step 2 — Add as a button on `#to-sort`**

In the `#to-sort` supertag config, add the command as a button. Then whenever you have a batch of `#to-sort` nodes, you can click the button on each one (or select multiple and run it).

**Step 3 — Test on 2-3 nodes first**

Run it on a couple of URLs you know well — check that it classifies correctly, sets the right fields, and creates proper clickable URLs.

### Option B — AI Command with Autotag (simpler, less control)

If the Text Processing Agent feels too complex to set up initially, you can start simpler:

- **Autotag command** — just classifies and applies the right supertag, without setting fields. You fill in fields manually or in a second pass.
- Run via Cmd+K → "Autotag" on selected `#to-sort` nodes
- Set your tag choices as the candidates

This gets you classification quickly, then you enrich fields manually or with a separate AI command for field population.

---

## What Tana AI can't do (still needs MCP or manual work)

A few things to watch for:

**Creating new `#author` or `#publication` nodes** — the Text Processing Agent can set field values that reference existing nodes, but creating entirely new nodes (like a new author who doesn't exist yet) may not work reliably. You might need to create those manually or via MCP. Test this — Tana's AI has been improving and may handle it now.

**The native URL clickability** — the AI command should preserve the URL field since it's working within Tana natively (not through MCP's `set_field_content`). But verify this on your test nodes.

**Removing the `#to-sort` tag after processing** — you may need to do this manually, or add a step in the command that removes it.

---

## My recommendation

Start with **Option A** (Text Processing Agent). The setup takes 15-20 minutes, but once built it becomes a reusable one-click workflow for every future `#to-sort` batch — no Claude Code session needed, no MCP tokens burned, no context management. Given that you process `#to-sort` nodes regularly, the investment pays for itself quickly.

Would you like me to write out the exact prompt text and field mappings for the command, using the field IDs from your schema?

---

→ Great. Let's go with option A. But first let us consider a couple of questions:
- the url. I am in two minds whether to merge Media Source and Url (the system field created when importing a link into Tana). Shall I have both, even when they contain the same link, since you can populate the created field (Media Source) but not the system one (Url)? If I try and merge them there may be issues. If I simply rename Media Source as URL or Url, there may be confusion. Can they really be seamlessly merge while maintiaing the native behaviour and allowing Claude to populate fields?
- the new supertags. I guess I should create those first manually in Tana UI (as per your revised Phase 2 recommendation) for this set up to work?


---

Two good questions. Let me address them in turn.

---

## The URL question

The core tension is: Tana's native `Url` field (created when you paste or capture a link) gives you clickable node names — this is a *system behaviour* tied to how the node was created, not just to a field value. Your schema field `Media Source` is a regular URL-type field you defined, which stores a URL but doesn't make the node name clickable.

Here's what I'd recommend: **keep both, don't merge.**

The reason is that they serve different functions:

**Native `Url` field** — this is created automatically when you capture a link (via browser extension, paste, etc.). It makes the node name itself a clickable link. You can't reliably create this behaviour via MCP or AI commands — it's a property of how the node was born. Think of it as the node's *origin link*.

**`Media Source` field** — this is your schema field. It stores a canonical URL that Claude Code, AI commands, and you can read and write programmatically. It's the *reference link* — where this thing lives on the web.

In practice, for `#to-sort` nodes they'll contain the same URL. That's fine — a small redundancy that preserves both behaviours. The native field keeps the node clickable; the schema field keeps the URL accessible to your tools and queries.

**What I'd do about naming:** Don't rename `Media Source` to `Url` or `URL` — that creates confusion with the system field. Keep `Media Source` as the schema name. If you want to make it clearer, add a field description in Tana: "Canonical URL for this source. May duplicate the native Url field — both are intentional."

**The rule for the `#to-sort` processing workflow becomes:**
1. Leave the native `Url` field intact (don't trash it — it keeps the node clickable)
2. Copy the URL into `Media Source` as well (so your schema queries and Claude Code can find it)
3. When processing via MCP in future, use `import_tana_paste` with markdown link syntax to create clickable URLs in `Media Source`

---

## The new supertags question

Yes — create the tags first in Tana UI before setting up the AI command. The Text Processing Agent needs to know which tags are available as candidates for classification. If `#idea`, `#idea/fleeting`, `#idea/writing`, `#idea/journal`, `#claim`, and the film role fields don't exist yet, the agent can't assign them.

Here's the order:

**Step 1 — Create tags in Tana UI (Phase 1):**
- `#idea` (root, no extends)
- `#idea/fleeting` (extends `#idea`)
- `#idea/writing` (extends `#idea`)
- `#idea/journal` (extends `#idea`)
- `#claim` (independent)
- Add fields to each (Topics, Source, Related, Status, Media Source)
- Add role fields to `#film` (Director, Writer, Cast, Producer)
- Sever `#book` from `#source`

**Step 2 — Set up the Text Processing Agent command:**
- Tag choices should include all the tags the agent might need to apply: `#article`, `#article/academic`, `#article/press`, `#article/web`, `#book`, `#podcast episode`, `#publication`, `#idea/fleeting`, `#idea/writing`
- The agent only needs the tags that `#to-sort` items might become — you probably won't be sorting items into `#claim` or `#evergreen` from a raw URL capture, so those can be left out of the tag choices for this command

**Step 3 — Test on 2-3 nodes**

Once you've done Phase 1 and built the command, want me to write out the exact prompt text for the Text Processing Agent? I can tailor it to your specific field IDs and tag names.

---

→ Yes please. For when I save and sort tweets, shall I add `#article/tweet` or should I use the  separate `#tweet` supertag I created in the past (it has no fields set though)? Tana now renders tweets nicely but I'd like to process them so that I can set a node title, summary, author etc. (screenshot attached).

---

For tweets, I'd recommend `#tweet` as a separate independent type, not a sub-type of `#article`. Here's why:

A tweet isn't really an article — it's a short-form post by a specific person, often a quote, opinion, or link to something else. It doesn't have a publication, a publication date in the article sense, or a journalist byline. It has an author (the tweeter), a date, and often embedded content. The fields you'd want are different enough to warrant separation.

However, tweets *are* a source type in your ontology — something you consume and reference. They sit in Stage 1 alongside articles, books, and films.

**Proposed `#tweet` schema:**

```
#tweet  ← independent type (no extends)

  Fields:
  - Author         instance of #person / #author (who tweeted)
  - Topics         instance of #topic, multi-value
  - Media Source   url (link to the tweet)
  - Summary        plain text (your note on why you saved it)
  - Status         options: to process · processed
```

Keep it lean — Bri's principle. The tweet itself is already rendered by Tana as embedded content, so you don't need to duplicate the text in a field. The `Summary` is for *your* note about why it matters.

This also means adding `#tweet` to the source types list in the ontology reference, and to the tag choices for your `#to-sort` processing command.

---

Now let me write the full Text Processing Agent prompt. I'll include `#tweet` in the tag choices:

---

## Text Processing Agent — `#to-sort` processor

### Setup in Tana UI

**Command type:** Text processing agent

**Node filter:** Nodes with tag `#to-sort`

**Tag choices:**
- `#article/academic`
- `#article/press`
- `#article/web`
- `#book`
- `#podcast episode`
- `#publication`
- `#tweet`
- `#idea/fleeting` (for captures that aren't external sources but your own thoughts)

**Prompt:**

```
Analyze this node. It contains a URL or embedded content that needs to be classified and enriched.

## Your task

1. CLASSIFY: Choose the single most appropriate tag from the available options:
   - #article/academic — peer-reviewed papers from academic publishers (ACM, IEEE, JSTOR, university press, journals with DOI)
   - #article/press — newspaper or magazine journalism (Guardian, BBC, NYT, Economist, etc.)
   - #article/web — blog posts, newsletters, web-native essays, non-journalistic web content
   - #book — book product pages or references to specific books
   - #podcast episode — podcast episode pages
   - #publication — media outlet or publication homepages (not a specific article — the publication itself)
   - #tweet — embedded tweets or links to tweets/X posts
   - #idea/fleeting — if this is not an external source but a personal thought or observation

2. RENAME: Set the node title to a clear, descriptive name:
   - For articles: the article headline
   - For books: "Book Title" (no author in title)
   - For podcast episodes: "Guest Name: Episode Topic" or the episode title
   - For publications: the publication name
   - For tweets: a short description of the tweet's content or argument (not the full tweet text)
   - For ideas: keep the existing text or clean it up

3. SUMMARISE: Write a 1-2 sentence summary as a child node describing what this content is about and why it might be worth reading/referencing.

4. SET FIELDS:
   - Media Source: set to the URL
   - Author(s): if you can identify the author from the content, set this field. For tweets, the author is the person who tweeted.
   - Published in: for articles, identify the publication (newspaper, magazine, blog, journal). If the publication already exists as a node, reference it. If not, note the publication name.
   - Topics: suggest 2-3 topics that match existing topics in the workspace. Prefer specific topics over broad ones.

5. REVIEW FLAG: Add a child node "- [ ] Review: validate classification and fields" so the user can check your work.

## Rules
- Do NOT remove or modify the native Url field — it keeps the node name clickable
- If the URL cannot be accessed or the content is unclear, set the title to what you can infer and note the limitation in the summary
- For tweets, use the tweet author as the Author field, not the person being quoted in the tweet
- If you are unsure between two tags, pick the more specific one and note your uncertainty in the review flag
```

**Fields to set:** Map these to your actual field IDs:
- Media Source
- Author(s)
- Published in (for articles)
- Topics

### How to use it

1. Open your daily note or wherever `#to-sort` nodes live
2. Select the node(s) you want to process
3. Click the command button (or run via Cmd+K → your command name)
4. The agent processes each node: classifies, renames, summarises, sets fields
5. Review the results — check the flags, adjust Topics, validate Author nodes

### After processing

- Remove the `#to-sort` tag from processed nodes (the correct supertag has replaced it)
- Check that Author and Publication nodes exist and are correct
- Add any Topics the agent missed

---

Want me to add `#tweet` to the ontology reference document as well?


→ yes

Done — `#tweet` is now in the sources table (with its field description) and in the person role fields table. Ready for you to start building in Tana UI.

---
---











- 