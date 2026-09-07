# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lab_shell import page

CLAUDE="https://claude.ai/new"; GAMMA="https://gamma.app"

# ---------------------------------------------------------------- the ideas
IDEAS = [
 {"n":"01","name":"The Overtime Decision","dept":"Operations",
  "sit":"Overtime has been climbing for nine months while headcount falls. Two vacancies have been open since April and were never filled. One team is running noticeably higher absence than every other.",
  "ini":"A staffing decision you can defend in a budget meeting: hire, or keep paying overtime. Say which team, how many people, and what it costs or saves in year one.",
  "files":[("ops-overtime-2026.csv","Nine months of overtime by team and month: hours, cost, headcount, absence per person, open vacancies."),
           ("ops-hiring-costs-2026.csv","Salary, recruitment cost, onboarding weeks, standard hours and the overtime rate for each role.")],
  "warn":"One row is obviously impossible. Do not just delete it. The cost cell on that row is correct, so the real number can be recovered."},

 {"n":"02","name":"The Retention Programme","dept":"Human Resources",
  "sit":"146 people left over eighteen months. Leadership believes the problem is the biggest department and that people leave for money. Neither belief has been tested against the data.",
  "ini":"A targeted retention programme: which department the budget goes to, what the actual leaving reason is, and two interventions with an owner each.",
  "files":[("hr-leavers-2026.csv","Eighteen months of leavers: department, hire and leave dates, tenure band, reason, voluntary, exit interview done."),
           ("hr-headcount-2026.csv","Average headcount and number of locations per department, same period.")],
  "warn":"The department with the most leavers is not the department with the problem. You need both files to prove that."},

 {"n":"03","name":"The Channel Rescue","dept":"Customer Service",
  "sit":"564 tickets across five channels in six months. One channel breaches its target on almost every ticket and yet has the happiest customers in the business. Another is quietly collapsing.",
  "ini":"A channel rescue plan: name the channel that is genuinely failing, say why, and propose a staffing or target change with the numbers behind it.",
  "files":[("cs-tickets-2026.csv","Six months of tickets: channel, date, hour, request type, first response hours, resolved first contact, satisfaction."),
           ("cs-staffing-2026.csv","Agents assigned, hours covered and the response target for each channel.")],
  "warn":"A high breach rate is not proof of failure. Before you accuse a channel, check whether its target was ever realistic."},

 {"n":"04","name":"The Supplier Consolidation","dept":"Procurement",
  "sit":"193 purchase orders across five categories and a long tail of suppliers. Spend is concentrated in one category, and one supplier delivers late far more often than the rest.",
  "ini":"A consolidation recommendation: which category to address first, which supplier relationships to keep or exit, and what the change is worth.",
  "files":[("procurement-purchase-orders-2026.xlsx","A year of purchase orders: date, category, supplier, value, delivery days, on time, requested by."),
           ("procurement-purchase-orders-2026.csv","The same rows as plain text, if you would rather paste than upload.")],
  "warn":"Count your suppliers before you rank them. At least one appears under more than one spelling, and it changes the ranking."},

 {"n":"05","name":"The Recognition Programme","dept":"People",
  "sit":"161 staff responded to the engagement survey. One department scores far below every other, and one question scores worst across the whole company. The file itself is not clean.",
  "ini":"A 90 day recognition programme: two actions aimed at the weakest score, an owner for each, and a pulse survey to prove movement.",
  "files":[("employee-satisfaction-2026.csv","161 survey responses. Six questions scored 1 to 5, an overall score, and free text comments.")],
  "warn":"The department that looks best has three responses in it. Say what the data supports, and admit what it cannot."},

 {"n":"06","name":"The Cost Control Programme","dept":"Finance",
  "sit":"The year to date position is over budget, and the Summary sheet does not agree with the detail behind it. Three defensible answers exist to the question of how far over.",
  "ini":"A cost control programme for the next quarter: three concrete measures, each tied to a budget line, plus a monthly variance review so overruns surface in weeks.",
  "files":[("department-budget-2026.xlsx","Two sheets: 32 detail lines with budget against actual, and a department Summary."),
           ("department-budget-2026.csv","The same detail lines as plain text.")],
  "warn":"Every saving you promise must trace to a line in the workbook. A saving with no line behind it is a wish."},

 {"n":"07","name":"Your Own Work","dept":"Bring your own",
  "sit":"A decision from your own department, using your own data. Better than any of ours, if it clears the gate.",
  "ini":"The same four deliverables, on your own redacted material. The instructor signs it off before you start.",
  "files":[],
  "warn":"Four questions first, and all four must be yes. Can you name the decision somebody has to make? Do you have the data in a file today? Have you redacted every name, ID, salary and contract reference? Would you be comfortable if this file appeared on a screen in this room? Anything less than four, take one of ours."},
]

def ideas_widget():
    out='<div class="ds-note" style="margin-bottom:14px">Read two. Pick one. Commit before you open a single tool.</div>'
    for i in IDEAS:
        dls=''.join('<a class="dl" href="%s" download><span class="ic">&#11015;</span>'
                    '<span>Download<small>%s</small></span></a>'
                    '<div class="ds-note" style="margin:4px 0 12px">%s</div>'%(f,f,note)
                    for f,note in i["files"])
        out+=('<details class="idea"><summary>%s &middot; %s<span class="dept">%s</span></summary>'
              '<div class="body">'
              '<p><b>The situation.</b> %s</p>'
              '<p><b>Your initiative.</b> %s</p>'
              '%s'
              '<p class="warn"><b>Watch out.</b> %s</p>'
              '</div></details>'
              %(i["n"], i["name"], i["dept"], i["sit"], i["ini"],
                (('<p><b>Your data.</b></p>'+dls) if i["files"] else ''), i["warn"]))
    return out

TASKS=[
{
 "app":"Claude","sec":"S1 &middot; Connectors and Skills","mins":"~15 min",
 "title":"D3.1 &middot; Connect something real",
 "scenario":"Two days of pasting. Now stop. Turn on one connector, ask a question that only works because of it, then turn it off again and watch the answer change.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Connector settings live in your account settings."}],
 "goal":"One working connector, one answer you could not have got without it, and the confidence to explain to your IT team exactly what it does and how to revoke it.",
 "steps":["Open the connector settings and <b>read what one actually asks for</b> before you enable anything.",
          "Turn on a connector you are permitted to use.",
          "Ask a question that only works because of the connection.",
          "Revoke it, ask the same question again, and note what changed."],
 "promptSteps":[
  {"label":"If your organization blocks connectors",
   "goal":"Plenty of companies do, and that is a reasonable position. Do this instead and you get the same lesson without needing permission.",
   "prompt":"I want to understand what a connector would change for me. Here is a task I do weekly: [DESCRIBE IT]. Walk me through exactly what a connector to [TOOL] would read, what it would not read, what it would let me stop doing by hand, and what I would need to tell my IT team to get it approved. Be specific about the risks, not reassuring."},
  {"label":"The question to take to IT",
   "goal":"Turn what you just learned into something your IT team can actually answer, rather than a request they have to refuse.",
   "prompt":"Draft the message I would send to my IT or security team asking about connector access. Say what I want to connect, what business task it serves, what data it would touch, and what controls I am asking them to confirm. Short, specific, and easy to say yes or no to."}],
 "findings":[{"label":"What did you connect?","hint":"or, what would you connect first"},
             {"label":"The question that only worked with it","hint":"one line"},
             {"label":"What changed when you revoked it?","hint":"be specific"}],
 "expect":"A connector you have turned on and off yourself, or a specific, sendable request to your IT team. Either one means you understand what you are asking for.",
 "stretch":"Ask Claude what it can see through the connector that you did not expect. The answer is occasionally uncomfortable, and always worth knowing.",
 "boss":"Write the one paragraph a security reviewer would send back rejecting your request. Then rewrite the request so it survives that paragraph."
},
{
 "app":"In pairs","sec":"Capstone &middot; Phase 0","mins":"~10 min",
 "title":"D3.2 &middot; Phase 0. Pick your idea",
 "scenario":"Ten minutes, no tools open. Pair up, read two ideas, pick one, download your data, and agree who does what. For every deliverable one of you builds, the other verifies.",
 "widget": ideas_widget(), "widgetFirst": True, "widgetLabel": "Seven ideas. Pick one.",
 "goal":"An idea you both understand, the data open on one screen, and a role split written down. Nothing built yet, which is the whole point of Phase 0.",
 "steps":["Pair up. Somebody who does not do your job makes a better partner.",
          "Read two ideas above together. Pick one and <b>commit</b>. Do not shop around.",
          "Download your data and open it once, together, before anything else.",
          "Write down who <b>builds</b> and who <b>verifies</b> for each of the four deliverables."],
 "findings":[{"label":"Your idea","hint":"the number and the name"},
             {"label":"Who builds, who verifies","hint":"deliverable by deliverable"},
             {"label":"Your one sentence recommendation, before any analysis","hint":"you will check this at the end"}],
 "expect":"One idea, both of you clear on it, data downloaded, and a role split you have actually written down.",
 "stretch":"Write the one sentence version of your recommendation now, before the data. At the end, check whether the data changed your mind. If it did not, be suspicious of yourself.",
 "boss":"Name the single number in your data most likely to sink the initiative if it turns out to be wrong. That is the first thing the verifier checks."
},
{
 "app":"Claude","sec":"Capstone &middot; D1","mins":"~40 min",
 "title":"D3.3 &middot; Deliverable 1. Executive briefing",
 "scenario":"One page a director reads in ninety seconds: the decision, the evidence, the recommendation, the risk. You write the prompt from your idea, using everything from the last two days.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"One conversation for the whole capstone. Keep it open."}],
 "goal":"A one page briefing where the recommendation leads, every figure traces to your file, and the risk is named before anyone asks for it.",
 "steps":["Attach your data to one new Claude conversation and keep it for the whole capstone.",
          "Profile the files before you analyse them. You know how by now.",
          "Answer the question your idea asks. With numbers, and with the working shown.",
          "Then write the briefing. The verifier checks every figure against the file."],
 "promptSteps":[
  {"label":"Step 1 &middot; Profile, then answer",
   "goal":"Find what is wrong with the files before you let them tell you anything, then answer the actual question.",
   "prompt":"Before analysing anything, profile the attached files. Report row counts, exact duplicate rows, blank cells by column, any value impossible for its column, and any category spelled more than one way. Give me row identifiers. Then answer this question using the cleaned data, showing every calculation step by step: [YOUR IDEA'S QUESTION]. Where you assume something, say so on its own line.",
   "findings":[{"label":"Problems you found in the data","hint":"how many, and the worst one"},
               {"label":"Your answer, in one sentence","hint":"the decision, not a description"},
               {"label":"The number behind it","hint":"and what it is a number of"}]},
  {"label":"Step 2 &middot; Argue against yourself",
   "goal":"Every idea here has a trap that survives one question. Find yours before the room does.",
   "prompt":"Now argue against my conclusion. What in this data looks like a problem but is not? What looks fine but is not? Is there anything true here that my recommendation would hide from the reader? Give me the strongest case against what I just concluded.",
   "findings":[{"label":"The trap in your data","hint":"what looks like the answer and is not"},
               {"label":"Did it change your recommendation?","hint":"yes, no, or how"}]},
  {"label":"Step 3 &middot; The briefing",
   "goal":"One page. Decision at the top, three numbers, a recommendation with a cost, and the risk that would make you wrong.",
   "prompt":"Write a one page executive briefing from our analysis. Structure: the decision being asked for in one sentence at the top, then the evidence in three numbers maximum with the file each came from, then the recommendation with what it costs or saves, then the risk that would make this wrong. Direct and factual. Do not use a number we have not verified together.",
   "findings":[{"label":"The decision, in one sentence","hint":"as it appears at the top"},
               {"label":"The risk you named","hint":"what would make you wrong"},
               {"label":"Verifier: which figure did you check?","hint":"and did it hold up"}]}],
 "expect":"A one page briefing where the recommendation leads and every figure traces to your data. Ninety seconds to read, nothing wasted.",
 "stretch":"Ask Claude to attack it. “What would a sceptical finance director push back on in this briefing?” Fix the two best objections.",
 "boss":"Write the 60 word version, for the executive who will not read even one page. Same recommendation, nothing lost that matters."
},
{
 "app":"Claude Design or Gamma","sec":"Capstone &middot; D2","mins":"~35 min",
 "title":"D3.4 &middot; Deliverable 2. Stakeholder deck",
 "scenario":"Five or six slides that carry your briefing into a room. You compared the two tools yesterday. Now pick the one that fits this job and build it.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Same conversation. It already has your analysis and your briefing."},
             {"label":"Open Gamma","href":GAMMA,"note":"If you preferred Gamma yesterday, build it here."}],
 "goal":"A five or six slide deck that tells the same story as the briefing, with every number checked by the person who did not build it.",
 "steps":["Choose your tool. One sentence on why, in the findings box.",
          "Five or six slides: the decision, the situation, the evidence, the recommendation, the plan.",
          "Every headline eight words or fewer. Every figure carries its source.",
          "The verifier opens two slides and checks them against the data."],
 "promptSteps":[
  {"label":"The deck prompt",
   "goal":"The briefing turned into slides, without the story drifting on the way.",
   "prompt":"Turn that briefing into a six slide stakeholder deck. Slide 1 the decision as a headline. Slide 2 the situation in three numbers. Slide 3 the evidence with the claim written in the caption. Slide 4 the second finding, the one that complicates the obvious answer. Slide 5 the recommendation and its cost. Slide 6 the risk and what we would do about it. Eight words or fewer per headline. Every figure carries its source.",
   "findings":[{"label":"Which tool, and why","hint":"one sentence"},
               {"label":"A figure the verifier checked on a slide","hint":"and whether it held"}]}],
 "expect":"A five or six slide deck that tells the same story as the briefing. If the deck and the briefing disagree anywhere, one of them is wrong and you need to know which.",
 "stretch":"Regenerate your evidence slide for a different audience, the front line team rather than the director. Notice what has to change, and what must not.",
 "boss":"Run the same prompt in the other tool and keep whichever deck is honestly better. Be ready to say why when the room asks."
},
{
 "app":"Claude","sec":"Capstone &middot; D3","mins":"~25 min",
 "title":"D3.5 &middot; Deliverable 3. Charts that argue",
 "scenario":"Two or three charts that carry the argument, each with one written insight underneath. Not decoration. Evidence.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Same conversation."}],
 "goal":"Two or three charts, each defending exactly one claim in your briefing, each with a verified number and a one line insight. Plus the chart that argues against you.",
 "steps":["Decide the two or three claims your initiative stands on. Each gets exactly one chart.",
          "Build them. One claim, a caption that states the claim, and a source line.",
          "Ask Claude to list the exact rows behind every chart, then spot check two by hand.",
          "Build the counter chart, the one view that argues against your recommendation."],
 "promptSteps":[
  {"label":"Step 1 &middot; The charts",
   "goal":"Charts that each make one point, with the point written underneath rather than left for the reader to guess.",
   "prompt":"Build [TWO or THREE] charts from our corrected figures, one for each of these claims: [YOUR CLAIMS]. For each chart give me a caption that states the single claim the chart makes, and a source line naming the file and any correction I applied. No decoration, no second y axis, no chart that does not defend a claim.",
   "findings":[{"label":"Chart one, in one sentence","hint":"the claim it makes"},
               {"label":"Chart two, in one sentence","hint":"the claim it makes"}]},
  {"label":"Step 2 &middot; Cite the rows",
   "goal":"The single most useful verification habit of the three days. Do it here and then keep doing it at work.",
   "prompt":"List the exact rows from the source file behind every number in every chart. Give me the row identifiers, not a description.",
   "findings":[{"label":"Which two did you spot check?","hint":"and did they hold"},
               {"label":"Your counter chart","hint":"what does it show that hurts your case"}]}],
 "expect":"Two or three charts, each defending one claim, each with a verified number and a one line insight. If a chart defends nothing, it goes.",
 "stretch":"Put the counter chart in the deck rather than hiding it, and address it in the pitch before the room finds it. It reads as confidence, not weakness.",
 "boss":"Find a number in your own charts that you cannot fully trace back to a row. Then either fix it or cut it."
},
{
 "app":"Claude","sec":"Capstone &middot; D4","mins":"~15 min",
 "title":"D3.6 &middot; Deliverable 4. Communication pack",
 "scenario":"The initiative is decided. Now it has to land with the people it affects. Pick the two items that fit your audience, then bank three reusable templates.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Same conversation, so the facts already agree."}],
 "goal":"Two finished communication items that agree with the briefing on every fact, plus three templates ready for the prompt library you started yesterday.",
 "steps":["Choose TWO: an internal email to staff, a public FAQ, or a one page fact sheet.",
          "Draft them from the briefing, so the facts already agree.",
          "Write three reusable prompt templates with placeholders.",
          "The verifier checks the comms against the briefing, line by line."],
 "promptSteps":[
  {"label":"Step 1 &middot; The two items",
   "goal":"Communication that says the same thing as the briefing, in the language of the people it lands on.",
   "prompt":"From the briefing, draft [ITEM 1] and [ITEM 2] for [AUDIENCE]. Keep every fact identical to the briefing. Say what is happening, when, what it means for the reader, and what they need to do. Apologise once at most. Do not promise a date the data does not support.",
   "findings":[{"label":"Which two items, and for whom","hint":"be specific about the audience"},
               {"label":"Verifier: any fact that disagreed with the briefing?","hint":"which one"}]},
  {"label":"Step 2 &middot; Three templates",
   "goal":"The part that outlives today. Written so somebody who was not here can rerun this next quarter.",
   "prompt":"Now write three reusable prompt templates from this capstone, one per stage: profiling the data, doing the analysis, and writing the briefing. Use [PLACEHOLDERS] for anything that changes. Add a one line note under each saying what to check in the output before trusting it.",
   "findings":[{"label":"Your three templates","hint":"names only"},
               {"label":"Where did you save them?","hint":"be specific, you will want them next week"}]}],
 "expect":"Two finished communication items that agree with the briefing on every fact, plus three templates in your library.",
 "stretch":"Take one item and produce it in three lengths: a full email, a poster, and an SMS. Same facts, three formats. That is one more library entry, not three.",
 "boss":"Draft the answer to the most hostile question your audience could ask, and put it in the FAQ before anybody has to ask it out loud."
},
{
 "app":"In the room","sec":"Present","mins":"~20 min",
 "title":"D3.7 &middot; Assemble, rehearse, present",
 "scenario":"Assemble the package, run the pitch once out loud, cut what does not earn its place. Six minutes per pair, then one question from the room.",
 "goal":"A six minute pitch you have actually run once, a package that tells one consistent story, and a ready answer for the obvious challenge.",
 "steps":["Assemble: briefing, then deck with the charts in it, then the comms items. One package, one story.",
          "Run the pitch once out loud. Cut whatever does not earn its place.",
          "Present. Decision first, and both of you speak.",
          "When the question comes, <b>show where the number came from</b>. That is the whole test."],
 "findings":[{"label":"Who presents which section","hint":"agree it before you stand up"},
             {"label":"Your answer to “how do you know?”","hint":"the file, and the rows"},
             {"label":"The question you could not answer","hint":"write it down, it is the most useful thing today"},
             {"label":"One thing you will steal from another pair","hint":"be specific"}],
 "expect":"A six minute pitch you have run at least once, and a package where the briefing, the deck and the comms all say the same thing.",
 "stretch":"Prepare the three minute emergency version. Schedules slip, and the pairs who can compress still land their recommendation.",
 "boss":"Trade packages with another pair for two minutes and find one number in theirs to challenge in the questions. Expect them to do the same to you."
},
{
 "app":"Assessment","sec":"Close","mins":"~10 min",
 "title":"D3.8 &middot; Quiz, test and survey",
 "scenario":"Three short things, in this order. The quiz is a warm up. The MAP test is the same one you took on Tuesday morning. The survey is how the next version of this programme gets better.",
 "goal":"All three done before 14:00, and one honest sentence in the survey that would be uncomfortable to say out loud.",
 "steps":["<b>13:50</b> Quiz. The instructor gives you the link.",
          "<b>13:53</b> Post-program MAP test. Word for word the test from Tuesday morning.",
          "<b>13:56</b> End of program survey. Five minutes, and please be blunt.",
          "<b>13:58</b> Certificates and a photograph."],
 "findings":[{"label":"Quiz score","hint":"for your own reference"},
             {"label":"The topic you scored lowest on","hint":"that is your revision list"},
             {"label":"One thing you would change about this programme","hint":"put this in the survey too"}],
 "expect":"Quiz done, test submitted, survey submitted. Then a certificate and a photograph.",
 "stretch":"Look at the topics you got wrong and go back to the relevant day page. All three stay online after today.",
 "boss":"Write down the one question you were least sure about, then go and find the answer yourself rather than asking."
},
]

html = page("Day 3 Lab &middot; AI Essentials in the Workplace",
            json.dumps(TASKS, ensure_ascii=False),
            "Day 3 &middot; Features and capstone", "Day 3",
            "aiet_day3_lab", "coded-aiet-day-3.html")
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','site','coded-aiet-day-3-lab.html')
open(out,'w').write(html)
print('tasks:',len(TASKS),'ideas:',len(IDEAS),'bytes:',len(html),'em:',html.count('—'))
