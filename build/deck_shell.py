# -*- coding: utf-8 -*-
"""Shared shell for AIET decks: CODED navy theme + the workshop-builder deck engine."""

CSS = r"""
:root{
  --base:#00081C; --surf:#00112F; --surf2:#14243F; --deep:#00224D; --panel:#12294F;
  --deepest:#00224D; --deepblue:#004AA3; --primary:#2F74D6; --soft:#6F9CE8; --light:#A8C6F2;
  --indigo:#3E50DD; --red:#F84B4B;
  --w:#fff;--w8:rgba(255,255,255,.8);--w7:rgba(255,255,255,.7);--w6:rgba(255,255,255,.6);
  --w5:rgba(255,255,255,.5);--w4:rgba(255,255,255,.4);--w3:rgba(255,255,255,.3);
  --w2:rgba(255,255,255,.2);--w1:rgba(255,255,255,.1);--w06:rgba(255,255,255,.06);
  --line:rgba(255,255,255,.10);
  --green:#3DC873;--green-lt:#8FE6AE;--amber:#E9C46A;--danger:#FF5A6E;
  --mf:'IBM Plex Sans','IBM Plex Sans Arabic',system-ui,sans-serif;
  --mono:'IBM Plex Mono',ui-monospace,monospace;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden;font-family:var(--mf);background:var(--base);color:var(--w)}
svg{display:block}
.icn{width:1em;height:1em;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;flex:none}

.slide{position:fixed;inset:0;display:none;flex-direction:column;overflow-y:auto;overflow-x:hidden}
.slide.active{display:flex}
.slide::-webkit-scrollbar{width:8px}
.slide::-webkit-scrollbar-thumb{background:var(--w1);border-radius:4px}

.bg-grid{position:absolute;inset:0;pointer-events:none;background-image:linear-gradient(rgba(255,255,255,.016) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.016) 1px,transparent 1px);background-size:58px 58px;-webkit-mask:radial-gradient(circle at 50% 26%,#000,transparent 80%);mask:radial-gradient(circle at 50% 26%,#000,transparent 80%)}
.blob{position:absolute;border-radius:50%;pointer-events:none;filter:blur(120px);mix-blend-mode:screen}
.blob.b1{width:760px;height:760px;background:rgba(0,74,163,.34);top:-280px;right:-200px}
.blob.b2{width:560px;height:560px;background:rgba(47,116,214,.20);bottom:-180px;left:-140px}
.blob.b3{width:420px;height:420px;background:rgba(62,80,221,.16);top:40%;left:46%}

#prail-wrap{position:fixed;top:0;left:0;right:0;height:2px;z-index:120;background:var(--w06)}
#prail{height:100%;width:0;background:linear-gradient(90deg,var(--indigo),var(--deepblue),var(--primary),var(--soft));transition:width .4s ease}

.deck-back{position:fixed;top:14px;left:16px;z-index:110;display:flex;align-items:center;gap:7px;background:rgba(20,36,63,.9);border:1px solid var(--line);border-radius:30px;padding:7px 14px 7px 10px;font-family:var(--mono);font-size:11px;color:var(--w6);letter-spacing:.08em;text-transform:uppercase;text-decoration:none;backdrop-filter:blur(10px);transition:all .15s}
.deck-back:hover{color:var(--w);border-color:var(--w2);background:rgba(20,36,63,1)}
.deck-back svg{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}

.deck-nav{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);z-index:100;display:flex;align-items:center;gap:8px;background:rgba(20,36,63,.92);backdrop-filter:blur(20px);border:1px solid var(--line);border-radius:40px;padding:6px;box-shadow:0 12px 40px rgba(0,0,0,.5)}
.nav-btn{background:none;border:none;color:var(--w7);cursor:pointer;width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;transition:all .15s;font-size:18px}
.nav-btn:hover{background:var(--w06);color:var(--w)}
.nav-btn:active{transform:scale(.94)}
.nav-btn.fs{font-size:14px}
.nav-divider{width:1px;height:20px;background:var(--w1);margin:0 4px}
.nav-pos{color:var(--w);font-weight:600;letter-spacing:.06em;padding:0 10px;font-size:12px;min-width:54px;text-align:center;font-family:var(--mono)}
.nav-pos .cur{color:var(--soft)}
.nav-pos .tot{color:var(--w4)}

.nav-dots{position:fixed;top:50%;right:18px;transform:translateY(-50%);z-index:90;display:flex;flex-direction:column;gap:7px;padding:13px 8px;background:rgba(20,36,63,.6);backdrop-filter:blur(12px);border:1px solid var(--line);border-radius:30px;opacity:.4;transition:opacity .2s;max-height:86vh;overflow:auto}
.nav-dots::-webkit-scrollbar{display:none}
.nav-dots:hover{opacity:1}
@media(max-width:900px){.nav-dots{display:none}}
.nav-dot{width:9px;height:9px;border-radius:50%;background:var(--w2);cursor:pointer;border:none;padding:0;transition:all .2s;position:relative;flex:none}
.nav-dot:hover{background:var(--w5);transform:scale(1.3)}
.nav-dot.active{background:var(--primary);transform:scale(1.35);box-shadow:0 0 0 3px rgba(47,116,214,.25)}
.nav-dot.sec{background:var(--soft);opacity:.5}
.nav-dot .nav-tip{position:absolute;right:20px;top:50%;transform:translateY(-50%);background:var(--surf2);border:1px solid var(--line);padding:5px 10px;border-radius:6px;font-family:var(--mono);font-size:10px;color:var(--w);white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .15s}
.nav-dot:hover .nav-tip{opacity:1}

.kbd-hint{position:fixed;bottom:18px;right:22px;z-index:90;font-family:var(--mono);font-size:10px;color:var(--w4);letter-spacing:.1em;display:flex;align-items:center;gap:8px;opacity:.6}
.kbd-hint kbd{background:var(--w06);border:1px solid var(--w1);border-radius:4px;padding:3px 7px;color:var(--w7);font-size:10px}
@media(max-width:1200px){.kbd-hint{display:none}}

.slide-pad{flex:1;display:flex;flex-direction:column;justify-content:center;padding:84px 70px 96px;position:relative;z-index:2;max-width:1320px;margin:0 auto;width:100%;min-height:100vh}
@media(max-width:1400px){.slide-pad{padding:80px 54px 96px}}
@media(max-width:1100px){.slide-pad{padding:72px 32px 96px}}
@media(max-height:760px){.slide-pad{padding-top:60px;padding-bottom:84px}}
.slide-pad.center{justify-content:center}
.slide-pad.top{justify-content:flex-start}

.eyebrow{font-family:var(--mono);font-size:10px;letter-spacing:.26em;color:var(--soft);text-transform:uppercase;margin-bottom:18px;display:flex;align-items:center;gap:10px}
.eyebrow::before{content:'';width:32px;height:1px;background:var(--primary);flex:none}
.eyebrow .tnum{color:var(--w4)}
.hl{color:var(--soft)} .hl.c{color:var(--primary)}
.demo-h{font-size:clamp(32px,4.6vw,60px);font-weight:700;line-height:1.05;letter-spacing:-2.2px;margin-bottom:14px}
.demo-h.sm{font-size:clamp(28px,3.6vw,44px)}
.lead{font-size:18px;color:var(--w7);line-height:1.55;max-width:820px}
.lead b{color:var(--w);font-weight:600}

/* the big question slide */
.qmark{font-family:var(--mono);font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:var(--soft);margin-bottom:30px;display:flex;align-items:center;gap:12px}
.qmark::before{content:'';width:44px;height:1px;background:var(--primary)}
.bigq{font-size:clamp(34px,5.6vw,74px);font-weight:700;line-height:1.1;letter-spacing:-2.4px;max-width:26ch}
.bigq b{color:var(--soft);font-weight:700}
.qsub{margin-top:28px;font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--w4)}

.badge{display:inline-flex;align-items:center;gap:8px;padding:5px 12px;border-radius:30px;font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin-bottom:18px}
.badge.disc{background:var(--w06);border:1px solid var(--w1);color:var(--w6)}
.badge.scored{background:rgba(47,116,214,.12);border:1px solid rgba(47,116,214,.36);color:var(--soft)}
.badge.scored .ld{width:7px;height:7px;border-radius:50%;background:var(--primary);animation:livedot 1.4s ease-in-out infinite}
@keyframes livedot{0%,100%{box-shadow:0 0 0 0 rgba(47,116,214,.7)}70%{box-shadow:0 0 0 10px rgba(47,116,214,0)}}

.anchor{margin-bottom:8px;background:linear-gradient(135deg,rgba(47,116,214,.14),rgba(47,116,214,.02));border:1px solid rgba(47,116,214,.32);border-left:3px solid var(--primary);border-radius:0 12px 12px 0;padding:16px 22px;max-width:900px;font-size:17px;line-height:1.5;color:var(--w8)}
.anchor .al{font-family:var(--mono);font-size:9.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--soft);font-weight:600;display:block;margin-bottom:7px}
.anchor b{color:var(--w);font-weight:700}

/* build engine */
.b{opacity:0;transform:translateY(16px);transition:opacity .5s cubic-bezier(.2,.7,.2,1),transform .5s cubic-bezier(.2,.7,.2,1)}
.b.in{opacity:1;transform:none}
.b.step{opacity:1;transform:none}

/* cover */
#cover .stage,.coverstage{flex:1;display:flex;flex-direction:column;justify-content:center;padding:90px 70px 100px;position:relative;z-index:2;max-width:1320px;margin:0 auto;width:100%}
@media(max-width:1100px){.coverstage{padding:80px 32px 100px}}
.clock{font-family:var(--mono);font-size:11px;color:var(--soft);letter-spacing:.28em;text-transform:uppercase;margin-bottom:26px;display:flex;align-items:center;gap:12px}
.live-dot{width:8px;height:8px;border-radius:50%;background:var(--primary);animation:livedot 1.4s ease-in-out infinite}
.mega{font-size:clamp(44px,7vw,96px);font-weight:700;line-height:.98;letter-spacing:-3.4px}
.mega .accent{color:var(--soft)}
.covsub{margin-top:28px;font-size:19px;color:var(--w7);max-width:700px;line-height:1.5}
.covmeta{margin-top:38px;display:flex;gap:26px;flex-wrap:wrap;font-family:var(--mono);font-size:12px;color:var(--w5);letter-spacing:.06em}

/* roadmap / outcomes */
.road{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:28px;max-width:1100px}
@media(max-width:820px){.road{grid-template-columns:1fr}}
.road.one{grid-template-columns:1fr;max-width:820px}
.ritem{display:flex;gap:16px;align-items:flex-start;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012));border:1px solid var(--w1);border-radius:13px;padding:16px 18px}
.ritem .rn{font-family:var(--mono);font-size:15px;font-weight:600;color:var(--soft);width:34px;flex:none}
.ritem .rt{font-size:16.5px;font-weight:600;letter-spacing:-.2px;line-height:1.25}
.ritem .rd{font-size:13px;color:var(--w6);margin-top:4px;line-height:1.4}
.rtag{font-family:var(--mono);font-size:8.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;padding:3px 8px;border-radius:20px;margin-top:8px;display:inline-block}
.rtag.s{background:rgba(47,116,214,.16);border:1px solid rgba(47,116,214,.32);color:var(--soft)}
.rtag.d{background:var(--w06);border:1px solid var(--w1);color:var(--w5)}

/* three-card spread */
.spread-row{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px}
.spread-row.two{grid-template-columns:repeat(2,1fr);max-width:1000px}
.spread-row.four{grid-template-columns:repeat(4,1fr)}
@media(max-width:920px){.spread-row,.spread-row.two,.spread-row.four{grid-template-columns:1fr}}
.sc{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012));border:1px solid var(--w1);border-radius:16px;padding:22px 22px 20px;position:relative;overflow:hidden}
.sc .sic{font-size:26px;color:var(--soft);margin-bottom:14px}
.sc .sw{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--soft);margin-bottom:8px}
.sc .st{font-size:20px;font-weight:700;letter-spacing:-.4px;margin-bottom:8px;line-height:1.16}
.sc .sd{font-size:14.5px;color:var(--w7);line-height:1.5}
.sc .sd b{color:var(--w)}
.punch{margin-top:22px;font-size:22px;font-weight:700;letter-spacing:-.5px;line-height:1.34;max-width:980px}
.punch b{color:var(--soft)}
.punch .sm{display:block;font-size:15px;font-weight:500;color:var(--w6);margin-top:9px;letter-spacing:0}

/* term / definition */
.defbox{margin-top:24px;background:linear-gradient(135deg,rgba(0,74,163,.20),rgba(0,74,163,.04));border:1px solid rgba(47,116,214,.34);border-radius:16px;padding:24px 28px;max-width:1000px}
.defbox .dt{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--soft);font-weight:600;margin-bottom:12px}
.defbox .dd{font-size:22px;line-height:1.42;color:var(--w);font-weight:600;letter-spacing:-.4px}
.defbox .dd b{color:var(--soft)}
.keyline{margin-top:22px;background:rgba(47,116,214,.08);border:1px solid rgba(47,116,214,.28);border-radius:13px;padding:18px 22px;font-size:17px;font-weight:600;color:var(--w);max-width:1060px;line-height:1.4;letter-spacing:-.3px}
.keyline b{color:var(--soft)}

/* two-column compare */
.vs{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:26px;max-width:1120px}
@media(max-width:860px){.vs{grid-template-columns:1fr}}
.vcol{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012));border:1px solid var(--w1);border-radius:16px;padding:22px 24px}
.vcol.good{border-top:3px solid var(--green)}
.vcol.bad{border-top:3px solid var(--danger)}
.vcol .vh{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin-bottom:16px}
.vcol.good .vh{color:var(--green-lt)}
.vcol.bad .vh{color:var(--danger)}
.vcol ul{list-style:none;display:flex;flex-direction:column;gap:11px}
.vcol li{font-size:15.5px;color:var(--w8);line-height:1.4;display:flex;gap:11px}
.vcol li::before{font-family:var(--mono);font-size:13px;flex:none;margin-top:1px}
.vcol.good li::before{content:'+';color:var(--green)}
.vcol.bad li::before{content:'\2013';color:var(--danger)}

/* mini list */
.mini-list{margin-top:24px;display:flex;flex-direction:column;gap:10px;max-width:960px}
.mini-row{display:flex;gap:16px;align-items:flex-start;background:rgba(255,255,255,.028);border:1px solid var(--w1);border-radius:12px;padding:15px 19px}
.mini-row .mk{font-family:var(--mono);font-size:12px;font-weight:600;color:var(--soft);min-width:112px;flex:none;letter-spacing:.04em;padding-top:2px}
.mini-row .mv{font-size:15.5px;color:var(--w8);line-height:1.45}
.mini-row .mv b{color:var(--w);font-weight:600}

/* multiple choice check */
.mc{margin-top:24px;max-width:940px}
.mc-q{font-size:21px;font-weight:600;letter-spacing:-.4px;margin-bottom:16px;line-height:1.3}
.mc-opts{display:flex;flex-direction:column;gap:10px}
.mc-opt{text-align:left;background:rgba(255,255,255,.035);border:1px solid var(--w1);border-radius:12px;padding:15px 18px;font-family:var(--mf);font-size:16px;color:var(--w8);cursor:pointer;transition:all .16s;display:flex;gap:13px;align-items:center}
.mc-opt:hover{background:var(--w06);border-color:var(--w2)}
.mc-opt .mo-k{font-family:var(--mono);font-size:12px;font-weight:600;width:24px;height:24px;border-radius:6px;background:var(--w06);border:1px solid var(--w1);display:flex;align-items:center;justify-content:center;flex:none;color:var(--w6)}
.mc-opt.correct{background:rgba(61,200,115,.13);border-color:rgba(61,200,115,.5);color:#fff}
.mc-opt.correct .mo-k{background:var(--green);border-color:var(--green);color:#04220f}
.mc-opt.wrong{background:rgba(255,90,110,.12);border-color:rgba(255,90,110,.45)}
.mc-opt.wrong .mo-k{background:var(--danger);border-color:var(--danger);color:#2a0207}
.mc-fb{margin-top:14px;display:none;background:rgba(47,116,214,.08);border:1px solid rgba(47,116,214,.28);border-radius:12px;padding:16px 20px}
.mc-fb.show{display:block}
.mc-fb .fbh{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--soft);font-weight:600;margin-bottom:8px}
.mc-fb .fbt{font-size:16px;color:var(--w8);line-height:1.45}

/* lab task */
.labcard{margin-top:24px;background:linear-gradient(135deg,rgba(0,74,163,.18),rgba(0,74,163,.03));border:1px solid rgba(47,116,214,.34);border-radius:18px;padding:26px 30px;max-width:1060px}
.labcard .lh{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:18px}
.labcard .lnum{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;background:var(--primary);color:#fff;border-radius:20px;padding:5px 12px}
.labcard .ltime{font-family:var(--mono);font-size:11px;color:var(--w5);letter-spacing:.1em;text-transform:uppercase}
.labcard .lwhere{margin-left:auto;font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--light);background:rgba(255,255,255,.06);border:1px solid var(--w1);border-radius:20px;padding:5px 12px}
.labcard .lt{font-size:26px;font-weight:700;letter-spacing:-.7px;margin-bottom:16px;line-height:1.2}
.labsteps{list-style:none;display:flex;flex-direction:column;gap:12px;counter-reset:ls}
.labsteps li{counter-increment:ls;display:flex;gap:14px;font-size:16px;color:var(--w8);line-height:1.45}
.labsteps li::before{content:counter(ls);font-family:var(--mono);font-size:11px;font-weight:600;width:24px;height:24px;border-radius:50%;background:var(--w06);border:1px solid var(--w1);color:var(--soft);display:flex;align-items:center;justify-content:center;flex:none;margin-top:1px}
.labsteps li b{color:var(--w);font-weight:600}
.labgo{margin-top:20px;display:inline-flex;align-items:center;gap:10px;background:linear-gradient(135deg,var(--primary),var(--deepblue));color:#fff;border-radius:12px;padding:13px 22px;font-size:15px;font-weight:600;text-decoration:none;transition:all .18s}
.labgo:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(0,74,163,.6)}

/* MAP test placeholder */
.testbox{margin-top:26px;background:rgba(255,255,255,.03);border:1px dashed var(--w2);border-radius:18px;padding:30px 34px;max-width:900px;text-align:center}
.testbox .tl{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--soft);font-weight:600;margin-bottom:14px}
.testbox .tv{font-size:26px;font-weight:700;letter-spacing:-.6px;margin-bottom:12px}
.testbox .td{font-size:15.5px;color:var(--w6);line-height:1.5;max-width:520px;margin:0 auto}
.testbox .qr{margin:22px auto 6px;width:188px;height:188px;padding:12px;background:#fff;border-radius:14px;
  box-shadow:0 10px 34px rgba(0,0,0,.45)}
.testbox .qr svg{display:block;width:100%;height:100%;shape-rendering:crispEdges}
.testbox .qrcap{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--w4);margin-top:10px}
.testbox .tph{margin-top:20px;display:inline-flex;font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--w4);background:var(--w06);border:1px dashed var(--w2);border-radius:10px;padding:11px 18px}
.testbox a.tph{color:#fff;background:linear-gradient(135deg,var(--primary),var(--deepblue));border:1px solid rgba(255,255,255,.14);border-style:solid;text-decoration:none}

/* prompt / code block */
.pbox{margin-top:20px;background:rgba(0,0,0,.32);border:1px solid var(--w1);border-radius:14px;padding:20px 24px;max-width:1000px;font-family:var(--mono);font-size:14.5px;line-height:1.66;color:var(--w7);white-space:pre-wrap}
.pbox .pk{color:var(--soft);font-weight:600}
.pbox.ar{font-family:'IBM Plex Sans Arabic',var(--mono);direction:rtl;text-align:right;font-size:16px}
.pbox-lbl{margin-top:22px;font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--w4);font-weight:600}
.split2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px;max-width:1180px}
@media(max-width:900px){.split2{grid-template-columns:1fr}}
.split2 .pbox{margin-top:8px;max-width:none}

.close-punch{font-size:clamp(26px,3.4vw,46px);font-weight:700;letter-spacing:-1.6px;line-height:1.16;max-width:1060px;margin-top:8px}
.close-punch b{color:var(--soft)}
.src{margin-top:auto;padding-top:22px;font-family:var(--mono);font-size:10px;color:var(--w4);letter-spacing:.04em;line-height:1.5}
.src strong{color:var(--w6)}


/* ---- definition hero (What is AI) ---- */
.bigemoji{font-size:52px;line-height:1;margin-bottom:18px}
.defhero{margin-top:6px;background:linear-gradient(135deg,rgba(47,116,214,.16),rgba(47,116,214,.02));
  border:1px solid rgba(47,116,214,.3);border-left:3px solid var(--primary);border-radius:0 14px 14px 0;
  padding:22px 28px;max-width:1160px;font-size:22px;line-height:1.45;color:var(--w8);font-weight:400}
.defhero b{color:#fff;font-weight:700}
.frows{display:flex;flex-direction:column;gap:11px;margin-top:22px;max-width:1160px}
.frow{display:flex;align-items:center;gap:16px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012));
  border:1px solid var(--w1);border-radius:13px;padding:16px 22px}
.frow .fe{font-size:22px;flex:none;line-height:1}
.frow .ft{font-size:17px;color:var(--w7);line-height:1.4}
.frow .ft b{color:#fff;font-weight:700}
.closebar{margin-top:20px;background:linear-gradient(135deg,rgba(47,116,214,.14),rgba(47,116,214,.03));
  border:1px solid rgba(47,116,214,.3);border-radius:14px;padding:20px 26px;max-width:1160px;
  font-size:21px;font-weight:700;color:#fff;letter-spacing:-.4px;line-height:1.35}
.closebar b{color:var(--soft)}
.subline{margin-top:14px;font-size:19px;color:var(--w6);line-height:1.5;max-width:900px}

/* ---- use case: safe vs guardrails, plus an ethical risk bar ---- */
.uc{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:26px;max-width:1160px}
@media(max-width:860px){.uc{grid-template-columns:1fr}}
.ucol{border-radius:16px;padding:22px 24px}
.ucol.safe{background:linear-gradient(180deg,rgba(61,200,115,.10),rgba(61,200,115,.02));border:1px solid rgba(61,200,115,.34)}
.ucol.stop{background:linear-gradient(180deg,rgba(255,90,110,.09),rgba(255,90,110,.02));border:1px solid rgba(255,90,110,.32)}
.ucol .uh{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;
  margin-bottom:16px;display:flex;align-items:center;gap:9px}
.ucol.safe .uh{color:var(--green-lt)} .ucol.stop .uh{color:var(--danger)}
.ucol ul{list-style:none;display:flex;flex-direction:column;gap:12px}
.ucol li{font-size:16.5px;color:var(--w8);line-height:1.4;display:flex;gap:12px;align-items:flex-start}
.ucol li::before{flex:none;font-weight:700;font-size:15px;margin-top:1px}
.ucol.safe li::before{content:'\2713';color:var(--green)}
.ucol.stop li::before{content:'\2715';color:var(--danger)}
.ethbar{margin-top:18px;background:linear-gradient(135deg,rgba(233,196,106,.12),rgba(233,196,106,.02));
  border:1px solid rgba(233,196,106,.34);border-radius:14px;padding:18px 24px;max-width:1160px;
  font-size:16.5px;color:var(--w8);line-height:1.5}
.ethbar b{color:var(--amber);font-weight:700}

/* ---- side by side compare (Copilot) ---- */
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:24px;max-width:1160px}
@media(max-width:860px){.cmp{grid-template-columns:1fr}}
.cmp .cc{background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.014));
  border:1px solid var(--w1);border-radius:16px;padding:22px 24px}
.cmp .cc.hi{border-color:rgba(47,116,214,.4);background:linear-gradient(180deg,rgba(47,116,214,.13),rgba(47,116,214,.02))}
.cmp .ct{font-size:19px;font-weight:700;letter-spacing:-.4px;margin-bottom:6px}
.cmp .cs{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin-bottom:15px}
.cmp .cr{display:flex;gap:11px;font-size:15px;color:var(--w7);line-height:1.45;margin-bottom:11px}
.cmp .cr b{color:#fff;font-weight:600}
.cmp .cr::before{content:'\2022';color:var(--soft);flex:none}

/* ---- why-care card grid ---- */
.wc{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:26px}
@media(max-width:1080px){.wc{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.wc{grid-template-columns:1fr}}
.wcard{background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.014));
  border:1px solid var(--w1);border-radius:16px;padding:24px 22px}
.wcard .we{font-size:28px;line-height:1;margin-bottom:16px}
.wcard .wt{font-size:20px;font-weight:700;letter-spacing:-.4px;margin-bottom:9px}
.wcard .wd{font-size:14.5px;color:var(--w6);line-height:1.55}
.footline{margin-top:24px;font-size:18px;color:var(--w6);line-height:1.5}
.footline b{color:#fff;font-weight:600}

/* ---- autocomplete demo ---- */
.ac-wrap{margin-top:26px;max-width:840px}
.ac-screen{background:rgba(0,0,0,.42);border:1px solid var(--w2);border-radius:18px;padding:26px 28px 22px}
.ac-lbl{font-family:var(--mono);font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--w4);margin-bottom:16px}
.ac-line{font-size:26px;line-height:1.45;color:#fff;min-height:76px;font-weight:500;letter-spacing:-.4px}
.ac-line .acc{color:var(--soft)}
.ac-caret{display:inline-block;width:2px;height:26px;background:var(--primary);vertical-align:-4px;
  margin-left:2px;animation:accaret 1s step-end infinite}
@keyframes accaret{0%,50%{opacity:1}51%,100%{opacity:0}}
.ac-bar{margin-top:20px;padding-top:18px;border-top:1px solid var(--w1);display:flex;gap:10px;flex-wrap:wrap}
.ac-chip{flex:1;min-width:130px;text-align:center;background:var(--w06);border:1px solid var(--w1);
  border-radius:10px;padding:13px 12px;font-size:16px;color:var(--w7);transition:all .25s}
.ac-chip.hot{background:rgba(47,116,214,.26);border-color:var(--primary);color:#fff;transform:translateY(-3px)}

/* ---- break slide ---- */
.brk-pad{align-items:center;text-align:center}
.brk-h{font-size:clamp(38px,6vw,76px);font-weight:700;letter-spacing:-2.6px;line-height:1.05}
.brk-h b{color:var(--soft)}
.brk-sub{margin-top:20px;font-size:19px;color:var(--w6);max-width:620px;line-height:1.5}
.brk-pick{margin-top:40px;display:flex;gap:16px;flex-wrap:wrap;justify-content:center}
.brk-opt{background:linear-gradient(135deg,var(--primary),var(--deepblue));color:#fff;border:none;
  border-radius:16px;padding:26px 44px;cursor:pointer;font-family:var(--mf);transition:all .18s;
  box-shadow:0 12px 34px -10px rgba(0,74,163,.8)}
.brk-opt:hover{transform:translateY(-3px);box-shadow:0 18px 46px -10px rgba(0,74,163,.95)}
.brk-opt .bn{display:block;font-size:44px;font-weight:700;line-height:1;letter-spacing:-2px}
.brk-opt .bu{display:block;margin-top:8px;font-family:var(--mono);font-size:11px;letter-spacing:.2em;
  text-transform:uppercase;opacity:.8}
.brk-opt.alt{background:var(--w06);border:1px solid var(--w1);box-shadow:none}
.brk-opt.alt:hover{background:var(--w1);box-shadow:none}
.brk-note{margin-top:30px;font-family:var(--mono);font-size:11.5px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--w4)}

/* break timer */
.brkbtn{font-size:16px}
.break-pick{position:fixed;inset:0;z-index:300;display:none;align-items:center;justify-content:center;background:rgba(0,8,28,.78);backdrop-filter:blur(8px)}
.break-pick.on{display:flex}
.bp-card{background:linear-gradient(180deg,var(--surf2),var(--surf));border:1px solid var(--w1);border-radius:22px;padding:30px 30px 24px;width:min(440px,90vw);box-shadow:0 30px 80px rgba(0,0,0,.6);text-align:center}
.bp-h{font:700 24px/1.1 var(--mf);color:#fff;letter-spacing:-.5px}
.bp-sub{font:500 14px/1.5 var(--mf);color:var(--w6);margin:8px 0 22px}
.bp-chips{display:flex;gap:9px;justify-content:center;flex-wrap:wrap;margin-bottom:16px}
.bp-chip{background:var(--w06);border:1px solid var(--w1);color:#fff;border-radius:11px;padding:12px 16px;font:600 15px/1 var(--mono);cursor:pointer;transition:all .14s}
.bp-chip:hover{background:var(--primary);border-color:var(--primary);transform:translateY(-2px)}
.bp-custom{display:flex;gap:8px;margin-bottom:18px}
.bp-custom input{flex:1;min-width:0;background:var(--base);border:1.5px solid var(--w1);color:#fff;border-radius:11px;padding:12px 14px;font:600 15px/1 var(--mono)}
.bp-custom input:focus{outline:none;border-color:var(--primary)}
.bp-go{flex:none;background:linear-gradient(180deg,var(--primary),var(--deepblue));color:#fff;border:none;border-radius:11px;padding:0 18px;font:700 14px/1 var(--mf);cursor:pointer}
.bp-cancel{background:none;border:none;color:var(--w5);font:500 13px/1 var(--mf);cursor:pointer;padding:6px}
.bp-cancel:hover{color:var(--w8)}
.break-ov{position:fixed;inset:0;z-index:290;display:none;align-items:center;justify-content:center;background:var(--base);overflow:hidden}
.break-ov.on{display:flex}
.break-ov .brk{position:relative;z-index:2;text-align:center}
.brk-eye{font-family:var(--mono);font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--soft);margin-bottom:22px}
.brk-clock{font-family:var(--mono);font-size:clamp(70px,16vw,190px);font-weight:600;letter-spacing:-6px;line-height:1;color:#fff;text-shadow:0 0 60px rgba(47,116,214,.45)}
.brk-clock.over{color:var(--w5);text-shadow:none;animation:brkpulse 1.1s ease-in-out infinite}
@keyframes brkpulse{0%,100%{opacity:.45}50%{opacity:1}}
.brk-back{margin-top:18px;font-size:18px;color:var(--w6)}
.brk-back b{color:#fff}
.bo-cta{margin-top:26px;display:flex;gap:12px;justify-content:center}
.bo-btn{background:var(--w06);border:1px solid var(--w1);color:#fff;border-radius:12px;padding:13px 22px;font:600 14px/1 var(--mf);cursor:pointer;transition:all .14s}
.bo-btn:hover{background:var(--w1);transform:translateY(-2px)}
.bo-btn.end{background:linear-gradient(180deg,var(--primary),var(--deepblue));border-color:transparent}

/* blank + help */
#blank{position:fixed;inset:0;z-index:280;background:#000;display:none}
#blank.on{display:block}
#help{position:fixed;inset:0;z-index:285;background:rgba(0,8,28,.86);backdrop-filter:blur(10px);display:none;align-items:center;justify-content:center}
#help.on{display:flex}
#help .hc{background:linear-gradient(180deg,var(--surf2),var(--surf));border:1px solid var(--w1);border-radius:20px;padding:30px 34px;width:min(460px,90vw)}
#help h3{font-size:20px;font-weight:700;margin-bottom:18px;letter-spacing:-.4px}
#help .hrow{display:flex;justify-content:space-between;gap:20px;padding:9px 0;border-bottom:1px solid var(--w06);font-size:14px;color:var(--w7)}
#help .hrow:last-child{border-bottom:none}
#help kbd{background:var(--w06);border:1px solid var(--w1);border-radius:5px;padding:3px 8px;font-family:var(--mono);font-size:11px;color:var(--w8)}
"""

CHROME = r"""
<a class="deck-back" href="coded-aiet-day-1.html" title="Back to the Day 1 overview"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"></path></svg><span>Back</span></a>

<div id="prail-wrap"><div id="prail"></div></div>
<div class="nav-dots" id="nav-dots"></div>

<div class="deck-nav">
  <button class="nav-btn" onclick="prev()" title="Previous">&#8249;</button>
  <div class="nav-pos"><span class="cur" id="pos-cur">1</span><span class="tot"> / <span id="pos-tot">0</span></span></div>
  <button class="nav-btn" onclick="next()" title="Next">&#8250;</button>
  <div class="nav-divider"></div>
  <button class="nav-btn brkbtn" onclick="openBreak()" title="Start a break">&#9749;</button>
  <button class="nav-btn fs" onclick="toggleFs()" title="Full screen">&#9974;</button>
</div>

<div class="kbd-hint"><kbd>&rarr;</kbd> next <kbd>&larr;</kbd> back <kbd>F</kbd> full <kbd>?</kbd> help</div>

<div class="break-pick" id="breakPick">
  <div class="bp-card">
    <div class="bp-h">Take a break</div>
    <div class="bp-sub">How long?</div>
    <div class="bp-chips">
      <button class="bp-chip" data-min="5">5</button>
      <button class="bp-chip" data-min="10">10</button>
      <button class="bp-chip" data-min="15">15</button>
      <button class="bp-chip" data-min="20">20</button>
      <button class="bp-chip" data-min="30">30</button>
    </div>
    <div class="bp-custom"><input id="bpCustom" type="number" min="1" max="180" placeholder="minutes"><button class="bp-go" id="bpGo">Start</button></div>
    <button class="bp-cancel" id="bpCancel">Cancel</button>
  </div>
</div>

<div class="break-ov" id="breakOv">
  <div class="blob b1"></div><div class="blob b2"></div>
  <div class="brk">
    <div class="brk-eye" id="boEye">Break</div>
    <div class="brk-clock" id="boClock">00:00</div>
    <div class="brk-back" id="boBack"></div>
    <div class="bo-cta"><button class="bo-btn" id="boAdd">+5 min</button><button class="bo-btn end" id="boEnd">End break</button></div>
  </div>
</div>

<div id="blank"></div>
<div id="help"><div class="hc">
  <h3>Keyboard</h3>
  <div class="hrow"><span>Next slide</span><kbd>&rarr;</kbd></div>
  <div class="hrow"><span>Previous slide</span><kbd>&larr;</kbd></div>
  <div class="hrow"><span>Full screen</span><kbd>F</kbd></div>
  <div class="hrow"><span>Black the screen</span><kbd>B</kbd></div>
  <div class="hrow"><span>First / last slide</span><kbd>Home</kbd> <kbd>End</kbd></div>
  <div class="hrow"><span>Close anything</span><kbd>Esc</kbd></div>
</div></div>
"""

JS = r"""
var slides=[].slice.call(document.querySelectorAll('.slide'));
var total=slides.length,idx=0;
document.getElementById('pos-tot').textContent=total;
var dc=document.getElementById('nav-dots');
for(var i=0;i<total;i++){var d=document.createElement('button');
  d.className='nav-dot'+(i===0?' active':'')+(slides[i].dataset.sec?' sec':'');
  (function(n){d.onclick=function(){show(n);};})(i);
  var tip=document.createElement('span');tip.className='nav-tip';
  tip.textContent=(i+1)+'. '+(slides[i].dataset.title||slides[i].id);
  d.appendChild(tip);dc.appendChild(d);}
var dots=[].slice.call(dc.querySelectorAll('.nav-dot'));

/* ===== autocomplete demo (single-interval state machine) ===== */
var acTimer=null;
function acReset(s){
  if(acTimer){clearInterval(acTimer);acTimer=null;}
  var box=s.querySelector('.ac-demo');if(!box)return;
  var line=box.querySelector('.ac-line'),bar=box.querySelector('.ac-bar');
  var SEED='Thank you for ';
  var STEPS=[['your','the','taking'],['patience','time','help'],
             ['and','with','while'],['understanding','support','the delay'],
             ['.','while we fix it','on this one']];
  var TICK=70;                 /* ms per tick */
  var typed='',step=0,phase='seed',n=0;
  function paint(ghost){
    line.innerHTML=(typed||'&nbsp;')+(ghost?'<span class="acc">'+ghost+'</span>':'')+'<span class="ac-caret"></span>';}
  function chips(o,hot){bar.innerHTML=o.map(function(w,i){
    return '<span class="ac-chip'+(i===hot?' hot':'')+'">'+w+'</span>'}).join('')}
  function reset(){typed='';step=0;phase='seed';n=0;bar.innerHTML='';paint('');}
  reset();
  acTimer=setInterval(function(){
    n++;
    if(phase==='seed'){
      if(n<=SEED.length){typed=SEED.slice(0,n);paint('');}
      else if(n>SEED.length+4){phase='offer';n=0;}
      return;
    }
    if(phase==='offer'){                       /* chips appear, none chosen */
      if(n===1)chips(STEPS[step],-1);
      if(n>5){phase='pick';n=0;}
      return;
    }
    if(phase==='pick'){                        /* one lights up, ghost text shows */
      if(n===1){chips(STEPS[step],0);paint(STEPS[step][0]);}
      if(n>9){phase='commit';n=0;}
      return;
    }
    if(phase==='commit'){                      /* the word is accepted */
      if(n===1){var w=STEPS[step][0];typed+=w+(w==='.'?'':' ');paint('');step++;}
      if(n>3){phase=(step>=STEPS.length)?'hold':'offer';n=0;}
      return;
    }
    if(phase==='hold'){                        /* full sentence sits, then loop */
      if(n===1)bar.innerHTML='';
      if(n>32)reset();
      return;
    }
  },TICK);
}

function mcReset(s){[].slice.call(s.querySelectorAll('.mc-opts')).forEach(function(o){o.classList.remove('done');
  [].slice.call(o.querySelectorAll('.mc-opt')).forEach(function(b){b.classList.remove('correct','wrong');});});
  [].slice.call(s.querySelectorAll('.mc-fb')).forEach(function(f){f.classList.remove('show');f.innerHTML='';});}

function show(n){
  slides[idx].classList.remove('active');if(dots[idx])dots[idx].classList.remove('active');
  idx=(n+total)%total;var s=slides[idx];s.classList.add('active');
  if(dots[idx])dots[idx].classList.add('active');s.scrollTop=0;
  document.getElementById('pos-cur').textContent=idx+1;
  /* content shows on arrival */
  [].slice.call(s.querySelectorAll('.b')).forEach(function(el){
    el.classList.add('shown');el.classList.add(el.classList.contains('step')?'on':'in');});
  mcReset(s);
  acReset(s);
  var pr=document.getElementById('prail');
  if(pr)pr.style.width=(total>1?(idx/(total-1)*100):0)+'%';
}
function next(){if(idx<total-1)show(idx+1);}
function prev(){if(idx>0)show(idx-1);}
function toggleFs(){if(!document.fullscreenElement){document.documentElement.requestFullscreen().catch(function(){});}else{document.exitFullscreen();}}
function toggleBlank(){var b=document.getElementById('blank');if(b)b.classList.toggle('on');}
function toggleHelp(){var h=document.getElementById('help');if(h)h.classList.toggle('on');}
function closeOverlays(){var h=document.getElementById('help');if(h)h.classList.remove('on');
  var b=document.getElementById('blank');if(b)b.classList.remove('on');closeBreakPick();}
(function(){var h=document.getElementById('help');if(h)h.addEventListener('click',closeOverlays);
  var b=document.getElementById('blank');if(b)b.addEventListener('click',function(){toggleBlank();});})();

document.addEventListener('keydown',function(e){
  if(e.target.tagName==='INPUT')return;
  if(e.key==='b'||e.key==='B'||e.key==='.'){toggleBlank();e.preventDefault();return;}
  if(e.key==='?'||(e.shiftKey&&e.key==='/')){toggleHelp();e.preventDefault();return;}
  if(e.key==='Escape'){closeOverlays();e.preventDefault();return;}
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){next();e.preventDefault();}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){prev();e.preventDefault();}
  else if(e.key==='Home'){show(0);e.preventDefault();}
  else if(e.key==='End'){show(total-1);e.preventDefault();}
  else if(e.key==='f'||e.key==='F'){toggleFs();e.preventDefault();}
});
slides.forEach(function(s){s.addEventListener('click',function(e){
  if(e.target.closest('button,input,a,.mc-opt,.mc-opts,.brk-opt,.ac-screen'))return;next();});});

document.addEventListener('click',function(e){var b=e.target.closest('.brk-opt');
  if(b){e.stopPropagation();startBreak(+b.dataset.min);return;}
});
document.addEventListener('click',function(e){var opt=e.target.closest('.mc-opt');if(!opt)return;
  var box=opt.closest('.mc-opts');if(!box||box.classList.contains('done'))return;e.stopPropagation();
  box.classList.add('done');
  var correctBtn=box.querySelector('.mc-opt[data-k="1"]');
  if(opt.dataset.k==='1')opt.classList.add('correct');
  else{opt.classList.add('wrong');if(correctBtn)correctBtn.classList.add('correct');}
  var fb=box.parentNode.querySelector('.mc-fb');
  if(fb){fb.innerHTML='<div class="fbh">'+(opt.dataset.k==='1'?'Correct':'Not quite')+'</div><div class="fbt">'+(opt.dataset.fb||'')+'</div>';fb.classList.add('show');}
});

/* ===== on-demand BREAK timer ===== */
var boTimer=null,boLeft=0;
function _pad2(n){return (n<10?'0':'')+n;}
function _boFmt(s){return Math.floor(s/60)+':'+_pad2(s%60);}
function boRender(){var cl=document.getElementById('boClock');
  if(cl){cl.textContent=_boFmt(Math.max(0,boLeft));cl.classList.toggle('over',boLeft<=0);}
  var end=new Date(Date.now()+Math.max(0,boLeft)*1000);var bk=document.getElementById('boBack');
  if(bk)bk.innerHTML=(boLeft<=0?'Time is up. ':'Back at ')+'<b>'+_pad2(end.getHours())+':'+_pad2(end.getMinutes())+'</b>';}
function _boTick(){boLeft--;if(boLeft<=0){boLeft=0;boRender();
  var eye=document.getElementById('boEye');if(eye)eye.textContent='Break is over';
  if(boTimer){clearInterval(boTimer);boTimer=null;}return;}boRender();}
function _boRun(){if(boTimer)clearInterval(boTimer);boTimer=setInterval(_boTick,1000);}
function openBreak(){var p=document.getElementById('breakPick');if(p)p.classList.add('on');
  var c=document.getElementById('bpCustom');if(c)c.value='';}
function closeBreakPick(){var p=document.getElementById('breakPick');if(p)p.classList.remove('on');}
function startBreak(min){min=Math.round(min);if(!min||min<1)return;if(min>180)min=180;closeBreakPick();
  boLeft=min*60;var eye=document.getElementById('boEye');
  if(eye)eye.textContent=min+(min===1?' minute':' minutes');boRender();
  var o=document.getElementById('breakOv');if(o)o.classList.add('on');_boRun();}
function addBreak(){boLeft=Math.max(0,boLeft)+300;var eye=document.getElementById('boEye');
  if(eye)eye.textContent='Break extended';boRender();_boRun();}
function endBreak(){if(boTimer){clearInterval(boTimer);boTimer=null;}
  var o=document.getElementById('breakOv');if(o)o.classList.remove('on');}
(function(){
  [].slice.call(document.querySelectorAll('.bp-chip')).forEach(function(b){b.onclick=function(){startBreak(+b.dataset.min);};});
  var go=document.getElementById('bpGo');if(go)go.onclick=function(){startBreak(+(document.getElementById('bpCustom').value));};
  var cx=document.getElementById('bpCancel');if(cx)cx.onclick=closeBreakPick;
  var bc=document.getElementById('bpCustom');if(bc)bc.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();startBreak(+bc.value);}});
  var ad=document.getElementById('boAdd');if(ad)ad.onclick=addBreak;
  var en=document.getElementById('boEnd');if(en)en.onclick=endBreak;
  var pk=document.getElementById('breakPick');if(pk)pk.addEventListener('click',function(e){if(e.target===pk)closeBreakPick();});
})();
show(0);
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&'
         'family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&'
         'display=swap" rel="stylesheet">')


def qr_svg(url):
    """Inline SVG QR code for a URL. Built at generation time, so the deck
    stays self contained and works offline. High error correction, so a
    projector at the back of the room still scans."""
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
    q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=0)
    q.add_data(url)
    q.make(fit=True)
    m = q.get_matrix()
    n = len(m)
    d = ''.join('M%d %dh1v1h-1z' % (x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-label="QR code for %s">'
            '<rect width="%d" height="%d" fill="#fff"/><path d="%s" fill="#000"/></svg>' % (n, n, url, n, n, d))

def qr_block(url, caption="Scan with your phone, or use the button"):
    return '<div class="qr">' + qr_svg(url) + '</div><div class="qrcap">' + caption + '</div>'

def page(title, slides_html, back_href="coded-aiet-day-1.html"):
    chrome = CHROME.replace('coded-aiet-day-1.html', back_href)
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            "<title>" + title + "</title>\n" + FONTS + "\n<style>" + CSS + "</style>\n</head>\n<body>\n"
            + chrome + "\n" + slides_html + "\n<script>" + JS + "</script>\n</body>\n</html>\n")


def slide(sid, title, body, sec=False, center=False, bg=True):
    secattr = ' data-sec="1"' if sec else ''
    pad = 'slide-pad center' if center else 'slide-pad'
    grid = '<div class="bg-grid"></div><div class="blob b1"></div><div class="blob b2"></div>' if bg else ''
    return ('<section class="slide" id="' + sid + '" data-title="' + title + '"' + secattr + '>'
            + grid + '<div class="' + pad + '">' + body + '</div></section>\n')
