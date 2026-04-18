from __future__ import annotations


def suggest_sources(file_record: dict, intake_data: dict) -> dict[str, list[dict[str, str]]]:
    """Return first-pass source suggestions using simple rule-based matching."""
    divorce_type = (intake_data.get("divorce_type") or file_record.get("case_type") or "").lower()
    has_children = (intake_data.get("has_children") or "").lower()
    custody_request = (intake_data.get("custody_request") or "").lower()
    alimony_request = (intake_data.get("alimony_request") or "").lower()
    compensation_request = (intake_data.get("compensation_request") or "").lower()

    statutes: list[dict[str, str]] = [
        {
            "title": "Turk Medeni Kanunu - Bosanma genel hukumleri",
            "reference": "TMK m.161-166",
            "reason": "Bosanma sebepleri ve dava tipi icin temel dayanak maddelerdir.",
        }
    ]
    decisions: list[dict[str, str]] = [
        {
            "title": "Ornek karar - evlilik birliginin temelinden sarsilmasi",
            "reference": "Yargisal ornek / test veri",
            "reason": "Cekismeli bosanma olay ozetiyle uyumlu genel karar basligidir.",
        }
    ]

    if "anlasmali" in divorce_type:
        statutes.append(
            {
                "title": "Turk Medeni Kanunu - Anlasmali bosanma",
                "reference": "TMK m.166/3",
                "reason": "Anlasmali bosanma senaryolarinda dogrudan uygulanir.",
            }
        )
        decisions.append(
            {
                "title": "Ornek karar - anlasmali bosanma protokolu denetimi",
                "reference": "Aile hukuku ornek / test veri",
                "reason": "Protokolun hakim tarafindan denetlenmesi gereken durumlara isaret eder.",
            }
        )

    if "cekismeli" in divorce_type:
        statutes.append(
            {
                "title": "Turk Medeni Kanunu - Evlilik birliginin sarsilmasi",
                "reference": "TMK m.166/1-2",
                "reason": "Cekismeli bosanma taslaginda en temel hukuki dayanaklardan biridir.",
            }
        )

    if has_children == "evet" or custody_request == "evet":
        statutes.append(
            {
                "title": "Turk Medeni Kanunu - Velayet ve cocugun yarari",
                "reference": "TMK m.182",
                "reason": "Velayet ve cocukla ilgili taleplerde temel dayanaktir.",
            }
        )
        decisions.append(
            {
                "title": "Ornek karar - cocugun ustun yarari ve velayet",
                "reference": "Aile mahkemesi ornek / test veri",
                "reason": "Velayet taleplerinde degerlendirmenin cocugun yarari uzerinden yapildigini gosterir.",
            }
        )

    if alimony_request == "evet":
        statutes.append(
            {
                "title": "Turk Medeni Kanunu - Nafaka hukumleri",
                "reference": "TMK m.169, m.175, m.182",
                "reason": "Tedbir, yoksulluk ve istirak nafakasi talepleri icin temel maddelerdir.",
            }
        )
        decisions.append(
            {
                "title": "Ornek karar - nafaka degerlendirmesi",
                "reference": "Aile hukuku ornek / test veri",
                "reason": "Nafaka taleplerinde sosyal ve ekonomik durumun onemini vurgular.",
            }
        )

    if compensation_request == "evet":
        statutes.append(
            {
                "title": "Turk Medeni Kanunu - Maddi ve manevi tazminat",
                "reference": "TMK m.174",
                "reason": "Tazminat talebi iceren bosanma dosyalarinda dogrudan uygulanir.",
            }
        )
        decisions.append(
            {
                "title": "Ornek karar - bosanma nedeniyle tazminat",
                "reference": "Aile hukuku ornek / test veri",
                "reason": "Kusur ve kisilik hakki ihlali temelli tazminat degerlendirmelerine ornek olur.",
            }
        )

    return {"statutes": statutes, "decisions": decisions}
