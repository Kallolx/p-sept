# -*- coding: utf-8 -*-
"""Convert every PNG/JPG/JPEG under assets/images to WebP, update every
reference in *.html/*.css/*.js (fixing any stale extension mismatches
along the way), then delete the original raster files."""
import glob
import os
import re

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

IMG_EXTS = ('.png', '.jpg', '.jpeg')
converted = []  # (old_path_posix, new_path_posix)

for path in glob.glob('assets/images/**/*', recursive=True):
    if not os.path.isfile(path):
        continue
    stem, ext = os.path.splitext(path)
    if ext.lower() not in IMG_EXTS:
        continue
    webp_path = stem + '.webp'
    posix_old = path.replace('\\', '/')
    posix_new = webp_path.replace('\\', '/')
    if os.path.exists(webp_path):
        print('SKIP (webp already exists):', webp_path)
        converted.append((posix_old, posix_new))
        continue
    img = Image.open(path)
    if img.mode in ('P',):
        img = img.convert('RGBA')
    img.save(webp_path, 'WEBP', quality=88, method=6)
    print('converted:', path, '->', webp_path)
    converted.append((posix_old, posix_new))

# Build a stem-based rename map so a reference to the WRONG existing
# extension (e.g. html says .jpg but the file on disk was actually .png)
# still gets fixed to the correct new .webp path.
stem_map = {}
for old, new in converted:
    stem = os.path.splitext(old)[0]
    stem_map[stem] = new

pattern = re.compile(r'(assets/images/[a-zA-Z0-9_/\-\.]+?)\.(png|jpg|jpeg)', re.IGNORECASE)

def repl(m):
    stem = m.group(1)
    return stem_map.get(stem, m.group(0))

text_files = glob.glob('*.html') + glob.glob('js/*.js') + glob.glob('css/*.css')
changed_files = []
for f in text_files:
    s = open(f, encoding='utf-8').read()
    new_s = pattern.sub(repl, s)
    if new_s != s:
        open(f, 'w', encoding='utf-8', newline='').write(new_s)
        changed_files.append(f)

print()
print('reference-updated files:', changed_files)

# delete the original raster files now that everything points to .webp
deleted = 0
for old, new in converted:
    if os.path.exists(old) and os.path.exists(new):
        os.remove(old)
        deleted += 1
print('deleted originals:', deleted)
