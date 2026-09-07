# -*- coding: utf-8 -*-
import json, os

Q = [
{"topic":"Day 1 · AI and LLMs","diff":"Easy",
 "q":"What is a large language model actually doing when it answers you?",
 "opts":["Looking the answer up in the documents it was trained on",
         "Predicting the most likely next piece of text",
         "Searching the internet in real time",
         "Running a database query against its memory"],
 "k":1,"why":"It kept the patterns, not the documents. Everything good and everything bad about the tool comes out of that one sentence."},
{"topic":"Day 1 · Limits","diff":"Easy",
 "q":"Which of these is a large language model weakest at?",
 "opts":["Shortening a long document","Changing the tone of a draft",
         "Knowing when it is wrong","Translating between English and Arabic"],
 "k":2,"why":"It never says “I do not know” by default. When it has no real answer, the most likely next text is still an answer, delivered with the same confidence."},
{"topic":"Day 1 · Hallucination","diff":"Moderate",
 "q":"An AI answer cites “the 2024 Gulf Workforce Productivity Report, page 112”. The report does not exist. What is this?",
 "opts":["An invented fact","An invented source","An invented confidence","A retrieval error"],
 "k":1,"why":"Title, authors, year and a page number that all look real. This is the shape that damages you most, because a fake citation in a circulated document is very hard to walk back."},
{"topic":"Day 1 · Prompting","diff":"Easy",
 "q":"Which part of a prompt is your main defence against invented facts?",
 "opts":["Tone","Format","Constraints","Role"],
 "k":2,"why":"“Use only the figures I give you. Do not estimate. If something is missing, ask.” Constraints are the half people skip, and the half that keeps you safe."},
{"topic":"Day 1 · Prompting","diff":"Moderate",
 "q":"Your team writes customer replies in a style nobody has ever written down. What do you do?",
 "opts":["Describe the style carefully in the prompt",
         "Paste two real examples and ask for a third",
         "Ask Claude to invent a house style",
         "Write it yourself, it cannot be taught"],
 "k":1,"why":"Few-shot. When the style is real but nobody wrote it down, stop describing and start showing. Two good examples beat a paragraph of description."},
{"topic":"Day 1 · Research","diff":"Moderate",
 "q":"You need a summary of a twenty page report. What is the single most useful habit?",
 "opts":["Ask it to be accurate","Give it the source and forbid outside facts",
         "Ask for bullet points","Ask it to search the web as well"],
 "k":1,"why":"Give it the source. Do not ask it for the source. That turns a guessing machine into a reading machine. Then check the summary back against the document."},
{"topic":"Day 2 · Presentations","diff":"Easy",
 "q":"You have a forty page report and need six slides where every figure traces back to it. Where do you start?",
 "opts":["Gamma, then fix the numbers","Claude with the report attached",
         "PowerPoint by hand","Either, it makes no difference"],
 "k":1,"why":"The document has to be in the room. Gamma generates from a prompt, not from your attached report, so every figure would be invented or copied in by you."},
{"topic":"Day 2 · Presentations","diff":"Moderate",
 "q":"What is the honest claim about AI built decks?",
 "opts":["Better than what you would have written",
         "Faster than what you would have formatted",
         "Both of those","Neither, it is only useful for images"],
 "k":1,"why":"Two completely different claims. Only one of them is true, and it is still worth a lot. A deck that looks right and misquotes a number is worse than no deck."},
{"topic":"Day 2 · Data","diff":"Moderate",
 "q":"A survey file shows Procurement with the highest satisfaction at 4.33, from three responses. What do you do?",
 "opts":["Report it, it is the highest score",
         "Report it with a note about the sample",
         "Do not report it as a result at all",
         "Recalculate it without the outliers"],
 "k":2,"why":"The smallest sample always looks like the best result. Three people is noise, and putting it in a board pack gives it a title it has not earned."},
{"topic":"Day 2 · Validation","diff":"Hard",
 "q":"You need a total your finance team will accept. What do you ask Claude for?",
 "opts":["The number, with its working shown","The Excel formula to paste into the sheet",
         "A chart of the numbers","A confidence score on the number"],
 "k":1,"why":"A number you cannot reproduce is a rumour. A formula sitting in the real spreadsheet is a result. Your finance team will accept a formula and will not accept “the AI said”."},
{"topic":"Day 3 · Workflow","diff":"Moderate",
 "q":"In a workflow audit, which steps should you automate?",
 "opts":["Every step that takes more than ten minutes",
         "The judgment steps, because they are the slowest",
         "The pattern steps you would still check afterwards",
         "All of them, or the audit was pointless"],
 "k":2,"why":"Automate the step you would still check. If you would not check the output, you have built a machine for producing confident mistakes at speed."},
{"topic":"Day 3 · Connectors","diff":"Moderate",
 "q":"What does turning on a connector change about your data exposure?",
 "opts":["Nothing, it only changes how the data gets there",
         "It makes the data more secure because it never leaves your account",
         "It removes the need for a paste rule",
         "It gives Claude access to files you cannot see yourself"],
 "k":0,"why":"A connector changes the plumbing, not the exposure. It reads only what you already have access to, and every rule you wrote about what is safe to share still applies."},
]

CSS = r"""
:root{
  --bg:#00081C;--surface:#00112F;--surface2:#14243F;--line:#152A4A;--line2:#223D63;--line3:#31527F;
  --primary:#2F74D6;--deep:#004AA3;--soft:#6F9CE8;--light:#A8C6F2;
  --green:#3DC873;--green-lt:#8FE6AE;--amber:#E9C46A;--danger:#FF5A6E;
  --ink:#F2F6FC;--ink2:#DCE6F5;--dim:#9FB2D4;--faint:#6F83A8;--ghost:#4D6188;
  --mono:'IBM Plex Mono',ui-monospace,monospace;
  --sans:'IBM Plex Sans','IBM Plex Sans Arabic',system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{background:radial-gradient(1100px 640px at 85% -8%,rgba(0,74,163,.20),transparent 60%),var(--bg);
  color:var(--ink);font-family:var(--sans);line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.top{position:sticky;top:0;z-index:30;background:rgba(0,8,28,.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--line)}
.top .in{max-width:680px;margin:0 auto;padding:13px 24px;display:flex;align-items:center;gap:14px}
.backlink{font-size:13px;font-weight:600;color:var(--dim);background:rgba(255,255,255,.05);
  border:1px solid var(--line2);border-radius:8px;padding:7px 12px}
.backlink:hover{color:var(--ink)}
.brand{display:flex;align-items:center;gap:9px;font-weight:600;font-size:15.5px;letter-spacing:-.3px}
.brand .dot{width:9px;height:9px;border-radius:50%;background:var(--primary);box-shadow:0 0 10px var(--primary)}
.brand b{color:var(--soft);font-weight:600}
.score{margin-left:auto;font-family:var(--mono);font-size:12.5px;color:var(--green-lt);
  background:rgba(61,200,115,.12);border:1px solid rgba(61,200,115,.36);border-radius:99px;padding:6px 14px}
.prail{height:4px;background:rgba(255,255,255,.06)}
.prail i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--deep),var(--soft));transition:width .4s}
.wrap{max-width:680px;margin:0 auto;padding:36px 24px 90px}
.lede{margin-bottom:30px}
.lede h1{font-size:clamp(28px,5vw,40px);font-weight:700;letter-spacing:-1.2px;line-height:1.1}
.lede p{margin-top:14px;color:var(--dim);font-size:16px;line-height:1.6}
.q{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:24px 26px;margin-bottom:18px}
.qtags{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin-bottom:15px}
.qn{font-family:var(--mono);font-size:11px;color:var(--faint);letter-spacing:.1em}
.qtopic{font-family:var(--mono);font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;
  background:rgba(47,116,214,.16);border:1px solid rgba(47,116,214,.4);color:var(--soft);border-radius:99px;padding:4px 11px}
.qdiff{font-family:var(--mono);font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;
  border-radius:99px;padding:4px 11px;margin-left:auto}
.qdiff.Easy{background:rgba(61,200,115,.14);border:1px solid rgba(61,200,115,.4);color:var(--green-lt)}
.qdiff.Moderate{background:rgba(233,196,106,.14);border:1px solid rgba(233,196,106,.4);color:var(--amber)}
.qdiff.Hard{background:rgba(255,90,110,.14);border:1px solid rgba(255,90,110,.4);color:#FFC2CA}
.qtext{font-size:20px;font-weight:600;letter-spacing:-.4px;line-height:1.35;margin-bottom:17px}
.opts{display:flex;flex-direction:column;gap:9px}
.opt{display:flex;align-items:center;gap:12px;text-align:left;background:rgba(0,0,0,.26);
  border:1px solid var(--line2);border-radius:13px;padding:14px 16px;font-family:var(--sans);
  font-size:15.5px;color:var(--ink2);cursor:pointer;transition:all .15s}
.opt:hover{border-color:var(--line3);color:var(--ink)}
.opt .k{font-family:var(--mono);font-size:11.5px;font-weight:600;width:24px;height:24px;border-radius:7px;
  background:rgba(255,255,255,.06);border:1px solid var(--line2);display:grid;place-items:center;flex:none;color:var(--faint)}
.opt.ok{background:rgba(61,200,115,.14);border-color:var(--green);color:#fff}
.opt.ok .k{background:var(--green);border-color:var(--green);color:#04220f}
.opt.no{background:rgba(255,90,110,.13);border-color:var(--danger)}
.opt.no .k{background:var(--danger);border-color:var(--danger);color:#2a0207}
.exp{display:none;margin-top:16px;padding-top:16px;border-top:1px solid var(--line)}
.exp.on{display:block}
.exp .v{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;margin-bottom:9px}
.exp .v.ok{color:var(--green-lt)} .exp .v.no{color:var(--danger)}
.exp .w{font-size:15px;color:var(--dim);line-height:1.6}
.exp .m{margin-top:12px;font-family:var(--mono);font-size:11.5px;color:var(--ghost)}
.endcard{display:none;background:linear-gradient(150deg,rgba(47,116,214,.16),rgba(0,74,163,.05));
  border:1px solid rgba(47,116,214,.4);border-radius:22px;padding:34px 30px;text-align:center;margin-top:26px}
.endcard.on{display:block}
.ring{width:150px;height:150px;margin:0 auto 20px;position:relative}
.ring svg{transform:rotate(-90deg)}
.ring .bg{stroke:rgba(255,255,255,.08)}
.ring .fg{stroke-linecap:round;transition:stroke-dashoffset 1.1s cubic-bezier(.2,.7,.2,1)}
.ring .num{position:absolute;inset:0;display:grid;place-items:center;font-family:var(--mono);
  font-size:34px;font-weight:600;letter-spacing:-1px}
.endcard h2{font-size:26px;font-weight:700;letter-spacing:-.7px;margin-bottom:10px}
.endcard p{color:var(--dim);font-size:15.5px;line-height:1.6;max-width:420px;margin:0 auto 22px}
.bars{text-align:left;margin:22px 0}
.bar{margin-bottom:13px}
.bar .bl{display:flex;justify-content:space-between;font-family:var(--mono);font-size:11.5px;color:var(--dim);margin-bottom:6px}
.bar .bt{height:6px;border-radius:99px;background:rgba(255,255,255,.07);overflow:hidden}
.bar .bf{height:100%;border-radius:99px;background:linear-gradient(90deg,var(--deep),var(--soft));width:0;transition:width .8s}
.acts{display:flex;gap:11px;justify-content:center;flex-wrap:wrap}
.btn{background:linear-gradient(135deg,var(--primary),var(--deep));color:#fff;border:none;border-radius:13px;
  padding:14px 24px;font-family:var(--sans);font-size:15px;font-weight:600;cursor:pointer;transition:all .18s}
.btn:hover{transform:translateY(-2px)}
.btn.ghost{background:transparent;border:1px solid var(--line2);color:var(--dim)}
.btn.ghost:hover{color:var(--ink);border-color:var(--line3);transform:none}
.foot{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);font-family:var(--mono);font-size:12px;color:var(--ghost)}
"""

JS = r"""
var answered=0,correct=0,byTopic={};
Q.forEach(function(q){byTopic[q.topic]=byTopic[q.topic]||{n:0,c:0};byTopic[q.topic].n++;});
var wrap=document.getElementById('qs');
Q.forEach(function(q,i){
  var el=document.createElement('div');el.className='q';el.id='q'+i;
  el.innerHTML='<div class="qtags"><span class="qn">Q'+(i+1)+' / '+Q.length+'</span>'
    +'<span class="qtopic">'+q.topic+'</span><span class="qdiff '+q.diff+'">'+q.diff+'</span></div>'
    +'<div class="qtext">'+q.q+'</div><div class="opts">'
    +q.opts.map(function(o,j){return '<button class="opt" data-j="'+j+'">'
      +'<span class="k">'+'ABCD'[j]+'</span><span>'+o+'</span></button>'}).join('')
    +'</div><div class="exp"><div class="v"></div><div class="w"></div>'
    +'<div class="m">&#9670; Maps to '+q.topic+' &middot; '+q.diff+'</div></div>';
  wrap.appendChild(el);
  el.querySelectorAll('.opt').forEach(function(b){
    b.onclick=function(){
      if(el.dataset.done)return; el.dataset.done='1';
      var j=+b.dataset.j, right=j===q.k;
      el.querySelectorAll('.opt')[q.k].classList.add('ok');
      if(!right)b.classList.add('no');
      var e=el.querySelector('.exp');
      e.querySelector('.v').className='v '+(right?'ok':'no');
      e.querySelector('.v').textContent=right?'Correct':'Not quite';
      e.querySelector('.w').textContent=q.why;
      e.classList.add('on');
      answered++; if(right){correct++;byTopic[q.topic].c++;}
      document.getElementById('sc').textContent=correct+' / '+answered;
      document.getElementById('pf').style.width=(answered/Q.length*100)+'%';
      if(answered===Q.length)finish();
    };
  });
});
function finish(){
  var card=document.getElementById('end');card.classList.add('on');
  var pct=Math.round(correct/Q.length*100);
  var col=pct>=80?'var(--green)':pct>=60?'var(--amber)':'var(--danger)';
  var ring=document.getElementById('ringfg');
  var C=2*Math.PI*66;
  ring.style.stroke=col;ring.style.strokeDasharray=C;ring.style.strokeDashoffset=C;
  document.getElementById('ringnum').textContent=correct+'/'+Q.length;
  document.getElementById('ringnum').style.color=col;
  document.getElementById('endmsg').textContent =
    pct>=80?'You could teach most of this. Look at the one you missed and you are done.'
    :pct>=60?'Solid. The topics below with a short bar are the ones worth ten minutes each.'
    :'Worth another pass. Every day page is still online, and the shortest bar below is where to start.';
  var bars=document.getElementById('bars');bars.innerHTML='';
  Object.keys(byTopic).forEach(function(t){
    var b=byTopic[t],p=Math.round(b.c/b.n*100);
    var d=document.createElement('div');d.className='bar';
    d.innerHTML='<div class="bl"><span>'+t+'</span><span>'+b.c+' / '+b.n+'</span></div>'
      +'<div class="bt"><div class="bf"></div></div>';
    bars.appendChild(d);
    setTimeout(function(){d.querySelector('.bf').style.width=p+'%';},60);
  });
  setTimeout(function(){ring.style.strokeDashoffset=C*(1-correct/Q.length);},120);
  card.scrollIntoView({behavior:'smooth',block:'center'});
}
document.getElementById('again').onclick=function(){location.reload()};
document.getElementById('review').onclick=function(){
  var first=[].slice.call(document.querySelectorAll('.q')).filter(function(el){
    return el.querySelector('.opt.no')})[0];
  if(first)first.scrollIntoView({behavior:'smooth',block:'center'});
  else alert('Nothing to review. You got them all.');
};
"""

BODY = """
<div class="top"><div class="in">
  <a class="backlink" href="coded-aiet-day-3.html">&lsaquo; Day 3</a>
  <span class="brand"><span class="dot"></span>Practice <b>quiz</b></span>
  <span class="score" id="sc">0 / 0</span>
</div><div class="prail"><i id="pf"></i></div></div>

<div class="wrap">
  <div class="lede">
    <h1>Twelve questions,<br>three days.</h1>
    <p>Answer each one and the reason appears straight away. Nobody sees your score,
       and there is a topic breakdown at the end telling you what to look at again.</p>
  </div>
  <div id="qs"></div>

  <div class="endcard" id="end">
    <div class="ring">
      <svg width="150" height="150" viewBox="0 0 150 150">
        <circle class="bg" cx="75" cy="75" r="66" fill="none" stroke-width="9"></circle>
        <circle class="fg" id="ringfg" cx="75" cy="75" r="66" fill="none" stroke-width="9"></circle>
      </svg>
      <div class="num" id="ringnum"></div>
    </div>
    <h2>That is the lot.</h2>
    <p id="endmsg"></p>
    <div class="bars" id="bars"></div>
    <div class="acts">
      <button class="btn" id="again">Practice again</button>
      <button class="btn ghost" id="review">Review what I missed</button>
    </div>
  </div>

  <div class="foot">AI Essentials in the Workplace &middot; CODED &middot; 8 to 10 September 2026</div>
</div>
"""

html = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>Practice Quiz &middot; AI Essentials in the Workplace</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&'
        'family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
        '<style>'+CSS+'</style>\n</head>\n<body>\n'+BODY+
        '\n<script>var Q='+json.dumps(Q,ensure_ascii=False)+';\n'+JS+'</script>\n</body>\n</html>\n')
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','site','coded-aiet-quiz.html')
open(out,'w').write(html)
print('questions:',len(Q),'bytes:',len(html),'em:',html.count('—'))
