# Generators

The pages in `site/` are generated. Edit the generator, not the HTML.

```bash
python3 build/build_day1_deck.py    # -> site/coded-aiet-day-1-deck.html
python3 build/build_day1_lab.py     # -> site/coded-aiet-day-1-lab.html
python3 build/build_day1_page.py    # -> site/coded-aiet-day-1.html
```

| File | Holds |
|---|---|
| `deck_shell.py` | Shared deck CSS, chrome and JS engine. Every day's deck imports it, so a theme change here hits all of them. |
| `build_day1_deck.py` | Day 1 slide content, in order, plus the parked slides |
| `build_day1_lab.py` | Day 1 lab tasks, in the `TASKS` array at the top |
| `build_day1_page.py` | Day 1 plan rows and task rows |
| `manifest.json` | Workshop config: dates, branding, days, assessment placeholders |
| `coded-logo.txt` | CODED logo as a base64 data URI |

`index.html` is hand written and has no generator.

## Parked slides

`build_day1_deck.py` ends with a `RESTORE_PARKED = False` block holding nine written
but unused slides: one prompting check, three on hallucinations, and five on privacy.
Set the flag to `True` and add the ids to `ORDER` to bring them back.

## Day 2

```bash
python3 build/build_day2_deck.py   # -> site/coded-aiet-day-2-deck.html
python3 build/build_day2_lab.py    # -> site/coded-aiet-day-2-lab.html
python3 build/build_day2_page.py   # -> site/coded-aiet-day-2.html
```

`lab_shell.py` holds the shared lab CSS, body and task renderer. Both days use it,
so a change there hits both labs. It supports:

| Task field | Renders |
|---|---|
| `steps` | The numbered steps card |
| `prompt` | One tap to copy prompt inside the steps card |
| `starterlist` | A menu of tap to copy prompts |
| `asset` / `files` | Download links |
| `dataset` | Download plus a preview table |
| `launches` | Open Claude / Open Gamma buttons |
| `goal` | The amber "what you are aiming for" box |
| `promptSteps` | Multi step tasks, each with its own goal, prompt and findings |
| `findings` | Labelled inputs that save to the browser |
| `engine` | The classify engine (Day 1 only, currently unused) |
| `expect` / `stretch` / `boss` | The three closing cards |
