# 🌐 LinguaFlow — Language Translation Tool

> **CodeAlpha AI Internship · Task 1**
> A beginner-friendly Python web app that translates text across 80+ languages using Google Translate — completely free, no API key required.

---

## 👩‍💻 About the Developer

**Sehar Andleeb**
🎓 BS Artificial Intelligence — 8th Semester
💡 Passionate AI Engineer
🏢 AI Intern @ [CodeAlpha](https://www.codealpha.tech/)

This is my **first project** of the CodeAlpha AI Internship Program, built as Task 1: Language Translation Tool. I'm passionate about using AI and Python to build real-world tools that solve everyday problems.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🌍 80+ Languages | Full Google Translate language coverage |
| 🔍 Auto-Detect | Automatically detects the source language |
| 📋 Copy Button | One-click copy of translated text |
| ⚡ Instant | Real-time translation with loading spinner |
| 🛡️ Error Handling | Friendly messages for network & input errors |
| 🎨 Dark UI | Clean dark theme — no eye strain |

---

## 📁 Project Structure

```
language-translation-tool/
│
├── .streamlit/
│   └── config.toml       ← Forces dark theme (fixes text visibility)
│
├── app.py                ← Main Streamlit application
├── requirements.txt      ← Python dependencies
├── .gitignore            ← Git ignore rules
└── README.md             ← This file
```

---

## 🚀 Setup Instructions (Step by Step)

### Step 1 — Make sure Python is installed

```bash
python --version
```

You need **Python 3.9 or higher**. Download from [python.org](https://www.python.org/downloads/) if needed.

---

### Step 2 — Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/language-translation-tool.git
cd language-translation-tool
```

---

### Step 3 — Create a virtual environment

```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac / Linux:
source venv/bin/activate
```

You'll see `(venv)` in your terminal — that means it's active ✅

---

### Step 4 — Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 5 — Run the app

```bash
streamlit run app.py
```

Your browser will open automatically at **http://localhost:8501** 🎉

---

## 🎮 How to Use

1. **Select source language** — choose the input language or leave as *Auto Detect*
2. **Select target language** — choose the language to translate into
3. **Type or paste** your text in the input box
4. Click **🌐 Translate**
5. Your translation appears below
6. Click **📋 Copy Translation** to copy it

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| `streamlit: command not found` | Activate your virtual environment first |
| Text is invisible in input box | Make sure `.streamlit/config.toml` exists in the project folder |
| Translation fails | Check your internet connection (requires network access) |
| Blank page in browser | Refresh or open `http://localhost:8501` manually |

---

## 🛠️ Tech Stack

| Library | Purpose | Cost |
|---|---|---|
| [Streamlit](https://streamlit.io) | Web UI framework | Free & open-source |
| [deep-translator](https://github.com/nidhaloff/deep-translator) | Google Translate wrapper | Free, no API key |

---

## 📦 Dependencies

```
streamlit>=1.32.0
deep-translator>=1.11.4
```

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
Translation displayed in the result box
      ↓
User copies with one click
```

---

## 🏢 Internship Details

| | |
|---|---|
| **Program** | CodeAlpha AI Internship |
| **Task** | Task 1 — Language Translation Tool |
| **Intern** | Sehar Andleeb |
| **Degree** | BS Artificial Intelligence (8th Semester) |

---

*Built with ❤️ by Sehar Andleeb — CodeAlpha AI Intern*