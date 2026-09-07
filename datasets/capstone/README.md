# Capstone scenario files

Choose one scenario. Read the whole pack in `day-3-labs.md` before you open a
file. The decision shapes which numbers matter.

| Scenario | Files |
|---|---|
| **A · Operations** — hire, or keep paying overtime? | `ops-overtime-2026.csv` · `ops-hiring-costs-2026.csv` |
| **B · Human Resources** — where does the retention budget go? | `hr-leavers-2026.csv` · `hr-headcount-2026.csv` |
| **C · Customer Service** — which channel is failing? | `cs-tickets-2026.csv` · `cs-staffing-2026.csv` |
| **D · Procurement** — consolidate, or not? | `procurement-purchase-orders-2026.xlsx` · `procurement-purchase-orders-2026.csv` |
| **E · Your own work** | Your own redacted data. Four qualifying questions first. |

## A · Operations

`ops-overtime-2026.csv` — nine months of overtime by team and month: hours,
cost, headcount, absence days per person, and open vacancies.
`ops-hiring-costs-2026.csv` — salary, recruitment cost, onboarding time,
standard monthly hours and the overtime rate for each role.

## B · Human Resources

`hr-leavers-2026.csv` — eighteen months of leavers: department, hire and leave
dates, tenure band, reason, whether the leaver went voluntarily, and whether an
exit interview happened.
`hr-headcount-2026.csv` — average headcount per department over the same
period, and how many locations each one covers.

**You need both files.** A count of leavers on its own does not tell you where
the problem is.

## C · Customer Service

`cs-tickets-2026.csv` — six months of tickets: channel, date and hour opened,
request type, first response time in hours, whether it was resolved on first
contact, and a satisfaction score out of 5.
`cs-staffing-2026.csv` — agents assigned per channel, hours covered, and the
response target for each channel.

## D · Procurement

`procurement-purchase-orders-2026.xlsx` — nine months of purchase orders on the
first sheet, and a category summary on the second.
`procurement-purchase-orders-2026.csv` — the same order lines as plain text,
for pasting.

## The rule for every one of these files

**Profile it before you ask it anything.**

> Before you answer anything, tell me:
> how many rows are in this file,
> how many are exact duplicates,
> how many rows have missing values and in which columns,
> what distinct values appear in each category column,
> and whether any value looks impossible.
> Do not analyze anything yet.

Every pack has problems in it. They were put there. Find them before your
colleagues find them at 13:20.

**Every number in your package needs a validation note.** How many records it
is built on, what you removed, and the headline figure recomputed by hand.
