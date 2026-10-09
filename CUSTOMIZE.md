# Customize your GitHub profile

The **Nicricht/Nicricht** repository is a GitHub profile repository: its root `README.md` appears automatically on [github.com/Nicricht](https://github.com/Nicricht) when the repository is public.

## Design

- `README.md`: all visible sections and links.
- `assets/banner-*.svg`: hero branding, with automatic dark/light variants.
- `assets/terminal-*.svg`: terminal bio cards with automatic dark/light variants.
- `assets/focus-map-*.svg`: engineering interests, not skill proficiency scores.
- `assets/project-*.svg`: clickable project cover art.
- `.github/workflows/validate-profile.yml`: checks local SVG assets, links and README paths on each push and PR.

All vector artwork is authored specifically for this profile. No cloning or copying of pagaliv's graphics or assets.

## Edit names, descriptions, contacts

Open `README.md` and edit text using GitHub's pencil icon. For the SVGs, open the corresponding file in `assets/` and edit SVG `text` nodes. You can also edit in VS Code.

**Privacy:** no contact email, phone number or LinkedIn URL is published here. Your public display name and student status are included; edit those if you prefer more privacy.

**Accuracy:** references to Java, Spring, Docker, React, etc. indicate project experience, not claimed expert proficiency. The Engineering Horizon lists interests, not numeric skills.

## External image services

These third-party images are optional and may occasionally be unavailable:
- https://readme-typing-svg.demolab.com
- https://skillicons.dev
- https://streak-stats.demolab.com
- https://img.shields.io
- https://komarev.com

The core design (banner, terminal, project cards, horizon) works without any of those services. If an external widget fails, you can remove its `<img>` from `README.md` without breaking the rest.

## How to publish (GitHub web)

1. Create a **public** repository named `Nicricht` under user `Nicricht`, and check **Add a README file**.
2. Upload `assets/`, `.github/workflows/`, `scripts/` and `CUSTOMIZE.md` preserving their paths. Replace the default `README.md` with this template.
3. Visit https://github.com/Nicricht and refresh.

You do not need to enable GitHub Pages, purchase a domain or reveal an API key.

## Test locally

Run `python scripts/check_profile.py` from the root of the repository. No third-party Python dependencies are required.