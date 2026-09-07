# AI Essentials in the Workplace

Workshop site for the CODED three day programme.

**8 to 10 September 2026 · 09:00 to 14:00 · CODED Campus, Kuwait · Built on Claude**

## What is here

| Page | File |
|---|---|
| Landing | `site/index.html` |
| Day 1 hub | `site/coded-aiet-day-1.html` |
| Day 1 deck, 57 slides | `site/coded-aiet-day-1-deck.html` |
| Day 1 lab, 7 tasks | `site/coded-aiet-day-1-lab.html` |
| Sample report for Day 1 task 6 | `site/aiet-sample-operations-report.txt` |

Day 2 and Day 3 are not built yet. The landing page already links to
`coded-aiet-day-2.html` and `coded-aiet-day-3.html`, so those two links are dead
until those pages exist.

## Deploy

Every page is self contained. CSS is inline, the logo is a base64 data URI, and
there is no build step or bundler at deploy time.

Vercel serves `site/` as the output directory, set in `vercel.json`. Import the
repository in Vercel, leave the framework preset as **Other**, and leave the build
command empty. `outputDirectory` in `vercel.json` does the rest.

`cleanUrls` is on, so `/coded-aiet-day-1` serves the page and the `.html` form
redirects to it. Links between pages are same directory relative, so nothing
breaks either way.

The datasets and the sample report live inside `site/` because the labs link to
them for download. `build/`, `datasets/` and `instructor/` are excluded from the
deployment by `.vercelignore`.

## Rebuild

The pages in `site/` are generated. Edit the generator, not the HTML.
See `build/README.md`.

```bash
python3 build/build_day1_deck.py
python3 build/build_day1_lab.py
python3 build/build_day1_page.py
```

## Theme

Taken from the CODED brand site. Navy base with a blue ramp, plus IBM Plex Sans,
IBM Plex Mono and IBM Plex Sans Arabic.

| Token | Value | Use |
|---|---|---|
| `--base` | `#00081C` | page background |
| `--card` / `--card-2` | `#00112F` / `#14243F` | card gradient |
| `--deepest` | `#00224D` | darkest blue |
| `--deep` | `#004AA3` | CODED blue |
| `--primary` | `#2F74D6` | primary accent |
| `--soft` | `#6F9CE8` | eyebrows, taglines, icons |
| `--light` | `#A8C6F2` | highlights |
| `--indigo` | `#3E50DD` | Day 3 accent only |
| `--ink` / `--ink-dim` / `--ink-faint` | `#F2F6FC` / `#9FB2D4` / `#6F83A8` | text |

## Placeholders still to fill

Three assessment links are not live yet.

| Element id | Item | Lives on |
|---|---|---|
| `map-pre` | Pre-program MAP test | Day 1 page, and slide 3 of the Day 1 deck |
| `map-post` | Post-program MAP test | Day 3, once built |
| `survey` | End of program survey | Day 3, once built |

To activate the Day 1 one, change the `<span class="slides-btn ph">` to an
`<a href="..." class="slides-btn">` and drop the `ph` class and the
`data-placeholder` attribute.

## Day 1 at a glance

| Time | Section |
|---|---|
| 09:00 to 09:25 | Open. MAP test, the question |
| 09:25 to 10:10 | AI and LLMs. Task 1 |
| 10:10 to 10:25 | Break |
| 10:25 to 11:15 | Prompting. Tasks 2 and 3 |
| 11:15 to 11:30 | Break |
| 11:30 to 12:10 | Professional writing. Tasks 4 and 5 |
| 12:10 to 12:55 | Lunch and prayer |
| 12:55 to 13:20 | Research and summarizing. Task 6 |
| 13:20 to 13:30 | Break |
| 13:30 to 13:50 | Email. Task 7 |
| 13:50 to 13:58 | Connectors and MCP. Live demo, flexible block |
| 13:58 to 14:00 | Close |

Every section ends on a break slide with a countdown. The three short breaks offer
10 or 15 minutes, lunch offers 45 or 60. The coffee button in the deck nav opens
the same timer at any point.

All seven Day 1 tasks run inside Claude. Notes and done marks save to the
browser under `aiet_day1_lab`.

## A note on instructor material

This repository is public. Answer keys, planted fault solutions and facilitator
notes are deliberately not committed. They are listed in `.gitignore` and stay
with the instructor.
