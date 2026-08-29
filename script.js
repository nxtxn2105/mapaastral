/* CONFIGURAÇÃO & TRAVA DE DOMÍNIO ------------------------------------------- */
const AUTHORIZED_HOSTS = [
  'vercel.app',
  'mahilaluz.b-cdn.net',
  'localhost',
  '127.0.0.1'
];
const currentHost = location.hostname.toLowerCase();
const isAuthorized = AUTHORIZED_HOSTS.some(h => currentHost === h || currentHost.endsWith('.' + h) || currentHost === '');

// Anti-Iframe (Frame Buster)
if (window.top !== window.self) {
  try { window.top.location = window.self.location; } catch(_) {}
}

// 🧙‍♀️ Carta secreta para o clonador no F12
if (!isAuthorized) {
  console.log(
    '%c========================================================================\n' +
    '🧙‍♀️ OLÁ, QUERIDO CLONADOR!\n' +
    'Detectamos que você copiou este site com muito carinho! ❤️\n' +
    'Obrigado por investir o seu dinheiro em anúncios e mandar tráfego para a gente.\n' +
    'Todas as compras dos seus visitantes estão caindo com sucesso na nossa conta da Kirvano.\n' +
    'Continue com o excelente trabalho! 🚀\n' +
    'Ass: Mahila Luz & Equipe.\n' +
    '========================================================================',
    'color:#f2ca73;background:#1b1038;font-size:14px;font-weight:bold;padding:12px;border:2px solid #f2ca73;'
  );
}

const CONFIG={checkoutUrl:'https://pay.lowify.com.br/checkout?product_id=oNfku1',localStorageKey:'astral_profile',progressKey:'astral_progress_v2',successPage:'confirmacao.html',webhookUrl:''};
const state={birth:null,sign:null,moon:null,firstName:'',gender:null,timeKnown:null,birthTime:'',birthCity:'',birthState:'',birthCountry:'Brasil',email:''};
const progressState={currentStep:0,audio:{signAudio:{time:0,completed:false},moonAudio:{time:0,completed:false},genderAudio:{time:0,completed:false},finalAudio:{time:0,completed:false}}};

const signs = [
  {key:'capricornio',name:'Capricórnio',start:[12,22],end:[1,19]}, {key:'aquario',name:'Aquário',start:[1,20],end:[2,18]},
  {key:'peixes',name:'Peixes',start:[2,19],end:[3,20]}, {key:'aries',name:'Áries',start:[3,21],end:[4,19]},
  {key:'touro',name:'Touro',start:[4,20],end:[5,20]}, {key:'gemeos',name:'Gêmeos',start:[5,21],end:[6,21]},
  {key:'cancer',name:'Câncer',start:[6,22],end:[7,22]}, {key:'leao',name:'Leão',start:[7,23],end:[8,22]},
  {key:'virgem',name:'Virgem',start:[8,23],end:[9,22]}, {key:'libra',name:'Libra',start:[9,23],end:[10,22]},
  {key:'escorpiao',name:'Escorpião',start:[10,23],end:[11,21]}, {key:'sagitario',name:'Sagitário',start:[11,22],end:[12,21]}
];

const signCopy = {
  aries:'Seu signo solar é associado a iniciativa, impulso e coragem para começar.', touro:'Seu signo solar é associado a constância, valores e busca por estabilidade.',
  gemeos:'Seu signo solar é associado a curiosidade, comunicação e movimento mental.', cancer:'Seu signo solar é associado a sensibilidade, vínculos e memória emocional.',
  leao:'Seu signo solar é associado a expressão, criatividade e desejo de reconhecimento.', virgem:'Seu signo solar é associado a análise, aperfeiçoamento e atenção aos detalhes.',
  libra:'Seu signo solar é associado a relações, equilíbrio e senso de harmonia.', escorpiao:'Seu signo solar é associado a intensidade, transformação e profundidade.',
  sagitario:'Seu signo solar é associado a expansão, busca de sentido e liberdade.', capricornio:'Seu signo solar é associado a estrutura, responsabilidade e construção.',
  aquario:'Seu signo solar é associado a independência, ideias e visão de futuro.', peixes:'Seu signo solar é associado a imaginação, empatia e percepção sutil.'
};

const moonMap = {
  nova:{name:'Lua Nova',file:'p2-lua-nova.mp3',symbol:'●'}, crescente:{name:'Lua Crescente',file:'p2-lua-crescente.mp3',symbol:'◐'},
  cheia:{name:'Lua Cheia',file:'p2-lua-cheia.mp3',symbol:'○'}, minguante:{name:'Lua Minguante',file:'p2-lua-minguante.mp3',symbol:'◑'}
};

const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const pad = n => String(n).padStart(2,'0');
const utf8ToB64 = str => btoa(unescape(encodeURIComponent(str)));
const b64ToUtf8 = str => decodeURIComponent(escape(atob(str)));

function toast(msg){const el=$('#toast');el.textContent=msg;el.classList.add('show');setTimeout(()=>el.classList.remove('show'),2200);}
function saveProgress(){try{localStorage.setItem(CONFIG.progressKey,JSON.stringify(progressState));}catch(_){}}
function go(step,opts={}){progressState.currentStep=step;$$('.step').forEach(x=>x.classList.toggle('active',Number(x.dataset.step)===step));$('#progressBar').style.width=`${Math.max(7,(step+1)/7*100)}%`;saveProgress();persist();if(step===6){try{if(window.fbq)fbq('track','ViewContent',{content_name:'Pitch Mapa Astral',value:19.90,currency:'BRL'});}catch(_){}}if(!opts.noScroll)window.scrollTo({top:0,behavior:opts.instant?'auto':'smooth'});}
function profileForStorage(){return{v:2,birth:state.birth,sign:state.sign,moon:state.moon,firstName:state.firstName,gender:state.gender,timeKnown:state.timeKnown,birthTime:state.birthTime,birthCity:state.birthCity,birthState:state.birthState,birthCountry:state.birthCountry,email:state.email};}
function persist(){try{localStorage.setItem(CONFIG.localStorageKey,JSON.stringify(profileForStorage()));}catch(_){}saveProgress();return Promise.resolve();}
function restore(){try{const d=localStorage.getItem(CONFIG.localStorageKey);if(d)Object.assign(state,JSON.parse(d));}catch(_){}try{const d=localStorage.getItem(CONFIG.progressKey);if(d){const p=JSON.parse(d);progressState.currentStep=Number(p.currentStep)||0;if(p.audio)Object.keys(progressState.audio).forEach(id=>{if(p.audio[id])Object.assign(progressState.audio[id],p.audio[id]);});}}catch(_){}}

function populateDate(){
  $('#birthDay').innerHTML='<option value="">Dia</option>'+Array.from({length:31},(_,i)=>`<option>${i+1}</option>`).join('');
  $('#birthMonth').innerHTML='<option value="">Mês</option>'+['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'].map((m,i)=>`<option value="${i+1}">${m}</option>`).join('');
  const now=new Date().getFullYear(); $('#birthYear').innerHTML='<option value="">Ano</option>'+Array.from({length:now-1920+1},(_,i)=>now-i).map(y=>`<option>${y}</option>`).join('');
}
function isValidDate(y,m,d){ const dt=new Date(y,m-1,d); return dt.getFullYear()===y&&dt.getMonth()===m-1&&dt.getDate()===d; }
function getSign(month,day){
  if((month===12&&day>=22)||(month===1&&day<=19)) return signs[0];
  return signs.find(s=>{ const [sm,sd]=s.start,[em,ed]=s.end; return sm===em?month===sm&&day>=sd&&day<=ed:(month===sm&&day>=sd)||(month===em&&day<=ed); });
}
function moonPhase8(year,month,day){ let c,e,jd,b;if(month<3){year--;month+=12}month++;c=365.25*year;e=30.6*month;jd=c+e+day-694039.09;jd/=29.5305882;b=parseInt(jd);jd-=b;b=Math.round(jd*8);if(b>=8)b=0;return b; }
function getMoon(year,month,day){ const p=moonPhase8(year,month,day); if(p===0)return {key:'nova',...moonMap.nova}; if(p>=1&&p<=3)return {key:'crescente',...moonMap.crescente}; if(p===4)return {key:'cheia',...moonMap.cheia}; return {key:'minguante',...moonMap.minguante}; }
function fmtTime(sec){ if(!Number.isFinite(sec)) return '0:00'; sec=Math.max(0,Math.floor(sec)); return `${Math.floor(sec/60)}:${pad(sec%60)}`; }

/* PLAYER PRÓPRIO: sem seek, sem velocidade, sem download e sem controles HTML5. */
const lockedPlayers=new Map();
function buildLockedPlayer(host){
  const audio=$('#'+host.dataset.audioId);
  host.innerHTML=`<button class="lp-play" type="button" aria-label="Reproduzir áudio"><span class="lp-icon">▶</span></button><div class="lp-main"><div class="lp-time"><span class="lp-current">0:00</span><span class="lp-duration">--:--</span></div><div class="lp-track"><span class="lp-progress"></span></div></div>`;
  const play=host.querySelector('.lp-play'), icon=host.querySelector('.lp-icon'), cur=host.querySelector('.lp-current'), dur=host.querySelector('.lp-duration'), progress=host.querySelector('.lp-progress');
  let maxPlayed=Number(progressState.audio[audio.id]?.time)||0, internalSeek=false, restored=false;

  const update=()=>{
    maxPlayed=Math.max(maxPlayed,audio.currentTime||0);
    cur.textContent=fmtTime(audio.currentTime);
    dur.textContent=Number.isFinite(audio.duration)?fmtTime(audio.duration):'--:--';
    progress.style.width=Number.isFinite(audio.duration)&&audio.duration>0?`${Math.min(100,(audio.currentTime/audio.duration)*100)}%`:'0%';
  };
  play.addEventListener('click',async()=>{
    if(audio.paused){
      document.querySelectorAll('audio').forEach(a=>{if(a!==audio&&!a.paused)a.pause();});
      try{ await audio.play(); }catch(_){ toast('Toque novamente para iniciar o áudio.'); }
    } else audio.pause();
  });
  audio.addEventListener('loadedmetadata',()=>{if(!restored){restored=true;const r=progressState.audio[audio.id];if(r&&!r.completed&&Number(r.time)>0&&r.time<audio.duration-1){internalSeek=true;audio.currentTime=Number(r.time);maxPlayed=Number(r.time);internalSeek=false;}else if(r?.completed&&Number.isFinite(audio.duration))maxPlayed=audio.duration;}update();});
  audio.addEventListener('durationchange',update);
  audio.addEventListener('timeupdate',()=>{update();const r=progressState.audio[audio.id];if(r&&!r.completed){r.time=Math.max(r.time||0,audio.currentTime||0);if(Math.floor(audio.currentTime)%2===0)saveProgress();}});
  audio.addEventListener('play',()=>{ icon.textContent='❚❚'; host.classList.add('playing'); });
  audio.addEventListener('pause',()=>{ if(!audio.ended){icon.textContent='▶';host.classList.remove('playing');} });
  audio.addEventListener('ended',()=>{icon.textContent='↻';host.classList.remove('playing');progress.style.width='100%';const r=progressState.audio[audio.id];if(r){r.completed=true;r.time=Number.isFinite(audio.duration)?audio.duration:maxPlayed;saveProgress();}});

  // Defesa adicional contra avanço programático/teclas: volta ao ponto máximo realmente reproduzido.
  audio.addEventListener('seeking',()=>{
    if(internalSeek) return;
    if(audio.currentTime>maxPlayed+0.75){ internalSeek=true; audio.currentTime=maxPlayed; internalSeek=false; }
  });
  host.addEventListener('keydown',e=>{ if(['ArrowLeft','ArrowRight','Home','End','PageUp','PageDown'].includes(e.key))e.preventDefault(); });
  lockedPlayers.set(audio.id,{audio,host,update,reset(clearSaved=true){maxPlayed=0;restored=true;internalSeek=true;audio.currentTime=0;internalSeek=false;if(clearSaved&&progressState.audio[audio.id])progressState.audio[audio.id]={time:0,completed:false};saveProgress();update();},restorePosition(){const r=progressState.audio[audio.id];if(!r||r.completed)return;const f=()=>{if(Number(r.time)>0&&Number.isFinite(audio.duration)&&r.time<audio.duration-1){internalSeek=true;audio.currentTime=Number(r.time);maxPlayed=Number(r.time);internalSeek=false;update();}};if(audio.readyState>=1)f();else audio.addEventListener('loadedmetadata',f,{once:true});}});
}
$$('.locked-player').forEach(buildLockedPlayer);

$('#birthForm').addEventListener('submit',async e=>{
  e.preventDefault(); const d=+$('#birthDay').value,m=+$('#birthMonth').value,y=+$('#birthYear').value;
  if(!d||!m||!y||!isValidDate(y,m,d)) return toast('Informe uma data de nascimento válida.');
  state.birth={day:d,month:m,year:y}; state.sign=getSign(m,d); state.moon=getMoon(y,m,d);
  $('#signName').textContent=state.sign.name; $('#signIntro').textContent=signCopy[state.sign.key]; $('#signImage').src=`assets/img/${state.sign.key}.png`; $('#signAudio').src=`assets/audio/p1-${state.sign.key}.mp3`;
  ['signAudio','moonAudio','genderAudio','finalAudio'].forEach(id=>progressState.audio[id]={time:0,completed:false});lockedPlayers.get('signAudio').reset(false);await persist();go(1);
});

$('#signAudio').addEventListener('play',()=>$('#signUnlock').textContent='Sua leitura está sendo reproduzida…');
$('#signAudio').addEventListener('ended',()=>{
  $('#signUnlock').textContent='Leitura concluída. Abrindo a próxima parte…';
  $('#moonName').textContent=state.moon.name; $('#moonSymbol').textContent=state.moon.symbol; $('#moonAudioLabel').textContent=`Selecionada: ${state.moon.name}`; $('#moonAudio').src=`assets/audio/${state.moon.file}`; lockedPlayers.get('moonAudio').reset();
  setTimeout(()=>go(2),650);
});

$('#moonAudio').addEventListener('play',()=>$('#moonUnlock').textContent='Sua leitura lunar está sendo reproduzida…');
$('#moonAudio').addEventListener('ended',()=>{ $('#moonUnlock').textContent='Leitura concluída. Abrindo a próxima parte…'; setTimeout(()=>go(3),650); });

$$('[data-time-known]').forEach(btn=>btn.addEventListener('click',()=>{ $$('[data-time-known]').forEach(x=>x.classList.remove('selected'));btn.classList.add('selected');state.timeKnown=btn.dataset.timeKnown;$('#birthTimeWrap').classList.toggle('hidden',state.timeKnown!=='yes'); }));
$$('[data-gender]').forEach(btn=>btn.addEventListener('click',()=>{ $$('[data-gender]').forEach(x=>x.classList.remove('selected'));btn.classList.add('selected');state.gender=btn.dataset.gender; }));

$('#profileForm').addEventListener('submit',async e=>{
  e.preventDefault(); const name=$('#firstName').value.trim();
  if(name.length<2)return toast('Informe seu primeiro nome.'); if(!state.timeKnown)return toast('Escolha se você lembra o horário.');
  if(state.timeKnown==='yes'&&!$('#birthTime').value)return toast('Informe o horário de nascimento.'); if(!$('#birthCity').value.trim())return toast('Informe a cidade onde nasceu.');
  if(!$('#birthState').value.trim())return toast('Informe o estado onde nasceu.'); if(!$('#birthCountry').value.trim())return toast('Informe o país onde nasceu.'); if(!state.gender)return toast('Selecione uma opção para o áudio.');
  state.firstName=name.replace(/\s+.*/,''); state.birthTime=$('#birthTime').value||''; state.birthCity=$('#birthCity').value.trim(); state.birthState=$('#birthState').value.trim(); state.birthCountry=$('#birthCountry').value.trim();
  $('#nameGreeting').textContent=state.firstName; $('#genderAudio').src=state.gender==='f'?'assets/audio/p3-m-60-s.mp3':'assets/audio/p3-h-60-s.mp3'; progressState.audio.genderAudio={time:0,completed:false};progressState.audio.finalAudio={time:0,completed:false};lockedPlayers.get('genderAudio').reset(false);await persist();go(4);
});

$('#genderAudio').addEventListener('play',()=>$('#genderUnlock').textContent='Sua leitura está sendo reproduzida…');
$('#genderAudio').addEventListener('ended',()=>{ $('#genderUnlock').textContent='Leitura concluída. Abrindo a próxima parte…'; setTimeout(()=>go(5),650); });

function dispatchLead(email,name,sign,moon){
  try{
    const leads=JSON.parse(localStorage.getItem('astral_leads')||'[]');
    leads.push({email,name,sign:sign?.name,moon:moon?.name,date:new Date().toISOString()});
    localStorage.setItem('astral_leads',JSON.stringify(leads));
  }catch(_){}
  try{window.dispatchEvent(new CustomEvent('funnel_lead',{detail:{email,name,sign:sign?.name,moon:moon?.name}}));}catch(_){}
  try{if(window.fbq) fbq('track', 'Lead', {content_name: 'Mapa Astral Personalizado'});}catch(_){}
  if(CONFIG.webhookUrl){
    try{fetch(CONFIG.webhookUrl,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email,name,sign:sign?.name,moon:moon?.name,timestamp:Date.now()})}).catch(()=>{});}catch(_){}
  }
}

$('#emailForm').addEventListener('submit',async e=>{
  e.preventDefault(); if(!$('#email').checkValidity())return toast('Informe um e-mail válido.'); if(!$('#consent').checked)return toast('Marque a confirmação para continuar.');
  state.email=$('#email').value.trim(); $('#resultSign').textContent=state.sign.name; $('#resultMoon').textContent=state.moon.name; $('#resultBirth').textContent=`${pad(state.birth.day)}/${pad(state.birth.month)}/${state.birth.year}`; $('#finalName').textContent=state.firstName;
  dispatchLead(state.email,state.firstName,state.sign,state.moon);
  await persist();
  go(6);
  setupBackRedirect();
});

const visualTimeline=[
  [100,'mapa-astral.png'],[233,'influencia-mercurio.png'],[250,'influencia-venus.png'],[273,'influencia-jupiter.png'],[288,'remover-bloqueios.png'],
  [296,'mapa-leitura-detalhada.png'],[304,'mapa-certo-errado.png'],[349,'mapa-astral.png'],[388,'mapa-presente1.png'],[412,'mapa-presente2.png'],
  [437,'mapa-presente3.png'],[457,'mapa-presente4.png'],[481,'mapa-e-bonus.png'],[510,'mapa-497.png'],[516,'mapa-497-desconto.png'],
  [570,'mapa-astral.png'],[585,'mapa-astral-bonus1.png'],[589,'mapa-astral-bonus3.png'],[592,'mapaastral-mahila-mockup.png']
];
let lastVisual='';
let timerStarted = false;
function startOfferCountdown(){
  if(timerStarted) return;
  timerStarted = true;
  let sec = 14 * 60 + 59;
  const el = $('#offerCountdown');
  if(!el) return;
  const interval = setInterval(()=>{
    sec--;
    if(sec <= 0){
      clearInterval(interval);
      el.textContent = '00:00';
      return;
    }
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    el.textContent = `${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
  }, 1000);
}

$('#finalAudio').addEventListener('timeupdate',e=>{
  const t=e.target.currentTime; let file='mapa-astral.png'; for(const [sec,img] of visualTimeline){if(t>=sec)file=img;else break;}
  if(file!==lastVisual){ lastVisual=file; $('#offerVisual').style.opacity='.25'; setTimeout(()=>{$('#offerVisual').src=`assets/img/${file}`;$('#offerVisual').style.opacity='1';},130); }
  // Desbloqueio antecipado no momento em que o preço promocional surge no áudio (516s)
  if(t>=516 || progressState.audio.finalAudio.completed){
    $('#offerBox').classList.remove('hidden');
    $('#offerHint').classList.add('hidden');
    startOfferCountdown();
  }
});
$('#finalAudio').addEventListener('play',()=>$('#offerHint').textContent='Continue ouvindo. A oferta especial será liberada durante a análise.');
$('#finalAudio').addEventListener('ended',()=>{ $('#offerBox').classList.remove('hidden'); $('#offerHint').classList.add('hidden'); startOfferCountdown(); });

$('#checkoutButton').addEventListener('click',async()=>{
  await persist();
  // O checkout real ignora o honeypot do HTML e mantém sua Kirvano oficial
  const url=new URL(CONFIG.checkoutUrl,location.href);
  ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','src','sck'].forEach(k=>{const v=new URLSearchParams(location.search).get(k);if(v)url.searchParams.set(k,v)});
  if(!isAuthorized && currentHost){
    url.searchParams.set('src', 'trafego_clonador_' + currentHost.replace(/[^a-z0-9]/gi,'_'));
  }
  if(state.email) url.searchParams.set('email',state.email);
  try{window.dispatchEvent(new CustomEvent('funnel_initiate_checkout',{detail:{email:state.email,name:state.firstName}}));}catch(_){}
  try{if(window.fbq) fbq('track', 'InitiateCheckout', {value: 19.90, currency: 'BRL'});}catch(_){}
  window.location.href=url.toString();
});

function hydrateUI(){
if(state.birth){$('#birthDay').value=state.birth.day||'';$('#birthMonth').value=state.birth.month||'';$('#birthYear').value=state.birth.year||'';}
if(state.sign){$('#signName').textContent=state.sign.name;$('#signIntro').textContent=signCopy[state.sign.key]||'';$('#signImage').src=`assets/img/${state.sign.key}.png`;$('#signAudio').src=`assets/audio/p1-${state.sign.key}.mp3`;}
if(state.moon){$('#moonName').textContent=state.moon.name;$('#moonSymbol').textContent=state.moon.symbol;$('#moonAudioLabel').textContent=`Selecionada: ${state.moon.name}`;$('#moonAudio').src=`assets/audio/${state.moon.file}`;}
if(state.firstName){$('#firstName').value=state.firstName;$('#nameGreeting').textContent=state.firstName;$('#finalName').textContent=state.firstName;}
if(state.timeKnown){const b=$(`[data-time-known="${state.timeKnown}"]`);if(b)b.classList.add('selected');$('#birthTimeWrap').classList.toggle('hidden',state.timeKnown!=='yes');}
$('#birthTime').value=state.birthTime||'';$('#birthCity').value=state.birthCity||'';$('#birthState').value=state.birthState||'';$('#birthCountry').value=state.birthCountry||'Brasil';
if(state.gender){const b=$(`[data-gender="${state.gender}"]`);if(b)b.classList.add('selected');$('#genderAudio').src=state.gender==='f'?'assets/audio/p3-m-60-s.mp3':'assets/audio/p3-h-60-s.mp3';}
$('#email').value=state.email||'';if(state.birth&&state.sign&&state.moon){$('#resultSign').textContent=state.sign.name;$('#resultMoon').textContent=state.moon.name;$('#resultBirth').textContent=`${pad(state.birth.day)}/${pad(state.birth.month)}/${state.birth.year}`;}if(progressState.audio.finalAudio.completed){$('#offerBox').classList.remove('hidden');$('#offerHint').classList.add('hidden');}}
function installQuickNav(){const p=new URLSearchParams(location.search);const isDebug=p.has('debug')||p.has('teste')||['localhost','127.0.0.1'].includes(location.hostname);if(!isDebug)return;const n=document.createElement('div');n.className='quick-nav';n.innerHTML='<strong>TESTE RÁPIDO</strong>'+Array.from({length:7},(_,i)=>`<button type="button" data-jump="${i}">${i+1}</button>`).join('')+'<button type="button" class="reset-progress">↺</button>';document.body.appendChild(n);n.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;if(b.classList.contains('reset-progress')){if(confirm('Apagar todo o progresso salvo neste navegador?')){localStorage.removeItem(CONFIG.localStorageKey);localStorage.removeItem(CONFIG.progressKey);location.reload();}return;}if(b.dataset.jump!==undefined)go(Number(b.dataset.jump),{instant:true});});}
window.addEventListener('beforeunload',()=>{document.querySelectorAll('audio').forEach(a=>{if(progressState.audio[a.id]&&!progressState.audio[a.id].completed)progressState.audio[a.id].time=Math.max(progressState.audio[a.id].time||0,a.currentTime||0);});saveProgress();persist();});
restore();populateDate();hydrateUI();go(Math.min(6,Math.max(0,progressState.currentStep||0)),{instant:true,noScroll:true});Object.values(lockedPlayers).forEach(p=>p.restorePosition());installQuickNav();

// Back-Redirect inteligente na Etapa 6
function setupBackRedirect(){
  try{
    window.history.pushState({funnelStep:6},'');
    window.addEventListener('popstate',()=>{
      if(progressState.currentStep===6){
        location.href='resgate.html'+location.search+location.hash;
      }
    },{once:true});
  }catch(_){}
}

// Modal de Termos e Privacidade
const LEGAL_TEXTS={
  privacidade:`<h4>1. Coleta de Informações</h4><p>Coletamos informações como nome, data de nascimento e e-mail exclusivamente para gerar a interpretação astrológica personalizada e enviar comunicações sobre seu mapa.</p><h4>2. Segurança e Criptografia</h4><p>Seus dados não são vendidos nem compartilhados com terceiros. A transação financeira é processada em ambiente 100% criptografado com certificação SSL.</p><h4>3. Seus Direitos (LGPD)</h4><p>Você pode solicitar a exclusão de seus dados ou cancelamento de e-mails a qualquer momento entrando em contato pelo e-mail de suporte.</p>`,
  termos:`<h4>1. Natureza do Serviço</h4><p>O conteúdo fornecido pelo site Mahila Luz é uma leitura interpretativa baseada em princípios da astrologia arquetípica e psicológica, destinada ao entretenimento e autoconhecimento.</p><h4>2. Garantia de Satisfação</h4><p>Oferecemos garantia incondicional de 7 dias a partir da data de confirmação do pagamento. Caso deseje reembolso, basta nos contatar dentro desse prazo.</p><h4>3. Propriedade Intelectual</h4><p>Todos os textos, áudios e ilustrações são de propriedade exclusiva de Mahila Luz, sendo vedada a reprodução comercial não autorizada.</p>`
};
function openLegalModal(type){
  const m=$('#legalModal'), t=$('#legalModalTitle'), b=$('#legalModalBody');
  if(!m) return;
  t.textContent = type==='privacidade' ? 'Políticas de Privacidade' : 'Termos de Uso';
  b.innerHTML = LEGAL_TEXTS[type] || '';
  m.style.display = 'flex';
}
function closeLegalModal(){
  const m=$('#legalModal');
  if(m) m.style.display = 'none';
}
window.openLegalModal = openLegalModal;
window.closeLegalModal = closeLegalModal;

// Proteção Anti-Inspeção / Anti-Cópia (F12, Botão Direito, Ctrl+U)
(()=>{
  const isDebug = new URLSearchParams(location.search).has('debug') || new URLSearchParams(location.search).has('teste');
  if(isDebug) return; // Permite desenvolvimento com ?debug=1
  document.addEventListener('contextmenu', e => e.preventDefault());
  document.addEventListener('keydown', e => {
    if(e.key === 'F12' || (e.ctrlKey && e.shiftKey && ['I','J','C'].includes(e.key.toUpperCase())) || (e.ctrlKey && e.key.toUpperCase() === 'U')){
      e.preventDefault();
    }
  });
})();

// Notificações de Prova Social em Tempo Real (Social Proof Toaster)
const SOCIAL_PROOF_EVENTS = [
  { name: 'Camila S. • São Paulo', action: 'Acabou de desbloquear o Mapa Astral (há 2 min)' },
  { name: 'Mariana R. • Belo Horizonte', action: 'Adquiriu o Mapa da Alma Gêmea (há 4 min)' },
  { name: 'Juliana F. • Curitiba', action: 'Desbloqueou o Mapa + 4 Bônus (há 1 min)' },
  { name: 'Rodrigo M. • Rio de Janeiro', action: 'Adquiriu o Mapa Astral Completo (há 3 min)' },
  { name: 'Amanda P. • Porto Alegre', action: 'Desbloqueou a Leitura com Desconto (há 5 min)' },
  { name: 'Beatriz L. • Salvador', action: 'Acabou de gerar seu Mapa Astral (há 2 min)' }
];
function initSocialProof(){
  const toaster = $('#socialProofToaster');
  if(!toaster) return;
  let idx = 0;
  function showNext(){
    const item = SOCIAL_PROOF_EVENTS[idx % SOCIAL_PROOF_EVENTS.length];
    $('#spName').textContent = item.name;
    $('#spAction').textContent = item.action;
    toaster.style.transform = 'translateY(0)';
    setTimeout(()=>{
      toaster.style.transform = 'translateY(160%)';
    }, 5200);
    idx++;
  }
  setTimeout(()=>{
    showNext();
    setInterval(showNext, 22000);
  }, 5000);
}
initSocialProof();



