# -*- coding: utf-8 -*-
import re

DOMAIN = 'https://www.kamrulhasan.site'

PAGES = {
    'index.html': {
        'path': '/', 'type': 'website',
        'title': 'Kamrul H. - Full-Stack Software Engineer',
        'desc': 'Full-stack software engineer building reliable, scalable products. Founder of Softune. 150+ projects, 40+ clients.',
    },
    'about.html': {
        'path': '/about.html', 'type': 'profile',
        'title': 'About - Kamrul H.',
        'desc': 'About Kamrul Hasan Kallol - full-stack software engineer and founder of Softune.',
    },
    'works.html': {
        'path': '/works.html', 'type': 'website',
        'title': 'Works - Kamrul H.',
        'desc': 'Selected software projects by Kamrul Hasan Kallol - full-stack platforms, backend systems and automation.',
    },
    'work-hoteleasy.html': {
        'path': '/work-hoteleasy.html', 'type': 'article',
        'title': 'HotelEasy - Kamrul H.',
        'desc': 'HotelEasy - a hotel management platform built by Kamrul Hasan Kallol for Sea View Resort.',
    },
    'work-softunebd.html': {
        'path': '/work-softunebd.html', 'type': 'article',
        'title': 'Softunebd - Kamrul H.',
        'desc': 'Softunebd - a no-code e-commerce platform for Bangladesh, built and run by Kamrul Hasan Kallol.',
    },
    'work-wonderscore.html': {
        'path': '/work-wonderscore.html', 'type': 'article',
        'title': 'Wonderscore - Kamrul H.',
        'desc': 'Wonderscore - an AI search marketing platform Kamrul Hasan Kallol helped build as a Python developer at Wonder AI.',
    },
    'work-zinetic.html': {
        'path': '/work-zinetic.html', 'type': 'article',
        'title': 'Zinetic Music - Kamrul H.',
        'desc': 'Zinetic Music - a music distribution, AI voice and AI video platform built by Kamrul Hasan Kallol with Claude Code.',
    },
    'contact.html': {
        'path': '/contact.html', 'type': 'website',
        'title': 'Contact - Kamrul H.',
        'desc': 'Start a project with Kamrul Hasan Kallol - full-stack software engineer, founder of Softune.',
    },
    'blog.html': {
        'path': '/blog.html', 'type': 'website',
        'title': 'Blog - Kamrul H.',
        'desc': 'Notes and insights on software engineering by Kamrul Hasan Kallol.',
    },
    'post.html': {
        'path': '/post.html', 'type': 'article',
        'title': 'What I Learned Building 150+ Projects - Kamrul H.',
        'desc': 'Lessons from 3+ years and 150+ projects, by Kamrul Hasan Kallol.',
    },
}

PERSON_JSONLD = '''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Kamrul Hasan Kallol",
    "alternateName": "Kamrul H.",
    "url": "%(domain)s/",
    "image": "%(domain)s/assets/images/site/portrait.png",
    "jobTitle": "Full-Stack Software Engineer",
    "worksFor": { "@type": "Organization", "name": "Softune" },
    "address": { "@type": "PostalAddress", "addressLocality": "Dhaka", "addressCountry": "BD" },
    "sameAs": [
      "https://www.facebook.com/developer.kamrulhasan/",
      "https://github.com/Kallolx",
      "https://x.com/khxKallol",
      "https://www.linkedin.com/in/kamrul-hasan-dev/"
    ]
  }
  </script>
''' % {'domain': DOMAIN}

WEBSITE_JSONLD = '''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Kamrul H.",
    "url": "%(domain)s/",
    "author": { "@type": "Person", "name": "Kamrul Hasan Kallol" }
  }
  </script>
''' % {'domain': DOMAIN}


def build_head_block(meta):
    url = DOMAIN + meta['path']
    img = DOMAIN + '/assets/images/site/og.jpg'
    return f'''  <link rel="canonical" href="{url}" />
  <meta name="robots" content="index, follow" />
  <meta name="theme-color" content="#12110d" />
  <meta property="og:type" content="{meta['type']}" />
  <meta property="og:site_name" content="Kamrul H." />
  <meta property="og:title" content="{meta['title']}" />
  <meta property="og:description" content="{meta['desc']}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:image" content="{img}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{meta['title']}" />
  <meta name="twitter:description" content="{meta['desc']}" />
  <meta name="twitter:image" content="{img}" />'''


for fname, meta in PAGES.items():
    s = open(fname, encoding='utf-8').read()
    orig = s

    # replace the existing single relative og:image line with the full SEO block
    old_og = '  <meta property="og:image" content="assets/images/site/og.jpg" />'
    new_block = build_head_block(meta)
    if old_og not in s:
        print(fname + ': OLD OG LINE NOT FOUND, skipping head block')
    else:
        s = s.replace(old_og, new_block)

    jsonld = PERSON_JSONLD if fname in ('index.html', 'about.html') else WEBSITE_JSONLD
    if '</head>' in s and 'application/ld+json' not in s:
        s = s.replace('</head>', jsonld + '</head>')

    if s != orig:
        open(fname, 'w', encoding='utf-8', newline='').write(s)
        print(fname + ': updated')
    else:
        print(fname + ': NO CHANGE')
