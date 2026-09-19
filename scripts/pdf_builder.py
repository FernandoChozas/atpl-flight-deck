#!/usr/bin/env python3
"""
ATPL Professional PDF Document Builder
Generates publication-quality, vector-sharp PDF study manuals from structured Python data.
Pure Python (zero external dependencies).
A4 format with running headers, footers, callouts, and styled tables.
"""

import os
import zlib
import re

class PDFBuilder:
    PAGE_WIDTH = 595.28
    PAGE_HEIGHT = 841.89
    MARGIN_LEFT = 45.0
    MARGIN_RIGHT = 45.0
    MARGIN_TOP = 50.0
    MARGIN_BOTTOM = 50.0
    USABLE_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT

    def __init__(self, title, subject_code, chapter_str):
        self.title = title
        self.subject_code = subject_code
        self.chapter_str = chapter_str
        self.pages = []  # list of list of stream operations
        self.current_page_ops = []
        self.current_y = self.PAGE_HEIGHT - self.MARGIN_TOP
        self.font_regular = "F1"
        self.font_bold = "F2"
        self.font_italic = "F3"
        self.font_mono = "F4"
        self.start_new_page()

    def start_new_page(self):
        if self.current_page_ops:
            self.pages.append(self.current_page_ops)
        self.current_page_ops = []
        self.current_y = self.PAGE_HEIGHT - self.MARGIN_TOP

    def finish(self):
        if self.current_page_ops:
            self.pages.append(self.current_page_ops)
        self.current_page_ops = []

    def check_space(self, height_needed):
        if (self.current_y - height_needed) < self.MARGIN_BOTTOM:
            self.start_new_page()

    @staticmethod
    def normalize_text(text):
        # Map common typography characters to Windows-1252 / WinAnsi bytes
        replacements = {
            "\u2022": "- ",   # bullet to clean dash
            "\u2013": "-",     # en-dash
            "\u2014": "--",    # em-dash
            "\u2018": "'",     # left single quote
            "\u2019": "'",     # right single quote
            "\u201c": '"',     # left double quote
            "\u201d": '"',     # right double quote
            "≥": ">=",
            "≤": "<=",
            "°": "\xb0",      # degree sign in WinAnsi
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        # [MEJORA] Eliminar caracteres no imprimibles que corrompen el stream PDF
        text = ''.join(ch if ord(ch) < 256 else '?' for ch in text)
        return text

    # --- Drawing Primitives ---
    def draw_text(self, text, x, y, font="F1", size=10, r=0.15, g=0.15, b=0.15):
        # Escape special PDF characters and normalize WinAnsi
        safe_text = self.normalize_text(text)
        safe_text = safe_text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        self.current_page_ops.append(
            f"BT /{font} {size} Tf {r:.3f} {g:.3f} {b:.3f} rg {x:.2f} {y:.2f} Td ({safe_text}) Tj ET"
        )

    def draw_rect(self, x, y, width, height, fill_rgb=None, stroke_rgb=None, line_width=1.0):
        ops = ["q"]
        if fill_rgb:
            ops.append(f"{fill_rgb[0]:.3f} {fill_rgb[1]:.3f} {fill_rgb[2]:.3f} rg")
        if stroke_rgb:
            ops.append(f"{stroke_rgb[0]:.3f} {stroke_rgb[1]:.3f} {stroke_rgb[2]:.3f} RG {line_width:.2f} w")
        
        ops.append(f"{x:.2f} {y:.2f} {width:.2f} {height:.2f} re")
        if fill_rgb and stroke_rgb:
            ops.append("B")
        elif fill_rgb:
            ops.append("f")
        elif stroke_rgb:
            ops.append("S")
        ops.append("Q")
        self.current_page_ops.append(" ".join(ops))

    def draw_line(self, x1, y1, x2, y2, stroke_rgb=(0.7, 0.7, 0.7), line_width=0.75):
        self.current_page_ops.append(
            f"q {stroke_rgb[0]:.3f} {stroke_rgb[1]:.3f} {stroke_rgb[2]:.3f} RG {line_width:.2f} w "
            f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S Q"
        )

    # --- High-level Content Elements ---
    def add_title_banner(self, subject_name, chapter_num, chapter_title, pages_str):
        self.check_space(110)
        y = self.current_y
        
        # Banner box
        self.draw_rect(self.MARGIN_LEFT, y - 85, self.USABLE_WIDTH, 85, fill_rgb=(0.06, 0.18, 0.35), stroke_rgb=(0.04, 0.12, 0.25), line_width=1.5)
        
        # Accent top bar
        self.draw_rect(self.MARGIN_LEFT, y - 4, self.USABLE_WIDTH, 4, fill_rgb=(0.25, 0.65, 0.95))
        
        # Text inside banner
        self.draw_text(f"ATPL EASA STUDY GUIDE | {self.subject_code} - {subject_name.upper()}", 
                       self.MARGIN_LEFT + 16, y - 24, font="F2", size=9, r=0.7, g=0.85, b=1.0)
        
        # Chapter title (wrap by words cleanly)
        title_text = f"Chapter {chapter_num}: {chapter_title}"
        title_lines = self.wrap_text(title_text, 44)
        if len(title_lines) > 1:
            self.draw_text(title_lines[0], self.MARGIN_LEFT + 16, y - 46, font="F2", size=13.5, r=1.0, g=1.0, b=1.0)
            self.draw_text(title_lines[1], self.MARGIN_LEFT + 16, y - 62, font="F2", size=13.5, r=1.0, g=1.0, b=1.0)
        else:
            self.draw_text(title_text, self.MARGIN_LEFT + 16, y - 50, font="F2", size=14.5, r=1.0, g=1.0, b=1.0)

        # Meta tags badge
        meta_str = f"Syllabus Source: CAE Oxford (pp. {pages_str})  |  Pass Target: >= 90% AviationExam"
        self.draw_text(meta_str, self.MARGIN_LEFT + 16, y - 76, font="F1", size=8.5, r=0.75, g=0.82, b=0.92)

        self.current_y -= 102

    def add_heading_1(self, text):
        self.check_space(38)
        y = self.current_y
        self.draw_rect(self.MARGIN_LEFT, y - 22, self.USABLE_WIDTH, 22, fill_rgb=(0.92, 0.95, 0.98))
        self.draw_rect(self.MARGIN_LEFT, y - 22, 4, 22, fill_rgb=(0.10, 0.35, 0.65))
        self.draw_text(text.upper(), self.MARGIN_LEFT + 10, y - 16, font="F2", size=11, r=0.08, g=0.25, b=0.50)
        self.current_y -= 32

    def add_heading_2(self, text):
        self.check_space(26)
        y = self.current_y
        self.draw_text(text, self.MARGIN_LEFT, y - 14, font="F2", size=10.5, r=0.10, g=0.25, b=0.45)
        self.draw_line(self.MARGIN_LEFT, y - 18, self.MARGIN_LEFT + self.USABLE_WIDTH, y - 18, stroke_rgb=(0.82, 0.85, 0.90), line_width=0.75)
        self.current_y -= 26

    def wrap_text(self, text, max_chars):
        text = self.normalize_text(text)
        words = text.split(" ")
        lines = []
        cur_line = []
        cur_len = 0
        for w in words:
            if cur_len + len(w) + 1 <= max_chars:
                cur_line.append(w)
                cur_len += len(w) + 1
            else:
                if cur_line:
                    lines.append(" ".join(cur_line))
                cur_line = [w]
                cur_len = len(w)
        if cur_line:
            lines.append(" ".join(cur_line))
        return lines

    def add_paragraph(self, text, max_chars=95, size=9.5, font="F1", line_spacing=13.0, space_after=8.0):
        lines = self.wrap_text(text, max_chars)
        needed = len(lines) * line_spacing + space_after
        self.check_space(needed)
        for line in lines:
            self.draw_text(line, self.MARGIN_LEFT, self.current_y - 9, font=font, size=size, r=0.15, g=0.15, b=0.15)
            self.current_y -= line_spacing
        self.current_y -= space_after

    def add_bullet(self, title, text, max_chars=90):
        full_text = f"{title}: {text}" if title else text
        lines = self.wrap_text(full_text, max_chars)
        needed = len(lines) * 13.0 + 4.0
        self.check_space(needed)
        
        # Bullet dot
        self.draw_rect(self.MARGIN_LEFT + 4, self.current_y - 7, 3.5, 3.5, fill_rgb=(0.2, 0.45, 0.75))
        
        for i, line in enumerate(lines):
            self.draw_text(line, self.MARGIN_LEFT + 14, self.current_y - 9, font="F1", size=9.0, r=0.15, g=0.15, b=0.15)
            self.current_y -= 13.0
        self.current_y -= 3.0

    def add_callout(self, box_type, title, text, max_chars=88):
        # Config styles
        if box_type == "trap":
            bg = (0.99, 0.93, 0.93)
            border = (0.85, 0.22, 0.22)
            title_r, title_g, title_b = 0.75, 0.10, 0.10
            icon = "[!] EXAM TRAP (AVIATIONEXAM)"
        elif box_type == "definition":
            bg = (0.94, 0.97, 1.00)
            border = (0.18, 0.45, 0.85)
            title_r, title_g, title_b = 0.10, 0.30, 0.70
            icon = "[*] OFFICIAL DEFINITION"
        else: # key_fact / note
            bg = (0.98, 0.96, 0.90)
            border = (0.85, 0.60, 0.15)
            title_r, title_g, title_b = 0.65, 0.40, 0.05
            icon = "[KEY FACT]"

        lines = self.wrap_text(text, max_chars)
        box_height = 24 + len(lines) * 13.0 + 10.0
        self.check_space(box_height + 8.0)

        y = self.current_y
        # Box background & border
        self.draw_rect(self.MARGIN_LEFT, y - box_height, self.USABLE_WIDTH, box_height, fill_rgb=bg, stroke_rgb=border, line_width=1.0)
        # Left accent stripe
        self.draw_rect(self.MARGIN_LEFT, y - box_height, 4, box_height, fill_rgb=border)
        # Title
        full_title = f"{icon} - {title}" if title else icon
        self.draw_text(full_title, self.MARGIN_LEFT + 12, y - 16, font="F2", size=9.0, r=title_r, g=title_g, b=title_b)
        
        # Body
        cur_text_y = y - 30
        for l in lines:
            self.draw_text(l, self.MARGIN_LEFT + 12, cur_text_y, font="F1", size=8.5, r=0.15, g=0.15, b=0.15)
            cur_text_y -= 13.0

        self.current_y -= (box_height + 8.0)

    def add_table(self, headers, rows, col_widths=None):
        num_cols = len(headers)
        if not col_widths:
            w = self.USABLE_WIDTH / num_cols
            col_widths = [w] * num_cols

        header_height = 20.0
        self.check_space(header_height + 35)

        y = self.current_y
        # Draw Header row
        self.draw_rect(self.MARGIN_LEFT, y - header_height, self.USABLE_WIDTH, header_height, fill_rgb=(0.10, 0.28, 0.50))
        cur_x = self.MARGIN_LEFT
        for i, h in enumerate(headers):
            self.draw_text(h, cur_x + 6, y - 14, font="F2", size=8.5, r=1.0, g=1.0, b=1.0)
            cur_x += col_widths[i]
        self.current_y -= header_height

        # Draw Data rows with dynamic multi-line wrapping
        for r_idx, row in enumerate(rows):
            wrapped_cells = []
            max_lines = 1
            for c_idx, cell in enumerate(row):
                w_pts = col_widths[c_idx] - 10.0
                chars_per_line = max(5, int(w_pts / 4.7))  # [FIX] mínimo 5 evita bucle infinito con columnas muy estrechas
                lines = self.wrap_text(str(cell), chars_per_line)
                wrapped_cells.append(lines)
                if len(lines) > max_lines:
                    max_lines = len(lines)

            row_height = max_lines * 11.5 + 6.0
            self.check_space(row_height + 4)
            y = self.current_y

            fill = (0.96, 0.97, 0.99) if (r_idx % 2 == 1) else (1.0, 1.0, 1.0)
            self.draw_rect(self.MARGIN_LEFT, y - row_height, self.USABLE_WIDTH, row_height, fill_rgb=fill, stroke_rgb=(0.85, 0.88, 0.92), line_width=0.5)

            cur_x = self.MARGIN_LEFT
            for c_idx, cell_lines in enumerate(wrapped_cells):
                f = "F2" if c_idx == 0 else "F1"
                line_y = y - 11.0
                for l in cell_lines:
                    self.draw_text(l, cur_x + 5, line_y, font=f, size=7.8, r=0.15, g=0.15, b=0.15)
                    line_y -= 11.0
                cur_x += col_widths[c_idx]

            self.current_y -= row_height

        self.current_y -= 8.0

    # --- Compile PDF stream ---
    def compile_pdf(self, output_path):
        self.finish()
        total_pages = len(self.pages)

        # Add headers and footers to every page
        for p_idx, page_ops in enumerate(self.pages):
            page_num = p_idx + 1
            # Running Header
            header_ops = [
                f"BT /F2 8 Tf 0.4 0.4 0.4 rg {self.MARGIN_LEFT:.2f} {self.PAGE_HEIGHT - 28:.2f} Td (ATPL STUDY MANUAL  |  {self.subject_code} - {self.chapter_str}) Tj ET",
                f"BT /F1 8 Tf 0.5 0.5 0.5 rg {self.PAGE_WIDTH - self.MARGIN_RIGHT - 110:.2f} {self.PAGE_HEIGHT - 28:.2f} Td (EXCLUSIVELY FOR EXAM PREP) Tj ET",
                f"q 0.82 0.85 0.90 RG 0.5 w {self.MARGIN_LEFT:.2f} {self.PAGE_HEIGHT - 32:.2f} m {self.PAGE_WIDTH - self.MARGIN_RIGHT:.2f} {self.PAGE_HEIGHT - 32:.2f} l S Q"
            ]
            # Running Footer
            footer_ops = [
                f"q 0.82 0.85 0.90 RG 0.5 w {self.MARGIN_LEFT:.2f} 36.00 m {self.PAGE_WIDTH - self.MARGIN_RIGHT:.2f} 36.00 l S Q",
                f"BT /F1 8 Tf 0.5 0.5 0.5 rg {self.MARGIN_LEFT:.2f} 24.00 Td (EASA ECQB Syllabus Compliance  |  Target Score: >=90% AviationExam) Tj ET",
                f"BT /F2 8 Tf 0.3 0.3 0.3 rg {self.PAGE_WIDTH - self.MARGIN_RIGHT - 55:.2f} 24.00 Td (Page {page_num} of {total_pages}) Tj ET"
            ]
            page_ops[:0] = header_ops
            page_ops.extend(footer_ops)

        # Build PDF structure
        # Obj 1: Catalog
        # Obj 2: Pages
        # Obj 3..(3+N-1): Page objects
        # Obj 3+N: Font F1 (Helvetica)
        # Obj 3+N+1: Font F2 (Helvetica-Bold)
        # Obj 3+N+2: Font F3 (Helvetica-Oblique)
        # Obj 3+N+3: Font F4 (Courier)
        # Obj 3+N+4 .. : Content streams
        num_pages = len(self.pages)
        catalog_id = 1
        pages_id = 2
        page_start_id = 3
        font_f1_id = page_start_id + num_pages
        font_f2_id = font_f1_id + 1
        font_f3_id = font_f1_id + 2
        font_f4_id = font_f1_id + 3
        stream_start_id = font_f4_id + 1

        kids_refs = " ".join(f"{page_start_id + i} 0 R" for i in range(num_pages))
        
        objects = {}
        objects[catalog_id] = f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode("latin1")
        objects[pages_id] = f"<< /Type /Pages /Kids [{kids_refs}] /Count {num_pages} >>".encode("latin1")

        for i in range(num_pages):
            p_id = page_start_id + i
            s_id = stream_start_id + i
            page_dict = (
                f"<< /Type /Page /Parent {pages_id} 0 R "
                f"/MediaBox [0 0 {self.PAGE_WIDTH:.2f} {self.PAGE_HEIGHT:.2f}] "
                f"/Resources << /Font << "
                f"/F1 {font_f1_id} 0 R /F2 {font_f2_id} 0 R /F3 {font_f3_id} 0 R /F4 {font_f4_id} 0 R "
                f">> >> /Contents {s_id} 0 R >>"
            )
            objects[p_id] = page_dict.encode("latin1")

        objects[font_f1_id] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
        objects[font_f2_id] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"
        objects[font_f3_id] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"
        objects[font_f4_id] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>"

        for i, ops in enumerate(self.pages):
            s_id = stream_start_id + i
            stream_raw = "\n".join(ops).encode("windows-1252", "replace")
            compressed = zlib.compress(stream_raw)
            stream_obj = f"<< /Length {len(compressed)} /Filter /FlateDecode >>\nstream\n".encode("latin1") + compressed + b"\nendstream"
            objects[s_id] = stream_obj

        # Assemble PDF file
        out = bytearray()
        out.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        
        total_objs = max(objects.keys())
        offsets = {0: 0}
        for o_id in range(1, total_objs + 1):
            offsets[o_id] = len(out)
            out.extend(f"{o_id} 0 obj\n".encode("latin1"))
            out.extend(objects[o_id])
            out.extend(b"\nendobj\n")

        xref_pos = len(out)
        out.extend(f"xref\n0 {total_objs + 1}\n0000000000 65535 f \n".encode("latin1"))
        for o_id in range(1, total_objs + 1):
            out.extend(f"{offsets[o_id]:010d} 00000 n \n".encode("latin1"))

        trailer = f"trailer\n<< /Size {total_objs + 1} /Root {catalog_id} 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n"
        out.extend(trailer.encode("latin1"))

        dirname = os.path.dirname(os.path.abspath(output_path))
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(out)

        print(f"Generated PDF ({num_pages} pages): {output_path} ({len(out)} bytes)")
