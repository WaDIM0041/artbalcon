import os
from PIL import Image, ImageOps

IMG_DIR = 'images'
MAX_SIDE = 2000
QUALITIES = [85, 80, 75, 70, 65, 60]

names = sorted(n for n in os.listdir(IMG_DIR) if n.lower().endswith(('.jpg', '.jpeg')))
use_webp = {}

for name in names:
    src = os.path.join(IMG_DIR, name)
    base = os.path.splitext(name)[0]
    dst = os.path.join(IMG_DIR, base + '.webp')
    jpg = os.path.getsize(src)
    img = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    if max(img.size) > MAX_SIDE:
        img.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    best_q = None
    best = None
    for q in QUALITIES:
        img.save(dst, 'WEBP', quality=q, method=6)
        size = os.path.getsize(dst)
        if best is None or size < best:
            best_q = q
            best = size
        if size < jpg:
            break
    img.save(dst, 'WEBP', quality=best_q, method=6)
    use_webp[base] = best < jpg
    if use_webp[base]:
        print('OK   %-18s %7d -> %7d  q%d' % (name, jpg, best, best_q))
    else:
        os.remove(dst)
        print('KEEP %-18s %7d  (webp %d)' % (name, jpg, best))

html = open('index.html', encoding='utf-8').read()
for name in names:
    base = os.path.splitext(name)[0]
    if use_webp[base]:
        html = html.replace('images/' + name, 'images/' + base + '.webp')
    else:
        html = html.replace('images/' + base + '.webp', 'images/' + name)
open('index.html', 'w', encoding='utf-8').write(html)
print('index.html updated')
