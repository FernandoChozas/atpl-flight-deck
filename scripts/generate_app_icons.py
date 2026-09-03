#!/usr/bin/env python3
"""
Generates high-resolution, pixel-perfect iOS Apple Touch Icons and Favicons
for the ATPL Flight Deck application without external dependencies.
Features:
- Premium Cockpit Navy Gradient
- Sleek Twin-Engine Commercial Jet Silhouette
- Aviation Captain Gold Wings Accent
- Bold "ATPL" Pilot Typography
"""

import os
import zlib
import struct
import math

def make_png(width, height, get_pixel):
    raw_data = bytearray()
    for y in range(height):
        raw_data.append(0) # Filter type 0
        for x in range(width):
            r, g, b, a = get_pixel(x, y)
            raw_data.extend([int(r), int(g), int(b), int(a)])
    
    def chunk(tag, data):
        c = struct.pack('>I', len(data)) + tag + data
        crc = zlib.crc32(tag + data) & 0xffffffff
        return c + struct.pack('>I', crc)
    
    header = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0))
    idat = chunk(b'IDAT', zlib.compress(bytes(raw_data), 9))
    iend = chunk(b'IEND', b'')
    return header + ihdr + idat + iend

# 5x7 bitmap font for "ATPL"
FONT_5X7 = {
    'A': [
        " 111 ",
        "1   1",
        "1   1",
        "11111",
        "1   1",
        "1   1",
        "1   1"
    ],
    'T': [
        "11111",
        "  1  ",
        "  1  ",
        "  1  ",
        "  1  ",
        "  1  ",
        "  1  "
    ],
    'P': [
        "1111 ",
        "1   1",
        "1   1",
        "1111 ",
        "1    ",
        "1    ",
        "1    "
    ],
    'L': [
        "1    ",
        "1    ",
        "1    ",
        "1    ",
        "1    ",
        "1    ",
        "11111"
    ]
}

def generate_atpl_icon(size=192):
    # Precompute text mask for "ATPL"
    text_grid = [[False for _ in range(size)] for _ in range(size)]
    word = "ATPL"
    scale = int(size * 0.08) # scale factor for 5x7 font
    letter_w = 5 * scale
    letter_h = 7 * scale
    spacing = int(scale * 1.5)
    total_w = len(word) * letter_w + (len(word) - 1) * spacing
    start_x = (size - total_w) // 2
    start_y = int(size * 0.72)

    for i, char in enumerate(word):
        grid = FONT_5X7.get(char, [])
        ox = start_x + i * (letter_w + spacing)
        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                if val == '1':
                    px_start = ox + col_idx * scale
                    py_start = start_y + row_idx * scale
                    for py in range(py_start, py_start + scale):
                        for px in range(px_start, px_start + scale):
                            if 0 <= px < size and 0 <= py < size:
                                text_grid[py][px] = True

    def get_pixel(x, y):
        # 1. Base Gradient: Deep Cockpit Navy/Midnight to Royal Blue
        dx = (x - size / 2) / (size / 2)
        dy = (y - size / 2) / (size / 2)
        dist_center = math.sqrt(dx * dx + dy * dy)
        
        # Radial gradient from #1e3a8a (center-top) to #080d1a (bottom/corners)
        t = min(1.0, max(0.0, dist_center * 0.8 + (y / size) * 0.4))
        r = 30 * (1 - t) + 8 * t
        g = 58 * (1 - t) + 13 * t
        b = 138 * (1 - t) + 26 * t

        # Subtle gold outer border circle
        r_dist = math.hypot(x - size/2, y - size/2) / (size * 0.47)
        if 0.95 <= r_dist <= 1.0:
            return (212, 160, 23, 255) # Gold accent ring

        # 2. Jet Airplane Silhouette (Facing Upwards)
        # Coordinate system relative to center of airplane
        cx = size * 0.5
        cy = size * 0.40
        nx = abs(x - cx)
        ny = y - cy

        # Fuselage (sleek needle body)
        is_fuselage = False
        if -size*0.22 <= ny <= size*0.22:
            body_w = size * 0.035 * (1.0 - (ny / (size*0.25))**2) if ny < 0 else size * 0.035
            if ny > size*0.18:
                body_w = size * 0.015 # Tail taper
            if nx <= max(1.5, body_w):
                is_fuselage = True

        # Swept Wings
        is_wing = False
        wing_y_start = -size * 0.05
        wing_y_end = size * 0.12
        if wing_y_start <= ny <= wing_y_end:
            # Swept back line
            span_prog = (ny - wing_y_start) / (wing_y_end - wing_y_start)
            max_span = size * 0.40 * (span_prog ** 0.85)
            min_span = max_span - size * 0.06
            if min_span <= nx <= max_span:
                is_wing = True

        # Horizontal Stabilizer (Tail wings)
        is_tail = False
        tail_y_start = size * 0.15
        tail_y_end = size * 0.22
        if tail_y_start <= ny <= tail_y_end:
            t_prog = (ny - tail_y_start) / (tail_y_end - tail_y_start)
            max_tspan = size * 0.16 * (t_prog ** 0.8)
            min_tspan = max_tspan - size * 0.035
            if min_tspan <= nx <= max_tspan:
                is_tail = True

        # Engines pods under wings
        is_engine = False
        if (size * 0.00 <= ny <= size * 0.07) and (size * 0.12 <= nx <= size * 0.155):
            is_engine = True

        if is_fuselage or is_wing or is_tail or is_engine:
            # Jet color: Pure crisp aeronautical white with slight cyan highlight
            return (248, 250, 252, 255)

        # 3. Pilot Gold Captain Wings (Curved horizon beneath jet)
        h_dy = (y - size * 0.58)
        curve = (abs(x - size/2) / (size * 0.42)) ** 2 * (size * 0.08)
        if 0 <= (h_dy + curve) <= size * 0.022 and abs(x - size/2) <= size * 0.42:
            return (234, 179, 8, 255) # Captain Gold

        # 4. "ATPL" Bold Pilot Typography
        if text_grid[y][x]:
            return (255, 255, 255, 255)

        return (r, g, b, 255)

    return make_png(size, size, get_pixel)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dashboard_dir = os.path.join(base_dir, "dashboard")
    
    print("🎨 Generando icono de alta resolución Apple Touch Icon (192x192)...")
    icon_192 = generate_atpl_icon(192)
    
    # Save to dashboard
    with open(os.path.join(dashboard_dir, "apple-touch-icon.png"), "wb") as f:
        f.write(icon_192)
    with open(os.path.join(dashboard_dir, "favicon.png"), "wb") as f:
        f.write(icon_192)
        
    # Also save to root directory for root-level requests
    with open(os.path.join(base_dir, "apple-touch-icon.png"), "wb") as f:
        f.write(icon_192)
    with open(os.path.join(base_dir, "favicon.png"), "wb") as f:
        f.write(icon_192)
        
    print("✅ Iconos guardados con éxito:")
    print(f"   - {os.path.join(dashboard_dir, 'apple-touch-icon.png')}")
    print(f"   - {os.path.join(dashboard_dir, 'favicon.png')}")
    print(f"   - {os.path.join(base_dir, 'apple-touch-icon.png')}")

if __name__ == "__main__":
    main()
