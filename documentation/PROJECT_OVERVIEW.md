# USAF PT Test Calculator — Project Overview

## Project Purpose
A professional, modular, and accurate web application for calculating United States Air Force Physical Training (USAF PT) test scores. The app is designed for both desktop and mobile, providing instant feedback, official requirements, and a modern, user-friendly interface. It is suitable for both personal and organizational use, and is deployable on Fly.io or similar platforms.

## Scope
- Implements the official USAF PT scoring tables for all age and gender groups.
- Modular scoring logic: each age/gender group is a separate Python module in `/tables/` for maintainability and accuracy.
- Responsive, accessible, and visually appealing UI using modern React and custom CSS (no Bootstrap).
- Live scoring and requirements display as the user enters data.
- Robust backend and frontend validation.
- Designed for easy deployment and maintainability.

## Key Features

### Scoring Logic
- All official USAF PT test components supported:
  - Cardio: 1.5 Mile Run, HAMR (shuttles)
  - Upper: Push-ups, Hand Release Push-ups
  - Core: Sit-ups, Cross-Leg Reverse Crunches, Plank
- Modular Python scoring files for each age/gender group (e.g., `tables/males_25_29.py`).
- Centralized scoring logic in `app/services/pt_service.py`.
- Accurate calculation of component and total scores, with official max/min limits.

### User Interface
- Modern, responsive layout with mobile/touch-friendly design.
- All form fields grouped for minimal vertical scrolling.
- Live result card updates instantly as user enters data.
- Requirements for each component (min/max) shown live based on age/gender selection.
- HTML5 and JS validation for all fields, including time auto-formatting (mm:ss).
- Error messages shown for invalid input or backend errors.

### API & Backend
- `/api/pt/calculate`: Returns PT score for given input (AJAX endpoint).
- `/api/pt/minmax`: Returns official min/max requirements for selected age/gender/component (AJAX endpoint).
- Robust backend validation for all fields.
- FastAPI backend with clear separation of logic and presentation.

### Deployment
- Dockerfile for containerized deployment (uses Gunicorn + Uvicorn, exposes port 8080).
- Ready for Fly.io or similar cloud platforms.
- React frontend built and served as static files by FastAPI.

## Results Section and Footer

- The results section displays only the following for each calculation:
  - Cardio Points: XX.XX
  - Upper Points: XX.XX
  - Core Points: XX.XX
  - Total Score: XX.XX
  - Overall Rating: Satisfactory/Excellent/Unsatisfactory (based on total score)
- The raw input values (e.g., run time, pushups, plank time) are NOT shown in the results.
- The footer is always present, styled as follows:

  For bug reports, suggestions, and feedback, please feel free to email us at usafptcalc@protonmail.com.
  © 2025 USAF PT Calc. All rights reserved.
  This site is not endorsed by the U.S. Air Force.

- The footer must appear below the results section and match the style in the production app and screenshots.

---
**Last updated:** July 6, 2025
