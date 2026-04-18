from __future__ import annotations


def build_petition_draft(
    file_record: dict,
    intake_data: dict,
    suggestions: dict[str, list[dict[str, str]]],
) -> str:
    """Generate a first-pass divorce petition draft from local data."""
    divorce_type = intake_data.get("divorce_type") or file_record.get("case_type") or "-"
    plaintiff = intake_data.get("plaintiff_label") or "Davaci"
    defendant = intake_data.get("defendant_label") or "Davali"
    marriage_date = intake_data.get("marriage_date") or "belirtilmemistir"
    separation_status = intake_data.get("separation_status") or "belirtilmemistir"
    event_summary = intake_data.get("event_summary") or "Olay ozeti henuz girilmemistir."
    evidence_notes = intake_data.get("evidence_notes") or "Sun asamada ayri delil notu belirtilmemistir."

    request_lines: list[str] = ["Taraflarin bosanmalarina karar verilmesi"]
    if (intake_data.get("custody_request") or "").lower() == "evet":
        request_lines.append("Ortak cocuk varsa velayetin davaciya verilmesi")
    if (intake_data.get("alimony_request") or "").lower() == "evet":
        request_lines.append("Davaci lehine uygun nafakaya hukum olunmasi")
    if (intake_data.get("compensation_request") or "").lower() == "evet":
        request_lines.append("Davaci lehine uygun maddi ve manevi tazminata hukum olunmasi")
    request_lines.append("Yargilama giderleri ve vekalet ucretinin davaliya yukletilmesi")

    statute_lines = [
        f"- {item['reference']} ({item['title']})"
        for item in suggestions.get("statutes", [])
    ] or ["- Ilgili mevzuat daha sonra eklenecektir."]

    decision_lines = [
        f"- {item['title']} - {item['reference']}"
        for item in suggestions.get("decisions", [])
    ] or ["- Ilgili karar onerileri daha sonra eklenecektir."]

    request_block = "\n".join(f"{index}. {line}" for index, line in enumerate(request_lines, start=1))

    return f"""AILE MAHKEMESI SAYIN HAKIMLIGINE

DAVACI: {plaintiff}
DAVALI: {defendant}

KONU:
{divorce_type} niteligindeki bosanma davasina iliskin ilk taslak dilekcedir.

ACIKLAMALAR:
1. Taraflar {marriage_date} tarihinde evlenmis olup fiili durum olarak {separation_status.lower()}.
2. Davaya esas olaylar kisaca su sekildedir:
{event_summary}
3. Davacinin dayandigi ilk delil ve notlar su sekildedir:
{evidence_notes}

HUKUKI SEBEPLER:
{chr(10).join(statute_lines)}

EMSAL / ILGILI KARAR NOTLARI:
{chr(10).join(decision_lines)}

SONUC VE ISTEM:
Yukarida arz ve izah edilen nedenlerle;
{request_block}
karar verilmesini saygilarimizla arz ve talep ederiz.

EK NOT:
Bu metin ilk taslak olup, kaynaklar ve olay ayrintilari gelistikce zenginlestirilecektir.
"""
