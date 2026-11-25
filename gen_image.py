#!/usr/bin/env python3
"""Generate the one-image world news summary for 25 November 2026.

Renders a 1024x1024 navy-and-amber digest: five headlines with a short
sub-line each, matching the layout of entry.png. Pure Pillow, no network.
"""

import os

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1024
HEIGHT = 1024
NAVY = (15, 30, 51)
AMBER = (240, 165, 0)
WHITE = (255, 255, 255)
GREY = (168, 178, 190)
RULE = (58, 82, 110)

MARGIN = 64
DATE_LINE = "WEDNESDAY 25 NOVEMBER 2026"

ITEMS = [
    (
        "Two tankers hit mines in Hormuz",
        "Two oil tankers struck mines and caught fire; Iran's IRGC "
        "Navy blamed an 'unauthorized route'.",
    ),
    (
        "Huawei convicted on 10 of 12 counts",
        "Trade-secret theft and bank fraud proven; racketeering "
        "cleared. Huawei says it will appeal.",
    ),
    (
        "Nvidia down about 7%, Nikkei down 2.76%",
        "Chip and market sell-off as the AI boom cools; investors "
        "rethink sky-high valuations.",
    ),
    (
        "Cartagena hostages freed after siege",
        "Forces stormed a supermarket after a botched armed robbery; "
        "about 20-30 people had been held.",
    ),
    (
        "First Pakistani astronaut on Shenzhou-24",
        "First foreign national to visit China's space station.",
    ),
]


def load_font(bold, size):
    """Pick a bundled DejaVu font; fall back to Pillow's default."""
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for folder in ("/usr/share/fonts/truetype/dejavu", "/usr/share/fonts"):
        path = os.path.join(folder, name)
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap(draw, text, font, max_width):
    """Greedy word wrap returning a list of lines that fit max_width."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            trial = (current + " " + word).strip()
            if draw.textlength(trial, font=font) <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_item(draw, number, headline, sub, top, text_x, num_x, max_w):
    """Draw one numbered story; return the y position after it."""
    num_font = load_font(True, 38)
    head_font = load_font(True, 33)
    sub_font = load_font(False, 25)

    draw.text((num_x, top), number, font=num_font, fill=AMBER)

    head_lines = wrap(draw, headline, head_font, max_w)
    y = top
    for line in head_lines:
        draw.text((text_x, y), line, font=head_font, fill=WHITE)
        y += 42
    y += 2
    for line in wrap(draw, sub, sub_font, max_w):
        draw.text((text_x, y), line, font=sub_font, fill=GREY)
        y += 31
    return y


def build(output_path):
    img = Image.new("RGB", (WIDTH, HEIGHT), NAVY)
    draw = ImageDraw.Draw(img)

    title_font = load_font(True, 80)
    date_font = load_font(True, 32)
    foot_font = load_font(False, 26)

    y = 48
    draw.text((MARGIN, y), "WORLD NEWS", font=title_font, fill=WHITE)
    y += 96
    draw.text((MARGIN, y), DATE_LINE, font=date_font, fill=AMBER)
    y += 46
    draw.line([(MARGIN, y), (WIDTH - MARGIN, y)], fill=RULE, width=3)
    y += 28

    text_x = MARGIN + 96
    max_w = WIDTH - MARGIN - text_x
    for index, (headline, sub) in enumerate(ITEMS, start=1):
        y = draw_item(draw, f"{index:02d}", headline, sub,
                      y, text_x, MARGIN, max_w)
        y += 18

    foot_y = HEIGHT - 96
    draw.line([(MARGIN, foot_y), (WIDTH - MARGIN, foot_y)],
              fill=RULE, width=3)
    draw.text((MARGIN, foot_y + 20),
              "One-image summary  \u00b7  news-image-20261125",
              font=foot_font, fill=GREY)

    img.save(output_path, "PNG")
    print(f"wrote {output_path} ({WIDTH}x{HEIGHT})")


if __name__ == "__main__":
    import sys

    target = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    build(target)
