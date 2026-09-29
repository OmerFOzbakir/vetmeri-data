# -*- coding: utf-8 -*-
"""
Sindirim Sistemi - Çoktan Seçmeli Sorular (Bölüm 3: 91 - 140)
Kapsam: Slayt 140 - 240 (GDV Patofizyolojisi, Aritmiler, L-laktat, Dekompresyon, Mide Tümörleri, Parvo/FIP, PLE/Lenfanjiyektazi, Vaka Analizi: Myasthenia Gravis & Tensilon)
"""

QUESTIONS_PART3 = [
    {
        "soru_id": "mcq_sind_091",
        "soru_metni": "Gastrik Dilatasyon ve Volvulus (GDV) tablosunda mide anatomik olarak genellikle hangi yönde ve kaç derece döner?",
        "secenekler": {
            "A": "Saat yönünün tersine 45 derece",
            "B": "Genelde saat yönünde 90 - 360 derece",
            "C": "Sadece dorsale doğru 180 derece ters takla",
            "D": "Pilor sola, fundus sağa doğru 10 derece"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; GDV olgularında mide çoğunlukla saat yönünde 90 ile 360 derece arasında aksiyel rotasyona uğrar (Slayt 142).",
            "celdirici_analizi": "Dönme ekseni ve yönü saat yönündedir; dekompresyonda sonda takılırken direnç gelirse bu yüzden hafif saat yönü tersine manevra yapılır."
        },
        "slayt_no": 142,
        "zorluk_derecesi": "orta",
        "etiketler": ["GDV", "rotasyon", "patofizyoloji"]
    },
    {
        "soru_id": "mcq_sind_092",
        "soru_metni": "GDV gelişen bir köpekte dalak damarlarının kısmen tıkanması ve splenik rotasyon sekonder olarak hangi organ patolojisine yol açar?",
        "secenekler": {
            "A": "Venöz konjesyon ve splenomegali (dalağın aşırı büyümesi ve nekrozu)",
            "B": "Pankreatik atrofi ve insülin eksikliği",
            "C": "Safra kesesi rüptürü",
            "D": "Böbrek taşları oluşumu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; gastro-splenik ligament ile mideye bağlı olan dalak midenin dönmesiyle birlikte döner, venöz staz ve masif splenomegali/nekroz şekillenir (Slayt 142).",
            "celdirici_analizi": "Bu nedenle birçok GDV cerrahisinde splenektomi (dalak alımı) gerekebilir."
        },
        "slayt_no": 142,
        "zorluk_derecesi": "orta",
        "etiketler": ["GDV", "dalak", "splenomegali"]
    },
    {
        "soru_id": "mcq_sind_093",
        "soru_metni": "GDV olgularında karaciğer portal venöz kan akımının kesilmesi sonucu endotoksik şoku tetikleyen temel immün yetersizlik nedir?",
        "secenekler": {
            "A": "Karaciğer retiküloendotelyal sisteminin (RES) gram (-) bakteriyel endotoksinleri nötralize edememesi",
            "B": "Karaciğerin safra tuzu üretememesi",
            "C": "Albumin üretiminin 1 saatte sıfıra inmesi",
            "D": "Kandaki fibrinojenin tamamen tükenmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; portal perfüzyon kesilince karaciğer Kupffer hücreleri (RES) bağırsaktan gelen gram negatif bakteriyel endotoksinleri temizleyemez ve endotoksik şok gelişir (Slayt 143).",
            "celdirici_analizi": "Bu durum mevcut hipovolemik şoku katlayarak kardiyovasküler çöküşe yol açar."
        },
        "slayt_no": 143,
        "zorluk_derecesi": "zor",
        "etiketler": ["GDV", "endotoksemi", "karaciger_RES"]
    },
    {
        "soru_id": "mcq_sind_094",
        "soru_metni": "GDV tanısında yetersiz doku perfüzyonunu ve anaerobik metabolizmayı gösteren, preoperatif gastrik nekrozun kuvvetli belirteci olan parametre hangisidir?",
        "secenekler": {
            "A": "Serum L-laktat konsantrasyonu",
            "B": "Kan üre azotu (BUN)",
            "C": "Serum kalsiyum düzeyi",
            "D": "Plazma kolesterolü"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; doku hipoksisi sonucu yükselen L-laktat, gastrik nekrozun ve operasyonel mortalite riskinin en değerli biyobelirtecidir (Slayt 145, 147).",
            "celdirici_analizi": "BUN, kalsiyum ve kolesterol nekrozu spesifik olarak yansıtmaz."
        },
        "slayt_no": 147,
        "zorluk_derecesi": "orta",
        "etiketler": ["L_laktat", "GDV", "biyobelirtec"]
    },
    {
        "soru_id": "mcq_sind_095",
        "soru_metni": "GDV'li köpeklerde cerrahi öncesi plazma L-laktat düzeyinin hangi kritik eşik değerinin üzerinde olması %88 sensitivite ile gastrik nekrozu işaret eder?",
        "secenekler": {
            "A": "> 6 mmol/L",
            "B": "> 0.5 mmol/L",
            "C": "> 20 mmol/L",
            "D": "> 100 mmol/L"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; plazma L-laktat konsantrasyonunun >6 mmol/L olması %88 duyarlılık ve %61 özgüllükle gastrik nekrozu gösterir (Slayt 148, 161).",
            "celdirici_analizi": "L-laktat <4 mmol/L olanlarda sağkalım yüksek iken >6 mmol/L olanlarda nekroz ve komplikasyon çok yüksektir."
        },
        "slayt_no": 148,
        "zorluk_derecesi": "zor",
        "etiketler": ["L_laktat", "esik_deger", "gastrik_nekroz"]
    },
    {
        "soru_id": "mcq_sind_096",
        "soru_metni": "GDV'li bir köpeğe acil dekompresyon amacıyla orogastrik sonda takılırken sonda uzunluğu nereden nereye ölçülerek işaretlenmelidir?",
        "secenekler": {
            "A": "Burun ucundan omuz eklemine kadar",
            "B": "İnsisör (ön kesici) dişlerden son kostaya (son kaburga) kadar",
            "C": "Alt çene ucundan göğüs kemiğine kadar",
            "D": "Kulak tabanından kuyruk sokumuna kadar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; sonda insisör dişlerden son kaburgaya (kosta) kadar ölçülür, işaretlenir ve köpek sternal yatış pozisyonundayken dikkatle uygulanır (Slayt 151).",
            "celdirici_analizi": "A, C ve D şıklarındaki ölçümler mideye ulaşmak için ya çok kısa ya da çok uzundur."
        },
        "slayt_no": 151,
        "zorluk_derecesi": "kolay",
        "etiketler": ["orogastrik_sonda", "olcum", "dekompresyon"]
    },
    {
        "soru_id": "mcq_sind_097",
        "soru_metni": "Orogastrik sonda takılması sırasında sfinkterdeki direnç aşılamazsa acil gastrik dekompresyon için uygulanan alternatif cerrahi girişim hangisidir?",
        "secenekler": {
            "A": "Perkütan gastrosentez (trokarizasyon)",
            "B": "Acil trakeotomi",
            "C": "Rektal tüp uygulaması",
            "D": "Epidural anestezi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; sonda geçmezse sağ abdominal duvarda son kosta gerisinde perküsyonla belirlenen timpanik alandan bir kanül ile perkütan gastrosentez yapılır (Slayt 154).",
            "celdirici_analizi": "Bu işlemle mide gazı boşaltılarak intragastrik basınç düşürülür ve sonda geçişi kolaylaşır."
        },
        "slayt_no": 154,
        "zorluk_derecesi": "orta",
        "etiketler": ["gastrosentez", "trokarizasyon", "dekompresyon"]
    },
    {
        "soru_id": "mcq_sind_098",
        "soru_metni": "GDV geçiren köpeklerin yaklaşık %40'ında operasyon sonrasında ne zaman aritmi başlar?",
        "secenekler": {
            "A": "Operasyon bittikten hemen 5 dakika sonra",
            "B": "Genellikle postoperatif 12 - 36. saatlerde",
            "C": "Ameliyattan 3 ay sonra",
            "D": "Sadece dikişler alınırken 10. günde"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; reperfüzyon hasarı, miyokardiyal iskemi ve toksinler nedeniyle ventriküler aritmiler sıklıkla postop 12-36. saatler arasında patlak verir (Slayt 155).",
            "celdirici_analizi": "Bu nedenle hastalar ameliyat sonrası en az 48 saat sürekli EKG monitörizasyonunda tutulmalıdır."
        },
        "slayt_no": 155,
        "zorluk_derecesi": "orta",
        "etiketler": ["aritmi", "postoperatif_zaman", "GDV"]
    },
    {
        "soru_id": "mcq_sind_099",
        "soru_metni": "GDV'li köpeklerde postoperatif gelişen ventriküler taşiaritmilerin sağaltımında ilk tercih edilen antiaritmik ilaç ve dozu hangisidir?",
        "secenekler": {
            "A": "IV Lidokain (2 mg/kg yavaş bolus, 8 mg/kg doza kadar çıkılabilir)",
            "B": "Oral aspirin (10 mg/kg)",
            "C": "Subkutan atropin sülfat (1 mg/kg)",
            "D": "Yüksek doz kalsiyum glukonat bolusu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; ventriküler taşikardi ve PVC'lerde ilk tercih IV Lidokaindir (2 mg/kg bolus, gerekirse 8 mg/kg'a kadar) (Slayt 158).",
            "celdirici_analizi": "Lidokaine yanıt alınamazsa Prokainamid (10-15 mg/kg bolus veya infüzyon) kullanılır."
        },
        "slayt_no": 158,
        "zorluk_derecesi": "orta",
        "etiketler": ["lidokain", "antiaritmik", "GDV"]
    },
    {
        "soru_id": "mcq_sind_100",
        "soru_metni": "GDV cerrahisinde mide düzeltildikten sonra 'Gastropeksi' yapılmazsa nüks oranı ile yapıldığındaki nüks oranı sırasıyla nasıldır?",
        "secenekler": {
            "A": "Gastropeksi yapılmazsa nüks %0 ; yapılırsa nüks %100",
            "B": "Gastropeksi yapılmazsa nüks % 54.5 - 75.8 ; yapılırsa nüks % 4.5 - 6.6",
            "C": "Her iki durumda da nüks oranı tamamen aynıdır (%50)",
            "D": "Gastropeksi sadece kedilerde nüksü önler köpeklerde etkisizdir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; gastropeksi yapılmayanlarda nüks oranı %54.5-75.8 iken, gastropeksi yapılanlarda %4.5-6.6'ya düşer (Slayt 161).",
            "celdirici_analizi": "Bu dramatik fark nedeniyle gastropeksi GDV cerrahisinin vazgeçilmez temel basamağıdır."
        },
        "slayt_no": 161,
        "zorluk_derecesi": "kolay",
        "etiketler": ["gastropeksi", "nuks_orani", "istatistik"]
    },
    {
        "soru_id": "mcq_sind_101",
        "soru_metni": "Pilor stenozu (mide çıkış darlığı) olan genç hayvanlarda en karakteristik kusma paterni ve klinik davranış hangisidir?",
        "secenekler": {
            "A": "Damla damla safra kusma ve sudan korkma",
            "B": "Özellikle sütten kesilme sonrası katı gıda alımını takiben 'fışkıran tarzda' kusma ve kusulan içeriği tekrar yeme isteği",
            "C": "Sadece geceleri kuru öksürük nöbetleri",
            "D": "Kusma olmaksızın sadece mukuslu dışkılama"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; pilor darlığında mide içi basınç aşırı yükselir ve fışkırır tarzda (projektil) kusma görülür; kusmuk sindirilmemiş olduğundan hayvan tekrar yemeye isteklidir (Slayt 165).",
            "celdirici_analizi": "Brakisefalik köpek ırkları ve Siyam kedileri konjenital pilor stenozuna yatkındır."
        },
        "slayt_no": 165,
        "zorluk_derecesi": "orta",
        "etiketler": ["pilor_stenozu", "fiskiran_kusma"]
    },
    {
        "soru_id": "mcq_sind_102",
        "soru_metni": "Kontrastlı mide radyografisinde normalde baryum sülfatın midede kalma süresi 5-15 dakika iken, baryumun midede kaç saatten fazla kalması anormal gastrik retansiyonu belgeler?",
        "secenekler": {
            "A": "30 dakika",
            "B": "1 - 2 saat",
            "C": "12 - 24 saatten fazla kalması",
            "D": "3 gün"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; baryumun midede 12-24 saatten fazla kalması anormaldir ve belirgin bir mekanik veya fonksiyonel gastrik retansiyona işaret eder (Slayt 166).",
            "celdirici_analizi": "Normal mide boşalma süresi 30 dakikadan azdır."
        },
        "slayt_no": 166,
        "zorluk_derecesi": "orta",
        "etiketler": ["baryum", "gastrik_retansiyon", "radyoloji"]
    },
    {
        "soru_id": "mcq_sind_103",
        "soru_metni": "Köpeklerde en yaygın görülen gastrik neoplazi olup tüm mide tümörlerinin %47-72'sini oluşturan ve sıklıkla pilorik antruma yerleşen tümör hangisidir?",
        "secenekler": {
            "A": "Gastrik Adenokarsinoma",
            "B": "Liposarkom",
            "C": "Benign fibrom",
            "D": "Kavernöz hemanjiyom"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; köpeklerde en yaygın gastrik neoplazi Adenokarsinomadır; sıklıkla antrum ve küçük kurvatura yerleşir (Slayt 168).",
            "celdirici_analizi": "Akciğer, lenf nodu ve karaciğere çok hızlı metastaz yapar."
        },
        "slayt_no": 168,
        "zorluk_derecesi": "kolay",
        "etiketler": ["adenokarsinom", "mide_tumoru", "kopek"]
    },
    {
        "soru_id": "mcq_sind_104",
        "soru_metni": "Düz kas hücrelerinden köken alan, oldukça yavaş büyüyen ve sürekli İnsülin-benzeri Büyüme Faktörü (IGF) üreterek paraneoplastik hipoglisemi ve nöbetlere yol açan mide tümörü hangisidir?",
        "secenekler": {
            "A": "Gastrik Leiomyosarkoma",
            "B": "Mast hücre tümörü",
            "C": "Lenfosarkoma",
            "D": "Karsinoid tümör"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Leiomyosarkom IGF salgılayarak kanda glukozu aşırı düşürür (paraneoplastik hipoglisemi) ve epileptik nöbetlere neden olur (Slayt 168).",
            "celdirici_analizi": "Bu klinik tablo insülinoma ile karışabilir ancak kitle midededir."
        },
        "slayt_no": 168,
        "zorluk_derecesi": "orta",
        "etiketler": ["leiomyosarkom", "IGF", "paraneoplastik_hipoglisemi"]
    },
    {
        "soru_id": "mcq_sind_105",
        "soru_metni": "Hem kedilerde hem de köpeklerde tüm gastrointestinal kanalda EN ÇOK karşılaşılan neoplazi türü hangisidir?",
        "secenekler": {
            "A": "Lenfosarkoma (Alimentar Lenfoma)",
            "B": "Melanosarkom",
            "C": "Kondrosarkom",
            "D": "Schwannoma"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kedi ve köpeklerde tüm GI kanalın en yaygın tümörü Lenfosarkomdur (Lenfoma) (Slayt 168).",
            "celdirici_analizi": "Karaciğer, bölgesel lenf nodları, ince bağırsaklar ve kemik iliğine yoğun metastaz yapar."
        },
        "slayt_no": 168,
        "zorluk_derecesi": "kolay",
        "etiketler": ["lenfosarkom", "lenfoma", "GI_tumor"]
    },
    {
        "soru_id": "mcq_sind_106",
        "soru_metni": "Loperamid ve difenoksilat gibi motilite ve sekresyon baskılayıcı antidiyareik ajanlar hangi durumlarda KESİNLİKLE KULLANILMAMALIDIR?",
        "secenekler": {
            "A": "Obstrüksiyonlarda (bağırsak tıkanmalarında) ve enfeksiyöz enteritlerde",
            "B": "Sadece basit diyet değişikliği ishallerinde",
            "C": "Aşı öncesi rutin korumada",
            "D": "Her türlü ishalde güvenle kullanılır hiçbir kontrendikasyonu yoktur"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; loperamid motiliteyi durdurur; obstrüksiyonda rüptüre, enfeksiyöz enteritte ise toksinlerin ve bakterilerin lümende birikip sepsise yol açmasına neden olur (Slayt 175).",
            "celdirici_analizi": "Enfeksiyöz enteritlerde toksinlerin dışarı atılması engellenmemelidir."
        },
        "slayt_no": 175,
        "zorluk_derecesi": "orta",
        "etiketler": ["loperamid", "kontrendikasyon", "motilite"]
    },
    {
        "soru_id": "mcq_sind_107",
        "soru_metni": "Canine Parvovirus Tip-2 (CPV-2) virüsünün patogenezinde en belirgin hücresel hedef hangisidir?",
        "secenekler": {
            "A": "Mitotik aktivitesi yüksek olan hücreler (bağırsak kript epitelleri, kemik iliği, lenfoid doku)",
            "B": "Sadece miyelinli periferik motor sinirler",
            "C": "Mide parietal hücreleri",
            "D": "Göz kornea endotel hücreleri"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Parvovirüs yüksek mitotik aktiviteye sahip kript epitelini yıkarak hemorojik enterit, kemik iliğini yıkarak lökopeni/nötropeni yapar (Slayt 176).",
            "celdirici_analizi": "Kript epiteli yıkılınca villuslar dökülür ve bağırsak bariyeri çöker."
        },
        "slayt_no": 176,
        "zorluk_derecesi": "kolay",
        "etiketler": ["parvovirus", "mitotik_aktivite", "patogenez"]
    },
    {
        "soru_id": "mcq_sind_108",
        "soru_metni": "Canine Parvovirus ile intrauterin (anne karnında) veya doğumdan hemen sonra enfekte olan yavrularda gelişen fatal komplikasyon hangisidir?",
        "secenekler": {
            "A": "Akut Myokarditis",
            "B": "Hiatal herni",
            "C": "Diş minesi hipoplazisi",
            "D": "Megakolon"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; neonatal dönemde kalp kası hücreleri hızla bölündüğü için CPV miyokard hücrelerini enfekte eder ve akut myokarditise yol açar (Slayt 177).",
            "celdirici_analizi": "Bu yavrular enterit belirtisi göstermeden ani kalp yetmezliğiyle ölebilirler."
        },
        "slayt_no": 177,
        "zorluk_derecesi": "orta",
        "etiketler": ["parvovirus", "myokarditis", "intrauterin"]
    },
    {
        "soru_id": "mcq_sind_109",
        "soru_metni": "Parvoviral enteritli köpeklerde derin nötropeniyi düzeltmek ve kemik iliği granülosit üretimini uyarmak amacıyla kullanılan rekombinant sitokin hangisidir?",
        "secenekler": {
            "A": "Filgrastim (Human G-CSF)",
            "B": "İnsülin glargin",
            "C": "Eritropoietin",
            "D": "Oksitosin"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Filgrastim (G-CSF) nötropenik kritik olgularda nötrofil sayısını hızla yükselterek sepsisi engellemek için kullanılır (Slayt 179).",
            "celdirici_analizi": "Slayt 180'deki bilimsel çalışmada PIND-ORF'un klinik iyileşmeye katkı sağlamadığı gösterilmiştir."
        },
        "slayt_no": 179,
        "zorluk_derecesi": "orta",
        "etiketler": ["filgrastim", "G_CSF", "parvovirus_tedavi"]
    },
    {
        "soru_id": "mcq_sind_110",
        "soru_metni": "Gebe kedilerin Feline Panleukopenia (kedi gençlik hastalığı) canlı aşıları ile aşılanması veya intrauterin enfeksiyon yavrularda hangi kalıcı konjenital defekte yol açar?",
        "secenekler": {
            "A": "Serebellar Hipoplazi (Cerebellar hypoplasia)",
            "B": "Pilor stenozu",
            "C": "Portosistemik şant",
            "D": "Krikofaringeal aklazi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; virüs fötal dönemde hızla gelişen serebellum Purkinje ve granüler hücrelerini tahrip ederek Serebellar Hipoplazi ve ataksiye yol açar (Slayt 181).",
            "celdirici_analizi": "Bu nedenle gebe kedilere kesinlikle canlı modifiye aşı yapılmamalıdır."
        },
        "slayt_no": 181,
        "zorluk_derecesi": "kolay",
        "etiketler": ["FPV", "panleukopeni", "serebellar_hipoplazi"]
    },
    {
        "soru_id": "mcq_sind_111",
        "soru_metni": "Canine Coronavirus (CCV) enfeksiyonu Parvoviral enteritten (PVE) klinik ve hematolojik olarak hangi yönüyle ayrılır?",
        "secenekler": {
            "A": "Daha hafif sarı-portakal renkli ishal yapması ve PVE'nin aksine LÖKOPENİNİN NADİREN GÖRÜLMESİ",
            "B": "CCV'de daima felç gelişmesi",
            "C": "CCV'nin sadece 10 yaş üzeri köpeklerde görülmesi",
            "D": "PVE'nin aksine sadece kusma ile seyredip hiç ishal yapmaması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; CCV orta derecede sınırlı bir ishal yapar, kemik iliğini vurmadığı için lökopeni nadirdir; ancak parvo ile birlikte miks enfeksiyon mortaliteyi artırır (Slayt 182).",
            "celdirici_analizi": "PVE derin lökopeni ve kötü kokulu kanlı ishal ile karakterizedir."
        },
        "slayt_no": 182,
        "zorluk_derecesi": "orta",
        "etiketler": ["canine_coronavirus", "parvovirus_ayrimi", "lokopeni"]
    },
    {
        "soru_id": "mcq_sind_112",
        "soru_metni": "Kedilerde FIP (Feline Enfeksiyöz Peritonitis) hastalığının ortaya çıkış mekanizması hangisinde doğru açıklanmıştır?",
        "secenekler": {
            "A": "Feline Enterik Coronavirus'un (FECV) konakçı kedi içinde mutasyona uğrayarak FIPV'ye dönüşmesi",
            "B": "Kedinin doğrudan köpekten Parvovirüs kapması",
            "C": "Yalnızca çiğ balık tüketimine bağlı B1 vitamini eksikliği",
            "D": "Genel anestezi gazlarının immün sistemi felç etmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; yaygın ve hafif enterik seyreden FECV, makrofaj tropizmi kazandıran iç mutasyonla öldürücü FIPV'ye dönüşür (Slayt 183).",
            "celdirici_analizi": "B, C ve D şıklarının FIP patogeneziyle ilgisi yoktur."
        },
        "slayt_no": 183,
        "zorluk_derecesi": "kolay",
        "etiketler": ["FIP", "FECV", "mutasyon"]
    },
    {
        "soru_id": "mcq_sind_113",
        "soru_metni": "Nonefüziv (Kuru) FIP formunun en karakteristik klinik göz ve sinir sistemi bulguları hangileridir?",
        "secenekler": {
            "A": "Anterior üveitis, koryoretinitis, konvülsiyon ve nistagmus",
            "B": "Sadece kuru öksürük ve burun kanaması",
            "C": "Kör barsak torsiyonu",
            "D": "Tek taraflı tırnak kırılması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kuru FIP pyogranülomlarla seyreder; gözde anterior üveit/koryoretinit ve MSS tutulumunda nistagmus/konvülsiyon tipiktir (Slayt 185, 187).",
            "celdirici_analizi": "Bazen göz lezyonları kuru FIP'in tek klinik belirtisi olabilir."
        },
        "slayt_no": 187,
        "zorluk_derecesi": "orta",
        "etiketler": ["kuru_FIP", "uveit", "MSS_lezyonlari"]
    },
    {
        "soru_id": "mcq_sind_114",
        "soru_metni": "2 yaşından küçük genç kedilerde ikterus (sarılık) tablosunun en yaygın nedenlerinden biri hangisidir?",
        "secenekler": {
            "A": "Feline Enfeksiyöz Peritonitis (FIP)",
            "B": "Mide adenokarsinomu",
            "C": "Aspirin intoksikasyonu",
            "D": "Pilor stenozu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; FIP 2 yaşından küçük kedilerde hiperbilirubinemi ve ikterusun en yaygın nedenlerinden biridir (Slayt 186, 190).",
            "celdirici_analizi": "Bu artışa karaciğer tutulumu nedeniyle ALT ve ALP artışları da eşlik eder."
        },
        "slayt_no": 186,
        "zorluk_derecesi": "orta",
        "etiketler": ["FIP", "ikterus", "kedi_sarilik"]
    },
    {
        "soru_id": "mcq_sind_115",
        "soru_metni": "FIP şüpheli kedilerde serum veya efüzyon sıvısı Albümin/Globülin (A/G) oranının tanısal eşik değerleri nasıldır?",
        "secenekler": {
            "A": "A/G < 0.4 ise FIP olasılığı yüksek (%89 PPV) ; A/G > 0.8 ise FIP olmama olasılığı yüksektir",
            "B": "A/G > 2.0 ise FIP kesin tanıdır",
            "C": "A/G oranının FIP tanısında hiçbir değeri yoktur",
            "D": "A/G oranı sadece hemoglobin seviyesini gösterir"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; poliklonal hiperglobulinemi nedeniyle A/G oranı < 0.4 ise FIP olasılığı çok yüksektir, > 0.8 ise FIP dışlanır (Slayt 189, 192).",
            "celdirici_analizi": "Efüzyon sıvısındaki A/G oranı serumdakine göre tanısal açıdan daha da güvenilirdir."
        },
        "slayt_no": 189,
        "zorluk_derecesi": "zor",
        "etiketler": ["FIP", "albumin_globulin", "tani_kriteri"]
    },
    {
        "soru_id": "mcq_sind_116",
        "soru_metni": "Efüziv FIP hastalarında vücut boşluklarında biriken sıvının transudat-eksudat ayrımını yapmak amacıyla asetik asit ve distile su ile yapılan pratik test hangisidir?",
        "secenekler": {
            "A": "Rivalta Testi",
            "B": "Coombs Testi",
            "C": "Tensilon Testi",
            "D": "Schirmer Göz Testi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; 8 ml distile su + 1 damla %98 asetik asit + 1 damla efüzyon sıvısı damlatılarak duman/çökelti incelenen test Rivalta testidir (Slayt 191, 192).",
            "celdirici_analizi": "Coombs hemoliz içindir; Tensilon Myasthenia gravis içindir; Schirmer gözyaşı ölçer."
        },
        "slayt_no": 192,
        "zorluk_derecesi": "kolay",
        "etiketler": ["rivalta_testi", "FIP", "efuzyon"]
    },
    {
        "soru_id": "mcq_sind_117",
        "soru_metni": "Son yıllarda FIP tedavisinde çığır açan ve yüksek klinik iyileşme sağlayan nükleozid analoğu antiviral molekül hangisidir?",
        "secenekler": {
            "A": "GS-441524",
            "B": "Metoklopramid",
            "C": "Sukralfat",
            "D": "Levamizol"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; GS-441524 viral RNA polimerazı inhibe ederek hem ıslak hem kuru FIP'te %90'ın üzerinde sağkalım sağlayan antiviral moleküldür (Slayt 193, 194).",
            "celdirici_analizi": "Diğer şıklar semptomatik veya antiparaziter ilaçlardır."
        },
        "slayt_no": 193,
        "zorluk_derecesi": "kolay",
        "etiketler": ["GS441524", "FIP_tedavi", "antiviral"]
    },
    {
        "soru_id": "mcq_sind_118",
        "soru_metni": "Antihelmintik bir ilaç olan 'Pirantel pamoat' (10 mg/kg) ile ilgili klinik farmakolojik kural hangisidir?",
        "secenekler": {
            "A": "Özellikle Ascarid ve diğer nematodların tedavisinde etkilidir; Cestodlara (şeritlere) karşı ETKİSİ YOKTUR",
            "B": "Sadece tenyaları ve sestodları öldürür nematoda etki etmez",
            "C": "Sadece protozoon enfeksiyonlarında (Giardia) kullanılır",
            "D": "Kedilerde aşırı toksik olup asla kullanılamaz"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Pirantel pamoat nematodlara karşı çok etkilidir ancak cestodlara (Dipylidium vb.) hiçbir etkisi yoktur (Slayt 197).",
            "celdirici_analizi": "Cestod tedavisi için Prazikuantel (5 mg/kg) tercih edilmelidir."
        },
        "slayt_no": 197,
        "zorluk_derecesi": "orta",
        "etiketler": ["pirantel_pamoat", "nematod", "cestod"]
    },
    {
        "soru_id": "mcq_sind_119",
        "soru_metni": "Kedi ve köpeklerde tenya (Cestod - Dipylidium caninum) tedavisinde kullanılan 5 mg/kg dozundaki spesifik ilaç hangisidir?",
        "secenekler": {
            "A": "Prazikuantel (Piraziquantel)",
            "B": "Metronidazol",
            "C": "Omeprazol",
            "D": "Sukralfat"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Prazikuantel 5 mg/kg dozda sestodların tedavisinde altın standarttır (Slayt 197).",
            "celdirici_analizi": "Metronidazol protozoon/anaerob içindir; omeprazol asit baskılayıcıdır."
        },
        "slayt_no": 197,
        "zorluk_derecesi": "kolay",
        "etiketler": ["prazikuantel", "sestod", "tenya"]
    },
    {
        "soru_id": "mcq_sind_120",
        "soru_metni": "Özellikle barınak ve çoklu kedi ortamlarında kronik inatçı kalın bağırsak diyaresine yol açan kamçılı protozoon etkeni hangisidir?",
        "secenekler": {
            "A": "Tritrichomonas foetus",
            "B": "Dipylidium caninum",
            "C": "Toxocara canis",
            "D": "Spirocerca lupi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Tritrichomonas foetus kedilerde kronik kolit ve mukoid dışkılamanın önemli bir protozoal sebebidir (Slayt 198).",
            "celdirici_analizi": "Dipylidium şerittir; Toxocara nematoddur; Spirocerca özefagus parazitidir."
        },
        "slayt_no": 198,
        "zorluk_derecesi": "orta",
        "etiketler": ["tritrichomonas_foetus", "kedi_diyare"]
    },
    {
        "soru_id": "mcq_sind_121",
        "soru_metni": "Kedi ve köpeklerde kronik ince bağırsak diyaresi ve malabsorpsiyona yol açan Giardia enfeksiyonunun medikal sağaltım protokolü hangisidir?",
        "secenekler": {
            "A": "Metronidazol (25 mg/kg oral 5 gün) ve/veya Fenbendazol (50 mg/kg 3-5 gün)",
            "B": "Tek doz aspirin enjeksiyonu",
            "C": "Sadece loperamid şurup verilmesi",
            "D": "Genel anestezi altında mide lavajı"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Giardia tedavisinde 25 mg/kg metronidazol 5 gün veya 50 mg/kg fenbendazol 3-5 gün tek başına ya da kombine kullanılır (Slayt 198).",
            "celdirici_analizi": "B, C ve D şıklarının antiprotozoal etkinliği yoktur."
        },
        "slayt_no": 198,
        "zorluk_derecesi": "orta",
        "etiketler": ["giardia", "metronidazol", "fenbendazol"]
    },
    {
        "soru_id": "mcq_sind_122",
        "soru_metni": "Kedi ve köpeklerde en yaygın olarak teşhis edilen Kronik Yangısal Bağırsak Hastalığı (IBD) tipi hangisidir?",
        "secenekler": {
            "A": "Lenfositik - Plasmasitik Enteritis",
            "B": "Granülomatöz enteritis",
            "C": "Nötrofilik enterit",
            "D": "Fungal enterit"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Lenfositik-Plasmasitik Enteritis kedi ve köpeklerde en sık teşhis edilen kronik yangısal bağırsak hastalığıdır (Slayt 201).",
            "celdirici_analizi": "Biyopside lamina propriada yoğun lenfosit ve plazma hücre infiltrasyonu görülür."
        },
        "slayt_no": 201,
        "zorluk_derecesi": "kolay",
        "etiketler": ["IBD", "lenfositik_plasmasitik", "enteritis"]
    },
    {
        "soru_id": "mcq_sind_123",
        "soru_metni": "Kronik yangısal ince bağırsak hastalıklarında hipoalbüminemi geliştiğinde kedilerde neden köpeklere kıyasla asites (karında sıvı) daha nadir görülür?",
        "secenekler": {
            "A": "Hipoalbümineminin şiddeti kedilerde köpeklere oranla daha azdır",
            "B": "Kedilerde karın zarı sıvı toplayamaz",
            "C": "Kedilerin onkotik basıncı albümine bağlı değildir",
            "D": "Kedilerde lenf dolaşımı bulunmaz"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; hipoalbümineminin derinliği kedilerde genellikle köpekler kadar şiddetli seyretmediğinden kedilerde asites tablosu daha nadirdir (Slayt 201).",
            "celdirici_analizi": "Köpeklerde ise derin hipoalbüminemi hızla abdominal ve plöral transudata yol açar."
        },
        "slayt_no": 201,
        "zorluk_derecesi": "orta",
        "etiketler": ["hipoalbuminemi", "asites", "kedi_kopek_farki"]
    },
    {
        "soru_id": "mcq_sind_124",
        "soru_metni": "Lenfositik plasmasitik enteritisli kedilerde kortikosteroid tedavisine başlamadan önce yapılması gereken ilk basamak yaklaşım nedir?",
        "secenekler": {
            "A": "Diyet hipersensitivitesi olasılığına karşı eliminasyon/hipoalerjenik diyet denemesi",
            "B": "Hemen cerrahi olarak ince bağırsakların yarısını rezeke etmek",
            "C": "Kediyi 10 gün boyunca susuz bırakmak",
            "D": "Sadece yüksek doz kemoterapi başlamak"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; gıda alerjisi tablonun birincil nedeni olabileceğinden steroide başlamadan önce sıkı diyet denemesi yapılmalıdır (Slayt 203).",
            "celdirici_analizi": "Diyetle düzelmeyen vakalarda oral prednizolon (2.2 mg/kg/gün) başlanır."
        },
        "slayt_no": 203,
        "zorluk_derecesi": "orta",
        "etiketler": ["IBD", "diyet_denemesi", "kedi"]
    },
    {
        "soru_id": "mcq_sind_125",
        "soru_metni": "Köpeklerin eozinofilik gastroenteritisinde abdominal palpasyonda saptanabilen ve lümeni tıkayarak tümörle karışabilen karakteristik lezyon hangisidir?",
        "secenekler": {
            "A": "Bağırsakta segmental tümör benzeri kalınlaşma",
            "B": "Sadece dalakta kist",
            "C": "Mesane duvarında polip",
            "D": "Böbrek boyutlarında küçülme"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; eozinofilik infiltrasyon segmental olarak bağırsak duvarını aşırı kalınlaştırıp tümör benzeri kitle oluşturabilir ve tıkanma yapabilir (Slayt 204).",
            "celdirici_analizi": "Kanda eozinofili eşlik eder ve glukokortikoidlere (prednizolon 2-3 mg/kg) çok hızlı cevap verir."
        },
        "slayt_no": 204,
        "zorluk_derecesi": "orta",
        "etiketler": ["eozinofilik_gastroenterit", "segmental_kalinlasma"]
    },
    {
        "soru_id": "mcq_sind_126",
        "soru_metni": "Kedilerin Hipereozinofilik Sendromu ile ilgili klinik gidişat ve prognoz değerlendirmesi nasıldır?",
        "secenekler": {
            "A": "Genellikle tedaviye rağmen progresif kötüleşme ve ölümle sonuçlanan, yüksek mortaliteli kötü prognozlu bir hastalıktır",
            "B": "Tek doz antibiyotikle 2 günde tamamen iyileşir",
            "C": "Hiçbir organı tutmaz sadece tırnaklarda kaşıntı yapar",
            "D": "Sadece genç yavrularda görülüp kendiliğinden geçer"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; hipereozinofilik sendrom karaciğer, dalak, kemik iliği, akciğer gibi birçok organı tutar, progresiftir ve mortalitesi çok yüksektir (Slayt 206).",
            "celdirici_analizi": "Yüksek doz prednizolona (4-5 mg/kg) rağmen yanıt zayıftır."
        },
        "slayt_no": 206,
        "zorluk_derecesi": "orta",
        "etiketler": ["hipereozinofilik_sendrom", "kedi", "prognoz"]
    },
    {
        "soru_id": "mcq_sind_127",
        "soru_metni": "İntestinal Lenfanjiyektazi (Lymphangiectasia) hastalığının patolojik tanımı hangisidir?",
        "secenekler": {
            "A": "Lenfatik damarların dilatasyonu ve villuslardan bağırsak lümenine lenf sıvısının sızması",
            "B": "Bağırsak atardamarlarının pıhtı ile tıkanması",
            "C": "Mide bezlerinin tamamen körelmesi",
            "D": "Pankreas kanalının taşla tıkanması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; mukozal lenfatiklerin (laktealler) genişleyip yırtılmasıyla protein ve lipitten zengin lenf sıvısı lümene akar (Slayt 208).",
            "celdirici_analizi": "Bu durum protein kayıplı enteropatinin (PKE) en önemli nedenlerindendir."
        },
        "slayt_no": 208,
        "zorluk_derecesi": "kolay",
        "etiketler": ["lenfanjiyektazi", "tanim", "PLE"]
    },
    {
        "soru_id": "mcq_sind_128",
        "soru_metni": "İntestinal lenfanjiyektazili bir köpeğin kan tahlilinde görülen karakteristik biyokimyasal ve hematolojik bulgu üçlüsü (triad) hangisidir?",
        "secenekler": {
            "A": "Hipoalbüminemi + Hipokolesterolemi + Lenfopeni",
            "B": "Hiperalbüminemi + Hiperkolesterolemi + Lökositoz",
            "C": "Normal albümin + Trombositoz + Hipoglisemi",
            "D": "Hipernatremi + Hiperkalsemi + Polistemi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; lenf sıvısı protein, kolesterol ve lenfosit içerdiğinden lümene sızması sonucu kanda bu üç parametre de belirgin düşer (Slayt 208, 210).",
            "celdirici_analizi": "Hipoalbüminemi, hipokolesterolemi ve lenfopeni birlikteliği lenfanjiyektazi için çok güçlü bir göstergedir."
        },
        "slayt_no": 210,
        "zorluk_derecesi": "orta",
        "etiketler": ["lenfanjiyektazi", "triad", "hipokolesterolemi"]
    },
    {
        "soru_id": "mcq_sind_129",
        "soru_metni": "İntestinal lenfanjiyektazi tanısı almış bir köpeğin beslenme yönetiminde hangi diyet modifikasyonu esastır?",
        "secenekler": {
            "A": "Uzun zincirli trigliseritlerin (LCT) kısıtlanması ve Orta Zincirli Trigliseritlerin (MCT) diyete eklenmesi",
            "B": "Aşırı yağlı kuyruk yağı verilmesi",
            "C": "Protein içeriğinin %0'a indirilmesi",
            "D": "Sadece çiğ kemik ve şeker verilmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; uzun zincirli yağlar lenf akımını ve lakteal basıncını artırır. Orta zincirli yağlar (MCT) ise lenfe değil doğrudan portal vene emilir, lenfatik basıncı düşürür (Slayt 211).",
            "celdirici_analizi": "Ayrıca yağda çözünen vitaminler (A, D, E, K) diyete eklenmelidir."
        },
        "slayt_no": 211,
        "zorluk_derecesi": "orta",
        "etiketler": ["lenfanjiyektazi", "MCT", "diyet"]
    },
    {
        "soru_id": "mcq_sind_130",
        "soru_metni": "Mukusla dolu intestinal kriptlerin şiddetli dilatasyonu ve epitel döküntüleriyle karakterize 'Kript Hastalığı' özellikle hangi köpek ırklarında yaygındır?",
        "secenekler": {
            "A": "Yorkshire Terrier ve Rottweiler",
            "B": "Kangal ve Akbaş",
            "C": "Golden Retriever ve Labrador",
            "D": "Doberman ve Beagle"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kript lezyonları özellikle Yorkshire terrier ve Rottweiler ırkı köpeklerde yaygındır ve PKE'ye neden olur (Slayt 212).",
            "celdirici_analizi": "Endoskopik biyopside fokal lezyonların tespiti cerrahiye göre daha üstündür."
        },
        "slayt_no": 212,
        "zorluk_derecesi": "orta",
        "etiketler": ["kript_hastaligi", "yorkshire", "rottweiler"]
    },
    {
        "soru_id": "mcq_sind_131",
        "soru_metni": "Köpek ve kedilerde şiddetli granülomatöz intestinal infiltrasyon oluşturarak sekonder Protein Kayıplı Enteropatiye (PKE) yol açan fungal enfeksiyon hangisidir?",
        "secenekler": {
            "A": "Histoplasma capsulatum",
            "B": "Microsporum canis",
            "C": "Malassezia pachydermatis",
            "D": "Aspergillus fumigatus"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Histoplasma capsulatum sistemik ve gastrointestinal granülomlar yaparak ağır protein kaybına yol açar (Slayt 213).",
            "celdirici_analizi": "Hastalarda sıklıkla hipoalbüminemi ile birlikte poliklonal hiperglobulinemi görülür."
        },
        "slayt_no": 213,
        "zorluk_derecesi": "orta",
        "etiketler": ["histoplazmozis", "PKE", "fungal_enterit"]
    },
    {
        "soru_id": "mcq_sind_132",
        "soru_metni": "Protein Kayıplı Enteropatili (PKE) köpeklerde anestezi uygulanması gerektiğinde hekimin mutlaka dikkat etmesi ve ekarte etmesi gereken ölümcül risk nedir?",
        "secenekler": {
            "A": "Teşhis edilmemiş plöral efüzyonun anestezi indüksiyonunda ölümcül asfiksi yaratması",
            "B": "Göz tansiyonunun aniden düşmesi",
            "C": "Diş minesi dökülmesi",
            "D": "Kuyruk refleksinin kaybolması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; hipoalbüminemiye bağlı toraksta toplanan plöral sıvı fark edilmezse anestezi sırasında akciğerler genişleyemez ve hasta asfiksiden kaybedilir (Slayt 216).",
            "celdirici_analizi": "Bu nedenle anestezi öncesi toraks grafisi veya USG ile sıvı ekarte edilmeli, varsa drene edilmelidir."
        },
        "slayt_no": 216,
        "zorluk_derecesi": "orta",
        "etiketler": ["PKE", "anestezi_riski", "pleural_efuzyon"]
    },
    {
        "soru_id": "mcq_sind_133",
        "soru_metni": "PKE'li köpeklerde Antitrombin-III (AT-III) kaybına bağlı gelişen aşırı pıhtılaşma (tromboz) riskini önlemek için uygulanan antitrombotik protokol nedir?",
        "secenekler": {
            "A": "Düşük doz Aspirin (0.5 mg/kg/gün PO) ve Heparin (200-250 IU/kg SC G3K)",
            "B": "Yüksek doz K vitamini enjeksiyonu",
            "C": "Sadece kalsiyum glukonat verilmesi",
            "D": "Streptokinazın her gün damardan verilmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; tromboemboli profilaksisinde mikrodoz aspirin (0.5 mg/kg) ve heparin kombinasyonu önerilir (Slayt 217, 222).",
            "celdirici_analizi": "K vitamini pıhtılaşmayı uyarır; tromboz riskini daha da artırır."
        },
        "slayt_no": 222,
        "zorluk_derecesi": "orta",
        "etiketler": ["tromboz", "aspirin", "heparin", "PKE"]
    },
    {
        "soru_id": "mcq_sind_134",
        "soru_metni": "Hipoalbüminemik bir köpekte protein kaybının böbrekten mi bağırsaktan mı olduğunu ayırt etmek için ilk adımda hangi analiz yapılmalıdır?",
        "secenekler": {
            "A": "İdrar Protein / Kreatinin oranı (UPC) ve karaciğer fonksiyon testleri",
            "B": "Sadece kulak arkası deri kazıntısı",
            "C": "Göz dibi muayenesi",
            "D": "Beyin omurilik sıvısı analizi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; önce Protein Kayıplı Nefropati (PLN) idrar protein/kreatinin oranıyla ekarte edilmeli ve karaciğer yetmezliği dışlanmalıdır (Slayt 218).",
            "celdirici_analizi": "Böbrek ve karaciğer dışlandıktan sonra gastrointestinal kayıp (PKE) araştırılır."
        },
        "slayt_no": 218,
        "zorluk_derecesi": "orta",
        "etiketler": ["UPC", "ayirici_tani", "hipoalbuminemi"]
    },
    {
        "soru_id": "mcq_sind_135",
        "soru_metni": "Protein Kayıplı Enteropatinin tanısında gastrointestinal kanaldan protein kaybı olup olmadığını doğrudan gösteren tek spesifik test hangisidir?",
        "secenekler": {
            "A": "Fekal Alfa-1 Proteinaz İnhibitörü (α1-PI) ölçümü",
            "B": "Serum amilaz ve lipaz testi",
            "C": "Tam idrar tahlili",
            "D": "Kanda glukoz tolerans testi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Fekal α1-proteinaz inhibitörü bağırsak enzimleriyle sindirilmez ve feçeste değişmeden atılır; bağırsaktan protein kaçağının tek kanıtıdır (Slayt 219).",
            "celdirici_analizi": "Albümin lümende bakterilerce sindirildiği için dışkıda albümin ölçülemez; bu yüzden α1-PI ölçülür."
        },
        "slayt_no": 219,
        "zorluk_derecesi": "orta",
        "etiketler": ["fekal_alfa1_proteinaz", "PKE", "kesin_test"]
    },
    {
        "soru_id": "mcq_sind_136",
        "soru_metni": "Fekal alfa-1 proteinaz inhibitörü analizi için dışkı örneği nasıl toplanmalıdır?",
        "secenekler": {
            "A": "Üst üste 3 gün boyunca taze feçes örneği toplanmalı ve rektal lavman/müdahale yapılmamalıdır",
            "B": "Sadece 1 kez kuru kumdan alınmalıdır",
            "C": "Lavman yapıldıktan 10 dakika sonra rektumdan kazınmalıdır",
            "D": "Hayvan 1 hafta aç bırakıldıktan sonra dışkı aranmalıdır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; intrarektal manipülasyon mukoza kanaması yapabileceği için yasaktır; üst üste 3 gün taze dışkı toplanır (Slayt 219).",
            "celdirici_analizi": "Rektal travma yalancı pozitif sonuçlara neden olur."
        },
        "slayt_no": 219,
        "zorluk_derecesi": "orta",
        "etiketler": ["fekal_test", "ornekleme", "protokol"]
    },
    {
        "soru_id": "mcq_sind_137",
        "soru_metni": "PKE'li köpeklerde ileum mukozasındaki ağır hasara sekonder olarak emilemeyen ve 500-1500 mcg dozunda parenteral verilmesi gereken vitamin hangisidir?",
        "secenekler": {
            "A": "Kobalamin (B12 Vitamini)",
            "B": "C Vitamini",
            "C": "E Vitamini",
            "D": "B1 Vitamini (Tiamin)"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; B12 vitamini (kobalamin) sadece ileumdan emildiği için PKE'de hipokobalaminemi çok sıktır ve enjeksiyonla takviye edilir (Slayt 222).",
            "celdirici_analizi": "B12 eksikliği enterosit rejenerasyonunu engeller; düzeltilmezse diyare iyileşmez."
        },
        "slayt_no": 222,
        "zorluk_derecesi": "orta",
        "etiketler": ["kobalamin", "B12", "PKE"]
    },
    {
        "soru_id": "mcq_sind_138",
        "soru_metni": "Genç köpeklerde bağırsak segmentinin birbiri içine teleskop gibi girmesi (İnvaginasyon / İntussusepsiyon) durumunda ultrasonografide görülen karakteristik görüntü hangisidir?",
        "secenekler": {
            "A": "Konsantrik halkalar / 'Hedef tahtası' (Target sign) görünümü",
            "B": "Saf tek katmanlı anekoik kist",
            "C": "Karaciğer içinde kireçlenme",
            "D": "Midede çift başlı kum saati bulgusu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; invaginasyonda iç içe geçen bağırsak katmanları ultrasonda tipik 'konsantrik halkalar' veya 'hedef tahtası' (target sign) görüntüsü verir (Slayt 226, 227).",
            "celdirici_analizi": "Palpasyonda ise sosis/sucuk benzeri hareketli bir kitle ele gelir."
        },
        "slayt_no": 227,
        "zorluk_derecesi": "orta",
        "etiketler": ["invaginasyon", "ultrason", "hedef_tahtasi"]
    },
    {
        "soru_id": "mcq_sind_139",
        "soru_metni": "Haftanın vakasında sunulan 2 yaşındaki erkek Collie melezinde egzersiz intoleransı ve halsizlik araştırılırken bazal serum kortizol düzeyi 132 nmol/L bulunmuştur. Bu laboratuvar sonucu hangi hastalığı kesin olarak ekarte etmiştir?",
        "secenekler": {
            "A": "Hipoadrenokortizm (Addison Hastalığı)",
            "B": "Myasthenia Gravis",
            "C": "Megaözefagus",
            "D": "Aspirasyon pnömonisi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; bazal kortizol düzeyinin >= 70 nmol/L olması hipoadrenokortizmi (Addison) kesin olarak ekarte eder (Slayt 237).",
            "celdirici_analizi": "Eğer < 70 nmol/L çıksaydı Addison'ı doğrulamak için ACTH stimülasyon testi gerekirdi."
        },
        "slayt_no": 237,
        "zorluk_derecesi": "orta",
        "etiketler": ["kortizol", "addison", "vaka_analizi"]
    },
    {
        "soru_id": "mcq_sind_140",
        "soru_metni": "Vakadaki köpeğe 0.1-0.2 mg/kg IV Edrofonyum klorid (Tensilon) uygulandıktan sonra lokomotor aktivitede dramatik düzelme görülmesine karşın kesin tanı için Asetilkolin Reseptör Antikor titresi istenmesinin nedeni nedir?",
        "secenekler": {
            "A": "Tensilon testi yalancı pozitif veya yalancı negatif sonuçlar verebildiğinden kesin tanı için kullanılamaz; kesin tanı AchR antikor titresiyle konur",
            "B": "Edrofonyum klorid sadece parazitleri öldürdüğü için",
            "C": "Asetilkolin reseptör antikorunun sadece kuduzda pozitifleşmesi",
            "D": "Tensilon testinin köpeği kalıcı olarak kör etmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Tensilon testi hızlı bir tarama testidir ancak yalancı sonuçlar verebilir ve özefagus kasına etkisi yoktur; Myasthenia Gravis'in kesin tanısı Asetilkolin Reseptör Antikoru titresiyle konur (Slayt 240).",
            "celdirici_analizi": "Vaka: Myasthenia gravis'e sekonder megaözefagus ve buna bağlı aspirasyon pnömonisidir."
        },
        "slayt_no": 240,
        "zorluk_derecesi": "orta",
        "etiketler": ["tensilon_testi", "myasthenia_gravis", "achr_antikoru", "vaka"]
    }
]

print(f"Bölüm 3 hazır: {len(QUESTIONS_PART3)} soru.")
