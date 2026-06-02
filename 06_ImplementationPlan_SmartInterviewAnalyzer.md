# Implementation Plan
## Smart Interview Analyzer

**Version:** 1.0  
**Date:** June 2026  
**Timeline:** 14 Weeks (3.5 Months)  
**Team Size:** 1–2 developers (B.Tech final year project)

---

## 1. Project Phases Overview

| Phase | Name | Duration | Weeks |
|-------|------|----------|-------|
| 0 | Setup & Architecture | 1 week | 1 |
| 1 | Auth & User Management | 2 weeks | 2–3 |
| 2 | Resume & Question Module | 2 weeks | 4–5 |
| 3 | Interview Core | 2 weeks | 6–7 |
| 4 | AI Analysis Engine | 2 weeks | 8–9 |
| 5 | Recruiter Dashboard | 2 weeks | 10–11 |
| 6 | Reports & Analytics | 1 week | 12 |
| 7 | Polish, Testing & Deploy | 2 weeks | 13–14 |

---

## 2. Phase 0 — Project Setup (Week 1)

### Goal
Scaffold the full project with folder structure, tooling, DB, and CI ready.

### Tasks

**Backend**
- [ ] Initialize FastAPI project with `pyproject.toml` / `requirements.txt`
- [ ] Set up folder structure: `app/routers`, `app/models`, `app/schemas`, `app/services`, `app/utils`
- [ ] Configure PostgreSQL connection via SQLAlchemy
- [ ] Set up Alembic for migrations
- [ ] Configure Redis connection
- [ ] Set up Celery worker
- [ ] Configure `.env` with all environment variables
- [ ] Create `docker-compose.yml` (api, db, redis, worker)

**Frontend**
- [ ] Initialize React + TypeScript project with Vite
- [ ] Configure Tailwind CSS
- [ ] Set up React Router with route structure
- [ ] Configure Axios instance with base URL + interceptors
- [ ] Set up Zustand store
- [ ] Create base layout components (Sidebar, Navbar, PageWrapper)

**Database**
- [ ] Write and run initial migration (all 13 tables + enums)
- [ ] Seed: 20 sample questions across 4 domains

**Deliverable:** Running `docker-compose up` brings up API, DB, Redis, and frontend dev server.

---

## 3. Phase 1 — Auth & User Management (Weeks 2–3)

### Goal
Users can register, verify, log in, and access role-specific dashboards.

### Backend Tasks
- [ ] `POST /auth/register` — hash password, create user + role record
- [ ] `POST /auth/login` — validate credentials, return JWT pair
- [ ] `POST /auth/refresh` — validate refresh token, return new access token
- [ ] OTP generation and email delivery (SMTP)
- [ ] `POST /auth/verify-otp`
- [ ] `POST /auth/forgot-password` + `POST /auth/reset-password`
- [ ] JWT middleware (dependency injection in FastAPI)
- [ ] RBAC decorator / role guard

### Frontend Tasks
- [ ] Register page (candidate / recruiter toggle)
- [ ] Login page
- [ ] OTP verification screen
- [ ] Forgot password flow
- [ ] Auth context with token storage (memory + refresh token in httpOnly cookie)
- [ ] Protected route wrapper (redirects by role)
- [ ] Candidate dashboard shell (sidebar + placeholder main)
- [ ] Recruiter dashboard shell

**Deliverable:** Full registration → OTP → login → role-based dashboard flow working.

---

## 4. Phase 2 — Resume & Question Module (Weeks 4–5)

### Goal
Candidates can upload a resume and get it analyzed. Recruiters can manage job roles and questions.

### Backend Tasks — Resume
- [ ] `POST /candidates/resume/upload` — upload to S3, trigger Celery parse job
- [ ] Celery task: pdfplumber + spaCy extraction (name, skills, projects, education)
- [ ] ATS score calculation (keyword matching against target role)
- [ ] Skill gap analysis
- [ ] `GET /candidates/resume/analysis` — return analysis results

### Backend Tasks — Questions
- [ ] `POST /recruiter/job-roles` — create job role
- [ ] `GET /recruiter/job-roles` — list roles
- [ ] `POST /recruiter/questions` — add custom question
- [ ] `GET /recruiter/questions` — paginated question bank
- [ ] AI question generation: build Gemini prompt from resume + JD → parse response → store
- [ ] `GET /candidates/questions/suggested` — questions for candidate based on resume

### Frontend Tasks
- [ ] Resume upload component (drag-and-drop + file picker)
- [ ] Resume analysis results card (ATS score, skill tags, gaps)
- [ ] Job role creation form (recruiter)
- [ ] Question bank table with filters (recruiter)
- [ ] Add question modal

**Deliverable:** Resume upload → parsing → ATS score visible on dashboard. Recruiter can create job roles with questions.

---

## 5. Phase 3 — Interview Core Module (Weeks 6–7)

### Goal
Candidates can take text-based and voice-based interviews end-to-end.

### Backend Tasks
- [ ] `POST /interviews/start` — create interview session, load questions
- [ ] `GET /interviews/:id/questions` — return ordered questions
- [ ] `POST /interviews/:id/answers` — save text answer
- [ ] `POST /interviews/:id/answers/audio` — upload audio to S3
- [ ] Celery task: Whisper transcription of audio file
- [ ] `POST /interviews/:id/submit` — finalize, trigger full analysis pipeline
- [ ] Interview session state machine (pending → in_progress → submitted → processing → completed)
- [ ] Auto-save on timeout

### Frontend Tasks
- [ ] Interview setup screen (type selection, job role)
- [ ] Interview session screen:
  - Question card with timer
  - Text answer textarea
  - Audio recording UI (MediaRecorder API, waveform via Web Audio API)
  - Video recording UI (camera preview)
- [ ] Progress bar (Q3 of 10)
- [ ] Submit interview confirmation modal
- [ ] Processing screen (animated status steps)

**Deliverable:** A candidate can start → answer all questions (text + voice) → submit → see "processing" screen.

---

## 6. Phase 4 — AI Analysis Engine (Weeks 8–9)

### Goal
Every submitted interview gets scored and AI feedback generated automatically.

### Backend Tasks — NLP Pipeline
- [ ] Keyword extraction and coverage scoring function
- [ ] Semantic similarity via `sentence-transformers` (MiniLM-L6-v2)
- [ ] Grammar scoring via LanguageTool Python API
- [ ] Sentiment analysis via VADER
- [ ] Filler word count function (regex-based)
- [ ] Communication score aggregation

### Backend Tasks — Voice Pipeline
- [ ] Librosa feature extraction: speech rate, pitch variation, pause frequency, energy
- [ ] Confidence score formula

### Backend Tasks — Scoring & Feedback
- [ ] Final score formula: `0.35T + 0.25C + 0.20Conf + 0.20K`
- [ ] AI feedback generation: Gemini API prompt (with strengths/weaknesses/suggestions)
- [ ] Store all results in `interview_answers`, `analysis_results`, `interviews` tables

### Frontend Tasks
- [ ] Report page — score breakdown with animated bars
- [ ] AI feedback section (strengths, weaknesses, suggestions)
- [ ] Per-question accordion with individual scores
- [ ] "Report Ready" notification (in-app toast + email)

**Deliverable:** Full end-to-end: interview → analysis → detailed report visible to candidate.

---

## 7. Phase 5 — Recruiter Dashboard (Weeks 10–11)

### Goal
Recruiters can view, compare, and shortlist candidates with rich data.

### Backend Tasks
- [ ] `GET /recruiter/candidates` — ranked list with filters
- [ ] `GET /recruiter/candidates/:id` — full candidate report view
- [ ] `GET /recruiter/compare?a=:id&b=:id` — comparison data
- [ ] `PATCH /recruiter/reports/:id/notes` — add recruiter notes
- [ ] `GET /recruiter/analytics` — aggregated stats

### Frontend Tasks
- [ ] Candidate ranking table (sortable, filterable by role/score/date)
- [ ] Candidate detail modal / page
- [ ] Comparison view (side-by-side metric cards)
- [ ] Skill heatmap (Recharts HeatMapChart or custom SVG grid)
- [ ] Download PDF button

**Deliverable:** Recruiter dashboard fully functional with live candidate data.

---

## 8. Phase 6 — Reports & Analytics (Week 12)

### Goal
PDF reports are auto-generated. Analytics dashboard is populated.

### Backend Tasks
- [ ] Celery task: generate PDF report using ReportLab
  - Candidate profile section
  - Score breakdown table
  - AI feedback narrative
  - Per-question scores table
  - Recruiter notes section
- [ ] Upload PDF to S3, store URL in `reports` table
- [ ] `GET /interviews/:id/report/pdf` — stream PDF download
- [ ] Analytics aggregation queries (avg scores, skill distribution, trends)

### Frontend Tasks
- [ ] Analytics page (Recharts: line chart, bar chart, donut chart)
- [ ] PDF download flow (trigger generation if not ready; download when done)
- [ ] Candidate progress page (score over time line chart)

**Deliverable:** PDF reports downloadable. Analytics dashboard showing real data.

---

## 9. Phase 7 — Polish, Testing & Deployment (Weeks 13–14)

### Goal
Production-ready build, tested and deployed.

### Testing Tasks
- [ ] Backend unit tests: scoring functions, NLP utils, auth (pytest)
- [ ] Backend integration tests: interview submission flow (TestClient)
- [ ] Frontend: manual E2E walkthrough of all 3 user flows
- [ ] Load test: simulate 50 concurrent interview submissions

### Polish Tasks
- [ ] Responsive design fixes (mobile / tablet)
- [ ] Error boundaries in React
- [ ] Toast notifications for all async operations
- [ ] Loading skeletons on all data-fetching components
- [ ] Empty states for all list/table views
- [ ] Form validation (all forms have inline errors)

### Deployment Tasks
- [ ] Dockerize FastAPI app + Nginx reverse proxy
- [ ] Set up EC2 instance (t3.medium)
- [ ] Configure RDS PostgreSQL (db.t3.micro)
- [ ] Set up S3 bucket with proper CORS and IAM policy
- [ ] Configure CloudFront for React static build
- [ ] Set environment variables in EC2 / Secrets Manager
- [ ] Run Alembic migrations on production DB
- [ ] Configure systemd service for Celery worker
- [ ] Set up GitHub Actions CI: lint + test on every push

**Deliverable:** Live URL with full working product. Ready for project demo.

---

## 10. MVP vs Full Build Prioritization

### Must Build (MVP — Weeks 1–9)
- Auth + roles
- Resume upload + parsing
- Text-based interview
- NLP analysis + scoring
- Basic report page
- Candidate dashboard

### Should Build (Weeks 10–12)
- Voice interview + Whisper
- Recruiter dashboard
- PDF reports
- Comparison view
- Analytics charts

### Nice to Have (Post-MVP / v2)
- Video interview + face analysis
- Live coding round
- Proctoring
- Multi-language support
- AI recruiter chatbot

---

## 11. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Whisper too slow on CPU | Medium | High | Use faster-whisper with int8 quantization; fallback to cloud API |
| Gemini API rate limits | Medium | Medium | Cache prompts; queue requests; fallback to rule-based feedback |
| Resume parsing accuracy | High | Medium | Normalize with spaCy NER; allow manual skill input by candidate |
| Large audio/video uploads | Medium | Medium | Limit size (50MB/200MB); chunk upload with presigned S3 URLs |
| Scoring inconsistency | Low | High | Normalize all sub-scores to 0–1 before weighting |

---

## 12. Folder Structure

### Backend
```
backend/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── user.py
│   │   ├── candidate.py
│   │   ├── interview.py
│   │   └── ...
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── interview.py
│   │   └── ...
│   ├── routers/
│   │   ├── auth.py
│   │   ├── candidates.py
│   │   ├── interviews.py
│   │   ├── recruiter.py
│   │   └── admin.py
│   ├── services/
│   │   ├── nlp_service.py
│   │   ├── audio_service.py
│   │   ├── resume_service.py
│   │   ├── feedback_service.py
│   │   └── report_service.py
│   ├── tasks/
│   │   ├── celery_app.py
│   │   ├── analysis_tasks.py
│   │   └── report_tasks.py
│   └── utils/
│       ├── jwt.py
│       ├── s3.py
│       └── email.py
├── alembic/
├── tests/
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

### Frontend
```
frontend/
├── src/
│   ├── pages/
│   │   ├── auth/
│   │   ├── candidate/
│   │   ├── recruiter/
│   │   └── admin/
│   ├── components/
│   │   ├── ui/              # Button, Input, Modal, Badge...
│   │   ├── interview/       # QuestionCard, Timer, Recorder...
│   │   ├── report/          # ScoreCard, FeedbackSection...
│   │   └── charts/          # ScoreTrend, SkillHeatmap...
│   ├── store/               # Zustand stores
│   ├── hooks/               # useInterview, useAuth...
│   ├── services/            # API service functions
│   ├── types/               # TypeScript interfaces
│   └── utils/
├── public/
├── tailwind.config.ts
├── vite.config.ts
└── package.json
```
