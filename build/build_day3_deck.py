# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_shell import page, slide, qr_block

MAP_POST = "https://portal.joincoded.com/sv/ai-essentials-in-the-workplace-map-test-pre-day-1-09-00-copy"

S=[]
def add(sid,title,body,**kw): S.append(slide(sid,title,body,**kw))
def eyebrow(t,n=""): return '<div class="eyebrow b">'+t+(' <span class="tnum">'+n+'</span>' if n else '')+'</div>'
def question(sid,title,q,sub="",sec=False):
    add(sid,title,'<div class="qmark b">Question</div><h1 class="bigq b">'+q+'</h1>'
        +('<div class="qsub b">'+sub+'</div>' if sub else ''), sec=sec, center=True)
def cards(items,cls=""):
    return '<div class="spread-row '+cls+'">'+''.join(
      '<div class="sc b"><div class="sw">%s</div><div class="st">%s</div><div class="sd">%s</div></div>'%it
      for it in items)+'</div>'
def minilist(rows):
    return '<div class="mini-list">'+''.join(
      '<div class="mini-row b"><div class="mk">%s</div><div class="mv">%s</div></div>'%r for r in rows)+'</div>'
def lab(num,mins,title,steps,where="In Claude"):
    out=('<div class="labcard b"><div class="lh"><span class="lnum">Task '+str(num)+'</span>'
         '<span class="ltime">'+mins+' minutes</span><span class="lwhere">'+where+'</span></div>'
         '<div class="lt">'+title+'</div><ol class="labsteps">')
    for st in steps: out+='<li>'+st+'</li>'
    return out+('</ol><a class="labgo" href="coded-aiet-day-3-lab.html#t'+str(num)+'">'
                'Open task '+str(num)+' &rarr;</a></div>')
def usecase(sid,dept,head,safe,stop,risk):
    add(sid,'Use case &middot; '+dept,
        eyebrow('Use case &middot; '+dept) +
        '<h2 class="demo-h b">'+head+'</h2>'
        '<div class="uc">'
        '<div class="ucol safe b"><div class="uh">Safe productivity boosters</div><ul>'
        + ''.join('<li>'+x+'</li>' for x in safe) + '</ul></div>'
        '<div class="ucol stop b"><div class="uh">Strict guardrails</div><ul>'
        + ''.join('<li>'+x+'</li>' for x in stop) + '</ul></div></div>'
        '<div class="ethbar b"><b>Ethical risk:</b> '+risk+'</div>')

def brk(bid,title,head,sub,opts,note):
    o=''.join('<button class="brk-opt%s" data-min="%d"><span class="bn">%d</span><span class="bu">minutes</span></button>'
              %((' alt' if i else ''),m,m) for i,m in enumerate(opts))
    add(bid,title,eyebrow('Break')+'<h2 class="brk-h b">'+head+'</h2>'
        '<div class="brk-sub b">'+sub+'</div><div class="brk-pick b">'+o+'</div>'
        '<div class="brk-note b">'+note+'</div>', center=True)

# ============================== OPEN

add('cover','Title',
  '<div class="clock b"><span class="live-dot"></span>Day 3 &middot; Thursday 10 September 2026 &middot; 09:00 to 14:00</div>'
  '<h1 class="mega b">Your work,<br>your <span class="accent">plan</span></h1>'
  '<div class="covsub b">Two days on sample data. Today you point all of it at your own job, '
  'and present what you build.</div>'
  '<div class="covmeta b"><span>CODED Campus, Kuwait</span><span>Connectors &middot; MCP &middot; Skills</span><span>Day 3 of 3</span></div>',
  center=True)

add('outcomes','Outcomes',
  eyebrow('Today') +
  '<h2 class="demo-h b">One thing you<br>leave with.</h2>'
  '<div class="lead b">Not three this time. One package, and it has four parts.</div>'
  '<div class="road one">'
  '<div class="ritem b"><div class="rn">01</div><div><div class="rt">An executive briefing</div>'
  '<div class="rd">One page. The decision, the evidence, the recommendation, the risk.</div></div></div>'
  '<div class="ritem b"><div class="rn">02</div><div><div class="rt">A stakeholder deck with its charts</div>'
  '<div class="rd">Charts first, each defending one claim. Then six slides, built the way you learned yesterday.</div></div></div>'
  '<div class="ritem b"><div class="rn">03</div><div><div class="rt">A communication pack</div>'
  '<div class="rd">Two items that land the decision, and three templates so the next person can run it without you.</div></div></div>'
  '<div class="ritem b"><div class="rn">04</div><div><div class="rt">Three minutes in front of the room</div>'
  '<div class="rd">Then one question from the room. Expect somebody to check a number.</div></div></div>'
  '</div>')

# ---- quick review of days 1 and 2 ----

question('r0','Review','What do you remember<br>from <b>Tuesday</b>?',
         'Shout it. No hands.', sec=True)

add('r1','Review · Day 1',
    eyebrow('Review','Day 1') +
    '<h2 class="demo-h b">Day 1, in four lines.</h2>'
    + minilist([('It predicts','It kept the patterns, not the documents. That one fact explains every strength and every failure.'),
                ('Six parts','Role, Context, Task, Format, Tone, Constraints. Constraints are the half people skip.'),
                ('Show, do not describe','Two examples beat a paragraph, when the style is real but nobody wrote it down.'),
                ('Give it the source','Then check the summary back against the source. Both halves, every time.')]) +
    '<div class="keyline b">If any of those four are fuzzy, <b>say so now.</b> '
    'Today builds directly on all of them.</div>')

add('r2','Review · Day 2',
    eyebrow('Review','Day 2') +
    '<h2 class="demo-h b">Day 2, in four lines.</h2>'
    + minilist([('Profile before you trust','Duplicates, blanks, impossible values, four spellings of one department.'),
                ('The small sample trap','Three people who happen to be content will out-score forty who are fine.'),
                ('Three answers','One budget file gave you 111,050, 187,200 and 152,850. Which one did you sign?'),
                ('Ask for the formula','A number you cannot reproduce is a rumour.')]) +
    '<div class="keyline b">Today you point all of it at a real decision, '
    '<b>and somebody in this room will check your arithmetic.</b></div>')

add('r3','Review · The one rule',
    '<h2 class="close-punch b">And the rule<br>that has not changed.<br><br><b>Your name goes<br>on the output.</b></h2>',
    center=True)

# ---- privacy and data security, restored from the parked Day 1 block ----

question('p0','Security · Where it goes','Where does what you<br><b>paste</b> actually go?',
         'Today you stop using our files and start using yours.',sec=True)

add('p1','Privacy · Four boxes',
  eyebrow('Data security','0.1') +
  '<h2 class="demo-h b">Four boxes.</h2>'
  + minilist([('Box 1','Your screen. You paste the paragraph.'),
              ('Box 2','The internet. It leaves your building and your network.'),
              ('Box 3','A server somewhere else. Another country, another company\'s control.'),
              ('Box 4','A log. It may be kept. It may be reviewed by a human. It depends on the plan you are on.')]) +
  '<div class="keyline b">A free consumer account and a company account '
  '<b>are not the same on box 4.</b> Ask your IT team which one you have, today.</div>')

add('p2','Privacy · The rule',
  eyebrow('Data security','0.2') +
  '<h2 class="close-punch b">If you would not<br><b>email it to a supplier,</b><br>do not paste it.</h2>'
  '<div class="lead b" style="margin-top:30px">One sentence. It covers almost every case, '
  'and you can remember it under pressure.</div>')

add('p3','Privacy · Five second scan',
  eyebrow('Data security','0.3') +
  '<h2 class="demo-h sm b">The five second scan.</h2>'
  '<div class="lead b">Before you press paste, look for five things.</div>'
  + minilist([('Names','A person who did not agree to this'),
              ('Numbers','Account, ID, licence, passport, phone'),
              ('Contracts','Anything with a signature or a price on it'),
              ('Salary','Pay, bonus, headcount by person'),
              ('Health','Sick leave, medical notes, insurance claims')]) +
  '<div class="keyline b">Find one? <b>Replace it with a placeholder and keep going.</b> '
  'You almost never need the real value for the tool to help you.</div>')

add('p3b','Security · Anonymise first',
    eyebrow('Security','3 of 5') +
    '<h2 class="demo-h b">Never paste raw<br>customer data.<br>Anonymise first.</h2>'
    '<div class="subline b">What is safe to type into a prompt, and what never is.</div>'
    '<div class="frows">'
    '<div class="frow b"><span class="fe">\U0001F534</span><span class="ft">'
    '<b>The golden rule.</b> Never paste raw personal data: civil ID numbers, account numbers, '
    'balances, salaries, or passwords. Ever.</span></div>'
    '<div class="frow b"><span class="fe">\U0001F3AD</span><span class="ft">'
    '<b>The anonymising technique.</b> Swap real names for placeholders. '
    '"Analyse customer Khalid Al-Sabah\'s payment history" becomes '
    '"Analyse Customer A\'s payment history."</span></div>'
    '<div class="frow b"><span class="fe">\U0001F3F7\uFE0F</span><span class="ft">'
    '<b>Sensitivity labels.</b> If your organization labels files as confidential, '
    'those labels can stop a tool extracting the data at all. Ask whether yours does.</span></div>'
    '</div>'
    '<div class="closebar b">You almost never need the real value. '
    '<b>The shape of the problem is what the tool works on.</b></div>')

add('p3c','Security · Compared to Copilot',
    eyebrow('Security','4 of 5') +
    '<h2 class="demo-h b">Why be more careful<br>than with Copilot?</h2>'
    '<div class="subline b">Not because one is good and one is bad. Because of where each one sits.</div>'
    '<div class="cmp">'
    '<div class="cc b"><div class="ct">Microsoft Copilot</div><div class="cs">Inside your tenant</div>'
    '<div class="cr">Sits <b>inside</b> your company\'s Microsoft environment</div>'
    '<div class="cr">Sees only what <b>your account already has permission</b> to see</div>'
    '<div class="cr">Your IT team already set the boundary, so the guardrail is on by default</div>'
    '<div class="cr">Your files usually <b>never leave</b> the tenant</div></div>'
    '<div class="cc hi b"><div class="ct">A public AI tool</div><div class="cs">Outside your tenant</div>'
    '<div class="cr">Sits <b>outside</b> your organization entirely</div>'
    '<div class="cr">Sees exactly what <b>you</b> paste into it, and nothing else</div>'
    '<div class="cr"><b>You</b> are the boundary. There is no IT team between you and the box.</div>'
    '<div class="cr">Whatever you paste has <b>left the building</b></div></div>'
    '</div>'
    '<div class="ethbar b"><b>The difference that matters:</b> with Copilot the guardrail is '
    'configured for you. With a public tool the guardrail is your own judgment, every single time.</div>')

add('p4','Privacy · Your rule',
  eyebrow('Write it down now') +
  '<h2 class="demo-h b">Your own<br>paste rule.</h2>'
  '<div class="lead b">One line, in your own words, for your own job. '
  'Something you will still remember on a busy Thursday.</div>'
  '<div class="pbox b">My paste rule:\n\nI will never paste ______________________ into an AI tool.\n\n'
  'If I need help with it, I will ______________________ first.</div>'
  '<div class="keyline b">Everything you touch after this slide is <b>your own material.</b> '
  'The rule has to hold before we go any further.</div>')

# ---- use cases by department ----

add('u0','Use cases · Intro',
    eyebrow('Use cases') +
    '<h2 class="demo-h b">Same tool.<br>Different rules<br>per department.</h2>'
    '<div class="lead b">What is a safe productivity boost in one team is a compliance problem in another. '
    'Find yours in the next four slides.</div>'
    '<div class="keyline b">The pattern is always the same: <b>drafting and structuring are safe. '
    'Deciding about a named person is not.</b></div>')

usecase('u1','HR','Human Resources',
  ['Draft job descriptions','Summarize policy manuals','Format interview templates',
   'Turn messy notes into a structured brief'],
  ['Employee performance scores','Salary and bonus data','Medical and sick leave records',
   'Anything naming an individual employee'],
  'Automation bias when filtering CVs. A human reads the shortlist and owns the call.')

usecase('u2','Finance','Finance and procurement',
  ['Explain a variance in plain English','Draft the commentary around a number',
   'Build the formula, then check it yourself','Summarize a supplier contract you already have'],
  ['Live account or card numbers','Unpublished results before they are released',
   'Signed contract terms and pricing','Anything you would not email a supplier'],
  'A confident wrong number looks exactly like a confident right one. Every figure gets recalculated by hand.')

usecase('u3','Ops','Operations and customer service',
  ['Summarize a long ticket thread','Draft a customer reply, then edit it',
   'Spot patterns across anonymised tickets','Write the notice, the poster and the SMS'],
  ['Customer names, numbers and addresses','Complaint records tied to a person',
   'Anything going out without a human reading it first','Promises about dates the data does not support'],
  'Speed makes it tempting to send without reading. Every outgoing message gets a human read.')

usecase('u4','Leadership','Management and leadership',
  ['Turn a report into a briefing','Pressure test your own argument',
   'Prepare for a difficult conversation','Draft the first version of a plan'],
  ['Restructuring or redundancy plans','Individual performance judgments',
   'Confidential board material','Legal advice you would normally pay for'],
  'It is fluent enough to sound like a decision. It is not one. The decision, and the accountability, stay with you.')

# ============================== S1 CONNECTORS, MCP, SKILLS

brk('brk1','Break 1','Section 0 and 1 done.<br><b>Take a break.</b>',
    'Rules set, tools connected. Next we find the one task in your week that is worth all this.',[10,15],
    'Pick a length. The countdown goes full screen and shows the room when to be back.')

# ============================== S2 WORKFLOW AUDIT

question('s1q','S1 · Still pasting','Two days in.<br>Are you still <b>pasting</b>?',sec=True)

add('s1t1','S1 · Connectors and MCP',
  '<div class="bigemoji b">\U0001F50C</div>'
  '<h2 class="demo-h b">Connectors, and MCP</h2>'
  '<div class="defhero b">A <b>connector</b> gives Claude permission to read one of your tools directly. '
  '<b>MCP</b> is the standard that makes those connections work the same way everywhere.</div>'
  '<div class="frows">'
  '<div class="frow b"><span class="fe">\U0001F4C1</span><span class="ft">'
  '<b>No more pasting</b> because Claude opens the thread, the file or the calendar itself</span></div>'
  '<div class="frow b"><span class="fe">\U0001F510</span><span class="ft">'
  '<b>You grant it, and you can remove it</b> because a connector is a permission, not a copy of your data</span></div>'
  '<div class="frow b"><span class="fe">\U0001F9F0</span><span class="ft">'
  '<b>It works across tools</b> because MCP is one standard rather than one integration per app</span></div>'
  '</div>'
  '<div class="closebar b">This is the difference between a clever tab and '
  '<b>something that sits inside your actual work.</b></div>')

add('s1t2','S1 · The honest limits',
  eyebrow('Section 1','1.1') +
  '<h2 class="demo-h b">Read this before<br>you ask IT.</h2>'
  '<div class="vs">'
  '<div class="vcol good b"><div class="vh">What a connector does</div><ul>'
  '<li>Reads what you already have access to</li>'
  '<li>Asks you once, then remembers</li>'
  '<li>Shows you what it touched</li>'
  '<li>Stops the moment you revoke it</li></ul></div>'
  '<div class="vcol bad b"><div class="vh">What it does not do</div><ul>'
  '<li>Give you access you did not already have</li>'
  '<li>Make your data less confidential</li>'
  '<li>Work without your organization allowing it</li>'
  '<li>Replace the paste rule you wrote this morning</li></ul></div>'
  '</div>'
  '<div class="keyline b">Everything from box 2 onward <b>still applies.</b> '
  'A connector changes the plumbing, not the exposure.</div>')

add('s1t3','S1 · Skills, deeper',
  '<div class="bigemoji b">\U0001F9E9</div>'
  '<h2 class="demo-h b">Skills, one level deeper</h2>'
  '<div class="defhero b">Yesterday you built one from a prompt. Today the question is different: '
  '<b>which of your tasks deserves one</b>, and what has to go in it so somebody else can run it.</div>'
  '<div class="frows">'
  '<div class="frow b"><span class="fe">\U0001F501</span><span class="ft">'
  '<b>Three times</b> is the threshold. Done a task three times the same way? It is a Skill.</span></div>'
  '<div class="frow b"><span class="fe">\U0001F4CF</span><span class="ft">'
  '<b>Write the checks in</b> so the output arrives already verified, not just already written</span></div>'
  '<div class="frow b"><span class="fe">\U0001F465</span><span class="ft">'
  '<b>Write it for the next person</b> because a Skill only you can use is just a saved prompt</span></div>'
  '</div>'
  '<div class="closebar b">The test: <b>could a new colleague get your result without asking you a question?</b></div>')

add('lab1','Task 1',
    eyebrow('Task 1&nbsp;&middot;&nbsp;Claude') +
    '<h2 class="demo-h sm b">Connect<br>something real.</h2>'
    + lab(1,'15','One connector, one question that needs it, then revoke it',
          ["Open the connector settings in Claude and read what one actually asks for.", "Turn on a connector you are allowed to use. If your organization blocks them, use the fallback on the lab page.", "Ask a question that <b>only works</b> because of the connection.", "Then <b>revoke it</b>, and ask the same question again."],
          where='In Claude') +
    '<div class="keyline b">Knowing how to turn it off is the part <b>your IT team will ask about.</b></div>')


add('lab2','Task 2',
    eyebrow('Task 2&nbsp;&middot;&nbsp;Assessment&nbsp;&middot;&nbsp;10:30') +
    '<h2 class="demo-h sm b">The same test<br>as Tuesday.</h2>'
    '<div class="testbox b"><div class="tl">Post-program MAP test</div>'
    '<div class="tv">8 minutes, silent</div>'
    '<div class="td">Word for word the test you took on the first morning, before we taught anything. '
    'We take it now, before the capstone, so it measures the teaching and not the afternoon. '
    'Compare the two and you can see exactly how far you moved.</div>'
    + qr_block(MAP_POST) +
    '<a class="tph" id="map-post" href="' + MAP_POST + '" target="_blank" rel="noopener">Open the MAP test &#8599;</a></div>'
    '<div class="keyline b">Submit, close the tab, and wait. <b>The capstone starts at 10:40.</b></div>'
    '<a class="labgo b" href="coded-aiet-day-3-lab.html#t2">Open task 2 &rarr;</a>',
    center=True)


question('cap0','Capstone','Now build something<br>you would actually <b>send.</b>',
         'In pairs. Three hours. Presented at 13:20.', sec=True)

add('cap1','Capstone · How it works',
    eyebrow('Capstone','How it works') +
    '<h2 class="demo-h b">Pairs.<br>One idea each.</h2>'
    + minilist([('Pair up','Two people. Pick somebody who does not do your job.'),
                ('Choose one idea','Seven on the lab page. Read two, pick one, commit.'),
                ('Split the work','For every deliverable one of you <b>builds</b>, the other <b>verifies</b>.'),
                ('Four deliverables','A briefing, the charts, a deck, and a communication pack. In that order.'),
                ('Present at 13:20','Three minutes, then one question from the room.')]) +
    '<div class="keyline b">The verifier is not a formality. '
    '<b>Every number gets checked by the person who did not produce it.</b></div>')



add('cap2','Capstone · The ideas',
    eyebrow('Capstone','Seven ideas') +
    '<h2 class="demo-h b">Pick the one you<br>would actually run.</h2>'
    + minilist([('01 &middot; Operations','The overtime decision. Hire, or keep paying?'),
                ('02 &middot; Human Resources','The retention programme. Where does the budget go?'),
                ('03 &middot; Customer Service','The channel rescue. Which one is failing, and why?'),
                ('04 &middot; Procurement','The supplier consolidation. Fewer suppliers, or not?'),
                ('05 &middot; People','The recognition programme. The weakest score in the company.'),
                ('06 &middot; Finance','The cost control programme. Three measures, each on a line.'),
                ('07 &middot; Your own','Your workflow, your redacted data, signed off first.')]) +
    '<div class="keyline b">Every dataset has <b>deliberate problems in it</b>, exactly like yesterday. '
    'Finding them is part of the work.</div>')



add('cap3','Capstone · Three failures',
    eyebrow('Capstone','Before you start') +
    '<h2 class="demo-h b">The three failures,<br>in order.</h2>'
    + cards([('Failure 1','Trusting the first answer','You asked, it answered, you believed it. Every dataset has a trap that survives one question.'),
             ('Failure 2','Answering a different question','Your idea asks you to decide something. A description of the data is not a decision.'),
             ('Failure 3','No number behind it','"We should improve retention" is not a recommendation. It is a feeling.')]) +
    '<div class="punch b">Your briefing needs <b>a decision, a number, and a risk.</b>'
    '<span class="sm">If any of the three is missing, the room will find it in the questions.</span></div>')



add('lab3','Task 3',
    eyebrow('Phase 0&nbsp;&middot;&nbsp;No tools open') +
    '<h2 class="demo-h sm b">Pick your idea.<br>Split the work.</h2>'
    + lab(3,'10','Ten minutes, in pairs, before anything is opened',
          ["Pair up. Somebody who does not do your job is a better partner.", "Read two ideas on the lab page. Pick one and <b>commit</b>.", "Download your data and open it once, together.", "Agree who <b>builds</b> and who <b>verifies</b> for each of the four deliverables."],
          where='In pairs') +
    '<div class="keyline b">No deliverable starts in this phase. <b>That is the point of it.</b></div>')


add('s4t1','S4 · The briefing',
  eyebrow('Deliverable 1') +
  '<h2 class="demo-h b">One page.<br>Four parts.</h2>'
  + minilist([('The decision','What you are asking them to decide. One sentence, at the top.'),
              ('The evidence','Three numbers maximum, each traceable to a file'),
              ('The recommendation','What you would do, and what it costs or saves'),
              ('The risk','What could make you wrong. Say it before they ask.')]) +
  '<div class="keyline b">The risk section is what separates a briefing from a pitch. '
  '<b>Leaders trust the person who names the weakness first.</b></div>')

add('lab4','Task 4',
    eyebrow('Deliverable 1&nbsp;&middot;&nbsp;In Claude') +
    '<h2 class="demo-h sm b">The executive<br>briefing.</h2>'
    + lab(4,'40','One page a director reads in ninety seconds',
          ["Attach your data to one Claude conversation and keep it for the whole capstone.", "Profile the files first. You know how. Then answer the question your idea asks.", "Write the briefing: the decision, three numbers, the recommendation, the risk.", "The verifier checks <b>every figure</b> against the file before it is finished."],
          where='In Claude') +
    '<div class="keyline b">Ask it to argue against your own conclusion before you write. <b>Every dataset has a trap.</b></div>')


brk('brk2','Break 2','Section 2 done.<br><b>Short break.</b>',
    'You know what to build. The rest of the day is building it.',[10,15],
    'Pick a length. Then we do not stop again until lunch.')

# ============================== S3 CAPSTONE CHARTS

add('cap4','Capstone · Charts',
    eyebrow('Deliverable 2') +
    '<h2 class="demo-h b">Two or three charts.<br>Each one argues.</h2>'
    + minilist([('One claim per chart','If you cannot say it in a sentence, it is decoration'),
                ('The caption states it','Not "Overtime by team". Say what the chart shows you.'),
                ('A source line','Which file, which rows, and what you corrected'),
                ('The counter chart','The one view that argues against you. Address it before the room finds it.')]) +
    '<div class="keyline b">A chart that defends nothing <b>goes in the bin.</b> '
    'The ones that survive go into the deck after lunch.</div>')

add('lab5','Task 5',
    eyebrow('Deliverable 2&nbsp;&middot;&nbsp;In Claude') +
    '<h2 class="demo-h sm b">Charts that<br>argue.</h2>'
    + lab(5,'25','Two or three charts, each defending one claim',
          ["Decide the two or three claims your idea stands on. Each gets exactly one chart.", "Build them. One claim, a caption that states it, and a source line.", "Ask Claude to list <b>the exact rows</b> behind every chart, then spot check two.", "Build the <b>counter chart</b>: the one view that argues against you."],
          where='In Claude') +
    '<div class="keyline b">That citation habit is <b>the single most useful thing you take back to work.</b></div>')


brk('brk3','Lunch','Charts done.<br><b>Lunch and prayer.</b>',
    'After lunch: the deck, with the charts in it. Then the comms pack. Then you present it.',[40,50],
    'Back at the time on screen. Do not lose your working.')

# ============================== S4 THE PACKAGE

add('s4t2','S4 · The deck',
  eyebrow('Deliverable 3') +
  '<h2 class="demo-h b">Six slides.<br>Yesterday\'s method.</h2>'
  '<div class="lead b">Claude Design or Gamma. Your choice, and you already have an opinion about which.</div>'
  + minilist([('Slide 1','The decision, as a headline'),
              ('Slide 2','The situation in three numbers'),
              ('Slide 3','Your first chart, with its claim as the caption'),
              ('Slide 4','Your second chart, the second story that complicates the obvious answer'),
              ('Slide 5','The recommendation and what it costs'),
              ('Slide 6','The risk, and what you would do about it')]) +
  '<div class="keyline b">Every figure traceable. <b>Somebody in this room will check one of them.</b></div>')

add('lab6','Task 6',
    eyebrow('Deliverable 3&nbsp;&middot;&nbsp;Claude or Gamma') +
    '<h2 class="demo-h sm b">The stakeholder<br>deck.</h2>'
    + lab(6,'20','Five or six slides that carry the briefing into a room',
          ["Pick your tool. You earned an opinion on this yesterday. Gamma users: paste the briefing text first, it cannot see your conversation.", "Five or six slides: the decision, the situation, <b>your charts on slides 3 and 4</b>, the recommendation, the risk.", "Every headline eight words or fewer. Every figure carries its source.", "Verifier checks two slides against the data before you move on."],
          where='Claude or Gamma') +
    '<div class="keyline b">The deck tells the <b>same story</b> as the briefing. If it does not, one of them is wrong.</div>')


add('cap5','Capstone · Comms pack',
    eyebrow('Deliverable 4') +
    '<h2 class="demo-h b">It is decided.<br>Now it has to land.</h2>'
    '<div class="lead b">Pick two that fit your audience, then bank three reusable templates.</div>'
    + minilist([('An internal email','To the staff the change lands on'),
                ('A public FAQ','For the customers or the tenants who will ask'),
                ('A one page fact sheet','For the manager who has to explain it in a meeting'),
                ('Three templates','So the next person reruns this without you in the room')]) +
    '<div class="keyline b">Every fact in the comms pack has to agree with the briefing. '
    '<b>Your verifier checks that, not you.</b></div>')



add('lab7','Task 7',
    eyebrow('Deliverable 4&nbsp;&middot;&nbsp;In Claude') +
    '<h2 class="demo-h sm b">The comms<br>pack.</h2>'
    + lab(7,'15','Two communication items, plus three reusable templates',
          ["Pick two: an internal email, a public FAQ, or a one page fact sheet.", "Draft them from the briefing, so every fact already agrees.", "Write three <b>reusable prompt templates</b> with placeholders.", "Verifier checks the comms against the briefing, line by line."],
          where='In Claude') +
    '<div class="keyline b">The templates are the part that <b>outlives today.</b></div>')


add('s5t1','Present · How this works',
    eyebrow('13:20') +
    '<h2 class="demo-h b">Three minutes.<br>Then one question.</h2>'
    + minilist([('Three minutes','Both of you speak. Split it however you like.'),
                ('The decision first','Not the background, not the method, not an apology.'),
                ('One question','From the room. Expect somebody to check a number.'),
                ('"How do you know?"','That is the question. Have the file open when it comes.')]) +
    '<div class="keyline b">The instructor scores nothing. '
    '<b>You are rehearsing the meeting, not sitting an exam.</b></div>')



add('lab8','Task 8',
    eyebrow('Present&nbsp;&middot;&nbsp;In the room') +
    '<h2 class="demo-h sm b">Assemble,<br>then present.</h2>'
    + lab(8,'30','Three minutes per pair, then one question',
          ["Assemble one package: briefing, then deck with charts in, then comms.", "Run the pitch once out loud. Cut whatever does not earn its place.", "Present. Decision first. Both of you speak.", "When the question comes, <b>show where the number came from.</b>"],
          where='In the room') +
    '<div class="keyline b">Prepare the ninety second version too. <b>Schedules slip.</b></div>')


add('a3','Survey',
  eyebrow('13:50') +
  '<h2 class="demo-h b">Tell us what<br>to fix.</h2>'
  '<div class="testbox b"><div class="tl">End of program survey</div>'
  '<div class="tv">5 minutes</div>'
  '<div class="td">What worked, what did not, and what you will actually use on Sunday. '
  'Please be blunt. The polite answers do not help us build the next one.</div>'
  '<a class="tph" id="survey" href="https://portal.joincoded.com/sv/ai-essentials-in-the-workplace-end-of-programme-survey" target="_blank" rel="noopener">Open the survey &#8599;</a></div>',
  center=True)

add('lab9','Task 9',
    eyebrow('Before you leave&nbsp;&middot;&nbsp;13:50') +
    '<h2 class="demo-h sm b">Survey,<br>then certificates.</h2>'
    + lab(9,'10','Two things, in this order',
          ["<b>13:50</b> End of program survey. Five minutes. Please be blunt.", "<b>13:55</b> Certificates and a photograph."],
          where='Assessment') +
    '<div class="keyline b">All three day pages <b>stay online</b> after today.</div>')


add('c1','Close · Three days',
  eyebrow('Three days') +
  '<h2 class="demo-h b">Where you started.</h2>'
  '<div class="road one">'
  '<div class="ritem b"><div class="rn">Tue</div><div><div class="rt">You named a task you dreaded</div>'
  '<div class="rd">Then wrote a prompt that got something useful back.</div></div></div>'
  '<div class="ritem b"><div class="rn">Wed</div><div><div class="rt">You built a deck and checked a number</div>'
  '<div class="rd">And found out one file can give you three different answers.</div></div></div>'
  '<div class="ritem b"><div class="rn">Thu</div><div><div class="rt">You presented a real recommendation</div>'
  '<div class="rd">With the evidence behind it and the risk named out loud.</div></div></div>'
  '</div>'
  '<div class="keyline b">Three days ago most of this room had never written a prompt on purpose.</div>')

add('c2','Close · Monday',
  eyebrow('What happens Monday') +
  '<h2 class="close-punch b">Pick <b>one</b> thing.<br>Do it for a month.</h2>'
  '<div class="lead b" style="margin-top:30px">Not the whole library. Not every workflow. '
  'One task, the one you audited this morning, done the new way every week until it is automatic.</div>'
  '<div class="keyline b">People who try to change ten things change nothing. '
  '<b>People who change one thing keep it.</b></div>')

add('c3','Close · The rule',
  '<h2 class="close-punch b">Your name still goes<br>on the <b>output.</b></h2>'
  '<div class="lead b" style="margin-top:32px">It was true on Tuesday morning and it is true now. '
  'Everything you learned this week makes you faster. None of it makes you less responsible.</div>',
  center=True)

add('close','End',
  '<div class="clock b"><span class="live-dot"></span>End of programme</div>'
  '<h1 class="mega b">Thank you.</h1>'
  '<div class="covsub b">Certificates, then a photograph. Go and use it.</div>',
  center=True)

html = page('Day 3 &middot; Claude Features and Capstone &middot; CODED', ''.join(S),
            back_href='coded-aiet-day-3.html')
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site', 'coded-aiet-day-3-deck.html')
open(out,'w').write(html)
print('slides:', len(S), 'bytes:', len(html), 'em:', html.count('—'))
