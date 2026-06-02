# App Flow Document
## Smart Interview Analyzer

**Version:** 1.0  
**Date:** June 2026

---

## 1. High-Level Application Flow

```
┌─────────────┐     ┌────────────────┐     ┌─────────────────┐
│  Landing    │────▶│  Auth          │────▶│  Role-Based     │
│  Page       │     │  (Login/Reg)   │     │  Dashboard      │
└─────────────┘     └────────────────┘     └────────┬────────┘
                                                    │
                    ┌───────────────────────────────┤
                    │                               │
             ┌──────▼──────┐               ┌────────▼────────┐
             │  Candidate  │               │   Recruiter     │
             │  Dashboard  │               │   Dashboard     │
             └──────┬──────┘               └────────┬────────┘
                    │                               │
     ┌──────────────┼──────────────┐     ┌──────────┼──────────┐
     │              │              │     │          │          │
┌────▼───┐   ┌──────▼──┐   ┌──────▼─┐  ┌▼──────┐ ┌▼───────┐ ┌▼──────┐
│ Resume │   │Interview│   │Reports │  │Create │ │View    │ │Compare│
│ Upload │   │  Flow   │   │& Track │  │Roles  │ │Scores  │ │Cands. │
└────────┘   └─────────┘   └────────┘  └───────┘ └────────┘ └───────┘
```

---

## 2. Candidate Flow — Detailed

### 2.1 Onboarding Flow

```
[1] Visit Landing Page
        ↓
[2] Click "Sign Up as Candidate"
        ↓
[3] Registration Form
    - Name
    - Email
    - Password
    - Phone
        ↓
[4] OTP Verification (email)
        ↓
[5] Profile Setup
    - Upload Resume (PDF/DOCX)
    - Select Target Role
    - Preferred Interview Type
        ↓
[6] Resume Analysis Processing (background job)
    - Extract skills, education, experience
    - Calculate ATS score
    - Identify skill gaps
        ↓
[7] Candidate Dashboard (home)
```

### 2.2 Interview Flow

```
[1] Dashboard → "Start New Interview"
        ↓
[2] Select Interview Type
    ┌─────────────────────────────────┐
    │  [ Text ]  [ Voice ]  [ Video ] │
    └─────────────────────────────────┘
        ↓
[3] Select Job Role (from available roles)
        ↓
[4] Questions loaded
    - Static questions from question bank
    - AI-generated questions from resume + JD
        ↓
[5] Interview Session
    ┌─────────────────────────────────────────────────────┐
    │  For each question (1 to N):                        │
    │    - Display question + difficulty level            │
    │    - Timer starts                                   │
    │    - Candidate responds (type / speak / record)     │
    │    - Confirm & submit answer                        │
    │    - Move to next question                          │
    └─────────────────────────────────────────────────────┘
        ↓
[6] "Submit Interview" clicked
        ↓
[7] Background processing triggered:
    - If audio/video: Whisper transcription
    - NLP analysis per answer
    - Voice/video confidence analysis
    - AI feedback generation
    - Score calculation
    - PDF report generation
        ↓
[8] "Your report is ready" notification (email + in-app)
        ↓
[9] Candidate views report
    - Overall score breakdown
    - Per-question feedback
    - Strengths / Weaknesses / Suggestions
    - Download PDF
```

### 2.3 Progress Tracking Flow
```
Dashboard → "My Progress"
    ↓
View:
  - Score trend graph (line chart over time)
  - Skill improvement table
  - Interview history list
  - Best and latest scores
```

---

## 3. Recruiter Flow — Detailed

### 3.1 Setup Flow
```
[1] Register as Recruiter
[2] Create Company Profile
[3] Create Job Role(s)
    - Role name, description, required skills
[4] Add / select questions for each role
    - From question bank
    - Or write custom questions
[5] Share interview link with candidates
```

### 3.2 Evaluation Flow
```
[1] Recruiter Dashboard → "Candidates"
        ↓
[2] View ranked list of candidates for a job role
    | Name | Score | Technical | Comm. | Confidence | Date |
        ↓
[3] Click on any candidate → Detailed report view
    - Resume summary
    - Per-question analysis
    - AI-generated strengths & weaknesses
    - Score breakdown
    - Recruiter can add manual notes
        ↓
[4] Download PDF report
        ↓
[5] Optionally: Compare two candidates
    - Select Candidate A and Candidate B
    - Side-by-side metrics view
    - Skill heatmap comparison
```

---

## 4. Admin Flow

```
[1] Admin Login → Admin Dashboard
        ↓
    ┌───────────────────────────────────┐
    │  Manage Users   │  Manage Q Bank  │
    │  View Analytics │  AI Config      │
    └───────────────────────────────────┘

User Management:
    - View all users (candidates + recruiters)
    - Activate / Deactivate accounts
    - Reset passwords

Question Bank:
    - Add / edit / delete questions
    - Assign domain tags (Java, Python, SQL, ML...)
    - Set difficulty level

AI Config:
    - Switch between Gemini / GPT / Llama
    - Adjust scoring weights (technical, comm, confidence, keyword)

Analytics:
    - Platform-wide interview counts
    - Average scores by job role
    - Most common skill gaps
```

---

## 5. State Diagram — Interview Session

```
[IDLE]
  ↓  Start Interview
[LOADING_QUESTIONS]
  ↓  Questions ready
[IN_PROGRESS]
  ├── Answer submitted → [NEXT_QUESTION] → loop back to IN_PROGRESS
  └── All questions done
[SUBMITTING]
  ↓  API confirms submission
[PROCESSING]
  ↓  Background jobs complete
[REPORT_READY]
  ↓  User views report
[COMPLETED]
```

---

## 6. Notification Flow

| Event | Channel | Recipient |
|-------|---------|-----------|
| OTP sent | Email | Candidate/Recruiter |
| Interview report ready | Email + In-app | Candidate |
| New candidate completed interview | In-app | Recruiter |
| Resume analysis complete | In-app | Candidate |
| Password reset | Email | All users |

---

## 7. Error Flow Handling

| Scenario | Behavior |
|----------|----------|
| Audio upload fails | Show retry button; allow text fallback |
| Whisper transcription fails | Mark answer as "manual review needed" |
| AI feedback API timeout | Use rule-based fallback feedback |
| Session timeout mid-interview | Auto-save progress; resume on next login |
| Invalid file type on resume upload | Show accepted formats error |
