import base64,os,shutil,json,zipfile
from tourdata import ORDER
h=open('index.html').read()
i=h.index('<body>\n<title>')+len('<body>\n'); assert h.endswith('</body></html>')
os.makedirs('pub',exist_ok=True); open('pub/index.html','w').write(h[i:-len('</body></html>')].rstrip()+"\n")
full='<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'+h[h.index('<style>'):]
out='/home/user/claude-code/vantageos-export'
shutil.rmtree(out,ignore_errors=True); os.makedirs(out+'/VantageOS/screens')
open(out+'/VantageOS/index.html','w').write(full)
fs=[f for m in ORDER.values() for f in m]
for f in fs: shutil.copy('screens/'+f,out+'/VantageOS/screens/'+f)
shots={f:'data:image/jpeg;base64,'+base64.b64encode(open('screens/'+f,'rb').read()).decode() for f in fs}
assert full.count('<script>')==1
sa=full.replace('<script>','<script>window.SHOTS='+json.dumps(shots)+';</script>\n<script>',1)
open(out+'/What-is-VantageOS.html','w').write(sa)
shutil.copy(out+'/What-is-VantageOS.html',out+'/VantageOS/What-is-VantageOS-standalone.html')
with zipfile.ZipFile(out+'/What-is-VantageOS.zip','w',zipfile.ZIP_DEFLATED) as z:
  for root,_,files in os.walk(out+'/VantageOS'):
    for fn in files:
      p=os.path.join(root,fn); z.write(p,os.path.relpath(p,out))
shutil.rmtree(out+'/VantageOS'); shutil.rmtree('site',ignore_errors=True); os.makedirs('site/screens')
shutil.copy('index.html','site/index.html')
for f in fs: shutil.copy('screens/'+f,'site/screens/'+f)
print(os.listdir(out))
