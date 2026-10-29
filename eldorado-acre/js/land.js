(function(){const u=new URLSearchParams(location.search).get("use")||"",g=document.getElementById("lg"),mk=document.getElementById("mk"),cur=document.getElementById("cur");
document.querySelectorAll("#lf a").forEach(a=>a.classList.toggle("on",a.dataset.u===u));
function r(){const l=PROPERTIES.filter(p=>p.kind==="land"&&(!u||p.use.toLowerCase()===u)&&(!mk.value||REGION[p.country]===mk.value));
g.innerHTML=l.length?l.map(p=>cardHTML(p,cur.value)).join(""):'<p class="note">No plots match these filters. Try another market or <a href="land"><u>view all land</u></a>.</p>'}
r();mk.addEventListener("change",r);cur.addEventListener("change",r)})();
