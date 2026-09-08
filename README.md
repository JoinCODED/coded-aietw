# AI Essentials in the Workplace

Workshop site for the CODED three day programme.

**8 to 10 September 2026 · 09:00 to 14:00 · CODED Campus, Kuwait · Built on Claude**

## What is here

| Page | File |
|---|---|
| Landing | `site/index.html` |
| Day 1 hub | `site/coded-aiet-day-1.html` |
| Day 1 deck, 60 slides | `site/coded-aiet-day-1-deck.html` |
| Day 1 lab, 7 tasks | `site/coded-aiet-day-1-lab.html` |
| Day 2 hub | `site/coded-aiet-day-2.html` |
| Day 2 deck, 40 slides | `site/coded-aiet-day-2-deck.html` |
| Day 2 lab, 7 tasks | `site/coded-aiet-day-2-lab.html` |
| Day 3 hub | `site/coded-aiet-day-3.html` |
| Day 3 deck, 48 slides | `site/coded-aiet-day-3-deck.html` |
| Day 3 lab, 9 tasks | `site/coded-aiet-day-3-lab.html` |

All three days are built and every internal link resolves.

Participant files, all invented and safe to upload:
`aiet-sample-operations-report.txt`, `employee-satisfaction-2026.csv`,
`department-budget-2026.xlsx` and its `.csv` twin, and the eight capstone
scenario files.

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

## Assessment links

The MAP tests and the survey are live. The URLs are recorded in
`build/manifest.json` under `assessments` and written into the generators.

| Element id | Item | Lives on |
|---|---|---|
| `map-pre` | Pre-program MAP test | Day 1 page CTA panel, and slide 3 of the Day 1 deck |
| `map-post` | Post-program MAP test | Day 3 page CTA panel, slide 25 of the Day 3 deck, and the lab's Task 2. Taken at 10:30, before the capstone |
| `survey` | End of program survey | Day 3 page "Before you leave" panel, slide 43 of the Day 3 deck, and the lab's Task 9 |
| `survey-foot` | End of program survey | Landing page footer, Connect column |

There is no quiz. The post-program MAP test is taken at 10:30 on Day 3, before
the capstone, so it measures the teaching rather than the afternoon. Day 3
closes with the survey and certificates. No placeholders remain; this should
return nothing:

```bash
grep -rn 'data-placeholder' site/
```

## Day 3 at a glance

| Time | Section |
|---|---|
| 09:00 to 09:15 | Review. Day 1 and Day 2 in four lines each |
| 09:15 to 09:50 | Security and data sharing, then use cases by department |
| 10:05 to 10:30 | Connectors, MCP and Skills. Task 1 |
| 10:30 to 10:40 | Post-program MAP test, before the capstone. Task 2 |
| 10:40 to 10:50 | Capstone Phase 0. Pair up, pick an idea. Task 3 |
| 10:50 to 11:30 | Deliverable 1, the executive briefing. Task 4 |
| 11:40 to 12:05 | Deliverable 2, charts that argue. Task 5 |
| 12:45 to 13:05 | Deliverable 3, the stakeholder deck, with the charts in it. Task 6 |
| 13:05 to 13:20 | Deliverable 4, the communication pack. Task 7 |
| 13:20 to 13:50 | Present, three minutes per pair, then one question. Task 8 |
| 13:50 to 14:00 | Survey and certificates. Task 9 |

### The security block

Five slides on where pasted text goes, anonymising before you paste, and a
side by side on why a public AI tool needs more care than Microsoft Copilot:
Copilot sits inside the tenant with the guardrail configured by IT, a public
tool sits outside it with your own judgment as the only guardrail. Then four
use case slides, one per department, each with safe productivity boosters,
strict guardrails, and the ethical risk.

### The capstone

Participants work **in pairs** and pick one of seven ideas. For every
deliverable one of them builds and the other verifies. The ideas map onto the
datasets already in the repo:

| # | Idea | Department | Data |
|---|---|---|---|
| 01 | The Overtime Decision | Operations | `ops-overtime`, `ops-hiring-costs` |
| 02 | The Retention Programme | Human Resources | `hr-leavers`, `hr-headcount` |
| 03 | The Channel Rescue | Customer Service | `cs-tickets`, `cs-staffing` |
| 04 | The Supplier Consolidation | Procurement | `procurement-purchase-orders` |
| 05 | The Recognition Programme | People | `employee-satisfaction-2026` |
| 06 | The Cost Control Programme | Finance | `department-budget-2026` |
| 07 | Your Own Work | Bring your own | Redacted, instructor sign off first |

Each idea carries the situation, the initiative, its data, and a "watch out"
that points at the trap without giving it away. Every dataset has deliberate
flaws. Notes save under `aiet_day3_lab`.

The four deliverables, in order, are an executive briefing, two or
three charts that each defend one claim, a stakeholder deck that carries those
charts, and a communication pack with three reusable templates.

## Day 2 at a glance

| Time | Section |
|---|---|
| 09:00 to 09:10 | Open |
| 09:10 to 10:10 | Report to deck, Claude Design. Task 1 |
| 10:25 to 11:10 | Another tool, Gamma. Task 2 |
| 11:25 to 12:10 | Data analysis. Tasks 3 and 4 |
| 12:55 to 13:25 | Validation and charts. Tasks 5 and 6 |
| 13:35 to 13:57 | Prompt library and one Skill. Task 7 |
| 13:57 to 14:00 | Close |

Participants need a free Gamma account before 10:25 and a spreadsheet app for
task 6. Notes save under `aiet_day2_lab`.

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
