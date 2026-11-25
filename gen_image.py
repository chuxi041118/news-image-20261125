"""Draw the news-image-20261125 poster: a 1024x1024 one-image summary of
world news on Wednesday 25 November 2026. Saves entry.png next to this script."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
MARGIN = 64
HERE = Path(__file__).resolve().parent

NAVY = (15, 27, 45)
INK = (255, 255, 255)
MUTED = (176, 190, 205)
AMBER = (242, 183, 5)
RULE = (58, 80, 108)

TITLE = "WORLD NEWS"
DATE = "WEDNESDAY 25 NOVEMBER 2026"

ITEMS = [
    ("Two tankers hit mines in Hormuz",
     "Iran's IRGC Navy blames an 'unauthorized route'."),
    ("Huawei convicted on 10 of 12 counts",
     "Trade-secret theft and bank fraud; racketeering cleared."),
    ("Nvidia down about 7%, Nikkei down 2.76%",
     "Lawmakers questioned Trump's role in Huang's return."),
    ("Cartagena hostages freed after siege",
     "Forces stormed a supermarket; about 20-30 had been held."),
    ("First Pakistani astronaut on Shenzhou-24",
     "First foreign national to visit China's space station."),
]

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def load_font(bold, size):
    path = FONT_PATHS[0] if bold else FONT_PATHS[1]
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, font, width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def main():
    img = Image.new("RGB", (SIZE, SIZE), NAVY)
    draw = ImageDraw.Draw(img)

    title_font = load_font(True, 76)
    date_font = load_font(True, 30)
    head_font = load_font(True, 34)
    sub_font = load_font(False, 26)
    num_font = load_font(True, 34)
    foot_font = load_font(False, 22)

    draw.text((MARGIN, 56), TITLE, font=title_font, fill=INK)
    draw.text((MARGIN, 150), DATE, font=date_font, fill=AMBER)
    draw.line([(MARGIN, 200), (SIZE - MARGIN, 200)], fill=RULE, width=3)

    y = 236
    for i, (head, sub) in enumerate(ITEMS, start=1):
        draw.text((MARGIN, y), f"{i:02d}", font=num_font, fill=AMBER)
        text_x = MARGIN + 76
        width = SIZE - MARGIN - text_x
        for line in wrap(draw, head, head_font, width):
            draw.text((text_x, y), line, font=head_font, fill=INK)
            y += 44
        for line in wrap(draw, sub, sub_font, width):
            draw.text((text_x, y), line, font=sub_font, fill=MUTED)
            y += 36
        y += 64

    draw.line([(MARGIN, SIZE - 92), (SIZE - MARGIN, SIZE - 92)], fill=RULE, width=2)
    draw.text((MARGIN, SIZE - 72),
              "One-image summary  ·  news-image-20261125",
              font=foot_font, fill=MUTED)

    out = HERE / "entry.png"
    img.save(out)
    print(f"wrote {out} ({SIZE}x{SIZE})")


if __name__ == "__main__":
    main()
