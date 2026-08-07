---
title: Tana Ui Changes Instructions
updated: 2026-03-29
---

# Tana UI changes instructions


Good catch on `#video`. From the screenshot I can see it extends `#source` and has fields: Host, Publication, Media Source, Year, Quotes, Highlights, Zettelkasten Entry. It's mostly documentaries and talks — different from `#film` (which has Director, Writer, Cast, Producer, Genre, Language). Makes sense to keep both.

Let me also note what I see about your current `#author (★)` and `#film (★)`:

**`#author (★)`** — extends `#person (★)`, has fields: Works, Quotes and Highlights, Related Notes, Website(s). This is well-structured already.

**`#film (★)`** — extends `#source`, has fields: Director, Writer, Genre, Language, Year, Media Source, and `Topic(s) ★`. Similar pattern to `#book` before rationalisation.

---

## Phase 1 & 2 — Complete Tana UI instructions

Work through these in order. Each step says exactly what to do in the Tana UI. Estimate: 45-60 minutes total.

### Part A — Sever inheritance chains (5 minutes)

**A1.** Open `#book` supertag config → Building blocks → remove `#source` from "Extend other supertags". (The fields are already on `#book` independently from the migration you did.)

**A2.** Open `#film (★)` supertag config → Building blocks → remove `#source` from "Extend other supertags". The fields (Director, Writer, etc.) stay — they're defined on the tag itself.

**A3.** Open `#podcast episode (★)` supertag config → Building blocks → remove `#source` from "Extend other supertags".

**A4.** Open `#video (★)` supertag config → Building blocks → remove `#source` from "Extend other supertags".

**A5.** Open `#note` supertag config → Building blocks → remove `#input` from "Extend other supertags". (Keep the tag — it's used in Projects/Areas. Just sever the OCP inheritance.)

### Part B — Clean up tag names (10 minutes)

For each of these, open the supertag config and edit the name:

**B1.** `#author (★)` → rename to `#author`
**B2.** `#film (★)` → rename to `#film`
**B3.** `#podcast episode (★)` → rename to `#podcast episode`
**B4.** `#podcast (★)` → rename to `#podcast`
**B5.** `#video (★)` → rename to `#video`
**B6.** `#person (★)` → rename to `#person`
**B7.** `#evergreen (★)` → rename to `#evergreen`
**B8.** `#garden card (★)` → rename to `#garden card`
**B9.** `#host (★)` → rename to `#host`
**B10.** `#literature note (★)` → rename to `#literature note`

For each renamed tag, add a description if missing. Use the descriptions from the ontology reference (e.g. `#author`: "People who create works — books, articles, films, podcasts, music").

### Part C — Create new tags (15 minutes)

**C1. Create `#idea`**
- No extends (independent root)
- Description: "Your own thinking — sparks, plans, reflections"
- Base type: None
- Fields to add:
  - `Topics` — instance of `#topic`, multi-value
  - `Source` — instance of `#article`, `#book`, `#film`, `#podcast episode`, `#video`, `#tweet` (what prompted this idea)
  - `Related` — multi-value, any node type (other ideas, concepts, claims, sources)
  - `Status` — options: seed · hypothesis · draft · active · evergreen
  - `Media Source` — url (optional, hide when empty)

**C2. Create `#idea/fleeting`**
- Extends: `#idea`
- Description: "Sparks, observations, quick captures"
- No additional fields (inherits from `#idea`)

**C3. Create `#idea/writing`**
- Extends: `#idea`
- Description: "Notes about things you intend to write"
- No additional fields

**C4. Create `#idea/journal`**
- Extends: `#idea`
- Description: "Reflective, time-bound entries, diary"
- No additional fields

**C5. Create `#claim`**
- No extends (independent)
- Description: "Assertable, evidential. Can be backed or refuted by evidence."
- Fields to add:
  - `Topics` — instance of `#topic`, multi-value
  - `Source` — instance of source types (evidence or provenance)
  - `Related` — multi-value (other claims, ideas, concepts)
  - `Status` — options: seed · hypothesis · draft · active · evergreen
  - `Media Source` — url (optional, hide when empty)

**C6. Create `#tweet`**
- No extends (independent)
- Description: "Tweets and X posts — short-form social media content"
- Fields to add:
  - `Author` — instance of `#person` / `#author`
  - `Topics` — instance of `#topic`, multi-value
  - `Media Source` — url (link to the tweet)
  - `Summary` — plain text (your note on why you saved it, hide when empty)

**C7. Create `#reference note`** (if it doesn't already exist as a clean tag)
- No extends (independent)
- Description: "What the author said, distilled in your words"
- Fields:
  - `Source` — instance of source types
  - `Topics` — instance of `#topic`, multi-value
  - `Status` — options: seed · draft · active · evergreen

### Part D — Update existing tags with missing fields (10 minutes)

**D1. `#film`** — check and add these fields if missing:
- `Director` — instance of `#person` / `#author`
- `Writer` — instance of `#person` / `#author` (hide when empty)
- `Cast` — instance of `#person`, multi-value (hide when empty)
- `Producer` — instance of `#person` (hide when empty)
- Confirm existing: Topics, Year, Genre, Language, Media Source, Status

**D2. `#video`** — check current fields against your needs:
- `Host` is already there — good → instance of `#person`
- `Publication` is already there — good
- Add `Director` — instance of `#person` / `#author` (hide when empty) if useful for documentaries
- Confirm: Media Source, Year, Topics are present

**D3. `#podcast episode`** — check and add:
- `Host` — instance of `#person` / `#author`
- `Guest(s)` — instance of `#person` / `#author`, multi-value
- `Podcast` — instance of `#podcast` (the show)
- Confirm: Topics, Media Source, Status are present

**D4. `#author`** — review current fields (Works, Quotes and Highlights, Related Notes, Website(s)). These look good for the knowledge branch. No changes needed unless you want to add `Topics` for subject-area tagging of authors.

**D5. `#person`** — check it has at minimum: name (node title), `Topics` (optional), `Media Source` (website/profile, optional). This is the lean base — CRM fields live on `#contact` and its children, not here.

**D6. `#publisher`** — if this tag doesn't exist yet, create it:
- Extends: `#organisation`
- Description: "Book publishers"
- No additional fields needed beyond what `#organisation` provides

### Part E — Audit node counts via Tana AI Chat (10 minutes)

Open Tana AI Chat and ask these questions. Copy the answers into a note for your Claude Code session:

- "How many nodes have the `#thoughts ★` tag?" (or whatever it's called after renaming)
- "How many nodes have the `#fleeting note` tag?"
- "How many nodes have the `#writing inbox` tag?"
- "How many nodes have the `#day notes` tag?"
- "How many nodes have the `#ideas` tag?"
- "How many nodes have the `#to-sort` tag?"
- "Show me 3 example nodes for each"

`#idea` notes 375, of which 9 simple, plus
`#idea/writing` 120
`#idea/fleeting` 236
`#idea/journal` 10

`#to-sort` is used 32 times, however I often group several nodes and I apply the tag to the parent node. At times I have applied it directly to the node. These may be pure links or text nodes with or without links.

This gives you the migration scope for Phase 3 (bulk retag).

### Part F — Set up the `#to-sort` Text Processing Agent (15 minutes)

**F1.** Create a new command node in your workspace
**F2.** Set command type: Text processing agent
**F3.** Set node filter: Nodes with tag `#to-sort`
**F4.** Set tag choices: `#article/academic`, `#article/press`, `#article/web`, `#book`, `#podcast episode`, `#publication`, `#tweet`, `#video`, `#idea/fleeting`
**F5.** Paste the prompt I wrote in my previous message
**F6.** Map the fields to set: Media Source, Author(s), Published in, Topics
**F7.** Test on 2-3 `#to-sort` nodes you know well — verify classification, title, summary, and field population
**F8.** Add as a button on the `#to-sort` supertag config (under AI and Commands)

---

After completing all of this, update your `HANDOFF.md` with what you did, then you're ready for Phase 3 (bulk retag in Tana UI) and Phase 4 (Obsidian work with Claude Code).

