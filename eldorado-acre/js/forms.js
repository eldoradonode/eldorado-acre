document.querySelectorAll("form[data-form]").forEach(f=>{f.noValidate=true;const box=f.closest(".fwrap"),done=box.querySelector(".done"),ref=new URLSearchParams(location.search).get("ref");
if(ref&&f.elements.ref)f.elements.ref.value=ref;
f.addEventListener("submit",e=>{e.preventDefault();let ok=true,first=null;
f.querySelectorAll("[required]").forEach(i=>{const em=i.type==="email",bad=!i.value.trim()||(em&&!/^\S+@\S+\.\S+$/.test(i.value.trim())),m=i.parentElement.querySelector(".err");i.setAttribute("aria-invalid",bad);if(m)m.textContent=bad?(em&&i.value.trim()?"Enter a valid email address.":"This field is required."):"";if(bad){ok=false;first=first||i}});
if(!ok){first.focus();return}
const lines=["Eldorado & Acre: "+f.dataset.title];[...f.elements].forEach(i=>{if(i.name&&i.value.trim()&&i.type!=="hidden"||i.name==="ref"&&i.value)lines.push((i.dataset.l||i.name)+": "+i.value.trim())});
const txt=lines.join("\n");done.querySelector("[data-wa]").href="https://wa.me/"+CONTACT.wa+"?text="+encodeURIComponent(txt);
done.querySelector("[data-mail]").href="mailto:"+CONTACT.email+"?subject="+encodeURIComponent(lines[0])+"&body="+encodeURIComponent(txt);
f.hidden=true;done.hidden=false;done.querySelector("h3").focus()});
done.querySelector("[data-edit]").addEventListener("click",()=>{done.hidden=true;f.hidden=false;f.querySelector("input,select,textarea").focus()})});
