# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lab_shell import page

CLAUDE="https://claude.ai/new"; GAMMA="https://gamma.app"

def sc(key,label,q,files,head,rows,more):
    return {"key":key,"label":label,"q":q,"files":files,"head":head,"rows":rows,"more":more}

SCEN = [
 sc("a","A &middot; Operations","Hire, or keep paying overtime?",
    [("ops-overtime-2026.csv","Nine months of overtime by team and month: hours, cost, headcount, absence days per person, and open vacancies."),
     ("ops-hiring-costs-2026.csv","Salary, recruitment cost, onboarding time, standard monthly hours and the overtime rate for each role.")],
    ["month","team","overtime_hours","overtime_cost_kd","headcount","absence_days","open_vacancies"],
    [["2026-01","Night Shift","115","862.50","12","3.14","0"],
     ["2026-01","Warehouse","138","897.00","34","1.42","1"],
     ["2026-07","Warehouse","264","(blank)","34","1.51","1"],
     ["2026-08","Night Shift","9999","1221.00","10","3.02","2"]],
    "46 rows across five teams. Look hard at that last one."),
 sc("b","B &middot; Human Resources","Where does the retention budget go?",
    [("hr-leavers-2026.csv","Eighteen months of leavers: department, hire and leave dates, tenure band, reason, whether they went voluntarily, and whether an exit interview happened."),
     ("hr-headcount-2026.csv","Average headcount and number of locations per department, for the same period.")],
    ["employee_id","department","hire_date","leave_date","tenure_band","leave_reason","voluntary"],
    [["E4087","Retail Operations","2025-01-05","2025-07-19","6-12 months","better offer elsewhere","Yes"],
     ["E4110","Customer Care","2025-09-08","2025-09-08","1-2 years","No development opportunities","Yes"]],
    "146 leavers across seven departments. The biggest number is not the biggest problem."),
 sc("c","C &middot; Customer Service","Which channel is failing?",
    [("cs-tickets-2026.csv","Six months of tickets: channel, date, hour opened, request type, first response time, whether it resolved first contact, and a satisfaction score."),
     ("cs-staffing-2026.csv","Agents assigned, hours covered and the response target for each channel.")],
    ["ticket_id","channel","date_opened","hour_opened","first_response_hours","resolved_first","satisfaction"],
    [["T70001","WhatsApp","2026-04-23","10:00","2.5","No","5"],
     ["T70002","Walk-in","2026-05-09","17:00","0.3","Yes","3"]],
    "564 tickets across five channels. One channel breaches almost every time and has the happiest customers."),
 sc("d","D &middot; Procurement","Consolidate, or not?",
    [("procurement-purchase-orders-2026.xlsx","A year of purchase orders: date, category, supplier, value, delivery days, whether it arrived on time, and who requested it."),
     ("procurement-purchase-orders-2026.csv","The same rows as plain text, if you would rather paste than upload.")],
    ["po_number","order_date","category","supplier","value_kd","delivery_days","on_time"],
    [["PO90021","2026-02-14","IT hardware","Gulf Digital Supply","3266","18","No"],
     ["PO90126","2026-09-02","Office supplies","Office Plus Kuwait","313","12","Yes"]],
    "193 orders across five categories. Count the suppliers carefully before you rank them."),
]

def scen_widget():
    tabs='<div class="lw-tabs">'+''.join(
      '<button class="lw-tab%s" data-sc="%s">%s</button>'%(' on' if i==0 else '', s["key"], s["label"])
      for i,s in enumerate(SCEN))+'</div>'
    job='<div class="lw-job">'+''.join(
      '<span data-sc="%s"%s><b>The question you must answer:</b> %s</span>'
      %(s["key"], '' if i==0 else ' hidden', s["q"]) for i,s in enumerate(SCEN))+'</div>'
    docs='<div class="lw-doc">'
    for i,s in enumerate(SCEN):
        rows=''.join('<tr>'+''.join('<td>'+c+'</td>' for c in r)+'</tr>' for r in s["rows"])
        dls=''.join('<a class="dl" href="%s" download><span class="ic">&#11015;</span>'
                    '<span>Download<small>%s</small></span></a><div class="ds-note">%s</div>'
                    %(f,f,note) for f,note in s["files"])
        docs+=('<div data-sc="%s"%s>%s<div class="ds-table-wrap"><table class="ds-table"><thead><tr>%s</tr></thead>'
               '<tbody>%s</tbody></table><div class="ds-more">%s</div></div></div>'
               %(s["key"], '' if i==0 else ' hidden', dls,
                 ''.join('<th>'+h+'</th>' for h in s["head"]), rows, s["more"]))
    docs+='</div>'
    e = ('<div data-sc="e" hidden><div class="ds-note"><b>Scenario E: your own work.</b> '
         'Answer these four before you start, and check them with the instructor.<br><br>'
         '1. Can you name the decision somebody actually has to make?<br>'
         '2. Do you have the data in front of you, today, in a file?<br>'
         '3. Have you redacted every name, ID, salary and contract reference?<br>'
         '4. Would you be comfortable if this file appeared on a screen in this room?<br><br>'
         'Four yeses and you are clear. Anything else, take Scenario A to D. '
         'You can do your own work on Sunday, with more time and no audience.</div></div>')
    tabs=tabs.replace('</div>','<button class="lw-tab" data-sc="e">E &middot; Your own work</button></div>')
    job=job.replace('</div>','<span data-sc="e" hidden><b>Your job:</b> the same four deliverables, '
                    'on your own redacted data. Instructor sign off required first.</span></div>')
    docs=docs.replace('</div>', e+'</div>', 1) if False else docs[:-6]+e+'</div>'
    return tabs+job+docs

TASKS=[
{
 "app":"Claude","sec":"S1 &middot; Connectors and Skills","mins":"~18 min",
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
   "goal":"Plenty of companies do, and that is a reasonable position. Do this instead, and you will get the same lesson without needing permission.",
   "prompt":"I want to understand what a connector would change for me. Here is a task I do weekly: [DESCRIBE IT]. Walk me through exactly what a connector to [TOOL] would read, what it would not read, what it would let me stop doing by hand, and what I would need to tell my IT team to get it approved. Be specific about the risks, not reassuring."},
  {"label":"The question to take to IT",
   "goal":"Turn what you just learned into something your IT team can actually answer, rather than a request they have to refuse.",
   "prompt":"Draft the message I would send to my IT or security team asking about connector access. Say what I want to connect, what business task it serves, what data it would touch, and what controls I am asking them to confirm. Short, specific, and easy to say yes or no to."}],
 "findings":[{"label":"What did you connect?","hint":"or, what would you connect first"},
             {"label":"The question that only worked with it","hint":"one line"},
             {"label":"What changed when you revoked it?","hint":"be specific"}],
 "expect":"A connector you have turned on and off yourself, or a specific, sendable request to your IT team. Either one means you understand what you are asking for.",
 "stretch":"Ask Claude what it can see through the connector that you did not expect. The answer is occasionally uncomfortable, and always worth knowing.",
 "boss":"Write the one paragraph a security reviewer would send back rejecting your request. Then rewrite your request so it survives that paragraph."
},
{
 "app":"Paper first, then Claude","sec":"S2 &middot; Workflow audit","mins":"~22 min",
 "title":"D3.2 &middot; The workflow audit",
 "scenario":"One real task you do every week and resent. Map it honestly, including the steps nobody counts, then pick the single thing worth changing.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Do the mapping on paper first. Bring it to Claude at step four."}],
 "goal":"One task fully mapped with minutes attached, every step marked P or J, an honest yearly cost, and exactly one opportunity chosen.",
 "steps":["Do the first three steps on paper. It is faster and you will be more honest.",
          "List every step with its minutes, including finding the file, chasing the input, and waiting for approval.",
          "Mark each step <b>P</b> for pattern or <b>J</b> for judgment.",
          "Multiply the total by how often you do it. Write the yearly hours down.",
          "Pick one P step. The one that costs the most and that you would still check afterwards."],
 "promptSteps":[
  {"label":"Step 4 &middot; Pressure test it",
   "goal":"Get Claude to argue with your map. It will find the steps you skipped and the ones you marked P that are really J.",
   "prompt":"Here is a weekly task of mine, mapped step by step with minutes: [PASTE YOUR MAP]. I have marked each step P for pattern or J for judgment. Argue with me. Which steps did I probably forget? Which did I mark P that are really J, and why? Which single step would you automate first, and which one should never be automated? Be direct, not encouraging.",
   "findings":[{"label":"Total minutes, one run","hint":"be honest, include the waiting"},
               {"label":"Times per year","hint":"weekly is 48, fortnightly is 24"},
               {"label":"Hours per year","hint":"multiply them"},
               {"label":"The one P step you chose","hint":"name it"},
               {"label":"A step Claude said was really J","hint":"did you agree?"}]}],
 "expect":"A yearly number that surprises you, and one chosen opportunity you can name in a sentence. If you chose five, you chose none.",
 "stretch":"Map the same task as it would run after the change. What is the new yearly number, and what did you have to add to make it safe?",
 "boss":"Find a step in your task that <b>should not be automated even though it easily could be</b>. Write the one sentence explaining why to somebody who only sees the time saving."
},
{
 "app":"Claude","sec":"S3 &middot; Capstone","mins":"~40 min",
 "title":"D3.3 &middot; Interrogate the data",
 "scenario":"Pick one scenario and answer the question it asks. Every file has deliberate problems in it, exactly like yesterday. Every scenario also has a second story that contradicts the obvious answer.",
 "widget": scen_widget(), "widgetFirst": True, "widgetLabel": "Pick your scenario",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Upload both files for your scenario and work in one conversation."}],
 "goal":"A defensible answer to the scenario question, backed by numbers you have checked, plus the second story that the first answer hides.",
 "steps":["Pick your scenario above and download both files.",
          "Profile them before you analyse them. Duplicates, blanks, impossible values, spelling variants.",
          "Answer the question the scenario actually asks. With numbers.",
          "Then hunt the second story. It is there in every scenario.",
          "Build your charts now, while the working is in front of you."],
 "promptSteps":[
  {"label":"Step 1 &middot; Profile before you analyse",
   "goal":"Find what is wrong with the files before you let them tell you anything.",
   "prompt":"Before analysing anything, profile both attached files. Report: row counts, exact duplicate rows, blank cells by column, any value that is impossible for its column, and any category spelled more than one way. Give me specific row identifiers. Then tell me which of these problems would change a headline number, and by roughly how much.",
   "findings":[{"label":"Problems you found","hint":"how many, and the worst one"},
               {"label":"The one that would change a headline","hint":"which, and by how much"}]},
  {"label":"Step 2 &middot; Answer the question",
   "goal":"The actual decision, with the arithmetic shown so you can check it and so you can defend it at 13:20.",
   "prompt":"Now answer the scenario question using the cleaned data. Show every calculation step by step so I can check it by hand. Where you have made an assumption, say so on its own line. Do not round anything until the final answer.",
   "findings":[{"label":"Your answer, in one sentence","hint":"the decision, not the description"},
               {"label":"The number behind it","hint":"and what it is a number of"},
               {"label":"One assumption you had to make","hint":"and whether it is safe"}]},
  {"label":"Step 3 &middot; Find the second story",
   "goal":"Every scenario has something that looks like the answer and is not, or something true that the obvious answer hides.",
   "prompt":"Now argue against your own conclusion. What in this data looks like a problem but is not? What looks fine but is not? Is there anything true here that my recommendation would hide from the reader? Give me the strongest case against what I just concluded.",
   "findings":[{"label":"The trap in your scenario","hint":"what looks like the answer and is not"},
               {"label":"Did it change your recommendation?","hint":"yes, no, or how"}]}],
 "expect":"An answer you would defend in a meeting, the working behind it, and a second finding that makes you sound like somebody who actually read the data.",
 "stretch":"Ask what the data cannot tell you. Then write the one question you would ask the department before you acted on any of this.",
 "boss":"Find the problem in your files that Claude did not flag on its own. There is at least one in every scenario that only a human notices."
},
{
 "app":"Claude or Gamma","sec":"S4 &middot; The package","mins":"~30 min",
 "title":"D3.4 &middot; Briefing, deck, templates",
 "scenario":"Turn the analysis into something a leader can act on in five minutes, and something your successor can rerun next quarter without you.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Same conversation. It already has your analysis."},
             {"label":"Open Gamma","href":GAMMA,"note":"If you preferred Gamma yesterday, build the deck here."}],
 "goal":"Three artefacts: a one page briefing with a named risk, a six slide deck with traceable figures, and prompt templates a colleague could run cold.",
 "steps":["Write the briefing first. The deck comes from the briefing, not the other way round.",
          "Build the deck. Six slides, the decision in slide one.",
          "Write the templates last, while you still remember what you actually had to do.",
          "Read the briefing out loud once before 13:20."],
 "promptSteps":[
  {"label":"Step 1 &middot; The executive briefing",
   "goal":"One page. The decision at the top, three numbers, a recommendation with a cost, and the risk named before anyone asks.",
   "prompt":"Write a one page executive briefing from our analysis. Structure: the decision being asked for in one sentence at the top, then the evidence in three numbers maximum with the file each came from, then the recommendation with what it costs or saves, then the risk that would make this wrong. Direct and factual. Do not use a number we have not verified together.",
   "findings":[{"label":"The decision, in one sentence","hint":"as it appears at the top"},
               {"label":"The risk you named","hint":"what would make you wrong"}]},
  {"label":"Step 2 &middot; The stakeholder deck",
   "goal":"Six slides from the briefing, each with one point, built the way you learned yesterday.",
   "prompt":"Turn that briefing into a six slide stakeholder deck. Slide 1 the decision as a headline. Slide 2 the situation in three numbers. Slide 3 the chart with the claim written in the caption. Slide 4 the second finding. Slide 5 the recommendation and its cost. Slide 6 the risk and the mitigation. Eight words or fewer per headline. Every figure carries its source.",
   "findings":[{"label":"Which tool did you use?","hint":"Claude Design or Gamma"},
               {"label":"How long did the deck take?","hint":"minutes"}]},
  {"label":"Step 3 &middot; The reusable templates",
   "goal":"The part that outlives today. Written so a colleague who was not here can rerun this next quarter.",
   "prompt":"Now write the reusable prompt templates for this whole piece of work, so somebody who was not in the room could rerun it next quarter. One template per stage: profiling the data, doing the analysis, arguing against the conclusion, and writing the briefing. Use [PLACEHOLDERS] for anything that changes. Add a one line note under each saying what to check in the output before trusting it.",
   "findings":[{"label":"How many templates?","hint":"four is the target"},
               {"label":"Where did you save them?","hint":"be specific"}]}],
 "expect":"A briefing, a deck and a set of templates. If somebody who was not here could rerun your analysis from the templates alone, you are finished.",
 "stretch":"Ask Claude to write the three hardest questions a sceptical director would ask about your recommendation. Prepare answers for all three before 13:20.",
 "boss":"Write the version of the briefing where your recommendation is wrong. What would have to be true for that to happen, and how quickly would you find out?"
},
{
 "app":"In the room","sec":"S5 &middot; Present","mins":"~15 min",
 "title":"D3.5 &middot; Present it",
 "scenario":"Three minutes to present, two to defend. Your peers score it and the instructor scores nothing. This is a rehearsal for the meeting, not an exam.",
 "goal":"A three minute presentation that leads with the decision, survives two minutes of questions, and shows the source of any number somebody challenges.",
 "steps":["Find your trio. Three minutes each, then two minutes of questions.",
          "Lead with the decision. Not the background, not the method, not an apology.",
          "When somebody questions a number, <b>show where it came from</b>. That is the whole test.",
          "Score each other on the six lines below. Honest scores only, they are the only useful ones."],
 "findings":[{"label":"Score: did they lead with the decision?","hint":"out of 5"},
             {"label":"Score: was every number sourced?","hint":"out of 5"},
             {"label":"Score: did they name a real risk?","hint":"out of 5"},
             {"label":"Score: could you act on this?","hint":"out of 5"},
             {"label":"The best question they were asked","hint":"write it down"},
             {"label":"One thing you will steal from their approach","hint":"be specific"}],
 "expect":"Everybody presents, everybody is questioned, and everybody leaves with one question they could not answer. That question is the most useful thing you take home.",
 "stretch":"Present it a second time in ninety seconds instead of three minutes. What did you cut, and did the argument get weaker or stronger?",
 "boss":"Present the version your most sceptical colleague would give. Same data, opposite conclusion. Then say which of the two you actually believe, and why."
},
{
 "app":"Claude","sec":"S5 &middot; After today","mins":"~8 min",
 "title":"D3.6 &middot; The Monday plan",
 "scenario":"Last task of the programme. Everything above stays theoretical unless one thing changes in your actual week. Pick that one thing and write it down before you leave.",
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Start a fresh chat. This one is for you, not for anyone else."}],
 "goal":"One task, one method, one month, written down with a date on it. Not ten things you intend to try.",
 "steps":["Go back to the workflow audit from this morning.",
          "Pick the single opportunity you chose there. Not a different, easier one.",
          "Write down exactly how you will run it differently, and when.",
          "Name the person you will tell, so somebody expects it to happen."],
 "promptSteps":[
  {"label":"The plan",
   "goal":"Something specific enough that you would notice if you had not done it.",
   "prompt":"I want to change one thing about how I work, starting Monday. The task is: [YOUR TASK]. The step I am changing is: [THE P STEP]. Write me a plan for the next four weeks: what I do the first time, what I check every time before I trust the output, what would tell me it is not working, and what I should have to show for it after a month. Keep it to one short page. Do not add anything I did not ask for.",
   "findings":[{"label":"The one task you are changing","hint":"name it"},
               {"label":"When you will do it first","hint":"a date, not 'soon'"},
               {"label":"What you check before you trust it","hint":"one line"},
               {"label":"Who you told","hint":"a name"}]}],
 "expect":"A one page plan with a date and a name on it. The date and the name are what make it happen.",
 "stretch":"Write the note you would send that person now, so it is already sent before you leave the room.",
 "boss":"Write what you would tell somebody in four weeks if it did not work. Naming the failure in advance makes it far easier to admit, and far easier to fix."
},
{
 "app":"Assessment","sec":"S6 &middot; Close","mins":"~25 min",
 "title":"D3.7 &middot; Quiz, test and survey",
 "scenario":"Three short things, in this order. The quiz is a warm up. The MAP test is the same one you took on Tuesday morning. The survey is how the next version of this programme gets better.",
 "goal":"All three done before 14:00, and one honest sentence in the survey that would be uncomfortable to say out loud.",
 "steps":["<b>13:35</b> Quiz. The instructor gives you the link.",
          "<b>13:45</b> Post-program MAP test. Word for word the test from Tuesday morning.",
          "<b>13:52</b> End of program survey. Five minutes, and please be blunt.",
          "<b>13:57</b> Certificates and a photograph."],
 "findings":[{"label":"Quiz score","hint":"for your own reference"},
             {"label":"The topic you scored lowest on","hint":"that is your revision list"},
             {"label":"One thing you would change about this programme","hint":"put this in the survey too"}],
 "expect":"Quiz done, test submitted, survey submitted. Then a certificate and a photograph.",
 "stretch":"Look at the topics you got wrong and go back to the relevant day page. All three stay online after today.",
 "boss":"Write down the one question from the quiz you were least sure about, then go and find the answer yourself rather than asking."
},
]

html = page("Day 3 Lab &middot; AI Essentials in the Workplace",
            json.dumps(TASKS, ensure_ascii=False),
            "Day 3 &middot; Features and capstone", "Day 3",
            "aiet_day3_lab", "coded-aiet-day-3.html")
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','site','coded-aiet-day-3-lab.html')
open(out,'w').write(html)
print('tasks:',len(TASKS),'bytes:',len(html),'em:',html.count('—'))
