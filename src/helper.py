def extract_references_from_pdf(pdf_path: str) -> str:
    """
    Opens a PDF, reads all text, and returns ONLY the References section
    (starting at the 'References' heading).
    """
    pdf_path = pdf_path
    text_chunks = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text_chunks.append(page_text)
    
    full_text = "\n".join(text_chunks)

    match = re.search(r"(?im)^\s*references\s*$", full_text)
    if not match:
        print("WARNING: could not find a clear 'References' heading, returning full text")
        return full_text
    
    start_index = match.start()

    # ---- 3) Slice from 'References' to the end ----
    references_text = full_text[start_index:]
    return references_text