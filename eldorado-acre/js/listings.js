(function(){const mode=document.getElementById("app").dataset.mode,f=document.getElementById("ff"),g=document.getElementById("lg"),mk=document.getElementById("mk"),cur=document.getElementById("cur"),rc=document.getElementById("rc"),so=document.getElementById("sort"),q=new URLSearchParams(location.search);
["q","type","min","max","beds","status"].forEach(k=>{if(f.elements[k]&&q.get(k))f.elements[k].value=q.get(k)});
if(q.get("price")&&f.elements.min){const a=q.get("price").split("-");f.elements.min.value=a[0]||"";f.elements.max.value=a[1]||""}
const base=p=>mode==="buy"?p.status==="sale":mode==="rent"?p.status==="rent":(p.kind==="commercial"||(p.kind==="land"&&p.use==="Commercial")),mo=p=>p.per==="year"?p.usd/12:p.usd;
function run(){const v=k=>f.elements[k]?f.elements[k].value.trim():"",t=v("q").toLowerCase(),mn=parseFloat(v("min"))||0,mx=parseFloat(v("max"))||Infinity,b=parseInt(v("beds"))||0;
let l=PROPERTIES.filter(base).filter(p=>(!t||(p.city+" "+p.title+" "+COUNTRY[p.country]).toLowerCase().indexOf(t)>-1)&&(!v("type")||p.kind===v("type"))&&(!v("status")||p.status===v("status"))&&(!mk.value||REGION[p.country]===mk.value)&&(!b||(p.beds||0)>=b)&&(mode==="rent"?mo(p):p.usd)>=mn&&(mode==="rent"?mo(p):p.usd)<=mx);
if(so.value==="lo")l.sort((a,c)=>a.usd-c.usd);if(so.value==="hi")l.sort((a,c)=>c.usd-a.usd);
rc.textContent=l.length+(l.length==1?" property":" properties");
g.innerHTML=l.length?l.map(p=>cardHTML(p,cur.value)).join(""):'<div class="empty"><h3>No properties match</h3><p>Try a wider price range or a different location.</p><button class="btn btn-o" type="button" id="rs">Reset filters</button></div>';}
f.addEventListener("input",run);f.addEventListener("submit",e=>e.preventDefault());so.addEventListener("change",run);mk.addEventListener("change",run);cur.addEventListener("change",run);
document.addEventListener("click",e=>{if(e.target.id==="rs"||e.target.closest("[data-reset]")){f.reset();so.value="";run()}});
const d=document.getElementById("fd");if(d&&innerWidth>860)d.open=true;run()})();
