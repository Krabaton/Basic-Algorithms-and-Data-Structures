from time import sleep


def convert_doc_to_pdf(doc_path, pdf_path):
    print(f"Converting {doc_path} to {pdf_path} ...")
    sleep(0.5)
    return f"{pdf_path}.pdf"

