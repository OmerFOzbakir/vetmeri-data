# -*- coding: utf-8 -*-
"""
Sindirim Sistemi - Çoktan Seçmeli Sorular (Bölüm 1: 1 - 45)
Kapsam: Slayt 1 - 70 (Anatomi, Semptomlar, Disfaji, Kusma vs Regürgitasyon, Diyare, Stomatit, Sialadenit)
"""

QUESTIONS_PART1 = [
    {
        "soru_id": "mcq_sind_001",
        "soru_metni": "Sindirim sistemi organlarından ince bağırsakların anatomik sıralaması aşağıdakilerden hangisinde kranialden kaudale doğru doğru olarak verilmiştir?",
        "secenekler": {
            "A": "İleum - Jejunum - Duodenum",
            "B": "Duodenum - Jejunum - İleum",
            "C": "Duodenum - İleum - Sekum",
            "D": "Jejunum - Duodenum - Kolon"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ince bağırsaklar kranialden kaudale doğru Duodenum, Jejunum ve İleum olmak üzere üç ana bölümden oluşur (Slayt 4).",
            "celdirici_analizi": "A şıkkı ters sıralamadır; C ve D seçeneklerinde kalın bağırsak bölümleri yer almaktadır."
        },
        "slayt_no": 4,
        "zorluk_derecesi": "kolay",
        "etiketler": ["anatomi", "ince_bagirsak"]
    },
    {
        "soru_id": "mcq_sind_002",
        "soru_metni": "Sindirim sistemi organlarının metabolik aktiviteleri süresince gereksinim duyulan kan akışı hangi dolaşım sistemi tarafından desteklenir?",
        "secenekler": {
            "A": "Pulmoner dolaşım sistemi",
            "B": "Splanchnic kan dolaşımı",
            "C": "Kardiyak koroner dolaşım",
            "D": "Serebral kapiller sistem"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; tüm sindirim ve emilim olayları süresince metabolik aktivite splanchnic kan dolaşımı ile desteklenir (Slayt 5).",
            "celdirici_analizi": "A şıkkı akciğer dolaşımıdır; C şıkkı kalp kasını; D şıkkı ise beyni besler."
        },
        "slayt_no": 5,
        "zorluk_derecesi": "orta",
        "etiketler": ["fizyoloji", "kan_akisi"]
    },
    {
        "soru_id": "mcq_sind_003",
        "soru_metni": "Kedi ve köpeklerde 'Pitiyalismus' ile 'Pseudopitiyalismus' arasındaki temel fark hangisinde doğru açıklanmıştır?",
        "secenekler": {
            "A": "Pitiyalismusta tükürük salgısı artarken, pseudopitiyalismusta oral ağrı veya yutma güçlüğü nedeniyle tükürük yutulamaz ve dışarı akar",
            "B": "Pitiyalismus sadece köpeklerde, pseudopitiyalismus ise sadece kedilerde şekillenen bir durumdur",
            "C": "Pitiyalismus mide asiditesini azaltırken, pseudopitiyalismus safra sekresyonunu tamamen durdurur",
            "D": "Pseudopitiyalismus tükürük bezlerinin enfeksiyonuyken, pitiyalismus sadece diş tartarına bağlıdır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; pitiyalismus tükürük bezlerinin aşırı tükürük üretmesidir (hipersekresyon). Pseudopitiyalismus ise üretim normal olmasına rağmen ağrı veya mekanik/nörolojik yutma felci sebebiyle tükürüğün yutulamayıp akmasıdır (Slayt 9).",
            "celdirici_analizi": "B, C ve D şıkları fizyolojik ve klinik gerçeklerle uyuşmayan yanlış genellemelerdir."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "orta",
        "etiketler": ["semptom", "pitiyalismus"]
    },
    {
        "soru_id": "mcq_sind_004",
        "soru_metni": "Özellikle kedilerde şiddetli salya akıntısına (pitiyalismus) neden olabilen ve karaciğer fonksiyon bozukluğuyla seyreden nörometabolik tablo hangisidir?",
        "secenekler": {
            "A": "Pilorik stenoz sendromu",
            "B": "Hepatik ensefalopati",
            "C": "Megakolon hastalığı",
            "D": "Eozinofilik gastrit"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; özellikle kedilerde hepatik ensefalopati tablosunda şiddetli bulantı ve pitiyalismus en belirgin klinik semptomlardan biridir (Slayt 9).",
            "celdirici_analizi": "A şıkkı mide çıkış darlığıdır; C şıkkı obstipasyon tablosudur; D şıkkı ise alerjik mukoza yangısıdır."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "kolay",
        "etiketler": ["karaciger", "hepatik_ensefalopati", "kedi"]
    },
    {
        "soru_id": "mcq_sind_005",
        "soru_metni": "Hangisi kimyasal veya toksik bir uyaran olarak kedi-köpeklerde doğrudan pitiyalismusa yol açan ajanlardan biri DEĞİLDİR?",
        "secenekler": {
            "A": "Organofosfatlı insektisitler",
            "B": "Kostik ve irrite edici kimyasallar",
            "C": "Metronidazol ve atropin",
            "D": "Sukralfat ve kaolin pektin"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği doğrudur; sukralfat ve kaolin pektin mukoza koruyucu/adsorban ajanlar olup pitiyalismus toksik sebebi değildir. Organofosfat, kostik maddeler, metronidazol ve atropin toksik uyaranlar arasındadır (Slayt 9).",
            "celdirici_analizi": "A, B ve C seçeneklerindeki tüm maddeler slaytta kimyasal-toksik uyaranlar altında açıkça sıralanmıştır."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "orta",
        "etiketler": ["toksikoloji", "pitiyalismus"]
    },
    {
        "soru_id": "mcq_sind_006",
        "soru_metni": "Yutma fonksiyonunun (deglutisyon) anatomik fazları sırasıyla hangi seçenekte eksiksiz verilmiştir?",
        "secenekler": {
            "A": "Oral faz - Faringeal faz - Krikofaringeal faz",
            "B": "Glossofaringeal faz - Gastrik faz - Kolonik faz",
            "C": "Özefagal faz - Kardial faz - Pilorik faz",
            "D": "Faringeal faz - Laringeal faz - Trakeal faz"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; yutma işlemi Oral faz, Faringeal faz ve Krikofaringeal faz olmak üzere üç aşamada gerçekleşir (Slayt 11).",
            "celdirici_analizi": "B, C ve D seçeneklerinde yutma fizyolojisine ait olmayan uydurma veya mide-solunum evreleri verilmiştir."
        },
        "slayt_no": 11,
        "zorluk_derecesi": "kolay",
        "etiketler": ["disfaji", "yutma_fizyo"]
    },
    {
        "soru_id": "mcq_sind_007",
        "soru_metni": "Gıdanın ağıza alınması, çiğnenmesi, tükürükle yumuşatılması ve dil yardımıyla farenkse iletilmesi yutmanın hangi fazıdır?",
        "secenekler": {
            "A": "Krikofaringeal faz",
            "B": "Oral faz",
            "C": "Faringeal faz",
            "D": "Retrograd faz"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; gıdanın ağıza alınması, çiğnenip yumuşatılması ve bolus oluşturularak dilden farenkse itilmesi Oral fazdır (Slayt 11).",
            "celdirici_analizi": "A şıkkı özefagusa giriş fazıdır; C şıkkı farenksten geçiştir; D şıkkı ise kusma ile ilişkilidir."
        },
        "slayt_no": 11,
        "zorluk_derecesi": "kolay",
        "etiketler": ["disfaji", "oral_faz"]
    },
    {
        "soru_id": "mcq_sind_008",
        "soru_metni": "Disfajik bir hastanın nörolojik klinik muayenesinde değerlendirilmesi gereken temel kraniyal sinirler (CN) hangileridir?",
        "secenekler": {
            "A": "CN 1 (Olfaktör), CN 2 (Optik), CN 8 (Vestibulokohlear)",
            "B": "CN 5 (Trigeminal), CN 7 (Fasiyal), CN 9 (Glossofaringeal), CN 12 (Hipoglossal)",
            "C": "CN 3 (Okülomotor), CN 4 (Troklear), CN 6 (Abdusens)",
            "D": "CN 10 (Vagus) ve CN 11 (Aksesuar) hariç sadece spinal sinirler"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; yutma ve çiğneme mekanizmasında CN 5 (Trigeminal), CN 7 (Fasiyal), CN 9 (Glossofaringeal) ve CN 12 (Hipoglossal) kraniyal sinirleri muayene edilir (Slayt 16).",
            "celdirici_analizi": "A şıkkı duyu sinirleridir; C şıkkı göz kaslarını inerve eden sinirlerdir."
        },
        "slayt_no": 16,
        "zorluk_derecesi": "orta",
        "etiketler": ["noroloji", "kraniyal_sinirler", "disfaji"]
    },
    {
        "soru_id": "mcq_sind_009",
        "soru_metni": "Disfaji şüphesi olan bir kedi veya köpekte en değerli klinik tanısal yaklaşım adımı hangisidir?",
        "secenekler": {
            "A": "Mümkünse hayvan gıda alırken İNSPEKSİYON (gözlem) yapılması",
            "B": "Hayvanı 48 saat aç bırakıp doğrudan acil gastrotomiye almak",
            "C": "Hiçbir muayene yapmadan doğrudan geniş spektrumlu antibiyotik başlamak",
            "D": "Hemen genel anesteziye alıp sadece kalın bağırsak lavmanı yapmak"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; disfajinin hangi fazda (oral, faringeal, krikofaringeal) olduğunu ayırt etmek için hasta yemek yerken İNSPEKSİYON yapılması altın değerindedir (Slayt 16).",
            "celdirici_analizi": "B, C ve D şıkları amaca yönelik olmayan veya hastaya zarar verebilecek yaklaşımlardır."
        },
        "slayt_no": 16,
        "zorluk_derecesi": "kolay",
        "etiketler": ["klinik_yaklasim", "inspeksiyon"]
    },
    {
        "soru_id": "mcq_sind_010",
        "soru_metni": "Gıdayı ağızdan düşürme, başı aşağı eğme, ağzı açma ve kapamada güçlük ve yanak boşluğunda gıda birikimi hangi disfaji tipinin tipik bulgusudur?",
        "secenekler": {
            "A": "Krikofaringeal disfaji",
            "B": "Oral disfaji",
            "C": "Faringeal disfaji",
            "D": "Özefagal reflüks"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; çiğneme, bolus yapamama ve gıdanın yanakta birikip ağızdan düşürülmesi 'Oral Disfaji'nin kardinal bulgularıdır (Slayt 17).",
            "celdirici_analizi": "Faringeal ve krikofaringeal disfajide bolus oluşturma tamamen normaldir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "kolay",
        "etiketler": ["oral_disfaji", "klinik_bulgu"]
    },
    {
        "soru_id": "mcq_sind_011",
        "soru_metni": "Gıdayı ağıza alma, kavrama ve bolus oluşturmanın tamamen NORMAL olduğu, ancak yutma girişimi süresince şiddetli ÖĞÜRME ile gıdanın ağızdan düşürüldüğü disfaji tipi hangisidir?",
        "secenekler": {
            "A": "Oral disfaji",
            "B": "Faringeal disfaji",
            "C": "Krikofaringeal disfaji",
            "D": "Mide çıkış obstrüksiyonu"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; faringeal disfajide bolus oluşturma normaldir ancak yutma refleksi sırasında şiddetli öğürme oluşur ve gıda dışarı atılır (Slayt 17).",
            "celdirici_analizi": "Krikofaringeal disfajide öğürme genellikle YOKTUR; oral disfajide ise bolus hiç oluşturulamaz."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "orta",
        "etiketler": ["faringeal_disfaji", "ogurme"]
    },
    {
        "soru_id": "mcq_sind_012",
        "soru_metni": "Tekrarlayan yutma girişimleri görülen, bolus oluşturması normal olan, yutma girişimleri sonrası gıdayı ağızdan düşüren fakat ÖĞÜRMENİN GENELLİKLE OLMADIĞI disfaji tipi hangisidir?",
        "secenekler": {
            "A": "Krikofaringeal disfaji",
            "B": "Faringeal disfaji",
            "C": "Oral disfaji",
            "D": "Stomatitis ülserosa"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; krikofaringeal disfajide gıda üst özefagus sfinkterini geçemez; tekrarlayan yutkunma sonrası gıda düşürülür ancak öğürme genellikle YOKTUR (Slayt 17).",
            "celdirici_analizi": "Öğürmenin olmaması krikofaringeal formu faringeal formdan ayıran en kritik kriterdir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "orta",
        "etiketler": ["krikofaringeal_disfaji", "ayirici_tani"]
    },
    {
        "soru_id": "mcq_sind_013",
        "soru_metni": "Özellikle genç köpeklerde faringeal-krikofaringeal disfajiye neden olan konjenital fonksiyonel darlık anomalisi hangisidir?",
        "secenekler": {
            "A": "Krikofaringeal aklazi",
            "B": "Pilor stenozu",
            "C": "Hiatal herni",
            "D": "İntestinal invaginasyon"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; özellikle genç köpeklerde krikofaringeal kasın gevşeyememesi sonucu 'Krikofaringeal aklazi' gelişir ve yutma engellenir (Slayt 18).",
            "celdirici_analizi": "B şıkkı midededir; C şıkkı diyaframdadır; D şıkkı bağırsaktadır."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "orta",
        "etiketler": ["krikofaringeal_aklazi", "kopek"]
    },
    {
        "soru_id": "mcq_sind_014",
        "soru_metni": "Sıvı veya katı gıda materyalinin PASİF OLARAK özefagustan oral yönde uzaklaştırılması hangi klinik tablodur?",
        "secenekler": {
            "A": "Kusma (Vomitus)",
            "B": "Regürgitasyon",
            "C": "Hematemezis",
            "D": "Disfaji"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; gıda materyalinin hiçbir aktif abdominal efor veya bulantı olmaksızın pasif geri gelmesi 'Regürgitasyon' olarak tanımlanır (Slayt 19).",
            "celdirici_analizi": "Kusma aktif nörolojik reflekstir; hematemez kan kusmadır; disfaji yutma güçlüğüdür."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "kolay",
        "etiketler": ["regurgitasyon", "tanim"]
    },
    {
        "soru_id": "mcq_sind_015",
        "soru_metni": "Regürgitasyon sıvısı ile kusmuk karşılaştırıldığında, regürgitasyon içeriği için hangisi KESİNLİKLE DOĞRUDUR?",
        "secenekler": {
            "A": "İçerik asidiktir (pH <= 3) ve bol miktarda safra içerir",
            "B": "İçerik nötr veya alkalidir (pH >= 7) ve safra içeriği bulunmaz (-)",
            "C": "İçerikte daima yoğun miktarda sindirilmiş kan (kahve telvesi) vardır",
            "D": "Gıda alımından en az 12 saat sonra ortaya çıkar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; regürgitasyonda materyal mideye ulaşmadığından pH >= 7'dir, safra içermez ve gıdadan hemen sonra çıkarılır (Slayt 20).",
            "celdirici_analizi": "A, C ve D şıkları kusma ve mide patolojilerinin özellikleridir."
        },
        "slayt_no": 20,
        "zorluk_derecesi": "kolay",
        "etiketler": ["regurgitasyon", "kusma_farki", "pH"]
    },
    {
        "soru_id": "mcq_sind_016",
        "soru_metni": "Regürgitasyon ve öksürük şikayetiyle getirilen bir köpeğin lateral toraks grafisinde dilate özefagusun trakeayı ventrale itmesi ve trakea dorsal duvarının belirginleşmesi hangi patognomonik radyolojik bulgudur?",
        "secenekler": {
            "A": "Trakeal strip bulgusu",
            "B": "Ters C (Popeye) bulgusu",
            "C": "Hedef tahtası bulgusu",
            "D": "Pilorik gürz belirtisi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; megaözefagusta özefagus içi gaz ve ventral yer değiştirme sonucu trakeanın dorsal sınırının netleşmesi 'Trakeal Strip Bulgusu' olarak adlandırılır (Slayt 23).",
            "celdirici_analizi": "B şıkkı GDV'ye; C şıkkı intestinal invaginasyona aittir."
        },
        "slayt_no": 23,
        "zorluk_derecesi": "orta",
        "etiketler": ["radyoloji", "trakeal_strip", "megaozefagus"]
    },
    {
        "soru_id": "mcq_sind_017",
        "soru_metni": "Midenin fonksiyonel anatomisi dikkate alındığında, alınan gıdanın miktarına bağlı olarak genişleyip depo görevi gören mide kısımları hangileridir?",
        "secenekler": {
            "A": "Pilorus ve duodenal ampul",
            "B": "Fundus ve Korpus (Body)",
            "C": "Sadece pilorik antrum",
            "D": "Kardiya ve özefagal sfinkter"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; midenin Fundus ve Korpus bölgeleri alınan gıda miktarına bağlı olarak relakse olup genişleyerek depo işlevi görür (Slayt 26, 27).",
            "celdirici_analizi": "Antrum gıdaları öğütüp parçalayan kalın kaslı kısımdır; pilor ise boşalmayı denetler."
        },
        "slayt_no": 27,
        "zorluk_derecesi": "kolay",
        "etiketler": ["anatomi", "mide", "fundus"]
    },
    {
        "soru_id": "mcq_sind_018",
        "soru_metni": "Mide mukozasında yer alan Parietal Hücrelerin temel sekresyon ürünleri hangi seçenekte doğru verilmiştir?",
        "secenekler": {
            "A": "Pepsinojen ve gastrin",
            "B": "Hidroklorik asit (HCl) ve İntrinsik Faktör",
            "C": "Histamin ve somatostatin",
            "D": "Mukus ve bikarbonat"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; parietal hücreler lümene HCl salgılar ve B12 emilimi için şart olan intrinsik faktörü üretir (Slayt 28, 29).",
            "celdirici_analizi": "Pepsinojeni Chief hücreleri, gastrini G hücreleri, histamini ECL hücreleri salgılar."
        },
        "slayt_no": 29,
        "zorluk_derecesi": "kolay",
        "etiketler": ["mide_hucreleri", "parietal_hucre", "HCl"]
    },
    {
        "soru_id": "mcq_sind_019",
        "soru_metni": "Midede protein sindirimini başlatan pepsinojen enzim öncülü hangi mide hücreleri tarafından salgılanır?",
        "secenekler": {
            "A": "Parietal hücreler",
            "B": "Şef (Chief) hücreler",
            "C": "Enterokromafin benzeri (ECL) hücreler",
            "D": "G hücreleri"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; pepsinojen şef (chief) hücreleri tarafından lümene salgılanır ve asit ortamda aktif pepsine dönüşür (Slayt 29).",
            "celdirici_analizi": "A şıkkı asit salgılar; C şıkkı histamin salgılar; D şıkkı gastrin hormonunu kana verir."
        },
        "slayt_no": 29,
        "zorluk_derecesi": "kolay",
        "etiketler": ["mide_hucreleri", "chief_hucre", "pepsinojen"]
    },
    {
        "soru_id": "mcq_sind_020",
        "soru_metni": "Parietal hücrelerin bazolateral membranında histamin bağlanarak asit salgısını artıran reseptör tipi hangisidir?",
        "secenekler": {
            "A": "H1 histamin reseptörü",
            "B": "H2 histamin reseptörü",
            "C": "M3 muskarinik reseptör",
            "D": "CCKB kolesistokinin reseptörü"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; histamin parietal hücre üzerindeki H2 reseptörüne bağlanarak Gs/cAMP yolu üzerinden proton pompasını uyarır (Slayt 30).",
            "celdirici_analizi": "H1 alerjiyle ilişkilidir; M3 vagal asetilkolin reseptörüdür; CCKB gastrin reseptörüdür."
        },
        "slayt_no": 30,
        "zorluk_derecesi": "orta",
        "etiketler": ["farmakoloji", "H2_reseptor", "asit_salgisi"]
    },
    {
        "soru_id": "mcq_sind_021",
        "soru_metni": "Parietal hücrenin lümene proton (H+) pompalayan H+/K+ ATPase enzimini geri dönüşümsüz olarak inhibe eden ilaç grubu hangisidir?",
        "secenekler": {
            "A": "H2 reseptör blokörleri (Famotidin)",
            "B": "Proton Pompa İnhibitörleri (Omeprazol)",
            "C": "M1 antimuskarinikler (Atropin)",
            "D": "Dopamin D2 antagonistleri (Metoklopramid)"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Omeprazol, Pantoprazol gibi Proton Pompa İnhibitörleri doğrudan H+/K+ ATPase pompasını bloke eder (Slayt 30).",
            "celdirici_analizi": "Famotidin H2 reseptörünü bloke eder; atropin M3'ü engeller; metoklopramid prokinetiktir."
        },
        "slayt_no": 30,
        "zorluk_derecesi": "orta",
        "etiketler": ["farmakoloji", "omeprazol", "proton_pompasi"]
    },
    {
        "soru_id": "mcq_sind_022",
        "soru_metni": "Gastrik mukozal bariyerin korunmasında, mikrosirkülasyonun sürdürülmesinde ve mukus-bikarbonat salgılanmasında kilit rol oynayan koruyucu moleküller hangileridir?",
        "secenekler": {
            "A": "Prostaglandinler (PGE2 ve PGI2)",
            "B": "Lökotrienler (LTB4)",
            "C": "Tromboksan A2 (TXA2)",
            "D": "İnterlökin-6 (IL-6)"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; PGE2 ve PGI2 mukus tabakasını kalınlaştırır, bikarbonat salgısını artırır ve mukozal kan akımını temin eder (Slayt 32).",
            "celdirici_analizi": "NSAID ilaçların gastrik ülsere yol açmasının nedeni koruyucu PGE2 ve PGI2 sentezini baskılamalarıdır."
        },
        "slayt_no": 32,
        "zorluk_derecesi": "orta",
        "etiketler": ["mide_bariyeri", "prostaglandin"]
    },
    {
        "soru_id": "mcq_sind_023",
        "soru_metni": "Kedi ve köpeklerde kusmanın klinik olarak 'Akut Kusma' kabul edilmesi için süre sınırı nedir?",
        "secenekler": {
            "A": "12 saat içinde kesilmesi",
            "B": "5 - 7 gün boyunca devam edip kesilmesi",
            "C": "En az 30 gün boyunca sürmesi",
            "D": "Sadece aşı uygulamasından sonraki 1 saatte görülmesi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kusma 5-7 gün boyunca devam edip kesiliyorsa akut kusma; 5-7 günden uzun sürüyorsa kronik kusma kabul edilir (Slayt 34).",
            "celdirici_analizi": "Diyarede bu eşik süre 14 gündür (akut vs kronik diyare)."
        },
        "slayt_no": 34,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kusma", "akut_kusma"]
    },
    {
        "soru_id": "mcq_sind_024",
        "soru_metni": "Üremik toksinler, endotoksinler, hepatotoksinler, apomorfin ve ksilazin gibi ajanlar kusma merkezini hangi yolak üzerinden uyarırlar?",
        "secenekler": {
            "A": "Gastrointestinal lokal nöral gerilme yolağı",
            "B": "Kemoreseptör Tetikleme Bölgesi (CRTZ) üzerinden humoral yolak",
            "C": "Sadece periferik sempatik deri sinirleri",
            "D": "Vestibüler iç kulak denge çekirdekleri"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kanda dolaşan ematojenik/toksik ajanlar doğrudan kan-beyin bariyeri dışındaki CRTZ'yi uyararak humoral yoldan kusmayı tetikler (Slayt 35).",
            "celdirici_analizi": "A şıkkı obstrüksiyon ve lokal hasarda devreye giren nöral yolaktır."
        },
        "slayt_no": 35,
        "zorluk_derecesi": "orta",
        "etiketler": ["kusma_fizyolojisi", "CRTZ", "humoral_yolak"]
    },
    {
        "soru_id": "mcq_sind_025",
        "soru_metni": "Kusma refleksi sürecinde hipersalivasyon, mide-özefagus motilitesinde azalma ve proksimal ince bağırsağın retrograd motilitesinde artış kusmanın hangi fazıdır?",
        "secenekler": {
            "A": "FAZ 1 (Bulantı / Erken evre)",
            "B": "FAZ 2 (Öğürme evresi)",
            "C": "FAZ 3 (Kusma / Ejektif evre)",
            "D": "Refrakter dönem"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Faz 1 hipersalivasyon ve duodenal içeriğin retrograd mideye itilmesiyle karakterizedir. Faz 2 öğürmedir, Faz 3 ise atılmadır (Slayt 36).",
            "celdirici_analizi": "Faz 2 abdominal kasların kasılmasıdır; Faz 3 mide içeriğinin dışarı çıkışıdır."
        },
        "slayt_no": 36,
        "zorluk_derecesi": "orta",
        "etiketler": ["kusma_fazlari", "faz_1"]
    },
    {
        "soru_id": "mcq_sind_026",
        "soru_metni": "Akut kusma tedavisinde kullanılan NK1 reseptör antagonisti güçlü antiemetik olan 'Maropitant'ın (Cerenia) subkutan (SQ) veya intravenöz (IV) kullanım dozu nedir?",
        "secenekler": {
            "A": "0.1 mg/kg haftada bir",
            "B": "1 mg/kg SQ veya IV günde 1 kez (q24h)",
            "C": "10 mg/kg günde 4 kez",
            "D": "25 mg/kg oral her 6 saatte bir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Maropitant dozu parenteral (SQ/IV) yolla 1 mg/kg q24h; oral yolla ise 2 mg/kg q24h'dir (Slayt 39, 126).",
            "celdirici_analizi": "A, C ve D şıklarındaki dozlar hatalıdır (10 ve 25 mg/kg aşırı toksiktir)."
        },
        "slayt_no": 39,
        "zorluk_derecesi": "orta",
        "etiketler": ["antiemetik", "maropitant", "doz"]
    },
    {
        "soru_id": "mcq_sind_027",
        "soru_metni": "Kusulan içeriğin kanlı olması veya kan kusulması olarak tanımlanan ve genellikle 'kahve telvesi' görünümünde olan klinik tablo hangisidir?",
        "secenekler": {
            "A": "Hematüri",
            "B": "Hematoşezi",
            "C": "Hematemezis",
            "D": "Hemoptizi"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; kan kusulması hematemezistir; mide asidiyle temas eden kan sindirilerek kahve telvesi görünümü alır (Slayt 42).",
            "celdirici_analizi": "A şıkkı idrarda kan, B şıkkı dışkıda taze kan, D şıkkı solunumdan öksürükle kan gelmesidir."
        },
        "slayt_no": 42,
        "zorluk_derecesi": "kolay",
        "etiketler": ["hematemezis", "tanim"]
    },
    {
        "soru_id": "mcq_sind_028",
        "soru_metni": "Hematemezis değerlendirmesinde hekimin 'psödo-hematemezis' yanılgısına düşmemesi için dikkat etmesi gereken önemli durum nedir?",
        "secenekler": {
            "A": "Oral boşluk veya solunum sisteminden yutulan kanın bir süre sonra kusulması",
            "B": "Hayvanın sadece safra boyalı kusmuk çıkarması",
            "C": "Kusmuğun pH değerinin 9'un üzerinde ölçülmesi",
            "D": "Hematokrit değerinin %35 seviyesinde olması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; ağız veya burun/solunum kanamasını yutan hayvanlar daha sonra bu kanı kusabilirler; bu durum gerçek hematemezis sayılmaz (Slayt 42).",
            "celdirici_analizi": "B, C ve D şıkları yutulan kan uyarısı ile ilgili değildir."
        },
        "slayt_no": 42,
        "zorluk_derecesi": "orta",
        "etiketler": ["hematemezis", "klinik_ayrim"]
    },
    {
        "soru_id": "mcq_sind_029",
        "soru_metni": "Kedi ve köpeklerde 'Kronik Diyare' tanımı için ishalin en az kaç günden uzun sürmesi gerekir?",
        "secenekler": {
            "A": "3 gün",
            "B": "7 gün",
            "C": "14 gün",
            "D": "60 gün"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; 14 güne kadar devam eden diyareler akut, 14 günden uzun süren diyareler kronik diyare kabul edilir (Slayt 44).",
            "celdirici_analizi": "Kusmada bu süre eşiği 5-7 gündür; diyarede ise 14 gündür."
        },
        "slayt_no": 44,
        "zorluk_derecesi": "kolay",
        "etiketler": ["diyare", "kronik_diyare", "sure"]
    },
    {
        "soru_id": "mcq_sind_030",
        "soru_metni": "İnce bağırsak ishali ile kalın bağırsak ishali karşılaştırıldığında hangisi İNCE BAĞIRSAK İSHALİNİN özelliğidir?",
        "secenekler": {
            "A": "Dışkıda çoğu zaman jöle kıvamında bol mukus bulunması",
            "B": "Kilo kaybının yaygın görülmesi ve dışkı miktarının genellikle artması",
            "C": "Dışkılama sıklığının günde 10-15 kez gibi aşırı artması",
            "D": "Dışkılama sırasında sürekli şiddetli tenesmus (ıkınma) olması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ince bağırsakta sindirim ve emilim bozulduğu için kilo kaybı yaygındır ve dışkı hacmi artar. Mukus ve tenesmus kalın bağırsağa özgüdür (Slayt 45).",
            "celdirici_analizi": "A, C ve D seçenekleri kalın bağırsak ishalinin belirteçleridir."
        },
        "slayt_no": 45,
        "zorluk_derecesi": "kolay",
        "etiketler": ["ince_bagirsak_ishali", "karsilastirma"]
    },
    {
        "soru_id": "mcq_sind_031",
        "soru_metni": "Dışkıda taze, sindirilmemiş kırmızı kan bulunması tablosuna ne ad verilir?",
        "secenekler": {
            "A": "Melena",
            "B": "Hematoşezi",
            "C": "Hemotorkas",
            "D": "Hematüri"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; dışkıda sindirilmemiş taze kırmızı kan bulunması hematoşezi olarak adlandırılır ve alt GI kanamayı gösterir (Slayt 48).",
            "celdirici_analizi": "Melena sindirilmiş siyah kandır; hematüri idrarda kandır; hemotoraks göğüste kandır."
        },
        "slayt_no": 48,
        "zorluk_derecesi": "kolay",
        "etiketler": ["hematosezi", "tanim"]
    },
    {
        "soru_id": "mcq_sind_032",
        "soru_metni": "Dışkıda sindirilmiş siyah, katran renkli kan bulunması (Melena) öncelikle hangi bölgedeki kanamaları işaret eder?",
        "secenekler": {
            "A": "Anüs ve anal kese bölgesi",
            "B": "Rektum ve inen kolon",
            "C": "Üst Gastrointestinal Kanal (mide, duodenum)",
            "D": "Sadece idrar kesesi mukozası"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; kan sindirim enzimleri ve asitle temas edip sindirildiğinde siyahlaşır; bu nedenle Melena Üst GI kanamayı işaret eder (Slayt 47).",
            "celdirici_analizi": "A ve B şıklarındaki lezyonlar sindirilmemiş taze kırmızı kan (hematoşezi) yapar."
        },
        "slayt_no": 47,
        "zorluk_derecesi": "kolay",
        "etiketler": ["melena", "ust_GI"]
    },
    {
        "soru_id": "mcq_sind_033",
        "soru_metni": "Dışkı ŞEKİLLİ ve normal kıvamdayken dışkı üzerinde taze kan (hematoşezi) görülmesi durumunda hangisi öncelikli etiyolojik nedenlerden biridir?",
        "secenekler": {
            "A": "Ekzokrin pankreas yetersizliği (EPI)",
            "B": "Rektal polip, perianal fistül veya anal kese yangısı",
            "C": "Şiddetli parvoviral enterit",
            "D": "Histoplazmozis kaynaklı yaygın granülomatöz kolit"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; dışkı şekilli ise kanama rektal polip, anal kese, perianal fistül veya sert dışkı travmasına bağlıdır (Slayt 49).",
            "celdirici_analizi": "Parvo, histoplazmozis ve EPI yumuşak/sulu ishalli dışkıda hematoşez veya melena yapar."
        },
        "slayt_no": 49,
        "zorluk_derecesi": "orta",
        "etiketler": ["hematosezi", "anal_kese", "rektal_polip"]
    },
    {
        "soru_id": "mcq_sind_034",
        "soru_metni": "Dışkılama esnasında ağrı veya zorlanma duyulması ile rektal irritasyona bağlı tekrarlayan dışkılama/ıkınma eğilimi sırasıyla hangi terimlerdir?",
        "secenekler": {
            "A": "Diskezi - Tenesmus",
            "B": "Tenesmus - Diskezi",
            "C": "Konstipasyon - Obstipasyon",
            "D": "Disfaji - Odinofaji"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; dışkılama esnasında ağrı/zorlanma Diskezi; sürekli ıkınma eğilimi ise Tenesmustur (Slayt 50).",
            "celdirici_analizi": "B şıkkı tersidir; D şıkkı yutma ile ilgilidir."
        },
        "slayt_no": 50,
        "zorluk_derecesi": "kolay",
        "etiketler": ["terminoloji", "diskezi", "tenesmus"]
    },
    {
        "soru_id": "mcq_sind_035",
        "soru_metni": "Ağız mukozasında dilin inflamasyonuna verilen özel tıbbi terim hangisidir?",
        "secenekler": {
            "A": "Gingivitis",
            "B": "Glossitis",
            "C": "Palatitis",
            "D": "Stomatitis"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; dilin inflamasyonu Glossitis, diş etininki Gingivitis, damağınki Palatitis, tüm ağız boşluğununkisi Stomatitistir (Slayt 53).",
            "celdirici_analizi": "A şıkkı diş eti, C şıkkı damak, D şıkkı genel ağız boşluğudur."
        },
        "slayt_no": 53,
        "zorluk_derecesi": "kolay",
        "etiketler": ["agiz_hastaliklari", "glossitis"]
    },
    {
        "soru_id": "mcq_sind_036",
        "soru_metni": "Kedilerde dilde ve damakta ağrılı vezikül ve ülserlerle karakterize stomatitise en sık yol açan viral enfeksiyon hangisidir?",
        "secenekler": {
            "A": "Feline Calicivirus",
            "B": "Canine Parvovirus",
            "C": "Kuduz virüsü",
            "D": "Bovine Viral Diarrhea Virüsü"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kedilerde dilde ülser ve stomatitiste birincil viral etken Feline Calicivirus'tür (Slayt 54, 58).",
            "celdirici_analizi": "B şıkkı köpeğindir; C kuduzdur; D sığırlara aittir."
        },
        "slayt_no": 54,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kedi", "calicivirus", "stomatitis"]
    },
    {
        "soru_id": "mcq_sind_037",
        "soru_metni": "Stomatitli bir hayvanda ağız muayenesi yapılırken hasta ağrı nedeniyle muayeneye kesinlikle izin vermiyorsa en doğru yaklaşım nedir?",
        "secenekler": {
            "A": "Muayeneden vazgeçip hastayı eve göndermek",
            "B": "Hafif sedasyon altında detaylı oral muayene yapmak",
            "C": "Zorla ağzı tahta kamalarla açmaya çalışmak",
            "D": "Radyografi çekmeden doğrudan dişleri çekmek"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ağrısı yoğun olan ve oral muayeneye izin vermeyen vakalarda lezyonların tespiti için hafif sedasyon altında muayene şarttır (Slayt 56).",
            "celdirici_analizi": "A ve C şıkları hekimlik etiğine ve hasta güvenliğine aykırıdır."
        },
        "slayt_no": 56,
        "zorluk_derecesi": "kolay",
        "etiketler": ["oral_muayene", "sedasyon"]
    },
    {
        "soru_id": "mcq_sind_038",
        "soru_metni": "Kedi Plazmositik Lenfositik Gingivitis-Stomatitis-Farengitis tablosunda lezyonlar ağızda en karakteristik olarak nereye yerleşir?",
        "secenekler": {
            "A": "Sadece alt çene kesici diş etlerinde tek tük papüller",
            "B": "Glossofarengeal ark boyunca simetrik proliferatif ve ülseratif lezyonlar",
            "C": "Sert damağın kranial üçte birinde tek fokal kist",
            "D": "Burun boşluğunun vestibüler girişinde"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; glossofarengeal ark boyunca (boğaz kavsi) proliferatif, parlak kırmızı, karnabahar benzeri yangısal lezyonlar tipiktir (Slayt 63).",
            "celdirici_analizi": "A, C ve D şıkları hastalığın karakteristik anatomik yerleşimini yansıtmaz."
        },
        "slayt_no": 63,
        "zorluk_derecesi": "orta",
        "etiketler": ["kedi_stomatit", "glossofarengeal_ark"]
    },
    {
        "soru_id": "mcq_sind_039",
        "soru_metni": "Plazmositik lenfositik stomatitli kedilerin lezyon biyopsisinde mikroskobik olarak hangi hücrelerin yoğun infiltrasyonu saptanır?",
        "secenekler": {
            "A": "Sadece eritrositler ve trombositler",
            "B": "Plazma hücreleri ve lenfositler",
            "C": "Epitelyal keratin kistleri ve melanositler",
            "D": "Saf nötrofil ve osteoblast kümeleri"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; hastalığın adından da anlaşılacağı üzere mikroskopide mukoza lamina propriasında plazma hücreleri ve lenfositler görülür (Slayt 64).",
            "celdirici_analizi": "Vakaların %40'ında kanda lökositoz da saptanır."
        },
        "slayt_no": 64,
        "zorluk_derecesi": "kolay",
        "etiketler": ["biyopsi", "plazma_hucresi", "lenfosit"]
    },
    {
        "soru_id": "mcq_sind_040",
        "soru_metni": "Stomatitisli kedilerde uzun süreli iyileşme ve hastalığın uzun dönemli kontrolünde 'altın standart' kabul edilen radikal cerrahi sağaltım hangisidir?",
        "secenekler": {
            "A": "Sadece dil papillalarının lazerle koterize edilmesi",
            "B": "Tüm premolar ve molar dişlerin (kısmi) veya tüm dişlerin çekilmesi (tam ekstraksiyon)",
            "C": "Mandibula kemiğinin tamamen kesilerek çıkarılması",
            "D": "Tükürük kanallarının cerrahi olarak bağlanması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; plak birikimi ve periodontal antijenleri tamamen ortadan kaldırmak için premolar/molar ya da tüm dişlerin çekimi altın standarttır (Slayt 65).",
            "celdirici_analizi": "A, C ve D şıkları uygulanan standart tedavi yöntemleri değildir."
        },
        "slayt_no": 65,
        "zorluk_derecesi": "orta",
        "etiketler": ["stomatitis", "dis_cekimi", "altin_standart"]
    },
    {
        "soru_id": "mcq_sind_041",
        "soru_metni": "Köpeklerde farenjitis ve tonsillitise en sık eşlik eden veya predispoze olan primer faktörler hangileridir?",
        "secenekler": {
            "A": "Kusma ve regürgitasyon sonrası temas eden asidik sekresyonlar ve viral enfeksiyonlar",
            "B": "Aşırı miktarda havuç ve marul tüketilmesi",
            "C": "Yalnızca hipokalsemiye bağlı kas kasılmaları",
            "D": "Genel anestezi uygulanmamış olması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; farenjitis sıklıkla kusma/regürgitasyon sonrası mukozanın kimyasal tahrişi veya viral enfeksiyonlarla sekonder ortaya çıkar (Slayt 66).",
            "celdirici_analizi": "B, C ve D şıkları farenjitis etiyolojisiyle ilgisizdir."
        },
        "slayt_no": 66,
        "zorluk_derecesi": "kolay",
        "etiketler": ["farenjitis", "tonsillitis"]
    },
    {
        "soru_id": "mcq_sind_042",
        "soru_metni": "Köpeklerde tükürük bezlerinin yangısında (Sialadenitis) en sık etkilenen tükürük bezi hangisidir?",
        "secenekler": {
            "A": "Parotis tükürük bezi",
            "B": "Mandibular tükürük bezi",
            "C": "Sublingual bez",
            "D": "Zigomatik bez"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; sialadenitiste köpeklerde en sık Mandibular bezler etkilenir (Slayt 68).",
            "celdirici_analizi": "Zigomatik bez daha az etkilenir ancak strabismus yapmasıyla meşhurdur."
        },
        "slayt_no": 68,
        "zorluk_derecesi": "orta",
        "etiketler": ["sialadenitis", "mandibular_bez"]
    },
    {
        "soru_id": "mcq_sind_043",
        "soru_metni": "Bir köpekte şaşılık (strabismus) ve ağız açmaya karşı şiddetli isteksizlik saptandığında öncelikle hangi tükürük bezinin yangısı (sialadenitis) düşünülmelidir?",
        "secenekler": {
            "A": "Mandibular sialadenitis",
            "B": "Zigomatik sialadenitis",
            "C": "Sublingual ranula",
            "D": "Parotis kanalı kisti"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; zigomatik tükürük bezinin yangısı retrobulbar alana baskı yaparak strabismusa ve ağız açarken şiddetli ağrıya yol açar (Slayt 68).",
            "celdirici_analizi": "Mandibular bez çene altında şişlik yapar; ranula dil altında kisttir."
        },
        "slayt_no": 68,
        "zorluk_derecesi": "orta",
        "etiketler": ["zigomatik_bez", "strabismus", "sialadenitis"]
    },
    {
        "soru_id": "mcq_sind_044",
        "soru_metni": "Boxer ırkı köpeklerde diş etlerinde sıkça karşılaşılan benign (iyi huylu) hiperplastik proliferatif kitle hangisidir?",
        "secenekler": {
            "A": "Malign melanoma",
            "B": "Fibromatöz epulis",
            "C": "Skuamöz hücreli karsinom",
            "D": "Osteosarkom"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; özellikle Boxer ırkı köpeklerde diş etlerini tutan fibromatöz epulisler çok yaygındır (Slayt 69, 74).",
            "celdirici_analizi": "Melanom, SCC ve osteosarkom yüksek dereceli malign tümörlerdir."
        },
        "slayt_no": 69,
        "zorluk_derecesi": "orta",
        "etiketler": ["epulis", "boxer", "oral_tumor"]
    },
    {
        "soru_id": "mcq_sind_045",
        "soru_metni": "Kedilerde ağız boşluğunda görülen oral tümörlerin biyolojik davranışı hakkında hangisi KESİNLİKLE DOĞRUDUR?",
        "secenekler": {
            "A": "Oral tümörlerin %95'inden fazlası maligndir ve en sık Skuamöz Hücreli Karsinom (SCC) görülür",
            "B": "Kedilerde görülen tümörlerin tamamı iyi huylu olup cerrahiye gerek duyulmaz",
            "C": "En sık görülen tümör kemoterapiye tam yanıt veren benign papillomdur",
            "D": "Kedilerde oral kitleler daima diş tartarı temizliğiyle kendiliğinden geriler"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kedilerde oral tümörlerin %95-100'ü maligndir ve bunların en büyük kısmını invaziv Skuamöz Hücreli Karsinom (SCC) oluşturur (Slayt 69).",
            "celdirici_analizi": "B, C ve D şıkları oral tümörlerin agresif ve ölümcül karakteriyle çelişen yanlış ifadelerdir."
        },
        "slayt_no": 69,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kedi", "oral_tumor", "SCC", "malign"]
    }
]

print(f"Bölüm 1 hazır: {len(QUESTIONS_PART1)} soru.")
