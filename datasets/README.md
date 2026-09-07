# Day 2 data files

Two files. Download them when the lab tells you to, not before.

| File | Used in | What it is |
|---|---|---|
| `employee-satisfaction-2026.csv` | Lab 5 and Lab 6 | An employee engagement survey export. One row per response. |
| `department-budget-2026.xlsx` | Lab 8 | The finance export for the nine months to 30 September 2026. Two sheets. |
| `department-budget-2026.csv` | Lab 8 | The same detail lines as plain text, for pasting into Claude. |

## `employee-satisfaction-2026.csv`

An anonymous survey run across the company this year.

| Column | What it holds |
|---|---|
| `response_id` | The response reference |
| `department` | The department the person selected |
| `q1_workload` … `q6_recognition` | Six questions, scored 1 to 5 |
| `overall_satisfaction` | One overall score, 1 to 5 |
| `would_recommend` | Yes or No |
| `comments` | Free text, left blank by most people |

The six questions, in full:

1. **q1_workload** — my workload is manageable
2. **q2_manager_support** — my manager supports me
3. **q3_tools** — I have the tools I need to do my job
4. **q4_communication** — I know what is happening in the company
5. **q5_development** — I can develop my career here
6. **q6_recognition** — my work is recognised

## `department-budget-2026.xlsx`

| Sheet | What it holds |
|---|---|
| **Budget vs Actual** | One row per budget line: annual budget, year-to-date budget, year-to-date actual, variance and variance % |
| **Summary** | One row per department, and a total |

All figures are in Kuwaiti dinar. A positive variance means the department has
spent more than its year-to-date budget.

## Before you ask either file a question

Profile it first. Every file, every time:

> Before you answer anything, tell me:
> how many rows are in this file,
> how many are exact duplicates,
> how many rows have missing values and in which columns,
> what distinct values appear in each category column,
> and whether any value looks impossible.
> Do not analyze anything yet.

**These are real exports, and real exports have problems in them.** Finding
those problems is part of the lab, not an obstacle to it.
