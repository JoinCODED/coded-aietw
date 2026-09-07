# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_shell import page, slide

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
  '<div class="ritem b"><div class="rn">02</div><div><div class="rt">A stakeholder deck</div>'
  '<div class="rd">Six slides with charts, built the way you learned yesterday.</div></div></div>'
  '<div class="ritem b"><div class="rn">03</div><div><div class="rt">Reusable prompt templates</div>'
  '<div class="rd">So the next person can run it without you in the room.</div></div></div>'
  '<div class="ritem b"><div class="rn">04</div><div><div class="rt">Five minutes in front of the room</div>'
  '<div class="rd">Three to present, two to defend it.</div></div></div>'
  '</div>')

# ---- privacy and data security, restored from the parked Day 1 block ----
question('p0','Privacy · Where it goes','Where does what you<br><b>paste</b> actually go?',
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

add('p4','Privacy · Your rule',
  eyebrow('Write it down now') +
  '<h2 class="demo-h b">Your own<br>paste rule.</h2>'
  '<div class="lead b">One line, in your own words, for your own job. '
  'Something you will still remember on a busy Thursday.</div>'
  '<div class="pbox b">My paste rule:\n\nI will never paste ______________________ into an AI tool.\n\n'
  'If I need help with it, I will ______________________ first.</div>'
  '<div class="keyline b">Everything you touch after this slide is <b>your own material.</b> '
  'The rule has to hold before we go any further.</div>')

# ============================== S1 CONNECTORS, MCP, SKILLS
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
  '<li>Replace the paste rule you wrote at 09:20</li></ul></div>'
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
  eyebrow('Task 1','Claude') +
  '<h2 class="demo-h sm b">Connect<br>something real.</h2>'
  + lab(1,'18','One connector, one question that needs it, then revoke it',
        ['Open the connector settings in Claude and read what one actually asks for.',
         'Turn on a connector you are allowed to use. If your organization blocks all of them, use the fallback on the lab page.',
         'Ask a question that <b>only works</b> because of the connection.',
         'Then <b>revoke it</b>, and ask the same question again. Watch what changes.']) +
  '<div class="keyline b">Knowing how to turn it off is the part <b>your IT team will ask about.</b></div>')

brk('brk1','Break 1','Section 0 and 1 done.<br><b>Take a break.</b>',
    'Rules set, tools connected. Next we find the one task in your week that is worth all this.',[10,15],
    'Pick a length. The countdown goes full screen and shows the room when to be back.')

# ============================== S2 WORKFLOW AUDIT
question('s2q','S2 · The task','What is the task you do<br><b>every single week</b><br>that you resent?',sec=True)

add('s2t1','S2 · Map it honestly',
  eyebrow('Section 2','2.1') +
  '<h2 class="demo-h b">Map it, with<br>minutes attached.</h2>'
  '<div class="lead b">Every step. Including the ones nobody counts.</div>'
  + minilist([('Counted','Writing it, formatting it, sending it'),
              ('Never counted','Finding the file. Again.'),
              ('Never counted','Chasing the person who owes you the input'),
              ('Never counted','Waiting for approval, then re-reading it to remember where you were'),
              ('Never counted','Doing it twice because the first version went to the wrong reader')]) +
  '<div class="keyline b">The uncounted steps are usually <b>more than half the time.</b> '
  'They are also where the frustration lives.</div>')

add('s2t2','S2 · The split',
  eyebrow('Section 2','2.2') +
  '<h2 class="demo-h b">Two letters<br>per step.</h2>'
  '<div class="spread-row two">'
  '<div class="sc b"><div class="sw">Mark it P</div><div class="st">Pattern</div>'
  '<div class="sd">Repetitive, rules based, the same shape every time. '
  '<b>Summarizing, reformatting, drafting, sorting, first-pass checking.</b> '
  'This is where AI helps.</div></div>'
  '<div class="sc b"><div class="sw">Mark it J</div><div class="st">Judgment</div>'
  '<div class="sd">Deciding, negotiating, taking responsibility, knowing your business. '
  '<b>Choosing what matters, and being accountable for it.</b> This stays yours.</div></div>'
  '</div>'
  '<div class="punch b">Automate the <b>P</b> steps. Protect the <b>J</b> steps.'
  '<span class="sm">A task that is all J is not an opportunity. It is your job.</span></div>')

add('s2t3','S2 · The honest rule',
  eyebrow('Section 2','2.3') +
  '<h2 class="close-punch b">Automate the step<br>you would <b>still check.</b></h2>'
  '<div class="lead b" style="margin-top:30px">Two days ago you learned this thing invents facts. '
  'Yesterday you learned it cannot always add up. Nothing about today changes either.</div>'
  '<div class="keyline b">If you would not check the output, <b>do not automate that step.</b> '
  'You have just built a machine for producing confident mistakes at speed.</div>')

add('lab2','Task 2',
  eyebrow('Task 2','Paper first, then Claude') +
  '<h2 class="demo-h sm b">The workflow<br>audit.</h2>'
  + lab(2,'22','One real task, every step, minutes attached',
        ['Pick the task you named at 10:20. It has to be real and weekly.',
         'List every step with the minutes it takes. Include the uncounted ones.',
         'Mark each step <b>P</b> or <b>J</b>.',
         'Multiply your total by how often you do it. Say the yearly number out loud.',
         'Pick <b>one</b> P step. Not five. The one that costs the most and you would still check.'],
        where='Paper first, then Claude') +
  '<div class="keyline b">Ninety minutes, twice a month, is <b>thirty-six hours a year</b> on one task.</div>')

brk('brk2','Break 2','Section 2 done.<br><b>Short break.</b>',
    'You know what to build. The rest of the day is building it.',[10,15],
    'Pick a length. Then we do not stop again until lunch.')

# ============================== S3 CAPSTONE ANALYSIS
question('s3q','S3 · Capstone','Now build something<br>you would actually <b>send.</b>',
         'Four hours. Alone. Presented at 13:20.',sec=True)

add('s3t1','S3 · The five scenarios',
  eyebrow('Section 3','3.1') +
  '<h2 class="demo-h b">Pick one.</h2>'
  + minilist([('A &middot; Operations','Hire, or keep paying overtime? Nine months of overtime against hiring costs.'),
              ('B &middot; Human Resources','Where does the retention budget go? Eighteen months of leavers.'),
              ('C &middot; Customer Service','Which channel is failing? Six months of tickets against staffing.'),
              ('D &middot; Procurement','Consolidate, or not? A year of purchase orders across five categories.'),
              ('E &middot; Your own work','Your data, redacted. Four questions to answer first.')]) +
  '<div class="keyline b">Every file has <b>deliberate problems in it</b>, exactly like yesterday. '
  'Finding them is part of the work, not a distraction from it.</div>')

add('s3t2','S3 · What good looks like',
  eyebrow('Section 3','3.2') +
  '<h2 class="demo-h b">The three failures,<br>in order.</h2>'
  + cards([('Failure 1','Trusting the first answer','You asked, it answered, you believed it. Every scenario has a trap that survives one question.'),
           ('Failure 2','Answering a different question','The scenario asks you to decide something. A description of the data is not a decision.'),
           ('Failure 3','No number behind the recommendation','"We should improve retention" is not a recommendation. It is a feeling.')]) +
  '<div class="punch b">Your briefing needs <b>a decision, a number, and a risk.</b>'
  '<span class="sm">If any of the three is missing, the room will find it in the questions.</span></div>')

add('lab3','Task 3',
  eyebrow('Task 3','In Claude') +
  '<h2 class="demo-h sm b">Interrogate<br>the data.</h2>'
  + lab(3,'40','Profile it, analyse it, then find the trap',
        ['Pick your scenario and download both files.',
         'Profile them first. Duplicates, blanks, impossible values, spelling variants. You know this.',
         'Answer the actual question the scenario asks. With numbers.',
         'Then look for <b>the second story</b>. Every scenario has one that contradicts the obvious answer.',
         'Build the charts while you are here. You need them at 12:50.']) +
  '<div class="keyline b">Ask it to show its working on every calculation. '
  '<b>You will be asked to defend these numbers at 13:20.</b></div>')

brk('brk3','Lunch','Analysis done.<br><b>Lunch and prayer.</b>',
    'After lunch you turn it into a package. Briefing, deck, templates, then you present it.',[40,50],
    'Back at the time on screen. Do not lose your working.')

# ============================== S4 THE PACKAGE
add('s4t1','S4 · The briefing',
  eyebrow('Section 4','4.1') +
  '<h2 class="demo-h b">One page.<br>Four parts.</h2>'
  + minilist([('The decision','What you are asking them to decide. One sentence, at the top.'),
              ('The evidence','Three numbers maximum, each traceable to a file'),
              ('The recommendation','What you would do, and what it costs or saves'),
              ('The risk','What could make you wrong. Say it before they ask.')]) +
  '<div class="keyline b">The risk section is what separates a briefing from a pitch. '
  '<b>Leaders trust the person who names the weakness first.</b></div>')

add('s4t2','S4 · The deck',
  eyebrow('Section 4','4.2') +
  '<h2 class="demo-h b">Six slides.<br>Yesterday\'s method.</h2>'
  '<div class="lead b">Claude Design or Gamma. Your choice, and you already have an opinion about which.</div>'
  + minilist([('Slide 1','The decision, as a headline'),
              ('Slide 2','The situation in three numbers'),
              ('Slide 3','Your chart, with the claim in the caption'),
              ('Slide 4','What is really going on, the second story'),
              ('Slide 5','The recommendation and what it costs'),
              ('Slide 6','The risk, and what you would do about it')]) +
  '<div class="keyline b">Every figure traceable. <b>Somebody in this room will check one of them.</b></div>')

add('lab4','Task 4',
  eyebrow('Task 4','Claude or Gamma') +
  '<h2 class="demo-h sm b">The package.</h2>'
  + lab(4,'30','Briefing, deck, and the templates that make it repeatable',
        ['Write the one page briefing. Decision, evidence, recommendation, risk.',
         'Build the six slide deck from it, with your charts.',
         'Write the <b>reusable prompt templates</b> so somebody else could run this next quarter.',
         'Read the briefing out loud once. If you stumble, so will the room.'],
        where='Claude or Gamma') +
  '<div class="keyline b">The templates are the part that outlives today. '
  '<b>Write them for the next person, not for you.</b></div>')

# ============================== S5 PRESENT
add('s5t1','S5 · How this works',
  eyebrow('Section 5','13:20') +
  '<h2 class="demo-h b">Threes.<br>Five minutes each.</h2>'
  + minilist([('Three minutes','You present. The decision first, not last.'),
              ('Two minutes','They ask. Expect them to check a number.'),
              ('The card','Six lines. Your peers score it, and I score nothing.'),
              ('At 13:35','The three highest present to the whole room.')]) +
  '<div class="keyline b">Everybody presents. <b>Nobody presents to me.</b> '
  'You are practising the meeting, not the assessment.</div>')

add('lab5','Task 5',
  eyebrow('Task 5','In the room') +
  '<h2 class="demo-h sm b">Present it.</h2>'
  + lab(5,'15','Three to present, two to defend',
        ['Find your trio. You have three minutes each.',
         'Lead with the decision. Not the background, not the method.',
         'When they question a number, <b>show where it came from</b>.',
         'Score each other on the six line card. Be honest, it is the only feedback that helps.'],
        where='In the room') +
  '<div class="keyline b">The best question you will get today is the one you cannot answer. '
  '<b>Write it down.</b></div>')

# ============================== ASSESSMENT AND CLOSE
add('a1','Practice quiz',
  eyebrow('13:35') +
  '<h2 class="demo-h b">Practice quiz.</h2>'
  '<div class="lead b">Twelve questions across all three days. Instant feedback, and it tells you '
  'which topic to look at again. It is not scored by anyone but you.</div>'
  '<div class="testbox b"><div class="tl">Practice quiz</div>'
  '<div class="tv">10 minutes</div>'
  '<div class="td">A warm up for the test that follows. Lean on it. '
  'Getting one wrong here is cheaper than getting it wrong at your desk.</div>'
  '<a class="tph" href="coded-aiet-quiz.html">Open the quiz &rarr;</a></div>',
  center=True)

add('a2','Post MAP test',
  eyebrow('13:45') +
  '<h2 class="demo-h b">The same test<br>as Tuesday.</h2>'
  '<div class="testbox b"><div class="tl">Post-program MAP test</div>'
  '<div class="tv">8 minutes, silent</div>'
  '<div class="td">Word for word the test you took on the first morning, before we taught anything. '
  'Compare the two and you can see exactly how far you moved.</div>'
  '<span class="tph" id="map-post" data-placeholder="true">Link to be added</span></div>',
  center=True)

add('a3','Survey',
  eyebrow('13:52') +
  '<h2 class="demo-h b">Tell us what<br>to fix.</h2>'
  '<div class="testbox b"><div class="tl">End of program survey</div>'
  '<div class="tv">5 minutes</div>'
  '<div class="td">What worked, what did not, and what you will actually use on Sunday. '
  'Please be blunt. The polite answers do not help us build the next one.</div>'
  '<span class="tph" id="survey" data-placeholder="true">Link to be added</span></div>',
  center=True)

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
