# Technical Requirements Document (TRD)
## Smart Interview Analyzer

**Version:** 1.0  
**Date:** June 2026  
**Author:** Project Team  
**Status:** Draft

---

## 1. System Architecture Overview

```
┌────────────────────────────────────────────────────┐
│                 Frontend (React + TS)               │
│         Tailwind CSS  │  Recharts  │  Axios         │
└────────────────────────┬───────────────────────────┘
                         │ REST API / WebSocket
┌────────────────────────▼───────────────────────────┐
│               FastAPI Backend (Python)              │
│   Auth  │  Resume  │  Interview  │  Analytics       │
└──────┬──────────────┬──────────────────┬────────────┘
       │              │                  │
┌──────▼──────┐ ┌─────▼──────┐  ┌───────▼───────┐
│ PostgreSQL  │ │  Redis      │  │  AI Service   │
│  (Primary)  │ │  (Cache/    │  │  Layer        │
│             │ │   Queue)    │  │               │
└─────────────┘ └────────────┘  │  ┌───────────┐ │
                                │  │  Whisper  │ │
                                │  │  BERT/    │ │
                                │  │  MiniLM   │ │
                                │  │  Gemini   │ │
                                │  │  OpenCV   │ │
                                │  └───────────┘ │
                                └────────────────┘
                                        │
                              ┌─────────▼──────────┐
                              │   AWS S3 / Cloudinary│
                              │  (Media Storage)     │
                              └──────────────────────┘
```

---

## 2. Technology Stack

### 2.1 Frontend
| Layer | Technology | Version |
|-------|-----------|---------|
| Framework | React | 18.x |
| Language | TypeScript | 5.x |
| Styling | Tailwind CSS | 3.x |
| Charts | Recharts | 2.x |
| HTTP Client | Axios | 1.x |
| Routing | React Router | 6.x |
| State Management | Zustand | 4.x |
| Form Handling | React Hook Form | 7.x |
| Media Recording | MediaRecorder API (native) | — |

### 2.2 Backend
| Layer | Technology | Version |
|-------|-----------|---------|
| Framework | FastAPI | 0.110+ |
| Language | Python | 3.11+ |
| ORM | SQLAlchemy | 2.x |
| Migrations | Alembic | 1.x |
| Task Queue | Celery + Redis | 5.x |
| Auth | python-jose (JWT) | 3.x |
| File Handling | python-multipart | — |
| PDF Generation | ReportLab | 4.x |
| Validation | Pydantic | 2.x |

### 2.3 Database
| Type | Technology |
|------|-----------|
| Primary DB | PostgreSQL 15 |
| Cache / Broker | Redis 7 |
| Object Storage | AWS S3 (audio/video files) |
| Media CDN | Cloudinary (thumbnails) |

### 2.4 AI / ML Stack
| Purpose | Library / Model |
|---------|----------------|
| Speech-to-Text | OpenAI Whisper / Faster-Whisper |
| Semantic Similarity | Sentence Transformers (MiniLM-L6-v2) |
| Grammar Analysis | LanguageTool Python API |
| Sentiment Analysis | TextBlob / VADER |
| Voice Feature Extraction | Librosa |
| Video / Face Analysis | OpenCV + MediaPipe |
| Resume Parsing | pdfplumber + spaCy |
| AI Feedback Generation | Gemini 1.5 Flash API / GPT-4o Mini |

---

## 3. API Design

### 3.1 Base URL
```
https://api.smartinterview.app/v1
```

### 3.2 Auth Endpoints
```
POST   /auth/register          → Register user
POST   /auth/login             → Login, returns JWT
POST   /auth/refresh           → Refresh access token
POST   /auth/forgot-password   → Send reset email
POST   /auth/reset-password    → Reset with token
POST   /auth/verify-otp        → Verify OTP
```

### 3.3 Candidate Endpoints
```
GET    /candidates/me                  → Get own profile
PUT    /candidates/me                  → Update profile
POST   /candidates/resume/upload       → Upload resume PDF/DOCX
GET    /candidates/resume/analysis     → Get resume analysis result
GET    /candidates/interviews          → List own interviews
GET    /candidates/interviews/:id      → Interview detail + report
GET    /candidates/progress            → Score history over time
```

### 3.4 Interview Endpoints
```
POST   /interviews/start               → Create interview session
GET    /interviews/:id/questions       → Get questions for session
POST   /interviews/:id/answers         → Submit text answer
POST   /interviews/:id/answers/audio   → Upload audio answer
POST   /interviews/:id/answers/video   → Upload video answer
POST   /interviews/:id/submit          → Finalize interview
GET    /interviews/:id/report          → Get full report
GET    /interviews/:id/report/pdf      → Download PDF
```

### 3.5 Recruiter Endpoints
```
GET    /recruiter/job-roles            → List job roles
POST   /recruiter/job-roles            → Create job role
PUT    /recruiter/job-roles/:id        → Update job role
POST   /recruiter/questions            → Add question to bank
GET    /recruiter/candidates           → List all candidates with scores
GET    /recruiter/candidates/:id       → Candidate detail
GET    /recruiter/compare?a=:id&b=:id  → Compare two candidates
GET    /recruiter/analytics            → Aggregated analytics
```

### 3.6 Admin Endpoints
```
GET    /admin/users                    → List all users
PATCH  /admin/users/:id/status         → Activate/deactivate
GET    /admin/questions                → Manage question bank
GET    /admin/analytics                → Platform-wide metrics
PUT    /admin/config/ai                → Update AI model config
```

---

## 4. Authentication & Authorization

- **JWT tokens:** Access token (15 min) + Refresh token (7 days)
- **RBAC Roles:** `candidate`, `recruiter`, `admin`
- **Middleware:** Every protected route validates JWT and checks role
- **Password:** Hashed with `bcrypt` (12 rounds)
- **OTP:** 6-digit numeric, 10-minute expiry, stored in Redis

---

## 5. AI Service Layer — Technical Specs

### 5.1 NLP Pipeline (per text answer)
```
Input: raw_text (str)
  ↓
Step 1: Preprocessing (lowercase, remove stopwords)
  ↓
Step 2: Keyword Extraction → keyword_coverage_score (float 0–1)
  ↓
Step 3: Semantic Similarity via MiniLM → similarity_score (float 0–1)
  ↓
Step 4: Grammar Check via LanguageTool → grammar_score (float 0–1)
  ↓
Step 5: Sentiment Analysis via VADER → sentiment (pos/neu/neg)
  ↓
Step 6: Filler Word Count → filler_count (int)
  ↓
Step 7: Communication Score = weighted aggregate
Output: NLPResult (JSON)
```

### 5.2 Audio Pipeline (per voice answer)
```
Input: audio_file (wav/mp3)
  ↓
Step 1: Whisper transcription → transcript (str)
  ↓
Step 2: NLP pipeline on transcript
  ↓
Step 3: Librosa feature extraction:
        - speech_rate (words/min)
        - pitch_variation (Hz std dev)
        - pause_count (int)
        - energy_mean (float)
  ↓
Step 4: Confidence Score = f(speech_rate, pitch, pauses, energy)
Output: AudioAnalysisResult (JSON)
```

### 5.3 Scoring Formula
```python
final_score = (
    0.35 * technical_score +
    0.25 * communication_score +
    0.20 * confidence_score +
    0.20 * keyword_coverage_score
) * 100  # scaled to 0–100
```

### 5.4 AI Feedback Generation
```
Input: {
  questions: [...],
  candidate_answers: [...],
  nlp_results: [...],
  scores: {...}
}
  ↓
Prompt Engineering → Gemini 1.5 Flash / GPT-4o Mini
  ↓
Output: {
  strengths: [str, ...],
  weaknesses: [str, ...],
  suggestions: [str, ...]
}
```

---

## 6. File Storage Strategy

| File Type | Storage | Max Size | Format |
|-----------|---------|----------|--------|
| Resume | AWS S3 | 5 MB | PDF, DOCX |
| Audio answers | AWS S3 | 50 MB | WebM, MP3, WAV |
| Video answers | AWS S3 | 200 MB | WebM, MP4 |
| Generated PDF reports | AWS S3 | 10 MB | PDF |
| Profile photos | Cloudinary | 2 MB | JPEG, PNG |

---

## 7. Background Job Processing

Using **Celery** with **Redis** as broker:

| Job | Trigger | Priority |
|-----|---------|----------|
| Resume parsing | On upload | High |
| Audio transcription (Whisper) | On answer submit | High |
| NLP analysis | After transcription | High |
| AI feedback generation | After all answers scored | Medium |
| PDF report generation | On interview finalize | Medium |
| Analytics aggregation | Nightly cron | Low |

---

## 8. Security Requirements

- HTTPS enforced on all endpoints
- CORS whitelist for frontend origin only
- Rate limiting: 100 req/min per IP (unauthenticated), 500 req/min (authenticated)
- File upload: MIME type validation + virus scan hook
- SQL injection prevention via SQLAlchemy ORM (no raw queries)
- Secrets managed via `.env` + AWS Secrets Manager in production

---

## 9. Deployment Architecture

```
Route 53 (DNS)
    ↓
CloudFront (CDN for React static assets)
    ↓
Application Load Balancer
    ↓
EC2 (FastAPI via Uvicorn + Nginx)
    ↓
RDS PostgreSQL (Multi-AZ)
ElastiCache Redis
S3 (media storage)
```

**Local Development:**
```
Docker Compose:
  - api (FastAPI)
  - db (PostgreSQL)
  - redis
  - worker (Celery)
```

---

## 10. Environment Variables

```env
# App
SECRET_KEY=
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# Database
DATABASE_URL=postgresql://user:pass@localhost/smartinterview

# Redis
REDIS_URL=redis://localhost:6379/0

# AWS
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_BUCKET=

# AI APIs
GEMINI_API_KEY=
OPENAI_API_KEY=

# Email (OTP)
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=
```
