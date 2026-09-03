#!/usr/bin/env python3
"""
Scan pages 1-15 of Book 1 and Book 2 for text.
"""
import os
import re
import zlib

def dump_page_texts(fpath, max_p=12):
    with open(fpath, "rb") as f:
        data = f.read()

    # Find all /Type /Page objects
    page_matches = list(re.finditer(rb'(\d+)\s+0\s+obj[\s\S]*?/Type\s*/Page\b(?!\s*/Pages)[\s\S]*?endobj', data))
    print(f"\n{fpath}: Found {len(page_matches)} page objects")

    for p_idx, pm in enumerate(page_matches[:max_p]):
        p_str = pm.group(0)
        c_matches = re.findall(rb'/Contents\s+(\d+)\s+0\s+R', p_str)
        if not c_matches:
            c_arr = re.search(rb'/Contents\s*\[([^\]]+)\]', p_str)
            if c_arr:
                c_matches = re.findall(rb'(\d+)\s+0\s+R', c_arr.group(1))

        all_text = ""
        for cid in c_matches:
            cid_int = int(cid)
            obj_m = re.search(rf'\b{cid_int}\s+0\s+obj[\s\S]*?stream\r?\n([\s\S]*?)\r?\nendstream', data.decode('latin1', 'ignore'))
            if obj_m:
                raw_bytes = obj_m.group(1).encode('latin1', 'ignore')
                try:
                    decomp = zlib.decompress(raw_bytes)
                    # Find strings in parentheses
                    strings = re.findall(rb'\(([^\\)]*(?:\\.[^\\)]*)*)\)', decomp)
                    for s in strings:
                        s_clean = s.decode('latin1', 'ignore').replace('\\', '')
                        if len(s_clean) > 2:
                            all_text += s_clean + " "
                except Exception:
                    pass
        if len(all_text) > 30:
            print(f"Page {p_idx+1}: {all_text[:300]}")

if __name__ == "__main__":
    dump_page_texts("CAE Oxford Aviation Academy - 031 & 032 Mass and Balance & Performance.pdf", 10)
    dump_page_texts("CAE Oxford Aviation Academy - 033 Flight Planning and Monitoring.pdf", 10)
