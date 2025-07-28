import fitz  # PyMuPDF
from collections import defaultdict
import sys
import os

def extract_text_with_fonts(pdf_path):
    doc = fitz.open(pdf_path)

    if len(doc) > 50:
        print(f"❌ PDF has {len(doc)} pages. Only up to 50 pages are allowed.")
        return None

    font_data = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for line in b["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if text:
                            font_data.append({
                                "text": text,
                                "size": span["size"],
                                "font": span["font"],
                                "page": page_num + 1
                            })
    return font_data

def categorize_text_by_font_size(font_data):
    size_buckets = defaultdict(list)
    for item in font_data:
        size_buckets[item["size"]].append(item)

    sorted_sizes = sorted(size_buckets.keys(), reverse=True)

    structure = {
        "Title": [],
        "Headings": [],
        "Subheadings": [],
        "Body": []
    }

    for i, size in enumerate(sorted_sizes):
        items = size_buckets[size]
        if i == 0:
            structure["Title"].extend(items)
        elif i == 1:
            structure["Headings"].extend(items)
        elif i == 2:
            structure["Subheadings"].extend(items)
        else:
            structure["Body"].extend(items)

    return structure

def print_structure(structure):
    for key in ["Title", "Headings", "Subheadings"]:
        print(f"\n=== {key} ===")
        for item in structure[key]:
            print(f"[Page {item['page']}] {item['text']}")

if _name_ == "_main_":
    pdf_file = "sample.pdf"  # You can mount another file in Docker
    if not os.path.exists(pdf_file):
        print("❌ PDF file not found. Please mount or copy one into the container.")
        sys.exit(1)

    font_data = extract_text_with_fonts(pdf_file)
    if font_data:
        structured = categorize_text_by_font_size(font_data)
        print_structure(structured)
