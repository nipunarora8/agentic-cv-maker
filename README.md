# ⚡ Agentic CV Maker

> Paste a job description. Get a tailored CV, cover letter, and interview prep guide — compiled to PDF, downloaded as a ZIP, entirely in your browser.

![App Screenshot](docs/screenshot.png)

**[→ Try it live](https://nipunarora8.github.io/agentic-cv-maker)**

---

## How it works

Everything runs in the browser — no backend, no server, no data sent anywhere except directly to Google's Gemini API with your own key.

1. Upload your `base_cv.tex` and `base_cover_letter.tex` (saved to localStorage — persists across sessions)
2. Paste a job description — company name and job title are extracted automatically
3. Gemini tailors your CV and cover letter by editing your existing LaTeX files, not generating new ones
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

## What Gemini actually does

The agent is designed around **honest positioning** — it edits your real experience to match the JD, it does not fabricate.

- Rewrites your professional summary to address the company's core problem
- Reorders and reframes bullet points using the JD's vocabulary, only where the mapping is true
- Calculates a **transparent, deterministic ATS Match Score** fully in-browser (Original vs. Tailored comparison)
- Displays a native **„Recruiter Read“** Markdown review of your application
- Drafts an **"Outreach Pack"** containing a personalized Cold Email and LinkedIn connection note
- Provides a **Live PDF Preview** directly in the UI before you even download
- Supports **Multi-Language** processing seamlessly (e.g., German/English capabilities)
- Includes a **Tailoring Intensity** toggle (Light, Balanced, or Aggressive)
- Generates a full interview prep guide: vibe check, your best talking points, gap analysis, and mock questions

---

## Stack

| | |
|---|---|
| AI | Google Gemini (via REST API) |
| LaTeX compilation | [latex.ytotech.com](https://latex.ytotech.com) (free) |
| Frontend | Plain HTML — GitHub Pages |
| Storage | Browser localStorage only |

---

## Setup

### 1. Fork this repo

Click **Fork** at the top right. Keep it public to use GitHub Pages for free.

### 2. Enable GitHub Pages

Repo → **Settings → Pages** → Source: `Deploy from a branch` → Branch: `main`, folder: `/docs`

Your app will be live at:
```
https://your_github_username.github.io/agentic-cv-maker
```

### 3. Get a Gemini API key

Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) and create a free key. It starts with `AIza...`

### 4. Open the app and configure

1. Paste your Gemini API key → click **Save key**
2. Upload your `base_cv.tex` → click the CV slot
3. Upload your `base_cover_letter.tex` → click the cover letter slot

Both files are saved to your browser's localStorage. You only need to do this once.

### 5. Use it

1. Paste a job description into the textarea
2. Click **⚡ Generate**
3. Wait ~60–90 seconds
4. Download individual files or click **Download all as ZIP**

---

## Your base LaTeX files

The tool works best with a standard LaTeX CV using `article` class and `pdflatex`-compatible packages. The repo includes `base_cv.tex` and `base_cover_letter.tex` as examples — replace these with your own.

The agent is instructed to copy your preamble exactly and only edit text content. If you use a heavily custom LaTeX setup, it will still work — just verify the first output and adjust the system prompt in `docs/index.html` if needed.

---

## Customizing the agent

The system prompt lives inside a `<script type="text/plain" id="system-prompt">` tag in `docs/index.html`. Open it and edit directly — no escaping needed, paste plain text.

Key things to personalize:
- Your name (used in output filenames)
- Your background and degree
- How aggressively to reframe experience vs. flag gaps in the prep guide

---

## Privacy

- Your Gemini API key is stored in `localStorage` — it never appears in the source code or git history
- Your base CV and cover letter are stored in `localStorage` — they never leave your browser except when sent to Gemini as part of the generation prompt
- No analytics, no tracking, no third-party services except Gemini API and latex.ytotech.com

---

## Repo structure

```
├── docs/
│   └── index.html           # The entire app — GitHub Pages frontend
├── base_cv.tex              # Example base CV (replace with yours)
├── base_cover_letter.tex    # Example base cover letter (replace with yours)
├── requirements.txt
└── README.md
```

---

## License

MIT — use it, fork it, build on it.