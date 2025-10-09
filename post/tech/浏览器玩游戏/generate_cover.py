#!/usr/bin/env python3
"""
Generate cover banners for the Snake in URL bar article
- Chinese version: 2.35:1 aspect ratio (1880x800)
- English version: 16:9 aspect ratio (1920x1080)
"""

from PIL import Image, ImageDraw, ImageFont
import random
import sys

# Colors - inspired by browser URL bar
BG_COLOR = "#1a1a2e"  # Dark background
URL_BAR_COLOR = "#16213e"  # URL bar background
TEXT_COLOR = "#eaeaea"  # Light text
SNAKE_COLOR = "#00ff88"  # Bright green for snake
FOOD_COLOR = "#ff0055"  # Red for food
ACCENT_COLOR = "#0f3460"  # Accent blue

def generate_chinese_cover():
    """Generate Chinese version cover with 2.35:1 aspect ratio"""
    WIDTH = 1880
    HEIGHT = 800

    # Create image
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Draw browser window frame
    window_margin = 40
    window_top = 60
    browser_bar_height = 40

    # Browser window outline
    draw.rectangle(
        [(window_margin, window_top), (WIDTH - window_margin, HEIGHT - window_margin)],
        outline=ACCENT_COLOR,
        width=3
    )

    # Browser top bar
    draw.rectangle(
        [(window_margin, window_top), (WIDTH - window_margin, window_top + browser_bar_height)],
        fill=URL_BAR_COLOR,
        outline=ACCENT_COLOR,
        width=2
    )

    # Browser window buttons
    button_y = window_top + 12
    button_spacing = 25
    for i, color in enumerate(['#ff5f56', '#ffbd2e', '#27c93f']):
        draw.ellipse(
            [(window_margin + 20 + i * button_spacing, button_y),
             (window_margin + 35 + i * button_spacing, button_y + 15)],
            fill=color
        )

    # URL bar
    url_bar_y = window_top + browser_bar_height + 20
    url_bar_height = 50
    url_bar_margin = window_margin + 80

    draw.rounded_rectangle(
        [(url_bar_margin, url_bar_y),
         (WIDTH - url_bar_margin, url_bar_y + url_bar_height)],
        radius=8,
        fill="#2a2a3e",
        outline="#00ff88",
        width=2
    )

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 56)
        snake_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 28)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 28)
        url_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 20)
    except:
        title_font = ImageFont.load_default()
        snake_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        url_font = ImageFont.load_default()

    # Draw snake in URL bar
    snake_chars = "░░░⣿⣿⣿⣿⡇⠀⠀⢸⣿⠀⠀⠀⠀⣀⣀⣿⠀⠀⢠⣿⠀⠀⠀⠀⠀⣿⠀⠀⠀"
    draw.text((url_bar_margin + 50, url_bar_y + 8), snake_chars, fill=SNAKE_COLOR, font=snake_font)

    # Lock icon
    draw.text((url_bar_margin + 15, url_bar_y + 12), "🔒", fill="#666666", font=url_font)

    # Main title - centered
    title_text = "浏览器地址栏里的贪吃蛇"
    title_y = url_bar_y + url_bar_height + 100

    bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = bbox[2] - bbox[0]
    title_x = (WIDTH - title_width) // 2

    # Draw with shadow
    shadow_offset = 3
    draw.text((title_x + shadow_offset, title_y + shadow_offset), title_text, fill="#000000", font=title_font)
    draw.text((title_x, title_y), title_text, fill=SNAKE_COLOR, font=title_font)

    # Subtitle
    subtitle = "当互联网还能随便玩的时候"
    subtitle_y = title_y + 90
    bbox_sub = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = bbox_sub[2] - bbox_sub[0]
    subtitle_x = (WIDTH - subtitle_width) // 2

    draw.text((subtitle_x, subtitle_y), subtitle, fill="#aaaaaa", font=subtitle_font)

    # Decorative pixels
    dot_size = 4
    for i in range(20):
        x = random.randint(window_margin + 100, WIDTH - window_margin - 100)
        y = random.randint(HEIGHT - 120, HEIGHT - 60)
        draw.rectangle(
            [(x, y), (x + dot_size, y + dot_size)],
            fill=random.choice([SNAKE_COLOR, FOOD_COLOR, ACCENT_COLOR])
        )

    # URL hint
    url_hint = "https://demian.ferrei.ro/snake#"
    url_hint_y = HEIGHT - 50
    bbox_hint = draw.textbbox((0, 0), url_hint, font=url_font)
    url_hint_width = bbox_hint[2] - bbox_hint[0]
    url_hint_x = (WIDTH - url_hint_width) // 2
    draw.text((url_hint_x, url_hint_y), url_hint, fill="#666666", font=url_font)

    # Save
    output_path = "cover-zh-cn.svg"
    img.save("cover-zh-cn.png", quality=95)
    print(f"Chinese cover generated: cover-zh-cn.png ({WIDTH}x{HEIGHT})")
    return img

def generate_english_cover():
    """Generate English version cover with 16:9 aspect ratio"""
    WIDTH = 1920
    HEIGHT = 1080

    # Create image
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Draw browser window frame
    window_margin = 60
    window_top = 100
    browser_bar_height = 50

    # Browser window outline
    draw.rectangle(
        [(window_margin, window_top), (WIDTH - window_margin, HEIGHT - window_margin)],
        outline=ACCENT_COLOR,
        width=3
    )

    # Browser top bar
    draw.rectangle(
        [(window_margin, window_top), (WIDTH - window_margin, window_top + browser_bar_height)],
        fill=URL_BAR_COLOR,
        outline=ACCENT_COLOR,
        width=2
    )

    # Browser window buttons
    button_y = window_top + 15
    button_spacing = 25
    for i, color in enumerate(['#ff5f56', '#ffbd2e', '#27c93f']):
        draw.ellipse(
            [(window_margin + 20 + i * button_spacing, button_y),
             (window_margin + 35 + i * button_spacing, button_y + 15)],
            fill=color
        )

    # URL bar
    url_bar_y = window_top + browser_bar_height + 30
    url_bar_height = 55
    url_bar_margin = window_margin + 100

    draw.rounded_rectangle(
        [(url_bar_margin, url_bar_y),
         (WIDTH - url_bar_margin, url_bar_y + url_bar_height)],
        radius=8,
        fill="#2a2a3e",
        outline="#00ff88",
        width=2
    )

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 72)
        snake_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 30)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 36)
        url_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 22)
    except:
        title_font = ImageFont.load_default()
        snake_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        url_font = ImageFont.load_default()

    # Draw snake in URL bar
    snake_chars = "░░░⣿⣿⣿⣿⡇⠀⠀⢸⣿⠀⠀⠀⠀⣀⣀⣿⠀⠀⢠⣿⠀⠀⠀⠀⠀⣿⠀⠀⠀"
    draw.text((url_bar_margin + 50, url_bar_y + 10), snake_chars, fill=SNAKE_COLOR, font=snake_font)

    # Lock icon
    draw.text((url_bar_margin + 15, url_bar_y + 14), "🔒", fill="#666666", font=url_font)

    # Main title - two lines, centered
    title_text1 = "Playing Snake in Your"
    title_text2 = "Browser's Address Bar"
    title_y = url_bar_y + url_bar_height + 150

    bbox1 = draw.textbbox((0, 0), title_text1, font=title_font)
    title_width1 = bbox1[2] - bbox1[0]
    title_x1 = (WIDTH - title_width1) // 2

    bbox2 = draw.textbbox((0, 0), title_text2, font=title_font)
    title_width2 = bbox2[2] - bbox2[0]
    title_x2 = (WIDTH - title_width2) // 2

    # Draw with shadow
    shadow_offset = 4
    draw.text((title_x1 + shadow_offset, title_y + shadow_offset), title_text1, fill="#000000", font=title_font)
    draw.text((title_x1, title_y), title_text1, fill=TEXT_COLOR, font=title_font)

    draw.text((title_x2 + shadow_offset, title_y + 90 + shadow_offset), title_text2, fill="#000000", font=title_font)
    draw.text((title_x2, title_y + 90), title_text2, fill=SNAKE_COLOR, font=title_font)

    # Subtitle
    subtitle = "When the Internet Was Still Fun"
    subtitle_y = title_y + 200
    bbox_sub = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = bbox_sub[2] - bbox_sub[0]
    subtitle_x = (WIDTH - subtitle_width) // 2

    draw.text((subtitle_x, subtitle_y), subtitle, fill="#aaaaaa", font=subtitle_font)

    # Decorative pixels
    dot_size = 5
    for i in range(25):
        x = random.randint(window_margin + 150, WIDTH - window_margin - 150)
        y = random.randint(HEIGHT - 150, HEIGHT - 80)
        draw.rectangle(
            [(x, y), (x + dot_size, y + dot_size)],
            fill=random.choice([SNAKE_COLOR, FOOD_COLOR, ACCENT_COLOR])
        )

    # URL hint
    url_hint = "https://demian.ferrei.ro/snake#"
    url_hint_y = HEIGHT - 70
    bbox_hint = draw.textbbox((0, 0), url_hint, font=url_font)
    url_hint_width = bbox_hint[2] - bbox_hint[0]
    url_hint_x = (WIDTH - url_hint_width) // 2
    draw.text((url_hint_x, url_hint_y), url_hint, fill="#666666", font=url_font)

    # Save
    img.save("cover-en.png", quality=95)
    print(f"English cover generated: cover-en.png ({WIDTH}x{HEIGHT})")
    return img

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "cn":
            generate_chinese_cover()
        elif sys.argv[1] == "en":
            generate_english_cover()
        else:
            print("Usage: python generate_cover.py [cn|en]")
    else:
        # Generate both
        generate_chinese_cover()
        generate_english_cover()
        print("\nBoth covers generated successfully!")
