#!/usr/bin/env python3
"""
Master 80-Page Air Law Generator.
Builds all 25 chapters of 010 Air Law to the target depth of ~75-85 pages.
Every chapter contains:
1. Legal and Theoretical Foundations
2. Complete Regulatory Standards & Technical Values
3. AviationExam Specific Traps & Pitfalls
4. Step-by-Step Worked Practical Scenarios
5. 5 Full-Length Multiple-Choice Exam Questions (A, B, C, D) with Detailed Explanations
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"
os.makedirs(BASE_DIR, exist_ok=True)

def add_q(pdf, num, text, opt_a, opt_b, opt_c, opt_d, correct_letter, explanation):
    pdf.add_heading_2(f"AviationExam Question {num}")
    pdf.add_paragraph(text, max_chars=90)
    opts = f"[A] {opt_a}\n[B] {opt_b}\n[C] {opt_c}\n[D] {opt_d}"
    pdf.add_paragraph(opts, max_chars=88)
    exp_text = f"CORRECT: [{correct_letter}].\n{explanation}"
    pdf.add_callout("definition", "Exam Analysis & Rationale", exp_text, max_chars=86)

print("Master generator module initialized.")
