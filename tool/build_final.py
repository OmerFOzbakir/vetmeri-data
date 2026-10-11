# -*- coding: utf-8 -*-
"""
Kümülatif 7'li Modül Birleştirici:
1. Ders: Anesteziye Giriş & Muayene (38 Slayt - 65 Soru)
2. Ders: Preanestezik İlaçlar & İndüksiyon (74 Slayt - 60 Soru)
3. Ders: Sindirim Sistemi Hastalıkları (240 Slayt - 140 Soru)
4. Ders: Genel Anestezi & Anestezi Dönemleri (22 Slayt - 55 Soru)
5. Ders: Anestezi Ekipmanları ve Cihazları (25 Slayt - 60 Soru)
6. Ders: İnhalasyon Anestezikleri & Farmakolojisi (24 Slayt - 60 Soru)
7. Ders: Anestezi Hastasının Monitörizasyonu (35 Slayt - 65 Soru)
"""
import json
import os
import re

from sindirim_notes import METADATA as SIND_METADATA, SUMMARY_SECTIONS as SIND_SUMMARY_SECTIONS, BILGI_KARTLARI as SIND_BILGI_KARTLARI, ACIK_UCLU_SORULAR as SIND_ACIK_UCLU_SORULAR
from sindirim_part1 import QUESTIONS_PART1
from sindirim_part2 import QUESTIONS_PART2
from sindirim_part3 import QUESTIONS_PART3

from genel_anestezi_notes import (
    METADATA as GA_METADATA,
    SUMMARY_SECTIONS as GA_SUMMARY_SECTIONS,
    BILGI_KARTLARI as GA_BILGI_KARTLARI,
    ACIK_UCLU_SORULAR as GA_ACIK_UCLU_SORULAR,
    COKTAN_SECMELI_SORULAR as GA_COKTAN_SECMELI_SORULAR
)

from ekipman_notes import (
    METADATA as EKIP_METADATA,
    SUMMARY_SECTIONS as EKIP_SUMMARY_SECTIONS,
    BILGI_KARTLARI as EKIP_BILGI_KARTLARI,
    ACIK_UCLU_SORULAR as EKIP_ACIK_UCLU_SORULAR,
    COKTAN_SECMELI_SORULAR as EKIP_COKTAN_SECMELI_SORULAR
)

from inhalasyon_notes import (
    METADATA as INHAL_METADATA,
    SUMMARY_SECTIONS as INHAL_SUMMARY_SECTIONS,
    BILGI_KARTLARI as INHAL_BILGI_KARTLARI,
    ACIK_UCLU_SORULAR as INHAL_ACIK_UCLU_SORULAR,
    COKTAN_SECMELI_SORULAR as INHAL_COKTAN_SECMELI_SORULAR
)

from monitorizasyon_notes import (
    METADATA as MON_METADATA,
    SUMMARY_SECTIONS as MON_SUMMARY_SECTIONS,
    BILGI_KARTLARI as MON_BILGI_KARTLARI,
    ACIK_UCLU_SORULAR as MON_ACIK_UCLU_SORULAR,
    COKTAN_SECMELI_SORULAR as MON_COKTAN_SECMELI_SORULAR
)

# 1. Mevcut data.js'den anestezi verisini oku
with open('data.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Anestezi modülü
start_idx = js_content.find('{')
end_idx = js_content.rfind('};') + 1
modules_dict = json.loads(js_content[start_idx:end_idx])
anestezi_module = modules_dict['anestezi']

# 2. preanestezi_extracted.json'dan 2. dersi oku
with open('tool/preanestezi_extracted.json', 'r', encoding='utf-8') as f:
    pre_data = json.load(f)

preanestezi_module = {
    "id": "preanestezi",
    "name": "2. Ders: Preanestezik İlaçlar & İndüksiyon",
    "shortName": "Preanestezik İlaçlar",
    "icon": "💊",
    "badge": "74 Slayt • Atropin, Ksilazin, Ketamin, Tiyopental & Entübasyon",
    "kategori": "Veteriner Cerrahi ve Anesteziyoloji",
    "alt_kategori": "Preanestezik İlaçlar, Enjektabl Anestezikler ve İndüksiyon",
    "ozet": "Bu eğitim modülü; cerrahide preanestezik ilaçların amaçlarını, antikolinerjikler (Atropin), tranklizanlar (Asepromazin), benzodiazepinler (Diazepam, Midazolam), alfa-2 agonistler (Ksilazin), opioidler (Morfin, Fentanil), barbitüratlar (Tiyopental), dissosiyatifler (Ketamin), propofol ve endotrakeal entübasyon ilkelerini kapsamaktadır.",
    "kilit_noktalar": [
        "Preanestezikler sedasyon sağlamak, eksitasyonsuz giriş-çıkış temin etmek ve genel anestezik dozunu azaltmak için kullanılır (Slayt 4).",
        "Atropin vagus uyarımını engelleyerek bradikardiyi ve kardiyak debi düşüşünü önler; ketaminle salya aspirasyonunu engellemek için şarttır (Slayt 6, 7).",
        "Kuşlarda iris çizgili kas yapısında olduğu için atropin kuşlarda midriyazis oluşturmaz (Slayt 8).",
        "Asepromazin periferik vazodilatasyonla hipotermi ve hipotansiyon yapar; şoktaki hayvanda kullanılmaz, nöbet eşiğini düşürür (Slayt 14).",
        "Benzodiazepinlerin (Diazepam, Midazolam) sedatif ve analjezik etkisi YOKTUR; güçlü kas gevşetici ve antikonvülzandırlar, antidotu Flumazenildir (Slayt 16, 17).",
        "Ksilazin sedasyonu 1-2 saat sürerken, analjezik etkisi yalnızca 15-30 dakikadır; gebelerde abortus yapabilir (Slayt 18, 19).",
        "Tiyopental alkali pH (11-12) nedeniyle perivasküler veya intraarteriyel kaçarsa doku nekrozu ve gangrene yol açar (Slayt 32).",
        "Ketaminde palpebral refleks ve yutkunma refleksi kaybolmaz; gözler açık kalır, kornea kurumaması için göz pomadı zorunludur (Slayt 41).",
        "Ekstübasyon (tüpün çekilmesi) hayvanda yutkunma refleksi başladığı anda hemen yapılmalıdır; gecikilirse tüp ısırılıp koparılabilir (Slayt 74)."
    ],
    "summarySections": pre_data["summary_sections"],
    "bilgi_kartlari": pre_data["flashcards"],
    "acik_uclu_sorular": pre_data["open_ended"],
    "coktan_secmeli_sorular": pre_data["quiz_questions"]
}

# 3. Sindirim modülü (3. Ders)
sindirim_mcqs = QUESTIONS_PART1 + QUESTIONS_PART2 + QUESTIONS_PART3

sindirim_module = {
    "id": "sindirim",
    "name": "3. Ders: Kedi & Köpek Sindirim Sistemi Hastalıkları",
    "shortName": "Sindirim Sistemi",
    "icon": "🐾",
    "badge": "240 Slayt • Özefagus, Mide, GDV, İntestinal & Vaka",
    "kategori": SIND_METADATA["kategori"],
    "alt_kategori": SIND_METADATA["alt_kategori"],
    "ozet": SIND_METADATA["ozet"],
    "kilit_noktalar": SIND_METADATA["kilit_noktalar"],
    "summarySections": SIND_SUMMARY_SECTIONS,
    "bilgi_kartlari": SIND_BILGI_KARTLARI,
    "acik_uclu_sorular": SIND_ACIK_UCLU_SORULAR,
    "coktan_secmeli_sorular": sindirim_mcqs
}

# 4. Genel Anestezi modülü (4. Ders)
genel_anestezi_module = {
    "id": "genel_anestezi",
    "name": GA_METADATA["name"],
    "shortName": GA_METADATA["shortName"],
    "icon": GA_METADATA["icon"],
    "badge": GA_METADATA["badge"],
    "kategori": GA_METADATA["kategori"],
    "alt_kategori": GA_METADATA["alt_kategori"],
    "ozet": GA_METADATA["ozet"],
    "kilit_noktalar": GA_METADATA["kilit_noktalar"],
    "summarySections": GA_SUMMARY_SECTIONS,
    "bilgi_kartlari": GA_BILGI_KARTLARI,
    "acik_uclu_sorular": GA_ACIK_UCLU_SORULAR,
    "coktan_secmeli_sorular": GA_COKTAN_SECMELI_SORULAR
}

# 5. Anestezi Ekipmanları modülü (5. Ders)
ekipman_module = {
    "id": "ekipmanlar",
    "name": EKIP_METADATA["name"],
    "shortName": EKIP_METADATA["shortName"],
    "icon": EKIP_METADATA["icon"],
    "badge": EKIP_METADATA["badge"],
    "kategori": EKIP_METADATA["kategori"],
    "alt_kategori": EKIP_METADATA["alt_kategori"],
    "ozet": EKIP_METADATA["ozet"],
    "kilit_noktalar": EKIP_METADATA["kilit_noktalar"],
    "summarySections": EKIP_SUMMARY_SECTIONS,
    "bilgi_kartlari": EKIP_BILGI_KARTLARI,
    "acik_uclu_sorular": EKIP_ACIK_UCLU_SORULAR,
    "coktan_secmeli_sorular": EKIP_COKTAN_SECMELI_SORULAR
}

# 6. İnhalasyon Anestezikleri modülü (6. Ders)
inhalasyon_module = {
    "id": "inhalasyon",
    "name": INHAL_METADATA["name"],
    "shortName": INHAL_METADATA["shortName"],
    "icon": INHAL_METADATA["icon"],
    "badge": INHAL_METADATA["badge"],
    "kategori": INHAL_METADATA["kategori"],
    "alt_kategori": INHAL_METADATA["alt_kategori"],
    "ozet": INHAL_METADATA["ozet"],
    "kilit_noktalar": INHAL_METADATA["kilit_noktalar"],
    "summarySections": INHAL_SUMMARY_SECTIONS,
    "bilgi_kartlari": INHAL_BILGI_KARTLARI,
    "acik_uclu_sorular": INHAL_ACIK_UCLU_SORULAR,
    "coktan_secmeli_sorular": INHAL_COKTAN_SECMELI_SORULAR
}

# 7. Anestezi Monitörizasyonu modülü (7. Ders)
monitorizasyon_module = {
    "id": "monitorizasyon",
    "name": MON_METADATA["name"],
    "shortName": MON_METADATA["shortName"],
    "icon": MON_METADATA["icon"],
    "badge": MON_METADATA["badge"],
    "kategori": MON_METADATA["kategori"],
    "alt_kategori": MON_METADATA["alt_kategori"],
    "ozet": MON_METADATA["ozet"],
    "kilit_noktalar": MON_METADATA["kilit_noktalar"],
    "summarySections": MON_SUMMARY_SECTIONS,
    "bilgi_kartlari": MON_BILGI_KARTLARI,
    "acik_uclu_sorular": MON_ACIK_UCLU_SORULAR,
    "coktan_secmeli_sorular": MON_COKTAN_SECMELI_SORULAR
}

# 8. Kümülatif Veritabanı
all_modules = {
    "monitorizasyon": monitorizasyon_module,
    "inhalasyon": inhalasyon_module,
    "ekipmanlar": ekipman_module,
    "genel_anestezi": genel_anestezi_module,
    "sindirim": sindirim_module,
    "preanestezi": preanestezi_module,
    "anestezi": anestezi_module
}

new_js_content = f"""// VetMeri Eğitim Modülleri Veri Tabanı (Kümülatif 7 Modül)
window.ALL_MODULES = {json.dumps(all_modules, ensure_ascii=False, indent=2)};

// Geriye dönük uyumluluk (Varsayılan aktif modül: Hasta Monitörizasyonu)
window.MODULE_DATA = window.ALL_MODULES["monitorizasyon"];
"""

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_js_content)

print("data.js güncellendi!")
print(f"1. Anestezi: {len(anestezi_module['coktan_secmeli_sorular'])} MCQ, {len(anestezi_module['bilgi_kartlari'])} Kart, {len(anestezi_module['acik_uclu_sorular'])} Klasik")
print(f"2. Preanestezi: {len(preanestezi_module['coktan_secmeli_sorular'])} MCQ, {len(preanestezi_module['bilgi_kartlari'])} Kart, {len(preanestezi_module['acik_uclu_sorular'])} Klasik")
print(f"3. Sindirim: {len(sindirim_module['coktan_secmeli_sorular'])} MCQ, {len(sindirim_module['bilgi_kartlari'])} Kart, {len(sindirim_module['acik_uclu_sorular'])} Klasik")
print(f"4. Genel Anestezi: {len(genel_anestezi_module['coktan_secmeli_sorular'])} MCQ, {len(genel_anestezi_module['bilgi_kartlari'])} Kart, {len(genel_anestezi_module['acik_uclu_sorular'])} Klasik")
print(f"5. Anestezi Ekipmanları: {len(ekipman_module['coktan_secmeli_sorular'])} MCQ, {len(ekipman_module['bilgi_kartlari'])} Kart, {len(ekipman_module['acik_uclu_sorular'])} Klasik")
print(f"6. İnhalasyon Anestezikleri: {len(inhalasyon_module['coktan_secmeli_sorular'])} MCQ, {len(inhalasyon_module['bilgi_kartlari'])} Kart, {len(inhalasyon_module['acik_uclu_sorular'])} Klasik")
print(f"7. Hasta Monitörizasyonu: {len(monitorizasyon_module['coktan_secmeli_sorular'])} MCQ, {len(monitorizasyon_module['bilgi_kartlari'])} Kart, {len(monitorizasyon_module['acik_uclu_sorular'])} Klasik")

total_mcq = (
    len(anestezi_module['coktan_secmeli_sorular']) +
    len(preanestezi_module['coktan_secmeli_sorular']) +
    len(sindirim_module['coktan_secmeli_sorular']) +
    len(genel_anestezi_module['coktan_secmeli_sorular']) +
    len(ekipman_module['coktan_secmeli_sorular']) +
    len(inhalasyon_module['coktan_secmeli_sorular']) +
    len(monitorizasyon_module['coktan_secmeli_sorular'])
)
print(f"TOPLAM KÜMÜLATİF SORU: {total_mcq} MCQ")

# 9. data.json'ı da 7 dersli olarak güncelle
data_json = {
    "lessons": [
        {
            "id": "lesson_1",
            "title": anestezi_module["name"],
            "subtitle": anestezi_module["badge"],
            "icon": anestezi_module["icon"],
            "summarySections": anestezi_module["summarySections"],
            "flashcards": [
                {"id": f.get("kart_id", f.get("id")), "question": f.get("on_yuz", f.get("question")), "answer": f.get("arka_yuz", f.get("answer"))}
                for f in anestezi_module["bilgi_kartlari"]
            ],
            "quizQuestions": [
                {
                    "id": q.get("soru_id", q.get("id")),
                    "question": q.get("soru_metni", q.get("question")),
                    "options": q.get("secenekler", q.get("options")),
                    "correctAnswer": q.get("dogru_cevap", q.get("correctAnswer")),
                    "explanation": q.get("aciklama", {}).get("genel", q.get("explanation", "")),
                    "distractorAnalysis": q.get("aciklama", {}).get("celdirici_analizi", q.get("distractorAnalysis", "")),
                    "slideNumber": q.get("slayt_no", q.get("slideNumber", 1))
                }
                for q in anestezi_module["coktan_secmeli_sorular"]
            ],
            "openEndedQuestions": [
                {
                    "id": o.get("soru_id", o.get("id")),
                    "question": o.get("soru", o.get("question")),
                    "idealAnswer": o.get("ideal_cevap", o.get("idealAnswer")),
                    "slideNumber": o.get("slayt_no", o.get("slideNumber", 1))
                }
                for o in anestezi_module["acik_uclu_sorular"]
            ]
        },
        {
            "id": "lesson_2",
            "title": preanestezi_module["name"],
            "subtitle": preanestezi_module["badge"],
            "icon": preanestezi_module["icon"],
            "summarySections": preanestezi_module["summarySections"],
            "flashcards": [
                {"id": f["kart_id"], "question": f["on_yuz"], "answer": f["arka_yuz"]}
                for f in preanestezi_module["bilgi_kartlari"]
            ],
            "quizQuestions": [
                {
                    "id": q["soru_id"],
                    "question": q["soru_metni"],
                    "options": q["secenekler"],
                    "correctAnswer": q["dogru_cevap"],
                    "explanation": q["aciklama"]["genel"],
                    "distractorAnalysis": q["aciklama"]["celdirici_analizi"],
                    "slideNumber": q["slayt_no"]
                }
                for q in preanestezi_module["coktan_secmeli_sorular"]
            ],
            "openEndedQuestions": [
                {
                    "id": o["soru_id"],
                    "question": o["soru"],
                    "idealAnswer": o["ideal_cevap"],
                    "slideNumber": o["slayt_no"]
                }
                for o in preanestezi_module["acik_uclu_sorular"]
            ]
        },
        {
            "id": "lesson_3",
            "title": sindirim_module["name"],
            "subtitle": sindirim_module["badge"],
            "icon": sindirim_module["icon"],
            "summarySections": sindirim_module["summarySections"],
            "flashcards": [
                {"id": f["kart_id"], "question": f["on_yuz"], "answer": f["arka_yuz"]}
                for f in sindirim_module["bilgi_kartlari"]
            ],
            "quizQuestions": [
                {
                    "id": q["soru_id"],
                    "question": q["soru_metni"],
                    "options": q["secenekler"],
                    "correctAnswer": q["dogru_cevap"],
                    "explanation": q["aciklama"]["genel"],
                    "distractorAnalysis": q["aciklama"]["celdirici_analizi"],
                    "slideNumber": q["slayt_no"]
                }
                for q in sindirim_module["coktan_secmeli_sorular"]
            ],
            "openEndedQuestions": [
                {
                    "id": o["soru_id"],
                    "question": o["soru"],
                    "idealAnswer": o["ideal_cevap"],
                    "slideNumber": o["slayt_no"]
                }
                for o in sindirim_module["acik_uclu_sorular"]
            ]
        },
        {
            "id": "lesson_4",
            "title": genel_anestezi_module["name"],
            "subtitle": genel_anestezi_module["badge"],
            "icon": genel_anestezi_module["icon"],
            "summarySections": genel_anestezi_module["summarySections"],
            "flashcards": [
                {"id": f["kart_id"], "question": f["on_yuz"], "answer": f["arka_yuz"]}
                for f in genel_anestezi_module["bilgi_kartlari"]
            ],
            "quizQuestions": [
                {
                    "id": q["soru_id"],
                    "question": q["soru_metni"],
                    "options": q["secenekler"],
                    "correctAnswer": q["dogru_cevap"],
                    "explanation": q["aciklama"]["genel"],
                    "distractorAnalysis": q["aciklama"]["celdirici_analizi"],
                    "slideNumber": q["slayt_no"]
                }
                for q in genel_anestezi_module["coktan_secmeli_sorular"]
            ],
            "openEndedQuestions": [
                {
                    "id": o["soru_id"],
                    "question": o["soru"],
                    "idealAnswer": o["ideal_cevap"],
                    "slideNumber": o["slayt_no"]
                }
                for o in genel_anestezi_module["acik_uclu_sorular"]
            ]
        },
        {
            "id": "lesson_5",
            "title": ekipman_module["name"],
            "subtitle": ekipman_module["badge"],
            "icon": ekipman_module["icon"],
            "summarySections": ekipman_module["summarySections"],
            "flashcards": [
                {"id": f["kart_id"], "question": f["on_yuz"], "answer": f["arka_yuz"]}
                for f in ekipman_module["bilgi_kartlari"]
            ],
            "quizQuestions": [
                {
                    "id": q["soru_id"],
                    "question": q["soru_metni"],
                    "options": q["secenekler"],
                    "correctAnswer": q["dogru_cevap"],
                    "explanation": q["aciklama"]["genel"],
                    "distractorAnalysis": q["aciklama"]["celdirici_analizi"],
                    "slideNumber": q["slayt_no"]
                }
                for q in ekipman_module["coktan_secmeli_sorular"]
            ],
            "openEndedQuestions": [
                {
                    "id": o["soru_id"],
                    "question": o["soru"],
                    "idealAnswer": o["ideal_cevap"],
                    "slideNumber": o["slayt_no"]
                }
                for o in ekipman_module["acik_uclu_sorular"]
            ]
        },
        {
            "id": "lesson_6",
            "title": inhalasyon_module["name"],
            "subtitle": inhalasyon_module["badge"],
            "icon": inhalasyon_module["icon"],
            "summarySections": inhalasyon_module["summarySections"],
            "flashcards": [
                {"id": f["kart_id"], "question": f["on_yuz"], "answer": f["arka_yuz"]}
                for f in inhalasyon_module["bilgi_kartlari"]
            ],
            "quizQuestions": [
                {
                    "id": q["soru_id"],
                    "question": q["soru_metni"],
                    "options": q["secenekler"],
                    "correctAnswer": q["dogru_cevap"],
                    "explanation": q["aciklama"]["genel"],
                    "distractorAnalysis": q["aciklama"]["celdirici_analizi"],
                    "slideNumber": q["slayt_no"]
                }
                for q in inhalasyon_module["coktan_secmeli_sorular"]
            ],
            "openEndedQuestions": [
                {
                    "id": o["soru_id"],
                    "question": o["soru"],
                    "idealAnswer": o["ideal_cevap"],
                    "slideNumber": o["slayt_no"]
                }
                for o in inhalasyon_module["acik_uclu_sorular"]
            ]
        },
        {
            "id": "lesson_7",
            "title": monitorizasyon_module["name"],
            "subtitle": monitorizasyon_module["badge"],
            "icon": monitorizasyon_module["icon"],
            "summarySections": monitorizasyon_module["summarySections"],
            "flashcards": [
                {"id": f["kart_id"], "question": f["on_yuz"], "answer": f["arka_yuz"]}
                for f in monitorizasyon_module["bilgi_kartlari"]
            ],
            "quizQuestions": [
                {
                    "id": q["soru_id"],
                    "question": q["soru_metni"],
                    "options": q["secenekler"],
                    "correctAnswer": q["dogru_cevap"],
                    "explanation": q["aciklama"]["genel"],
                    "distractorAnalysis": q["aciklama"]["celdirici_analizi"],
                    "slideNumber": q["slayt_no"]
                }
                for q in monitorizasyon_module["coktan_secmeli_sorular"]
            ],
            "openEndedQuestions": [
                {
                    "id": o["soru_id"],
                    "question": o["soru"],
                    "idealAnswer": o["ideal_cevap"],
                    "slideNumber": o["slayt_no"]
                }
                for o in monitorizasyon_module["acik_uclu_sorular"]
            ]
        }
    ]
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data_json, f, ensure_ascii=False, indent=2)

print("data.json başarıyla 7 dersli olarak güncellendi!")
