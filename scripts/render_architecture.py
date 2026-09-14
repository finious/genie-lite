#!/usr/bin/env python3
"""Render the required Devpost architecture diagram as a PNG."""

from pathlib import Path
from math import atan2, cos, pi, sin

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "assets" / "genie_lite_architecture.png"


def font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica.ttc",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()


def centered(draw, box, label, fill, text_fill="#111111", width=4):
    draw.rounded_rectangle(box, radius=24, fill=fill, outline="#111111", width=width)
    bbox = draw.multiline_textbbox((0, 0), label, font=font(31, True), spacing=8, align="center")
    x = (box[0] + box[2] - (bbox[2] - bbox[0])) / 2
    y = (box[1] + box[3] - (bbox[3] - bbox[1])) / 2
    draw.multiline_text((x, y), label, font=font(31, True), fill=text_fill, spacing=8, align="center")


def arrow(draw, start, end, label):
    draw.line((start, end), fill="#111111", width=6)
    x2, y2 = end
    angle = atan2(y2 - start[1], x2 - start[0])
    left = (x2 - 24 * cos(angle - pi / 6), y2 - 24 * sin(angle - pi / 6))
    right = (x2 - 24 * cos(angle + pi / 6), y2 - 24 * sin(angle + pi / 6))
    draw.polygon([(x2, y2), left, right], fill="#111111")
    text_box = draw.textbbox((0, 0), label, font=font(20, True))
    w = text_box[2] - text_box[0]
    mx = (start[0] + end[0]) / 2
    my = (start[1] + end[1]) / 2
    draw.rounded_rectangle((mx - w / 2 - 12, my - 31, mx + w / 2 + 12, my + 1), radius=10, fill="#FFF9EE")
    draw.text((mx - w / 2, my - 29), label, font=font(20, True), fill="#111111")


def main():
    image = Image.new("RGB", (1600, 900), "#FFF9EE")
    draw = ImageDraw.Draw(image)

    draw.text((80, 52), "GENIE LITE", font=font(54, True), fill="#111111")
    draw.text((80, 118), "Human-led specialist routing with visible authority and receipts", font=font(27), fill="#333333")

    human = (80, 255, 380, 455)
    echo = (505, 255, 805, 455)
    create = (930, 255, 1230, 455)
    returned = (80, 590, 380, 755)
    receipt = (505, 590, 1230, 755)

    centered(draw, human, "HUMAN\nintent +\ncorrection", "#F7C948")
    centered(draw, echo, "ECHO\nconversational\nbridge", "#F28C28")
    centered(draw, create, "CREATE\nbounded\nspecialist", "#F45B69")
    centered(draw, returned, "HUMAN\njudgment +\nauthority", "#F7C948")
    centered(draw, receipt, "RECEIPT\nroute • return • correction • authority • limits", "#B8E0D2")

    arrow(draw, (380, 330), (505, 330), "HEAR")
    arrow(draw, (805, 330), (930, 330), "ROUTE")
    arrow(draw, (930, 420), (805, 420), "RETURN")
    arrow(draw, (655, 455), (655, 590), "RECEIPT")
    arrow(draw, (505, 650), (380, 670), "INSPECT")

    draw.rounded_rectangle((1285, 255, 1520, 755), radius=24, fill="#FFFFFF", outline="#111111", width=4)
    draw.text((1315, 290), "GOVERNANCE", font=font(25, True), fill="#111111")
    rules = [
        "Conversation ≠\nauthority",
        "Routing ≠\nexecution",
        "Execution ≠\nverification",
        "Recovery ≠\npermission",
        "Human owns\nconsequence",
    ]
    y = 355
    for rule in rules:
        draw.ellipse((1315, y + 6, 1331, y + 22), fill="#F28C28")
        draw.multiline_text((1345, y), rule, font=font(17, True), fill="#222222", spacing=4)
        y += 72

    draw.text((80, 822), "Strands Agents • Amazon Bedrock AgentCore • Amazon Nova Pro • CodeZip", font=font(24, True), fill="#333333")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
