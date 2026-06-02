# Product Requirements Document (PRD)
## Smart Interview Analyzer

**Version:** 1.0  
**Date:** June 2026  
**Author:** Project Team  
**Status:** Draft

---

## 1. Executive Summary

Smart Interview Analyzer is an AI-powered platform that automates the evaluation of job candidates during interviews. It analyzes communication quality, technical knowledge, and confidence using NLP, speech processing, and computer vision — reducing recruiter effort and improving hiring decisions.

---

## 2. Problem Statement

Recruiters spend significant time manually evaluating candidates across multiple interviews. The process is:

- **Time-intensive** — each interview requires manual review and notes
- **Inconsistent** — scores vary by recruiter bias and fatigue
- **Non-scalable** — growing hiring needs outpace recruiter bandwidth
- **Poorly documented** — feedback is often informal and lost

**Solution:** An automated platform that records, transcribes, scores, and generates structured feedback for every candidate interview.

---

## 3. Goals & Objectives

| Goal | Metric |
|------|--------|
| Reduce recruiter evaluation time | By ≥ 50% |
| Provide consistent scoring | Variance < 5% across same answer |
| Generate actionable feedback | Per candidate, per question |
| Enable data-driven hiring | Recruiter dashboard with comparisons |
| Support 3 interview modes | Text, Voice, Video |

---

## 4. Target Users

### 4.1 Candidates
- Final-year students / fresh graduates seeking jobs
- Working professionals applying for new roles
- Users who want to practice and improve interview skills

### 4.2 Recruiters
- HR professionals at companies
- Hiring managers running technical rounds
- Staffing agencies managing bulk hiring

### 4.3 Admins
- Platform administrators managing users, questions, and AI model configurations

---

## 5. User Stories

### Candidate
- As a candidate, I want to register and upload my resume so the system can generate relevant interview questions.
- As a candidate, I want to attend a voice-based interview so I can practice speaking.
- As a candidate, I want to receive a detailed feedback report so I can identify areas to improve.
- As a candidate, I want to track my progress over multiple interviews.

### Recruiter
- As a recruiter, I want to create job roles and assign question sets so candidates are evaluated consistently.
- As a recruiter, I want to view ranked candidates with scores so I can shortlist efficiently.
- As a recruiter, I want to compare two candidates side-by-side on all metrics.
- As a recruiter, I want to download a PDF report for any candidate.

### Admin
- As an admin, I want to manage the question bank so content stays relevant and high-quality.
- As an admin, I want to monitor platform-wide analytics to identify usage trends.
- As an admin, I want to configure which AI models are used for evaluation.

---

## 6. Feature Requirements

### 6.1 Authentication & Profiles
- Email/password registration and login for all roles
- OTP verification via email
- Forgot password with reset link
- Resume upload (PDF / DOCX) for candidates
- Company profile creation for recruiters
- Role-based access control (Candidate / Recruiter / Admin)

### 6.2 Resume Analysis
- Parse resume to extract: Name, Skills, Projects, Education, Experience
- Calculate ATS compatibility score
- Identify skill gaps based on job description
- Flag missing keywords

### 6.3 Interview Module
- **Text-Based Interview:** Candidate types answers to questions
- **Voice-Based Interview:** Candidate records audio answers
- **Video-Based Interview:** Candidate records video answers
- Timer per question
- Auto-save answers on timeout

### 6.4 Question Management
- Static question bank organized by domain (Java, Python, SQL, ML)
- AI-generated questions from resume + job description
- Recruiter-created custom question sets
- Question difficulty levels: Easy / Medium / Hard

### 6.5 NLP Analysis Engine
- Keyword coverage scoring
- Semantic similarity using sentence embeddings
- Grammar and readability analysis
- Sentiment analysis of answers
- Filler word detection (um, uh, basically, like, actually)
- Communication score (vocabulary, structure, readability)

### 6.6 Speech & Video Analysis
- Speech-to-text transcription via Whisper
- Voice confidence: speech rate, pitch, pause frequency, energy
- Video confidence: eye contact, head movement, facial expression (advanced)

### 6.7 AI Feedback Generator
- Per-question strengths and weaknesses
- Improvement suggestions per skill gap
- Overall interview summary
- Powered by: Gemini API / OpenAI API / Llama / Mistral

### 6.8 Scoring Engine
```
Final Score = 0.35 × Technical + 0.25 × Communication + 0.20 × Confidence + 0.20 × Keyword Coverage
```

### 6.9 Recruiter Dashboard
- Candidate ranking table by final score
- Skill heatmap across all candidates
- Side-by-side candidate comparison
- Interview session history
- Download PDF report per candidate

### 6.10 Analytics Dashboard
- Average score trends over time
- Skill distribution across candidates
- Confidence level distribution
- Interview volume and completion rates

### 6.11 Report Generation
- Auto-generated PDF reports with: candidate profile, scores, AI feedback, recruiter notes
- Exportable CSV for candidate data

---

## 7. Non-Functional Requirements

| Category | Requirement |
|----------|-------------|
| Performance | API response < 2s for text; < 10s for AI analysis |
| Scalability | Support 1000 concurrent users |
| Availability | 99.5% uptime |
| Security | JWT authentication, HTTPS, encrypted file storage |
| Accessibility | WCAG 2.1 AA compliance |
| Data Privacy | Candidate data stored securely, GDPR-aligned |

---

## 8. Out of Scope (v1.0)

- Live coding round with test case evaluation
- Proctoring (tab switch detection, multiple face detection)
- Multi-language support (Hindi, Marathi)
- Emotion detection
- AI recruiter chatbot
- Subscription/billing management

> These are planned for v2.0 as advanced modules.

---

## 9. Success Metrics

- 80%+ of recruiters rate feedback as "useful" in post-MVP survey
- Candidate report generation in under 60 seconds post-interview
- Platform NPS score ≥ 7/10 after 3-month pilot

---

## 10. Timeline Overview

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 1 | Weeks 1–3 | Auth, Resume Upload, Question Bank |
| Phase 2 | Weeks 4–6 | Interview Module (Text + Voice) |
| Phase 3 | Weeks 7–9 | NLP Engine + Scoring |
| Phase 4 | Weeks 10–11 | Recruiter Dashboard + Reports |
| Phase 5 | Week 12+ | Analytics, AI Feedback, Polish |
