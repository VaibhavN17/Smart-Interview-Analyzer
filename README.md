# 🎯 Smart Interview Analyzer

> An AI-powered platform that automates candidate evaluation — analyzing communication, confidence, and technical knowledge to help recruiters hire smarter and faster.

![Stack](https://img.shields.io/badge/Frontend-React_+_TypeScript-61DAFB?style=flat-square&logo=react)
![Stack](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi)
![Stack](https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=flat-square&logo=postgresql)
![Stack](https://img.shields.io/badge/AI-Whisper_+_BERT_+_Gemini-FF6F00?style=flat-square)
![Stack](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Project Structure](#-project-structure)
- [AI Scoring Formula](#-ai-scoring-formula)
- [API Reference](#-api-reference)
- [Documentation](#-documentation)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)

---

## 🧠 Overview

Smart Interview Analyzer solves a core problem in recruitment: **manual evaluation is slow, inconsistent, and hard to scale.**

The platform lets candidates attend text, voice, or video interviews, then automatically:
- Transcribes audio/video responses via **Whisper**
- Scores answers using **semantic similarity (MiniLM)**, keyword coverage, and grammar analysis
- Detects **confidence** from voice tone, speech rate, and pitch
- Generates **AI feedback** (strengths, weaknesses, suggestions) via Gemini API
- Provides recruiters a **ranked dashboard** with skill heatmaps and side-by-side comparisons

### User Roles
| Role | What they do |
|------|-------------|
| **Candidate** | Attend interviews, view reports, track progress |
| **Recruiter** | Create job roles, review and compare candidates, download reports |
| **Admin** | Manage users, question bank, AI model config, platform analytics |

---

## ✨ Features

### For Candidates
- 📄 Resume upload with ATS score + skill gap analysis
- 🎤 Text, Voice, and Video interview modes
- 🤖 AI-generated questions from resume + job description
- 📊 Detailed post-interview report with per-question breakdown
- 📈 Progress tracking across multiple interviews

### For Recruiters
- 🏆 Candidate ranking table by AI-computed final score
- 🔥 Skill heatmap across all candidates
- ⚖️ Side-by-side candidate comparison
- 📥 One-click PDF report download
- 📉 Analytics dashboard (score trends, skill distribution)

### AI Analysis Engine
- **Keyword Coverage** — checks expected domain keywords
- **Semantic Similarity** — MiniLM embeddings vs ideal answer
- **Grammar Analysis** — LanguageTool integration
- **Sentiment Analysis** — VADER / TextBlob
- **Filler Word Detection** — um, uh, basically, like...
- **Voice Confidence** — Librosa (pitch, speech rate, pauses, energy)
- **AI Feedback Generation** — Gemini 1.5 Flash prompt engineering

---

## 🛠 Tech Stack

### Frontend
| Technology | Purpose |
|-----------|---------|
| React 18 + TypeScript | UI framework |
| Tailwind CSS | Styling |
| Recharts | Analytics charts |
| Zustand | State management |
| React Hook Form | Form handling |
| Axios | HTTP client |
| MediaRecorder API | Audio/video recording |

### Backend
| Technology | Purpose |
|-----------|---------|
| FastAPI | REST API framework |
| SQLAlchemy 2 + Alembic | ORM + migrations |
| Celery + Redis | Background job queue |
| python-jose | JWT authentication |
| pdfplumber + spaCy | Resume parsing |
| ReportLab | PDF report generation |
| Pydantic v2 | Request/response validation |

### AI / ML
| Library / Model | Purpose |
|----------------|---------|
| OpenAI Whisper / Faster-Whisper | Speech-to-text |
| sentence-transformers (MiniLM-L6-v2) | Semantic similarity |
| LanguageTool Python | Grammar analysis |
| VADER / TextBlob | Sentiment analysis |
| Librosa | Voice feature extraction |
| OpenCV + MediaPipe | Video confidence (advanced) |
| Gemini 1.5 Flash API | AI feedback generation |

### Infrastructure
| Service | Purpose |
|---------|---------|
| PostgreSQL 15 | Primary database |
| Redis 7 | Cache + Celery broker |
| AWS S3 | Audio, video, resume, PDF storage |
| Cloudinary | Profile photo CDN |
| Docker + Nginx | Containerization + reverse proxy |
| AWS EC2 + RDS | Production deployment |

---

## 🏗 Architecture

```
┌──────────────────────────────────────┐
│        Frontend (React + TS)         │
│   Tailwind  │  Recharts  │  Axios    │
└──────────────────┬───────────────────┘
                   │ REST API
┌──────────────────▼───────────────────┐
│         FastAPI Backend              │
│  Auth │ Resume │ Interview │ Reports │
└───┬──────────────┬───────────────────┘
    │              │
┌───▼────┐   ┌─────▼──────────────────┐
│  PG DB │   │    AI Service Layer    │
│  Redis │   │  Whisper │ MiniLM      │
└────────┘   │  Librosa │ Gemini API  │
             └────────────────────────┘
                         │
              ┌──────────▼──────────┐
              │   AWS S3 / CDN      │
              │  (media + reports)  │
              └─────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker + Docker Compose
- PostgreSQL 15 (or use Docker)
- Redis 7 (or use Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-interview-analyzer.git
cd smart-interview-analyzer
```

### 2. Start with Docker Compose (Recommended)

```bash
cp .env.example .env
# Fill in your API keys in .env

docker-compose up --build
```

This starts:
- `api` — FastAPI on `http://localhost:8000`
- `worker` — Celery background worker
- `db` — PostgreSQL on port `5432`
- `redis` — Redis on port `6379`
- `frontend` — React dev server on `http://localhost:5173`

### 3. Manual Setup (Backend)

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Seed question bank
python scripts/seed_questions.py

# Start API
uvicorn app.main:app --reload --port 8000

# Start Celery worker (separate terminal)
celery -A app.tasks.celery_app worker --loglevel=info
```

### 4. Manual Setup (Frontend)

```bash
cd frontend
npm install
npm run dev
```

### 5. Open the App

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| API Docs (Swagger) | http://localhost:8000/docs |
| API Docs (Redoc) | http://localhost:8000/redoc |

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Application
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# Database
DATABASE_URL=postgresql://postgres:password@localhost:5432/smartinterview

# Redis
REDIS_URL=redis://localhost:6379/0

# AWS S3
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_S3_BUCKET=smart-interview-media
AWS_REGION=ap-south-1

# AI APIs
GEMINI_API_KEY=your-gemini-api-key
OPENAI_API_KEY=your-openai-api-key       # optional fallback

# Cloudinary (profile photos)
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

# Email (OTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
```

---

## 📁 Project Structure

```
smart-interview-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── main.py                  # FastAPI app entry point
│   │   ├── config.py                # Settings via pydantic-settings
│   │   ├── database.py              # SQLAlchemy engine + session
│   │   ├── models/                  # ORM models
│   │   │   ├── user.py
│   │   │   ├── candidate.py
│   │   │   ├── interview.py
│   │   │   ├── question.py
│   │   │   └── report.py
│   │   ├── schemas/                 # Pydantic request/response schemas
│   │   ├── routers/                 # API route handlers
│   │   │   ├── auth.py
│   │   │   ├── candidates.py
│   │   │   ├── interviews.py
│   │   │   ├── recruiter.py
│   │   │   └── admin.py
│   │   ├── services/                # Business logic
│   │   │   ├── nlp_service.py       # Keyword, grammar, sentiment
│   │   │   ├── audio_service.py     # Whisper + Librosa
│   │   │   ├── resume_service.py    # pdfplumber + spaCy
│   │   │   ├── feedback_service.py  # Gemini API
│   │   │   └── report_service.py    # ReportLab PDF
│   │   ├── tasks/                   # Celery background jobs
│   │   │   ├── celery_app.py
│   │   │   ├── analysis_tasks.py
│   │   │   └── report_tasks.py
│   │   └── utils/
│   │       ├── jwt.py
│   │       ├── s3.py
│   │       └── email.py
│   ├── alembic/                     # DB migrations
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── auth/                # Login, Register, OTP
│   │   │   ├── candidate/           # Dashboard, Interview, Report
│   │   │   ├── recruiter/           # Dashboard, Compare, Analytics
│   │   │   └── admin/
│   │   ├── components/
│   │   │   ├── ui/                  # Button, Input, Modal, Badge
│   │   │   ├── interview/           # QuestionCard, Timer, Recorder
│   │   │   ├── report/              # ScoreCard, FeedbackSection
│   │   │   └── charts/              # ScoreTrend, SkillHeatmap
│   │   ├── store/                   # Zustand stores
│   │   ├── hooks/                   # useInterview, useAuth
│   │   ├── services/                # Axios API service functions
│   │   └── types/                   # TypeScript interfaces
│   ├── tailwind.config.ts
│   ├── vite.config.ts
│   └── package.json
│
├── docs/
│   ├── 01_PRD_SmartInterviewAnalyzer.md
│   ├── 02_TRD_SmartInterviewAnalyzer.md
│   ├── 03_AppFlow_SmartInterviewAnalyzer.md
│   ├── 04_UIUXDesignBrief_SmartInterviewAnalyzer.md
│   ├── 05_BackendSchemas_SmartInterviewAnalyzer.md
│   └── 06_ImplementationPlan_SmartInterviewAnalyzer.md
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 📐 AI Scoring Formula

Every completed interview is scored using a weighted formula:

```
Final Score = (0.35 × Technical) + (0.25 × Communication) + (0.20 × Confidence) + (0.20 × Keyword Coverage)
```

**Example:**
```
Technical Score     : 80
Communication Score : 85
Confidence Score    : 70
Keyword Coverage    : 90

Final Score = (0.35×80) + (0.25×85) + (0.20×70) + (0.20×90)
            = 28 + 21.25 + 14 + 18
            = 81.25 / 100
```

Score thresholds: `≥75 = Strong` · `50–74 = Average` · `<50 = Needs Improvement`

---

## 📡 API Reference

Full interactive docs available at `/docs` (Swagger UI) after starting the server.

### Key Endpoints

```
POST   /api/v1/auth/register
POST   /api/v1/auth/login
POST   /api/v1/candidates/resume/upload
GET    /api/v1/candidates/resume/analysis
POST   /api/v1/interviews/start
GET    /api/v1/interviews/:id/questions
POST   /api/v1/interviews/:id/answers
POST   /api/v1/interviews/:id/answers/audio
POST   /api/v1/interviews/:id/submit
GET    /api/v1/interviews/:id/report
GET    /api/v1/interviews/:id/report/pdf
GET    /api/v1/recruiter/candidates
GET    /api/v1/recruiter/compare?a=:id&b=:id
GET    /api/v1/recruiter/analytics
```

---

## 📚 Documentation

All project documentation is in the `/docs` folder:

| Document | Description |
|----------|-------------|
| [PRD](docs/01_PRD_SmartInterviewAnalyzer.md) | Product requirements, user stories, feature specs |
| [TRD](docs/02_TRD_SmartInterviewAnalyzer.md) | Tech stack, API design, AI pipeline, deployment |
| [App Flow](docs/03_AppFlow_SmartInterviewAnalyzer.md) | User flows, state diagrams, error handling |
| [UI/UX Brief](docs/04_UIUXDesignBrief_SmartInterviewAnalyzer.md) | Design tokens, screen layouts, component specs |
| [Backend Schemas](docs/05_BackendSchemas_SmartInterviewAnalyzer.md) | Full PostgreSQL DDL for all 13 tables |
| [Implementation Plan](docs/06_ImplementationPlan_SmartInterviewAnalyzer.md) | 14-week roadmap, task checklist, risk register |

---

## 🗺 Roadmap

### v1.0 — MVP ✅
- [x] Auth (register, login, OTP)
- [x] Resume upload + ATS analysis
- [x] Text-based interview
- [x] NLP scoring engine
- [x] Candidate report page
- [x] Recruiter ranking dashboard

### v1.5 — Current Sprint 🔄
- [ ] Voice interview + Whisper transcription
- [ ] PDF report generation
- [ ] Candidate vs candidate comparison
- [ ] Analytics dashboard

### v2.0 — Advanced Features 🚧
- [ ] Video interview + facial confidence detection
- [ ] Live coding round with test case evaluation
- [ ] Proctoring (tab switch + multi-face detection)
- [ ] Multi-language support (Hindi, Marathi)
- [ ] AI recruiter chatbot ("Show top Python candidates")
- [ ] Emotion detection (happy, nervous, confused)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "feat: add voice confidence scoring"

# 4. Push and open a PR
git push origin feature/your-feature-name
```

Please make sure your code passes linting and tests before submitting:
```bash
# Backend
pytest tests/
flake8 app/

# Frontend
npm run lint
npm run type-check
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Vaibhava**  
B.Tech Computer Science — Final Year Project  
Stack: React · FastAPI · PostgreSQL · AI/ML

---

> ⭐ If this project helped you, consider giving it a star on GitHub!
