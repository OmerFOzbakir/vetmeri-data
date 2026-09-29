# -*- coding: utf-8 -*-
"""
preanestezi_data.dart dosyasını eksiksiz parse eder
"""
import re
import json

with open('lib/data/preanestezi_data.dart', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Summary sections
summary_sections = []
sections_block_match = re.search(r'static const List<KeyPointSection> summarySections = \[(.*?)\];\s*// ================= 2\. BİLGİ KARTLARI', content, re.DOTALL)
if sections_block_match:
    block = sections_block_match.group(1)
    raw_secs = block.split('KeyPointSection(')
    for raw_sec in raw_secs:
        if not raw_sec.strip():
            continue
        title_m = re.search(r'title:\s*"([^"]+)"', raw_sec)
        icon_m = re.search(r'icon:\s*"([^"]+)"', raw_sec)
        points_m = re.search(r'points:\s*\[(.*?)\]', raw_sec, re.DOTALL)
        if title_m and icon_m and points_m:
            title = title_m.group(1)
            icon = icon_m.group(1)
            points_raw = points_m.group(1)
            points = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', points_raw)
            points = [p.replace('\\"', '"').replace('\\n', '\n') for p in points]
            summary_sections.append({
                "title": title,
                "icon": icon,
                "points": points
            })

# 2. Flashcards
flashcards = []
fc_pattern = re.compile(r'FlashcardItem\s*\(\s*id:\s*"([^"]+)",\s*question:\s*"([^"]+)",\s*answer:\s*"([^"]+)"\s*,?\s*\)', re.DOTALL)
for match in fc_pattern.finditer(content):
    flashcards.append({
        "kart_id": match.group(1),
        "on_yuz": match.group(2).replace('\\"', '"'),
        "arka_yuz": match.group(3).replace('\\"', '"')
    })

# 3. Quiz questions
quiz_questions = []
q_pattern = re.compile(
    r'QuizQuestionItem\s*\(\s*id:\s*"([^"]+)",\s*question:\s*"([^"]+)",\s*options:\s*\{(.*?)\},\s*correctAnswer:\s*"([^"]+)",\s*explanation:\s*"([^"]+)",\s*distractorAnalysis:\s*"([^"]+)",\s*slideNumber:\s*(\d+),?\s*\)',
    re.DOTALL
)

for match in q_pattern.finditer(content):
    qid = match.group(1)
    qtext = match.group(2).replace('\\"', '"')
    opts_raw = match.group(3)
    opts = {}
    opt_matches = re.findall(r'"([A-E])":\s*"([^"\\]*(?:\\.[^"\\]*)*)"', opts_raw)
    for letter, val in opt_matches:
        opts[letter] = val.replace('\\"', '"')
    corr = match.group(4)
    exp = match.group(5).replace('\\"', '"')
    dis = match.group(6).replace('\\"', '"')
    sno = int(match.group(7))
    quiz_questions.append({
        "soru_id": qid,
        "soru_metni": qtext,
        "secenekler": opts,
        "dogru_cevap": corr,
        "aciklama": {
            "genel": exp,
            "celdirici_analizi": dis
        },
        "slayt_no": sno,
        "zorluk_derecesi": "orta",
        "etiketler": ["preanestezi", "ilaclar"]
    })

# 4. Open-ended questions
open_ended = []
oe_pattern = re.compile(
    r'OpenEndedQuestionItem\s*\(\s*id:\s*"([^"]+)",\s*question:\s*"([^"]+)",\s*idealAnswer:\s*"((?:[^"\\]|\\.)*)",\s*slideNumber:\s*(\d+),?\s*\)',
    re.DOTALL
)

for match in oe_pattern.finditer(content):
    oid = match.group(1)
    qtext = match.group(2).replace('\\"', '"')
    ans = match.group(3).replace('\\"', '"').replace('\\n', '\n')
    sno = int(match.group(4))
    open_ended.append({
        "soru_id": oid,
        "soru": qtext,
        "ideal_cevap": ans,
        "degerlendirme_kriteri": "İdeal cevapta belirtilen mekanizma ve terimler aranmalıdır.",
        "slayt_no": sno
    })

print(f"Summary Sections: {len(summary_sections)}")
print(f"Flashcards: {len(flashcards)}")
print(f"Quiz Questions: {len(quiz_questions)}")
print(f"Open-Ended: {len(open_ended)}")

output_data = {
    "summary_sections": summary_sections,
    "flashcards": flashcards,
    "quiz_questions": quiz_questions,
    "open_ended": open_ended
}

with open('tool/preanestezi_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("tool/preanestezi_extracted.json olusturuldu!")
