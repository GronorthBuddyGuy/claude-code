
  /* ---------- Tabs ---------- */
  const TABS=["work","research","music"];
  function showTab(id,scroll){
    TABS.forEach(t=>{
      $("#"+t).hidden=t!==id;
      $("#t-"+t).setAttribute("aria-selected",t===id);
    });
    if(scroll){const top=$("#"+id).getBoundingClientRect().top+window.scrollY-70;if(window.scrollY>top)window.scrollTo(0,top)}
  }
  function fromHash(scroll){
    const h=location.hash.slice(1);
    if(TABS.includes(h))return showTab(h,scroll);
    const el=h&&document.getElementById(h);
    const panel=el&&el.closest(".tabpanel");
    showTab(panel?panel.id:"work",false);
    if(el)el.scrollIntoView();
  }
  window.addEventListener("hashchange",()=>fromHash(true));
  fromHash(false);

  /* ---------- Research: pathway ---------- */
  const STEPS=[
    {t:"Chronic stress or trauma",s:"The trigger",
     p:"Long-running stress, trauma or another neurological insult puts the body's survival systems on alert. The hypothesis is that in IPF this alert never fully stands down.",
     ev:[["Chronic activation of the stress system shifts immune signalling toward persistent inflammation.","Elenkov & Chrousos, Ann N Y Acad Sci, 2004"],
         ["Stress has short-term benefits for immune defence but long-term costs when it becomes chronic.","Dhabhar, Immunol Res, 2014"]]},
    {t:"The hippocampal brake fails",s:"Feedback breaks down",
     p:"The hippocampus normally tells the hypothalamus to shut the stress response off once a threat has passed. Under chronic stress that feedback weakens.",
     ev:[["People with PTSD have measurably smaller hippocampal volume, in a study pooling many sites.","Logue et al., Biol Psychiatry, 2018"],
         ["The HPA stress response is governed by negative feedback that limits how long it runs.","Herman et al., Compr Physiol, 2016"]]},
    {t:"The stress axis stays switched on",s:"HPA and sympathetic overdrive",
     p:"Without the brake, the hypothalamic–pituitary–adrenal axis and the sympathetic nervous system stay active: the body is held in fight-or-flight.",
     ev:[["Sustained sympathetic and HPA activity alters cytokine production and immune balance.","Elenkov & Chrousos, 2004; Herman et al., 2016"]]},
    {t:"TGF-β1 rises",s:"The fibrosis signal",
     p:"Chronic stress mediators push immune signalling toward TGF-β1, the master regulator of fibrosis, which instructs cells to build scar matrix.",
     ev:[["Chronic stress stimulates a pro-fibrotic pathway in both lung and heart in animal studies.","Chen et al., Sci Rep, 2015"],
         ["TGF-β is the central driver of lung fibrosis and a leading therapeutic target.","Fernandez & Eickelberg, Proc Am Thorac Soc, 2012"]]},
    {t:"Fibroblasts lay down collagen",s:"Repair with no off switch",
     p:"Fibroblasts turn into collagen-producing myofibroblasts and keep building matrix, as if healing a wound that is no longer there.",
     ev:[["Removing the TGF-β type II receptor from lung epithelium protects mice from induced lung fibrosis.","Li et al., J Clin Invest, 2011"]]},
    {t:"The lungs scar",s:"Idiopathic pulmonary fibrosis",
     p:"The end result is progressive scarring of the lung with no ongoing injury to explain it: the “idiopathic” part of IPF.",
     ev:[["Stress alone, with no physical injury, produced collagen scarring in the hearts of rats in a PTSD model.","Rorabaugh et al., Stress, 2020"],
         ["The airways are richly supplied by vagal sensory nerves that take part in injury responses.","Mazzone & Undem, Physiol Rev, 2016"]]}
  ];
  const SIDE={t:"The thyroid–lung axis",s:"A systemic modifier",side:true,
     p:"The brain also controls the thyroid through TSH. Low thyroid function tracks with worse IPF, and restoring thyroid hormone reversed fibrosis in mice, which points to a whole-body signal rather than a lung-only problem.",
     ev:[["Thyroid disease is common in IPF and predicts survival.","Oldham et al., Chest, 2015"],
         ["Inhaled thyroid hormone reversed established lung fibrosis in mice by improving mitochondrial function in lung cells.","Yu et al., Nat Med, 2018"]]};
  const chainEl=$("#pwChain"),sideEl=$("#pwSide"),card=$("#pwCard");
  if(chainEl){
    const btn=(x,i,n)=>`<button class="pwbtn" role="tab" id="pw${i}" aria-controls="pwCard" aria-selected="false" data-i="${i}"><span class="n">${n}</span><span><b>${x.t}</b><small>${x.s}</small></span></button>`;
    chainEl.innerHTML=STEPS.map((x,i)=>`<li>${btn(x,i,i+1)}</li>`).join("");
    sideEl.innerHTML=`<p class="lab">Acts alongside steps 4–5</p>${btn(SIDE,"s","T")}`;
    const pick=i=>{
      const x=i==="s"?SIDE:STEPS[+i];
      document.querySelectorAll(".pwbtn").forEach(b=>b.setAttribute("aria-selected",b.dataset.i==String(i)));
      card.className="pw-card"+(x.side?" side":"");
      card.setAttribute("aria-labelledby","pw"+i);
      card.innerHTML=`<p class="eyebrow">${x.side?"Modifier":"Step "+(+i+1)+" of "+STEPS.length} · ${x.s}</p><h3>${x.t}</h3><p>${x.p}</p><div class="ev"><p class="eyebrow">Evidence</p>${x.ev.map(e=>`<p>${e[0]}<cite>${e[1]}</cite></p>`).join("")}</div>`;
    };
    document.querySelector(".pw").addEventListener("click",e=>{const b=e.target.closest(".pwbtn");if(b)pick(b.dataset.i)});
    pick(0);
  }

  /* ---------- Research: papers on Academia.edu ---------- */
  // Add each paper's title as t once known; links open on Academia.edu.
  const PUBS=[
    {id:"175880032",t:""},
    {id:"165634148",t:""},
    {id:"165013257",t:""},
    {id:"164999688",t:""}
  ];
  const pubs=$("#pubs");
  if(pubs)pubs.innerHTML=PUBS.map((x,i)=>`<a href="https://academia.edu/resource/work/${x.id}" target="_blank" rel="noopener"><b>${x.t||"Paper "+(i+1)+" on Academia.edu"}</b><span>Read on Academia.edu ↗</span></a>`).join("");

  /* ---------- Music ---------- */
  // Add links here to show the "Tracks & mixes" section, e.g.
  // {t:"Track title",s:"Mix · 2024",u:"https://soundcloud.com/..."}
  const TRACKS=[];
  if(TRACKS.length){
    $("#listen").hidden=false;
    $("#tracks").innerHTML=TRACKS.map(x=>`<a href="${x.u}" target="_blank" rel="noopener"><b>${x.t}</b><span>${x.s}</span></a>`).join("");
  }
  const STAGES=[
    {t:"Capture",p:"Getting the performance down cleanly: mic choice and placement, gain staging, and room sound, in the studio, on stage or in the field.",k:["Mic placement","Gain staging","Field recording"],w:{amp:.55,noise:.35,comp:0,trim:0}},
    {t:"Edit",p:"Choosing the best takes, tightening timing, cleaning noise and clicks, and cutting to picture when there is one.",k:["Comping","Timing","Noise repair"],w:{amp:.55,noise:.12,comp:0,trim:.18}},
    {t:"Mix",p:"Balancing every element so the song or scene reads: levels, EQ, compression, space and movement.",k:["Balance","EQ & dynamics","Space & depth"],w:{amp:.62,noise:.05,comp:.35,trim:.12}},
    {t:"Master",p:"Final polish for release: consistent loudness, tonal balance across speakers, and delivery formats for each platform.",k:["Loudness","Translation","Formats"],w:{amp:.82,noise:.03,comp:.8,trim:.08}},
    {t:"Deliver",p:"Stems, final mixes and synced audio, labelled and handed off so the client can release, broadcast or publish with no surprises.",k:["Stems","Sync to picture","Handoff"],w:{amp:.82,noise:.03,comp:.8,trim:.08,marks:true}}
  ];
  const chain=$("#chain"),ccard=$("#chainCard"),wave=$("#wave");
  if(chain){
    chain.innerHTML=STAGES.map((x,i)=>`${i?'<span class="arrow" aria-hidden="true">→</span>':""}<button role="tab" id="st${i}" aria-controls="chainCard" aria-selected="false" data-i="${i}">${x.t}</button>`).join("");
    let W=STAGES[0].w,cur={...W},phase=0;
    const reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const ctx=wave.getContext("2d");
    function draw(){
      const dpr=window.devicePixelRatio||1,w=wave.clientWidth,h=wave.clientHeight;
      if(wave.width!==Math.round(w*dpr)){wave.width=Math.round(w*dpr);wave.height=Math.round(h*dpr)}
      ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,w,h);
      for(const k in W)if(typeof W[k]==="number")cur[k]+=(W[k]-cur[k])*.12;
      const mid=h/2,N=Math.max(80,Math.floor(w/3));
      ctx.strokeStyle="#1F2A40";ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(0,mid);ctx.lineTo(w,mid);ctx.stroke();
      ctx.fillStyle="rgba(255,176,32,.9)";
      for(let i=0;i<N;i++){
        const x=i/N;
        if(x<cur.trim*.5||x>1-cur.trim*.5)continue;
        let env=Math.abs(Math.sin(x*9+phase*.6))*.6+Math.abs(Math.sin(x*23-phase))*.4;
        env=env*(1-cur.comp)+cur.comp*(.75+.25*env);
        const n=(Math.sin(i*12.9898+phase*3)*43758.5453%1)*cur.noise;
        const a=Math.min(1,cur.amp*env+Math.abs(n))*(h*.46);
        ctx.fillRect(x*w,mid-a,Math.max(1,w/N-1),a*2);
      }
      if(W.marks){ctx.fillStyle="#38BDF8";[.25,.5,.75].forEach(m=>ctx.fillRect(m*w,6,2,h-12))}
      if(!reduce){phase+=.02;requestAnimationFrame(draw)}
    }
    const pickStage=i=>{
      const x=STAGES[i];W=x.w;
      chain.querySelectorAll("button").forEach(b=>b.setAttribute("aria-selected",b.dataset.i==i));
      ccard.setAttribute("aria-labelledby","st"+i);
      ccard.innerHTML=`<p class="eyebrow">Stage ${i+1} of ${STAGES.length}</p><h3>${x.t}</h3><p>${x.p}</p><div class="tags">${x.k.map(k=>`<span>${k}</span>`).join("")}</div>`;
      if(reduce){cur={...W};draw()}
    };
    chain.addEventListener("click",e=>{const b=e.target.closest("button");if(b)pickStage(+b.dataset.i)});
    pickStage(0);draw();
    if(reduce)window.addEventListener("resize",draw);
  }
