# 🔁 Project Handoff — Dr. Vishal Kotha Portfolio

**For the incoming agent (Kimi K3 Cowork).** Read this file completely before touching anything. It is the single source of truth for project state, conventions, and the road ahead. Update the "Progress Log" at the bottom whenever you complete work, so Vishal can audit progress across agents.

- **Last updated:** 2026-07-25
- **Owner:** Dr. Vishal Kotha (vishalkotha1@gmail.com)
- **Repo:** https://github.com/vishal-kotha/vishalkotha.git (branch: `main`)
- **Live site:** https://vishalkotha.pages.dev (Cloudflare Pages; custom domain `vishalkotha.com` planned, not yet purchased)

---

## ⚡ CURRENT STATUS (2026-07-25) — supersedes stale items below

Several items described further down as "pending/critical" are now RESOLVED. Read this first:

- **All work is committed and pushed.** The "~150 uncommitted changes" era is over. `git status` is clean; `origin/main` has everything (blog, quiz, wow layer, CV sync, SEO, logo). The line-ending churn was fixed with `.gitattributes`; `public/` is now git-ignored (build output).
- **HOSTING MIGRATED: Netlify → Cloudflare Pages.** Reason: Netlify's 2026 credit model (300 credits/mo, 15 per deploy ≈ 20 deploys/mo) throttled active development. Cloudflare Pages = unlimited bandwidth, free, auto-builds on push. **Therefore all Netlify items in Section 4 (AUTH_TOKEN, SITE_ID, form notifications) are MOOT.** There are no Netlify secrets to set anymore.
- **CI pipeline changed accordingly.** `.github/workflows/site-sync.yml` no longer deploys anywhere — it only refreshes citation metrics weekly and commits them; Cloudflare rebuilds on that commit. It does NOT drain Netlify.
- **Contact form migrated to Web3Forms** (access key live in `content/contact/index.md`). Netlify Forms no longer used. Submissions route straight to Vishal's email — no dashboard notification setting needed.
- **New brand identity shipped:** perovskite unit-cell logo (`static/images/logo-mark.svg`) + crystal-tile favicon. Replaces the old `logo.png`.
- **UX reverts (per owner):** the prev/next section bar and the condense-on-scroll header were tried and REMOVED. Do not reintroduce them without asking.
- **Google Search Console:** verified for the pages.dev property (tag `dkQbZ3...` in `<head>`); sitemap submitted.
- **baseURL is now `https://vishalkotha.pages.dev/`** in `hugo.yaml` (canonical/OG/schema/sitemap all follow it). One-line change when the custom domain is bought.

### The ONE real open issue (as of this writing)
Cloudflare is serving a **stale build** — the live pages.dev still shows old content (Netlify canonical, `logo.png`, the removed prev/next bar). GitHub `main` is correct, so this is a Cloudflare-side build/cache problem being diagnosed via the Cloudflare **Deployments** tab (check: latest deploy status, production branch = `main`, Git auto-deploy connected). Nothing else should be built until the live site matches `main`.

### Still genuinely valid & pending
- **CV PDF is still the Nov 2025 version** (`static/files/CV-Vishal_Kotha.pdf`). A newer markdown CV exists; regenerate the PDF (ATS-safe, single-column) and swap it.
- **Next feature (agreed): the hybrid homepage redesign** — full-width cinematic layout (the `main` 800px cap is the "narrow/portrait" complaint), + a dedicated **Research Vision page in MSCA Excellence/Impact/Implementation language** (highest-leverage for the grant-committee audience).

---

## 1. The Mission (do not lose sight of this)

This is not a generic portfolio. It is a strategic instrument with three target audiences, and **every change must serve at least one of them**:

1. **Grant committees** (MSCA, Humboldt) — proof of research excellence, mobility, impact, and public outreach.
2. **Hiring / professorship committees & international peers** — research depth + teaching evidence. This site is used the way a LinkedIn profile is used: to vet Vishal before an academic or industry role.
3. **Young researchers** — a curiosity engine (blog + quiz + Ask-a-Doubt) that pulls students in and converts them into mentees.

**Design north star:** clean, smooth, *fast* (Vishal explicitly dislikes any lag), elegant, classic-but-dynamic. One memorable interactive moment rooted in his real science — never spectacle for its own sake. For committees, restraint reads as seniority.

**Growth goal:** the site should expand in length and breadth over time, and international scientists/professors should keep returning.

---

## 2. Tech Stack & How It Works

| Layer | Choice | Notes |
|---|---|---|
| Generator | **Hugo** (extended), theme `PaperMod` | Content in `/content/*.md`, most pages use raw HTML inside markdown (`unsafe: true` is on). |
| Hosting | **Netlify** (free tier) | Deploy is **prebuilt** — GitHub Actions builds `public/` and pushes it, so Netlify build minutes are NOT consumed. |
| Version control | GitHub | `main` branch auto-deploys via Actions. |
| Automation | GitHub Actions `.github/workflows/site-sync.yml` | Weekly metrics refresh + build + Netlify deploy. |
| Forms | Netlify Forms | Zero backend; the contact form posts to Netlify. |
| 3D | three.js r128 (CDN, lazy-loaded) | Homepage crystal only. |
| Math | MathJax 3 (CDN) | `$...$` inline, `$$...$$` display. |

**Design tokens** (defined in `static/css/style.css` `:root`):
- Navy `#0a192f` (primary), Gold `#d4af37` (accent), dark-mode teal `#64ffda`.
- Fonts: Merriweather (body/serif), Roboto (headers/UI), Fira Code (data).
- Keep this identity. Do not introduce new colors or fonts without a strong reason.

---

## 3. Current State — What's DONE (verified, in repo)

### Phase 1 — Foundation ✅
- **Blog** at `/blog/` — layouts in `layouts/blog/{list,single}.html`, RSS enabled, 3 seed posts in `content/blog/`. Every post ends with an "Ask Me a Doubt" + quiz CTA.
- **Interactive Science Quiz** at `/quiz/` — engine `layouts/_default/quiz.html`, question bank `static/data/quiz.json` (15 Qs, 10 shown per round, options shuffled so the answer isn't always first). Instant explanations, difficulty badges, result titles, copy-to-share. **To expand: just add objects to `quiz.json`** — no code change needed.
- **Content synced to latest CV** — BPCL role = **Scientist-B, CRDC, Greater Noida** (alkaline electrolyzer / H₂S valorization / ceramic H₂ burner). Isha reframed as **Teaching Volunteer**. Added Teaching Experience, Invited Lectures, Mentorship sections to `/experience/`.
- **Bugs fixed:** `/experience/` and `/publications/` were 404ing (permalink config) — fixed via `url:` front-matter. Footer email typo, dead Scholar placeholder link corrected.

### Phase 2 — Visibility engine ✅
- **Auto-sync pipeline** `.github/workflows/site-sync.yml` + `scripts/update_metrics.py` (Scholar primary, OpenAlex fallback, guards against zero/regressed data). Old `hugo.yaml` Pages workflow deleted (it was publishing a duplicate site — an SEO liability).
- **SEO layer** in `layouts/_default/baseof.html` `<head>`: per-page title/description, canonical, OpenGraph + Twitter cards, branded share image `static/images/og-card.png`, **schema.org Person JSON-LD** (home only), `layouts/robots.txt` + sitemap with absolute URLs.
- **Google Search Console** verified (tag in `<head>`), sitemap submitted successfully.
- `baseURL` set to `https://vishalkotha.netlify.app/`.

### Phase "Wow" layer ✅
- **Interactive 3D perovskite crystal** on homepage ("Touch My Research"): `static/js/crystal.js` + section in `content/_index.md`. Drag-to-rotate LaMnO₃ lattice; a button substitutes K⁺ for La³⁺ (Vishal's actual PhD trick) live. Lazy-loads three.js only on scroll-into-view, pauses off-screen, respects `prefers-reduced-motion`.
- **Motion polish:** IntersectionObserver scroll-reveals, card hover physics, focus-visible outlines. All reduced-motion safe.
- **Working contact / Ask-a-Doubt form** on `/contact/` (Netlify Forms, honeypot spam guard, role + topic selectors, success state).

### Mobile overhaul ✅
- **Animated hamburger menu** (`#nav-toggle` in baseof.html) replacing the old 9-item wrap.
- Fixed a **serious bug**: contact form was trapped in a 200px-tall container on mobile (form was cut off). Now stacks properly.
- iOS anti-zoom (16px inputs), horizontal-overflow guard, responsive crystal/typography/hero buttons/quiz targets.

### Sequential navigation ✅
- Prev/Next section links at the bottom of every page (`.page-nav` in baseof.html) + desktop **← / → arrow-key** navigation. (Deliberately NOT touch-swipe — it collides with iOS/browser back gestures; see Vishal's Q&A in chat history.)

---

## 4. ⚠️ PENDING — Actions Vishal Must Do (not code)

These are blocking full automation and must be confirmed:

1. **GitHub Secrets** (repo → Settings → Secrets and variables → Actions):
   - `NETLIFY_AUTH_TOKEN` (Netlify → User settings → Applications → New access token)
   - `NETLIFY_SITE_ID` (Netlify → Site configuration → Site details → Site ID)
   Without these the Actions deploy step fails.
2. **Disable GitHub Pages** (repo → Settings → Pages) — kills the leftover duplicate site.
3. **Netlify form notifications** (Netlify → Forms → Settings → Notifications → add email) so doubts reach his inbox.
4. **Commit & push** the current working tree — there are **~150 uncommitted changes** as of this handoff. Everything in Sections 3 above is on disk but may not all be pushed. Verify with `git status` and push.
5. **Update the CV PDF**: `static/files/CV-Vishal_Kotha.pdf` is the Nov 2025 version. A newer markdown CV exists at `static/files/CV-Vishal_Kotha.md`. When Vishal provides the new DOCX, generate an ATS-safe single-column PDF (his rule: no icon fonts, single column) and swap it in.
6. **Buy the domain** `vishalkotha.com`. Then: point DNS to Netlify, change `baseURL` in `hugo.yaml` to `https://vishalkotha.com/`, add a 301 from the netlify.app URL, and re-verify Search Console. Everything (canonicals, sitemap, schema, OG) follows the baseURL automatically.

---

## 5. The Roadmap — What's NEXT (build in this order)

### Phase 3 — remaining engagement pieces
- **Newsletter** subscription (Netlify Forms or Buttondown free tier) — capture returning visitors.
- **Auto-convert answered doubts → FAQ blog posts** (the content flywheel: every good question Vishal answers becomes public content that ranks in search).

### Phase 4 — content depth (this is how the site grows in "length and breadth")
- **Three recurring blog series:** *Perovskite Primer* (teaching → student magnet), *Industry Notebook* (BPCL-safe insights → peers; MUST stay confidentiality-safe), *Fellowship Diaries* (documenting MSCA prep → attracts reviewers + researchers).
- **Research Vision page** written explicitly in MSCA evaluation language (Excellence / Impact / Implementation).
- **Visual mobility timeline** (India → Israel → industry) — itself an MSCA selling point.

### Phase 5 — polish & authority
- **Quiz v2**: difficulty levels, topic filters, shareable result cards as images.
- **Live metrics wall** (animated citation/h-index counters from the auto-synced data).
- Lighthouse pass — target 95+ on all four axes (perf/a11y/best-practices/SEO).
- Optional: blog post cross-posting helper to LinkedIn.

---

## 6. Repo Map (key files)

```
content/
  _index.md ............ homepage (hero, crystal section, vision, cards)
  about/, expertise/, research/, publications/, experience/, gallery/, contact/
  blog/ ................ _index.md + 3 posts (add new posts here)
  quiz/index.md ........ quiz page (layout: "quiz")
layouts/
  _default/baseof.html . MASTER template: head/SEO/schema, nav+hamburger,
                         footer, page-nav, crystal loader, all global JS
  _default/quiz.html ... quiz engine
  blog/{list,single}.html
  robots.txt
  shortcodes/metrics.html  ({{< metrics >}} — reads auto-synced data)
static/
  css/style.css ........ ALL styling (single file; mobile rules at the BOTTOM)
  js/crystal.js ........ 3D perovskite viewer
  data/quiz.json ....... quiz question bank (expand here)
  data/roadmap.json .... footer "Coming Next" ticker
  images/og-card.png ... social share card
  files/CV-Vishal_Kotha.{pdf,md}
data/scholar_metrics.json  (auto-updated by CI; do not hand-edit)
scripts/update_metrics.py  (metrics fetcher; NEW — use this, not the old fetch_*.py)
.github/workflows/site-sync.yml  (the ONE pipeline)
```

**Legacy/ignore:** `scripts/fetch_metrics.py` & `fetch_pubs.py` are superseded by `update_metrics.py`. `z-help-docs/` and `progress tracker/` are historical notes. The old `project_state.json` and `Here is a comprehensive hand-off summary.md` describe a much earlier (pre-Hugo, BPCL-application) phase — **do not follow them; this file supersedes them.**

---

## 7. Conventions & Gotchas (learn from prior mistakes)

- **Markdown + HTML indentation trap:** Hugo/Goldmark turns any block indented ≥4 spaces into a `<pre><code>` block. When embedding raw HTML (forms, divs) in `.md` files, keep it **flush-left**. This already broke the contact form once.
- **Every non-trivial change: rebuild and verify.** `hugo --minify -d /tmp/check` then grep the output HTML for your change. Never assume.
- **Respect `prefers-reduced-motion`** in any new animation.
- **Mobile is first-class.** Test at ≤600px. Inputs must be ≥16px (iOS zoom). No horizontal overflow.
- **Speed is a hard requirement.** Lazy-load anything heavy (like three.js was). No render-blocking additions to `<head>`.
- **Don't hijack native gestures** (swipe = back on iOS/trackpad). Vishal asked about swipe-between-tabs; the answer was no — use the prev/next links instead.
- **Scholar ID is `ryaF3dIAAAAJ`** (the CV has a typo `rvaF...` — the working metrics script confirms `ryaF`). Keep it consistent.
- **BPCL content must stay confidentiality-safe** — no proprietary/internal details in blog posts.

---

## 8. How to Preview & Deploy

```bash
# Local preview (live-reload, no push):
hugo server -D                      # → http://localhost:1313
# Preview on a real phone (same WiFi):
hugo server --bind 0.0.0.0 --baseURL http://<YOUR-PC-IP>:1313

# Deploy to production:
git add -A && git commit -m "..." && git push    # CI builds + deploys
# (Manual fallback if CI secrets not set:)
hugo --minify && netlify deploy --prod --dir=public
```
> The contact form only works on the deployed Netlify site, not on localhost.

---

## 9. Progress Log (APPEND a dated entry every work session)

| Date | Agent | What changed | Verified? |
|---|---|---|---|
| 2026-07 | (prior) | Phase 1 blog+quiz, CV sync, BPCL role, fixed 404s | ✅ build |
| 2026-07 | (prior) | Phase 2 auto-sync pipeline + full SEO/schema/OG | ✅ build |
| 2026-07-22 | (prior) | Wow layer (3D crystal, motion, contact form), mobile overhaul, prev/next nav | ✅ build |
| 2026-07-25 | (prior) | Committed+pushed all work; fixed Experience raw-HTML bug; reverted prev/next + header condense; new perovskite logo/favicon; MIGRATED Netlify→Cloudflare Pages; form→Web3Forms; baseURL→pages.dev | ✅ build; ⚠️ Cloudflare serving stale build (open) |
| _add yours below_ | | | |

---

**First thing to do, incoming agent:** run `git status`, confirm what's committed vs. on-disk, run `hugo --minify` to confirm a clean build, then read Section 4 (pending owner actions) and Section 5 (roadmap) before proposing next steps to Vishal.
