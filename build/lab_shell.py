# -*- coding: utf-8 -*-
"""Shared lab shell for AIET labs. CSS, body and the task renderer."""

CSS = r'''
:root{
  --bg:#00081C;--bg2:#000C22;--surface:#00112F;--surface2:#14243F;--raise:#1B3055;
  --line:#152A4A;--line2:#223D63;--line3:#31527F;
  --primary:#2F74D6;--deepblue:#004AA3;--soft:#6F9CE8;--light:#A8C6F2;--indigo:#3E50DD;
  --green:#3DC873;--green-lt:#8FE6AE;--gold:#E9C46A;--gold-lt:#FFE9B3;--danger:#FF5A6E;
  --ink:#F2F6FC;--ink2:#DCE6F5;--dim:#9FB2D4;--faint:#6F83A8;--ghost:#4D6188;
  --ink-faint:#6F83A8;
  --mono:'IBM Plex Mono',ui-monospace,monospace;
  --sans:'IBM Plex Sans','IBM Plex Sans Arabic',system-ui,sans-serif;
  --r-sm:8px;--r:12px;--r-lg:16px;--r-xl:22px;
  --rail-w:290px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.55;font-size:16px;
  background-image:radial-gradient(70% 55% at 100% 0%,rgba(0,74,163,.20),transparent 62%),
                   radial-gradient(60% 50% at 0% 100%,rgba(62,80,221,.10),transparent 60%);
  background-attachment:fixed}
button{font-family:inherit}
a{color:inherit;text-decoration:none}
::selection{background:rgba(47,116,214,.34)}
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-thumb{background:var(--line2);border-radius:99px;border:2px solid var(--bg)}
::-webkit-scrollbar-track{background:transparent}

#app{display:grid;grid-template-columns:var(--rail-w) 1fr;min-height:100vh}
#rail{position:sticky;top:0;height:100vh;background:linear-gradient(180deg,var(--bg2),#00060F);
  border-right:1px solid var(--line);display:flex;flex-direction:column;z-index:40}
.rail-top{padding:20px 20px 16px;border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px}
.brand .mark{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,var(--primary),var(--deepblue));
  display:grid;place-items:center;font-weight:700;color:#fff;font-size:13px;flex:none;font-family:var(--mono)}
.brand .bt{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--faint);line-height:1.3}
.brand .bt b{color:var(--soft);display:block;font-size:12.5px;letter-spacing:.1em}
.daychip{margin-top:15px;display:inline-flex;align-items:center;gap:8px;font-family:var(--mono);font-size:11px;
  letter-spacing:.06em;color:var(--ink2);background:rgba(255,255,255,.04);border:1px solid var(--line2);border-radius:99px;padding:6px 12px}
.daychip .d{width:7px;height:7px;border-radius:99px;background:var(--primary);box-shadow:0 0 8px var(--primary)}
.prog{margin-top:16px}
.prog .pl{display:flex;justify-content:space-between;align-items:baseline;font-family:var(--mono);font-size:11px;color:var(--faint);margin-bottom:7px}
.prog .pl b{color:var(--ink);font-size:13px}
.prog .bar{height:7px;border-radius:99px;background:rgba(255,255,255,.06);overflow:hidden}
.prog .fill{height:100%;width:0;border-radius:99px;background:linear-gradient(90deg,var(--deepblue),var(--soft));transition:width .6s cubic-bezier(.2,.8,.2,1)}
#navList{flex:1;overflow-y:auto;padding:12px 12px 8px}
.nav-sec{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ghost);padding:13px 12px 6px}
.nav-item{display:flex;align-items:center;gap:11px;width:100%;text-align:left;cursor:pointer;border:1px solid transparent;
  background:none;color:inherit;padding:11px 12px;border-radius:var(--r);margin-bottom:4px;transition:all .15s}
.nav-item:hover{background:rgba(255,255,255,.035);border-color:var(--line)}
.nav-item.active{background:rgba(47,116,214,.14);border-color:rgba(47,116,214,.45)}
.nav-item .ni-n{font-family:var(--mono);font-size:11px;font-weight:600;color:var(--faint);width:26px;height:26px;
  border-radius:8px;border:1px solid var(--line2);display:grid;place-items:center;flex:none;background:rgba(0,0,0,.25)}
.nav-item.active .ni-n{color:var(--soft);border-color:rgba(47,116,214,.55)}
.nav-item.done .ni-n{color:#04220f;background:var(--green);border-color:var(--green)}
.nav-item .ni-t{flex:1;min-width:0;font-size:13.5px;font-weight:600;color:var(--ink2);line-height:1.3}
.nav-item.active .ni-t{color:var(--ink)}
.rail-foot{padding:12px;border-top:1px solid var(--line)}
.rfbtn{width:100%;font-family:var(--mono);font-size:12px;cursor:pointer;border:1px solid var(--line2);
  background:rgba(0,0,0,.25);color:var(--dim);border-radius:var(--r-sm);padding:9px 10px;transition:all .15s}
.rfbtn:hover{color:var(--ink);border-color:var(--line3)}

#main{min-width:0;display:flex;flex-direction:column}
#mtop{position:sticky;top:0;z-index:30;background:rgba(0,8,28,.9);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--line);padding:12px 26px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.backlink{font-weight:600;font-size:13px;color:var(--dim);background:rgba(255,255,255,.05);
  border:1px solid var(--line2);border-radius:8px;padding:7px 12px;transition:all .15s}
.backlink:hover{color:var(--ink);border-color:var(--line3)}
.ham{display:none;background:none;border:1px solid var(--line2);color:var(--dim);border-radius:8px;padding:7px 11px;cursor:pointer;font-size:14px}
#crumb{font-family:var(--mono);font-size:11.5px;color:var(--faint);letter-spacing:.08em;text-transform:uppercase}
.mtop-r{margin-left:auto;display:flex;align-items:center;gap:8px}
.navbtn{background:rgba(0,0,0,.25);border:1px solid var(--line2);color:var(--dim);border-radius:8px;
  padding:7px 12px;cursor:pointer;font-size:14px;transition:all .15s}
.navbtn:hover:not(:disabled){color:var(--ink);border-color:var(--line3)}
.navbtn:disabled{opacity:.35;cursor:not-allowed}

#view{padding:34px 26px 90px;max-width:900px;width:100%;margin:0 auto}
.task-tag{display:flex;align-items:center;gap:11px;flex-wrap:wrap;font-family:var(--mono);font-size:11px;
  letter-spacing:.1em;text-transform:uppercase;color:var(--faint);margin-bottom:16px}
.task-tag .app{color:var(--soft);background:rgba(47,116,214,.14);border:1px solid rgba(47,116,214,.34);
  border-radius:99px;padding:5px 12px;font-weight:600}
.task-tag .mins{color:var(--ghost)}
.task-h{font-size:clamp(26px,3.6vw,38px);font-weight:700;letter-spacing:-1.1px;line-height:1.14;margin-bottom:14px}
.scn{font-size:16.5px;color:var(--dim);line-height:1.6;margin-bottom:24px;max-width:780px}

.step-card{background:var(--surface);border:1px solid var(--line);border-left:3px solid var(--primary);
  border-radius:0 var(--r-lg) var(--r-lg) 0;padding:20px 24px;margin-bottom:20px}
.sc-k{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--soft);font-weight:600;margin-bottom:13px}
.step-card ol{list-style:none;counter-reset:sx;display:flex;flex-direction:column;gap:11px}
.step-card ol li{counter-increment:sx;display:flex;gap:13px;font-size:15.5px;color:var(--ink2);line-height:1.5}
.step-card ol li::before{content:counter(sx);font-family:var(--mono);font-size:10.5px;font-weight:600;
  width:23px;height:23px;border-radius:50%;background:rgba(0,0,0,.3);border:1px solid var(--line2);
  color:var(--soft);display:flex;align-items:center;justify-content:center;flex:none;margin-top:2px}
.step-card ol li b{color:var(--ink)}

.prompt{position:relative;background:rgba(0,0,0,.34);border:1px solid var(--line2);border-radius:var(--r);
  padding:15px 17px 15px;margin-top:13px;font-size:14.5px;color:var(--ink2);line-height:1.55;cursor:pointer;transition:all .15s}
.prompt:hover{border-color:var(--line3);background:rgba(0,0,0,.5)}
.prompt.copied{border-color:var(--green);background:rgba(61,200,115,.08)}
.copy-tag{position:absolute;top:-9px;right:12px;font-family:var(--mono);font-size:9px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--faint);background:var(--bg);border:1px solid var(--line2);border-radius:20px;padding:3px 9px}
.prompt.copied .copy-tag{color:var(--green-lt);border-color:var(--green)}
.lw-starters{display:flex;flex-direction:column;gap:4px}

.lw-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.lw-tab{font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;color:var(--dim);background:rgba(0,0,0,.28);
  border:1px solid var(--line2);border-radius:99px;padding:8px 15px;cursor:pointer;transition:all .15s}
.lw-tab:hover{color:var(--ink);border-color:var(--line3)}
.lw-tab.on{background:rgba(47,116,214,.2);border-color:var(--primary);color:#fff}
.lw-job{font-size:15px;color:var(--ink2);margin-bottom:13px;line-height:1.5}
.lw-job b{color:var(--soft)}
.lw-pre{background:rgba(0,0,0,.4);border:1px solid var(--line2);border-radius:var(--r);padding:18px 20px;
  font-family:var(--mono);font-size:12.5px;line-height:1.72;color:var(--ink2);white-space:pre-wrap;
  overflow-x:auto;max-height:340px;overflow-y:auto;transition:all .15s}
.lw-pre.copyable{cursor:pointer}
.lw-pre.copyable:hover{border-color:var(--line3)}
.lw-pre.copied{border-color:var(--green)}
.lw-fields{display:flex;flex-direction:column;gap:9px;margin-top:16px}
.lw-fields input{background:var(--bg);border:1.5px solid var(--line2);color:var(--ink);border-radius:var(--r);
  padding:13px 15px;font-family:var(--sans);font-size:14.5px}
.lw-fields input:focus{outline:none;border-color:var(--primary)}
.lw-row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:4px}
.lw-btn{background:linear-gradient(135deg,var(--primary),var(--deepblue));color:#fff;border:none;border-radius:var(--r);
  padding:12px 20px;font-size:14.5px;font-weight:600;cursor:pointer;transition:all .16s}
.lw-btn:hover{transform:translateY(-2px)}
.lw-btn.ghost{background:transparent;border:1px solid var(--line2);color:var(--dim)}
.lw-btn.ghost:hover{color:var(--ink);border-color:var(--line3);transform:none}
.lw-hint{font-family:var(--mono);font-size:11.5px;color:var(--ink-faint)}
.lw-out{background:rgba(0,0,0,.4);border:1px solid var(--line2);color:var(--ink2);border-radius:var(--r);
  padding:15px 17px;font-family:var(--mono);font-size:13px;line-height:1.6;min-height:100px;resize:vertical;margin-top:4px;width:100%}
.lw-test{display:inline-flex;align-items:center;gap:8px;background:rgba(47,116,214,.16);
  border:1px solid rgba(47,116,214,.45);color:var(--light);border-radius:var(--r);padding:12px 18px;
  font-size:14px;font-weight:600;transition:all .15s}
.lw-test:hover{background:rgba(47,116,214,.28);color:#fff}

.qi{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:20px 22px;margin-bottom:12px;transition:border-color .2s}
.qi.right{border-color:rgba(61,200,115,.45);background:rgba(61,200,115,.06)}
.qi.wrong{border-color:rgba(255,90,110,.45);background:rgba(255,90,110,.05)}
.qi .qt{font-size:16px;line-height:1.55;color:var(--ink);margin-bottom:15px}
.qi .qopts{display:flex;gap:8px;flex-wrap:wrap}
.qopt{font-size:13.5px;font-weight:600;color:var(--dim);background:rgba(0,0,0,.28);border:1px solid var(--line2);
  border-radius:99px;padding:8px 16px;cursor:pointer;transition:all .15s}
.qopt:hover{color:var(--ink);border-color:var(--line3)}
.qopt.sel{background:rgba(47,116,214,.2);border-color:var(--primary);color:#fff}
.qopt.ok{background:rgba(61,200,115,.18);border-color:var(--green);color:var(--green-lt)}
.qopt.no{background:rgba(255,90,110,.15);border-color:var(--danger);color:#FFC2CA}
.qwhy{display:none;margin-top:14px;padding-top:14px;border-top:1px solid var(--line);font-size:14.5px;color:var(--dim);line-height:1.55}
.qwhy.show{display:block}
.qwhy b{color:var(--ink2)}
.verdict{margin-top:14px;font-size:15px;font-weight:600;display:none}
.verdict.show{display:block}
.verdict.bad{color:var(--danger)}
.verdict.good{color:var(--green-lt)}

.expect{background:linear-gradient(135deg,rgba(0,74,163,.2),rgba(0,74,163,.03));
  border:1px solid rgba(47,116,214,.36);border-radius:var(--r-lg);padding:20px 24px;margin-bottom:20px}
.ex-k{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--soft);font-weight:600;margin-bottom:10px}
.expect p{font-size:15.5px;color:var(--ink2);line-height:1.55}

.capture{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-xl);padding:22px 24px;margin-top:24px}
.capture label{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--faint);font-weight:600;margin-bottom:12px}
.capture textarea{width:100%;background:var(--bg);border:1.5px solid var(--line2);color:var(--ink);
  border-radius:var(--r);padding:14px 16px;font-family:var(--sans);font-size:15px;line-height:1.55;min-height:110px;resize:vertical}
.capture textarea:focus{outline:none;border-color:var(--primary)}
.cap-row{display:flex;align-items:center;gap:14px;margin-top:14px;flex-wrap:wrap}
.cap-btn{background:linear-gradient(135deg,var(--primary),var(--deepblue));color:#fff;border:none;
  border-radius:var(--r);padding:12px 22px;font-size:14.5px;font-weight:600;cursor:pointer;transition:all .16s}
.cap-btn:hover{transform:translateY(-2px)}
.cap-done{font-family:var(--mono);font-size:12px;color:var(--green-lt);opacity:0;transition:opacity .2s}
.cap-done.on{opacity:1}

.task-foot{display:flex;justify-content:space-between;gap:12px;margin-top:28px}
.tf-btn{background:rgba(0,0,0,.25);border:1px solid var(--line2);color:var(--dim);border-radius:var(--r);
  padding:13px 22px;font-size:14.5px;font-weight:600;cursor:pointer;transition:all .15s}
.tf-btn:hover:not(:disabled){color:var(--ink);border-color:var(--line3)}
.tf-btn:disabled{opacity:.32;cursor:not-allowed}
.tf-btn.next{background:linear-gradient(135deg,var(--primary),var(--deepblue));color:#fff;border-color:transparent}

@media(max-width:900px){
  #app{grid-template-columns:1fr}
  #rail{position:fixed;left:0;top:0;width:var(--rail-w);transform:translateX(-100%);transition:transform .25s}
  #rail.open{transform:none;box-shadow:0 0 60px rgba(0,0,0,.7)}
  .ham{display:block}
  #view{padding:26px 18px 80px}
}

/* ---------- dataset / file blocks ---------- */
.dataset{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:20px 22px;margin-bottom:20px}
.ds-k{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--soft);font-weight:600;margin-bottom:11px}
.ds-note{font-size:14.5px;color:var(--dim);line-height:1.55;margin-bottom:14px}
.dl{display:inline-flex;align-items:center;gap:12px;background:rgba(47,116,214,.16);border:1px solid rgba(47,116,214,.45);
  color:var(--light);border-radius:var(--r);padding:12px 18px;font-size:14.5px;font-weight:600;transition:all .15s;margin-bottom:4px}
.dl:hover{background:rgba(47,116,214,.28);color:#fff}
.dl .ic{font-size:15px}
.dl small{display:block;font-family:var(--mono);font-size:11px;font-weight:400;color:var(--dim);margin-top:3px}
.ds-table-wrap{margin-top:16px;overflow-x:auto;border:1px solid var(--line);border-radius:var(--r)}
.ds-table{border-collapse:collapse;width:100%;font-family:var(--mono);font-size:11.5px;white-space:nowrap}
.ds-table th{background:rgba(0,0,0,.34);color:var(--soft);text-align:left;padding:10px 13px;font-weight:600;
  border-bottom:1px solid var(--line2);letter-spacing:.04em}
.ds-table td{padding:9px 13px;color:var(--ink2);border-bottom:1px solid var(--line)}
.ds-table tr:last-child td{border-bottom:none}
.ds-more{padding:10px 13px;font-family:var(--mono);font-size:11px;color:var(--ghost)}

/* ---------- launches ---------- */
.launches{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px}
.launch{flex:1;min-width:230px;display:flex;flex-direction:column;gap:6px;background:rgba(47,116,214,.12);
  border:1px solid rgba(47,116,214,.4);border-radius:var(--r-lg);padding:16px 18px;transition:all .15s}
.launch:hover{background:rgba(47,116,214,.22)}
.launch .ln{font-size:15.5px;font-weight:600;color:#fff;display:flex;align-items:center;gap:8px}
.launch .lnn{font-size:13px;color:var(--dim);line-height:1.45}

/* ---------- goal ---------- */
.goal{background:linear-gradient(135deg,rgba(233,196,106,.13),rgba(233,196,106,.02));
  border:1px solid rgba(233,196,106,.34);border-left:3px solid var(--gold);
  border-radius:0 var(--r-lg) var(--r-lg) 0;padding:18px 22px;margin-bottom:20px}
.goal .gk{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:600;margin-bottom:9px}
.goal p{font-size:15.5px;color:var(--ink2);line-height:1.55}

/* ---------- prompt steps ---------- */
.pstep{background:var(--surface);border:1px solid var(--line);border-left:3px solid var(--primary);
  border-radius:0 var(--r-lg) var(--r-lg) 0;padding:20px 24px;margin-bottom:16px}
.pstep .psk{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--soft);font-weight:600;margin-bottom:11px}
.pstep .psg{font-size:15px;color:var(--ink2);line-height:1.55}

/* ---------- findings ---------- */
.findings{margin-top:16px;display:flex;flex-direction:column;gap:11px}
.find{display:flex;flex-direction:column;gap:6px}
.find > span{font-size:13.5px;color:var(--dim);font-weight:600}
.find-in{background:var(--bg);border:1.5px solid var(--line2);color:var(--ink);border-radius:var(--r);
  padding:12px 15px;font-family:var(--sans);font-size:14.5px;width:100%}
.find-in:focus{outline:none;border-color:var(--primary)}
.find-in.filled{border-color:rgba(61,200,115,.5);background:rgba(61,200,115,.05)}
.find-in::placeholder{color:var(--ghost);font-style:italic}
'''

BODY_TPL = '''<div id="app">
<aside id="rail">
  <div class="rail-top">
    <div class="brand"><span class="mark">AI</span>
      <span class="bt">AI Essentials<b>Day 1 Lab</b></span></div>
    <div class="daychip"><span class="d"></span> Day 1 &middot; Foundations and prompting</div>
    <div class="prog"><div class="pl"><span id="progLabel">0 of 7 done</span></div>
      <div class="bar"><div class="fill" id="progFill"></div></div></div>
  </div>
  <div id="navList"></div>
  <div class="rail-foot"><button class="rfbtn" id="resetBtn">&#8634; Reset my notes</button></div>
</aside>
<main id="main">
  <div id="mtop">
    <button class="ham" id="ham">&#9776;</button>
    <a class="backlink" href="coded-aiet-day-1.html">&lsaquo; Back to Day 1</a>
    <span id="crumb"></span>
    <span class="mtop-r">
      <button class="navbtn" id="mPrev">&lsaquo;</button>
      <button class="navbtn" id="mNext">&rsaquo;</button>
    </span>
  </div>
  <div id="view"></div>
</main>
</div>'''

JS = r'''
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function datasetBlock(d){
  return '<div class="dataset"><div class="ds-k">Attached data</div>'
    +'<div class="ds-note">'+d.note+'</div>'
    +'<a class="dl" href="'+d.href+'" download><span class="ic">\u2b07</span>'
    +'<span>Download<small>'+esc(d.label)+'</small></span></a>'
    +(d.head?'<div class="ds-table-wrap"><table class="ds-table"><thead><tr>'
      +d.head.map(function(h){return '<th>'+esc(h)+'</th>'}).join('')+'</tr></thead><tbody>'
      +d.rows.map(function(r){return '<tr>'+r.map(function(c){return '<td>'+esc(c)+'</td>'}).join('')+'</tr>'}).join('')
      +'</tbody></table><div class="ds-more">'+esc(d.more||'')+'</div></div>':'')
    +'</div>';
}
function launchBlock(ls){
  return '<div class="launches">'+ls.map(function(l){
    return '<a class="launch" href="'+l.href+'" target="_blank" rel="noopener">'
      +'<span class="ln">'+esc(l.label)+' \u2197</span>'
      +(l.note?'<span class="lnn">'+esc(l.note)+'</span>':'')+'</a>'}).join('')+'</div>';
}
function goalBlock(g){return '<div class="goal"><div class="gk">What you are aiming for</div><p>'+g+'</p></div>'}
function findVal(k){return (state[cur]&&state[cur].findings&&state[cur].findings[k])||''}
function findingsBlock(list,prefix){
  return '<div class="findings">'+list.map(function(f,i){
    var k=prefix+':'+i, v=findVal(k);
    return '<label class="find"><span>'+esc(f.label)+'</span>'
      +'<input class="find-in'+(v?' filled':'')+'" data-fk="'+k+'" value="'+esc(v)+'" placeholder="'+esc(f.hint||'')+'"></label>';
  }).join('')+'</div>';
}
function promptStepsBlock(steps){
  return steps.map(function(s,i){
    return '<div class="pstep"><div class="psk">'+s.label+'</div><p class="psg">'+s.goal+'</p>'
      +(s.prompt?'<div class="prompt st-prompt" data-p="'+s.prompt.replace(/"/g,'&quot;')+'">'
        +'<span class="copy-tag">tap to copy</span>'+s.prompt+'</div>':'')
      +(s.findings?findingsBlock(s.findings,'ps'+i):'')
      +'</div>';
  }).join('');
}
function bindFindings(v){
  v.querySelectorAll('.find-in').forEach(function(inp){
    inp.oninput=function(){
      state[cur]=state[cur]||{}; state[cur].findings=state[cur].findings||{};
      state[cur].findings[inp.dataset.fk]=inp.value; save();
      inp.classList.toggle('filled',!!inp.value);
    };
  });
}

const KEY='aiet_day1_lab';
let state={}; try{state=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){state={}}
let cur=0;
function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}

const navList=document.getElementById('navList');
function buildNav(){
  navList.innerHTML='';let lastSec=null;
  TASKS.forEach((t,i)=>{
    if(t.sec!==lastSec){lastSec=t.sec;
      const h=document.createElement('div');h.className='nav-sec';h.innerHTML=t.sec;navList.appendChild(h);}
    const el=document.createElement('div');
    el.className='nav-item'+(i===cur?' active':'')+((state[i]&&state[i].done)?' done':'');
    el.innerHTML='<span class="ni-n">'+((state[i]&&state[i].done)?'✓':(i+1))+'</span><span class="ni-t">'+t.title+'</span>';
    el.onclick=()=>{cur=i;render();window.scrollTo(0,0)};
    navList.appendChild(el);
  });
}
function updateProg(){
  const done=Object.values(state).filter(x=>x&&x.done).length;
  document.getElementById('progFill').style.width=(done/TASKS.length*100)+'%';
  document.getElementById('progLabel').textContent=done+' of '+TASKS.length+' done';
}
function flash(el,tagSel){const tag=el.querySelector(tagSel);el.classList.add('copied');
  if(tag){const old=tag.textContent;tag.textContent='copied ✓';
    setTimeout(()=>{el.classList.remove('copied');tag.textContent=old},1500);}
  else setTimeout(()=>el.classList.remove('copied'),1200);}
function fallback(text,done){const ta=document.createElement('textarea');ta.value=text;
  ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();
  try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(ta);}
function copy(text,el,tagSel){const done=()=>flash(el,tagSel);
  if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(text).then(done).catch(()=>fallback(text,done));
  else fallback(text,done);}

function engineHTML(t){
  const e=t.engine;
  return '<div class="sc-k">Answer all '+e.items.length+'</div>'
   + e.items.map((it,i)=>'<div class="qi" data-i="'+i+'"><div class="qt">'+it.t+'</div><div class="qopts">'
      + e.opts.map(o=>'<button class="qopt" data-k="'+o[0]+'">'+o[1]+'</button>').join('')
      + '</div><div class="qwhy"><b>Why.</b> '+it.why+'</div></div>').join('')
   + '<div class="lw-row" style="margin-top:14px"><button class="lw-btn" id="engCheck">Check my answers</button>'
   + '<button class="lw-btn ghost" id="engReset">Start over</button></div>'
   + '<div class="verdict" id="engVerdict"></div>';
}
function bindEngine(t,v){
  const e=t.engine,pick={};
  v.querySelectorAll('.qi').forEach(q=>{
    const i=+q.dataset.i;
    q.querySelectorAll('.qopt').forEach(b=>{
      b.onclick=()=>{if(q.classList.contains('right'))return;
        q.querySelectorAll('.qopt').forEach(x=>x.classList.remove('sel'));
        b.classList.add('sel');pick[i]=b.dataset.k;};
    });
  });
  document.getElementById('engCheck').onclick=()=>{
    let all=true;
    v.querySelectorAll('.qi').forEach(q=>{
      const i=+q.dataset.i,want=e.items[i].k,got=pick[i];
      q.classList.remove('right','wrong');
      q.querySelectorAll('.qopt').forEach(x=>x.classList.remove('ok','no'));
      if(!got){all=false;return}
      if(got===want){q.classList.add('right');q.querySelector('.qwhy').classList.add('show');
        q.querySelector('.qopt[data-k="'+got+'"]').classList.add('ok');}
      else{all=false;q.classList.add('wrong');q.querySelector('.qopt[data-k="'+got+'"]').classList.add('no');}
    });
    const vd=document.getElementById('engVerdict');
    if(all){vd.className='verdict show good';vd.textContent='Six for six. Mark it done below.';}
    else{vd.className='verdict show bad';vd.textContent='Not yet. The wrong ones are marked in red. Fix them and check again.';}
  };
  document.getElementById('engReset').onclick=()=>{render()};
}

function render(){
  const t=TASKS[cur],st=state[cur]||{};
  document.getElementById('crumb').innerHTML='Task '+(cur+1)+' of '+TASKS.length+' · '+t.sec;
  location.hash='t'+(cur+1);
  const v=document.getElementById('view');
  v.innerHTML=
    '<div class="task-tag"><span class="app">'+t.app+'</span><span>Task '+(cur+1)+' of '+TASKS.length+'</span><span class="mins">'+t.mins+'</span></div>'
   +'<h1 class="task-h">'+t.title+'</h1>'
   +'<p class="scn">'+t.scenario+'</p>'
   +(t.steps?'<div class="step-card"><div class="sc-k">Steps</div><ol>'+t.steps.map(s=>'<li>'+s+'</li>').join('')+'</ol>'
      +(t.prompt?'<div class="prompt" id="promptBox"><span class="copy-tag">tap to copy</span>'+t.prompt+'</div>':'')
      +'</div>':'')
   +(t.asset?'<a class="lw-test" href="'+t.asset.href+'" download style="margin:0 0 20px">⬇ '+t.asset.label+'</a>':'')
   +(t.files?t.files.map(function(f){return datasetBlock({note:f.note||'',href:f.href,label:f.label})}).join(''):'')
   +(t.dataset?datasetBlock(t.dataset):'')
   +(t.launches?launchBlock(t.launches):'')
   +(t.goal?goalBlock(t.goal):'')
   +(t.promptSteps?promptStepsBlock(t.promptSteps):'')
   +(t.findings?'<div class="step-card"><div class="sc-k">Record what you found</div>'+findingsBlock(t.findings,'top')+'</div>':'')
   +(t.starterlist?'<div class="step-card"><div class="sc-k">Starter menu, tap any to copy</div>'
      +'<div class="lw-starters">'+t.starterlist.map(x=>'<div class="prompt st-prompt" data-p="'+x.replace(/"/g,'&quot;')+'"><span class="copy-tag">tap to copy</span>'+x+'</div>').join('')+'</div></div>':'')
   +(t.engine?'<div class="step-card">'+engineHTML(t)+'</div>':'')
   +(t.widget?'<div class="step-card"><div class="sc-k">Build and test</div>'+t.widget+'</div>':'')
   +'<div class="expect"><div class="ex-k">Done looks like</div><p>'+t.expect+'</p></div>'
   +(t.stretch?'<div class="step-card" style="border-left-color:var(--soft)"><div class="sc-k">Tier 2 · Stretch, finished early?</div><p style="font-size:15px;color:var(--ink2);line-height:1.55">'+t.stretch+'</p></div>':'')
   +(t.boss?'<div class="step-card" style="border-left-color:var(--gold)"><div class="sc-k" style="color:var(--gold-lt)">Tier 3 · Boss challenge</div><p style="font-size:15px;color:var(--ink2);line-height:1.55">'+t.boss+'</p></div>':'')
   +'<div class="capture"><label>Paste your Claude result, or a note on how it went</label>'
   +'<textarea id="note" placeholder="Optional. Saves to this browser so you can review it later.">'+(st.note||'')+'</textarea>'
   +'<div class="cap-row"><button class="cap-btn" id="markDone">'+(st.done?'Saved ✓':'Mark done')+'</button>'
   +'<span class="cap-done '+(st.done?'on':'')+'" id="capDone">✓ Captured</span></div></div>'
   +'<div class="task-foot"><button class="tf-btn" id="tfPrev"'+(cur===0?' disabled':'')+'>‹ Previous</button>'
   +'<button class="tf-btn next" id="tfNext"'+(cur===TASKS.length-1?' disabled':'')+'>Next task ›</button></div>';

  const pb=document.getElementById('promptBox');
  if(pb)pb.onclick=()=>copy(t.prompt,pb,'.copy-tag');
  v.querySelectorAll('.st-prompt').forEach(sp=>sp.onclick=()=>copy(sp.dataset.p,sp,'.copy-tag'));
  v.querySelectorAll('.lw-pre.copyable').forEach(p=>p.onclick=()=>copy(p.innerText,p,'.nope'));

  if(v.querySelector('.lw-tabs')){
    const tabs=v.querySelectorAll('.lw-tab');
    tabs.forEach(tb=>tb.onclick=()=>{const sc=tb.dataset.sc;
      tabs.forEach(x=>x.classList.toggle('on',x===tb));
      v.querySelectorAll('.lw-doc [data-sc], .lw-job [data-sc], .lw-briefs [data-sc]').forEach(el=>{el.hidden=el.dataset.sc!==sc});
    });
  }
  if(document.getElementById('lwBuild')){
    const gg=id=>{const el=document.getElementById(id);return el?el.value.trim():''};
    document.getElementById('lwBuild').onclick=()=>{
      document.getElementById('lwOut').value=[gg('lwR'),gg('lwC'),gg('lwT'),gg('lwF'),gg('lwTo'),gg('lwX')].filter(Boolean).join('\n\n')};
    document.getElementById('lwCopy').onclick=()=>{const o=document.getElementById('lwOut').value.trim();if(!o)return;
      const h=document.getElementById('lwCopyHint');
      const ok=()=>{h.textContent='copied ✓';setTimeout(()=>h.textContent='',1500)};
      if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(o).then(ok).catch(()=>fallback(o,ok));
      else fallback(o,ok);};
  }
  if(t.engine)bindEngine(t,v);
  bindFindings(v);

  document.getElementById('markDone').onclick=()=>{
    const note=document.getElementById('note').value;
    state[cur]={done:true,note};save();
    document.getElementById('capDone').classList.add('on');
    document.getElementById('markDone').textContent='Saved ✓';buildNav();updateProg();};
  document.getElementById('note').oninput=e=>{state[cur]=state[cur]||{};state[cur].note=e.target.value;save()};
  const p=document.getElementById('tfPrev'),n=document.getElementById('tfNext');
  if(p)p.onclick=()=>{if(cur>0){cur--;render();window.scrollTo(0,0)}};
  if(n)n.onclick=()=>{if(cur<TASKS.length-1){cur++;render();window.scrollTo(0,0)}};
  buildNav();updateProg();
}
document.getElementById('mPrev').onclick=()=>{if(cur>0){cur--;render();window.scrollTo(0,0)}};
document.getElementById('mNext').onclick=()=>{if(cur<TASKS.length-1){cur++;render();window.scrollTo(0,0)}};
document.getElementById('ham').onclick=()=>document.getElementById('rail').classList.toggle('open');
document.getElementById('resetBtn').onclick=()=>{if(confirm('Clear all your captured notes for Day 1?')){state={};save();cur=0;render()}};
(function(){const m=(location.hash||'').match(/#t(\d+)/);if(m){const n=+m[1]-1;if(n>=0&&n<TASKS.length)cur=n;}})();
window.addEventListener('hashchange',()=>{const m=(location.hash||'').match(/#t(\d+)/);
  if(m){const n=+m[1]-1;if(n>=0&&n<TASKS.length&&n!==cur){cur=n;render();window.scrollTo(0,0)}}});
render();
'''

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&'
         'family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&'
         'display=swap" rel="stylesheet">')


def page(title, tasks_json, day, day_label, storage_key, back_href):
    body = (BODY_TPL
            .replace("Day 1 Lab", day_label + " Lab")
            .replace("Day 1 &middot; Foundations and prompting", day)
            .replace("coded-aiet-day-1.html", back_href)
            .replace("Back to Day 1", "Back to " + day_label)
            .replace("0 of 7 done", "0 of 7 done"))
    js = JS.replace("aiet_day1_lab", storage_key)
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>' + title + '</title>\n' + FONTS + '\n'
            '<style>' + CSS + '</style>\n</head>\n<body>\n' + body +
            '\n<script>const TASKS=' + tasks_json + ';\n' + js + '</script>\n</body>\n</html>\n')
