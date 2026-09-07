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
def mc(q,opts,fb):
    return ('<div class="mc b"><div class="mc-q">'+q+'</div><div class="mc-opts">'
      +''.join('<button class="mc-opt" data-k="%s" data-fb="%s"><span class="mo-k">%s</span><span>%s</span></button>'
               %('1' if c else '0', fb, l, t) for l,t,c in opts)
      +'</div><div class="mc-fb"></div></div>')
def lab(num,mins,title,steps,where="In Claude"):
    out=('<div class="labcard b"><div class="lh"><span class="lnum">Task '+str(num)+'</span>'
         '<span class="ltime">'+mins+' minutes</span><span class="lwhere">'+where+'</span></div>'
         '<div class="lt">'+title+'</div><ol class="labsteps">')
    for st in steps: out+='<li>'+st+'</li>'
    return out+('</ol><a class="labgo" href="coded-aiet-day-2-lab.html#t'+str(num)+'">'
                'Open task '+str(num)+' &rarr;</a></div>')
def brk(bid,title,head,sub,opts,note):
    o=''.join('<button class="brk-opt%s" data-min="%d"><span class="bn">%d</span><span class="bu">minutes</span></button>'
              %((' alt' if i else ''),m,m) for i,m in enumerate(opts))
    add(bid,title,eyebrow('Break')+'<h2 class="brk-h b">'+head+'</h2>'
        '<div class="brk-sub b">'+sub+'</div><div class="brk-pick b">'+o+'</div>'
        '<div class="brk-note b">'+note+'</div>', center=True)

# ============================== OPEN
add('cover','Title',
  '<div class="clock b"><span class="live-dot"></span>Day 2 &middot; Wednesday 9 September 2026 &middot; 09:00 to 14:00</div>'
  '<h1 class="mega b">Presentations<br>and <span class="accent">data</span></h1>'
  '<div class="covsub b">Yesterday you learned to ask. Today you learn to build, and to check.</div>'
  '<div class="covmeta b"><span>CODED Campus, Kuwait</span><span>Claude Design &middot; Gamma &middot; Excel</span><span>Day 2 of 3</span></div>',
  center=True)

add('yesterday','Yesterday',
  eyebrow('Yesterday, in one line') +
  '<h2 class="close-punch b">You are<br>the <b>variable</b>.</h2>'
  '<div class="lead b" style="margin-top:30px">Six parts in a prompt. Show rather than describe. '
  'Give it the source, then check the summary back against the source.</div>'
  '<div class="keyline b">All of that still applies today. <b>The output just gets bigger, '
  'and the mistakes get more expensive.</b></div>')

add('outcomes','Outcomes',
  eyebrow('Today') +
  '<h2 class="demo-h b">Three things you<br>leave with.</h2>'
  '<div class="road one">'
  '<div class="ritem b"><div class="rn">01</div><div><div class="rt">A deck you did not format</div>'
  '<div class="rd">Built twice, in two tools, from one prompt.</div></div></div>'
  '<div class="ritem b"><div class="rn">02</div><div><div class="rt">Charts you can defend</div>'
  '<div class="rd">From data you cleaned yourself, with every number checked.</div></div></div>'
  '<div class="ritem b"><div class="rn">03</div><div><div class="rt">A prompt library and one Skill</div>'
  '<div class="rd">So you stop typing the same instruction twice.</div></div></div>'
  '</div>')

# ============================== S1 REPORT TO DECK
question('s1q','S1 · How long','How long does a deck<br>actually take you?','Split it: thinking, writing, formatting.',sec=True)

add('s1t1','S1 · Where the time goes',
  eyebrow('Section 1','1.1') +
  '<h2 class="demo-h b">Where the hours<br>actually go.</h2>'
  + cards([('Part 1','Deciding what to say','The genuinely hard part. Nobody can do this for you.'),
           ('Part 2','Writing it down','Quick, once you know what you are saying.'),
           ('Part 3','Making it look like a deck','Hours. Every time. For nothing anybody remembers.')]) +
  '<div class="punch b">AI is very good at <b>part three</b> and useful on part two.'
  '<span class="sm">It has almost nothing to offer on part one, which is the part that matters.</span></div>')

add('s1t2','S1 · Claude Design',
  '<div class="bigemoji b">\U0001F5A5️</div>'
  '<h2 class="demo-h b">What Claude Design is</h2>'
  '<div class="defhero b">You describe the deck you want. It builds the slides, the layout and the '
  'structure, <b>inside the same conversation that already has your document in it</b>.</div>'
  '<div class="frows">'
  '<div class="frow b"><span class="fe">\U0001F4CE</span><span class="ft">'
  '<b>It already has your context</b> because you attached the report earlier in the chat</span></div>'
  '<div class="frow b"><span class="fe">✏️</span><span class="ft">'
  '<b>You can change one slide</b> by asking, rather than rebuilding the whole thing</span></div>'
  '<div class="frow b"><span class="fe">\U0001F4CA</span><span class="ft">'
  '<b>It can carry the analysis through</b> from the same data you gave it</span></div>'
  '</div>'
  '<div class="closebar b">It is not a design tool. <b>It is a writing tool that outputs slides.</b></div>')

add('s1t3','S1 · The deck brief',
  eyebrow('Section 1','1.2') +
  '<h2 class="demo-h b">A deck is a document<br>with a shape.</h2>'
  '<div class="lead b">The shape is the prompt. Six things, and it is the same six as yesterday.</div>'
  + minilist([('Audience','Who is in the room, and how long they have'),
              ('Slide count','Say a number. Otherwise you get twelve.'),
              ('The spine','Name every slide. This is the part people skip.'),
              ('The numbers rule','Where figures may come from, and what to do when one is missing'),
              ('Tone','Direct, or diplomatic. They produce very different decks.'),
              ('The ask','What you want the room to do when it ends')]) +
  '<div class="keyline b">Name the six slides yourself. <b>If you cannot, the deck is not ready to build.</b></div>')

add('s1t4','S1 · The warning',
  eyebrow('Before you build anything') +
  '<h2 class="close-punch b">A deck that looks right<br>and <b>misquotes one number</b><br>is worse than no deck.</h2>'
  '<div class="lead b" style="margin-top:30px">A rough draft gets questioned. A polished slide gets believed. '
  'The better it looks, the less anyone checks it.</div>'
  '<div class="keyline b">Today\'s source is <b>yesterday\'s report</b>, and it still has five faults in it. '
  'That is on purpose.</div>')

add('lab1','Task 1',
  eyebrow('Task 1','Claude Design') +
  '<h2 class="demo-h sm b">Report to deck.</h2>'
  + lab(1,'20','Six slides from the report you already know is dirty',
        ['Attach yesterday\'s operations report to a new Claude conversation.',
         'Write your own six part prompt, then ask Claude to design it.',
         'Open two slides and <b>check every figure against the source</b>.',
         'Fix one slide by hand, so you feel where Claude stops and you start.'],
        where='Claude Design') +
  '<div class="keyline b">Boss tier: ask it to fact check the report against itself <b>before</b> it builds. '
  'How many of the five does it catch?</div>')

brk('brk1','Break 1','Section 1 done.<br><b>Take a break.</b>',
    'One deck built. Next we build the same thing somewhere else and compare.',[10,15],
    'Pick a length. The countdown goes full screen and shows the room when to be back.')

# ============================== S2 GAMMA
question('s2q','S2 · Tool or prompt','Are you learning a <b>tool</b>,<br>or learning a <b>prompt</b>?',sec=True)

add('s2t1','S2 · Gamma',
  eyebrow('Section 2','2.1') +
  '<h2 class="demo-h b">Gamma, in one line.</h2>'
  '<div class="defhero b">A presentation tool that generates the whole deck from a prompt, '
  'then lets you edit it like a web page. <b>Design first, where Claude is writing first.</b></div>'
  '<div class="vs">'
  '<div class="vcol good b"><div class="vh">Gamma is stronger at</div><ul>'
  '<li>Looking finished on the first try</li><li>Themes, images and layout variety</li>'
  '<li>Sharing as a link people can scroll</li><li>Speed from nothing to something</li></ul></div>'
  '<div class="vcol bad b" style="border-top-color:var(--soft)"><div class="vh" style="color:var(--soft)">Claude Design is stronger at</div><ul style="list-style:none">'
  '<li>Keeping your document in context</li><li>Getting the words right</li>'
  '<li>Carrying analysis through from data</li><li>Changing one slide without a rebuild</li></ul></div>'
  '</div>')

add('s2t2','S2 · Which one',
  eyebrow('Section 2','2.1') +
  '<h2 class="demo-h sm b">Your turn.</h2>'
  + mc('You have a 40 page report and you need six slides where every figure is traceable back to it. '
       'Where do you start?',
       [('A','Gamma, then fix the numbers afterwards',False),
        ('B','Claude with the report attached, then design it there',True),
        ('C','PowerPoint, by hand, like always',False),
        ('D','Either one. It makes no difference.',False)],
       'The document has to be in the room. Gamma generates from a prompt, not from your attached report, '
       'so every figure would be invented or copied by you. Start where the source is.'))

add('s2t3','S2 · The export test',
  eyebrow('Section 2','2.2') +
  '<h2 class="demo-h b">The export test.</h2>'
  '<div class="lead b">Somebody will ask you for the PowerPoint. They always do. '
  'So the real question is not how it looks in the tool.</div>'
  + minilist([('What usually survives','The words, the order, the basic layout'),
              ('What usually shifts','Spacing, font substitution, anything overlapping'),
              ('What usually breaks','Charts, custom graphics, and anything clever'),
              ('What to do','Export once, early, before you have built twelve slides on a broken pattern')]) +
  '<div class="keyline b">Run the export test <b>in task 2</b>, not the night before the meeting.</div>')

add('lab2','Task 2',
  eyebrow('Task 2','Gamma') +
  '<h2 class="demo-h sm b">Same prompt,<br>different tool.</h2>'
  + lab(2,'15','One prompt, two decks, one honest opinion',
        ['Copy the prompt from task 1. <b>The exact same one</b>, not an improved version.',
         'Generate it in Gamma and pick a theme.',
         'Put the two decks side by side and answer the four questions.',
         'Export the Gamma deck to PowerPoint and see what shifts.'],
        where='Gamma') +
  '<div class="keyline b">You need a Gamma account. <b>Free tier is enough.</b> '
  'Sign up now if you have not already.</div>')

add('s2close','S2 · The honest claim',
  eyebrow('Say this out loud') +
  '<h2 class="close-punch b">It is not better than what<br>you would have written.<br>It is <b>faster than what you<br>would have formatted.</b></h2>'
  '<div class="lead b" style="margin-top:30px">Those are two completely different claims. '
  'Only one of them is true, and it is still worth a lot.</div>')

brk('brk2','Break 2','Section 2 done.<br><b>Take a break.</b>',
    'Two decks, one prompt. After the break we stop making things look good and start checking whether they are true.',[10,15],
    'Pick a length. The countdown goes full screen and shows the room when to be back.')

# ============================== S3 DATA
question('s3q','S3 · Same question','Everyone ask the same file<br>the <b>same question</b>.',
         'We will compare answers in four minutes.',sec=True)

add('s3t1','S3 · Calculates or predicts',
  eyebrow('Section 3','3.1') +
  '<h2 class="demo-h b">Sometimes it calculates.<br>Sometimes it predicts.</h2>'
  '<div class="defhero b">When it writes and runs code on your file, it <b>calculates</b>. '
  'When it answers from the shape of the numbers, it <b>predicts</b>. '
  'You cannot tell which from looking at the answer.</div>'
  '<div class="keyline b">This is yesterday\'s prediction slide, arriving with a budget attached. '
  '<b>Ask it to show its working, every time.</b></div>')

add('s3t2','S3 · Profile first',
  eyebrow('Section 3','3.2') +
  '<h2 class="demo-h b">Ask what is <span class="hl">wrong</span><br>before what it says.</h2>'
  '<div class="lead b">Every real export is dirty. Nobody tells you which parts.</div>'
  + minilist([('Duplicates','The same response counted twice'),
              ('Blanks','Which some tools drop and some read as zero'),
              ('Impossible values','A 7 on a scale that stops at 5'),
              ('Spelling variants','One department, four names, four fake departments'),
              ('The re-identifier','A comment that names the person who wrote it')]) +
  '<div class="keyline b">The profiling prompt takes twenty seconds. '
  '<b>Skipping it costs you the whole analysis.</b></div>')

add('lab3','Task 3',
  eyebrow('Task 3','In Claude') +
  '<h2 class="demo-h sm b">Clean it before<br>you trust it.</h2>'
  + lab(3,'20','161 survey responses, and not one of them checked',
        ['Upload the survey file to Claude.',
         'Step one: profile it. What is wrong with the file, with row numbers.',
         'Step two: the company average, <b>raw and cleaned</b>, with the count behind each.',
         'Verify the counts yourself before you believe them.']) +
  '<div class="keyline b">The headline barely moves when you clean it. '
  '<b>Everything underneath it does.</b> That is the lesson.</div>')

add('s3t3','S3 · The small sample trap',
  eyebrow('Section 3','3.3') +
  '<h2 class="close-punch b">The smallest sample<br>always looks like<br>the <b>best result.</b></h2>'
  '<div class="lead b" style="margin-top:30px">Three people who happen to be content will out-score '
  'forty people who are doing fine. The ranking will put them first and say nothing about why.</div>'
  '<div class="keyline b">Put the sample size next to every average. '
  '<b>Then the trap cannot survive one glance.</b></div>')

add('lab4','Task 4',
  eyebrow('Task 4','In Claude') +
  '<h2 class="demo-h sm b">The answer<br>and the trap.</h2>'
  + lab(4,'18','Which team is struggling, on what, and what you would do',
        ['Stay in the same conversation. The cleaned data is already there.',
         'Rank the departments and rank the six questions.',
         'Insist on <b>the number of responses next to every average</b>.',
         'Then ask it which result it would not report to leadership, and why.']) +
  '<div class="keyline b">Boss tier: find a statement about this data that is '
  '<b>completely true and completely misleading.</b></div>')

brk('brk3','Lunch','Section 3 done.<br><b>Lunch and prayer.</b>',
    'After lunch: the same file, but now somebody is going to disagree with your number.',[45,60],
    'Back at the time on screen. Bring your laptop.')

# ============================== S4 VALIDATION
question('s4q','S4 · Over budget','How far over budget<br><b>are we</b>?',
         'It sounds like a question with one answer.',sec=True)

add('s4t1','S4 · Four checks',
  eyebrow('Section 4','4.1') +
  '<h2 class="demo-h b">Four checks,<br>in this order.</h2>'
  + minilist([('Recount','Does the detail add up to the total? Do it yourself once.'),
              ('Recompute','Is the percentage on the right base? Budget, not actual.'),
              ('Re-source','Where did this figure come from? Name the cell.'),
              ('Re-read','Does the sentence claim more than the number supports?')]) +
  '<div class="keyline b">Four checks, about six minutes. '
  '<b>Cheaper than one correction email to a board.</b></div>')

add('lab5','Task 5',
  eyebrow('Task 5','In Claude') +
  '<h2 class="demo-h sm b">Three answers<br>to one question.</h2>'
  + lab(5,'18','One budget file, three defensible totals',
        ['Upload the workbook. Read the Summary sheet first, then the detail.',
         'Ask whether the detail agrees with the Summary. It does not.',
         'Audit the detail: text stored as numbers, duplicates, a sign the wrong way, a wrong base.',
         'Produce <b>one number you would put your name on</b>, and say which corrections got you there.']) +
  '<div class="keyline b">Nobody finds all five in eighteen minutes. '
  '<b>Three is a strong result.</b></div>')

add('s4t2','S4 · The formula',
  eyebrow('Section 4','4.2') +
  '<h2 class="close-punch b">Ask for the <b>formula</b>,<br>not the answer.</h2>'
  '<div class="lead b" style="margin-top:30px">A number you cannot reproduce is a rumour. '
  'A formula sitting in the real spreadsheet is a result.</div>'
  '<div class="keyline b">Your finance team will accept a formula. '
  '<b>They will not accept "the AI said".</b></div>')

add('s4t3','S4 · The chart rule',
  eyebrow('Section 4','4.3') +
  '<h2 class="demo-h b">A chart makes<br>one claim.</h2>'
  + minilist([('One claim','If you cannot say it in a sentence, it is decoration'),
              ('The caption states it','Not "Spend by department". Say what the chart shows you.'),
              ('A source line','Which sheet, and what you corrected'),
              ('Nothing else','No second axis, no gradient, no logo on every slide')]) +
  '<div class="keyline b">If the chart has no claim, <b>delete the chart.</b> '
  'The room will thank you for the time back.</div>')

add('lab6','Task 6',
  eyebrow('Task 6','Claude and Excel') +
  '<h2 class="demo-h sm b">The formula<br>and the chart.</h2>'
  + lab(6,'15','Two habits that survive contact with finance',
        ['Step one: ask for the <b>Excel formula</b>, not the number. Paste it into the real sheet.',
         'Does it return the number you had? If not, find out which one was right.',
         'Step two: two charts from the corrected figures. One claim each.',
         'Add them to the deck you built this morning.'],
        where='Claude and Excel') +
  '<div class="keyline b">Notice whether the deck\'s story changed <b>once the numbers were corrected.</b></div>')

brk('brk4','Break 4','Section 4 done.<br><b>Short break.</b>',
    'Last stretch. Twenty minutes on the thing that makes all of today repeatable.',[10,15],
    'Pick a length. The countdown goes full screen and shows the room when to be back.')

# ============================== S5 PROMPT LIBRARY
add('s5cb','S5 · Callback',
  eyebrow('Count them') +
  '<h2 class="demo-h b">How many times today<br>did you retype<br>the same instruction?</h2>'
  '<div class="lead b">The six part prompt. The profiling prompt. "Show your working." '
  '"Put the sample size next to it."</div>'
  '<div class="keyline b">You have been building a library all day. '
  '<b>It is just scattered across nine conversations.</b></div>')

add('s5t1','S5 · Three homes',
  eyebrow('Section 5','5.1') +
  '<h2 class="demo-h b">Three places<br>a prompt can live.</h2>'
  + cards([('Home 1','A document','Simple, portable, works anywhere. You paste it in every time.'),
           ('Home 2','A Project','Instructions and files that apply to every chat inside it. Good for one ongoing job.'),
           ('Home 3','A Skill','Claude loads it on its own when the task matches. You stop pasting entirely.')]) +
  '<div class="punch b">Start with the document. <b>Promote the ones you actually reuse.</b>'
  '<span class="sm">A library of forty prompts you never open is not a library.</span></div>')

add('s5t2','S5 · What a Skill is',
  '<div class="bigemoji b">\U0001F9E9</div>'
  '<h2 class="demo-h b">What a Skill is</h2>'
  '<div class="defhero b">A saved set of instructions with a name and a trigger. '
  'When your request matches the trigger, <b>Claude loads it without being asked</b>.</div>'
  '<div class="frows">'
  '<div class="frow b"><span class="fe">\U0001F3F7️</span><span class="ft">'
  '<b>A name and a one line trigger</b> that says when it should fire</span></div>'
  '<div class="frow b"><span class="fe">\U0001F4DC</span><span class="ft">'
  '<b>The full instructions</b> which are just your best prompt, written to work on any input of that type</span></div>'
  '<div class="frow b"><span class="fe">\U0001F501</span><span class="ft">'
  '<b>Consistent output</b> because the same instructions run every time, not the ones you remembered</span></div>'
  '</div>'
  '<div class="closebar b">Worth making when you have done the same task <b>three times</b>. '
  'Not before.</div>')

add('lab7','Task 7',
  eyebrow('Task 7','In Claude') +
  '<h2 class="demo-h sm b">The library,<br>then one Skill.</h2>'
  + lab(7,'20','Five prompts with placeholders, and one that runs itself',
        ['Scroll back through two days and find the prompts that worked.',
         'Save four things for each: a title, the prompt with <b>[PLACEHOLDERS]</b>, the tool, what you fixed.',
         'Add one for a task <b>only your department has</b>.',
         'Then turn your best one into a Skill, and run it once to prove it works.']) +
  '<div class="keyline b">A prompt you cannot find again is not a saved prompt. '
  '<b>Name it for when you would reach for it.</b></div>')

# ============================== CLOSE
add('c1','Close · What you built',
  eyebrow('Today') +
  '<h2 class="demo-h b">What you built.</h2>'
  '<div class="road one">'
  '<div class="ritem b"><div class="rn">01</div><div><div class="rt">A six slide deck, built twice</div>'
  '<div class="rd">One prompt, two tools, and an opinion about which you would use.</div></div></div>'
  '<div class="ritem b"><div class="rn">02</div><div><div class="rt">A number you would sign</div>'
  '<div class="rd">From a file that offered you three, plus two charts that make a claim.</div></div></div>'
  '<div class="ritem b"><div class="rn">03</div><div><div class="rt">A library and a working Skill</div>'
  '<div class="rd">So tomorrow starts from something rather than nothing.</div></div></div>'
  '</div>')

add('c2','Close · Tomorrow',
  eyebrow('Tomorrow') +
  '<h2 class="close-punch b">Day 3: your own workflow,<br>and a package<br><b>you present.</b></h2>'
  '<div class="lead b" style="margin-top:30px">We open with data security and privacy, because tomorrow '
  'is the day you stop using our sample files and start looking at your own work.</div>'
  '<div class="keyline b">Then connectors, MCP and Skills, a workflow audit, '
  'and a capstone you present to the room.</div>')

add('c3','Close · Bring',
  eyebrow('Bring tomorrow') +
  '<h2 class="demo-h b">Three things.</h2>'
  + minilist([('Your prompt library','The one you built in task 7'),
              ('One real workflow','A task you do every week that you dread. We audit it at 09:30.'),
              ('Your laptop','Charged, with Claude and Excel open')]) +
  '<div class="keyline b">There is a short test tomorrow afternoon, and an end of programme survey. '
  '<b>Both take ten minutes together.</b></div>')

add('close','End',
  '<div class="clock b"><span class="live-dot"></span>End of Day 2</div>'
  '<h1 class="mega b">Thank you.</h1>'
  '<div class="covsub b">Day 3 starts at 09:00. Same room.</div>',
  center=True)

html = page('Day 2 &middot; Presentations and Data &middot; CODED', ''.join(S),
            back_href='coded-aiet-day-2.html')
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site', 'coded-aiet-day-2-deck.html')
open(out,'w').write(html)
print('slides:', len(S), 'bytes:', len(html), 'em:', html.count('—'))
