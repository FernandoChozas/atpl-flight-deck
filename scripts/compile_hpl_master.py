#!/usr/bin/env python3
"""
Master Compiler for 040 Human Performance & Limitations Complete Study Guide.
Combines all 13 generated chapters of HPL into a single, cohesive, consolidated Master Study Guide:
resumenes/convocatoria_1/040_human_performance/040_HUMAN_PERFORMANCE_MASTER_COMPLETE_STUDY_GUIDE.pdf
"""

import os
import sys
import zlib
import re

MASTER_PDF_PATH = "resumenes/convocatoria_1/040_human_performance/040_HUMAN_PERFORMANCE_MASTER_COMPLETE_STUDY_GUIDE.pdf"

def merge_pdf_pages(pdf_files, output_path):
    """
    Pure Python vector PDF merger.
    Re-indexes objects from multiple PDFs and combines into one single master document.
    """
    pdf_docs = []
    for fpath in pdf_files:
        if not os.path.exists(fpath):
            print(f"Warning: File not found: {fpath}")
            continue
        with open(fpath, "rb") as f:
            pdf_docs.append(f.read())

    print(f"Merging {len(pdf_docs)} chapter PDFs into {output_path}...")

    # For each document, parse page objects
    page_objs_data = []
    for doc in pdf_docs:
        m_pages = re.search(rb'/Type\s*/Pages\s*/Kids\s*\[([^\]]+)\]', doc)
        if not m_pages:
            continue
        kids_str = m_pages.group(1).decode('latin1')
        page_refs = re.findall(r'(\d+)\s+0\s+R', kids_str)
        
        for p_ref in page_refs:
            p_id = int(p_ref)
            m_page_obj = re.search(rf'{p_id}\s+0\s+obj([\s\S]*?)endobj', doc.decode('latin1', 'ignore'))
            if m_page_obj:
                page_body = m_page_obj.group(1)
                m_contents = re.search(r'/Contents\s+(\d+)\s+0\s+R', page_body)
                if m_contents:
                    c_id = int(m_contents.group(1))
                    m_stream_obj = re.search(rf'{c_id}\s+0\s+obj([\s\S]*?)endobj', doc.decode('latin1', 'ignore'))
                    if m_stream_obj:
                        stream_raw = m_stream_obj.group(1)
                        page_objs_data.append((page_body, stream_raw))

    total_pages = len(page_objs_data)
    print(f"Total extracted pages: {total_pages}")

    # Build new master PDF
    out = bytearray()
    out.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")

    catalog_id = 1
    pages_id = 2
    page_start_id = 3
    font_f1_id = page_start_id + total_pages
    font_f2_id = font_f1_id + 1
    font_f3_id = font_f1_id + 2
    font_f4_id = font_f1_id + 3
    stream_start_id = font_f4_id + 1

    kids_refs = " ".join(f"{page_start_id + i} 0 R" for i in range(total_pages))
    objects = {}
    objects[catalog_id] = f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode("latin1")
    objects[pages_id] = f"<< /Type /Pages /Kids [{kids_refs}] /Count {total_pages} >>".encode("latin1")

    for i in range(total_pages):
        p_id = page_start_id + i
        s_id = stream_start_id + i
        page_dict = (
            f"<< /Type /Page /Parent {pages_id} 0 R "
            f"/MediaBox [0 0 595.28 841.89] "
            f"/Resources << /Font << "
            f"/F1 {font_f1_id} 0 R /F2 {font_f2_id} 0 R /F3 {font_f3_id} 0 R /F4 {font_f4_id} 0 R "
            f">> >> /Contents {s_id} 0 R >>"
        )
        objects[p_id] = page_dict.encode("latin1")

    objects[font_f1_id] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
    objects[font_f2_id] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"
    objects[font_f3_id] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"
    objects[font_f4_id] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>"

    for i, (page_body, stream_raw) in enumerate(page_objs_data):
        s_id = stream_start_id + i
        idx_s = stream_raw.find("stream\n")
        idx_e = stream_raw.find("\nendstream")
        if idx_s != -1 and idx_e != -1:
            raw_bytes = stream_raw[idx_s + 7:idx_e].encode("latin1", "ignore")
            try:
                dec = zlib.decompress(raw_bytes)
                comp = zlib.compress(dec)
                objects[s_id] = f"<< /Length {len(comp)} /Filter /FlateDecode >>\nstream\n".encode("latin1") + comp + b"\nendstream"
            except Exception:
                objects[s_id] = stream_raw.encode("latin1")
        else:
            objects[s_id] = b"<< /Length 0 >>\nstream\nendstream"

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

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(out)

    print(f"Master Consolidated PDF created successfully! Total Pages: {total_pages} ({len(out)} bytes)")

if __name__ == "__main__":
    chapter_files = [
        "resumenes/convocatoria_1/040_human_performance/040_ch01_human_factors_concepts.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch02_aviation_physiology_gas_laws.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch03_hypoxia_hyperventilation.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch04_dcs_barotrauma.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch05_vision_illusions.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch06_hearing_vestibular.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch07_toxic_hazards_health.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch08_information_processing_memory.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch09_human_error_reliability.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch10_decision_making_judgement.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch11_stress_workload.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch12_fatigue_sleep_circadian.pdf",
        "resumenes/convocatoria_1/040_human_performance/040_ch13_communication_crm.pdf"
    ]
    merge_pdf_pages(chapter_files, MASTER_PDF_PATH)
