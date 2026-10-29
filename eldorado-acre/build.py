import re,glob
h=open('index.html').read()
TOP=h[h.index('<div class="top">'):h.index('</header>')+9].replace('class="on" href="/"','href="/"')
FOOT='''<footer><div class="wrap"><div><h4>Eldorado &amp; Acre</h4><p>Residential, commercial and land discovery across markets.</p><p><a href="tel:+2348096454731">+234 809 645 4731</a><a href="https://wa.me/2348096454731" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:daniel@eldoradonode.work">daniel@eldoradonode.work</a></p></div>
<div><h4>Explore</h4><a href="buy">Buy</a><a href="rent">Rent</a><a href="land">Land &amp; Plots</a><a href="commercial">Commercial</a><a href="developments">Developments</a></div>
<div><h4>Company</h4><a href="about">About</a><a href="contact">Contact</a><a href="list">List a Property</a></div>
<p class="fine">Portfolio concept. All listings, prices and images are illustrative samples and do not represent real properties for sale or rent. Exchange rates are illustrative.</p></div></footer>'''
def page(slug,title,desc,body,js,main_id=''):
    t=TOP.replace(f'<a href="{slug}">',f'<a class="on" href="{slug}">')
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | Eldorado &amp; Acre</title><meta name="description" content="{desc}"><meta property="og:title" content="{title} | Eldorado &amp; Acre"><link rel="canonical" href="/{slug}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css"><link rel="stylesheet" href="css/pages.css"></head><body>
{t}
<main{main_id}>{body}</main>
{FOOT}
<script src="data/properties.js"></script><script src="js/main.js"></script>{js}</body></html>'''
def img(n,a=''):return f'<img src="images/{n}.webp" srcset="images/{n}-640.webp 640w, images/{n}.webp 1376w" sizes="(max-width:860px) 100vw, 50vw" alt="{a}" width="1376" height="768">'
def fld(name,label,typ='text',req=False,opts=None,rows=0):
    r=' required' if req else '';e='<span class="err" role="alert"></span>' if req else ''
    if opts:return f'<label>{label}<select name="{name}" data-l="{label}">'+''.join(f'<option>{o}</option>' for o in opts)+'</select></label>'
    if rows:return f'<label>{label}<textarea name="{name}" data-l="{label}" rows="{rows}"{r}></textarea>{e}</label>'
    return f'<label>{label}<input name="{name}" type="{typ}" data-l="{label}"{r}>{e}</label>'
DONE='<div class="done" hidden><h3 tabindex="-1">Ready to send</h3><p>No mail service is connected to this site yet, so nothing has been sent. Choose how to send your message:</p><div class="btns"><a class="btn btn-g" data-wa target="_blank" rel="noopener">Send on WhatsApp</a><a class="btn btn-o" data-mail>Send by email</a><button type="button" class="lnk" data-edit>Edit message</button></div></div>'
def lst(mode,slug,title,eye,h1,lead,hero,alt,types,extra=''):
    ty=''.join(f'<option value="{v}">{t}</option>' for v,t in types)
    beds='<label>Bedrooms<select name="beds"><option value="">Any</option><option value="1">1+</option><option value="2">2+</option><option value="3">3+</option><option value="4">4+</option><option value="5">5+</option></select></label>' if mode!='commercial' else ''
    st='<label>For<select name="status"><option value="">Sale or rent</option><option value="sale">Sale</option><option value="rent">Rent</option></select></label>' if mode=='commercial' else ''
    pl='Monthly rent (approx. USD)' if mode=='rent' else 'Price (approx. USD)'
    body=f'''<section class="hd"><div class="wrap two"><div><p class="eyebrow">{eye}</p><h1>{h1}</h1><p class="body">{lead}</p></div><div class="ph">{img(hero,alt)}</div></div></section>
<section class="pg" style="padding-top:28px"><div class="wrap" id="app" data-mode="{mode}"><form id="ff" class="fbar" role="search"><details id="fd"><summary>Filters</summary><div><label>Location<input name="q" placeholder="City or country"></label><label>Type<select name="type"><option value="">Any type</option>{ty}</select></label>{st}{beds}<label>Min {pl}<input name="min" type="number" min="0" inputmode="numeric"></label><label>Max {pl}<input name="max" type="number" min="0" inputmode="numeric"></label><button class="btn btn-o" type="button" data-reset>Reset filters</button></div></details></form>
<div class="rbar"><p id="rc" aria-live="polite"></p><label>Sort <select id="sort"><option value="">Featured</option><option value="lo">Price: low to high</option><option value="hi">Price: high to low</option></select></label></div>
<div class="lg" id="lg"></div><p class="note">Illustrative sample listings. {extra}Prices are in each listing&rsquo;s local currency; use the currency selector for an approximate conversion.</p></div></section>'''
    return page(slug,title,f'{lead} Illustrative sample listings.',body,'<script src="js/listings.js"></script>')
W=[('house','Houses &amp; Duplexes'),('apartment','Apartments'),('land','Land')]
open('buy.html','w').write(lst('buy','buy','Buy Property','Buy','Homes, land and offices to buy.','Search sample properties for sale in Nigeria, the United States and Europe.','hero-lekki-duplex','Contemporary duplex at sunset',W+[('commercial','Commercial')]))
open('rent.html','w').write(lst('rent','rent','Rent Property','Rent','Places to rent, priced in local currency.','Rents are shown per year or per month as listed, never as purchase prices.','ny-apartment-living','Apartment living room with skyline views',[('house','Houses'),('apartment','Apartments')]))
open('commercial.html','w').write(lst('commercial','commercial','Commercial Property','Commercial','Offices and commercial land.','Sample commercial property. No returns or yields are shown because none are verified.','ng-abuja-office-exterior','Glazed office building',[('commercial','Offices &amp; buildings'),('land','Commercial land')],'No financial returns are shown or implied. '))
prop=page('property','Property','Property details.','<div id="pd"></div>','<script src="js/forms.js"></script><script src="js/property.js"></script>').replace('<div id="pd"></div>','<div id="pd"></div><dialog id="lb" aria-label="Photo viewer"><div class="lbw"><img id="lbi" alt="" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><p id="lbc"></p></div><button class="lbb" id="lbx" aria-label="Close viewer">&times;</button><button class="lbb" id="lbp" aria-label="Previous photo">&larr;</button><button class="lbb" id="lbn" aria-label="Next photo">&rarr;</button></dialog>')
prop=prop.replace('<script src="js/forms.js"></script><script src="js/property.js"></script>','<script src="js/property.js"></script><script src="js/forms.js"></script>')
open('property.html','w').write(prop)
cf='<form data-form="contact" data-title="Website enquiry" novalidate>'+fld('category','Enquiry category',opts=['Buying','Renting','Land','Commercial property','Listing a property','Something else'])+fld('name','Name','text',True)+fld('email','Email','email',True)+fld('phone','Phone (optional)','tel')+fld('ref','Property reference (optional)')+fld('message','Message','text',True,rows=5)+'<button class="btn btn-g" type="submit">Prepare message</button></form>'
open('contact.html','w').write(page('contact','Contact','Contact Eldorado &amp; Acre by phone, WhatsApp, email or message.',f'''<section class="hd"><div class="wrap"><p class="eyebrow">Contact</p><h1>Talk to us about a property.</h1></div></section><section class="pg" style="padding-top:24px"><div class="wrap ct"><div class="fwrap">{cf}{DONE}</div>
<aside><h2 style="font-size:1.8rem">Reach us directly</h2><p>Tel and WhatsApp</p><a href="tel:+2348096454731">+234 809 645 4731</a><a href="https://wa.me/2348096454731" target="_blank" rel="noopener">Message on WhatsApp</a><p>Email</p><a href="mailto:daniel@eldoradonode.work">daniel@eldoradonode.work</a><p class="note">The form prepares your message and lets you send it by WhatsApp or email. It is not delivered automatically.</p></aside></div></section>''','<script src="js/forms.js"></script>'))
lf='<form data-form="list" data-title="Property listing submission" novalidate>'+fld('name','Your name','text',True)+fld('email','Email','email',True)+fld('phone','Phone or WhatsApp','tel',True)+fld('type','Property type',opts=['House','Apartment','Land','Commercial','Development'])+fld('status','Listing for',opts=['Sale','Rent'])+fld('location','Location (city and area)','text',True)+fld('price','Asking price or rent, with currency','text',True)+fld('size','Size and key features (optional)',rows=3)+fld('desc','Description','text',True,rows=5)+'<button class="btn btn-g" type="submit">Prepare submission</button></form>'
open('list.html','w').write(page('list','List a Property','Submit your home, land or commercial property for review by Eldorado &amp; Acre.',f'''<section class="hd"><div class="wrap"><p class="eyebrow">For owners and authorised agents</p><h1>List your property.</h1></div></section><section class="pg" style="padding-top:24px"><div class="wrap ct"><div class="fwrap">{lf}{DONE}</div>
<aside><h2 style="font-size:1.8rem">What happens next</h2><ol class="steps"><li>Complete the form. It prepares a message with your details.</li><li>Send it by WhatsApp or email, and add your photos there.</li><li>We review it. Nothing is published automatically.</li></ol><p class="note">This is a concept site with no live listing system, so submitting does not create a listing. Only submit a property you own or are authorised to represent.</p></aside></div></section>''','<script src="js/forms.js"></script>'))
open('404.html','w').write(page('404','Page not found','The page you are looking for does not exist.','<section class="hd"><div class="wrap empty"><h1>Page not found</h1><p>That page does not exist.</p><a class="btn btn-g" href="/">Back to home</a></div></section>',''))
for f in glob.glob('*.html'):
    s=open(f).read();s=re.sub(r'<footer>.*?</footer>',lambda m:FOOT,s,count=1,flags=re.S);open(f,'w').write(s)
print(sorted(glob.glob('*.html')))
