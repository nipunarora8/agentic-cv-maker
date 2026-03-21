# ⚡ Agentic CV Maker

> Paste a job description. Get a tailored CV, cover letter, and interview prep guide — compiled to PDF, downloaded as a ZIP, entirely in your browser.

![App Screenshot](docs/screenshot.png)

**[→ Try it live](https://nipunarora8.github.io/agentic-cv-maker)**

---

## How it works

Everything runs in the browser — no backend, no server, no data sent anywhere except directly to your chosen AI provider with your own key.

1. Upload your `base_cv.tex` and `base_cover_letter.tex` (saved to localStorage — persists across sessions)
2. Paste a job description — company name and job title are extracted automatically
3. Your chosen AI tailors your CV and cover letter by editing your existing LaTeX files, not generating new ones
4. PDFs are compiled via [latex.ytotech.com](https://latex.ytotech.com)
5. Everything is packaged into a ZIP and downloaded directly to your machine

```
YourDownloads/
└── Company_Job_Title/
    ├── CV_YourName_Company.tex
    ├── CV_YourName_Company.pdf
    ├── Cover_YourName_Company.tex
    ├── Cover_YourName_Company.pdf
    ├── Interview_Prep_Company.md
    ├── JD_Profile_Company.json
    └── Recruiter_Read_Company.md
```

---

## Tools

### `index.html` — CV Maker
The main tool. Tailors, compiles, and packages your full application.

### `ats_analyzer.html` — ATS Analyzer
A standalone pre-check tool. Upload your CV, paste a JD, and get an ATS match score, keyword gap analysis, a candid recruiter review, and specific tips to boost your profile — without generating a new document. Accessible directly from the CV Maker via the **ATS Analyzer ↗** button.

---

## What the AI actually does

The agent is built around **honest positioning** — it edits your real experience to match the JD, it does not fabricate.

- Rewrites your professional summary to address the company's core problem
- Reorders and reframes bullet points using the JD's vocabulary, only where the mapping is true
- Computes a **transparent, deterministic ATS Match Score** fully in-browser (Original vs. Tailored)
- Displays a **Recruiter Read** — a candid first-pass review of your application
- Drafts an **Outreach Pack** — a personalized cold email and LinkedIn connection note
- Provides a **Live PDF Preview** directly in the UI before you download
- Supports **multi-language** processing (e.g. German / English JDs)
- **Tailoring Intensity** toggle: Light, Balanced, or Aggressive
- Generates a full **Interview Prep Guide**: vibe check, your strongest angles, honest gap analysis, and mock questions

---

## ATS Score Methodology

Computed entirely in-browser — not a black-box vendor score.

| Dimension | Max | What it checks |
|---|---|---|
| Hard Requirements | 30 | Must-have JD keywords found in the CV |
| Skills Coverage | 25 | Core keywords, tools, preferred requirements |
| Evidence Strength | 20 | Quantified results, action verbs, outcome language |
| Role Alignment | 15 | Job title, role family, domain, evidence priorities |
| Format Compatibility | 10 | Detectable sections, dates, contact info |

---

## Stack

| | |
|---|---|
| AI | Gemini, OpenAI, or Anthropic (your key, your choice) |
| LaTeX compilation | [latex.ytotech.com](https://latex.ytotech.com) (free) |
| Frontend | Plain HTML — GitHub Pages |
| Storage | Browser localStorage only |

---

## Your base LaTeX files

The tool works best with a standard LaTeX CV using the `article` class and `pdflatex`-compatible packages. The repo includes `base_cv.tex` and `base_cover_letter.tex` as examples — replace these with your own.

The agent copies your preamble exactly and only edits text content. If you use a custom LaTeX setup, verify the first output and adjust the system prompt in `docs/index.html` if needed.

---

## Customizing the agent

The system prompt lives inside a `<script type="text/plain" id="system-prompt">` tag in `docs/index.html`. Open it and edit directly — no escaping needed, plain text.

Key things to personalize:
- Your name (used in output filenames)
- Your background and target roles
- How aggressively to reframe experience vs. flag gaps in the prep guide

---

## Privacy

- API keys are stored in `localStorage` — never in source code or git history
- Your CV and cover letter are stored in `localStorage` — they never leave your browser except when sent to your chosen AI provider as part of the generation prompt
- No analytics, no tracking, no third-party services except your AI provider and latex.ytotech.com

---

## Repo structure

```
├── docs/
│   ├── index.html           # CV Maker — main app
│   └── ats_analyzer.html    # ATS & Recruiter Analyzer
├── base_cv.tex              # Example base CV (replace with yours)
├── base_cover_letter.tex    # Example base cover letter (replace with yours)
└── README.md
```

---

## License

MIT — use it, fork it, build on it.