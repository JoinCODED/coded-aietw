# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_shell import page, slide

S = []
def add(sid, title, body, **kw): S.append(slide(sid, title, body, **kw))

def eyebrow(t, n=""):
    return '<div class="eyebrow b">' + t + (' <span class="tnum">' + n + '</span>' if n else '') + '</div>'

def question(sid, title, q, sub="", sec=False):
    body = ('<div class="qmark b">Question</div>'
            '<h1 class="bigq b">' + q + '</h1>'
            + ('<div class="qsub b">' + sub + '</div>' if sub else ''))
    add(sid, title, body, sec=sec, center=True)

def cards(items, cls=""):
    out = '<div class="spread-row ' + cls + '">'
    for it in items:
        out += ('<div class="sc b"><div class="sw">' + it[0] + '</div>'
                '<div class="st">' + it[1] + '</div>'
                '<div class="sd">' + it[2] + '</div></div>')
    return out + '</div>'

def minilist(rows):
    out = '<div class="mini-list">'
    for k, v in rows:
        out += '<div class="mini-row b"><div class="mk">' + k + '</div><div class="mv">' + v + '</div></div>'
    return out + '</div>'

def mc(q, opts, fb):
    out = '<div class="mc b"><div class="mc-q">' + q + '</div><div class="mc-opts">'
    for i, (letter, text, correct) in enumerate(opts):
        out += ('<button class="mc-opt" data-k="' + ('1' if correct else '0') + '" data-fb="' + fb + '">'
                '<span class="mo-k">' + letter + '</span><span>' + text + '</span></button>')
    return out + '</div><div class="mc-fb"></div></div>'

def lab(num, mins, title, steps, where="In Claude"):
    out = ('<div class="labcard b"><div class="lh">'
           '<span class="lnum">Task ' + str(num) + '</span>'
           '<span class="ltime">' + mins + ' minutes</span>'
           '<span class="lwhere">' + where + '</span></div>'
           '<div class="lt">' + title + '</div><ol class="labsteps">')
    for st in steps: out += '<li>' + st + '</li>'
    out += ('</ol><a class="labgo" href="coded-aiet-day-1-lab.html#t' + str(num) + '">'
            'Open task ' + str(num) + ' &rarr;</a></div>')
    return out
add('cover', 'Title',
    '<div class="clock b"><span class="live-dot"></span>Day 1 &middot; Tuesday 8 September 2026 &middot; 09:00 to 14:00</div>'
    '<h1 class="mega b">AI Essentials<br>in the <span class="accent">Workplace</span></h1>'
    '<div class="covsub b">Foundations, responsible use, and prompting. Today you learn what this tool '
    'really does, and how to ask it properly.</div>'
    '<div class="covmeta b"><span>CODED Campus, Kuwait</span><span>Tool: Claude</span><span>Day 1 of 3</span></div>',
    center=True)

add('outcomes', 'Outcomes',
    eyebrow('Today') +
    '<h2 class="demo-h b">Three things you<br>leave with.</h2>'
    '<div class="road one">'
    '<div class="ritem b"><div class="rn">01</div><div><div class="rt">A document you improved</div>'
    '<div class="rd">One of your own. Real, not a sample.</div></div></div>'
    '<div class="ritem b"><div class="rn">02</div><div><div class="rt">A research summary you can defend</div>'
    '<div class="rd">Every fact checked back to its source.</div></div></div>'
    '<div class="ritem b"><div class="rn">03</div><div><div class="rt">Five prompts you will reuse</div>'
    '<div class="rd">Saved, named, and ready for tomorrow.</div></div></div>'
    '</div>')

add('maptest', 'MAP test (pre)',
    eyebrow('Before we start') +
    '<h2 class="demo-h b">First, a short test.</h2>'
    '<div class="testbox b"><div class="tl">Pre-program MAP test</div>'
    '<div class="tv">8 minutes, silent</div>'
    '<div class="td">This is your baseline. There is no pass mark, and your score is not shared '
    'with anyone. You take the same test again at the end of Day 3.</div>'
    '<span class="tph" id="map-pre" data-placeholder="true">Link to be added</span></div>',
    center=True)

question('theq', 'THE QUESTION',
         'What is one task or process<br>on your desk you <b>dread</b> the most?',
         'Say it out loud. We are writing them all down.', sec=True)

question('s1q', 'S1 · What is AI', 'What is <b>AI</b>?', 'No wrong answers. Shout.', sec=True)

add('s1t1', 'S1 · What is AI',
    '<div class="bigemoji b">\U0001F916</div>'
    '<h2 class="demo-h b">What is AI, really?</h2>'
    '<div class="defhero b">Software that can <b>understand</b>, <b>learn</b>, and <b>generate</b> '
    'content that used to need a person to do it.</div>'
    '<div class="frows">'
    '<div class="frow b"><span class="fe">\U0001F4D6</span><span class="ft">'
    '<b>Reads and understands text</b> such as a contract, a report, or an email thread</span></div>'
    '<div class="frow b"><span class="fe">\u270D\uFE0F</span><span class="ft">'
    '<b>Writes content</b> such as memos, notices, summaries and replies</span></div>'
    '<div class="frow b"><span class="fe">\U0001F4AC</span><span class="ft">'
    '<b>Answers questions</b> about anything you paste into it</span></div>'
    '<div class="frow b"><span class="fe">\U0001F9E9</span><span class="ft">'
    '<b>Helps you solve problems</b> by laying out options, trade-offs and next steps</span></div>'
    '<div class="frow b"><span class="fe">\U0001F50B</span><span class="ft">'
    '<b>Never gets tired and never forgets</b> at 8 AM or 8 PM, the same quality</span></div>'
    '</div>'
    '<div class="closebar b">Think of it as a <b>fast assistant</b>, not a replacement for your judgment.</div>')

add('s1t2', 'S1 · Already there',
    eyebrow('Section 1', '1.1') +
    '<h2 class="demo-h b">You already use it<br>every day.</h2>'
    + minilist([
        ('Your inbox', 'The spam filter learned what junk looks like. Nobody wrote a rule for each message.'),
        ('Your maps app', 'It predicts the traffic in twenty minutes, then routes you around it.'),
        ('Your bank', 'A card payment in another country gets flagged in under a second.'),
        ('Your phone', 'Face unlock. Photo search for "beach". Autocorrect.'),
    ]) +
    '<div class="keyline b">None of that felt like AI. <b>It just felt like the thing working.</b></div>')

question('s2q', 'S1 · What is an LLM', 'So what is a<br><b>large language model</b>?')

add('s2t1', 'S1 · It read',
    eyebrow('Section 1', '1.2') +
    '<h2 class="demo-h b">Step one:<br>it read.</h2>'
    '<div class="lead b">Books, websites, code, manuals, forum posts, transcripts. '
    'More text than any person could read in a thousand lifetimes.</div>'
    '<div class="keyline b">That is the <b>"large"</b> part. It is about the reading, not the file size.</div>')

add('s2t2', 'S1 · Patterns not documents',
    eyebrow('Section 1', '1.2') +
    '<h2 class="demo-h b">Step two: it kept<br>the patterns.</h2>'
    '<div class="defbox b"><div class="dt">The important part</div>'
    '<div class="dd">It did <b>not</b> keep the documents. It kept how words tend to follow '
    'other words. The library is gone. Only the habits are left.</div></div>'
    '<div class="keyline b">This is why it cannot quote your company handbook. '
    '<b>It never stored a copy of anything.</b></div>')

add('s2t3', 'S1 · Autocomplete',
    eyebrow('Section 1', '1.2') +
    '<h2 class="demo-h b">You have seen this<br>a thousand times.</h2>'
    '<div class="ac-wrap ac-demo b">'
    '<div class="ac-screen">'
    '<div class="ac-lbl">Your phone keyboard</div>'
    '<div class="ac-line"></div>'
    '<div class="ac-bar"></div>'
    '</div></div>'
    '<div class="keyline b">Your keyboard read your messages and learned what usually comes next. '
    '<b>Claude is the same idea, at an enormous scale.</b></div>')

add('s2t4', 'S1 · It predicts',
    eyebrow('Section 1', '1.2') +
    '<h2 class="demo-h b">Therefore:<br>it <span class="hl">predicts</span>.</h2>'
    '<div class="defbox b"><div class="dt">The one idea the whole day rests on</div>'
    '<div class="dd">A large language model does one thing. It looks at everything so far, '
    'and predicts <b>the most likely next piece of text</b>. Then it does it again. '
    'That is the entire trick.</div></div>'
    '<div class="keyline b">Everything good and everything bad about this tool '
    '<b>comes out of that one sentence.</b></div>')

question('s3q', 'S1 · Which tool', 'Which one should<br>you actually open?')

add('s3t1', 'S1 · The landscape',
    eyebrow('Section 1', '1.3') +
    '<h2 class="demo-h b">The four you will<br>hear about.</h2>'
    + cards([
        ('Anthropic', 'Claude', 'Long documents, careful writing, analysis you need to trust. Our tool for three days.'),
        ('OpenAI', 'ChatGPT', 'The one everybody knows. Broad, fast, huge add-on ecosystem.'),
        ('Google', 'Gemini', 'Sits inside Google Workspace. Docs, Sheets, Gmail.'),
        ('Microsoft', 'Copilot', 'Sits inside Office. Word, Excel, Teams, your company files.'),
    ], cls='four') +
    '<div class="punch b">They are closer to each other than the marketing suggests.'
    '<span class="sm">Pick by where your work already lives, not by the brand.</span></div>')

add('s4q', 'S1 · Why care',
    '<h2 class="demo-h b">Why should <span class="hl">you</span> care?</h2>'
    '<div class="subline b">Not because it is new. Because of what it gives back to your week.</div>'
    '<div class="wc">'
    '<div class="wcard b"><div class="we">\u23F1\uFE0F</div><div class="wt">Save time</div>'
    '<div class="wd">Automate repetitive writing. Shorten long documents. Get a first draft in minutes '
    'instead of an hour.</div></div>'
    '<div class="wcard b"><div class="we">\u2705</div><div class="wt">Improve quality</div>'
    '<div class="wd">Catch errors, tighten unclear writing, and sound consistently professional.</div></div>'
    '<div class="wcard b"><div class="we">\U0001F4A1</div><div class="wt">Think better</div>'
    '<div class="wd">Weigh up options, organize messy information, and see a problem from angles you '
    'had not considered.</div></div>'
    '<div class="wcard b"><div class="we">\U0001F4C8</div><div class="wt">Work smarter</div>'
    '<div class="wd">Read data faster, prepare for meetings quicker, and spend your hours on judgment '
    'instead of typing.</div></div>'
    '</div>'
    '<div class="footline b">None of this replaces you. <b>It removes the part of the job that was '
    'never the point.</b></div>', sec=True)

add('s4t1', 'S1 · Three changes',
    eyebrow('Section 1', '1.4') +
    '<h2 class="demo-h b">Three things change<br>for one person.</h2>'
    + cards([
        ('Change 1', 'The blank page is gone', 'You never start from nothing. You start by fixing a draft, which is far easier.'),
        ('Change 2', 'You get a second opinion', 'At 11pm. On anything. Before you send it to your manager.'),
        ('Change 3', 'The boring part shrinks', 'The formatting, the first summary, the rewrite for a different reader.'),
    ]) +
    '<div class="punch b">Nobody is going to do this <b>for</b> you.'
    '<span class="sm">IT can give you the licence. Only you know which of your tasks is worth it.</span></div>')

add('s4t2', 'S1 · Your name',
    eyebrow('Section 1', '1.4') +
    '<h2 class="close-punch b">One thing does<br>not change.<br><br><b>Your name goes<br>on the output.</b></h2>'
    '<div class="lead b" style="margin-top:32px">If it invents a number and you send it, '
    'you sent it. Not the tool. That rule holds for every hour of the next three days.</div>')

add('s5t1', 'S1 · Well vs fails',
    eyebrow('Section 1', '1.5') +
    '<h2 class="demo-h b">Strong here.<br>Weak there.</h2>'
    '<div class="vs">'
    '<div class="vcol good b"><div class="vh">It is strong at</div><ul>'
    '<li>Turning rough notes into clean writing</li>'
    '<li>Shortening something long</li>'
    '<li>Changing the tone for a different reader</li>'
    '<li>Translating between English and Arabic</li>'
    '<li>Finding the pattern in text you give it</li>'
    '<li>Structure: agendas, outlines, templates</li>'
    '</ul></div>'
    '<div class="vcol bad b"><div class="vh">It is weak at</div><ul>'
    '<li>Arithmetic, unless it writes the formula</li>'
    '<li>Today\'s facts, prices, and news</li>'
    '<li>Anything inside your company it was never given</li>'
    '<li>Knowing when it is wrong</li>'
    '<li>Saying "I do not know"</li>'
    '<li>Your judgement about your own business</li>'
    '</ul></div></div>')

add('s5t2', 'S1 · The junior',
    eyebrow('Section 1', '1.5') +
    '<h2 class="close-punch b">A fast, confident junior<br>who has <b>read everything</b><br>and remembers<br><b>nothing exactly.</b></h2>'
    '<div class="keyline b" style="margin-top:34px">You would check that person\'s numbers. '
    '<b>Check these too.</b></div>')

add('lab1', 'Task 1',
    eyebrow('Task 1', 'In Claude') +
    '<h2 class="demo-h sm b">First contact.</h2>'
    + lab(1, '8', 'Your first useful result, on your own laptop',
          ['Open Claude and start a new chat.',
           'Pick one starter from the menu and run it. There is an Arabic one too.',
           'Read what comes back. <b>Would you actually use it?</b> That is the bar.',
           'Turn to the person next to you and name one thing that surprised you.']) +
    '<div class="keyline b">Everything today runs on <b>sample data we supply</b>. Do not paste anything real from your own work. The rules for that come at <b>13:25</b>.</div>')

add('brk1', 'Break 1',
    eyebrow('Break') +
    '<h2 class="brk-h b">Section 1 done.<br><b>Take a break.</b></h2>'
    '<div class="brk-sub b">You know what it is, what it does, and where it fails. Prompting is next.</div>'
    '<div class="brk-pick b"><button class="brk-opt" data-min="10"><span class="bn">10</span><span class="bu">minutes</span></button><button class="brk-opt alt" data-min="15"><span class="bn">15</span><span class="bu">minutes</span></button></div>'
    '<div class="brk-note b">Pick a length. The countdown goes full screen and shows the room when to be back.</div>', center=True)

add('s8reveal', 'S3 · The reveal',
    eyebrow('Section 2', '2.1') +
    '<h2 class="demo-h b">Two prompts.<br>One task.</h2>'
    '<div class="split2">'
    '<div class="b"><div class="pbox-lbl">What most people type</div>'
    '<div class="pbox">Write me a report about last quarter.</div></div>'
    '<div class="b"><div class="pbox-lbl">The same task, written properly</div>'
    '<div class="pbox"><span class="pk">You are</span> a finance analyst writing for a busy director.\n\n'
    '<span class="pk">Context:</span> Q3 sales were 8% below target. The main gap was in\n'
    'the retail channel. I have the figures below.\n\n'
    '<span class="pk">Task:</span> Write the summary section of the quarterly report.\n\n'
    '<span class="pk">Format:</span> 200 words. Three short paragraphs. No bullet points.\n\n'
    '<span class="pk">Tone:</span> Direct and factual. No hedging.\n\n'
    '<span class="pk">Constraints:</span> Use only the figures I give you. If something\n'
    'is missing, ask me instead of estimating.</div></div>'
    '</div>'
    '<div class="keyline b">Same tool. Same task. <b>The only thing that changed was the person typing.</b></div>')

add('s8punch', 'S3 · You are the variable',
    '<h2 class="close-punch b">You are<br>the <b>variable</b>.</h2>'
    '<div class="lead b" style="margin-top:32px">Everyone in this room has the same model. '
    'The difference in what you get out is entirely the difference in what you put in.</div>',
    center=True)

question('s9q', 'S3 · What works', 'What actually makes<br>a prompt <b>work</b>?', sec=True)

add('s9t1', 'S3 · CTFT',
    eyebrow('Section 2', '2.1') +
    '<h2 class="demo-h b">C T F T</h2>'
    + minilist([
        ('Context', 'What is going on. Who the reader is. What already happened.'),
        ('Task', 'The one thing you want done. One verb.'),
        ('Format', 'How long. What shape. Paragraphs, table, bullet list, email.'),
        ('Tone', 'Formal, direct, warm, technical. Say it, do not hope for it.'),
    ]) +
    '<div class="keyline b">Most weak prompts have the <b>Task</b> and nothing else.</div>')

add('s9t2', 'S3 · Two upgrades',
    eyebrow('Section 2', '2.1') +
    '<h2 class="demo-h b">Then two upgrades.</h2>'
    '<div class="spread-row two">'
    '<div class="sc b"><div class="sw">Upgrade 1</div><div class="st">Role</div>'
    '<div class="sd">Tell it who to be. <b>"You are a procurement officer reviewing a supplier bid."</b> '
    'This changes the vocabulary, the priorities, and what it thinks matters.</div></div>'
    '<div class="sc b"><div class="sw">Upgrade 2</div><div class="st">Constraints</div>'
    '<div class="sd">Tell it what <b>not</b> to do. <b>"Use only the figures I give you. '
    'Do not estimate. If something is missing, ask."</b> This is your main defence against hallucination.</div></div>'
    '</div>'
    '<div class="keyline b">Constraints are the half people skip. '
    '<b>They are the half that keeps you safe.</b></div>')

add('lab2', 'Task 2',
    eyebrow('Task 2', 'In Claude') +
    '<h2 class="demo-h sm b">Build a<br>full prompt.</h2>'
    + lab(2, '14', 'Six parts, one stand-in document, one real result',
          ['Pick a scenario: a staff survey result, or a budget overrun. Both are sample data.',
           'Read the stand-in document, then fill all six fields in the builder.',
           'Press Assemble, press Copy, then run it in Claude.',
           'Compare the answer against the document. Did it <b>miss</b> anything? Did it <b>invent</b> anything?']) +
    '<div class="keyline b">Boss tier: drop one part on purpose and see which omission '
    '<b>does the most damage.</b></div>')

question('s10q', 'S3 · Describing', 'When is <b>describing</b><br>not enough?')

add('s10t1', 'S3 · Zero and few shot',
    eyebrow('Section 2', '2.2') +
    '<h2 class="demo-h b">Tell it, or<br>show it.</h2>'
    '<div class="spread-row two">'
    '<div class="sc b"><div class="sw">Zero-shot</div><div class="st">You describe</div>'
    '<div class="sd">"Write it in our house style: short, formal, no jargon." '
    'Fine when the style is easy to put into words.</div></div>'
    '<div class="sc b"><div class="sw">Few-shot</div><div class="st">You show</div>'
    '<div class="sd">"Here are two emails we sent last month. Write the third one like these." '
    'The examples do the explaining for you.</div></div>'
    '</div>'
    '<div class="keyline b">Two good examples beat a paragraph of description. '
    '<b>Every time.</b></div>')

add('s10t2', 'S3 · When to show',
    eyebrow('Section 2', '2.2') +
    '<h2 class="close-punch b">Use few-shot when the style<br>is <b>real but hard to explain.</b></h2>'
    '<div class="lead b" style="margin-top:30px">Your team has a way of writing customer replies. '
    'Nobody has ever written it down, and everybody knows when it is wrong. '
    'That is exactly the case for showing two examples instead of describing it.</div>')

add('lab3', 'Task 3',
    eyebrow('Task 3', 'In Claude') +
    '<h2 class="demo-h sm b">Show, do<br>not describe.</h2>'
    + lab(3, '10', 'Zero-shot against few-shot, same task',
          ['Two sample customer replies on the page are the house style.',
           'Round one: <b>describe</b> the style in words. Ask for a third reply. Do not paste the examples.',
           'Round two, new chat: <b>paste both examples</b>, then ask for the third.',
           'Put the two side by side. Which one sounds like the team?']))

add('brk2', 'Break 2',
    eyebrow('Break') +
    '<h2 class="brk-h b">Section 2 done.<br><b>Take a break.</b></h2>'
    '<div class="brk-sub b">You can write a prompt properly now. Next we point it at real writing.</div>'
    '<div class="brk-pick b"><button class="brk-opt" data-min="10"><span class="bn">10</span><span class="bu">minutes</span></button><button class="brk-opt alt" data-min="15"><span class="bn">15</span><span class="bu">minutes</span></button></div>'
    '<div class="brk-note b">Pick a length. The countdown goes full screen and shows the room when to be back.</div>', center=True)

question('s11q', 'S4 · Weak draft', 'The first draft<br>is <b>weak</b>. Now what?', sec=True)

add('s11t1', 'S4 · Three moves',
    eyebrow('Section 3') +
    '<h2 class="demo-h b">Three repair moves.</h2>'
    + cards([
        ('Move 1', 'Cut it', '"Half the length. Keep every fact." The fastest quality gain there is.'),
        ('Move 2', 'Sharpen it', '"Replace every vague phrase with a specific one. Point to the exact line."'),
        ('Move 3', 'Change the reader', '"Rewrite this for the finance director, who has ninety seconds."'),
    ]) +
    '<div class="punch b">Run them <b>in that order</b>, one at a time.'
    '<span class="sm">Asking for all three at once gets you a worse version of all three.</span></div>')

add('s11t2', 'S4 · In Arabic',
    eyebrow('Section 3') +
    '<h2 class="demo-h sm b">The same three moves,<br>in Arabic.</h2>'
    '<div class="split2">'
    '<div class="b"><div class="pbox-lbl">The draft</div>'
    '<div class="pbox ar">نود أن نحيطكم '
    'علماً بأنه وبعد الدراسة '
    'المستفيضة للموضوع قد تقرر '
    'تأجيل الموعد.</div></div>'
    '<div class="b"><div class="pbox-lbl">After "cut it, keep every fact"</div>'
    '<div class="pbox ar">تم تأجيل الموعد '
    'بعد المراجعة.</div></div>'
    '</div>'
    '<div class="keyline b">The moves are the same in both languages. '
    '<b>Ask in the language you want the answer in.</b></div>')

add('lab4', 'Task 4',
    eyebrow('Task 4', 'In Claude') +
    '<h2 class="demo-h sm b">Rewrite it.<br>Tone and length.</h2>'
    + lab(4, '10', 'One clunky paragraph, six commands, same chat',
          ['Copy the paragraph from the lab page into Claude.',
           'Run six rewrite commands in turn, <b>in the same conversation</b>. Do not start a new chat.',
           'The last one asks for it in Arabic, keeping the same tone.',
           'Notice what survives every version. <b>That is the actual message.</b>']))

add('lab5', 'Task 5',
    eyebrow('Task 5', 'In Claude') +
    '<h2 class="demo-h sm b">Draft a real<br>document.</h2>'
    + lab(5, '15', 'A brief in, a document you would send out',
          ['Pick one of three briefs: a staff memo, a customer notice, or a status update.',
           'Write a full six part prompt for it. Do not skip Format or Constraints.',
           'Generate the draft, then <b>edit it by hand</b>. Fix the tone, check every fact, cut repeats.',
           'Read it out loud once. If you stumble, so will the reader.']) +
    '<div class="keyline b">This is your Day 1 deliverable. <b>Bring it tomorrow.</b></div>')

add('brk3', 'Lunch',
    eyebrow('Break') +
    '<h2 class="brk-h b">Section 3 done.<br><b>Lunch and prayer.</b></h2>'
    '<div class="brk-sub b">Two documents built. After lunch: research, then the rules for your own work.</div>'
    '<div class="brk-pick b"><button class="brk-opt" data-min="45"><span class="bn">45</span><span class="bu">minutes</span></button><button class="brk-opt alt" data-min="60"><span class="bn">60</span><span class="bu">minutes</span></button></div>'
    '<div class="brk-note b">Back at the time on screen. Bring your laptop.</div>', center=True)

add('s11re', 'S4 · Re-entry',
    eyebrow('Welcome back') +
    '<h2 class="demo-h b">Turn to the person<br>next to you.</h2>'
    '<div class="lead b">Three minutes, seated. One question: '
    '<b>which prompt from this morning will you actually use next week?</b></div>'
    '<div class="keyline b">If your answer is "none yet", say that out loud. '
    '<b>We will fix it in the next hour.</b></div>')

question('s12q', 'S5 · Research', 'Can I use it to<br><b>find things out</b>?', sec=True)

add('s12t1', 'S5 · Callback',
    eyebrow('Callback', 'Section 1') +
    '<h2 class="demo-h b">Look at the<br>weak column again.</h2>'
    '<div class="lead b">"Today\'s facts." "Knowing when it is wrong." '
    'Those two are exactly what a research question asks for.</div>'
    '<div class="keyline b">So the answer is <b>no for facts, yes for structure.</b> '
    'The fix is to change where the facts come from.</div>')

add('s12t2', 'S5 · Give it the source',
    eyebrow('Section 4') +
    '<h2 class="close-punch b">Give it the source.<br>Do <b>not</b> ask it<br>for the source.</h2>'
    '<div class="lead b" style="margin-top:30px">Paste the report. Attach the PDF. Link the page. '
    'Then say: <b>"Answer only from what I gave you. If it is not in there, say so."</b></div>'
    '<div class="keyline b">This turns a guessing machine into a reading machine. '
    '<b>The single most useful habit on this slide deck.</b></div>')

add('s12t3', 'S5 · The brief',
    eyebrow('Section 4') +
    '<h2 class="demo-h b">The summarizing<br>brief.</h2>'
    + minilist([
        ('Who reads it', '"A department head with no background in this."'),
        ('How long', '"One page. Around 300 words."'),
        ('Keep', '"Every figure, and anything with a deadline attached."'),
        ('Drop', '"Background, methodology, and anything before 2024."'),
    ]) +
    '<div class="keyline b">A summary without a named reader is <b>just a shorter document.</b></div>')

add('lab6', 'Task 6',
    eyebrow('Task 6', 'In Claude') +
    '<h2 class="demo-h sm b">Summarize,<br>then verify.</h2>'
    + lab(6, '14', 'One operations report with five planted faults',
          ['Download the report from the lab page and attach it to Claude. It is sample data.',
           'Ask for a one page summary: the position, the risks, the open questions.',
           'Then ask it to <b>cite the exact line</b> for every number it used.',
           'Pick three numbers and check them yourself. The report has <b>five deliberate faults</b>.']) +
    '<div class="keyline b">Finding one is a pass. Finding three is very good. '
    '<b>Finding five means you are ready for Day 2.</b></div>')

add('brk4', 'Break 4',
    eyebrow('Break') +
    '<h2 class="brk-h b">Section 4 done.<br><b>Short break.</b></h2>'
    '<div class="brk-sub b">Last stretch. Trust, privacy, and the rules you take back to your desk.</div>'
    '<div class="brk-pick b"><button class="brk-opt" data-min="10"><span class="bn">10</span><span class="bu">minutes</span></button><button class="brk-opt alt" data-min="15"><span class="bn">15</span><span class="bu">minutes</span></button></div>'
    '<div class="brk-note b">Pick a length. The countdown goes full screen and shows the room when to be back.</div>', center=True)

question('s13q', 'S5 · Email',
         'How much of your week<br>is your <b>inbox</b>?',
         'Say a number. Most people say too low.', sec=True)

add('s13t1', 'S5 · Email end to end',
    '<div class="bigemoji b">\u2709\uFE0F</div>'
    '<h2 class="demo-h b">Email, end to end</h2>'
    '<div class="defhero b">Three things Claude handles well on email. All three are just '
    '<b>draft</b>, <b>rewrite</b> and <b>summarize</b> pointed at your inbox.</div>'
    '<div class="frows">'
    '<div class="frow b"><span class="fe">\U0001F4E5</span><span class="ft">'
    '<b>Summarize a thread</b> such as "what was decided, what is still open, and what do I owe anyone?"</span></div>'
    '<div class="frow b"><span class="fe">\u270D\uFE0F</span><span class="ft">'
    '<b>Draft a reply</b> such as "answer the customer below, apologize for the delay, '
    'give Thursday as the new date, under 100 words"</span></div>'
    '<div class="frow b"><span class="fe">\U0001F501</span><span class="ft">'
    '<b>Match your own voice</b> such as "reply in the same tone I used earlier in this thread"</span></div>'
    '</div>'
    '<div class="closebar b">Nothing here is new. <b>It is Sections 2, 3 and 4 pointed at one place '
    'you already spend your day.</b></div>')

add('s13t2', 'S5 · The catch',
    eyebrow('Section 5', '5.1') +
    '<h2 class="close-punch b">Right now, all of this<br>is <b>copy and paste.</b></h2>'
    '<div class="lead b" style="margin-top:30px">You open the thread. You select it. You copy it. '
    'You switch tabs. You paste it. You read the answer. You copy that back.</div>'
    '<div class="keyline b">It still saves you time. But it is the part people quietly stop doing '
    'after two weeks. <b>Hold that thought.</b></div>')

add('lab7', 'Task 7',
    eyebrow('Task 7', 'In Claude') +
    '<h2 class="demo-h sm b">Tame<br>the thread.</h2>'
    + lab(7, '12', 'A long thread you were copied into, and the reply you owe',
          ['Copy the thread from the lab page. Five messages, four people, one deadline.',
           'Ask for the summary in <b>the shape you need</b>: decisions made, questions still open, who owns what.',
           'Check it against the thread. Did it miss anything? Did it <b>invent an owner</b>?',
           'Draft your reply, then rewrite it once for tone.']) +
    '<div class="keyline b">There is a trap in the thread. Nobody actually agreed a date, '
    '<b>but it reads like they did.</b></div>')

question('s14q', 'S5 · MCP',
         'What if it could read<br>the inbox <b>itself</b>?',
         'Flexible block. Moves to Day 2 if we are short on time.')

add('s14t1', 'S5 · Connectors and MCP',
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

add('s14demo', 'S5 · Live demo',
    eyebrow('Watch this one') +
    '<h2 class="demo-h b">Live, on screen.</h2>'
    '<div class="road one">'
    '<div class="ritem b"><div class="rn">01</div><div><div class="rt">Turn a connector on</div>'
    '<div class="rd">What the permission screen actually asks for, and what it does not.</div></div></div>'
    '<div class="ritem b"><div class="rn">02</div><div><div class="rt">Ask the same question as Task 7</div>'
    '<div class="rd">Except this time nobody pastes a thread. It reads the thread itself.</div></div></div>'
    '<div class="ritem b"><div class="rn">03</div><div><div class="rt">Turn it back off</div>'
    '<div class="rd">Because knowing how to revoke it is the part your IT team will ask about.</div></div></div>'
    '</div>'
    '<div class="keyline b">You are watching, not doing. <b>Day 3 is when you build your own.</b></div>')

add('c1', 'Close · Callback',
    eyebrow('Callback', 'This morning') +
    '<h2 class="demo-h b">The task you said<br>you dreaded.</h2>'
    '<div class="lead b">Go back to the answer you gave at 09:15. '
    '<b>Would you do it differently on Sunday?</b></div>'
    '<div class="keyline b">Be honest about the ones that did not move. '
    'Some of them are Day 2 problems, and some are Day 3 problems.</div>')

add('c2', 'Close · What you built',
    eyebrow('Today') +
    '<h2 class="demo-h b">What you built.</h2>'
    '<div class="road one">'
    '<div class="ritem b"><div class="rn">01</div><div><div class="rt">An improved document</div>'
    '<div class="rd">Lab 5. Cut, sharpened, aimed at a new reader.</div></div></div>'
    '<div class="ritem b"><div class="rn">02</div><div><div class="rt">A research summary you checked</div>'
    '<div class="rd">Lab 6. Three facts traced back to the source.</div></div></div>'
    '<div class="ritem b"><div class="rn">03</div><div><div class="rt">Five reusable prompts</div>'
    '<div class="rd">Labs 1 to 6, plus your paste rule at the top.</div></div></div>'
    '</div>')

add('c3', 'Close · Prompt library',
    eyebrow('Homework, five minutes') +
    '<h2 class="demo-h b">Name your prompts<br>before you leave.</h2>'
    '<div class="lead b">A prompt you cannot find again is not a saved prompt. '
    'Give each one a name that says <b>when you would reach for it.</b></div>'
    + minilist([
        ('Good name', '"Shorten a long email for a director"'),
        ('Bad name', '"Prompt 3"'),
        ('Good name', '"Summarize a supplier report, source only"'),
        ('Bad name', '"Untitled chat"'),
    ]) +
    '<div class="keyline b">Bring the library tomorrow. <b>Day 2 adds to it.</b></div>')

add('c4', 'Close · Tomorrow',
    eyebrow('Tomorrow') +
    '<h2 class="close-punch b">Day 2: you turn this<br>into <b>slides and numbers.</b></h2>'
    '<div class="lead b" style="margin-top:30px">Claude Design and Gamma in the morning. '
    'Real data, real charts, and checking the maths in the afternoon.</div>'
    '<div class="keyline b">Bring your prompt library. Bring a laptop that opens Excel.</div>')

add('close', 'End',
    '<div class="clock b"><span class="live-dot"></span>End of Day 1</div>'
    '<h1 class="mega b">Thank you.</h1>'
    '<div class="covsub b">Day 2 starts at 09:00. Same room.</div>',
    center=True)


# ================================================================
# PARKED SLIDES. Not emitted into the deck.
#   s9t3    the "one test for any prompt" check
#   s6q s6t1 s6t2            hallucinations: three shapes of failure
#   s7q s7t1 s7t2 s7t3 s7close   privacy: the four boxes, the paste rule,
#                                the five second scan
# To restore: set RESTORE_PARKED = True and add the ids to ORDER above.
# Recommended home for the privacy block: the opening of Day 2, before
# anyone in the room touches real data.
# ================================================================
RESTORE_PARKED = False
if RESTORE_PARKED:
    question('s6q', 'S5 · When wrong', 'What is it doing<br>when it is <b>wrong</b>?', sec=True)

    add('s6t1', 'S2 · No I dont know',
        eyebrow('Section 5', '5.1') +
        '<h2 class="demo-h b">It does not say<br>"I do not know".</h2>'
        '<div class="defbox b"><div class="dt">Remember the prediction slide</div>'
        '<div class="dd">It predicts the most likely next piece of text. '
        'When it has no real answer, <b>the most likely next text is still an answer.</b> '
        'It sounds exactly as confident as when it is right.</div></div>'
        '<div class="keyline b">The word for this is <b>hallucination</b>. '
        'It is not lying. It has no idea it is doing it.</div>')

    add('s6t2', 'S2 · Three shapes',
        eyebrow('Section 5', '5.1') +
        '<h2 class="demo-h b">Three shapes<br>of failure.</h2>'
        + cards([
            ('Shape 1', 'Invented fact', 'A number, a date, a rule that sounds right and is not. The most common one.'),
            ('Shape 2', 'Invented source', 'A report title, an author, a link. It looks real. It does not exist.'),
            ('Shape 3', 'Invented confidence', 'It answers a question about your company it was never told anything about.'),
        ]) +
        '<div class="punch b">Shape 2 is the dangerous one at work.'
        '<span class="sm">A fake source in a report you circulate is very hard to walk back.</span></div>')

    add('s7close', 'S2 · Your paste rule',
        eyebrow('Section 5') +
        '<h2 class="demo-h b">Write your own<br>paste rule.</h2>'
        '<div class="lead b">One line, in your own words, for your own job. '
        'Something you will still remember on a busy Thursday.</div>'
        '<div class="pbox b">My paste rule:\n\nI will never paste ______________________ into an AI tool.\n\n'
        'If I need help with it, I will ______________________ first.</div>'
        '<div class="keyline b">Save it at the top of your prompt library. <b>It is the first entry.</b></div>')

    question('s7q', 'S5 · Where it goes', 'Where does what<br>you <b>paste</b> actually go?')

    add('s7t1', 'S2 · The path',
        eyebrow('Section 5', '5.2') +
        '<h2 class="demo-h b">Four boxes.</h2>'
        + minilist([
            ('Box 1', 'Your screen. You paste the paragraph.'),
            ('Box 2', 'The internet. It leaves your building and your network.'),
            ('Box 3', 'A server somewhere else. Another country, another company\'s control.'),
            ('Box 4', 'A log. It may be kept. It may be reviewed by a human. It depends on the plan you are on.'),
        ]) +
        '<div class="keyline b">A free consumer account and a company account '
        '<b>are not the same on box 4.</b> Ask your IT team which one you have.</div>')

    add('s7t2', 'S2 · The rule',
        eyebrow('Section 5', '5.2') +
        '<h2 class="close-punch b">If you would not<br><b>email it to a supplier,</b><br>do not paste it.</h2>'
        '<div class="lead b" style="margin-top:30px">One sentence. It covers almost every case, '
        'and you can remember it under pressure.</div>')

    add('s7t3', 'S2 · Five second test',
        eyebrow('Section 5', '5.2') +
        '<h2 class="demo-h sm b">The five second scan.</h2>'
        '<div class="lead b">Before you press paste, look for five things.</div>'
        + minilist([
            ('Names', 'A person who did not agree to this'),
            ('Numbers', 'Account, ID, licence, passport, phone'),
            ('Contracts', 'Anything with a signature or a price on it'),
            ('Salary', 'Pay, bonus, headcount by person'),
            ('Health', 'Sick leave, medical notes, insurance claims'),
        ]) +
        '<div class="keyline b">Find one? <b>Replace it with a placeholder and keep going.</b> '
        'You almost never need the real value for the tool to help you.</div>')

    add('s9t3', 'S3 · The test',
        eyebrow('Section 2', '2.1') +
        '<h2 class="demo-h sm b">One test for<br>any prompt.</h2>'
        + mc('You have written your prompt. What is the fastest way to tell whether it is good enough?',
             [('A', 'Count the words. Longer is better.', False),
              ('B', 'Ask whether a new colleague could do this task from your prompt alone.', True),
              ('C', 'Check that it uses polite language.', False),
              ('D', 'Run it twice and compare.', False)],
             'If a capable new colleague would still have to come back and ask you three questions, '
             'the model will guess at those three things instead. Guessing is where the errors come from.'))


html = page('Day 1 &middot; Foundations and Prompting &middot; CODED', ''.join(S))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site', 'coded-aiet-day-1-deck.html')
open(out, 'w').write(html)
print('slides:', len(S))
print('bytes:', len(html))
