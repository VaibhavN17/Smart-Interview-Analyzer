# Backend Schemas — Database Design
## Smart Interview Analyzer

**Version:** 1.0  
**Date:** June 2026  
**Database:** PostgreSQL 15

---

## 1. Entity Relationship Overview

```
users
  ├── candidates (1:1)
  ├── recruiters (1:1)
  └── admins (1:1)

recruiters
  └── job_roles (1:N)
        └── interview_questions (M:N via job_role_questions)

candidates
  ├── resumes (1:1)
  └── interviews (1:N)
        ├── interview_answers (1:N)
        │     └── analysis_results (1:1)
        └── reports (1:1)

questions
  └── interview_questions (M:N via job_role_questions)
```

---

## 2. Full DDL

### 2.1 ENUMS

```sql
-- User roles
CREATE TYPE user_role AS ENUM ('candidate', 'recruiter', 'admin');

-- Interview types
CREATE TYPE interview_type AS ENUM ('text', 'voice', 'video');

-- Interview status
CREATE TYPE interview_status AS ENUM (
  'pending', 'in_progress', 'submitted', 'processing', 'completed', 'failed'
);

-- Question difficulty
CREATE TYPE question_difficulty AS ENUM ('easy', 'medium', 'hard');

-- Question domain
CREATE TYPE question_domain AS ENUM (
  'java', 'python', 'sql', 'machine_learning',
  'system_design', 'react', 'devops', 'general'
);

-- Sentiment
CREATE TYPE sentiment_type AS ENUM ('positive', 'neutral', 'negative');
```

---

### 2.2 USERS TABLE

```sql
CREATE TABLE users (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email           VARCHAR(255) NOT NULL UNIQUE,
  password_hash   VARCHAR(255) NOT NULL,
  role            user_role NOT NULL,
  full_name       VARCHAR(150) NOT NULL,
  phone           VARCHAR(20),
  profile_photo   TEXT,                          -- Cloudinary URL
  is_active       BOOLEAN NOT NULL DEFAULT TRUE,
  is_verified     BOOLEAN NOT NULL DEFAULT FALSE,
  otp_secret      VARCHAR(10),
  otp_expires_at  TIMESTAMPTZ,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
```

---

### 2.3 CANDIDATES TABLE

```sql
CREATE TABLE candidates (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         UUID NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
  target_role     VARCHAR(100),
  skills          TEXT[],                        -- parsed from resume
  education       JSONB,                         -- {degree, institution, year}
  experience_years SMALLINT DEFAULT 0,
  linkedin_url    TEXT,
  github_url      TEXT,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_candidates_user_id ON candidates(user_id);
```

---

### 2.4 RECRUITERS TABLE

```sql
CREATE TABLE recruiters (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         UUID NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
  company_name    VARCHAR(200) NOT NULL,
  company_website TEXT,
  industry        VARCHAR(100),
  team_size       SMALLINT,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_recruiters_user_id ON recruiters(user_id);
```

---

### 2.5 RESUMES TABLE

```sql
CREATE TABLE resumes (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  candidate_id        UUID NOT NULL UNIQUE REFERENCES candidates(id) ON DELETE CASCADE,
  file_url            TEXT NOT NULL,                  -- AWS S3 URL
  file_name           VARCHAR(255) NOT NULL,
  file_type           VARCHAR(10) NOT NULL,           -- 'pdf' or 'docx'
  raw_text            TEXT,                           -- extracted plain text
  parsed_skills       TEXT[],
  parsed_projects     JSONB,
  parsed_education    JSONB,
  parsed_experience   JSONB,
  ats_score           NUMERIC(5,2),                   -- 0.00 to 100.00
  skill_gaps          TEXT[],
  missing_keywords    TEXT[],
  analysis_status     VARCHAR(20) DEFAULT 'pending',  -- pending | done | failed
  analyzed_at         TIMESTAMPTZ,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_resumes_candidate_id ON resumes(candidate_id);
```

---

### 2.6 JOB ROLES TABLE

```sql
CREATE TABLE job_roles (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recruiter_id        UUID NOT NULL REFERENCES recruiters(id) ON DELETE CASCADE,
  title               VARCHAR(150) NOT NULL,
  description         TEXT,
  required_skills     TEXT[],
  experience_required SMALLINT DEFAULT 0,            -- years
  is_active           BOOLEAN NOT NULL DEFAULT TRUE,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_job_roles_recruiter_id ON job_roles(recruiter_id);
```

---

### 2.7 QUESTIONS TABLE

```sql
CREATE TABLE questions (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  text                TEXT NOT NULL,
  domain              question_domain NOT NULL,
  difficulty          question_difficulty NOT NULL DEFAULT 'medium',
  expected_keywords   TEXT[],
  ideal_answer        TEXT,
  is_ai_generated     BOOLEAN NOT NULL DEFAULT FALSE,
  created_by          UUID REFERENCES users(id),     -- NULL = system/admin
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_questions_domain ON questions(domain);
CREATE INDEX idx_questions_difficulty ON questions(difficulty);
```

---

### 2.8 JOB ROLE QUESTIONS (Junction Table)

```sql
CREATE TABLE job_role_questions (
  job_role_id     UUID NOT NULL REFERENCES job_roles(id) ON DELETE CASCADE,
  question_id     UUID NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
  order_index     SMALLINT NOT NULL DEFAULT 0,
  PRIMARY KEY (job_role_id, question_id)
);

CREATE INDEX idx_jrq_job_role_id ON job_role_questions(job_role_id);
```

---

### 2.9 INTERVIEWS TABLE

```sql
CREATE TABLE interviews (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  candidate_id        UUID NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
  job_role_id         UUID REFERENCES job_roles(id) ON DELETE SET NULL,
  type                interview_type NOT NULL,
  status              interview_status NOT NULL DEFAULT 'pending',
  total_questions     SMALLINT NOT NULL DEFAULT 0,
  answered_questions  SMALLINT NOT NULL DEFAULT 0,
  final_score         NUMERIC(5,2),                  -- 0.00 to 100.00
  technical_score     NUMERIC(5,2),
  communication_score NUMERIC(5,2),
  confidence_score    NUMERIC(5,2),
  keyword_score       NUMERIC(5,2),
  started_at          TIMESTAMPTZ,
  submitted_at        TIMESTAMPTZ,
  completed_at        TIMESTAMPTZ,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_interviews_candidate_id ON interviews(candidate_id);
CREATE INDEX idx_interviews_job_role_id ON interviews(job_role_id);
CREATE INDEX idx_interviews_status ON interviews(status);
CREATE INDEX idx_interviews_created_at ON interviews(created_at DESC);
```

---

### 2.10 INTERVIEW ANSWERS TABLE

```sql
CREATE TABLE interview_answers (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  interview_id        UUID NOT NULL REFERENCES interviews(id) ON DELETE CASCADE,
  question_id         UUID NOT NULL REFERENCES questions(id),
  question_order      SMALLINT NOT NULL,

  -- Answer content
  text_answer         TEXT,
  audio_url           TEXT,                          -- S3 URL
  video_url           TEXT,                          -- S3 URL
  transcript          TEXT,                          -- Whisper output

  -- Raw scores (0.0 to 1.0)
  technical_score     NUMERIC(4,3),
  communication_score NUMERIC(4,3),
  confidence_score    NUMERIC(4,3),
  keyword_coverage    NUMERIC(4,3),
  semantic_similarity NUMERIC(4,3),
  grammar_score       NUMERIC(4,3),
  sentiment           sentiment_type,
  filler_word_count   SMALLINT DEFAULT 0,

  -- Voice metrics
  speech_rate         NUMERIC(6,2),                 -- words per minute
  pitch_variation     NUMERIC(6,3),
  pause_count         SMALLINT,
  energy_mean         NUMERIC(8,4),

  submitted_at        TIMESTAMPTZ,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_answers_interview_id ON interview_answers(interview_id);
CREATE INDEX idx_answers_question_id ON interview_answers(question_id);
```

---

### 2.11 ANALYSIS RESULTS TABLE

```sql
CREATE TABLE analysis_results (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  interview_id        UUID NOT NULL UNIQUE REFERENCES interviews(id) ON DELETE CASCADE,

  -- AI-generated narrative feedback
  strengths           TEXT[],
  weaknesses          TEXT[],
  suggestions         TEXT[],
  overall_summary     TEXT,

  -- Aggregate keyword stats
  total_keywords_expected INTEGER DEFAULT 0,
  total_keywords_covered  INTEGER DEFAULT 0,

  -- AI model used
  ai_model_used       VARCHAR(100),
  processing_time_ms  INTEGER,
  status              VARCHAR(20) DEFAULT 'pending',  -- pending | done | failed
  error_message       TEXT,

  analyzed_at         TIMESTAMPTZ,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_analysis_interview_id ON analysis_results(interview_id);
```

---

### 2.12 REPORTS TABLE

```sql
CREATE TABLE reports (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  interview_id        UUID NOT NULL UNIQUE REFERENCES interviews(id) ON DELETE CASCADE,
  candidate_id        UUID NOT NULL REFERENCES candidates(id),
  pdf_url             TEXT,                           -- S3 URL of generated PDF
  recruiter_notes     TEXT,
  is_shared           BOOLEAN NOT NULL DEFAULT FALSE,
  share_token         UUID UNIQUE DEFAULT gen_random_uuid(),
  generated_at        TIMESTAMPTZ,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_reports_interview_id ON reports(interview_id);
CREATE INDEX idx_reports_candidate_id ON reports(candidate_id);
CREATE INDEX idx_reports_share_token ON reports(share_token);
```

---

### 2.13 REFRESH TOKENS TABLE

```sql
CREATE TABLE refresh_tokens (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  token_hash    VARCHAR(255) NOT NULL UNIQUE,
  expires_at    TIMESTAMPTZ NOT NULL,
  is_revoked    BOOLEAN NOT NULL DEFAULT FALSE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_refresh_tokens_user_id ON refresh_tokens(user_id);
CREATE INDEX idx_refresh_tokens_token_hash ON refresh_tokens(token_hash);
```

---

## 3. Key JSONB Field Structures

### education (in candidates)
```json
[
  {
    "degree": "B.Tech Computer Science",
    "institution": "VJTI Mumbai",
    "year_of_passing": 2026,
    "percentage": 8.4
  }
]
```

### parsed_projects (in resumes)
```json
[
  {
    "name": "DigiAgro",
    "description": "Farm management platform",
    "tech_stack": ["Next.js", "FastAPI", "PostgreSQL"],
    "url": "https://github.com/..."
  }
]
```

---

## 4. Useful Queries

### Top candidates for a job role
```sql
SELECT
  u.full_name,
  i.final_score,
  i.technical_score,
  i.communication_score,
  i.confidence_score
FROM interviews i
JOIN candidates c ON c.id = i.candidate_id
JOIN users u ON u.id = c.user_id
WHERE i.job_role_id = :job_role_id
  AND i.status = 'completed'
ORDER BY i.final_score DESC
LIMIT 20;
```

### Average scores by domain over last 30 days
```sql
SELECT
  q.domain,
  AVG(ia.technical_score) AS avg_technical,
  AVG(ia.communication_score) AS avg_communication,
  COUNT(ia.id) AS answer_count
FROM interview_answers ia
JOIN questions q ON q.id = ia.question_id
WHERE ia.created_at >= NOW() - INTERVAL '30 days'
GROUP BY q.domain
ORDER BY avg_technical DESC;
```

### Candidate progress over time
```sql
SELECT
  DATE(i.completed_at) AS interview_date,
  i.final_score
FROM interviews i
WHERE i.candidate_id = :candidate_id
  AND i.status = 'completed'
ORDER BY i.completed_at ASC;
```
