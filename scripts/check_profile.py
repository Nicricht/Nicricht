#!/usr/bin/env python3
"""Basic, dependency-free checks for the public GitHub profile."""
from pathlib import Path
import re
import sys
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
ASSETS = sorted((ROOT / "assets").glob("*.svg"))
errors = []
for path in ASSETS:
    try:
        svg = ET.parse(path).getroot()
        if not svg.tag.endswith("svg"):
            errors.append(f"{path}: root is not SVG")
            continue
        vb = svg.get("viewBox", "").split()
        if len(vb) != 4:
            errors.append(f"{path}: missing viewBox")
            continue
        width, height = float(vb[2]), float(vb[3])
        if width <= 0 or height <= 0:
            errors.append(f"{path}: invalid viewBox dimensions")
        if float(svg.get("height", 0)) != height:
            errors.append(f"{path}: height differs from viewBox")
        for element in svg.iter():
            if not element.tag.endswith("text"):
                continue
            if "y" not in element.attrib:
                continue
            y = float(element.get("y"))
            font_size = float(element.get("font-size", 16))
            if y < font_size * 0.65 or y + font_size * 0.3 > height - 8:
                errors.append(f"{path}: text baseline too close to edge: {element.text!r} at y={y}")
    except (ET.ParseError, ValueError) as exc:
        errors.append(f"{path}: {exc}")

for ref in re.findall(r"(?:src|srcset)=[\"'](assets/[^\"']+)[\"']", README):
    if not (ROOT / ref).is_file():
        errors.append(f"Missing local image: {ref}")
for required in ("## About me", "## Selected projects", "## Technologies used in my projects"):
    if required not in README:
        errors.append(f"Missing README heading: {required}")
if not ASSETS:
    errors.append("No SVGs found")
for error in errors:
    print("ERROR:", error, file=sys.stderr)
print(f"Validated {len(ASSETS)} SVGs and README references. Issues: {len(errors)}")
sys.exit(bool(errors))
