#!/usr/bin/env python3
"""Verify profile graphics and local README links."""
from pathlib import Path
import re
import sys
from xml.etree import ElementTree as ET
root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text(encoding="utf-8")
svgs = sorted((root / "assets").glob("*.svg"))
errors = []
for file in svgs:
    try:
        if not ET.parse(file).getroot().tag.endswith("svg"):
            errors.append("Invalid SVG root: " + str(file))
    except ET.ParseError as exc:
        errors.append(f"{file}: {exc}")
for ref in re.findall(r'(?:src|srcset)=[\\\"\\\'](assets/[^\\\"\\\']+)[\\\"\\\']', readme):
    if not (root / ref).is_file():
        errors.append("Missing local asset: " + ref)
if not svgs:
    errors.append("No SVG assets found")
for err in errors:
    print("ERROR:",err,file=sys.stderr)
print(f"Checked {len(svgs)} SVG assets, broken refs: {len(errors)}")
sys.exit(1 if errors else 0)
