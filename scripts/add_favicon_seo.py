# -*- coding: utf-8 -*-
"""Add favicon links + the extra SEO meta tags the old kamrulhasan.site head
used (application-name, author, keywords, creator, publisher, googlebot,
category, og:image:alt), matching its pattern for every page here."""
import glob
import re

KEYWORDS = ("Kamrul Hasan,Kamrul Hasan Kallol,Softune,Software Developer,"
            "Full-stack Developer,Next.js Developer,React Developer,"
            "TypeScript Developer,Dhaka,Bangladesh,portfolio,"
            "software developer portfolio,full-stack portfolio")

FAVICON_BLOCK = '''  <link rel="icon" href="/favicon/favicon.ico" sizes="any" />
  <link rel="icon" href="/favicon/favicon-16x16.png" sizes="16x16" type="image/png" />
  <link rel="icon" href="/favicon/favicon-32x32.png" sizes="32x32" type="image/png" />
  <link rel="apple-touch-icon" href="/favicon/apple-touch-icon.png" sizes="180x180" type="image/png" />
  <link rel="manifest" href="/favicon/site.webmanifest" />
'''

MORE_META_TMPL = '''  <meta name="application-name" content="Kamrul Hasan" />
  <meta name="author" content="Kamrul Hasan" />
  <meta name="keywords" content="{keywords}" />
  <meta name="creator" content="Kamrul Hasan" />
  <meta name="publisher" content="Kamrul Hasan" />
  <meta name="googlebot" content="index, follow, max-video-preview:-1, max-image-preview:large, max-snippet:-1" />
  <meta name="category" content="portfolio" />
'''

OG_ALT_LINE = '  <meta property="og:image:alt" content="{alt}" />\n'

files = glob.glob('*.html')
changed = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    orig = s

    # 1) extra meta block, right after the robots line
    if 'name="application-name"' not in s:
        s = s.replace(
            '  <meta name="robots" content="index, follow" />\n',
            '  <meta name="robots" content="index, follow" />\n' + MORE_META_TMPL.format(keywords=KEYWORDS),
            1,
        )

    # 2) og:image:alt, right after og:image:height
    if 'og:image:alt' not in s:
        m = re.search(r'<title>(.*?)</title>', s)
        title = m.group(1) if m else 'Kamrul Hasan'
        s = s.replace(
            '  <meta property="og:image:height" content="630" />\n',
            '  <meta property="og:image:height" content="630" />\n' + OG_ALT_LINE.format(alt=title + ' preview'),
            1,
        )

    # 3) favicon links, right before the Google Fonts preconnect block
    if 'favicon/favicon.ico' not in s:
        s = s.replace(
            '  <link rel="preconnect" href="https://fonts.googleapis.com" />\n',
            FAVICON_BLOCK + '  <link rel="preconnect" href="https://fonts.googleapis.com" />\n',
            1,
        )

    if s != orig:
        open(f, 'w', encoding='utf-8', newline='').write(s)
        print(f, 'updated')
        changed += 1

print('total files changed:', changed)
