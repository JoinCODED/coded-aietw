# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lab_shell import page

CLAUDE = "https://claude.ai/new"
GAMMA  = "https://gamma.app"

SAT = {
 "label":"employee-satisfaction-2026.csv",
 "href":"employee-satisfaction-2026.csv",
 "note":"An anonymous staff engagement survey, 161 responses. Six questions scored 1 to 5, one overall score, and a free text comment. Every figure is invented for the workshop, so it is safe to upload.",
 "head":["response_id","department","q1_workload","q2_manager","q6_recognition","overall","recommend"],
 "rows":[["R1134","Human Resources","4","4","1","3","No"],
         ["R1043","Operations","3","4","2","4","Yes"],
         ["R1076","Information Technology","3","3","4","3","Yes"],
         ["R1073","(blank)","3","4","2","3","No"]],
 "more":"... 161 rows. The file is not clean. That is the exercise."}

BUD = {
 "label":"department-budget-2026.xlsx",
 "href":"department-budget-2026.xlsx",
 "note":"The finance export for the nine months to 30 September. Two sheets: Budget vs Actual with 32 detail lines, and a Summary with one row per department. All figures in Kuwaiti dinar. Invented for the workshop, safe to upload. A CSV of the same detail lines is on the page if you prefer pasting.",
 "head":["Department","Line item","Annual Budget","YTD Budget","YTD Actual","Variance","Variance %"],
 "rows":[["Operations","Salaries and wages","910000","682500","752600","70100","10.3"],
         ["Finance","Salaries and wages","379000","284250","302300","18050","6.4"],
         ["Human Resources","Recruitment","36000","27000","29900","2900","10.7"],
         ["Information Technology","Support contracts","32000","24000","27300","3300","13.8"]],
 "more":"... 32 detail lines across six departments, plus a Summary sheet"}

TASKS = [
{
 "app":"Claude Design","sec":"S1 &middot; Report to deck","mins":"~20 min",
 "title":"D2.1 &middot; Report to deck",
 "scenario":"Yesterday's operations report, turned into a deck for the leadership team. Same content, new format. You write the prompt yourself, using the six parts from Day 1.",
 "files":[{"label":"aiet-sample-operations-report.txt","href":"aiet-sample-operations-report.txt",
           "note":"Your source document. This is the same report you verified in Day 1 task 6, and it still has five deliberate faults in it. Attach it to Claude."}],
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Attach the report, then build the deck with Claude Design."}],
 "goal":"Get Claude to turn the report into a six slide management summary: the position, the money, the people, customer service, the risks, and a closing “so what”. Every figure traceable to the source.",
 "steps":["Attach the report to a new Claude conversation.",
          "Write your own six part prompt for the goal above, then ask Claude to design it.",
          "Open two slides and check every figure against the source.",
          "Fix one slide by hand, so you feel where Claude stops and you start."],
 "promptSteps":[
   {"label":"Reference prompt, if you want to compare after you write yours",
    "goal":"Write your own first. Only open this one once you have run yours, then look at what is different.",
    "prompt":"You are preparing a board level summary. The attached document is a quarterly operations review. Turn it into a six slide management summary: the overall position, the financial position, people and headcount, customer service, the risks, and a closing recommendation. Each slide gets a headline of eight words or fewer, three supporting lines, and the exact figure it came from. Direct and factual. Use only figures that appear in the document. If a figure is missing or looks wrong, flag it on the slide rather than filling the gap."}
 ],
 "findings":[{"label":"A figure you checked against the source","hint":"the number, and which section it came from"},
             {"label":"Anything Claude got wrong or left vague","hint":"what you would fix by hand"},
             {"label":"How long did the whole thing take?","hint":"minutes, honestly"}],
 "expect":"A six slide deck built from the report, with at least two figures you personally checked. A deck that looks right and misquotes a number is worse than no deck.",
 "stretch":"Ask Claude to rewrite the same deck for a different audience, the department heads rather than the board. Notice what it drops, and what it should never have said out loud.",
 "boss":"The report has five deliberate faults. Before it builds anything, ask Claude to fact check the report against itself and show its working. How many of the five does it catch?"
},
{
 "app":"Gamma","sec":"S2 &middot; Another tool","mins":"~15 min",
 "title":"D2.2 &middot; Same prompt, different tool",
 "scenario":"Take the prompt you just wrote and run it somewhere else. This is the whole point of learning the prompt rather than the product.",
 "launches":[{"label":"Open Gamma","href":GAMMA,"note":"Free account is enough. Paste the same prompt and generate."},
             {"label":"Open Claude","href":CLAUDE,"note":"To copy your prompt back out of yesterday's conversation."}],
 "goal":"Produce the same six slide summary in Gamma, then decide which tool you would actually use for this job, and be able to say why in one sentence.",
 "steps":["Copy the prompt you wrote in D2.1. The exact same one, not an improved version.",
          "Generate the deck in Gamma and pick a theme.",
          "Put the two decks side by side and answer the questions below honestly.",
          "Export the Gamma deck to PowerPoint and see what shifts."],
 "findings":[{"label":"Which gave the better first draft?","hint":"Claude Design or Gamma"},
             {"label":"Which needed less fixing?","hint":"and roughly how much less"},
             {"label":"What broke in the PowerPoint export?","hint":"spacing, fonts, charts, nothing"},
             {"label":"Which would you use on Sunday?","hint":"one sentence, with a reason"}],
 "expect":"Two decks from one prompt, and a clear personal answer on which tool suits which job. There is no right answer here. There is only your answer with a reason attached.",
 "stretch":"Change one word in the prompt, the audience, and regenerate in both. Which tool responds more to the change?",
 "boss":"Build it a third way. Ask Claude for the outline only, then paste that outline into Gamma. Does the hybrid beat either tool on its own?"
},
{
 "app":"Claude","sec":"S3 &middot; Data analysis","mins":"~20 min",
 "title":"D2.3 &middot; Clean it before you trust it",
 "scenario":"A staff survey export lands on your desk. Before you ask it what it says, ask it what is wrong with it. This is the habit that separates an analyst from a person with a spreadsheet.",
 "dataset":SAT,
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Upload the CSV, then work the two steps below."}],
 "steps":["Download the file and upload it to Claude.",
          "Write your own prompt for each step. Run it, then verify the counts yourself before you believe them."],
 "promptSteps":[
  {"label":"Step 1 &middot; Profile the file",
   "goal":"Get Claude to tell you what is wrong with the data before it tells you what the data says. Duplicates, blanks, impossible values, and any column where the same thing is spelled more than one way.",
   "prompt":"Before analysing anything, profile this file. Tell me: how many rows, how many exact duplicate rows, how many blank values in each column, any value outside the valid range for its column, and any column where the same category is spelled more than one way. Show me the specific row identifiers, not just counts.",
   "findings":[{"label":"How many exact duplicate rows?","hint":"and which response ids"},
               {"label":"How many blank overall scores?","hint":"count them yourself too"},
               {"label":"Any score outside 1 to 5?","hint":"the value and the row"},
               {"label":"How many spellings of one department?","hint":"list them"}]},
  {"label":"Step 2 &middot; The headline, before and after",
   "goal":"Get the company average overall satisfaction two ways: the raw file as it arrived, and the cleaned file. Then look at how little the headline moved.",
   "prompt":"Now give me the company average overall satisfaction two ways. First on the raw file exactly as it arrived. Second on a cleaned version with duplicates removed, blanks excluded, and out of range values removed. Show the count of responses behind each number.",
   "findings":[{"label":"Raw average","hint":"and how many responses"},
               {"label":"Cleaned average","hint":"and how many responses"},
               {"label":"How much did the headline move?","hint":"the difference"}]}
 ],
 "expect":"A profile of the file naming specific rows, and two averages with the response count behind each. The headline barely moves. Everything underneath it does.",
 "stretch":"One free text comment identifies its author in a survey that promised anonymity. Find it. Then decide what you would do if it were real.",
 "boss":"Ask Claude to redo the department breakdown twice: once with the spelling variants left alone, and once merged. How many departments does the messy version invent, and how many people are in each?"
},
{
 "app":"Claude","sec":"S3 &middot; Data analysis","mins":"~18 min",
 "title":"D2.4 &middot; The answer and the trap",
 "scenario":"Now the actual question. Which team is struggling, on what, and what would you recommend. The trap in this file is the kind that reaches a board pack.",
 "dataset":SAT,
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Keep working in the same conversation as D2.3, so the cleaning carries over."}],
 "goal":"Name the least satisfied department, the weakest question company wide, and one recommendation that goes to a named owner. Every claim carries a number and a sample size.",
 "steps":["Stay in the same conversation. The cleaned data is already there.",
          "Write your own prompt for the analysis. Insist on the sample size next to every average.",
          "Read the ranking carefully before you believe the top of it."],
 "promptSteps":[
  {"label":"The analysis prompt",
   "goal":"A department ranking and a question ranking, each with the number of responses behind it, so you can tell a real result from noise.",
   "prompt":"Using the cleaned data, rank the departments by average overall satisfaction and rank the six questions by average score. Put the number of responses next to every single average. Then tell me which result you would not report to leadership, and why.",
   "findings":[{"label":"Least satisfied department","hint":"name, score, and how many people"},
               {"label":"Weakest question company wide","hint":"question and score"},
               {"label":"Which department looks best?","hint":"name, score, and how many people"},
               {"label":"Would you report that top result?","hint":"yes or no, and why"}]}
 ],
 "expect":"A ranking you can defend line by line, and a clear view of which entry in it is noise with a title on top.",
 "stretch":"Look at the strongest question and the weakest question together. They tell a story about the company that neither tells alone. Write it in one sentence.",
 "boss":"Find a statement about this data that is completely true and completely misleading. Write it as it would appear on a slide. Then write the sentence that corrects it."
},
{
 "app":"Claude","sec":"S4 &middot; Validation","mins":"~18 min",
 "title":"D2.5 &middot; Three answers to one question",
 "scenario":"A simple question with a simple answer: how far over budget are we? This file produces three defensible looking answers to that question. They differ by more than seventy thousand dinar.",
 "dataset":BUD,
 "files":[{"label":"department-budget-2026.csv","href":"department-budget-2026.csv",
           "note":"The same detail lines as plain text, if you would rather paste than upload."}],
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Upload the workbook and start with the Summary sheet."}],
 "goal":"Produce a number for the total overspend that you would put your name on, and be able to say exactly which corrections you made to get there.",
 "steps":["Upload the workbook. Look at the Summary sheet first, then the detail.",
          "Ask what the Summary says. Then ask whether the detail agrees with it.",
          "Every time the two disagree, find out why before you pick a side.",
          "Nobody finds every problem in eighteen minutes. Three is a strong result."],
 "promptSteps":[
  {"label":"Step 1 &middot; Does the summary agree with the detail?",
   "goal":"Get Claude to add the detail lines itself and compare its total against the total the Summary sheet claims.",
   "prompt":"Add up the year to date actual column from the Budget vs Actual sheet yourself, department by department, and compare your totals against the Summary sheet. Show both sets of numbers side by side and tell me every place they disagree.",
   "findings":[{"label":"What the Summary claims the overspend is","hint":"KD"},
               {"label":"What the detail lines actually add up to","hint":"KD"},
               {"label":"The gap between them","hint":"KD"}]},
  {"label":"Step 2 &middot; Audit the detail lines",
   "goal":"Get Claude to hunt the detail for the things that quietly break a total: values stored as text, duplicated rows, a sign the wrong way round, and a percentage computed on the wrong base.",
   "prompt":"Now audit the detail lines. Look specifically for: numbers stored as text, exactly duplicated line items, any amount whose sign looks wrong for what it describes, and any Variance % that was not calculated against the year to date budget. Give me the row and the effect on the total for each one.",
   "findings":[{"label":"How many problems did you find?","hint":"there are five"},
               {"label":"The one with the biggest effect","hint":"what it is, and how much"},
               {"label":"Your corrected total overspend","hint":"KD, the number you would sign"}]}
 ],
 "expect":"Three different totals, an explanation of what separates them, and one number you would defend in a meeting. If you cannot say which corrections produced your number, you do not have an answer yet.",
 "stretch":"Rank the departments by overspend before and after your corrections. Does the ranking change? Two of them swap places.",
 "boss":"Find all five problems. Then work out which single one Claude was most confident about while being wrong, and which one it missed entirely."
},
{
 "app":"Claude and Excel","sec":"S4 &middot; Validation","mins":"~15 min",
 "title":"D2.6 &middot; The formula and the chart",
 "scenario":"Two habits that make your analysis survive contact with a finance team. Ask for the formula rather than the answer. Then build a chart that makes one claim and cites its source.",
 "dataset":BUD,
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Same conversation as D2.5."}],
 "goal":"One Excel formula that reproduces your corrected total in your own spreadsheet, and two charts that each make a single claim you can defend.",
 "steps":["Step one is the formula. Step two is the charts.",
          "For the formula: paste it into the real file and check it returns your number.",
          "For the charts: one claim per chart, a caption that states the claim, and a source line."],
 "promptSteps":[
  {"label":"Step 1 &middot; Ask for the formula, not the answer",
   "goal":"Get an Excel formula you can paste into the sheet yourself, so the number is reproducible by somebody who does not trust you.",
   "prompt":"Do not give me the number. Give me the Excel formula that calculates the corrected total year to date actual, excluding the duplicated line, treating the text value as a number, and correcting the sign on the credit. Write it so I can paste it straight into the sheet, and tell me which cells it assumes.",
   "findings":[{"label":"Does the formula return your number?","hint":"yes or no"},
               {"label":"If not, what was different?","hint":"and which one was right"}]},
  {"label":"Step 2 &middot; Two charts that make a claim",
   "goal":"Two charts from the corrected figures. Each one makes exactly one point, says that point in its caption, and names where the data came from.",
   "prompt":"Build two charts from the corrected figures. Chart one: overspend by department, largest first. Chart two: the five biggest line item variances. For each chart give me a caption that states the single claim the chart makes, and a source line naming the sheet and the correction I applied. No decoration, no second y axis.",
   "findings":[{"label":"Chart one, in one sentence","hint":"the claim it makes"},
               {"label":"Chart two, in one sentence","hint":"the claim it makes"},
               {"label":"Did you drop either chart?","hint":"a chart with no claim is decoration"}]}
 ],
 "expect":"A formula that reproduces your number inside Excel, and two charts you would put in the D2.1 deck without a caveat.",
 "stretch":"Add the charts to the deck you built this morning. Notice whether the deck's story changed once the numbers were corrected.",
 "boss":"Ask Claude to write the one paragraph a sceptical finance director would send back. Then answer it."
},
{
 "app":"Claude","sec":"S5 &middot; Stop retyping","mins":"~20 min",
 "title":"D2.7 &middot; The library, then one Skill",
 "scenario":"Count how many times today you typed the same instruction. Everything above was practice. This is the part you keep and reuse next week.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Start a fresh conversation for this one."}],
 "goal":"At least five reusable prompts written with placeholders, one of them for a task only your department has, and one of them turned into a working Claude Skill that you have actually run once.",
 "steps":["Scroll back through the last two days and find the prompts that worked best.",
          "For each, save four things: a title, the prompt with [PLACEHOLDERS], the tool it suits, and what you had to fix afterwards.",
          "Add one prompt for a task in your own department that nobody else in this room would need.",
          "Then turn your single best prompt into a Skill, and run it once to prove it works."],
 "promptSteps":[
  {"label":"Step 1 &middot; Build the library",
   "goal":"Turn a pile of chat history into a document you will open again on a Tuesday morning.",
   "prompt":"Here are the prompts that worked for me over the last two days: [PASTE THEM]. Turn them into a clean prompt library. For each one give a short title that says when I would reach for it, the prompt itself with [PLACEHOLDERS] where the details change, the tool it suits, and a one line note on what to check in the output. Format it as a document I can save.",
   "findings":[{"label":"How many prompts did you save?","hint":"five is the target"},
               {"label":"The one for your own department","hint":"what task is it for?"},
               {"label":"Where did you save it?","hint":"be specific, you will need this next week"}]},
  {"label":"Step 2 &middot; Turn the best one into a Skill",
   "goal":"A Skill is a saved instruction Claude loads on its own when the task matches, so you stop pasting the same prompt. Build one from your strongest prompt and run it.",
   "prompt":"I want to turn this prompt into a reusable Skill: [PASTE YOUR BEST PROMPT]. Write it as a Skill: a short name, a one line description of when it should trigger, and the full instructions. Keep the instructions specific enough that the output is consistent, and general enough that it works on any input of this type.",
   "findings":[{"label":"What did you name your Skill?","hint":"the name"},
               {"label":"When should it trigger?","hint":"one line"},
               {"label":"Did it work when you ran it?","hint":"yes, or what you had to change"}]}
 ],
 "expect":"A saved document with at least five ready to reuse prompts, one written for your own job, and one working Skill you have run at least once.",
 "stretch":"Ask Claude to spot the pattern across your saved prompts. What do your best ones have that the weaker ones do not?",
 "boss":"Write the prompt you would hand a colleague who was not here, so they could get one of today's results without the workshop. If it needs explaining out loud, it is not finished."
},
]

html = page("Day 2 Lab &middot; AI Essentials in the Workplace",
            json.dumps(TASKS, ensure_ascii=False),
            "Day 2 &middot; Presentations and data", "Day 2",
            "aiet_day2_lab", "coded-aiet-day-2.html")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site', 'coded-aiet-day-2-lab.html')
open(out,'w').write(html)
print('tasks:', len(TASKS), 'bytes:', len(html), 'em:', html.count('—'))
