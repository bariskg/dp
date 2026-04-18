from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

from app.services.storage import EXPORTS_DIR


class ExportDependencyError(RuntimeError):
    """Raised when an export dependency is not installed."""


def _slugify(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value.strip())
    return cleaned.strip("_") or "dosya"


def build_export_path(file_name: str, extension: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = _slugify(file_name)
    return EXPORTS_DIR / f"{safe_name}_{timestamp}.{extension}"


def export_docx(file_name: str, draft_text: str) -> Path:
    try:
        from docx import Document
    except ImportError as exc:
        raise ExportDependencyError(
            "Word export icin `python-docx` paketinin kurulmasi gerekiyor."
        ) from exc

    path = build_export_path(file_name, "docx")
    document = Document()
    for paragraph in draft_text.split("\n\n"):
        document.add_paragraph(paragraph)
    document.save(path)
    return path


def export_pdf(file_name: str, draft_text: str) -> Path:
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfbase.pdfmetrics import stringWidth
        from reportlab.pdfgen import canvas
    except ImportError as exc:
        raise ExportDependencyError(
            "PDF export icin `reportlab` paketinin kurulmasi gerekiyor."
        ) from exc

    path = build_export_path(file_name, "pdf")
    pdf = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4
    left_margin = 50
    top = height - 50
    line_height = 15
    font_name = "Helvetica"
    font_size = 11

    pdf.setFont(font_name, font_size)
    y = top

    for raw_paragraph in draft_text.split("\n"):
        line = raw_paragraph or " "
        words = line.split(" ")
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if stringWidth(candidate, font_name, font_size) <= width - (left_margin * 2):
                current = candidate
            else:
                pdf.drawString(left_margin, y, current)
                y -= line_height
                current = word
                if y <= 50:
                    pdf.showPage()
                    pdf.setFont(font_name, font_size)
                    y = top
        pdf.drawString(left_margin, y, current)
        y -= line_height
        if y <= 50:
            pdf.showPage()
            pdf.setFont(font_name, font_size)
            y = top

    pdf.save()
    return path
