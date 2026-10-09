# Recruiter-first motion system

This repository contains a public portfolio built for rapid scanning by technical recruiters.

## The one-second test
A visitor should instantly understand:
- Name: Nicolás Vega.
- Focus: Java Backend and Spring Boot.
- Evidence: AI voice SaaS (Helvoca), Java microservices (EduBío 360), Python automation (Case Hunter).
- Honesty: student / backend developer in training; learning areas are separate from project experience.

## Movement (all local, GitHub-compatible SVG)
- `banner-*.svg`: circuit scanner, orbit rings, pulse, cursor, moving accent.
- `proof-*.svg`: moving evidence lines and pulsing indicators.
- `project-*.svg`: animated track, pulse and navigation arrow.
- `terminal-*.svg`: terminal cursor, status pulse, progress line.
- `focus-map-*.svg`: orbiting focus indicator.
- Both light and dark variants are animated.
- Animation changes decoration, not essential text. **All text is visible from frame 1.**
- All SVGs include `prefers-reduced-motion` support. No external JavaScript.
- Markdown, not embedded SVG text alone, carries the important project links and explanations.

## Maintenance
- README is deliberately concise above the fold.
- Do not claim certifications, employment, production deployments, performance results or security guarantees without evidence.
- Project card links point to public source repositories.
- Keep vector text inside viewBox boundaries and test at 100% and narrower mobile-like widths.
- Animated SVG is supported by GitHub's Markdown renderer in current mainstream browsers; reduced-motion preferences or browser settings may suppress animations.

Test locally: `python3 scripts/check_profile.py`.
