# Maintaining the Nicricht GitHub profile

The public GitHub profile lives at https://github.com/Nicricht and is sourced from this repository's README.

## Layout
1. Hero identity and clear backend specialization.
2. Short about section and terminal-style engineering snapshot.
3. Four real public projects, each with a wide, responsive SVG card and textual evidence.
4. Project technologies and learning directions.
5. Optional activity stats and contact links.

SVG assets are original. All SVGs are static, with no JavaScript. Project graphics have dark and light versions, and links remain plain HTML/Markdown for GitHub compatibility.

## Accessibility and maintenance
- Keep critical descriptions in Markdown, not only inside SVG images.
- Prefer concise text with useful alt descriptions.
- Avoid percentage skill scores, visitor-count vanity metrics, and unverified certifications.
- Keep the role aligned with project evidence: Java/Spring Boot backend and automation.
- Project SVG designs are 1000x220 to remain legible within GitHub's content column.
- If adding new SVG text, avoid coordinates at or beyond the viewBox edges.
- Use the correct public project links; never claim private client deployments without evidence.
- External technology icons and optional streak statistics may be temporarily unavailable.
- Contact currently links to the educational email also displayed on the public GitHub profile.

## Check
Run: python3 scripts/check_profile.py

.github/workflows/validate-profile.yml runs this check on push and pull requests.
