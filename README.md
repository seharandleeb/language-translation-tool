# 🌐 LinguaFlow — Language Translation Tool

> **CodeAlpha AI Internship · Task 1**
> A beginner-friendly Python web app that translates text across 100+ languages using Google Translate — completely free, no API key required.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🌍 100+ Languages | Full Google Translate language coverage |
| 🔍 Auto-Detect | Automatically detects the source language |
| 📋 Copy Button | One-click copy of translated text |
| ⚡ Real-time | Instant translation with loading feedback |
| 🛡️ Error Handling | Friendly messages for network & input errors |
| 🎨 Modern UI | Clean dark theme built with custom CSS |

---

## 📁 Project Structure

```
language-translation-tool/
│
├── app.py              ← Main Streamlit application
├── requirements.txt    ← Python dependencies
└── README.md           ← This file
```

---

## 🚀 Setup Instructions (Step by Step)

### Step 1 — Make sure Python is installed

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and run:

```bash
python --version
```

You should see something like `Python 3.9.x` or higher. If not, download Python from [python.org](https://www.python.org/downloads/).

---

### Step 2 — Download / clone this project

**Option A — Download ZIP** (easiest for beginners):
1. Download this project as a ZIP file
2. Extract it to a folder on your Desktop (e.g. `language-translation-tool`)

**Option B — Git clone**:
```bash
git clone https://github.com/your-username/language-translation-tool.git
cd language-translation-tool
```

---

### Step 3 — Create a virtual environment (recommended)

A virtual environment keeps dependencies isolated from your system Python.

```bash
# Navigate into the project folder first
cd language-translation-tool

# Create virtual environment
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate

# On Mac / Linux:
source venv/bin/activate
```

You'll see `(venv)` at the start of your terminal line — that means it's active ✅

---

### Step 4 — Install dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `streamlit` — the web UI framework
- `deep-translator` — free Google Translate wrapper (no API key needed)
- `pyperclip` — clipboard support for the Copy button

---

### Step 5 — Run the app

```bash
streamlit run app.py
```

Your browser will automatically open at **http://localhost:8501** 🎉

---

### Step 6 — Use the app

1. **Select source language** — choose the language of your input text (or leave as *Auto Detect*)
2. **Select target language** — choose the language you want to translate into
3. **Type or paste** your text in the input box
4. Click **🌐 Translate**
5. Your translation appears below — click **📋 Copy Translation** to copy it

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| `streamlit: command not found` | Make sure your venv is activated |
| Copy button doesn't work | On some Linux systems, install `xclip`: `sudo apt install xclip` |
| Translation fails | Check your internet connection (Google Translate requires network access) |
| Blank page in browser | Try refreshing or opening `http://localhost:8501` manually |

---

## 🛠️ Tech Stack

| Library | Purpose | Cost |
|---|---|---|
| [Streamlit](https://streamlit.io) | Web UI framework | Free & open-source |
| [deep-translator](https://github.com/nidhaloff/deep-translator) | Translation engine | Free (no API key) |
| [pyperclip](https://github.com/asweigart/pyperclip) | Clipboard access | Free & open-source |

---

## 📚 How It Works

```
User types text
      ↓
Streamlit captures input + language selections
      ↓
GoogleTranslator(source=..., target=...).translate(text)
      ↓
deep-translator calls Google Translate (free tier)
      ↓
Translation result displayed in the UI
      ↓
User can copy with one click
```

---

## 🤝 About

Made as part of the **CodeAlpha AI Internship Program** — Task 1: Language Translation Tool.

> This project is intentionally kept simple and beginner-friendly. No paid APIs, no complex setup, no databases — just Python, Streamlit, and Google Translate.
