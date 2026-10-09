#!/usr/bin/env python3
"""Validate SVG assets, motion fallbacks and README project references."""
from pathlib import Path
from xml.etree import ElementTree as ET
import re
import sys

root = Path(__file__).resolve().parents[1]
assets = sorted((root / "assets").glob("*.svg"))
readme = (root / "README.md").read_text(encoding="utf-8")
errors = []

for svg_file in assets:
    try:
        node = ET.parse(svg_file).getroot()
        vb = node.attrib.get("viewBox", "").split()
        if len(vb) != 4:
            errors.append(f"{svg_file.name}: missing viewBox")
            continue
        w,h = float(vb[2]),float(vb[3])
        if w <= 0 or h <= 0 or float(node.get("width",0)) != w or float(node.get("height",0)) != h:
            errors.append(f"{svg_file.name}: dimensions inconsistent")
        text_svg = svg_file.read_text(encoding="utf-8")
        if "@keyframes" not in text_svg or "prefers-reduced-motion" not in text_svg:
            errors.append(f"{svg_file.name}: animation or reduced-motion safeguard missing")
        if not any(el.tag.endswith("title") for el in node):
            errors.append(f"{svg_file.name}: lacks accessible title")
        for el in node.iter():
            if el.tag.endswith("text") and el.get("y"):
                y = float(el.get("y"))
                fs = float(el.get("font-size", "16"))
                if y < fs*0.58 or y > h - 7:
                    errors.append(f"{svg_file.name}: clipped text baseline y={y}: {el.text}")
    except (ET.ParseError, ValueError) as ex:
        errors.append(f"{svg_file.name}: {ex}")

local_refs = re.findall(r'(?:src|srcset)="(assets/[^"]+)"',readme)
for ref in set(local_refs):
    if not (root / ref).is_file():
        errors.append(f"README missing asset: {ref}")
for path in ("README.md", "assets/banner-dark.svg", "assets/banner-light.svg", "assets/proof-dark.svg", "assets/proof-light.svg", "assets/project-helvoca.svg"):
    if not (root / path).is_file():
        errors.append(f"Missing required file: {path}")
for repo in ("Nicricht/helvoca","Nicricht/edubio360","Nicricht/casehunter"):
    if repo not in readme:
        errors.append(f"Missing public project link: {repo}")
if not assets:
    errors.append("No SVG assets found")
for error in errors:
    print("ERROR:",error,file=sys.stderr)
print(f"SVGs checked: {len(assets)} | README image references: {len(local_refs)} | Errors: {len(errors)}")
sys.exit(1 if errors else 0)
