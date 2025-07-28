# Adobe-Hackthon_2
#  PDF Heading Extractor (via Docker)

This project extracts **titles**, **headings**, and **subheadings** from a PDF document (up to 50 pages) using **Python** and **PyMuPDF**, and runs fully inside a **Docker container**. It uses font size analysis to distinguish different structural elements in the document.


##  Features

-  Extracts **Title**, **Heading**, **Subheading**, and **Body** based on font sizes
-  Works with PDF files up to **50 pages**
-  Runs seamlessly inside **D

-  pdf-heading-extractor/
├── main.py # Python script for PDF parsing and classification
├── requirements.txt # Python dependency list
├── Dockerfile # Docker instructions to build the container
├── sample.pdf # Optional test file (replace with your own)

##  Tech Stack

- Python 3.10
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- Docker
