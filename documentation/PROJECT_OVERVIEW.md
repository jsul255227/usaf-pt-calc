# USAF PT Test Calculator — Project Overview

## Project Purpose
A professional, modular, and accurate web application for calculating United States Air Force Physical Training (USAF PT) test scores. The app is designed for both desktop and mobile, providing instant feedback, official requirements, and a modern, user-friendly interface. It is suitable for both personal and organizational use, and is deployable on Fly.io or similar platforms.

## Scope
- Implements the official USAF PT scoring tables for all age and gender groups.
- Modular scoring logic: each age/gender group is a separate Python module for maintainability and accuracy.
- Responsive, accessible, and visually appealing UI using Bootstrap and custom CSS.
- Live scoring and requirements display as the user enters data.
- Robust backend and frontend validation.
- Designed for easy deployment and maintainability.

## Key Features

### Scoring Logic
- All official USAF PT test components supported:
  - Cardio: 1.5 Mile Run, HAMR (shuttles)
  - Upper: Push-ups, Hand Release Push-ups
  - Core: Sit-ups, Cross-Leg Reverse Crunches, Plank
- Modular Python scoring files for each age/gender group (e.g., `usaf_scoring/male_25_29.py`).
- Centralized scoring table registration and normalization in `app.py`.
- Accurate calculation of component and total scores, with official max/min limits.

### User Interface
- Modern, responsive layout with two-column design on desktop (form and results side by side).
- All form fields grouped for minimal vertical scrolling.
- Live result card updates instantly as user enters data.
- Requirements for each component (min/max) shown live based on age/gender selection.
- HTML5 and JS validation for all fields, including time auto-formatting (mm:ss).
- Error messages shown for invalid input or backend errors.

### API & Backend
- `/api/calculate`: Returns live PT score for given input (AJAX endpoint).
- `/api/requirements`: Returns official min/max requirements for selected age/gender (AJAX endpoint).
- Robust backend validation for all fields.
- Modular Flask app with clear separation of logic and presentation.

### Deployment
- Dockerfile for containerized deployment (uses Gunicorn, exposes port 8080).
- Ready for Fly.io or similar cloud platforms.
- Static and template folders for assets and HTML.

## Future Improvements
- Add more detailed requirements for all age/gender groups.
- Further UI/UX polish and accessibility enhancements.
- Admin/configuration interface for updating scoring tables.
- Export/print/share results.
- User authentication (optional).

---

**Maintained by:** Jesse & contributors

**Last updated:** July 5, 2025
