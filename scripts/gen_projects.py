# -*- coding: utf-8 -*-
import os

TEMPLATE = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} - Kamrul H.</title>
  <meta name="description" content="{meta_desc}" />
  <meta property="og:image" content="assets/images/og.jpg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@400;500;600&family=Geist+Mono:wght@400;500&family=Tinos&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
  <link rel="stylesheet" href="css/pages.css" />
</head>
<body class="page-work">

  <div data-layout="header"></div>

  <main>
    <!-- ============ PROJECT DETAIL: {brand} ============ -->
    <section class="container p-top detail-head">
      <p class="detail-brand hero-in">{brand}</p>
      <div class="detail-title">
        <h1 class="p-h1 hero-in">{h1}</h1>
        <p class="body-s hero-in">{tagline}</p>
      </div>
      <div class="detail-hero hero-in"><img src="assets/images/{hero_img}" alt="" /></div>
      <div class="detail-meta">
        <div class="reveal"><p class="meta">Role</p><p class="dm-val">{role}</p></div>
        <div class="reveal"><p class="meta">Year</p><p class="dm-val">{year}</p></div>
        <div class="reveal"><p class="meta">Service</p><p class="dm-val">{service}</p></div>
        <div class="reveal">{cta}</div>
      </div>
      <p class="detail-intro reveal">{overview}</p>
    </section>

    <section class="container detail-body">
      <div class="dsec">
        <p class="eyebrow gold reveal">The Challenge</p>
        <div><h2 class="h3 white reveal">{challenge_h}</h2>
        <p class="body-s reveal">{challenge_b}</p></div>
      </div>
      <div class="dsec">
        <p class="eyebrow gold reveal">The Approach</p>
        <div><h2 class="h3 white reveal">{approach_h}</h2>
        <p class="body-s reveal">{approach_b}</p></div>
      </div>
      <div class="dsec">
        <p class="eyebrow gold reveal">The Result</p>
        <div><h2 class="h3 white reveal">{result_h}</h2>
        <p class="body-s reveal">{result_b}</p></div>
      </div>
    </section>

    <section class="container more">
      <div class="more-head"><h2 class="h2 white reveal">More Projects</h2><a href="works.html" class="btn btn-outline"><span class="btn-ico"><i data-lucide="arrow-right"></i></span><span class="btn-txt">See More</span></a></div>
      <div class="works-grid more-grid">
          <a href="work-softunebd.html" class="work-card reveal" data-cats="fullstack ecommerce">
            <div class="work-img land"><img src="assets/images/work-softunebd-hero.png" alt="" /><span class="work-arrow"><i data-lucide="arrow-up-right"></i></span></div>
            <p class="meta">Full-Stack, SaaS</p>
            <h3 class="h3">Softunebd - E-Commerce Platform</h3>
          </a>
          <a href="work-zinetic.html" class="work-card reveal" data-cats="fullstack ai">
            <div class="work-img land"><img src="assets/images/work-zinetic-hero.png" alt="" /><span class="work-arrow"><i data-lucide="arrow-up-right"></i></span></div>
            <p class="meta">Full-Stack, AI</p>
            <h3 class="h3">Zinetic Music - AI Creative Studio</h3>
          </a>
      </div>
    </section>

    <div data-layout="footer"></div>

  </main>

  <script src="js/layout.js"></script>
  <script src="js/weather.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lucide@1.48.0/dist/umd/lucide.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
  <script src="js/main.js"></script>
  <script src="js/pages.js"></script>
</body>
</html>
'''

LIVE_CTA = '<a href="{url}" target="_blank" rel="noopener" class="btn btn-outline"><span class="btn-ico"><i data-lucide="arrow-up-right"></i></span><span class="btn-txt">Visit Live Site</span></a>'
CONTACT_CTA = '<a href="contact.html" class="btn btn-outline"><span class="btn-ico"><i data-lucide="arrow-right"></i></span><span class="btn-txt">Ask About It</span></a>'

projects = [
  dict(slug='starvibe', brand='Star Vibe', title='Star Vibe', h1='Star Vibe - Production Studio', service='Full-Stack, Web Platform',
    tagline='A cinematic landing experience for a content production studio in Gulshan, Dhaka - podcast, video, photography, and studio rental in one booking-focused site.',
    hero_img='work-starvibe-hero.jpg', role='Lead Developer', year='2026', live='https://star1-vibe.vercel.app/',
    overview='Star Vibe needed a premium, cinematic web presence that could represent a real studio space offering podcast recording, video production, photography, studio rental, and post-production - and turn visitors into bookings.',
    challenge_h='A premium, cinematic feel without the page becoming heavy or hard to navigate.',
    challenge_b='The site needed to communicate multiple studio services, build trust, and guide visitors toward booking, all while staying readable over a dark, media-rich hero background.',
    approach_h='A dark-and-gold visual system built on React, TypeScript, and Vite.',
    approach_b='Built with React, TypeScript, Vite, TanStack Router and TanStack Start, and Tailwind CSS, using section-based architecture, reusable service cards, and carefully layered overlays so the cinematic hero video stays readable.',
    result_h='A polished, booking-ready landing page for a real Dhaka production studio.',
    result_b='Star Vibe now has a professional presence covering podcast, video, photography, studio rental, and post-production, with package presentation and booking calls-to-action throughout.'),

  dict(slug='niyenin', brand='Niyenin.com', title='Niyenin.com', h1='Niyenin.com - Ecommerce Store', service='Full-Stack, E-Commerce',
    tagline='A multi-category ecommerce storefront for Bangladesh, with a dedicated jersey store, search, wishlist, and cart built in.',
    hero_img='work-niyenin-hero.jpg', role='Lead Developer', year='2026', live='https://niyenin-com.vercel.app/',
    overview='Niyenin.com is a modern ecommerce storefront for Bangladeshi shoppers, combining broad category discovery with a dedicated jersey store and familiar, trustworthy shopping flows.',
    challenge_h='A broad ecommerce homepage that feels organized, not crowded.',
    challenge_b='The store needed to support many categories, a large search experience, promotions, and cart/wishlist actions while staying clean and mobile-friendly.',
    approach_h='A Next.js storefront with a strong navbar, category sidebar, and reusable product sections.',
    approach_b='Built with Next.js, React, TypeScript, and Tailwind CSS, with Embla Carousel for promotional sections and a component structure that scales across many product categories.',
    result_h='A professional, blue-and-orange shopping experience for a Bangladesh audience.',
    result_b='Niyenin.com now runs a full catalog with search, a dedicated jersey store, cart and wishlist actions, and trust-building delivery messaging.'),

  dict(slug='mailflow', brand='MailFlow', title='MailFlow', h1='MailFlow - Email Automation System', service='Full-Stack, Automation',
    tagline='A node-based visual email automation builder backed by a reliable job queue, with live test runs and execution logs.',
    hero_img='work-mailflow-hero.jpg', role='Lead Developer', year='2025', live='https://automation-kallol.vercel.app/',
    overview='MailFlow makes email automation accessible through a visual, node-based workflow builder, so product and operations teams can create automations quickly and understand execution behavior through structured logs.',
    challenge_h='Coordinating graph-based workflow execution while keeping every run observable.',
    challenge_b='Delays, condition branches, and multi-step flows all needed to stay debuggable - a hard problem once automations start branching in different directions.',
    approach_h='A React Flow canvas over a queue-backed execution engine.',
    approach_b='Built with Next.js, React, TypeScript, and Tailwind CSS on the frontend, with a Node.js backend running flow steps through Agenda.js background jobs, recursive node traversal, and DB-backed logging.',
    result_h='A production-style automation builder with real observability.',
    result_b='MailFlow now supports rule-based conditional routing, flexible delay scheduling, live test runs with polling logs, and a dashboard tracking flows and execution counts.'),

  dict(slug='postra', brand='Postra', title='Postra', h1='Postra - Social Automation (n8n)', service='Backend, Automation',
    tagline='A fully autonomous social media manager built on n8n - content discovery, AI rewriting, image generation, and publishing in one pipeline.',
    hero_img='work-postra-hero.jpg', role='Lead Developer', year='2026', live=None,
    overview='Postra removes manual social media work entirely - an n8n-orchestrated pipeline that discovers content, rewrites it with AI, generates matching visuals, and publishes it automatically.',
    challenge_h='Coordinating multiple async systems without breaking content quality.',
    challenge_b='AI generation, third-party APIs, and social platform integrations all had to stay reliable together - including Facebook Graph API rate limits and keeping Reddit-sourced content non-repetitive.',
    approach_h='An n8n workflow tying together AI content, image generation, and publishing.',
    approach_b='Built on n8n with the OpenAI and Google Gemini APIs for content, the Facebook Graph and Reddit APIs for sourcing and publishing, and a Photocard SaaS integration for on-brand visuals - all queue-managed for retries and rate limits.',
    result_h='A self-running system that posts and engages daily without human input.',
    result_b='Postra now handles daily content publishing, branded image generation, and even automated comment replies, cutting content production time to near zero.'),

  dict(slug='aperitiv', brand='Aperitiv', title='Aperitiv', h1='Aperitiv - Restaurant Reservation', service='Full-Stack, Web &amp; Mobile',
    tagline='A dining platform combining table reservations, restaurant and event discovery, and a social feed across web and mobile.',
    hero_img='work-aperitiv-hero.jpg', role='Lead Developer', year='2026', live='https://aprtiv-psi1.vercel.app/',
    overview='Aperitiv goes beyond simple table booking - reservations, restaurant and event discovery, social engagement, and admin operations, all in one connected ecosystem across web and mobile.',
    challenge_h='Consistent state and performance across web, mobile, and API.',
    challenge_b='A multi-surface architecture needed to stay reliable and consistent, from booking flows to social feeds to admin analytics, without duplicating logic across platforms.',
    approach_h='A shared TypeScript-first API behind a Next.js web app and an Expo mobile app.',
    approach_b='Built with Next.js, React, TypeScript, and Tailwind CSS on the frontend, Expo and React Native for mobile, and an Express, MongoDB, and JWT backend with token rotation and rate limiting.',
    result_h='One reservation ecosystem, consistent across every surface.',
    result_b='Aperitiv now runs a full booking flow, a social community feed with likes and comments, and an admin operations dashboard - all backed by the same secure API.'),

  dict(slug='softune-agency', brand='Softune Agency', title='Softune Agency Portfolio', h1='Softune - Agency Portfolio', service='Full-Stack, Web Platform',
    tagline="Softune's own agency site - services, work showcase, and a client portal, in one bold, conversion-focused experience.",
    hero_img='work-softune-agency-hero.jpg', role='Lead Developer', year='2025', live='https://softune.xyz/',
    overview="Softune's agency portfolio pairs bold creative storytelling with practical business pathways - services discovery, work showcase, testimonials, and portal-based client operations.",
    challenge_h='Balancing expressive storytelling with production-grade backend utility.',
    challenge_b='The site needed animated, responsive marketing sections and a working admin/client portal in the same codebase, without one slowing down the other.',
    approach_h='A Next.js frontend backed by a MySQL admin and portal system.',
    approach_b='Built with Next.js, React, TypeScript, Tailwind CSS, and Framer Motion for the marketing experience, with a Node.js and MySQL backend handling client portal auth and proposal generation.',
    result_h='One system covering marketing, credibility, and client operations.',
    result_b="Softune's site now unifies service storytelling, case studies, and a working admin/customer portal with authentication and proposal tooling."),

  dict(slug='jamilifat', brand='JamilIfat', title='JamilIfat', h1='JamilIfat - Individual Portfolio', service='Full-Stack, Web Platform',
    tagline='A case-study-first personal portfolio for a UI/UX and SEO specialist, tuned for search visibility.',
    hero_img='work-jamilifat-hero.jpg', role='Lead Developer', year='2025', live='https://portfolio-silk-eight-30.vercel.app/',
    overview='A personal portfolio built around web applications engineered for search visibility - combining design craft with technical SEO and measurable, case-study-driven outcomes.',
    challenge_h='A design-forward experience without sacrificing SEO or performance.',
    challenge_b='Optimizing images, metadata, and client-side animation all had to happen without hurting crawlability or load speed.',
    approach_h='A Next.js site tuned for technical SEO from the ground up.',
    approach_b='Built with Next.js, React, TypeScript, Tailwind CSS, and Framer Motion, with Lenis for smooth scroll and careful attention to semantic metadata and Open Graph optimization.',
    result_h='A concise, fast portfolio that explains real outcomes.',
    result_b='The site now presents case-study-first work with smooth micro-interactions and metadata optimized for discovery.'),

  dict(slug='webify', brand='Webify', title='Webify', h1='Webify - Multi-Vendor E-Commerce', service='Full-Stack, SaaS',
    tagline='A multi-tenant ecommerce SaaS foundation with strict tenant isolation and super-admin governance.',
    hero_img='work-webify-hero.jpg', role='Lead Developer', year='2026', live=None,
    overview='Webify is a practical multi-tenant ecommerce SaaS foundation for emerging businesses - modern UI, secure tenant isolation, and operational workflows without high technical barriers.',
    challenge_h='Strict tenant-level security without breaking day-to-day workflows.',
    challenge_b='Balancing tenant boundaries with smooth product and order workflows, while still giving super-admins the visibility they need, required careful middleware and access-policy design.',
    approach_h='Row Level Security and role-aware routing on a Next.js and PostgreSQL stack.',
    approach_b='Built with Next.js 15, React 19, and TypeScript, with a PostgreSQL backend using tenant-scoped Row Level Security policies and Cloudinary for media handling.',
    result_h='A scalable multi-tenant base with real operational tooling.',
    result_b='Webify now supports isolated storefronts per tenant, live business analytics, and super-admin governance tools including cross-tenant analytics.'),

  dict(slug='eventra', brand='Eventra', title='Eventra', h1='Eventra - Event Management Platform', service='Full-Stack, SaaS',
    tagline='A SaaS platform centralizing event creation, registration, payments, and logistics into one organizer dashboard.',
    hero_img='work-eventra-hero.jpg', role='Lead Developer', year='2026', live='https://iftar17-19.vercel.app/',
    overview='Eventra simplifies event management end to end - creation, attendee registration, payments, and logistics like food planning, all centralized into one dashboard for organizers.',
    challenge_h='One flexible system for very different event types.',
    challenge_b='Dynamic registration forms, reliable payments, real-time attendee data, and logistics like food preferences all needed to work without becoming a maze of special cases.',
    approach_h='A role-aware Next.js and MongoDB platform with integrated payments.',
    approach_b='Built with Next.js, React, TypeScript, and Tailwind CSS, backed by Express.js and MongoDB, with digital payment integration and role-based access for organizers, attendees, and admins.',
    result_h='A full event operations system organizers actually run events on.',
    result_b='Eventra now handles event publishing, registration, payments, food and resource tracking, and a full organizer analytics dashboard.'),

  dict(slug='distribe', brand='Distribe', title='Distribe', h1='Distribe - Music Distribution Ops', service='Full-Stack, Music Tech',
    tagline='The operations side of music distribution - a role-aware workspace for release review, royalty analytics, and payouts.',
    hero_img='work-distribe-hero.jpg', role='Lead Developer', year='2026', live='https://streamo-dashboard.vercel.app/',
    overview='Distribe centralizes the day-to-day operations of digital music distribution - release review, royalty analytics, and payouts - into a single role-aware workspace for labels and artists.',
    challenge_h='Reliable royalty operations on messy, high-volume data.',
    challenge_b='Third-party royalty reports arrive as inconsistent CSV exports, and reconciling them against a growing catalog without losing accuracy was the core engineering problem.',
    approach_h='Background CSV processing with resilient field-mapping and admin recovery tools.',
    approach_b='Built with Next.js, React, and TypeScript on an Express.js and MongoDB backend, with background jobs for CSV ingestion, JWT auth, and AWS S3 for media handling.',
    result_h='One operational queue for distribution and royalties.',
    result_b='Distribe now runs release review workflows, CSV-driven analytics, royalty/payout tracking, and admin reconciliation tools using ISRC matching.'),

  dict(slug='allinone-ott', brand='AllInOne OTT', title='AllInOne OTT', h1='AllInOne OTT - Streaming Platform', service='Full-Stack, Web Platform',
    tagline='An all-in-one streaming navigator aggregating regional OTT platforms with TMDB-powered discovery.',
    hero_img='work-allinone-ott-hero.jpg', role='Lead Developer', year='2026', live='https://allinoneott.com/',
    overview='AllInOne OTT is a practical streaming navigator for audiences who want movies, TV, and regional OTT content in one place, blending curated sources with TMDB discovery data.',
    challenge_h='Reliable access control across many outbound platform links.',
    challenge_b='Serving dynamic discovery sections alongside member-level access required automatic expiry handling and a clean split between the discovery frontend and account governance.',
    approach_h='A TMDB-powered discovery layer over a member access system.',
    approach_b='Built with Vite, React, TypeScript, and Tailwind CSS on the frontend, with a Node.js, Express, and MySQL backend handling membership, periodic expiry deactivation, and admin tooling.',
    result_h='A centralized discovery hub with automated account operations.',
    result_b='AllInOne OTT now aggregates multi-region platforms with smart TMDB search, membership access control, and admin tools for user lifecycle management.'),

  dict(slug='foodmaster', brand='foodmaster', title='foodmaster', h1='foodmaster - Delivery Platform', service='Full-Stack, Web Platform',
    tagline='A QR-menu ordering and kitchen operations platform for small food stalls, with real-time order tracking.',
    hero_img='work-foodmaster-hero.jpg', role='Lead Developer', year='2026', live='https://foodmaster-nu.vercel.app/',
    overview='foodmaster gives small food stalls both customer convenience and operational clarity - menu publishing, checkout, order tracking, and back-office controls in one mobile-first platform.',
    challenge_h='Fast customer updates without losing admin control or data consistency.',
    challenge_b='Menu, order, and inventory modules all needed to stay in sync in real time, especially during peak order periods when speed matters most.',
    approach_h='Server-Sent Events for live order status on a Next.js and Supabase stack.',
    approach_b='Built with Next.js, React, TypeScript, and Tailwind CSS, backed by Supabase and PostgreSQL, using SSE-based status updates and recipe-linked inventory deduction tied to order creation.',
    result_h='A real-time ordering system stall owners actually run service on.',
    result_b='foodmaster now handles QR-menu ordering, real-time kitchen status tracking, and inventory that auto-deducts against recipes as orders come in.'),

  dict(slug='servicemarket', brand='Service Market', title='Service Market', h1='Service Market - On-Demand Home Services', service='Full-Stack, Web Platform',
    tagline='An end-to-end home services marketplace concept for the UAE, with multi-step booking and OTP-secured login.',
    hero_img='work-servicemarket-hero.jpg', role='Lead Developer', year='2026', live=None,
    overview='Service Market is a practical, end-to-end marketplace concept for booking home services across Dubai, Abu Dhabi, and Sharjah - discovery through to confirmed, paid booking with minimal friction.',
    challenge_h='Reliable bookings across several external dependencies at once.',
    challenge_b='Payment gateways, OTP delivery channels, and notification services all had to work together smoothly, with sensible fallbacks when any one of them had a hiccup.',
    approach_h='A multi-step booking flow with WhatsApp-first OTP and Ziina payments.',
    approach_b='Built with Vite, React, TypeScript, and Tailwind CSS, with a Node.js and MySQL backend integrating Twilio for OTP fallback and the Ziina API for payment intents.',
    result_h='A complete booking journey from discovery to confirmed payment.',
    result_b='Service Market now runs city-aware discovery, a guided multi-step checkout, integrated payments, and a role-based operations dashboard for admins and managers.'),

  dict(slug='mastertools', brand='MasterTools BD', title='MasterTools BD', h1='MasterTools BD - Premium Access Hub', service='Full-Stack, SaaS',
    tagline='A subscription hub that bundles access to multiple premium digital services behind one account.',
    hero_img='work-mastertools-hero.jpg', role='Lead Developer', year='2026', live='https://mastertools-bd.vercel.app/',
    overview='MasterTools BD simplifies access to premium digital services - instead of managing separate subscriptions, users get everything from one place, with payments and order workflows automated end to end.',
    challenge_h='Securely automating subscriptions across many service types.',
    challenge_b='Payment reliability, account integrity, and misuse prevention all needed strong backend architecture before the product could scale past a handful of users.',
    approach_h='A Next.js and PostgreSQL subscription engine with OAuth2 and automated order flows.',
    approach_b='Built with Next.js, React, and TypeScript on an Express.js and PostgreSQL backend, using OAuth2 for auth and Zustand for state, with automated order and service-allocation workflows.',
    result_h='A full subscription platform ready for a growing user base.',
    result_b='MasterTools BD now runs unified premium access, automated payment and order handling, and an admin dashboard for monitoring users and subscriptions.'),
]

os.makedirs('.', exist_ok=True)
for p in projects:
    cta = LIVE_CTA.format(url=p['live']) if p['live'] else CONTACT_CTA
    html = TEMPLATE.format(
        title=p['title'], brand=p['brand'], h1=p['h1'], tagline=p['tagline'],
        hero_img=p['hero_img'], role=p['role'], year=p['year'], service=p['service'],
        cta=cta, overview=p['overview'],
        challenge_h=p['challenge_h'], challenge_b=p['challenge_b'],
        approach_h=p['approach_h'], approach_b=p['approach_b'],
        result_h=p['result_h'], result_b=p['result_b'],
        meta_desc=p['tagline'].replace('"', "'"),
    )
    fname = f"work-{p['slug']}.html"
    with open(fname, 'w', encoding='utf-8', newline='') as f:
        f.write(html)
    print('wrote', fname)
