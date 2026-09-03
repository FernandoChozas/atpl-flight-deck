#!/usr/bin/env python3
"""
Inspect Table of Contents / Outline of Convocatoria 3 Oxford Textbooks.
"""

import os
import re
import zlib

def inspect_pdf_outlines(fpath):
    print(f"\n=======================================================")
    print(f"Inspecting: {fpath}")
    print(f"=======================================================")
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        return

    with open(fpath, "rb") as f:
        data = f.read()

    print(f"File size: {len(data):,} bytes")

    # Search for /Title in outline items
    titles = re.findall(rb'/Title\s*\(([^)]+)\)', data)
    if titles:
        print(f"Found {len(titles)} bookmark titles:")
        for i, t in enumerate(titles[:40]):
            try:
                title_str = t.decode('latin1')
                print(f"  {i+1}: {title_str}")
            except Exception:
                pass
    else:
        # Search for hex titles /Title <...>
        hex_titles = re.findall(rb'/Title\s*<([0-9A-Fa-f]+)>', data)
        if hex_titles:
            print(f"Found {len(hex_titles)} hex bookmark titles:")
            for i, h in enumerate(hex_titles[:40]):
                try:
                    bytes_val = bytes.fromhex(h.decode('ascii'))
                    title_str = bytes_val.decode('utf-16-be', 'ignore')
                    print(f"  {i+1}: {title_str}")
                except Exception:
                    pass
        else:
            print("No outline /Title found directly in raw text.")

if __name__ == "__main__":
    b1 = "CAE Oxford Aviation Academy - 031 & 032 Mass and Balance & Performance.pdf"
    if not os.path.exists(b1):
        b1 = "CAE Oxford Aviation Academy - 031 _ 032 Mass and Balance _ Performance.pdf"
    b2 = "CAE Oxford Aviation Academy - 033 Flight Planning and Monitoring.pdf"

    inspect_pdf_outlines(b1)
    inspect_pdf_outlines(b2)
