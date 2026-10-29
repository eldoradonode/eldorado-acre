document.documentElement.classList.add("js");
const bg=document.querySelector(".burger");bg&&bg.addEventListener("click",()=>{const o=document.querySelector(".links").classList.toggle("open");bg.setAttribute("aria-expanded",o)});
const tr=document.getElementById("track"),mk=document.getElementById("mk"),cur=document.getElementById("cur");
function render(){const l=PROPERTIES.filter(p=>!mk.value||REGION[p.country]===mk.value);
 tr.innerHTML=l.map(p=>cardHTML(p,cur.value)).join("")+'<aside class="locs"><h3>Explore properties in your preferred location</h3><p>Lagos, Abuja, London, Lisbon, Los Angeles and more.</p><a class="btn" href="buy">View Locations &rarr;</a></aside>'}
if(tr&&window.PROPERTIES){render();mk.addEventListener("change",render);cur.addEventListener("change",render);
 document.querySelectorAll("[data-dir]").forEach(b=>b.addEventListener("click",()=>tr.scrollBy({left:b.dataset.dir*270,behavior:"smooth"})))}
const f=document.querySelector(".search");
document.querySelectorAll(".tabs button").forEach(b=>b.addEventListener("click",()=>{document.querySelectorAll(".tabs button").forEach(x=>x.classList.toggle("on",x==b));f.action=b.dataset.a}));
if("IntersectionObserver"in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}}),{threshold:.12});document.querySelectorAll("[data-r]").forEach(el=>io.observe(el))}else document.querySelectorAll("[data-r]").forEach(el=>el.classList.add("in"));
if(document.querySelector("[data-sc-act]")&&window.ScrollCraft){if(ScrollCraft.reduce)document.querySelectorAll("[data-sc-span]").forEach(e=>e.setAttribute("data-sc-span","1"));ScrollCraft.mount(document.body)}
