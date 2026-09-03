#!/usr/bin/env python3
"""
Extract text from first 20 pages of Convocatoria 3 textbooks to read the Table of Contents.
"""

import os
import re
import zlib

def extract_toc(fpath, max_pages=15):
    print(f"\n=======================================================")
    print(f"Reading TOC from: {fpath}")
    print(f"=======================================================")
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        return

    with open(fpath, "rb") as f:
        data = f.read()

    # Find Kids
    m_pages = re.search(rb'/Type\s*/Pages\s*/Kids\s*\[([^\]]+)\]', data)
    if not m_pages:
        # Might be indirect or split
        kids_matches = re.findall(rb'/Kids\s*\[([^\]]+)\]', data)
        print(f"Kids matches found: {len(kids_matches)}")
        kids_str = b" ".join(kids_matches).decode('latin1', 'ignore')
    else:
        kids_str = m_pages.group(1).decode('latin1', 'ignore')

    page_refs = re.findall(r'(\d+)\s+0\s+R', kids_str)
    print(f"Total page references found: {len(page_refs)}")

    for i, p_ref in enumerate(page_refs[:max_pages]):
        p_id = int(p_ref)
        m_page = re.search(rf'{p_id}\s+0\s+obj([\s\S]*?)endobj', data.decode('latin1', 'ignore'))
        if not m_page:
            continue
        p_body = m_page.group(1)
        m_c = re.search(r'/Contents\s+(\d+)\s+0\s+R', p_body)
        if not m_c:
            m_c_arr = re.search(r'/Contents\s*\[([^\]]+)\]', p_body)
            if m_c_arr:
                c_ids = [int(x) for x in re.findall(r'(\d+)\s+0\s+R', m_c_arr.group(1))]
            else:
                continue
        else:
            c_ids = [int(m_c.group(1))]

        page_text = ""
        for c_id in c_ids:
            m_stream = re.search(rf'{c_id}\s+0\s+obj[\s\S]*?stream\r?\n([\s\S]*?)\r?\nendstream', data.decode('latin1', 'ignore'))
            if m_stream:
                raw_stream = m_stream.group(1).encode('latin1', 'ignore')
                try:
                    decomp = zlib.decompress(raw_stream)
                    # Extract text inside BT ... ET
                    text_parts = re.findall(rb'\(([^)]+)\)\s*T[jJ]', decomp)
                    for tp in text_parts:
                        page_text += tp.decode('latin1', 'ignore') + " "
                    # Also Tj in hex
                    text_hex = re.findall(rb'<([0-9A-Fa-f]+)>\s*T[jJ]', decomp)
                    for th in text_hex:
                        try:
                            page_text += bytes.fromhex(th.decode('ascii')).decode('latin1', 'ignore') + " "
                        except Exception:
                            pass
                except Exception as e:
                    pass

        clean_text = " ".join(page_text.split())
        if "Chapter" in clean_text or "Contents" in clean_text or "TABLE" in clean_text or len(clean_text) > 100:
            print(f"\n--- Page {i+1} Text Snippet (first 400 chars) ---")
            print(clean_text[:400])

if __name__ == "__main__":
    b1 = "CAE Oxford Aviation Academy - 031 & 032 Mass and Balance & Performance.pdf"
    if not os.path.exists(b1):
        b1 = "CAE Oxford Aviation Academy - 031 _ 032 Mass and Balance _ Performance.pdf"
    b2 = "CAE Oxford Aviation Academy - 033 Flight Planning and Monitoring.pdf"

    extract_toc(b1, max_pages=16)
    extract_toc(b2, max_pages=16)
