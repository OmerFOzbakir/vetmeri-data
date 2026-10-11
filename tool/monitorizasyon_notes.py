# -*- coding: utf-8 -*-
"""
VetMeri - 7. Ders: Anestezi Hastasının Monitörizasyonu
Kapsam: 35 Slayt
(Monitörize edilen parametreler, Pulmoner monitörizasyon, Solunum sayı/derinlik/karakteri,
Atelektazi & Rezerv balon desteği, Taşipne & Apnetik solunum, PaCO2 sınırları, Kapnografi & Pulse Oksimetre,
Kardiyovasküler monitörizasyon, Kalp frekansı limitleri, Kan basıncı ölçümü [direkt/indirekt], Kritik perfüzyon sınırları,
CRT & İdrar çıkışı, Mukoza rengi & Kan kaybı toleransı, Isı regülasyonu [hipotermi/malign hipertermi],
Refleksler [palpebral, yutkunma, pedal, korneal], Kas tonusu & Göz pozisyonu/pupil dinamikleri,
Cerrahi uyarıya tepkiler, Uyanma periyodu & Postoperatif takip)
"""

METADATA = {
    "id": "monitorizasyon",
    "name": "7. Ders: Anestezi Hastasının Monitörizasyonu",
    "shortName": "Hasta Monitörizasyonu",
    "icon": "📊",
    "badge": "35 Slayt • Solunum, PaCO2, EKG, Kan Basıncı, CRT & Refleksler",
    "kategori": "Veteriner Cerrahi ve Anesteziyoloji",
    "alt_kategori": "Hayati Parametreler, Pulmoner & Kardiyovasküler Monitörizasyon, Refleks Takibi",
    "ozet": "Bu eğitim modülü; anestezi altındaki hastaların yaşamsal fonksiyonlarının güvenle sürdürülmesi için gerekli tüm monitörizasyon parametrelerini (solunum sayısı/derinliği, tidal volüm, atelektazi yönetimi, PaCO2 ve kan gazları, kapnografi, pulse oksimetre, kalp frekansı ve ritmi, arteriyel kan basıncı sınırları, CRT, mukoza rengi, ısı dengesi, korneal/palpebral/yutkunma refleksleri, göz küresi pozisyonu ve uyanma dönemi takibini) kapsamaktadır.",
    "kilit_noktalar": [
        "Sağlıklı anestezi hastaları en geç 3-5 dakikada bir kontrol edilmelidir; uzaktan bakarak takip asla yeterli değildir (Slayt 2, 35).",
        "Orta düzey anestezide solunum sayısı büyük hayvanlarda 6-10/dk, küçük hayvanlarda 8-20/dk'dır; küçük hayvanda <8/dk, büyükte <6/dk derin anesteziye işaret eder (Slayt 7).",
        "Anestezide tidal volüm en az %25 azalır; alveollerin kollabe olması (atelektazi) durumunda her 5 dakikada bir rezerv balonu ılımlı sıkılarak solunum desteği verilmelidir (Slayt 8, 9).",
        "Ketamin apnetik solunuma yol açar (inspirasyon sonrası, ekspirasyon öncesi uzun bekleme) (Slayt 12).",
        "PaCO2 normalde 35-45 mmHg'dir. PaCO2 < 28 mmHg hiperventilasyonu, > 45 mmHg hipoventilasyonu, > 60 mmHg şiddetli respiratuar asidoz ve hipoksiyi (ventilasyon şart!), < 20 mmHg ise serebral kan akımını bozan şiddetli solunum alkalozunu gösterir (Slayt 13).",
        "Pulse oksimetre vazokonstriksiyonda hatalı düşük ölçüm verir (Slayt 14).",
        "Kabul edilebilir minimum kalp frekansı köpeklerde 70/dk, kedilerde 100/dk'dır; normal anestezi aralığı 90-120/dk'dır (Slayt 15).",
        "Sistolik kan basıncının 80 mmHg'nin, ortalama arter basıncının (MAP) 60 mmHg'nin altına düşmesi serebral ve koroner perfüzyonu bozar; sistolik < 70-80 mmHg olduğunda CRT belirgin uzar ve idrar atımı durur (Slayt 20, 22).",
        "Hipotansiyonun en sık nedeni hipovolemidir ve kristaloid/kolloid ile tedavi edilir (Slayt 23).",
        "Sağlıklı kedi ve köpekler kan volümünün %15'ini (~13 ml/kg) dolaşım şoku olmadan tolere edebilir (Slayt 24).",
        "Anestezi uzadıkça vücut ısısı 3°C veya daha fazla düşer; hipertermi nadirdir ancak halotanla tetiklenen malign hipertermi ölümcüldür (Slayt 25).",
        "Korneal refleksin kaybolması anestezinin tehlikeli derecede derinleştiğini (Dönem III Plan 3 sonrası) gösterir (Slayt 28).",
        "Göz pozisyonu: Dönem I'de merkezde, Dönem II'de ventromedial (çeneye bakar), Dönem III cerrahi evrede tekrar merkeze döner; merkezde + midriyazis + ışıksız refleks aşırı derin/ölümcül evredir (Slayt 30, 31).",
        "Uyanma döneminde hayvan her 5 dakikada bir mukoza rengi, CRT ve solunum yönünden yakından izlenmelidir (Slayt 35)."
    ]
}

SUMMARY_SECTIONS = [
    {
        "title": "1. Anestezi Monitörizasyonunun Temel İlkeleri & Rutin Kontroller",
        "icon": "⏱️",
        "points": [
            "Monitörizasyonun Amacı: Anestezinin güvenle sürdürülmesi, hayati organ perfüzyonundaki azalmanın önlenmesi ve sorunsuz uyanmanın temin edilmesidir (Slayt 2).",
            "Takip Edilen Temel Parametreler: Solunum (sayı, derinlik, karakter), kalp frekansı, pulzasyon gücü, CRT, çene tonusu, göz pozisyonu, palpebral refleks, O2 akış hızı, IV sıvı hızı ve vücut ısısı (Slayt 2).",
            "Kontrol Sıklığı: Sağlıklı anestezi hastaları cerrahi süresince her 3-5 dakikada bir düzenli olarak kontrol edilmeli ve kayıt tutulmalıdır (Slayt 2).",
            "Derinlik, Analjezi & Kas Gevşemesi: Hayvanın yeterli derinlikte olup olmadığı kas tonusu ve reflekslerle; cerrahi uyarıya taşikardi/hareket cevabı analjezi ihtiyacıyla değerlendirilir (Slayt 3, 4)."
        ]
    },
    {
        "title": "2. Pulmoner Monitörizasyon: Solunum Sayısı, Hacmi & Kalıpları",
        "icon": "🫁",
        "points": [
            "Fizyolojik Solunum Hızları: Uyanık köpeklerde 10-30/dk, kedilerde 25-40/dk; orta düzey cerrahi anestezide küçük hayvanlarda 8-20/dk, büyük hayvanlarda 6-10/dk'dır (Slayt 7).",
            "Derin Anestezi Solunum Sınırları: Solunumun küçük hayvanlarda 8/dk, büyüklerde 6/dk altına düşmesi aşırı derin anesteziye işaret eder (Slayt 7).",
            "Tidal Volüm & Hipoventilasyon: İnterkostal kas tonusunun azalmasıyla anestezi altındaki hastaların çoğunda tidal volüm en az %25 azalır ve solunum yüzeyselleşir (Slayt 8).",
            "Özel Solunum Kalıpları: Morfin taşipne/hiperventilasyona yol açabilir; Ketamin ise inspirasyon sonrası uzun bekleme ile karakterize apnetik solunum yaptırır (Slayt 10, 12)."
        ]
    },
    {
        "title": "3. Atelektazi Yönetimi & Solunum Dinamikleri",
        "icon": "💨",
        "points": [
            "Atelektazi Mekanizması: Yüzeysel solunum nedeniyle alt alveollere hava ulaşamaz ve alveoller kollabe olur (Slayt 9).",
            "Solunum Desteği (Bagging): Anestezi cihazının rezerv balonu dikkatle ve ılımlı şekilde sıkılarak akciğerler periyodik olarak şişirilir; rutin olarak 5 dakikada bir uygulanır (Slayt 9).",
            "Mekanik Ventilasyon: Atelektaziyi önlemede ve solunum parametrelerini sabit tutmada ventilatörlü anestezi cihazı altın standarttır (Slayt 9).",
            "İnspirasyon / Ekspirasyon Oranı: Normalde inspirasyon 1-1.5 saniye, ekspirasyon ise 3-5 saniye sürer (Slayt 11)."
        ]
    },
    {
        "title": "4. Kan Gazları (PaCO2), Kapnografi & Pulse Oksimetri",
        "icon": "📈",
        "points": [
            "PaCO2 Eşik Değerleri: < 28 mmHg hiperventilasyon, > 45 mmHg hipoventilasyon göstergesidir (Slayt 13).",
            "Kritik PaCO2 Sınırları: > 60 mmHg aşırı respiratuar asidoz ve hipoksiye işaret eder (mekanik ventilasyon şarttır); < 20 mmHg şiddetli alkaloz oluşturarak serebral kan akımını azaltır (Slayt 13).",
            "Kapnograf Cihazı: Ekspirasyon gazındaki CO2 konsantrasyonunu grafiksel (kapnogram) kaydeden, solunum sayısı ve çıkarılan CO2 miktarını veren cihazdır (Slayt 14).",
            "Pulse Oksimetre & Hatalar: Arteriyel oksihemoglobin satürasyonunu noninvaziv ölçer. Şiddetli periferal vazokonstriksiyonda hatalı düşük okuyarak hastayı yalancı hipoksemik gösterebilir (Slayt 14)."
        ]
    },
    {
        "title": "5. Kardiyovasküler Sistem: Kalp Frekansı, Nabız & Perfüzyon",
        "icon": "❤️",
        "points": [
            "Kabul Edilebilir Alt Sınırlar: Anestezide minimum kalp hızı köpeklerde 70/dk, kedilerde 100/dk'dır. Normal aralık 90-120/dk'dır (Slayt 15).",
            "Bradikardi Nedenleri: Birçok anestezik miyokard ve iletim sistemini baskılar; düşük frekans aşırı derin anesteziye işaret edebilir (Slayt 15).",
            "Nabız Palpasyon Bölgeleri: Femoral, lingual, karotid ve dorsal pedal arterler. Güçsüz nabız hipovolemi veya derin anestezik hipotansiyonu gösterir (Slayt 18).",
            "Hız vs Sirkülasyon: Kalp atımının olması sirkülasyonun yeterli olduğunu tek başına kanıtlamaz; nabız dolgunluğu ve kan basıncıyla birlikte değerlendirilmelidir (Slayt 16)."
        ]
    },
    {
        "title": "6. Arteriyel Kan Basıncı, CRT & Sıvı Dengesi",
        "icon": "🩺",
        "points": [
            "Normal Basınç Değerleri: Sistolik: 100-160 mmHg, Diastolik: 60-100 mmHg, Ortalama (MAP): 80-120 mmHg olmalıdır (Slayt 22).",
            "Kritik İskemi Eşiği: Sistolik < 80 mmHg veya MAP < 60 mmHg altına düşerse serebral ve koroner perfüzyon yetersiz kalır (Slayt 22).",
            "CRT & İdrar Çıkışı: Sistolik basınç 70-80 mmHg altına indiğinde CRT belirgin uzar; böbrek perfüzyonu çöktüğü için idrar atımı durur (Slayt 20).",
            "Hipotansiyon & Kan Kaybı: En yaygın neden hipovolemidir (kristaloid/kolloid ile sağaltılır). Sağlıklı kedi-köpekler kan volümünün %15'ini (~13 ml/kg) şoksuz tolere edebilir (Slayt 23, 24)."
        ]
    },
    {
        "title": "7. Isı Regülasyonu: Hipotermi & Malign Hipertermi",
        "icon": "🌡️",
        "points": [
            "Hipotermi Nedenleri: Anestezinin uzaması vücut ısısını 3°C veya daha fazla düşürür. Soğuk antiseptik, kas tonusunun/titremenin kaybı, metabolik yavaşlama, açılan vücut boşlukları ve vazodilatasyon etkendir (Slayt 25).",
            "Malign Hipertermi Tehlikesi: Nadir fakat ölümcül bir komplikasyondur; özellikle Halotan anestezisinde tetiklenebilir ve derhal acil müdahale gerektirir (Slayt 25)."
        ]
    },
    {
        "title": "8. Refleksler, Kas Tonusu, Göz Dinamikleri & Uyanma Takibi",
        "icon": "👁️",
        "points": [
            "Palpebral & Yutkunma Refleksi: Palpebral refleks göz kantusuna dokunularak aranır; ketaminde kaybolmaz, halotanda kaybolur. Yutkunma orta düzeyde kaybolur, uyanmada geri dönünce hasta ekstübe edilir (Slayt 26, 27).",
            "Pedal & Korneal Refleks: Pulvinus sıkıştırmada bacağı çekme (pedal) anestezide kaybolur. Korneal refleksin kaybolması anestezinin tehlikeli şekilde derinleştiğini gösterir (Slayt 28).",
            "Göz Pozisyonu & Pupil: Dönem I'de merkezde, Dönem II'de çeneye bakar (ventromedial), cerrahi dönemde merkeze döner. Merkezde göz + fiks midriyazis + ışıksızlık = tehlike/ölüm sınırıdır (Slayt 30, 31).",
            "Cerrahi Uyarı Cevabı & Uyanma: Ligament/organ çekilmesinde taşikardi, hipertansiyon, lakrimasyon ağrıyı gösterir. Uyanma döneminde hasta uzaktan değil, her 5 dakikada bir yakından izlenmelidir (Slayt 33, 35)."
        ]
    }
]

BILGI_KARTLARI = [
    {
        "kart_id": "fc_mon_001",
        "on_yuz": "Sağlıklı bir anestezi hastası operasyon boyunca hangi aralıklarla kontrol edilmelidir?",
        "arka_yuz": "Sağlıklı hayvanların anestezi süresince her 3-5 dakikada bir hayati parametreleri düzenli olarak kontrol edilmeli ve kaydedilmelidir (Slayt 2).",
        "slayt_no": 2
    },
    {
        "kart_id": "fc_mon_002",
        "on_yuz": "Anestezi hastasının rutin monitörizasyonunda değerlendirilen temel fiziksel parametreler nelerdir?",
        "arka_yuz": "Solunum (sayı, derinlik, karakter), kalp frekansı, pulzasyon gücü, mukoza rengi, CRT, çene kası gevşemesi, göz pozisyonu, palpebral refleks, O2 akış hızı, IV sıvı hızı ve vücut ısısı (Slayt 2).",
        "slayt_no": 2
    },
    {
        "kart_id": "fc_mon_003",
        "on_yuz": "Genel anestezide cerrahi uyarana karşı taşikardi veya hareket oluştuğunda yaklaşım ne olmalıdır?",
        "arka_yuz": "Hasta ağrı veya yetersiz derinliktedir; cerrahiyi olumsuz etkiliyorsa anestezi derinleştirilir veya ilave analjezik (özellikle opioid) uygulanır. Cerrahiyi etkilemiyorsa anestezi gereksiz derinleştirilmemelidir (Slayt 4).",
        "slayt_no": 4
    },
    {
        "kart_id": "fc_mon_004",
        "on_yuz": "Laparotomi, torakotomi ve osteosentez operasyonlarında kas tonusunu kırmak için ne yapılmalıdır?",
        "arka_yuz": "Anestezi derinliğini toksik seviyelere artırmak yerine, spesifik kas gevşetici ilaçlar (veya benzodiazepin/alfa2 agonist ilavesi) kullanılmalıdır (Slayt 5).",
        "slayt_no": 5
    },
    {
        "kart_id": "fc_mon_005",
        "on_yuz": "Anestezi altında orta düzey cerrahi dönemde küçük ve büyük hayvanlarda normal solunum sayısı kaçtır?",
        "arka_yuz": "Küçük hayvanlarda: 8-20 soluk/dakika. Büyük hayvanlarda: 6-10 soluk/dakika (Slayt 7).",
        "slayt_no": 7
    },
    {
        "kart_id": "fc_mon_006",
        "on_yuz": "Solunum sayısının hangi kritik eşiklerin altına düşmesi tehlikeli derin anesteziye işaret eder?",
        "arka_yuz": "Küçük hayvanlarda 8/dk'nın, büyük hayvanlarda 6/dk'nın altına düşmesi derin anestezi dönemine girildiğini gösterir (Slayt 7).",
        "slayt_no": 7
    },
    {
        "kart_id": "fc_mon_007",
        "on_yuz": "Anestezi uygulanan hayvanların çoğunda tidal volüm ne oranda azalır ve sebebi nedir?",
        "arka_yuz": "Tidal volüm en az %25 azalır (hipoventilasyon). Sebebi, anesteziklerin inspirasyon sırasında interkostal kasların genişleme yeteneğini baskılamasıdır (Slayt 8).",
        "slayt_no": 8
    },
    {
        "kart_id": "fc_mon_008",
        "on_yuz": "Anestezi sırasında gelişen alveolar atelektazi nedir ve nasıl tedavi edilir?",
        "arka_yuz": "Yetersiz havalanan alveollerin parsiyel kollabe olmasıdır. Anestezi cihazının rezerv balonu dikkatlice ve ılımlı sıkılarak (her 5 dakikada bir solunum desteği / bagging verilerek) akciğerler genişletilir (Slayt 9).",
        "slayt_no": 9
    },
    {
        "kart_id": "fc_mon_009",
        "on_yuz": "Taşipne ile hiperventilasyon arasındaki fark nedir?",
        "arka_yuz": "Taşipne solunum sayısındaki artıştır (hızlı ve yüzeyseldir). Hiperventilasyon ise solunum derinliğindeki artıştır (Slayt 10).",
        "slayt_no": 10
    },
    {
        "kart_id": "fc_mon_010",
        "on_yuz": "Hangi analjezik grubunun uygulanması anestezi hastasında sıklıkla taşipneye neden olur?",
        "arka_yuz": "Morfin ve türevleri (özellikle kedilerde veya eksitasyon/termoregülasyon değişimiyle) hızlı solunuma (taşipne) yol açabilir (Slayt 10).",
        "slayt_no": 10
    },
    {
        "kart_id": "fc_mon_011",
        "on_yuz": "Ketamin anestezisinde görülen tipik solunum kalıbı nedir ve nasıl tanımlanır?",
        "arka_yuz": "Apnetik solunumdur. İnspirasyonu takiben, ekspirasyona geçmeden önce uzun bir duraklama (bekleme süresi) meydana gelir (Slayt 12).",
        "slayt_no": 12
    },
    {
        "kart_id": "fc_mon_012",
        "on_yuz": "Anestezi sırasında normal inspirasyon ve ekspirasyon süreleri ne kadardır?",
        "arka_yuz": "İnspirasyon süresi 1 - 1.5 saniye, ekspirasyon süresi ise 3 - 5 saniye arasında değişir (Slayt 11).",
        "slayt_no": 11
    },
    {
        "kart_id": "fc_mon_013",
        "on_yuz": "Parsiyel karbondioksit basıncında (PaCO2) hipoventilasyon ve hiperventilasyon sınırları nelerdir?",
        "arka_yuz": "PaCO2'nin 28 mmHg'nın altına düşmesi hiperventilasyonu; 45 mmHg'nın üzerine çıkması ise hipoventilasyonu gösterir (Slayt 13).",
        "slayt_no": 13
    },
    {
        "kart_id": "fc_mon_014",
        "on_yuz": "PaCO2 değerinin 60 mmHg'nın üzerine çıkması neyi gösterir ve klinik yaklaşım ne olmalıdır?",
        "arka_yuz": "Aşırı respiratuar asidoz ve hipoksiye işaret eder; hastaya derhal mekanik ventilasyon desteği verilmelidir (Slayt 13).",
        "slayt_no": 13
    },
    {
        "kart_id": "fc_mon_015",
        "on_yuz": "PaCO2 değerinin 20 mmHg altına inmesinin beyin üzerindeki tehlikeli etkisi nedir?",
        "arka_yuz": "Şiddetli solunum alkalozu serebral damarlarda vazokonstriksiyon yaparak serebral kan akımını azaltır ve serebral oksijenizasyonu bozar (Slayt 13).",
        "slayt_no": 13
    },
    {
        "kart_id": "fc_mon_016",
        "on_yuz": "Kapnograf cihazı klinikte hangi parametreleri gösterir?",
        "arka_yuz": "Ekspirasyon sonu CO2 konsantrasyonunu grafiksel olarak sürekli kaydeder, solunum sayısını ve her solukta atılan CO2 miktarını ölçer (Slayt 14).",
        "slayt_no": 14
    },
    {
        "kart_id": "fc_mon_017",
        "on_yuz": "Pulse oksimetre probu nerelere takılır ve hangi durumda hatalı düşük (yalancı hipoksi) ölçer?",
        "arka_yuz": "Dil, dudak, prepisyum veya kuyruğa takılır. Şiddetli periferik vazokonstriksiyon (örn. alfa-2 agonistler veya hipotermi) varlığında doku perfüzyonu azaldığı için hatalı düşük okur (Slayt 14).",
        "slayt_no": 14
    },
    {
        "kart_id": "fc_mon_018",
        "on_yuz": "Anestezide kabul edilebilir en düşük kalp frekansı köpek ve kedilerde kaçtır?",
        "arka_yuz": "Köpeklerde en düşük 70/dk, kedilerde en düşük 100/dk'dır. Normal cerrahi anestezi aralığı ise 90-120/dk'dır (Slayt 15).",
        "slayt_no": 15
    },
    {
        "kart_id": "fc_mon_019",
        "on_yuz": "Kalp atım sesinin veya EKG'de QRS kompleksinin duyulması/görülmesi yeterli dolaşımı kanıtlar mı?",
        "arka_yuz": "Hayır! Kalp frekansının varlığı sirkülasyonun yeterli olduğunu tek başına göstermez; mutlaka nabız dolgunluğu ve arteriyel kan basıncıyla birlikte değerlendirilmelidir (Slayt 16).",
        "slayt_no": 16
    },
    {
        "kart_id": "fc_mon_020",
        "on_yuz": "Köpek ve kedilerde periferal arteriyel pulzasyon en kolay hangi arterlerden palpe edilir?",
        "arka_yuz": "Femoral arter, dorsal pedal arter, lingual arter ve karotid arterden palpe edilir (Slayt 18, 19).",
        "slayt_no": 18
    },
    {
        "kart_id": "fc_mon_021",
        "on_yuz": "Hangi inhalasyon anesteziği ve preanestezikler belirgin hipotansiyon oluşturur?",
        "arka_yuz": "İnhalasyonlardan Halotan; preanesteziklerden ise periferik vazodilatasyon yapan Asepromazin ve Ksilazin belirgin hipotansiyon yapar (Slayt 17).",
        "slayt_no": 17
    },
    {
        "kart_id": "fc_mon_022",
        "on_yuz": "Kapiller Dolum Zamanının (CRT) uzaması hangi sistolik kan basıncı eşiğinde belirginleşir?",
        "arka_yuz": "Sistolik kan basıncı 70-80 mmHg'nin altına düştüğünde periferal perfüzyon bozulur ve CRT belirgin şekilde uzar (Slayt 20).",
        "slayt_no": 20
    },
    {
        "kart_id": "fc_mon_023",
        "on_yuz": "İdrar atımının yavaşlaması veya durması anestezi sırasında neyin doğrudan göstergesidir?",
        "arka_yuz": "Arteriyel kan basıncının düştüğünün ve renal perfüzyon basıncının yetersiz kaldığının en net göstergelerindendir (Slayt 20).",
        "slayt_no": 20
    },
    {
        "kart_id": "fc_mon_024",
        "on_yuz": "Hayvanlarda normal sistolik, diastolik ve ortalama kan basıncı (MAP) değerleri ne olmalıdır?",
        "arka_yuz": "Sistolik: 100-160 mmHg, Diastolik: 60-100 mmHg, Ortalama kan basıncı (MAP): 80-120 mmHg olmalıdır (Slayt 22).",
        "slayt_no": 22
    },
    {
        "kart_id": "fc_mon_025",
        "on_yuz": "Serebral ve koroner perfüzyonun bozulduğu kritik kan basıncı eşikleri nelerdir?",
        "arka_yuz": "Sistolik kan basıncının 80 mmHg'nin, ortalama kan basıncının (MAP) 60 mmHg'nin altına düşmesi hayati organ perfüzyonunu bozar (Slayt 22).",
        "slayt_no": 22
    },
    {
        "kart_id": "fc_mon_026",
        "on_yuz": "Anestezideki hipotansiyonun en önemli nedeni nedir ve nasıl tedavi edilir?",
        "arka_yuz": "En önemli neden hipovolemidir; izotonik kristalloidler (Serum Fizyolojik, Laktatlı Ringer) ve gerekirse kolloid solüsyonlarla sıvı desteği yapılarak tedavi edilir (Slayt 23).",
        "slayt_no": 23
    },
    {
        "kart_id": "fc_mon_027",
        "on_yuz": "Sağlıklı kedi ve köpekler dolaşım şoku gelişmeksizin vücut kan volümünün yüzde kaçını tolere edebilir?",
        "arka_yuz": "Kan volümünün %15'ini şok gelişmeden tolere edebilirler; bu miktar kedi ve köpeklerde yaklaşık 13 ml/kg'dır (Slayt 24).",
        "slayt_no": 24
    },
    {
        "kart_id": "fc_mon_028",
        "on_yuz": "Anestezi süresinin uzaması hastanın beden ısısını ne kadar düşürür ve temel nedenleri nelerdir?",
        "arka_yuz": "3°C veya daha fazla düşürür. Nedenleri: Soğuk antiseptik/alkol uygulaması, titremenin olmaması, metabolizmanın yavaşlaması, açık vücut boşlukları ve vazodilatasyondur (Slayt 25).",
        "slayt_no": 25
    },
    {
        "kart_id": "fc_mon_029",
        "on_yuz": "Halotan anestezisinde görülebilen ölümcül hipertermi tablosuna ne ad verilir?",
        "arka_yuz": "Malignant hipertermi (Malign Hipertermi) adı verilir; acilen önlem alınıp vücut ısısı düşürülmezse ölümle sonuçlanır (Slayt 25).",
        "slayt_no": 25
    },
    {
        "kart_id": "fc_mon_030",
        "on_yuz": "Ketamin ile Halotan anestezisinin palpebral refleks üzerindeki farkı nedir?",
        "arka_yuz": "Ketamin anestezisinde palpebral refleks ortadan kalkmaz (korunur); Halotan anestezisinde ise tamamen ortadan kalkar (Slayt 26).",
        "slayt_no": 26
    },
    {
        "kart_id": "fc_mon_031",
        "on_yuz": "Korneal refleksin yok olması ne anlama gelir?",
        "arka_yuz": "Anestezinin çok derin ve tehlikeli düzeye ulaştığını gösterir (Dönem III Plan 3'e kadar korunur, sonrasında kaybolur) (Slayt 28).",
        "slayt_no": 28
    },
    {
        "kart_id": "fc_mon_032",
        "on_yuz": "Anestezi dönemlerine göre göz küresi pozisyonu nasıl değişir?",
        "arka_yuz": "Dönem I'de merkezde; Dönem II'de ventromedial (çeneye bakar); Cerrahi dönemde (Dönem III) tekrar merkezdedir (Slayt 30).",
        "slayt_no": 30
    },
    {
        "kart_id": "fc_mon_033",
        "on_yuz": "Göz küresinin merkezde olması, midriyazis ve ışık refleksinin olmaması neyi belgeler?",
        "arka_yuz": "Anestezi derinliğinin tehlike sınırları içine (Dönem IV / solunum-dolaşım arresti öncesi) girdiğini gösterir (Slayt 31).",
        "slayt_no": 31
    },
    {
        "kart_id": "fc_mon_034",
        "on_yuz": "Cerrahi sırasında ovaryum ligamentinin çekilmesi veya organ manipülasyonunda ne tür yanıtlar oluşur?",
        "arka_yuz": "Ağrı algılanır; sempatik deşarjla kalp frekansı ve kan basıncı artar, solunum hızlanır, lakrimasyon, salivasyon ve pedal hareketler görülebilir (Slayt 33).",
        "slayt_no": 33
    },
    {
        "kart_id": "fc_mon_035",
        "on_yuz": "Uyanma dönemindeki bir hastaya uzaktan bakarak takip yapmak neden yanlıştır?",
        "arka_yuz": "Bu dönemde ölümcül bradikardi ve solunum yetmezliği gelişebilir; bunlar uzaktan gözle tespit edilemez, her 5 dakikada bir yakından mukoza, CRT ve nabız kontrol edilmelidir (Slayt 35).",
        "slayt_no": 35
    }
]

ACIK_UCLU_SORULAR = [
    {
        "soru_id": "au_mon_001",
        "soru": "Anestezi hastasının monitörizasyonunun üç temel amacını ve sağlıklı bir hastada kontrol sıklığını yazınız.",
        "ideal_cevap": "Monitörizasyonun üç temel amacı: 1) Anestezinin maksimum derecede güvenli bir şekilde sürdürülmesini sağlamak, 2) Yaşamsal organ fonksiyonlarındaki azalmayı ve hasarı minimuma indirmek, 3) Cerrahi sonrasında sorunsuz ve sağlıklı bir şekilde uyanmanın gerçekleşmesini temin etmektir. Sağlıklı anestezi hastaları operasyon süresince her 3-5 dakikada bir düzenli olarak kontrol edilmeli ve parametreleri kaydedilmelidir.",
        "degerlendirme_kriteri": "Cevapta [güvenli anestezi sürdürme, organ fonksiyonu azalmasını en aza indirme, kaliteli uyanma sağlama ve 3-5 dakikada bir kontrol] maddeleri yer almalıdır.",
        "slayt_no": 2
    },
    {
        "soru_id": "au_mon_002",
        "soru": "Anestezi altındaki bir hastada cerrahi uyarana karşı taşikardi veya hareket şekillendiğinde analjezi ve anestezi derinliği açısından nasıl bir karar verilmelidir?",
        "ideal_cevap": "Cerrahi uyarıya sempatik yanıt (kalp frekansı artışı) veya spontan hareket oluşması ağrı algılandığını gösterir. Eğer bu hareketler cerrahi müdahaleyi olumsuz etkiliyorsa anestezi derinliği artırılır veya ilave analjezik ilaçlar (özellikle opioidler) uygulanır. Ancak hayvanın hafif hareketleri cerrahi müdahaleyi olumsuz etkilemiyorsa, hastayı kardiyorespiratuvar depresyon riskine sokmamak için anestezi derinliği gereksiz yere artırılmamalıdır.",
        "degerlendirme_kriteri": "Cevapta [cerrahiyi engelliyorsa derinleştirme veya analjezik ekleme, cerrahiyi etkilemiyorsa derinliği gereksiz artırmama, opioid desteği] mantığı bulunmalıdır.",
        "slayt_no": 4
    },
    {
        "soru_id": "au_mon_003",
        "soru": "Torakotomi ve laparotomi gibi operasyonlarda kas gevşemesini sağlamak amacıyla anestezi gazını artırmak yerine ne yapılmalıdır ve nedeni nedir?",
        "ideal_cevap": "Kas tonusunu minimal düzeye indirmek için genel anestezi derinliğini artırmak yerine spesifik kas gevşetici ilaçların (veya benzodiazepin/alfa-2 agonistlerin) kullanılması gerekir. Çünkü anestezi derinliğini sadece kas gevşetmek amacıyla artırmak; miyokard depresyonu, şiddetli hipotansiyon, solunum durması ve toksik doz aşımı gibi hayati risklere yol açar.",
        "degerlendirme_kriteri": "Cevapta [anesteziyi derinleştirmek yerine kas gevşetici ilaç kullanılması, anestezi derinliğini artırmanın miyokard/solunum depresyonu riski yaratması] belirtilmelidir.",
        "slayt_no": 5
    },
    {
        "soru_id": "au_mon_004",
        "soru": "Uyanık kedi/köpek ile orta düzey cerrahi anestezideki kedi/köpeğin normal solunum sayılarını yazarak, derin anesteziye işaret eden alt sınırları belirtiniz.",
        "ideal_cevap": "Uyanık normal solunum sayısı: Köpeklerde 10-30/dk, kedilerde 25-40/dk'dır. Orta düzey cerrahi anestezide: Küçük hayvanlarda 8-20/dk, büyük hayvanlarda 6-10/dk normal kabul edilir. Solunum sayısının küçük hayvanlarda 8/dk'nın, büyük hayvanlarda ise 6/dk'nın altına düşmesi derin anestezi dönemine girildiğini gösterir.",
        "degerlendirme_kriteri": "Cevapta [köpek 10-30, kedi 25-40, anestezide küçük 8-20, büyük 6-10, derin anestezi sınırı küçük <8, büyük <6] değerleri bulunmalıdır.",
        "slayt_no": 7
    },
    {
        "soru_id": "au_mon_005",
        "soru": "Anestezide tidal volümün azalmasının (hipoventilasyon) patofizyolojik nedenini ve alveolar atelektazinin mekanizması ile sağaltımını açıklayınız.",
        "ideal_cevap": "Preanestezik ve anestezik maddeler inspirasyonda interkostal kasların genişleme yeteneğini azaltarak tidal volümün en az %25 azalmasına ve yüzeysel solunuma neden olur. Bu durumda alt alveollere yeterli hava ulaşamaz ve alveoller parsiyel olarak kollabe olur (atelektazi). Sağaltım: Anestezi cihazının rezerv balonu dikkatlice sıkılarak akciğerlere ılımlı basınçla solunum desteği verilir (her 5 dakikada bir rutin bagging). En iyi yöntem ise mekanik ventilatör kullanmaktır.",
        "degerlendirme_kriteri": "Cevapta [interkostal kas inhibisyonu, tidal volümün %25 azalması, alveollerin kollabe olması, rezerv balonunun sıkılması / bagging, mekanik ventilasyon] yer almalıdır.",
        "slayt_no": 9
    },
    {
        "soru_id": "au_mon_006",
        "soru": "Ketamin anestezisinde görülen 'apnetik solunum' paterninin özelliklerini açıklayınız.",
        "ideal_cevap": "Apnetik solunum; dissosiyatif anestezik olan ketamin uygulaması sonrasında gelişen özel bir solunum tipidir. Bu paternde hayvan derin bir inspirasyon yapar, inspirasyonu takiben soluğunu tutar ve ekspirasyon öncesinde belirgin, uzun bir duraklama (bekleme süresi) meydana gelir, ardından ekspirasyon gerçekleşir.",
        "degerlendirme_kriteri": "Cevapta [ketamin kaynaklı olması, inspirasyonu takiben ekspirasyon öncesi uzun bekleme/duraklama süresi] yer almalıdır.",
        "slayt_no": 12
    },
    {
        "soru_id": "au_mon_007",
        "soru": "Arteriyel PaCO2 değerinin 28, 45, 60 ve 20 mmHg olduğu durumlarda hastanın solunumsal durumunu ve organ etkilerini açıklayınız.",
        "ideal_cevap": "1) PaCO2 < 28 mmHg: Hiperventilasyonu gösterir. 2) PaCO2 > 45 mmHg: Hipoventilasyonu gösterir. 3) PaCO2 > 60 mmHg: Aşırı respiratuar asidoz ve hipoksiye işaret eder; hastaya acil mekanik ventilasyon verilmelidir. 4) PaCO2 < 20 mmHg: Şiddetli solunum alkalozunu gösterir; serebral damarlarda daralma oluşturarak serebral kan akımını azaltır ve beyin oksijenizasyonunu bozar.",
        "degerlendirme_kriteri": "Cevapta [<28 hiperventilasyon, >45 hipoventilasyon, >60 aşırı asidoz/hipoksi/mekanik ventilasyon, <20 alkaloz ve serebral kan akımı azalması] maddeleri eksiksiz yer almalıdır.",
        "slayt_no": 13
    },
    {
        "soru_id": "au_mon_008",
        "soru": "Pulse oksimetrenin çalışma prensibini yazarak, hangi klinik durumda hatalı düşük değer ölçebileceğini açıklayınız.",
        "ideal_cevap": "Pulse oksimetre; arteriyel kandaki oksijenle doymuş (sature) hemoglobin yüzdesini (SpO2) ve nabız frekansını probu (dil, dudak, kuyruk) aracılığıyla noninvaziv yöntemle sürekli ölçer. Yeterince doğru ölçüm yapamamasının en önemli nedeni periferal vazokonstriksiyondur (örn. alfa-2 agonistler veya hipotermi). Bu durumda probun altındaki doku perfüzyonu azaldığı için sinyal zayıflar, cihaz düşük değer okur ve hasta aslında hipoksemik olmadığı halde yalancı hipoksi tanısı konur.",
        "degerlendirme_kriteri": "Cevapta [oksihemoglobin satürasyonu ölçümü, prob yerleşimi, periferal vazokonstriksiyonun hatalı düşük ölçüm nedeni olması] yer almalıdır.",
        "slayt_no": 14
    },
    {
        "soru_id": "au_mon_009",
        "soru": "Anestezi altındaki kedi ve köpeklerde kabul edilebilir en düşük kalp frekanslarını ve normal anestezi aralığını yazınız.",
        "ideal_cevap": "Anestezi hastalarında kabul edilebilir en düşük kalp frekansı: Köpeklerde 70 atım/dakika, kedilerde 100 atım/dakikadır. Anestezi sırasında kalp frekansının dakikada 90-120 arasında olması normal kabul edilir. Bu sınırların altına inmesi miyokardiyal depresyon veya derin anestezi dönemine işaret eder.",
        "degerlendirme_kriteri": "Cevapta [köpek minimum 70/dk, kedi minimum 100/dk, normal aralık 90-120/dk, düşük değerin derin anesteziyi göstermesi] yer almalıdır.",
        "slayt_no": 15
    },
    {
        "soru_id": "au_mon_010",
        "soru": "Kalp seslerinin stetoskopla duyulması veya EKG ritminin varlığı tek başına dolaşımın yeterli olduğunu neden kanıtlamaz?",
        "ideal_cevap": "Çünkü EKG sadece kalbin elektriksel aktivitesini, stetoskop ise kapak seslerini yansıtır; kalbin her elektriksel veya mekanik vurusu dokuları perfüze edecek güçte bir atım hacmi (strok volüm) oluşturamayabilir. Yeterli bir dolaşımın varlığından emin olmak için kalp frekansı mutlaka arteriyel nabız kalitesi (dolgunluğu), kapiller dolum zamanı (CRT) ve arteriyel kan basıncı ölçümleri ile birlikte değerlendirilmelidir.",
        "degerlendirme_kriteri": "Cevapta [elektriksel aktivitenin mekanik debiyi garanti etmemesi, nabız dolgunluğu, CRT ve kan basıncı ile birlikte değerlendirilme zorunluluğu] bulunmalıdır.",
        "slayt_no": 16
    },
    {
        "soru_id": "au_mon_011",
        "soru": "Küçük hayvanlarda direkt ve indirekt kan basıncı ölçüm yöntemlerini ve kullanılan damarları karşılaştırınız.",
        "ideal_cevap": "Direkt yöntem: a. femoralis veya dorsal pedal artere kateter yerleştirilerek doğrudan basınç dönüştürücüye bağlanır; en doğru ortalama arter basıncını (MAP) verir. İndirekt yöntem: Ekstremiteye manşon takılarak sfigmomanometre (Doppler veya osilometrik) kullanılır; ilk pulzasyon sesi sistolik, sesin kaybolduğu nokta diastolik basınç olarak kaydedilir.",
        "degerlendirme_kriteri": "Cevapta [direkt yöntemde femoral/dorsal pedal kateteri ve MAP, indirektte sfigmomanometre, ilk pulzasyon sistolik, sönme diastolik] yer almalıdır.",
        "slayt_no": 21
    },
    {
        "soru_id": "au_mon_012",
        "soru": "Hayvanlarda normal sistolik, diastolik ve ortalama kan basıncı (MAP) değerleri ile kritik iskemi sınırlarını yazınız.",
        "ideal_cevap": "Normal değerler: Sistolik: 100-160 mmHg, Diastolik: 60-100 mmHg, Ortalama kan basıncı (MAP): 80-120 mmHg olmalıdır. Kritik iskemi sınırları: Sistolik kan basıncının 80 mmHg'nin, ortalama kan basıncının (MAP) 60 mmHg'nin altına düşmesi beyin (serebral) ve kalp (koroner) perfüzyonunun yetersiz kalmasına ve iskemik hasara yol açar.",
        "degerlendirme_kriteri": "Cevapta [Sistolik 100-160, Diastolik 60-100, MAP 80-120; kritik eşikler: Sistolik <80 ve MAP <60 mmHg] bulunmalıdır.",
        "slayt_no": 22
    },
    {
        "soru_id": "au_mon_013",
        "soru": "Anestezi sırasında CRT uzaması ve idrar atımının durması hangi patofizyolojik durumun göstergesidir?",
        "ideal_cevap": "Hastanın sistolik kan basıncının 70-80 mmHg'nin altına düştüğünün ve belirgin hipotansiyon/hipovolemi geliştiğinin göstergesidir. Kan basıncı bu kritik seviyenin altına indiğinde periferal kılcal damar yatağı çöker ve CRT uzar; aynı zamanda böbrek glomerül filtrasyon basıncı yetersiz kaldığı için idrar atımı belirgin yavaşlar veya tamamen durur.",
        "degerlendirme_kriteri": "Cevapta [sistolik basıncın 70-80 mmHg altına düşmesi, periferik perfüzyon bozulması, renal filtrasyon basıncının çökmesi] yer almalıdır.",
        "slayt_no": 20
    },
    {
        "soru_id": "au_mon_014",
        "soru": "Sağlıklı kedi ve köpeklerin dolaşım şoku gelişmeden tolere edebileceği kan kaybı oranını ve miktarını yazınız.",
        "ideal_cevap": "Sağlıklı hayvanlar toplam kan hacimlerinin %15'ini sirkülasyon şoku gelişmeksizin kompanse edip tolere edebilirler. Bu tolere edilebilir miktar kedi ve köpeklerde vücut ağırlığı başına yaklaşık 13 ml/kg'dır.",
        "degerlendirme_kriteri": "Cevapta [kan volümünün %15'i ve yaklaşık 13 ml/kg değeri] yer almalıdır.",
        "slayt_no": 24
    },
    {
        "soru_id": "au_mon_015",
        "soru": "Anestezi sırasında hastanın vücut ısısının 3°C veya daha fazla düşmesine (hipotermi) katkıda bulunan 5 temel nedeni yazınız.",
        "ideal_cevap": "1) Operasyon öncesinde operasyon bölgesinin soğuk antiseptik ve alkolle yıkanması, 2) Anestezi sırasında titreme ve kas aktivitesi oluşmamasına bağlı ısı üretilememesi, 3) Anestezi döneminde metabolizmanın yavaşlaması, 4) Operasyon sırasında vücut boşluklarının (karın, göğüs) açılmasına bağlı doğrudan ısı kaybı, 5) Birçok preanestezik ve anestezik ilacın periferik vazodilatasyon oluşturarak radyasyonla ısı kaybını artırması.",
        "degerlendirme_kriteri": "Cevapta [soğuk antiseptik, titreme/kas aktivitesi yokluğu, metabolizma yavaşlaması, vücut boşluklarının açılması, vazodilatasyon] 5 madde yer almalıdır.",
        "slayt_no": 25
    },
    {
        "soru_id": "au_mon_016",
        "soru": "Malignant hiperterminin tanımını, hangi anestezikle ilişkili olduğunu ve klinik önemini açıklayınız.",
        "ideal_cevap": "Malignant hipertermi; özellikle Halotan anestezisi uygulanan genetik duyarlı hayvanlarda iskelet kaslarında aşırı kalsiyum salınımı ile kontrolsüz ısı artışına yol açan nadir fakat ölümcül bir komplikasyondur. Vücut ısısı hızla kritik seviyeleri aşar; derhal anestezi kesilip agresif soğutma ve tedavi uygulanmazsa hızla ölümle sonuçlanır.",
        "degerlendirme_kriteri": "Cevapta [Halotan ilişkisi, kontrolsüz hızlı ısı artışı, acil tedavi edilmezse ölümcül olması] yer almalıdır.",
        "slayt_no": 25
    },
    {
        "soru_id": "au_mon_017",
        "soru": "Palpebral refleks ile korneal refleksin kontrol yöntemlerini ve anestezi derinliği açısından klinik farklarını açıklayınız.",
        "ideal_cevap": "Palpebral refleks: Gözün medial veya lateral açısına dokunularak aranır; I. ve II. dönemde pozitiftir, cerrahi dönemde kaybolur (ketaminde kaybolmaz, halotanda kaybolur), geri dönmesi uyanmayı gösterir. Korneal refleks ise doğrudan korneaya dokunularak bakılır; anestezinin 3. döneminin 3. planına kadar mevcuttur. Korneal refleksin kaybolması anestezinin hayati tehlike yaratacak düzeyde aşırı derinleştiğini belgeler.",
        "degerlendirme_kriteri": "Cevapta [palpebral için kantusa dokunma ve ketamin/halotan farkı, korneal için korneaya dokunma ve kaybolmasının tehlikeli derin anestezi olması] bulunmalıdır.",
        "slayt_no": 26
    },
    {
        "soru_id": "au_mon_018",
        "soru": "Anestezi dönemlerine göre göz küresi pozisyonunu ve tehlikeli anestezi evresindeki göz-pupil tablosunu açıklayınız.",
        "ideal_cevap": "Dönem I: Göz merkezdedir. Dönem II: Göz ventromedial pozisyondadır (hayvan çenesine bakar gibidir). Dönem III (Cerrahi dönem): Göz tekrar merkezi pozisyonuna geri döner. Tehlikeli aşırı derin anestezi evresinde ise; göz küresi merkezdedir, pupillalar tamamen dilate (fiks midriyazis) haldedir ve ışığa karşı hiçbir pupiller refleks cevabı yoktur.",
        "degerlendirme_kriteri": "Cevapta [Dönem I merkezde, Dönem II çeneye bakar, Dönem III merkezde; tehlike sınırı: merkezde göz + fiks midriyazis + ışıksızlık] yer almalıdır.",
        "slayt_no": 30
    },
    {
        "soru_id": "au_mon_019",
        "soru": "Cerrahi sırasında ovaryum ligamentinin çekilmesi gibi visceral ağrılı uyarılarda hastada ortaya çıkan otonom ve motor belirtileri yazınız.",
        "ideal_cevap": "Visceral ağrı ve sempatik uyarım algılandığında: Kalp frekansı (taşikardi) ve kan basıncı aniden yükselir, solunum sayısı artar (taşipne), lakrimasyon (gözyaşı akışı), salivasyon (tükürük artışı) ve pedal hareketler (bacakları çekme) meydana gelir. Bu bulgular anestezinin cerrahi için yetersiz olduğunu belgeler.",
        "degerlendirme_kriteri": "Cevapta [taşikardi, hipertansiyon, taşipne, lakrimasyon, salivasyon, pedal hareketler] semptomları yer almalıdır.",
        "slayt_no": 33
    },
    {
        "soru_id": "au_mon_020",
        "soru": "Uyanma döneminde hastanın uzaktan izlenmesinin neden kesinlikle yanlış olduğunu ve yapılması gereken kontrol protokolünü açıklayınız.",
        "ideal_cevap": "Uyanma dönemi mortalitenin en yüksek olduğu kritik dönemlerden biridir; bu dönemde akut bradikardi, aritmiler ve solunum yolu obstrüksiyonuna bağlı solunum yetmezliği gelişebilir ve bunlar uzaktan bakarak asla fark edilemez. Protokol: Hayvan uyanana kadar her 5 dakikada bir yakından kontrol edilmeli; stetoskopla kalp ve akciğer sesleri dinlenmeli, mukoza rengi, CRT, nabız kalitesi ve yutkunma refleksi muayene edilerek ekstübasyon güvenle yapılmalıdır.",
        "degerlendirme_kriteri": "Cevapta [bradikardi ve solunum yetmezliğinin uzaktan fark edilememesi, her 5 dakikada bir mukoza/CRT/solunum/stetoskop muayenesi] yer almalıdır.",
        "slayt_no": 35
    }
]

COKTAN_SECMELI_SORULAR = [
    {
        "soru_id": "mcq_mon_001",
        "soru_metni": "Anestezi hastasının rutin monitörizasyonunda, stabil ve sağlıklı hayvanların hayati parametreleri cerrahi boyunca en geç hangi zaman aralığında kontrol edilmelidir?",
        "secenekler": {
            "A": "Her 30 saniyede bir",
            "B": "3 - 5 dakikada bir",
            "C": "15 - 20 dakikada bir",
            "D": "30 dakikada bir",
            "E": "Sadece operasyon başında ve sonunda"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Slayt 2'de açıkça belirtildiği üzere, sağlıklı anestezi hastalarının operasyon boyunca her 3-5 dakikada bir düzenli olarak kontrol edilmesi gerekmektedir.",
            "celdirici_analizi": "15-20 veya 30 dakika gibi uzun aralıklar akut gelişen hipotansiyon, hipoventilasyon veya kardiyak arresti fark etmek için çok geçtir."
        },
        "slayt_no": 2
    },
    {
        "soru_id": "mcq_mon_002",
        "soru_metni": "Aşağıdakilerden hangisi anestezi sırasında solunum fonksiyonunun izlenmesinde solunum sayısını ve ritmini belirlemek için doğrudan kullanılan fiziksel yöntemlerden biridir?",
        "secenekler": {
            "A": "Sadece dil mukozasının rengine bakmak",
            "B": "Anestezi cihazının rezerv balonunun veya göğüs kafesinin hareketlerini izlemek",
            "C": "Sadece idrar torbasının doluluğunu ölçmek",
            "D": "Vücut ısısını rektal prob ile takip etmek",
            "E": "Kapiller dolum zamanını (CRT) kontrol etmek"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Solunum sayısı ve karakteri; göğüs kafesinin ekspansiyon hareketleri veya anestezi devresindeki rezerv balonunun inip kalkması izlenerek tayin edilir (Slayt 2).",
            "celdirici_analizi": "CRT, mukoza rengi veya idrar dolaşım göstergeleridir; solunum frekansını göstermez."
        },
        "slayt_no": 2
    },
    {
        "soru_id": "mcq_mon_003",
        "soru_metni": "Anestezi derinliğinin tespit edilmesinde klinisyenin değerlendirdiği en temel iki klinik parametre aşağıdakilerden hangisidir?",
        "secenekler": {
            "A": "Vücut ağırlığı ve deri elastikiyeti",
            "B": "Kas tonusundaki azalma ve refleksler",
            "C": "Kan glikoz düzeyi ve hematokrit değeri",
            "D": "Tüy dökülmesi ve idrar rengi",
            "E": "Ortam sıcaklığı ve nem oranı"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Anestezi derinliğinin belirlenmesinde özellikle iskelet kası tonusundaki azalma (örneğin çene tonusu) ve koruyucu refleksler (palpebral, pedal, korneal) dikkate alınır (Slayt 3).",
            "celdirici_analizi": "Laboratuvar parametreleri derinlik kontrolünde anlık bilgi vermez."
        },
        "slayt_no": 3
    },
    {
        "soru_id": "mcq_mon_004",
        "soru_metni": "Genel anestezi altındaki bir hastada daha iyi düzeyde kas gevşemesi temin etmek amacıyla anesteziklere ilave olarak hangilerinin kullanılması önerilir?",
        "secenekler": {
            "A": "Yalnızca sempatomimetik ajanlar",
            "B": "Benzodiazepinler, fenotiyazin türevleri veya alfa-2 agonistler",
            "C": "Sadece lokal vazokonstriktörler",
            "D": "Solunum stimülanları (Doksapram)",
            "E": "Antikolinesteraz inhibitörleri"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Daha iyi düzeyde kas gevşemesi ve dengeli anestezi için benzodiazepinler (diazepam, midazolam), fenotiyazinler (asepromazin) veya alfa-2 agonistler (ksilazin, medetomidin) genel anesteziklerle kombine edilir (Slayt 3).",
            "celdirici_analizi": "Doksapram solunum stimülanıdır; sempatomimetikler kas gevşetmez."
        },
        "slayt_no": 3
    },
    {
        "soru_id": "mcq_mon_005",
        "soru_metni": "Yüzeysel anestezi altındaki bir hayvanda cerrahi uyarıya bağlı refleks veya spontan hareketlerin görülmesiyle ilgili klinik gerçek aşağıdakilerden hangisidir?",
        "secenekler": {
            "A": "Hayvanın kesinlikle uyanık olduğunu ve cerrahiyi net olarak hatırlayacağını gösterir",
            "B": "Bu hareketlerin varlığı, hayvanın ağrıyı bilinçli olarak algıladığı anlamına gelmez",
            "C": "Derhal anestezi gazının maksimuma getirilmesini gerektiren acil bir krizdir",
            "D": "Kalbin durmak üzere olduğunun ilk belirtisidir",
            "E": "Spontan hareket sadece genel anestezi ölümle sonuçlandığında oluşur"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Slayt 4'te belirtildiği üzere, yüzeysel anestezide refleks ya da spontan hareketler meydana gelebilir ancak bu ağrıyı bilinçli olarak algıladığı anlamına gelmez.",
            "celdirici_analizi": "Subkortikal ve spinal refleksler bilinçli kortikal algı olmaksızın da tetiklenebilir."
        },
        "slayt_no": 4
    },
    {
        "soru_id": "mcq_mon_006",
        "soru_metni": "Anestezi sırasında cerrahi müdahale taşikardi gibi sempatik uyarılara yol açıyor ancak hayvanın hafif hareketleri cerrahiyi olumsuz etkilemiyorsa doğru klinik yaklaşım hangisidir?",
        "secenekler": {
            "A": "Anestezi derinliği artırılmamalı, gerekiyorsa analjezik eklenmelidir",
            "B": "Hasta hemen uyandırılmalıdır",
            "C": "Vaporizatör konsantrasyonu derhal üç katına çıkarılmalıdır",
            "D": "Tüm sıvılar kesilmelidir",
            "E": "Hasta entübe ise derhal ekstübe edilmelidir"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Hayvanın hareketleri cerrahi müdahaleyi olumsuz etkilemiyor ise anestezi derinliği gereksiz artırılmamalıdır; ağrı komponenti varsa ilave analjezik uygulanmalıdır (Slayt 4).",
            "celdirici_analizi": "Gereksiz derinleştirme hipotansiyon ve solunum depresyonunu artırır."
        },
        "slayt_no": 4
    },
    {
        "soru_id": "mcq_mon_007",
        "soru_metni": "Torakotomi, laparotomi veya uzun sürecek osteosentez operasyonlarında kas tonusunu minimal düzeye indirmek için en rasyonel yaklaşım nedir?",
        "secenekler": {
            "A": "Anestezi derinliğini tehlikeli boyutlara kadar artırmak",
            "B": "Anestezi derinliğini artırmak yerine spesifik kas gevşetici ilaçları kullanmak",
            "C": "Hastaya yüksek doz adrenalin enjekte etmek",
            "D": "Sadece oksijen akışını kesmek",
            "E": "Vücut ısısını kasıtlı olarak 30°C'ye düşürmek"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Bu tür operasyonlarda sadece kas gevşetmek için anestezi derinliğini artırmak kardiyotoksiktir; bunun yerine kas gevşetici ilaçların kullanılması esastır (Slayt 5).",
            "celdirici_analizi": "Anesteziyi aşırı derinleştirmek kardiyovasküler kollapsa yol açar."
        },
        "slayt_no": 5
    },
    {
        "soru_id": "mcq_mon_008",
        "soru_metni": "Orta düzey cerrahi anestezi döneminde küçük hayvanlarda (kedi/köpek) ve büyük hayvanlarda normal solunum sayısı aralıkları sırasıyla hangisinde doğru verilmiştir?",
        "secenekler": {
            "A": "Küçük: 25-40/dk | Büyük: 15-25/dk",
            "B": "Küçük: 8-20/dk | Büyük: 6-10/dk",
            "C": "Küçük: 2-4/dk | Büyük: 1-2/dk",
            "D": "Küçük: 40-60/dk | Büyük: 20-30/dk",
            "E": "Küçük: 1-5/dk | Büyük: 10-15/dk"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Orta düzey anestezi döneminde solunum sayısı büyük hayvanlarda 6-10/dk, küçük hayvanlarda ise 8-20/dk arasında olması normaldir (Slayt 7).",
            "celdirici_analizi": "25-40 uyanık kedilerin solunum hızıdır; anestezide 8-20/dk normaldir."
        },
        "slayt_no": 7
    },
    {
        "soru_id": "mcq_mon_009",
        "soru_metni": "Anestezi altındaki bir kedi veya köpekte solunum sayısının dakikada kaçın altına düşmesi derin anestezi dönemine girildiğini gösterir?",
        "secenekler": {
            "A": "8/dk",
            "B": "15/dk",
            "C": "20/dk",
            "D": "25/dk",
            "E": "30/dk"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Anestezi döneminde solunum sayısının küçük hayvanlarda 8/dk'nın (büyüklerde 6/dk'nın) altına düşmesi derin anesteziye girildiğini gösterir (Slayt 7).",
            "celdirici_analizi": "8'in altı hipoventilasyon ve PaCO2 retansiyonu ile arrest riskidir."
        },
        "slayt_no": 7
    },
    {
        "soru_id": "mcq_mon_010",
        "soru_metni": "Anestezi uygulanan hayvanların çoğunda tidal volümün en az %25 azalmasının temel patofizyolojik sebebi nedir?",
        "secenekler": {
            "A": "Mide içeriğinin bronşları tamamen tıkaması",
            "B": "Preanestezik ve anestezik maddelerin inspirasyon sırasında interkostal kasların genişleme yeteneğini azaltması",
            "C": "Kalp atımının durması",
            "D": "Kan basıncının aniden 200 mmHg üzerine çıkması",
            "E": "Hastanın hiperaktif olması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Birçok anestezik ve preanestezik madde interkostal kasların genişleme yeteneğini baskılayarak solunumu yüzeyselleştirir ve tidal volümü en az %25 azaltır (Slayt 8).",
            "celdirici_analizi": "Bu durum anesteziye bağlı hipoventilasyonun klasik fizyolojisidir."
        },
        "slayt_no": 8
    },
    {
        "soru_id": "mcq_mon_011",
        "soru_metni": "Anestezi sırasında yüzeysel solunum nedeniyle alt alveollere yeterli hava ulaşamaması ve alveollerin parsiyel kollabe olması tablosuna ne ad verilir?",
        "secenekler": {
            "A": "Pnömotoraks",
            "B": "Atelektazi",
            "C": "Amfizem",
            "D": "Plörizist",
            "E": "Laringospazm"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Akciğerlerdeki bazı alveollere yeteri kadar hava ulaşamaması ve bu alveollerin parsiyel olarak kollabe olması 'atelektazi' olarak adlandırılır (Slayt 9).",
            "celdirici_analizi": "Pnömotoraks göğüs boşluğunda serbest hava olmasıdır; atelektazi alveol kollapsıdır."
        },
        "slayt_no": 9
    },
    {
        "soru_id": "mcq_mon_012",
        "soru_metni": "İnhalasyon anestezisinde atelektaziyi önlemek amacıyla klinisyenin anestezi cihazının rezerv balonunu periyodik olarak dikkatlice sıkması işlemine ne ad verilir ve rutin aralığı nedir?",
        "secenekler": {
            "A": "Defibrilasyon - Her saat başı",
            "B": "Solunum desteği (Bagging) - Her 5 dakikada bir",
            "C": "Vakumlama - Her 30 dakikada bir",
            "D": "Hiperventilasyon şoku - Günde bir kez",
            "E": "Ekstübasyon - Her 10 dakikada bir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Rezerv balonu sıkılarak akciğerlerin ılımlı şişirilmesi (solunum desteği) rutin olarak her 5 dakikada bir uygulanarak atelektazi önlenir (Slayt 9).",
            "celdirici_analizi": "Aşırı basınç uygulamadan göğüs kafesi izlenerek ılımlı yapılmalıdır."
        },
        "slayt_no": 9
    },
    {
        "soru_id": "mcq_mon_013",
        "soru_metni": "Solunum sayısındaki artışa __________, solunum derinliğindeki artışa ise __________ denir. Boşluklara sırasıyla hangisi gelmelidir?",
        "secenekler": {
            "A": "Bradipne - Hipoventilasyon",
            "B": "Taşipne - Hiperventilasyon",
            "C": "Apne - Dispne",
            "D": "Taşikardi - Hipertansiyon",
            "E": "Siyanoz - Asidoz"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Solunum sayısındaki artış taşipne, solunum derinliğindeki artış ise hiperventilasyon olarak adlandırılır (Slayt 10).",
            "celdirici_analizi": "Bradipne solunum yavaşlaması, taşikardi kalp hızı artışıdır."
        },
        "slayt_no": 10
    },
    {
        "soru_id": "mcq_mon_014",
        "soru_metni": "Aşağıdaki ilaçlardan hangisi uygulandığında anestezi hastalarında sıklıkla hızlı fakat yüzeysel solunum (taşipne) gelişir?",
        "secenekler": {
            "A": "Morfin ve türevleri",
            "B": "Atropin",
            "C": "Tiyopental sodyum",
            "D": "Propofol",
            "E": "Lidokain"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Morfin ve türevleri uygulanan hayvanlarda bu tür hızlı ve yüzeysel solunum sıklıkla oluşur (Slayt 10).",
            "celdirici_analizi": "Tiyopental ve propofol solunumu hızlandırmaz, aksine belirgin deprese eder veya apne yapar."
        },
        "slayt_no": 10
    },
    {
        "soru_id": "mcq_mon_015",
        "soru_metni": "Anestezi altındaki bir hastada normal inspirasyon ve ekspirasyon süreleri yaklaşık ne kadardır?",
        "secenekler": {
            "A": "İnspirasyon: 5 sn | Ekspirasyon: 1 sn",
            "B": "İnspirasyon: 1-1.5 sn | Ekspirasyon: 3-5 sn",
            "C": "İnspirasyon: 10 sn | Ekspirasyon: 10 sn",
            "D": "İnspirasyon: 0.1 sn | Ekspirasyon: 0.2 sn",
            "E": "Her ikisi de tam olarak 2'şer saniyedir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Normalde inspirasyon süresi 1-1.5 saniye, ekspirasyon süresi ise 3-5 saniye arasında değişir (Slayt 11).",
            "celdirici_analizi": "Ekspirasyon pasif bir süreç olduğu için fizyolojik olarak inspirasyondan 2-3 kat daha uzundur."
        },
        "slayt_no": 11
    },
    {
        "soru_id": "mcq_mon_016",
        "soru_metni": "İnspirasyonu takiben ekspirasyon öncesinde uzun bir bekleme (duraklama) süresi ile karakterize 'apnetik solunum' hangi anestezik maddenin tipik etkisidir?",
        "secenekler": {
            "A": "Ketamin",
            "B": "Halotan",
            "C": "İzofluran",
            "D": "Eter",
            "E": "Sevofluran"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Ketamin ile anesteziye alınan hayvanlarda apnetik solunum oluşur; inspirasyon sonrasında ekspirasyon öncesi uzun bir bekleme süresi meydana gelir (Slayt 12).",
            "celdirici_analizi": "Ketamin dissosiyatif anesteziğe özgü apnetik solunum kalıbı yaratır."
        },
        "slayt_no": 12
    },
    {
        "soru_id": "mcq_mon_017",
        "soru_metni": "Arteriyel kanda ölçülen parsiyel CO2 basıncının (PaCO2) 45 mmHg'nın üzerine çıkması aşağıdakilerden hangisini belgeler?",
        "secenekler": {
            "A": "Aşırı hiperventilasyonu",
            "B": "Hipoventilasyonu",
            "C": "Solunum alkalozunu",
            "D": "Oksijen toksisitesini",
            "E": "Hastanın tamamen uyandığını"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "PaCO2'nin 45 mmHg'dan yukarı çıkması hastanın yeterli gaz değişimi yapamadığını, yani hipoventilasyonu gösterir (Slayt 13).",
            "celdirici_analizi": "PaCO2'nin 28 mmHg altına düşmesi hiperventilasyondur."
        },
        "slayt_no": 13
    },
    {
        "soru_id": "mcq_mon_018",
        "soru_metni": "PaCO2 değerinin 60 mmHg'dan daha yukarı çıkması halinde klinisyenin derhal başlatması gereken hayati müdahale hangisidir?",
        "secenekler": {
            "A": "Mekanik ventilasyon desteği vermek",
            "B": "Oksijen akışını tamamen kesmek",
            "C": "Hastaya yüksek doz potasyum enjekte etmek",
            "D": "Entübasyon tüpünü hemen çekmek",
            "E": "Anestezi gaz dozunu artırmak"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "PaCO2'nin 60 mmHg'dan daha da yukarı çıkması aşırı respiratuar asidoz ve hipoksi oluştuğuna işaret eder; bu hastalara derhal mekanik ventilasyon desteği verilmelidir (Slayt 13).",
            "celdirici_analizi": "Solunum asidozunu düzeltmenin tek yolu ventilasyon ile CO2'yi dışarı atmaktır."
        },
        "slayt_no": 13
    },
    {
        "soru_id": "mcq_mon_019",
        "soru_metni": "PaCO2 değerinin 20 mmHg'nin altına düşmesi şiddetli solunum alkalozu yaratır. Bu durumun beyin üzerindeki en tehlikeli klinik sonucu nedir?",
        "secenekler": {
            "A": "Serebral damarlarda aşırı genişleme ve beyin kanaması",
            "B": "Serebral kan akımında azalma meydana gelmesi ve serebral oksijenizasyonun bozulması",
            "C": "Kafatası kemiklerinin erimesi",
            "D": "Göz içi basıncının sıfıra inmesi",
            "E": "Beyin omurilik sıvısının tamamen kuruması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "PaCO2'nin 20 mmHg altına düşmesi serebral damarlarda vazokonstriksiyona neden olur; serebral kan akımı azalır ve beyin dokusunun oksijenizasyonu bozulur (Slayt 13).",
            "celdirici_analizi": "Hipokapni serebral iskemiye yol açabilir."
        },
        "slayt_no": 13
    },
    {
        "soru_id": "mcq_mon_020",
        "soru_metni": "Solunum sırasında ekspirasyon gazlarındaki CO2 konsantrasyonunu grafiksel olarak sürekli kaydeden ve solunum sayısı ile atılan CO2 miktarını veren cihaz hangisidir?",
        "secenekler": {
            "A": "Sfigmomanometre",
            "B": "Kapnograf",
            "C": "Özefageal stetoskop",
            "D": "Refraktometre",
            "E": "Glukometre"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Kapnograf; ekspirasyon gazlarındaki CO2 miktarını grafiksel kaydeden cihazdır (Slayt 14).",
            "celdirici_analizi": "Sfigmomanometre kan basıncı, refraktometre idrar/protein dansitesi ölçer."
        },
        "slayt_no": 14
    },
    {
        "soru_id": "mcq_mon_021",
        "soru_metni": "Pulse oksimetre probu hastanın dili veya dudağına takıldığında ölçümün yetersiz ve hatalı düşük çıkmasının en önemli nedeni nedir?",
        "secenekler": {
            "A": "Periferal vazodilatasyon",
            "B": "Periferal vazokonstriksiyon",
            "C": "Hipertansiyon",
            "D": "Aşırı yüksek hemoglobin konsantrasyonu",
            "E": "Ortamın karanlık olması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Pulse oksimetrenin yeterince doğru ölçüm yapamamasının en önemli nedeni periferal vazokonstriksiyondur; doku kanlanması azaldığı için cihaz düşük değer okur ve hasta yalancı hipoksemik değerlendirilir (Slayt 14).",
            "celdirici_analizi": "Vazokonstriksiyonda pulsatif arteriyel akım dalgası algılanamaz."
        },
        "slayt_no": 14
    },
    {
        "soru_id": "mcq_mon_022",
        "soru_metni": "Anestezi hastalarında kabul edilebilir en düşük kalp frekansı köpeklerde ve kedilerde sırasıyla kaçtır?",
        "secenekler": {
            "A": "Köpek: 40/dk | Kedi: 60/dk",
            "B": "Köpek: 70/dk | Kedi: 100/dk",
            "C": "Köpek: 120/dk | Kedi: 180/dk",
            "D": "Köpek: 90/dk | Kedi: 90/dk",
            "E": "Köpek: 30/dk | Kedi: 50/dk"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Anestezi hastalarında kabul edilebilir en düşük kalp frekansı köpeklerde 70/dk, kedilerde 100/dk'dır (Slayt 15).",
            "celdirici_analizi": "Bu değerlerin altına inmesi kardiyak debiyi tehlikeli şekilde düşürür."
        },
        "slayt_no": 15
    },
    {
        "soru_id": "mcq_mon_023",
        "soru_metni": "Anestezi sırasında stabil bir cerrahi dönemde kalp frekansının dakikada kaç arasında olması normal kabul edilir?",
        "secenekler": {
            "A": "30 - 50/dk",
            "B": "60 - 80/dk",
            "C": "90 - 120/dk",
            "D": "160 - 200/dk",
            "E": "200 - 250/dk"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "Anestezi sırasında kalp frekansının dakikada 90-120 arasında olması normal kabul edilir (Slayt 15).",
            "celdirici_analizi": "90-120 aralığı anestezi altındaki kedi ve köpekler için hedeflenen optimal aralıktır."
        },
        "slayt_no": 15
    },
    {
        "soru_id": "mcq_mon_024",
        "soru_metni": "Birçok anestezik madde miyokard üzerine depresyon oluşturup kalp frekansını azaltırken, aşağıdaki ilaçlardan hangisi kalp frekansını belirgin şekilde yükseltir?",
        "secenekler": {
            "A": "Atropin",
            "B": "Halotan",
            "C": "Ksilazin",
            "D": "Asepromazin",
            "E": "Tiyopental"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Atropin parasempatolitik (vagus blokeri) etkisi sayesinde hayvanlarda kalp frekansını belirgin yükseltir (Slayt 15).",
            "celdirici_analizi": "Halotan ve ksilazin bradikardi yapma eğilimindedir."
        },
        "slayt_no": 15
    },
    {
        "soru_id": "mcq_mon_025",
        "soru_metni": "Kalp monitörizasyonunda stetoskop veya EKG ile kalp frekansının saptanması sirkülasyonun yeterli olduğunu tek başına neden kanıtlamaz?",
        "secenekler": {
            "A": "Çünkü EKG sadece hayvan uyanıkken çalışır",
            "B": "Kalp frekansı yeterli olsa bile vuru hacmi ve kan basıncı düşük olabilir, bu nedenle pulzasyon dolgunluğu ve kan basıncı ile birlikte değerlendirilmelidir",
            "C": "Kalp sesleri akciğer sesleriyle tamamen aynıdır",
            "D": "Stetoskop sadece solunum seslerini duyar",
            "E": "Kalp atımı sadece idrar çıkışı varsa gerçekleşir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Kalp frekansının varlığı sirkülasyonun yeterli olduğunu göstermez; pulzasyonun dolgunluğu veya kan basıncı ile birlikte değerlendirilmelidir (Slayt 16).",
            "celdirici_analizi": "Elektromekanik disosiasyon veya derin hipotansiyonda ritim olabilir ama perfüzyon yoktur."
        },
        "slayt_no": 16
    },
    {
        "soru_id": "mcq_mon_026",
        "soru_metni": "İnhalasyon anesteziklerinden özellikle hangisi kullanıldığında, anestezi derinliğinin artması doğrudan belirgin hipotansiyon oluşturur?",
        "secenekler": {
            "A": "Halotan",
            "B": "N2O (Nitrous oxide)",
            "C": "Oksijen",
            "D": "Karbondioksit",
            "E": "Azot"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Özellikle halotan kullanıldığında anestezi derinliğinin artması doğrudan miyokard kontraktilitesini ve periferik direnci düşürerek hipotansiyon oluşturur (Slayt 17).",
            "celdirici_analizi": "Halotan doza bağımlı olarak güçlü bir kardiyovasküler depresandır."
        },
        "slayt_no": 17
    },
    {
        "soru_id": "mcq_mon_027",
        "soru_metni": "Preanestezik ilaçlardan Asepromazin ve Ksilazinin anestezi altındaki hastada hipotansiyon oluşturmasının temel mekanizması nedir?",
        "secenekler": {
            "A": "Damarlarda dilatasyon (vazodilatasyon) oluşturmaları",
            "B": "Akciğer alveollerini parçalamaları",
            "C": "Kanda eritrosit sayısını aşırı artırmaları",
            "D": "Vücut ısısını aniden 42°C'ye çıkarmaları",
            "E": "Böbreklerden aşırı su emilimi yapmaları"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Asepromazin (alfa-1 blokaj ile) ve Ksilazin periferik damarlarda dilatasyon oluşturduğu için hipotansiyon meydana getirirler (Slayt 17).",
            "celdirici_analizi": "Vazodilatasyon sistemik vasküler rezistansı düşürerek kan basıncını aşağı çeker."
        },
        "slayt_no": 17
    },
    {
        "soru_id": "mcq_mon_028",
        "soru_metni": "Anestezi altındaki bir köpekte periferal pulzasyon güçlükle hissediliyorsa veya zayıfsa bu durum öncelikle neye işaret eder?",
        "secenekler": {
            "A": "Aşırı hipertansiyona",
            "B": "Hipovolemi ya da derin anesteziye bağlı kan basıncının düştüğüne",
            "C": "Hastanın tamamen anestezi dışına çıktığına",
            "D": "Akciğerlerin aşırı havalandığına",
            "E": "Kan şekerinin çok yükseldiğine"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Pulzasyon güçlükle hissediliyor ise bu durum hipovolemi ya da derin anesteziye bağlı kan basıncının düştüğünü gösterir (Slayt 18).",
            "celdirici_analizi": "Zayıf nabız düşük atım hacmi ve düşük nabız basıncının işaretidir."
        },
        "slayt_no": 18
    },
    {
        "soru_id": "mcq_mon_029",
        "soru_metni": "Hastanın sistolik kan basıncı yaklaşık kaç mmHg'nın altına düştüğünde Kapiller Dolum Zamanı (CRT) belirgin derecede uzar?",
        "secenekler": {
            "A": "140 - 150 mmHg",
            "B": "110 - 120 mmHg",
            "C": "70 - 80 mmHg",
            "D": "95 - 100 mmHg",
            "E": "180 mmHg"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "Hastanın sistolik kan basıncı 70-80 mmHg'dan daha düşük ise periferik kılcal damar yatağı perfüzyonu çöker ve CRT belirgin derecede uzar (Slayt 20).",
            "celdirici_analizi": "70-80 mmHg sistolik basınç periferik kapiller dolumu sürdürmek için kritik eşiktir."
        },
        "slayt_no": 20
    },
    {
        "soru_id": "mcq_mon_030",
        "soru_metni": "Anestezi sırasında idrar atımının çok yavaşlaması veya tamamen durması öncelikle hangi parametrenin bozulduğunu gösterir?",
        "secenekler": {
            "A": "Arteriyel kan basıncının belirgin düştüğünü",
            "B": "Hastanın aşırı su içtiğini",
            "C": "Anestezi derinliğinin yetersiz olduğunu",
            "D": "Vücut ısısının aşırı yükseldiğini",
            "E": "Oksijen akış hızının fazla olduğunu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "İdrar atımı kan basıncının bir göstergesidir; kan basıncı düştüğünde böbrek glomerül filtrasyonu durur ve idrar atımı tamamen durabilir (Slayt 20).",
            "celdirici_analizi": "Oligüri veya anüri anestezi sırasında renal hipoperfüzyonun en net uyarısıdır."
        },
        "slayt_no": 20
    },
    {
        "soru_id": "mcq_mon_031",
        "soru_metni": "Direkt kan basıncı ölçüm yönteminde artere (örneğin a. femoralis) yerleştirilen kateter ile elde edilen basınç değeri aşağıdakilerden hangisidir?",
        "secenekler": {
            "A": "Sadece venöz santral basınç",
            "B": "Ortalama kan basıncı (MAP)",
            "C": "Sadece intrakraniyal basınç",
            "D": "İntraoküler basınç",
            "E": "Onkotik basınç"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Direkt yöntemde a. femoralis kateterizasyonu ile elde edilen basınç, ortalama kan basıncıdır (MAP) (Slayt 21).",
            "celdirici_analizi": "Direkt arteriyel monitörizasyon kardiyak siklus boyunca ortalama basıncı verir."
        },
        "slayt_no": 21
    },
    {
        "soru_id": "mcq_mon_032",
        "soru_metni": "İndirekt kan basıncı ölçümünde sfigmomanometre kullanılırken ilk pulzasyon hareketinin başladığı ve hareketin söndüğü değerler sırasıyla neyi ifade eder?",
        "secenekler": {
            "A": "Başladığı değer: Diastolik | Söndüğü değer: Sistolik",
            "B": "Başladığı değer: Sistolik | Söndüğü değer: Diastolik",
            "C": "Başladığı değer: Venöz | Söndüğü değer: Kapiller",
            "D": "Başladığı değer: MAP | Söndüğü değer: Nabız",
            "E": "Her iki değer de sadece nabız sayısını ifade eder"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "İlk pulzasyon hareketinin başladığı değer sistolik basınç, hareketin söndüğü değer ise diastolik basınç olarak ölçülür (Slayt 21).",
            "celdirici_analizi": "Manşon basıncı damar içi tepe basıncına eşitlendiğinde ilk akım (sistolik) başlar."
        },
        "slayt_no": 21
    },
    {
        "soru_id": "mcq_mon_033",
        "soru_metni": "Direkt kan basıncı ölçümü için köpek ve kedilerde en sık hangi arterler tercih edilir?",
        "secenekler": {
            "A": "Pulmoner arter veya renal arter",
            "B": "Dorsal pedal arter veya femoral arter",
            "C": "Sadece vena kava kranyalis",
            "D": "Portal ven veya juguler ven",
            "E": "Koroner arterler"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Direkt kan basıncı ölçümü için köpek ve kedilerde dorsal pedal arter veya femoral arter kullanılır (Slayt 22).",
            "celdirici_analizi": "At ve ruminantlarda ise dorsal metatarsal veya fasiyal arter kullanılır."
        },
        "slayt_no": 22
    },
    {
        "soru_id": "mcq_mon_034",
        "soru_metni": "Anestezi altındaki hayvanlarda normal sistolik, diastolik ve ortalama kan basıncı (MAP) sınırları hangisinde eksiksiz ve doğru verilmiştir?",
        "secenekler": {
            "A": "Sistolik: 50-70 | Diastolik: 30-50 | MAP: 40-50 mmHg",
            "B": "Sistolik: 100-160 | Diastolik: 60-100 | MAP: 80-120 mmHg",
            "C": "Sistolik: 180-220 | Diastolik: 120-140 | MAP: 150-180 mmHg",
            "D": "Sistolik: 80-90 | Diastolik: 40-50 | MAP: 50-60 mmHg",
            "E": "Sistolik: 120-130 | Diastolik: 110-120 | MAP: 115 mmHg"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Hayvanlarda sistolik 100-160 mmHg, diastolik 60-100 mmHg, ortalama kan basıncı ise 80-120 mmHg olmalıdır (Slayt 22).",
            "celdirici_analizi": "Bu değerler anestezi periyodunda organ hasarını önleyen ideal aralıklardır."
        },
        "slayt_no": 22
    },
    {
        "soru_id": "mcq_mon_035",
        "soru_metni": "Sistolik kan basıncının _____ mmHg'dan, ortalama kan basıncının ise _____ mmHg'dan aşağı düşmesi yetersiz serebral ve koroner perfüzyona neden olur. Boşluklara sırasıyla hangisi gelmelidir?",
        "secenekler": {
            "A": "120 - 90",
            "B": "80 - 60",
            "C": "100 - 80",
            "D": "60 - 40",
            "E": "50 - 30"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Sistolik kan basıncının 80 mmHg'dan, ortalama kan basıncının 60 mmHg'dan aşağı düşmesi beyin ve kalp perfüzyonunu bozar (Slayt 22).",
            "celdirici_analizi": "MAP < 60 mmHg böbrek, beyin ve miyokard iskemisinin başladığı mutlak sınırdır."
        },
        "slayt_no": 22
    },
    {
        "soru_id": "mcq_mon_036",
        "soru_metni": "Anestezi sırasında şekillenen hipotansiyonun klinikte karşılaşılan en önemli ve en yaygın nedeni aşağıdakilerden hangisidir?",
        "secenekler": {
            "A": "Hipovolemi",
            "B": "Hiperkalsemi",
            "C": "Aşırı hemoglobin miktarı",
            "D": "Hipotansiyon sadece travmatik beyin tümörlerinde görülür",
            "E": "Aşırı sıvı yüklemesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Hipotansiyonun en önemli nedeni hipovolemidir; hipovolemi meydana geldiğinde kristalloid ve kolloidlerle tedavi edilmelidir (Slayt 23).",
            "celdirici_analizi": "Dehidratasyon, kan kaybı veya açlık hipovolemiyi tetikler."
        },
        "slayt_no": 23
    },
    {
        "soru_id": "mcq_mon_037",
        "soru_metni": "Mukoza renginin değerlendirilmesinde en yaygın kullanılan bölge neresidir ve pigmentli olması halinde nerelere bakılır?",
        "secenekler": {
            "A": "Sadece kulak kepçesi",
            "B": "En yaygın gingivadır; pigmentliyse dil, yanak, alt göz kapağı konjonktivası, vulva/prepisyuma bakılır",
            "C": "Sadece tırnak dipleri",
            "D": "Karın derisi",
            "E": "Kuyruk ucu"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "En yaygın bölge diş etidir (gingiva). Pigmentliyse dil, yanak mukozası, konjonktiva, vulva ve prepisyum kontrol edilir (Slayt 24).",
            "celdirici_analizi": "Pigmentsiz müköz membranlar kapiller kan akımını en net yansıtan bölgelerdir."
        },
        "slayt_no": 24
    },
    {
        "soru_id": "mcq_mon_038",
        "soru_metni": "Mukoz membranların mavi renge dönmesi (siyanoz) anestezi altında öncelikle neyin göstergesidir?",
        "secenekler": {
            "A": "Aşırı yüksek oksijen satürasyonunun",
            "B": "Solunum yetmezliğinden veya üst solunum yolunda tıkanıklıktan kaynaklanan şiddetli hipoksinin",
            "C": "Hastanın derin uykuya geçtiğinin",
            "D": "Kan basıncının normale döndüğünün",
            "E": "Anestezi gazının bittiğinin"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Mavi renge dönen mukoz membranlar siyanozdur; solunum yetmezliğinden veya üst solunum yolundaki bir tıkanıklıktan kaynaklanır (Slayt 24).",
            "celdirici_analizi": "Deoksijenize hemoglobinin 5 g/dL üzerine çıkması siyanoz yaratır."
        },
        "slayt_no": 24
    },
    {
        "soru_id": "mcq_mon_039",
        "soru_metni": "Sağlıklı kedi ve köpekler vücut ağırlığı başına yaklaşık ne kadar kan kaybını sirkülasyon şoku gelişmeden tolere edebilirler?",
        "secenekler": {
            "A": "1 - 2 ml/kg",
            "B": "13 ml/kg (kan volümünün %15'i)",
            "C": "45 ml/kg (kan volümünün %60'ı)",
            "D": "80 ml/kg",
            "E": "Hiçbir kan kaybı tolere edilemez"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Sağlıklı hayvanlar kan volümünün %15'ini şoksuz tolere edebilirler; bu miktar kedi ve köpeklerde yaklaşık 13 ml/kg'dır (Slayt 24).",
            "celdirici_analizi": "13 ml/kg üzeri akut kanamalarda derhal kan/sıvı replasmanı gerekir."
        },
        "slayt_no": 24
    },
    {
        "soru_id": "mcq_mon_040",
        "soru_metni": "Anestezi süresinin uzaması hastanın beden ısısında genellikle kaç derece düşüşe neden olur?",
        "secenekler": {
            "A": "0.1°C",
            "B": "3°C veya daha fazla",
            "C": "10°C",
            "D": "Hiç düşmez, daima 40°C'ye yükselir",
            "E": "Isı değişimi sadece kuşlarda görülür"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Anestezi süresinin uzaması hastanın beden ısısında 3°C ya da daha fazla düşmeye (hipotermi) neden olur (Slayt 25).",
            "celdirici_analizi": "Hipotermi anesteziklerin metabolizmasını yavaşlatıp uyanmayı geciktirir."
        },
        "slayt_no": 25
    },
    {
        "soru_id": "mcq_mon_041",
        "soru_metni": "Aşağıdakilerden hangisi anestezi altındaki hastada beden ısısının düşmesine (hipotermi) katkıda bulunan nedenlerden biri DEĞİLDİR?",
        "secenekler": {
            "A": "Operasyon öncesi bölgenin soğuk antiseptik ve alkolle yıkanması",
            "B": "Kas aktivitesi ve titreme oluşmamasına bağlı ısı üretilememesi",
            "C": "Anestezi döneminde metabolizmanın belirgin yavaşlaması",
            "D": "Operasyon sırasında vücut boşluklarının açılmasına bağlı ısı kaybı",
            "E": "Tüm anesteziklerin aşırı vazokonstriksiyon yaparak ısıyı hapsetmesi"
        },
        "dogru_cevap": "E",
        "aciklama": {
            "genel": "Aksine, birçok preanestezik ve anestezik damarlarda vazodilatasyon oluşturarak radyasyonla ısı kaybını artırır (Slayt 25).",
            "celdirici_analizi": "Vazodilatasyon ısı kaybını hızlandıran ana mekanizmalardan biridir."
        },
        "slayt_no": 25
    },
    {
        "soru_id": "mcq_mon_042",
        "soru_metni": "Özellikle Halotan kullanılan hayvanlarda nadiren görülen, acil önlem alınmazsa vücut ısısının aşırı artmasıyla ölüme sebebiyet veren tablo hangisidir?",
        "secenekler": {
            "A": "Malignant hipertermi",
            "B": "Hipotermik koma",
            "C": "Anafilaktik şok",
            "D": "Status epileptikus",
            "E": "Solunum alkalozu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Özellikle halotan kullanılan hayvanlarda oluşabilen ve ölümcül olan bu aşırı ısı artışına 'malignant hipertermi' denir (Slayt 25).",
            "celdirici_analizi": "Malign hipertermi kalsiyum regülasyon bozukluğuna bağlı hiperkatabolik bir krizdir."
        },
        "slayt_no": 25
    },
    {
        "soru_id": "mcq_mon_043",
        "soru_metni": "Palpebral refleks nasıl test edilir ve hayvan için fizyolojik önemi nedir?",
        "secenekler": {
            "A": "Korneaya iğne batırılarak; görme keskinliğini test eder",
            "B": "Gözün medial ya da lateral açısına hafifçe dokunularak; bilinçli hayvanda gözün korunmasını sağlar",
            "C": "Pupillaya kuvvetli ışık tutularak; beyin omurilik sıvısını ölçer",
            "D": "Kulak kepçesi çekilerek; işitmeyi korur",
            "E": "Çene açılarak; diş tonusunu belirler"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Gözün medial ya da lateral kantusuna hafifçe dokunularak tespit edilir. Bilinçli hayvanlarda gözün korunmasını sağlayan bir reflekstir (Slayt 26).",
            "celdirici_analizi": "Cerrahi anestezide kaybolur, geri dönmesi uyanmayı gösterir."
        },
        "slayt_no": 26
    },
    {
        "soru_id": "mcq_mon_044",
        "soru_metni": "Ketamin anestezisi ile Halotan anestezisi altında palpebral refleksin durumu hangisinde doğru kıyaslanmıştır?",
        "secenekler": {
            "A": "Ketaminde tamamen kaybolur, halotanda hiç değişmez",
            "B": "Ketaminle anestezide palpebral refleks ortadan kalkmaz iken, halotan ile anestezide tamamen ortadan kalkar",
            "C": "Her iki anestezikte de palpebral refleks her zaman pozitiftir",
            "D": "Her iki anestezikte de ilk saniyede yok olur",
            "E": "Ketamin sadece korneal refleksi yok eder"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Ketamin dissosiyatif anestezi oluşturduğu için palpebral refleks ortadan kalkmaz; halotanda ise tamamen ortadan kalkar (Slayt 26).",
            "celdirici_analizi": "Ketamin kullanan hastada palpebral refleksin olması anestezinin yüzeysel olduğu anlamına gelmez."
        },
        "slayt_no": 26
    },
    {
        "soru_id": "mcq_mon_045",
        "soru_metni": "Palpebral refleksin cerrahi operasyonun sonunda geri dönmesi klinisyen için neyi müjdeler?",
        "secenekler": {
            "A": "Hayvanın arrest olduğunu",
            "B": "Hayvanın anesteziden uyanmak üzere olduğunu",
            "C": "Hayvanın felç geçirdiğini",
            "D": "Anestezi gazının bittiğini ama uyanamayacağını",
            "E": "Korneanın kuruduğunu"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Palpebral refleksin geri dönmesi hayvanın anesteziden uyanmak üzere olduğunu gösterir (Slayt 26).",
            "celdirici_analizi": "Uyanma sürecinde reflekslerin sırasıyla geri dönüşü gözlemlenir."
        },
        "slayt_no": 26
    },
    {
        "soru_id": "mcq_mon_046",
        "soru_metni": "Yutkunma refleksinin anestezi dönemlerindeki seyri ve ekstübasyon zamanı ile ilişkisi nasıldır?",
        "secenekler": {
            "A": "Yüzeyselde kaybolur, derinde ortaya çıkar",
            "B": "Yüzeysel dönemde mevcuttur, orta düzey cerrahide kalkar; hayvan uyanırken geri döndüğü anda ekstübasyon yapılmalıdır",
            "C": "Anestezi boyunca hiç kaybolmaz",
            "D": "Sadece köpeklerde vardır, kedilerde yutkunma refleksi bulunmaz",
            "E": "Yutkunma refleksi geri gelmeden tüp çekilmelidir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Yüzeysel dönemde mevcuttur, orta düzeyde ortadan kalkar. Uyanırken geri döner ve aspirasyonu önlemek için tüp bu anda çekilmelidir (Slayt 27).",
            "celdirici_analizi": "Yutkunma refleksi hava yolu güvenliğinin en kritik bekçisidir."
        },
        "slayt_no": 27
    },
    {
        "soru_id": "mcq_mon_047",
        "soru_metni": "Anestezi altındaki hastada korneaya dokunulması ile bakılan korneal refleksin tamamen yok olması neyi gösterir?",
        "secenekler": {
            "A": "Anestezinin çok hafif ve yetersiz olduğunu",
            "B": "Anestezinin çok derin düzeyde olduğunu (hayati risk)",
            "C": "Hastanın görme yetisinin açıldığını",
            "D": "Kalp frekansının arttığını",
            "E": "Oksijen satürasyonunun %100 olduğunu"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Korneal refleksin yok olması anestezinin çok derin düzeyde olduğunu gösterir (Dönem III Plan 3'e kadar görülebilir) (Slayt 28).",
            "celdirici_analizi": "Korneal refleks kaybı agoni ve medulla depresyonu sınırıdır; acil doz azaltılmalıdır."
        },
        "slayt_no": 28
    },
    {
        "soru_id": "mcq_mon_048",
        "soru_metni": "Aşağıdaki anestezik/sedatif maddelerden hangileri iskelet kas tonusunda gevşeme yerine tonus artışına (rijidite) neden olur?",
        "secenekler": {
            "A": "Ksilazin ve Diazepam",
            "B": "Ketamin ve Tiletamin",
            "C": "İzofluran ve Sevofluran",
            "D": "Propofol ve Tiopental",
            "E": "Asepromazin ve Midazolam"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Ketamin ve Tiletamin gibi dissosiyatif anestezikler kasların tonusunda artma meydana getirirler (Slayt 29).",
            "celdirici_analizi": "Bu nedenle dissosiyatifler daima kas gevşetici ajanlarla (ksilazin, diazepam) kombine edilir."
        },
        "slayt_no": 29
    },
    {
        "soru_id": "mcq_mon_049",
        "soru_metni": "Anestezinin II. döneminde (Eksitasyon/Deliryum) göz küresi tipik olarak hangi pozisyondadır?",
        "secenekler": {
            "A": "Tam merkezdedir",
            "B": "Hayvan çenesine bakıyormuş pozisyonundadır (ventromedial)",
            "C": "Tam yukarı tavana bakar",
            "D": "Göz küreleri sürekli saat yönünde döner",
            "E": "Gözler tamamen yuvasından dışarı fırlar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Anestezinin II. döneminde göz küresi ventromedial pozisyona kayar, yani hayvan çenesine bakıyormuş pozisyonundadır (Slayt 30).",
            "celdirici_analizi": "Cerrahi döneme (Dönem III) geçildiğinde göz tekrar merkezi pozisyona döner."
        },
        "slayt_no": 30
    },
    {
        "soru_id": "mcq_mon_050",
        "soru_metni": "Genel anestezide cerrahi anestezi dönemine (Dönem III) girildiğinde göz küresi pozisyonu nasıldır?",
        "secenekler": {
            "A": "Tekrar merkezi pozisyonuna geri döner",
            "B": "Çeneye doğru daha da aşağı sarkar",
            "C": "Sadece tek bir göz yukarı bakar",
            "D": "Göz kapakları asla kapanmaz",
            "E": "Göz tamamen kaybolur"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Cerrahi anestezi döneminde göz tekrar merkezi pozisyonuna geri döner (Slayt 30).",
            "celdirici_analizi": "Dönem I merkezde, Dönem II ventromedial, Dönem III cerrahide tekrar merkezdedir."
        },
        "slayt_no": 30
    },
    {
        "soru_id": "mcq_mon_051",
        "soru_metni": "Anestezi altındaki bir hastada gözün merkezde olması, belirgin midriyazis bulunması ve ışığa karşı pupiller refleksin hiç olmaması neyi belgeler?",
        "secenekler": {
            "A": "Anestezinin ideal cerrahi düzeyde olduğunu",
            "B": "Anestezi derinliğinin tehlike sınırları içerisine girdiğini (aşırı doz / arrest riski)",
            "C": "Hayvanın tamamen uyanıp ayağa kalkacağını",
            "D": "Kas gevşemesinin yetersiz olduğunu",
            "E": "Oksijen tüpünün dolu olduğunu"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Gözün merkezde olması, midriyazis ve ışığa tepkinin olmaması anestezi derinliğinin tehlike sınırları içerisine girdiğini gösterir (Slayt 31).",
            "celdirici_analizi": "Fiks dilate pupilla beyin sapı depresyonunu ve ölüm tehlikesini gösterir."
        },
        "slayt_no": 31
    },
    {
        "soru_id": "mcq_mon_052",
        "soru_metni": "Pupillanın değerlendirilmesinde, özellikle kedilerde midriyazis oluşturacağı için göz önünde bulundurulması gereken preanestezik ilaç hangisidir?",
        "secenekler": {
            "A": "Atropin",
            "B": "Ksilazin",
            "C": "Asepromazin",
            "D": "Fentanil",
            "E": "Lidokain"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Kedilerde kullanılan atropinin midriyazis oluşturacağı göz önünde bulundurulmalıdır; bu durum anestezi derinliğiyle karıştırılmamalıdır (Slayt 31).",
            "celdirici_analizi": "Atropin siliyer ganglion blokajı ile midriyazise neden olur."
        },
        "slayt_no": 31
    },
    {
        "soru_id": "mcq_mon_053",
        "soru_metni": "Genel kural olarak solunum sayısı ve kalp frekansı anestezi derinliği arttıkça nasıl bir seyir izler?",
        "secenekler": {
            "A": "Her ikisi de kontrolsüz şekilde artar",
            "B": "Her iki parametre de anestezi derinliği arttıkça azalma eğilimi gösterir",
            "C": "Solunum artarken kalp frekansı tamamen durur",
            "D": "Hiçbir şekilde değişmez",
            "E": "Kalp hızı 300'e çıkar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Bu iki parametre anestezi derinliği arttıkça azalma eğilimi gösterir (Slayt 32).",
            "celdirici_analizi": "Merkezi sinir sistemi ve miyokard depresyonu arttıkça frekanslar düşer."
        },
        "slayt_no": 32
    },
    {
        "soru_id": "mcq_mon_054",
        "soru_metni": "Cerrahi sırasında iç organlara dokunulması veya ovaryum ligamentlerinin gerdirilmesi durumunda hayvanda hangi fizyolojik tepki gelişir?",
        "secenekler": {
            "A": "Kalp frekansı ve kan basıncı düşer, hasta derin uykuya dalar",
            "B": "Ağrı algılanmasına bağlı sempatik deşarjla kalp frekansı ve kan basıncı artar",
            "C": "Vücut ısısı 25°C'ye iner",
            "D": "Solunum tamamen durur",
            "E": "CRT 0 saniyeye iner"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Ovaryum ligamenti çekildiğinde ağrı algılanır; cerrahi uyarıyı algılayan hayvanda kalp frekansı ve kan basıncı artar (Slayt 33).",
            "celdirici_analizi": "Viseral nosisepsiyon otonomik sempatik aktivasyonu tetikler."
        },
        "slayt_no": 33
    },
    {
        "soru_id": "mcq_mon_055",
        "soru_metni": "Cerrahi uyarı karşısında lakrimasyon (gözyaşı), salivasyon ve pedal hareketlerin görülmesi neyin kesin belgesidir?",
        "secenekler": {
            "A": "Anestezinin çok derin ve toksik olduğunun",
            "B": "Anestezinin yetersizliğini ve hayvanın ağrı hissettiğini",
            "C": "Hayvanın görme yeteneğini kaybettiğinin",
            "D": "Kan basıncının sıfıra indiğinin",
            "E": "Atelektazinin tamamen çözüldüğünün"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Lakrimasyon, salivasyon ve pedal hareketler anestezinin yetersizliğini ve ağrının hissedildiğini belgeler (Slayt 33).",
            "celdirici_analizi": "Bu klinik bulgular yetersiz anestezi derinliği ve yetersiz analjezinin açık kanıtıdır."
        },
        "slayt_no": 33
    },
    {
        "soru_id": "mcq_mon_056",
        "soru_metni": "Genel anesteziden uyanma süresinin uzamasını etkileyen faktörler arasında aşağıdakilerden hangisi YER ALMAZ?",
        "secenekler": {
            "A": "Genel anestezi süresinin uzun olması",
            "B": "Hayvanın genel durumunun zayıf veya kaşektik olması",
            "C": "Uygulanan anestezik maddenin cinsi ve uygulanış şekli",
            "D": "Enjektabl anesteziklerin IM yolla verilmiş olması",
            "E": "Anestezi devresinde bakteri filtresi kullanılmış olması"
        },
        "dogru_cevap": "E",
        "aciklama": {
            "genel": "Bakteri filtresi uyanma süresini etkilemez. Süre, anestezi süresi, genel durum ve ilaç cinsine/yoluna bağlıdır (Slayt 34).",
            "celdirici_analizi": "Uyanma süresini farmakokinetik faktörler ve hastanın metabolik kapasitesi belirler."
        },
        "slayt_no": 34
    },
    {
        "soru_id": "mcq_mon_057",
        "soru_metni": "İnhalasyon anestezisi ile enjektabl anesteziklerin uyanma süreleri kıyaslandığında doğru olan ifade hangisidir?",
        "secenekler": {
            "A": "İnhalasyon anestezisinden uyanma, enjektabl anestezisinden uyanmaya göre daha kısa sürede gerçekleşir",
            "B": "Enjektabl anesteziklerden uyanma daima inhalasyondan daha hızlıdır",
            "C": "Her iki yöntemde de uyanma süresi saniyesi saniyesine aynıdır",
            "D": "İnhalasyon anestezisinde uyanma için mutlaka antidot verilmelidir",
            "E": "Enjektabl anesteziklerde uyanma karaciğerden bağımsızdır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "İnhalasyon anestezisinden uyanma ekspirasyonla hızlı gaz atılımı sayesinde enjektabl anesteziye göre daha kısa sürede gerçekleşir (Slayt 34).",
            "celdirici_analizi": "Enjektabl anesteziklerin eliminasyonu karaciğer metabolizması ve renal atılıma bağımlıdır."
        },
        "slayt_no": 34
    },
    {
        "soru_id": "mcq_mon_058",
        "soru_metni": "Enjektabl anesteziklerin hangi yolla verilmesi, intramusküler (IM) yolla verilmesine kıyasla daha kısa sürede uyanma sağlar?",
        "secenekler": {
            "A": "Deri altı (SC) yol",
            "B": "İntravenöz (IV) yol",
            "C": "Ağızdan (Oral) yol",
            "D": "Rektal yol",
            "E": "İntradermal yol"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Enjektabl uygulanan anesteziklerin IV yolla verilmesi, IM verilmesinden daha kısa sürede uyanma sağlar (Slayt 34).",
            "celdirici_analizi": "IM uygulamada kastan kana emilim devam ettiği için uyanma belirgin şekilde gecikir."
        },
        "slayt_no": 34
    },
    {
        "soru_id": "mcq_mon_059",
        "soru_metni": "Uyanma dönemindeki bir hasta en geç hangi aralıklarla kontrol edilmelidir?",
        "secenekler": {
            "A": "Her 5 dakikada bir",
            "B": "Saatte bir kez",
            "C": "Yalnızca ertesi sabah",
            "D": "20 dakikada bir",
            "E": "Kontrole gerek yoktur"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Uyanma dönemindeki hayvan her 5 dakikada bir kontrol edilmelidir (Slayt 35).",
            "celdirici_analizi": "Postoperatif ilk saatler ölüm oranının en yüksek olduğu zaman dilimidir."
        },
        "slayt_no": 35
    },
    {
        "soru_id": "mcq_mon_060",
        "soru_metni": "Uyanma dönemindeki bir hastaya uzaktan bakarak değerlendirme yapmanın hekimlik açısından kesinlikle yanlış olmasının nedeni nedir?",
        "secenekler": {
            "A": "Uzaktan bakıldığında hayvanın cinsiyeti anlaşılmaz",
            "B": "Bu dönemde ölümcül bradikardi ve solunum yetmezliği oluşabilir ve bunlar uzaktan gözle asla tespit edilemez",
            "C": "Uzaktan bakmak hastanın tansiyonunu yükseltir",
            "D": "Işık yansıması nedeniyle göz refleksleri yanlış görülür",
            "E": "Tüm hayvanlar uzaktan bakıldığında uyanmış gibi görünür"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Uyanma dönemindeki hayvana uzaktan bakıp değerlendirme doğru değildir; bu dönemde bradikardi ve solunum yetmezliği oluşabilir, bunlar uzaktan gözle tespit edilemez (Slayt 35).",
            "celdirici_analizi": "Yakından stetoskop muayenesi, mukoza ve nabız kontrolü hayati önem taşır."
        },
        "slayt_no": 35
    },
    {
        "soru_id": "mcq_mon_061",
        "soru_metni": "Uyanma dönemindeki hastanın kontrolünde klinisyenin özellikle dikkat etmesi gereken üç temel parametre hangisidir?",
        "secenekler": {
            "A": "Mukoza rengi, Kapiller dolum zamanı (CRT) ve solunum",
            "B": "Tüy parlaklığı, tırnak uzunluğu ve iştah",
            "C": "Kuyruk sallama sıklığı, kulak ısısı ve kilo",
            "D": "Sadece idrarın berraklığı",
            "E": "Sadece kan grubu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "Özellikle mukoz membran rengi, CRT (kapillar dolum zamanı) ve solunuma dikkat edilmelidir (Slayt 35).",
            "celdirici_analizi": "Bu üç parametre oksijenizasyon, perfüzyon ve hava yolu güvenliğini doğrudan gösterir."
        },
        "slayt_no": 35
    },
    {
        "soru_id": "mcq_mon_062",
        "soru_metni": "Solunum sisteminin oskültasyonunda duyulan sürtünme veya ıslık sesi gibi anormal sesler öncelikle neyi düşündürür?",
        "secenekler": {
            "A": "Anestezi gazının bittiğini",
            "B": "Soluk yolunda daralma veya tıkanma ya da soluk yolları ve alveollerde sıvının varlığını",
            "C": "Hayvanın şarkı söylediğini",
            "D": "Kalp kapakçıklarının tamamen kapandığını",
            "E": "Akciğerlerin aşırı genişlediğini"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Sürtünme sesi, ıslık sesi gibi normal olmayan sesler soluk yolunda daralma veya tıkanma ya da soluk yolları ve alveollerde sıvı varlığını gösterebilir (Slayt 12).",
            "celdirici_analizi": "Stridor veya ronküs obstrüksiyon veya pulmoner ödem belirtisidir."
        },
        "slayt_no": 12
    },
    {
        "soru_id": "mcq_mon_063",
        "soru_metni": "Genel anestezi opioid türevleri (örn. fentanil, morfin) ile desteklendiğinde anesteziye mükemmel derecede ne eşlik eder?",
        "secenekler": {
            "A": "Sadece iskelet kası felci",
            "B": "Mükemmel derecede analjezi",
            "C": "Şiddetli hipertansiyon",
            "D": "Aşırı taşikardi",
            "E": "Hipertermi krizleri"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Genel anestezi opioid türevleri ile destekleniyor ise anesteziye mükemmel derecede analjezi eşlik eder (Slayt 4).",
            "celdirici_analizi": "Opioidler güçlü analjeziktir ancak yeterli kas gevşemesi için ilave ilaç gerekebilir."
        },
        "slayt_no": 4
    },
    {
        "soru_id": "mcq_mon_064",
        "soru_metni": "Büyük ruminant ve atlarda direkt arteriyel kan basıncı ölçümü için en sık kullanılan periferik arterler hangileridir?",
        "secenekler": {
            "A": "Femoral arter veya lingual arter",
            "B": "Dorsal metatarsal veya fasiyal arter",
            "C": "Koroner arter veya renal arter",
            "D": "Pulmoner arter",
            "E": "Abdominal aorta"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Ruminant ve atlarda dorsal metatarsal veya fasiyal arterler kullanılır (Slayt 22).",
            "celdirici_analizi": "Köpek ve kedilerde dorsal pedal ve femoral arter kullanılır."
        },
        "slayt_no": 22
    },
    {
        "soru_id": "mcq_mon_065",
        "soru_metni": "Anestezi altında mukoz membranların aşırı solgun olması klinisyene öncelikle hangi durumları düşündürmelidir?",
        "secenekler": {
            "A": "Aşırı yüksek hematokrit ve polisitemi",
            "B": "Kan kaybı, anemi veya anestezi süresinin uzamasına bağlı periferal perfüzyonun zayıflaması",
            "C": "Şiddetli hipertermi ve terleme",
            "D": "Üst solunum yolunun tıkandığını (siyanoz)",
            "E": "Hastanın tamamen iyileştiğini"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "Solgun mukoz membranlar kan kaybı ya da aneminin bir göstergesi veya anestezi süresinin uzamasına bağlı perfüzyonun zayıflamasından meydana gelebilir (Slayt 24).",
            "celdirici_analizi": "Siyanoz mavi renktir; solgunluk vazokonstriksiyon, hipovolemi veya anemidir."
        },
        "slayt_no": 24
    }
]

if __name__ == "__main__":
    print(f"Monitörizasyon modülü hazırlandı:")
    print(f"- Summary Sections: {len(SUMMARY_SECTIONS)}")
    print(f"- Bilgi Kartları: {len(BILGI_KARTLARI)}")
    print(f"- Açık Uçlu Sorular: {len(ACIK_UCLU_SORULAR)}")
    print(f"- Çoktan Seçmeli Sorular: {len(COKTAN_SECMELI_SORULAR)}")
