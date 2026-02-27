# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Discover Nevada — a travel guide website built with Astro 5, Tailwind CSS 4, and deployed to Cloudflare Pages. Content is markdown-based using Astro's content collections with Zod schemas.

## Commands

```bash
npm run dev       # Start dev server at localhost:4321
npm run build     # Production build to ./dist/
npm run preview   # Preview production build locally
```

No test runner is configured. No linter is configured.

## Branding

- Colors: Desert Teal #0D7377 (primary), Warm Coral #E8654A (accent)
- Deep Night #1A2332 (headings/dark backgrounds)
- Sand #F5F0E8 (light background), Sky #EFF8FF (alt background)
- Warm Gold #D4A574
- Fonts: Outfit (sans), DM Serif Display (serif)

## Regions

- las-vegas-metro
- northern
- southern
- western

## Architecture

### Content Collections (`src/content/`)

Two collections defined in `src/content/config.ts`:
- **destinations** — Travel destination pages with typed schema (region enum: las-vegas-metro/northern/southern/western, budgetPerDay in USD, highlights array, contentStatus workflow, gradientColors for per-destination theming)
- **blog** — Articles with categories (destination, food, festival, practical, budget, culture)

Both collections use a `draft: true` default. Content status tracks: draft -> review -> published -> needs-update.

### Routing (`src/pages/`)

- `index.astro` — Home page
- `destinations/[...slug].astro` — Dynamic catch-all route
- `blog/[...slug].astro` — Blog post pages
- `404.astro` — Custom error page

### Layouts

- `BaseLayout.astro` — Root layout with SEO meta, imports FloatingNav + Footer + global styles
- `DestinationLayout.astro` — Wraps BaseLayout, adds hero with per-destination gradient

### Deployment

- Domain: discovernevada.info
- D1 database: trip-planner-cache-nv (ID: db535744-6cfe-4365-9e6d-d291ece2a674)
- Cloudflare Pages via `@astrojs/cloudflare` adapter

## Destinations (10)

Las Vegas, Reno, Lake Tahoe, Valley of Fire, Red Rock Canyon, Great Basin, Virginia City, Henderson, Boulder City, Carson City

## Content Voice

- First-person singular — Scott's perspective as a visitor
- Prices in USD only
- Honest, opinionated, insider perspective
- **Names rule:** Only use "Scott" and "I" in content. Never include names of family members, children, or other companions.
- Cross-link every page to at least 2 other content pillars
- Question-based H2/H3 headings for GEO
- Answer-first paragraphs: lead with the answer, then supporting detail

### Required Pro Tips (Every Destination Page)

1. **Getting There** — Airport options (LAS, RNO), driving distances
2. **Best Time to Visit** — Summer heat warnings, ski season, best months by region
3. **Getting Around** — Car rental essential, highway corridors (I-15, I-80, US-93, US-50)
4. **Budget Tips** — Free attractions, resort fee awareness, midweek deals
5. **Safety** — Heat safety, dehydration, altitude changes, desert driving
6. **Packing** — Sun protection, layers for elevation changes, hiking boots, water bottles

Use `<div class="scott-tips">` block format.

## Affiliate Links

- Booking.com: aid=2778866, label=discovernevada
- GetYourGuide: partner_id=IVN6IQ3
- Viator: pid=P00290009
- SafetyWing: referenceID=24858745
