# -*- coding: utf-8 -*-
"""
VetMeri - 5. Ders: Anestezi Ekipmanları ve Cihazları
Kapsam: 25 Slayt (Likid Anestezikler, Vaporizatör, Endotrakeal Tüpler [Kauçuk, Vinil, Silikon, Murphy, Magill], 
İç Çap Tablosu, Oksijen Tankları, Flowmetre, Rezerv Balonu, Valfler [İnspirasyon, Ekspirasyon, O2 Flash, Pop-off], 
Karbondioksit Tutucu Kanister & Sodalime)
"""

METADATA = {
    "id": "ekipmanlar",
    "name": "5. Ders: Anestezi Ekipmanları ve Cihazları",
    "shortName": "Anestezi Ekipmanları",
    "icon": "🎛️",
    "badge": "25 Slayt • Endotrakeal Tüpler, Vaporizatör, Balon & Kanister",
    "kategori": "Veteriner Cerrahi ve Anesteziyoloji",
    "alt_kategori": "İnhalasyon Anestezi Cihazları, Ekipmanlar ve Devre Sistemleri",
    "ozet": "Bu eğitim modülü; inhalasyon anestezisinde kullanılan alet ve ekipmanları, volatil anesteziklerin buharlaştırılmasını, endotrakeal tüp çeşitlerini (kauçuk, vinil, silikon, Murphy, Magill) ve iç çap ölçülerini, kaflı/kafsız tüp dinamiklerini, anestezi cihazının ana bileşenlerini (O2 tankı, flowmetre, vaporizatör, rezerv balonu, inspirasyon/ekspirasyon valfleri, O2 flash valfi, pop-off valfi) ve karbondioksit tutucu kanister (sodalime) işleyişini eksiksiz kapsamaktadır.",
    "kilit_noktalar": [
        "İnsanlar için dizayn edilmiş anestezi cihazları kedi ve köpeklerde kullanılabilirken, at ve sığır gibi büyük hayvanlar için özel tasarlanmış cihazlar gereklidir (Slayt 2).",
        "Eter gibi açık damlatma yöntemleri terk edilmiş olup günümüzde volatil likid anestezikler vaporizatörlerde buharlaştırılarak güvenli konsantrasyonda verilir (Slayt 2).",
        "Kauçuk tüpler ucuzdur ancak dezenfektanı absorbe edip çatlar ve kolay kıvrılır; spiral telli (armored) olanlar ezilmeye dirençlidir (Slayt 5).",
        "Silikonlu kauçuk tüpler pahalıdır ancak veteriner hekimlikte EN ÇOK TERCİH EDİLMESİ GEREKEN en az irritan tüplerdir (Slayt 6).",
        "Murphy tüplerinin distal ucunda 'Murphy deliği' bulunur; tüp ucu mukus veya trakea duvarına değerek tıkandığında alternatif hava yolu sağlar (Slayt 7).",
        "Kaflı tüpler oda havasının karışmasını ve kusmuk aspirasyonunu önler; ancak aşırı şişirilirse trakeada basınç nekrozuna yol açar (Slayt 8).",
        "Endotrakeal tüp internal çapı 1 kg kedide 2.5-3 mm iken, 10-14 kg köpekte 7-8 mm, yetişkin at/sığırda 22-26 mm'dir (Slayt 9).",
        "Anestezi cihazında oksijen sadece hastanın solunumu için değil, aynı zamanda volatil anesteziklerin TAŞIYICISI olarak zorunludur (Slayt 10).",
        "Flowmetre dakikada litre (L/dk) cinsinden gaz akışını ayarlar; oksijen tüpü açılsa bile flowmetre açılmadan sisteme gaz gitmez (Slayt 14).",
        "Rezerv balonu hacmi kedi ve yavru köpeklerde 500 ml, köpeklerde 1-2 litre, at ve sığırlarda ise 30 litredir (Slayt 16).",
        "Rezerv balonuna aralıklı ılımlı basınç uygulanması (IPPV) uzun anestezilerde atelektaziyi önler, kollabe alveolleri açar ve tidal volümü destekler (Slayt 18).",
        "Rezerv balonunun aşırı şişmesi alveol yırtılmasına (barotravma) yol açabilir; bunu önlemek için pop-off valfi bir miktar açık tutulmalıdır (Slayt 19, 23).",
        "Oksijen Flash Valfi (O2 Flush) flowmetre ve vaporizatöre uğramadan doğrudan sisteme saf O2 verir; acilde ve uyanmada kullanılır ancak NON-REBREATHING sistemlerde barotravma riski nedeniyle KULLANILMAMALIDIR (Slayt 22).",
        "Pop-off valfinin kapalı unutulması aşırı basınç artışına ve alveollerin yırtılmasına neden olur (Slayt 24).",
        "Karbondioksit tutucu kanisterde soda lime veya barium lime kullanılır; taze granüller kolayca ufalanırken doymuş granüller serttir ve renkleri mavi-mora döner (Slayt 25)."
    ]
}

SUMMARY_SECTIONS = [
    {
        "title": "1. İnhalasyon Anestezi Prensipleri & Temel Ekipman Listesi",
        "icon": "🧪",
        "points": [
            "Likid Anestezikler & Buharlaştırma: İnhalasyon anestezikleri sıvı haldedir; uygulanabilmeleri için özel vaporizatör sistemlerinde buharlaştırılıp gaz haline getirilmeleri gerekir (Slayt 2).",
            "Cihaz Boyutu & Tür Uyumu: İnsan anestezi cihazları kedi ve köpekler için uygundur; fakat at ve sığır gibi büyük hayvanlarda çok daha büyük hacimli özel cihazlar şarttır (Slayt 2).",
            "Tarihsel Gelişim: Eskiden eter gazlı beze damlatılarak açık sistemle solutulurken, modern anesteziyolojide hassas vaporizatörlerle kontrollü konsantrasyon sağlanır (Slayt 2).",
            "Ekipman Listesi 1: Enjektör ve iğneler, laringoskop, endotrakeal tüpler, tüp kaf enjektörü, lidokain sprey (özellikle kedi larinksi için), göz damlası/pomadı, maske, oksijen ve N2O (Slayt 3).",
            "Ekipman Listesi 2: Y parçası ve konnektörler, rezerv balonu, ventilatör, İngiliz anahtarı, acil resüsitasyon ilaçları, hastayı ısıtma örtüleri/battaniyeler, steteskop, termometre, atık gaz sistemi ve gözlem kartı (Slayt 4)."
        ]
    },
    {
        "title": "2. Endotrakeal Tüp Çeşitleri & Malzeme Özellikleri",
        "icon": "🩺",
        "points": [
            "Tüp Materyalleri: Kauçuk, vinil plastik ve silikonlu kauçuktan imal edilirler (Slayt 5).",
            "Kauçuk Tüpler (Turuncu): Ucuzdur ve yaygındır. Ancak dezenfektanları absorbe eder; zamanla yüzeyinde çatlak, kuruma ve matlaşma oluşur. Çok esnektir, ince olanları kıvrılıp kollabe olabilir. Spiral metal/plastik telli olanları (armored) bükülmeye dirençlidir (Slayt 5).",
            "Vinil Plastik Tüpler: Şeffaftır (transparent), çatlamaz; ancak kauçuğa göre daha sert yapıdadır (Slayt 6).",
            "Silikonlu Kauçuk Tüpler: Pahalıdır fakat veteriner hekimlikte EN ÇOK TERCİH EDİLMESİ GEREKEN tüptür. Yumuşak, esnek ve dokulara karşı en az irritandır (Slayt 6)."
        ]
    },
    {
        "title": "3. Murphy vs Magill Tüpler & Kaflı Sistem Dinamikleri",
        "icon": "📐",
        "points": [
            "Murphy ve Magill Tasarımları: Her iki tüp de eğimlidir. Murphy tüpünün distal ucunda 'Murphy deliği' bulunur. Bu delik, tüpün ana ucu mukus veya trakea duvarına yapışıp tıkandığında alternatif hava yolu sağlar (Slayt 7).",
            "Uygulama Yolu: Çoğunlukla oral entübasyon yapılır; ağız içi cerrahilerde nazal entübasyon tercih edilebilir (Slayt 7).",
            "Kaflı Tüp Avantajları: Ekspirasyon gazının odaya sızıp personeli zehirlemesini önler; kan, mukus, salya ve kusmuğun akciğerlere aspirasyonunu engeller; hastanın oda havası soluyup anesteziden uyanmasını engeller (Slayt 8).",
            "Kaf Dezavantajı: Kaf aşırı şişirilirse trakea mukozasında basınç nekrozu ve yırtılma oluşabilir (özellikle kedilerde ve uzun süreli operasyonlarda) (Slayt 8)."
        ]
    },
    {
        "title": "4. Canlı Ağırlığa Göre Endotrakeal Tüp Çapları (mm)",
        "icon": "⚖️",
        "points": [
            "Kedi Tüp Çapları: 1 kg kedi için 2.5 - 3 mm; 3 kg kedi için 3 - 3.5 mm; 5 kg kedi için 4 - 4.5 mm internal çap (Slayt 9).",
            "Köpek Tüp Çapları: 2 kg için 4-5 mm; 4 kg için 5 mm; 7 kg için 6 mm; 9 kg için 7 mm; 12 kg için 7-8 mm; 14 kg için 8 mm; 16-20 kg için 9 mm; 30-40 kg için 9-10 mm internal çap (Slayt 9).",
            "At ve Sığır Tüp Çapları: <30 kg tay/buzağı için 4-7 mm; 30-40 kg için 8-10 mm; 60-80 kg için 10-12 mm; 100 kg için 12 mm; 200-300 kg için 14-16 mm; 300-400 kg için 16-22 mm; 400-600 kg için 22-26 mm; >600 kg için 26 mm internal çap kullanılır (Slayt 9)."
        ]
    },
    {
        "title": "5. Anestezi Cihazı Görevleri & Oksijen Kaynağı",
        "icon": "💨",
        "points": [
            "Cihazın Temel Fonksiyonu: Volatil anestezikleri istenen oranda buharlaştırıp taşıyıcı gazla (O2 / O2+N2O) hastaya ulaştırmak ve ekspirasyon gazlarını sistemden tahliye etmektir (Slayt 10, 11).",
            "Kritik Oksijen Desteği: Anestezi cihazları vaporizatör kapatılarak kritik hastalarda maske veya entübasyonla saf oksijen ventilasyonu sağlamak için de kullanılır (Slayt 11).",
            "Neden Yüksek O2 Verilir?: 1) Anestezideki hastanın oksijen ihtiyacı uyanık hayvana göre daha fazladır; 2) Hastanın tidal volümü ve solunumu azaldığı için hipoksiyi önlemek adına %100 O2 uygulanır (Slayt 12).",
            "O2 Tankı Güvenliği: Basınçlı metal silindirlerde bulunur. Vana SOLA çevrilerek açılır, SAĞA çevrilerek tamamen kapatılır (Slayt 13)."
        ]
    },
    {
        "title": "6. Flowmetre & Vaporizatör İşleyişi",
        "icon": "⚙️",
        "points": [
            "Flowmetre: Gaz akışını dakikada litre (L/dk) olarak hassas şekilde ayarlayan kısımdır. Oksijen tankı açılsa dahi flowmetre açılmadıkça sisteme gaz iletilemez (Slayt 14).",
            "Vaporizatör: Oksijen flowmetreden geçerek vaporizatöre ulaşır. Görevi likid anestezik maddeyi buharlaştırıp belirli konsantrasyonda sisteme katmaktır (Slayt 15).",
            "Buharlaşma Şartı: Sıvı anesteziğin buharlaşması için vaporizatör içinden gaz akışı (flow) geçmesi zorunludur; flowmetre kapatılırsa vaporizatörden anestezik çıkışı durur (Slayt 15)."
        ]
    },
    {
        "title": "7. Rezerv Balonu Fonksiyonları & Ventilasyon Desteği",
        "icon": "🎈",
        "points": [
            "Rezerv Balonu Hacimleri: Kedi ve küçük yavrularda 500 ml; köpeklerde 1-2 litre; at ve sığırlarda 30 litredir (Slayt 16).",
            "Solunum Kolaylığı & Monitörizasyon: Sert borular yerine esnek balondan nefes almak hastaya kolaylık sağlar. Balonun hareketi solunum hızı, derinliği ve tüpün trakeada olup olmadığı hakkında doğrudan bilgi verir (Slayt 17).",
            "Basınçlı Ventilasyon (IPPV): Anestezide tidal volüm %50 azalır. Rezerv balonuna aralıklı ılımlı basınç uygulanarak atelektazi önlenir, kollabe alveoller açılır ve solunumu duran hastada hayat kurtarılır (Slayt 18).",
            "Balon Riskleri: Aşırı şişerse alveol rüptürü (barotravma) yapar; bunu önlemek için pop-off valfi açık tutulmalıdır. Tamamen sönerse hasta nefes alamaz (Slayt 19)."
        ]
    },
    {
        "title": "8. Tek Yönlü Valfler, O2 Flash, Pop-off & Kanister (Sodalime)",
        "icon": "🔄",
        "points": [
            "İnspirasyon ve Ekspirasyon Valfleri: Tek yönlü kanatçıklardır. Gazın sadece hastaya ve hastadan da kanistere doğru tek yönde akmasını sağlar (Slayt 20, 21).",
            "O2 Flash Valfi: Flowmetre ve vaporizatörü baypas ederek sisteme doğrudan yüksek debili saf O2 verir. Rezerv balonu söndüğünde, acilde veya uyanmada kullanılır. Non-rebreathing sistemlerde barotravma riski nedeniyle KULLANILMAZ (Slayt 22).",
            "Pop-off Valfi: Fazla gazı tahliye eden emniyet valfidir. Kapalı unutulursa sistem basıncı aşırı artar ve akciğer alveolleri yırtılır (Slayt 23, 24).",
            "Karbondioksit Tutucu Kanister: Sodalime veya baryum lime içerir. Ekspirasyon havasındaki CO2'yi kimyasal olarak bağlar. Taze granüller ufalanabilirken doymuş olanlar serttir ve rengi mavi-mora döner (Slayt 25)."
        ]
    }
]

BILGI_KARTLARI = [
    {
        "kart_id": "ekart_001",
        "on_yuz": "İnhalasyon anestezisinde sıvı anesteziklerin hastaya verilebilmesi için hangi özel sisteme ihtiyaç vardır?",
        "arka_yuz": "Volatil likid anestezik maddeleri belirli konsantrasyonda buharlaştırıp gaz haline getiren vaporizatör kabinlerine gereksinim vardır (Slayt 2)."
    },
    {
        "kart_id": "ekart_002",
        "on_yuz": "Küçük hayvanlar ile büyük hayvanların (at, sığır) anestezi cihazları arasındaki temel fark nedir?",
        "arka_yuz": "İnsan anestezi cihazları kedi ve köpekler için uygundur; ancak at ve sığır gibi büyük cüsseli hayvanlar için yüksek hacim ve akış kapasitesine sahip özel dizayn edilmiş anestezi cihazları gereklidir (Slayt 2)."
    },
    {
        "kart_id": "ekart_003",
        "on_yuz": "Eski dönemlerde eter gibi volatil anestezikler nasıl uygulanıyordu?",
        "arka_yuz": "Bir gazlı beze damlatılması ve buharının solutulması şeklinde (açık damlatma) uygulanıyordu; günümüzde sadece bazı laboratuvar hayvanlarında kullanılır (Slayt 2)."
    },
    {
        "kart_id": "ekart_004",
        "on_yuz": "Veteriner hekimlikte kullanılan endotrakeal tüpler hangi 3 temel materyalden üretilir?",
        "arka_yuz": "Kauçuk, vinil plastik ve silikonlu kauçuktan üretilir (Slayt 5)."
    },
    {
        "kart_id": "ekart_005",
        "on_yuz": "Kauçuk endotrakeal tüplerin avantaj ve dezavantajları nelerdir?",
        "arka_yuz": "Ucuzdurlar. Ancak dezenfektanları absorbe ederler, uzun sürede çatlar ve kururlar, çok esnek olduklarından kolayca kıvrılıp kollabe olabilirler (Slayt 5)."
    },
    {
        "kart_id": "ekart_006",
        "on_yuz": "Spiral telli (armored / reinforced) endotrakeal tüplerin yapısal özelliği nedir?",
        "arka_yuz": "Yapımında spiral metal ya da plastik teller kullanılır; esnektirler ancak dış baskılardan ezilmez ve kıvrılmaz yapıya sahiptirler (Slayt 5)."
    },
    {
        "kart_id": "ekart_007",
        "on_yuz": "Vinil plastik endotrakeal tüplerin temel fiziksel özellikleri nelerdir?",
        "arka_yuz": "Şeffaf (transparent) görünümdedirler, yüzeyinde çatlak oluşmaz ancak kauçuk tüplere kıyasla daha sert yapıdadırlar (Slayt 6)."
    },
    {
        "kart_id": "ekart_008",
        "on_yuz": "Silikonlu kauçuk endotrakeal tüplerin klinik açıdan en büyük üstünlüğü nedir?",
        "arka_yuz": "Pahalıdır ancak en çok tercih edilmesi gereken tüptür; yumuşak ve esnektir, kauçuk ve vinile göre dokulara çok daha az irritandır (Slayt 6)."
    },
    {
        "kart_id": "ekart_009",
        "on_yuz": "Murphy endotrakeal tüpü Magill tüpünden ayıran en kritik yapı nedir?",
        "arka_yuz": "Distal ucuna yakın gövdesinde bulunan 'Murphy deliği'dir (Slayt 7)."
    },
    {
        "kart_id": "ekart_010",
        "on_yuz": "Murphy deliğinin hayati fonksiyonu nedir?",
        "arka_yuz": "Tüp ucu mukusla veya trakea çeperine değerek tıkandığında gaz geçişi için alternatif bir açıklık sağlar (Slayt 7)."
    },
    {
        "kart_id": "ekart_011",
        "on_yuz": "Endotrakeal tüpler veteriner hekimlikte hangi yollarla uygulanabilir?",
        "arka_yuz": "Daha sıklıkla oral yoldan uygulanır; ağız içi operasyonlarda ise nazal uygulama yolu tercih edilebilir (Slayt 7)."
    },
    {
        "kart_id": "ekart_012",
        "on_yuz": "Kaflı endotrakeal tüplerin sağladığı 3 büyük avantaj nedir?",
        "arka_yuz": "1) Atık gazın ameliyathaneye kaçmasını önler, 2) Kusmuk, kan ve salyanın akciğerlere aspirasyonunu önler, 3) Hayvanın oda havası soluyup anesteziden çıkmasını engeller (Slayt 8)."
    },
    {
        "kart_id": "ekart_013",
        "on_yuz": "Endotrakeal tüp kafının aşırı şişirilmesinin en tehlikeli komplikasyonu nedir?",
        "arka_yuz": "Trakeanın iç çeperinde basınç nekrozuna ve yırtılmaya neden olabilir (özellikle küçük hayvanlarda ve uzun süreli anestezide) (Slayt 8)."
    },
    {
        "kart_id": "ekart_014",
        "on_yuz": "1 kg, 3 kg ve 5 kg ağırlığındaki kedilerde hangi çapta (internal mm) tüpler kullanılır?",
        "arka_yuz": "1 kg kedi: 2.5-3 mm; 3 kg kedi: 3-3.5 mm; 5 kg kedi: 4-4.5 mm internal çaplı tüpler kullanılır (Slayt 9)."
    },
    {
        "kart_id": "ekart_015",
        "on_yuz": "10-14 kg ve 30-40 kg ağırlığındaki köpeklerde hangi iç çapta tüpler tercih edilir?",
        "arka_yuz": "12-14 kg köpekte 7-8 mm; 30-40 kg köpekte 9-10 mm internal çaplı tüpler kullanılır (Slayt 9)."
    },
    {
        "kart_id": "ekart_016",
        "on_yuz": "400-600 kg ağırlığındaki bir at veya sığırda kullanılacak endotrakeal tüpün çapı nedir?",
        "arka_yuz": "22 - 26 mm internal çaplı tüpler kullanılır (Slayt 9)."
    },
    {
        "kart_id": "ekart_017",
        "on_yuz": "Anestezi cihazında oksijen gazının iki temel fonksiyonu nedir?",
        "arka_yuz": "1) Hastanın hücresel oksijen ihtiyacını karşılamak, 2) Volatil anestezik maddeleri taşıyıcı gaz olarak hastaya iletmek (Slayt 10)."
    },
    {
        "kart_id": "ekart_018",
        "on_yuz": "Anestezi hastasına neden %100'e yakın yüksek konsantrasyonda oksijen verilir?",
        "arka_yuz": "Anestezide oksijen ihtiyacı artmıştır ve anestezik depresyon nedeniyle tidal volüm azaldığından hipoksiyi önlemek için yüksek O2 verilir (Slayt 12)."
    },
    {
        "kart_id": "ekart_019",
        "on_yuz": "Oksijen silindirinin vanası hangi yöne açılarak devreye sokulur, hangi yöne kapatılır?",
        "arka_yuz": "Vana SOLA çevrilerek açılır, SAĞA doğru çevrilerek tamamen kapatılır (Slayt 13)."
    },
    {
        "kart_id": "ekart_020",
        "on_yuz": "Flowmetrenin görevi ve ölçüm birimi nedir?",
        "arka_yuz": "Cihazdan dakikada hastaya ulaşacak gaz miktarını ayarlar; gaz akışı dakikada litre (L/dk) olarak sağlanır (Slayt 14)."
    },
    {
        "kart_id": "ekart_021",
        "on_yuz": "Vaporizatörün çalışabilmesi için flowmetrenin açık olması neden şarttır?",
        "arka_yuz": "Volatil likid anestezik maddenin buharlaşabilmesi için vaporizatör içinden gaz akışı olması gerekir; akış kapatılırsa anestezik buharlaşamaz ve sisteme giremez (Slayt 15)."
    },
    {
        "kart_id": "ekart_022",
        "on_yuz": "Kedi, köpek ve büyük hayvanlarda kullanılan rezerv balonu hacimleri nelerdir?",
        "arka_yuz": "Kedi ve yavru köpeklerde 500 ml; köpeklerde sıklıkla 1-2 litre; at ve sığırlarda ise 30 litrelik rezerv balonları kullanılır (Slayt 16)."
    },
    {
        "kart_id": "ekart_023",
        "on_yuz": "Rezerv balonunun yeterli miktarda hareket etmemesi hekime neyi düşündürür?",
        "arka_yuz": "Hastanın bir miktar oda havası soluduğunu, yani endotrakeal tüp kafının yeterince şişirilmediğini ve kaf etrafından hava kaçtığını gösterir (Slayt 17)."
    },
    {
        "kart_id": "ekart_024",
        "on_yuz": "Anestezide rezerv balonuna ılımlı basınç uygulamanın (IPPV) temel faydaları nelerdir?",
        "arka_yuz": "Atelektaziyi önler, kollabe olan akciğerleri tekrar şişirir, azalan tidal volümde taze gazın alveollere ulaşmasını sağlar ve solunumu duran hastada hayat kurtarır (Slayt 18)."
    },
    {
        "kart_id": "ekart_025",
        "on_yuz": "Rezerv balonunun aşırı şişmesi neden tehlikelidir ve nasıl önlenir?",
        "arka_yuz": "Akciğer alveollerinin yırtılmasına (barotravma) neden olabilir; önlemek için pop-off valfi bir miktar açık bırakılmalıdır (Slayt 19)."
    },
    {
        "kart_id": "ekart_026",
        "on_yuz": "İnhalasyon ve ekspirasyon valflerinin devre sistemindeki ortak görevi nedir?",
        "arka_yuz": "Tek yönlü çalışarak gazın sadece ileriye doğru hareket etmesini ve atık ekspirasyon gazının kanisterden geçmeden geri solunmasını engellerler (Slayt 20, 21)."
    },
    {
        "kart_id": "ekart_027",
        "on_yuz": "Oksijen Flash Valfine basıldığında ne gerçekleşir?",
        "arka_yuz": "Oksijen flowmetre ve vaporizatöre uğramadan doğrudan sisteme yüksek debide saf oksijen olarak verilir (Slayt 22)."
    },
    {
        "kart_id": "ekart_028",
        "on_yuz": "Oksijen Flash Valfi hangi anestezi sistemlerinde KESİNLİKLE kullanılmamalıdır?",
        "arka_yuz": "Non-rebreathing sistemlerde kullanılmamalıdır; balonu hızla aşırı şişirip akciğerleri yırtabilir (Slayt 22)."
    },
    {
        "kart_id": "ekart_029",
        "on_yuz": "Pop-off valfinin kapalı unutulması halinde hastada ne gibi ölümcül sonuçlar doğar?",
        "arka_yuz": "Sistem gaz basıncı aşırı artar; bu aşırı basınç akciğer alveollerinde yırtılmalara, pnömotoraksa ve kardiyak basıya yol açar (Slayt 24)."
    },
    {
        "kart_id": "ekart_030",
        "on_yuz": "Karbondioksit tutucu kanisterdeki granüllerin doyduğunu nasıl anlarız?",
        "arka_yuz": "Taze granüller parmakla kolayca ufalanırken doymuş olanlar sertleşir ve rengi beyazdan mavi-mora döner (Slayt 25)."
    }
]

ACIK_UCLU_SORULAR = [
    {
        "soru_id": "au_ekip_001",
        "soru": "Volatil likid anesteziklerin uygulanmasında vaporizatör kullanımının gerekliliğini ve büyük hayvan (at, sığır) ile küçük hayvan anestezi cihazları arasındaki farkı açıklayınız.",
        "ideal_cevap": "Volatil anestezikler oda ısısında sıvı formdadır. Hastaya solutulabilmeleri için buharlaştırılıp gaz fazına geçirilmeleri ve taşıyıcı gazla hassas yüzdelerde karıştırılmaları zorunludur; bunu vaporizatör kabinleri sağlar. İnsan anestezi cihazları kedi ve köpeklerin tidal volüm ve gaz akış dinamiklerine uyumludur. Ancak at ve sığır gibi yüzlerce kiloluk büyük hayvanların akciğer kapasitesi, tidal volümü ve dakika ventilasyonu çok yüksek olduğundan, devasa rezerv balonları (30 L) ve yüksek akış kapasiteli özel dizayn edilmiş büyük anestezi cihazları gereklidir.",
        "degerlendirme_kriteri": "Cevapta [likid anesteziklerin buharlaştırılması, vaporizatör gerekliliği, insan cihazlarının kedi/köpeğe uyumu, büyük hayvanlarda özel yüksek kapasiteli cihaz ihtiyacı] yer almalıdır.",
        "slayt_no": 2
    },
    {
        "soru_id": "au_ekip_002",
        "soru": "Kauçuk, vinil plastik ve silikonlu kauçuk endotrakeal tüplerin yapısal özelliklerini, avantaj ve dezavantajlarını karşılaştırınız.",
        "ideal_cevap": "1) Kauçuk tüpler (turuncu): Ucuzdur ancak dezenfektanları absorbe eder, zamanla çatlar ve kurur; aşırı esnek olduklarından bükülüp tıkanabilir (spiral telli olanları bükülmeye dirençlidir). 2) Vinil plastik tüpler: Şeffaftır, çatlama yapmaz, ancak kauçuğa göre daha serttir. 3) Silikonlu kauçuk tüpler: Pahalıdır fakat veteriner hekimlikte en çok tercih edilmesi gereken tüptür; son derece yumuşak ve esnektir, trakea mukozasına karşı en az irritandır.",
        "degerlendirme_kriteri": "Cevapta [kauçukta dezenfektan emilimi/çatlama/kıvrılma, vinilde şeffaflık/sertlik, silikonda en çok tercih edilme/yumuşaklık/en az irritan olma] karşılaştırmalı yer almalıdır.",
        "slayt_no": 5
    },
    {
        "soru_id": "au_ekip_003",
        "soru": "Murphy endotrakeal tüpünün distal ucunda bulunan 'Murphy deliği'nin anatomik yapısını ve hayati fonksiyonunu açıklayınız.",
        "ideal_cevap": "Murphy tüpünün eğimli gövdesinin distal ucuna yakın yan duvarında oval bir delik bulunur ve buna 'Murphy deliği' adı verilir. Hayati önemi: Eğer endotrakeal tüpün primer distal ağzı trakea çeperine (mukozaya) dayanarak veya lümendeki kalın mukus/sekresyon tıkacıyla tamamen kapanırsa, Murphy deliği gaz ve oksijen akışının kesilmesini engelleyen alternatif bir acil hava kanalı oluşturarak hastanın asfiksiden boğulmasını önler.",
        "degerlendirme_kriteri": "Cevapta [distal yan duvarda delik, primer uç tıkandığında alternatif açıklık sağlama, mukus/çeper tıkanmasında gaz akışını sürdürme] yer almalıdır.",
        "slayt_no": 7
    },
    {
        "soru_id": "au_ekip_004",
        "soru": "Kaflı endotrakeal tüp kullanımının ameliyathane güvenliği ve hasta fizyolojisi açısından 3 temel avantajını ve aşırı şişirilmesinin riskini yazınız.",
        "ideal_cevap": "Avantajları: 1) Ekspirasyon gazlarının odaya sızmasını engelleyerek ameliyathane personelinin kronik atık gaz solumasını önler. 2) Regürgitasyon veya kusma anında mide içeriğinin, kan ve salyanın akciğerlere kaçmasını (aspirasyon pnömonisini) önler. 3) Hastanın tüp etrafından oda havası solumasını engelleyerek anestezi derinliğinin stabil kalmasını sağlar. Dezavantaj/Risk: Kaf enjektörle aşırı şişirilirse trakea kapiller perfüzyonunu aşan basınca bağlı olarak trakea iç çeperinde iskemi, basınç nekrozu ve yırtılma oluşabilir.",
        "degerlendirme_kriteri": "Cevapta [atık gaz sızıntısını önleme, aspirasyonu engelleme, oda havası solunmasını önleme, aşırı şişirmede basınç nekrozu] eksiksiz bulunmalıdır.",
        "slayt_no": 8
    },
    {
        "soru_id": "au_ekip_005",
        "soru": "Farklı tür ve ağırlıktaki hayvanlarda endotrakeal tüp internal çapı (mm) seçimini kedi, orta ırk köpek ve yetişkin at örnekleri üzerinden açıklayınız.",
        "ideal_cevap": "Tüp çapı canlı ağırlığa göre seçilir: 1 kg yavru kedide 2.5-3 mm, yetişkin 3-5 kg kedilerde 3.5-4.5 mm kullanılır. 12-14 kg ağırlığında bir köpekte 7-8 mm, 30-40 kg iri bir köpekte 9-10 mm internal çap tercih edilir. 400-600 kg yetişkin bir atta ise 22-26 mm (>600 kg atta 26 mm) internal çapa sahip geniş endotrakeal tüpler kullanılır.",
        "degerlendirme_kriteri": "Cevapta [kedi: 2.5-4.5 mm, orta köpek: 7-8 mm, yetişkin at: 22-26 mm] değerleri yer almalıdır.",
        "slayt_no": 9
    },
    {
        "soru_id": "au_ekip_006",
        "soru": "Anestezi cihazlarında hastaya neden anestezide olmayana kıyasla yüksek konsantrasyonda (%100) oksijen uygulanır? İki temel fizyolojik gerekçesini yazınız.",
        "ideal_cevap": "1) Anestezide olmayan sağlıklı hayvana kıyasla genel anestezi altındaki hastanın hücresel bazda oksijen gereksinimi daha yüksektir. 2) Genel anesteziklerin santral solunum merkezini ve interkostal kasları deprese etmesi sonucu hastanın tidal volümü (%50 oranında) ve dakika solunumu belirgin şekilde azalır. Azalan ventilasyonda hipoksinin önlenmesi ve doku perfüzyonunun korunması için yüksek konsantrasyonda oksijen verilmesi şarttır.",
        "degerlendirme_kriteri": "Cevapta [1: Anestezi hastasının oksijen gereksiniminin artması, 2: Tidal volüm ve solunumun azalması, hipoksinin önlenmesi] belirtilmelidir.",
        "slayt_no": 12
    },
    {
        "soru_id": "au_ekip_007",
        "soru": "Anestezi cihazında flowmetrenin fonksiyonunu, ölçüm birimini ve oksijen tankı ile vaporizatör arasındaki konumunun önemini açıklayınız.",
        "ideal_cevap": "Flowmetre, anestezi cihazına gelen basınçlı oksijen gazının dakikada hastaya ulaşacak miktarını hassas olarak ayarlayan kısımdır ve gaz akışını 'dakikada litre' (L/dk) cinsinden sağlar. Konum önemi: Oksijen tankından gelen gaz önce flowmetreden geçer, ardından vaporizatöre ulaşır. Oksijen tüpü açık olsa dahi flowmetrenin vanası açılmazsa sisteme gaz gitmez ve vaporizatör içinden gaz akışı gerçekleşmediği için anestezik madde buharlaşamaz.",
        "degerlendirme_kriteri": "Cevapta [L/dk birimi, gaz miktarını ayarlama, O2 tankı açık olsa da flowmetre vanası gerekliliği, vaporizatör öncesi akış sağlama] bulunmalıdır.",
        "slayt_no": 14
    },
    {
        "soru_id": "au_ekip_008",
        "soru": "Vaporizatörün temel çalışma prensibini ve gaz akışı kesildiğinde volatil anestezik maddelere ne olduğunu açıklayınız.",
        "ideal_cevap": "Vaporizatör, sıvı haldeki volatil anestezik maddeyi kontrollü sıcaklık ve basınç altında buharlaştırarak, içinden geçen oksijen gazına belirli bir konsantrasyonda (% hacim) karışmasını sağlar. Buharlaşmanın gerçekleşebilmesi için vaporizatörün içinden sürekli bir taşıyıcı gaz akışının olması şarttır. Eğer flowmetreden gaz akışı kapatılırsa buharlaşma durur, volatil likid anestezik sisteme giremez ve hastaya anestezi gazı iletilemez.",
        "degerlendirme_kriteri": "Cevapta [likid anesteziği buharlaştırma, taşıyıcı gaza belirli konsantrasyonda katma, gaz akışı olmadan buharlaşamama] yer almalıdır.",
        "slayt_no": 15
    },
    {
        "soru_id": "au_ekip_009",
        "soru": "Rezerv balonunun farklı hayvan cüsselerine göre hacim standartlarını (kedi, köpek, at/sığır) yazınız.",
        "ideal_cevap": "Rezerv balonları hayvanın tidal volümüne göre seçilir: Kedi ve küçük yavru köpeklerde 500 ml hacimli balonlar kullanılır. Köpeklerde vücut ağırlığına bağlı olarak sıklıkla 1 - 2 litrelik rezerv balonları tercih edilir. At ve sığır gibi büyük cüsseli hayvanlarda ise çok daha hacimli olan 30 litrelik devasa rezerv balonları kullanılmaktadır.",
        "degerlendirme_kriteri": "Cevapta [kedi/yavru: 500 ml, köpek: 1-2 L, at/sığır: 30 L] hacimleri eksiksiz yer almalıdır.",
        "slayt_no": 16
    },
    {
        "soru_id": "au_ekip_010",
        "soru": "Anestezi sırasında rezerv balonunun hareketlerine bakılarak elde edilen klinik izlem parametrelerini ve balonun az hareket etmesinin nedenini açıklayınız.",
        "ideal_cevap": "Rezerv balonunun inip kalkmasıyla dakikadaki solunum sayısı (solunum frekansı) ve her nefeste alınan gaz hacmi (tidal volüm) gözle takip edilir. Balonun yeterli ve senkron hareketi endotrakeal tüpün doğru olarak trakea içine yerleştiğini gösterir. Eğer balon yeterli miktarda hareket etmiyorsa, hasta solunumunun bir kısmını oda havasından alıyor demektir; bu da endotrakeal tüp kafının yetersiz şişirilmesine bağlı kaf etrafından hava kaçışı olduğunu kanıtlar.",
        "degerlendirme_kriteri": "Cevapta [solunum sayısı ve hacmi izleme, tüpün trakeada olduğunu doğrulama, az hareketin kaf kaçığı ve oda havası solunması anlamına gelmesi] bulunmalıdır.",
        "slayt_no": 17
    },
    {
        "soru_id": "au_ekip_011",
        "soru": "Rezerv balonuna basınç uygulayarak ventilasyon yaptırılmasının (IPPV) atelektazi ve alveolar gaz değişimi üzerindeki etkilerini açıklayınız.",
        "ideal_cevap": "Genel anestezide solunum depresyonuna bağlı olarak tidal volüm %50 oranında azalır ve alveollerde biriken sekresyonlar atelektaziye (alveol kollapsı) yol açar. Rezerv balonuna aralıklı ılımlı basınç uygulandığında pozitif basınçlı ventilasyon sağlanarak kollabe olmuş alveoller yeniden açılır, taze oksijen ve anestezik gazın alveol kılcal damar membranına ulaşması temin edilir ve atelektazi önlenir; spontan solunumu duran hastalarda ise hayat kurtarır.",
        "degerlendirme_kriteri": "Cevapta [tidal volümün %50 azalması, sekresyon ve atelektazi önlenmesi, kollabe alveollerin açılması, taze gazın alveollere ulaştırılması] yer almalıdır.",
        "slayt_no": 18
    },
    {
        "soru_id": "au_ekip_012",
        "soru": "Rezerv balonunun aşırı dolu tutulmasının ve tamamen sönmesinin yaratacağı tehlikeleri yazınız.",
        "ideal_cevap": "Aşırı dolu olması durumunda: Balonun solunumla hareketleri izlenemez hale gelir ve devre içi basınç tehlikeli seviyelere fırlayarak akciğer alveollerinin yırtılmasına (barotravma, pnömotoraks) yol açabilir. Tamamen sönmesi durumunda ise: Hasta nefes almak istediğinde devreden yeterli gaz çekemez, hipoksi ve asfiksiye girer. Bu dengeyi korumak için pop-off valfi uygun açıklıkta tutulmalıdır.",
        "degerlendirme_kriteri": "Cevapta [aşırı doluluk: barotravma ve izleme güçlüğü, sönme: gaz alamama ve hipoksi, pop-off valf dengesi] yer almalıdır.",
        "slayt_no": 19
    },
    {
        "soru_id": "au_ekip_013",
        "soru": "İnhalasyon valfi, 'Y' parçası ve ekspirasyon valfinin tek yönlü çalışma prensibini ve gaz sirkülasyonundaki rolünü açıklayınız.",
        "ideal_cevap": "İnhalasyon valfi tek yönlü bir klapedir; hasta nefes aldığında açılarak gazın sadece hastaya doğru akmasını sağlar; gaz 'Y' parçasını geçerek endotrakeal tüple akciğere ulaşır. Ekspirasyonda ise atılan gaz yine endotrakeal tüp ve 'Y' parçasından geçerek tek yönlü ekspirasyon valfine ulaşır. Ekspirasyon valfi gazın hastaya geri dönmesini engeller ve atık gazı karbondioksit tutucu kanistere (veya atık sistemine) yönlendirir; böylece CO2'li havanın temizlenmeden geri solunması önlenir.",
        "degerlendirme_kriteri": "Cevapta [tek yönlü akış, Y parçasından geçiş, ekspirasyon valfinin geri akışı engellemesi, kanistere yönlendirme] bulunmalıdır.",
        "slayt_no": 20
    },
    {
        "soru_id": "au_ekip_014",
        "soru": "Oksijen Flash Valfinin (O2 Flush) kullanım amaçlarını ve non-rebreathing sistemlerde neden kesinlikle KONTRENDİKE olduğunu açıklayınız.",
        "ideal_cevap": "O2 flash valfine basıldığında yüksek basınçlı saf oksijen, flowmetre ve vaporizatörü baypas ederek doğrudan devreye girer. Kullanım amaçları: 1) Genel durumu kötü acil hastalara saf oksijen sağlamak, 2) Sönen rezerv balonunu saniyeler içinde doldurmak, 3) Anestezi bitiminde devredeki anestezik gazı temizleyip saf O2 ile uyanmayı hızlandırmak. Kontrendikasyon: Non-rebreathing (açık/yarı açık) sistemlerde devre hacmi çok küçük olduğundan, bu yüksek akımlı valfe basılması rezerv balonunu ve hayvanın akciğerlerini anında patlatarak ölümcül barotravmaya neden olur.",
        "degerlendirme_kriteri": "Cevapta [flowmetre/vaporizatörü baypas etme, acilde O2, sönen balonu doldurma, anestezik gazı temizleme, non-rebreathing sistemde barotravma riski] yer almalıdır.",
        "slayt_no": 22
    },
    {
        "soru_id": "au_ekip_015",
        "soru": "Pop-off valfinin işlevini, anestezi sırasındaki ideal konumunu ve kapalı unutulmasının patofizyolojik sonucunu izah ediniz.",
        "ideal_cevap": "Pop-off valfi sistemdeki fazla gazın atık sistemine tahliyesini sağlayarak devre içi basıncı düzenleyen bir emniyet valfidir. İdeal olarak bir miktar açık bırakılmalı ve az miktarda sürekli gaz kaçışı sağlanmalıdır. Eğer pop-off valfi kapalı unutulursa, sürekli gelen taze gaz sistemi ve rezerv balonunu aşırı şişirir; oluşan yüksek intratorasik basınç venöz dönüşü engelleyip kardiyak arrest oluşturur ve doğrudan alveolleri patlatarak tansiyon pnömotoraksa ve ölüme yol açar.",
        "degerlendirme_kriteri": "Cevapta [fazla gaz tahliyesi, bir miktar açık tutulması, kapalı kalırsa aşırı gaz basıncı, alveol yırtılması ve barotravma] yer almalıdır.",
        "slayt_no": 23
    },
    {
        "soru_id": "au_ekip_016",
        "soru": "Karbondioksit tutucu kanisterde kullanılan kimyasal maddeleri, granüllerin doymuşluk testini ve renk değişim mekanizmasını açıklayınız.",
        "ideal_cevap": "Kanister içinde CO2 tutucu kimyasal olarak 'soda lime' (kalsiyum hidroksit bazı) veya 'baryum hidroksit lime' bulunur. Doymuşluk testi: Taze granüller parmaklar arasında kolayca ufalanıp parçalanabilirken, CO2 ile doyup kalsiyum karbonata dönüşen granüller taş gibi sert ve dayanıklıdır. Renk değişimi: İçerdiği etil menekşesi (pH indikatörü) sayesinde granüller asitlendikçe ve CO2 ile doydukça beyaz renkten mavi-mora döner; mor renk granüllerin değiştirilmesi gerektiğini bildirir.",
        "degerlendirme_kriteri": "Cevapta [soda lime, barium lime, taze granül ufalanabilir, doymuş granül sert, beyazdan mavi-mora dönme] yer almalıdır.",
        "slayt_no": 25
    },
    {
        "soru_id": "au_ekip_017",
        "soru": "Anestezi cihazının sadece anestezi için değil, kritik acil hastalarda ventilasyon amacıyla nasıl kullanıldığını açıklayınız.",
        "ideal_cevap": "Anestezi cihazları acil veya kritik kardiyorespiratuvar yetmezlikteki hastalarda oksijen ventilasyonu sağlamak için mükemmel bir platformdur. Bu amaçla kullanıldığında anestezi cihazının vaporizatörü kesinlikle 'KAPALI' konumda tutulur; böylece sisteme anestezik madde karışmaz. Yalnızca flowmetreden oksijen akışı açılarak maske aracılığıyla veya entübe edilen hastalarda doğrudan endotrakeal tüp üzerinden saf oksijen ventilasyonu uygulanır.",
        "degerlendirme_kriteri": "Cevapta [vaporizatörün kapalı tutulması, flowmetreden saf oksijen akışı, maske veya entübasyon ile saf O2 desteği] yer almalıdır.",
        "slayt_no": 11
    },
    {
        "soru_id": "au_ekip_018",
        "soru": "Rezerv balonunun hayvanın nefes alma ve verme döngüsündeki hacimsel değişimini ve tek yönlü valflerle koordinasyonunu açıklayınız.",
        "ideal_cevap": "Gaz akışı sürdükçe taze gaz rezerv balonuna dolar. Hayvan inspirasyon yaptığında gazın bir kısmı inhalasyon valfini açarak hayvana gideceğinden rezerv balonunun hacminde azalma (boşalma) meydana gelir. Ekspirasyon anında ise hasta nefesini ekspirasyon valfinden kanistere doğru verirken, flowmetreden gelen taze gaz rezerv balonunu tekrar doldurur. Böylece rezerv balonu her nefeste düzenli olarak bir miktar boşalır ve ardından yeniden şişer.",
        "degerlendirme_kriteri": "Cevapta [inspirasyonda balonun boşalması/hacim azalması, ekspirasyonda ve taze gazla yeniden dolması, döngüsel inip kalkma] yer almalıdır.",
        "slayt_no": 16
    },
    {
        "soru_id": "au_ekip_019",
        "soru": "İnhalasyon anestezi hazırlığında laringoskop, lidokain sprey ve göz pomadının kullanılma gerekçelerini açıklayınız.",
        "ideal_cevap": "1) Laringoskop: Epiglottisi ekarte edip vokal kordları ve glottisi aydınlatarak körleme olmadan atravmatik entübasyon sağlar. 2) Lidokain sprey: Özellikle kedilerde aşırı hassas olan laringeal refleksleri baskılamak ve entübasyon esnasında ölümcül laringospazmı önlemek için larinkse sıkılır. 3) Göz pomadı/damlası: Anestezide lakrimal sekresyon azaldığı ve göz kapakları açık kaldığı için korneanın kurumasını, kornea ülseri ve keratit şekillenmesini önlemek amacıyla her iki göze rutin uygulanır.",
        "degerlendirme_kriteri": "Cevapta [laringoskop ile glottis görüşü, kedide lidokain sprey ile laringospazm önleme, göz pomadı ile kornea kuruluğunu önleme] yer almalıdır.",
        "slayt_no": 3
    },
    {
        "soru_id": "au_ekip_020",
        "soru": "Anestezi devresinde 'atık gaz sistemi' (scavenging system) neden zorunlu bir ekipmandır ve hangi valf üzerinden çalışır?",
        "ideal_cevap": "İnhalasyon anestezikleri (izofluran, halotan vb.) ameliyathane ortamına salındığında cerrahi ekipte baş ağrısı, yorgunluk, hepatotoksisite, teratojenite ve spontan abortus gibi mesleki sağlık risklerine yol açar. Atık gaz sistemi, pop-off valfinden tahliye edilen fazla anestezi gazlarını ve ekspirasyon havasını toplayarak aktif veya pasif tahliye hatlarıyla bina dışına atar; böylece ameliyathane havasının kirlenmesi önlenir.",
        "degerlendirme_kriteri": "Cevapta [pop-off valfi bağlantısı, ameliyathane hava kirliliğini önleme, cerrahi ekibin mesleki toksisiteden korunması, bina dışına tahliye] yer almalıdır.",
        "slayt_no": 24
    }
]

COKTAN_SECMELI_SORULAR = [
    {
        "soru_id": "mcq_ekip_001",
        "soru_metni": "Anestezik maddelerin uygulanması için anestezi cihazlarında özel buharlaştırıcı sistemlere (vaporizatör) gereksinim duyulmasının temel nedeni nedir?",
        "secenekler": {
            "A": "Anestezik maddelerin oda ısısında katı kristal halde bulunması",
            "B": "Anestezik maddelerin likid (sıvı) halde olmaları",
            "C": "Anestezik maddelerin sadece damar içi enjeksiyonla verilebilmesi",
            "D": "Gaz moleküllerinin kanda çözünememesi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; anestezik maddeler likid haldedirler ve uygulanabilmeleri için özel buharlaştırıcı sistemlere (vaporizatör) gereksinim vardır (Slayt 2).",
            "celdirici_analizi": "A şıkkı katı değildir; likittir. C ve D şıkları bilimsel olarak yanlıştır."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "kolay",
        "etiketler": ["likid_anestezik", "vaporizator"]
    },
    {
        "soru_id": "mcq_ekip_002",
        "soru_metni": "Anestezi cihazlarının türlere uyumu konusunda aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "secenekler": {
            "A": "İnsanlar için dizayn edilmiş anestezi cihazları at ve sığırlarda doğrudan kullanılabilir",
            "B": "İnsanlar için dizayn edilmiş anestezi cihazları kedi ve köpek gibi küçük hayvanlar için uygundur, ancak at ve sığırlar için özel dizayn edilmiş cihazlar gerekir",
            "C": "Kedi ve köpekler için sadece açık gazlı bez yöntemi kullanılır",
            "D": "Büyük hayvanlarda anestezi cihazına hiçbir zaman ihtiyaç duyulmaz"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; insan cihazları kedi ve köpeğe uygundur ancak büyük hayvanlar için özel tasarlanmış büyük anestezi cihazları gereklidir (Slayt 2).",
            "celdirici_analizi": "İnsan cihazı atın 30 L'lik solunum hacmini karşılayamaz."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "kolay",
        "etiketler": ["cihaz_uyumu", "tur_ozelligi"]
    },
    {
        "soru_id": "mcq_ekip_003",
        "soru_metni": "Eskiden uygulanan eter damlatma yönteminin günümüzdeki kullanım alanı ve yerini alan modern sistem hangisidir?",
        "secenekler": {
            "A": "At anestezisinde kullanılır / Yerini enjeksiyona bırakmıştır",
            "B": "Daha çok laboratuvar hayvanlarında kullanılır / Yerini vaporizatörlü anestezi cihazlarına bırakmıştır",
            "C": "Rutin kedi cerrahisinde kullanılır / Yerini elektrokoter almıştır",
            "D": "Tamamen yasaklanmıştır / Yerini lokal anestezi almıştır"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; eter damlatma artık laboratuvar hayvanlarında kullanılır; modern cerrahide vaporizatörlerle buharlaştırılıp verilir (Slayt 2).",
            "celdirici_analizi": "Slayt 2'de açıkça belirtilen tarihsel ve klinik gelişimdir."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "kolay",
        "etiketler": ["eter", "vaporizator"]
    },
    {
        "soru_id": "mcq_ekip_004",
        "soru_metni": "İnhalasyon anestezi hazırlığında özellikle kedilerde entübasyon esnasında larinkse uygulanmak üzere hazır bulundurulan lokal anestezik sprey hangisidir?",
        "secenekler": {
            "A": "Bupivakain sprey",
            "B": "Lidokain (Lidocaine) sprey",
            "C": "Prokain sprey",
            "D": "Artikain sprey"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ekipman listesinde yer alan lokal anestezik Lidokain spreydir (Slayt 3).",
            "celdirici_analizi": "Lidokain sprey kedilerde laringospazmı engellemek için larinks vokal kordlarına sıkılır."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "kolay",
        "etiketler": ["ekipman", "lidokain_sprey"]
    },
    {
        "soru_id": "mcq_ekip_005",
        "soru_metni": "Aşağıdakilerden hangisi inhalasyon anestezisinde kullanılan temel ekipman ve aletlerden biri DEĞİLDİR?",
        "secenekler": {
            "A": "Laringoskop ve endotrakeal tüpler",
            "B": "Göz pomadı ve damlaları",
            "C": "Oksijen tankı ve atık gaz sistemi",
            "D": "Kemik iliği biyopsi iğnesi"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği anestezi hazırlık ekipman listesinde yer almaz (Slayt 3, 4).",
            "celdirici_analizi": "A, B ve C seçenekleri Slayt 3 ve 4'te listelenen temel anestezi ekipmanlarıdır."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "kolay",
        "etiketler": ["ekipman_listesi"]
    },
    {
        "soru_id": "mcq_ekip_006",
        "soru_metni": "Veteriner hekimlikte en sık kullanılan turuncu renkli kauçuk endotrakeal tüplerin temel dezavantajı hangisidir?",
        "secenekler": {
            "A": "Hiç esnek olmaması ve kırılması",
            "B": "Dezenfektan solüsyonları absorbe edebilmeleri, zamanla yüzeyinde çatlak ve matlaşma olması ve kolayca kıvrılıp kollabe olabilmeleri",
            "C": "Fiyatlarının aşırı pahalı olması",
            "D": "İçlerinden oksijen gazının geçememesi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kauçuk tüpler dezenfektanları emer, çatlar, kurur ve ince çaplıları kolayca kıvrılıp tıkanabilir (Slayt 5).",
            "celdirici_analizi": "A şıkkı yanlıştır (aşırı esnektir); C şıkkı yanlıştır (aksine ucuzdur)."
        },
        "slayt_no": 5,
        "zorluk_derecesi": "orta",
        "etiketler": ["kaucuk_tup", "dezavantaj"]
    },
    {
        "soru_id": "mcq_ekip_007",
        "soru_metni": "Dış baskılardan etkilenmeyen, ezilmeyen ve kıvrılmayan yapıya sahip kuvvetlendirilmiş tüplerin üretiminde ne kullanılır?",
        "secenekler": {
            "A": "Ahşap çıtalar",
            "B": "Spiral metal ya da plastik teller",
            "C": "Cam lifleri",
            "D": "Kurşun plakalar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; spiral metal ya da plastik teller kullanılarak kuvvetlendirilmiş tüpler (armored tüpler) dış baskılardan etkilenmez ve kıvrılmaz (Slayt 5).",
            "celdirici_analizi": "Spiral tel desteği tüp lümeninin bükülmesini ve tıkanmasını engeller."
        },
        "slayt_no": 5,
        "zorluk_derecesi": "kolay",
        "etiketler": ["spiral_tup", "armored"]
    },
    {
        "soru_id": "mcq_ekip_008",
        "soru_metni": "Şeffaf (transparent) görünümlü, yüzeyinde çatlak meydana gelmeyen ancak kauçuk tüplere göre daha sert olan endotrakeal tüp türü hangisidir?",
        "secenekler": {
            "A": "Kauçuk tüp",
            "B": "Vinil plastik tüp",
            "C": "Silikon tüp",
            "D": "Lateks tüp"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; vinil plastik tüpler transparent görünümdedir, çatlamaz ancak kauçuğa göre daha serttir (Slayt 6).",
            "celdirici_analizi": "Şeffaflık ve çatlamama vinil plastiğin ayırıcı özelliğidir."
        },
        "slayt_no": 6,
        "zorluk_derecesi": "orta",
        "etiketler": ["vinil_tup", "ozellikler"]
    },
    {
        "soru_id": "mcq_ekip_009",
        "soru_metni": "Pahalı olmasına rağmen veteriner anesteziyolojide 'EN ÇOK TERCİH EDİLMESİ GEREKEN', yumuşak, esnek ve en az irritan endotrakeal tüp hangisidir?",
        "secenekler": {
            "A": "Vinil plastik tüpler",
            "B": "Kauçuk tüpler",
            "C": "Silikonlu kauçuktan yapılmış tüpler",
            "D": "Alüminyum tüpler"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; silikonlu kauçuk tüpler pahalıdır ancak yumuşak, esnek ve en az irritan oldukları için en çok tercih edilmesi gereken tüplerdir (Slayt 6).",
            "celdirici_analizi": "Slayt 6'da kırmızıyla vurgulanmış kritik sınav bilgisidir."
        },
        "slayt_no": 6,
        "zorluk_derecesi": "kolay",
        "etiketler": ["silikon_tup", "en_iyi_tercih"]
    },
    {
        "soru_id": "mcq_ekip_010",
        "soru_metni": "Veteriner hekimlikte kullanılan Murphy endotrakeal tüpünü Magill tüpünden ayıran karakteristik anatomik özellik hangisidir?",
        "secenekler": {
            "A": "Tüpün tamamen düz olması",
            "B": "Distal ucuna yakın gövdesinde bir delik bulunması (Murphy deliği)",
            "C": "Kafının bulunmaması",
            "D": "Sadece metalden üretilmesi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Murphy türündeki tüplerin distal ucuna yakın bölgesinde tüpün gövdesinde bir delik (Murphy deliği) mevcuttur (Slayt 7).",
            "celdirici_analizi": "Magill tüplerinde bu yan delik yoktur."
        },
        "slayt_no": 7,
        "zorluk_derecesi": "kolay",
        "etiketler": ["murphy_tupu", "murphy_deligi"]
    },
    {
        "soru_id": "mcq_ekip_011",
        "soru_metni": "Endotrakeal tüplerde bulunan 'Murphy deliği'nin temel işlevi nedir?",
        "secenekler": {
            "A": "Kafı şişirmek için hava girişi sağlamak",
            "B": "Tüp ucunun mukus ya da trakea çeperine değerek tıkanması durumunda alternatif bir açıklık sağlamak",
            "C": "İçine stete sokulmasını engellemek",
            "D": "Tüpün ağırlığını azaltmak"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; tüp ucu tıkandığında alternatif bir açıklık sağlayarak hastanın havasız kalmasını önler (Slayt 7).",
            "celdirici_analizi": "A şıkkı pilot balona aittir; C ve D işlevsiz çeldiricilerdir."
        },
        "slayt_no": 7,
        "zorluk_derecesi": "kolay",
        "etiketler": ["murphy_deligi", "islev"]
    },
    {
        "soru_id": "mcq_ekip_012",
        "soru_metni": "Ağız içinde yapılacak cerrahi operasyonlarda endotrakeal tüpün hangi yolla uygulanması tercih edilebilir?",
        "secenekler": {
            "A": "Oral yol",
            "B": "Nazal uygulama yolu",
            "C": "Rektal yol",
            "D": "Özefagal yol"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ağız içinde yapılacak operasyonlarda nazal uygulama yolu tercih edilebilir (Slayt 7).",
            "celdirici_analizi": "Rutin oraldir ancak ağız cerrahisinde ağız boşluğunu rahatlatmak için nazal tercih edilir."
        },
        "slayt_no": 7,
        "zorluk_derecesi": "orta",
        "etiketler": ["entubasyon_yolu", "nazal"]
    },
    {
        "soru_id": "mcq_ekip_013",
        "soru_metni": "Kaflı endotrakeal tüplerde kafın temel görevi hangisinde doğru tanımlanmıştır?",
        "secenekler": {
            "A": "Tüpün trakeadan kayıp mideye gitmesini sağlamak",
            "B": "Endotrakeal tüpün dış çeperi ile trakea arasında bir tıpa görevi görmek",
            "C": "Oksijen üretimini artırmak",
            "D": "Tüpün sıcaklığını vücut sıcaklığına eşitlemek"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kaf endotrakeal tüpün dış çeperi ile trakea arasında bir tıpa (mühür) görevi görür (Slayt 7).",
            "celdirici_analizi": "Hava ve sıvı geçişini bloke eden mekanik bariyerdir."
        },
        "slayt_no": 7,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kaf", "islev"]
    },
    {
        "soru_id": "mcq_ekip_014",
        "soru_metni": "Aşağıdakilerden hangisi kaflı endotrakeal tüp kullanılmasının sağladığı avantajlardan biri DEĞİLDİR?",
        "secenekler": {
            "A": "Ekspirasyon havasının odaya karışmasını önleyerek oda havasının atık gazlarla kirlenmesini önlemesi",
            "B": "Kan, mukus, salya veya kusmuğun akciğerlere kaçmasını önlemesi",
            "C": "İnspirasyonda hayvanın oda havasından solumasını engelleyerek anestezi derinliğinin korunmasını sağlaması",
            "D": "Kafın şişirilmesiyle hayvanın spontan solunum yapmasını tamamen durdurması"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği yanlıştır; kaf solunumu durdurmaz, sadece hava yolu sızdırmazlığını sağlar (Slayt 8).",
            "celdirici_analizi": "A, B ve C seçenekleri slayt 8'de sıralanan kaflı tüpün temel avantajlarıdır."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "orta",
        "etiketler": ["kaf_avantajlari"]
    },
    {
        "soru_id": "mcq_ekip_015",
        "soru_metni": "Endotrakeal tüpün kafı çok fazla şişirilecek olursa özellikle küçük hayvanlarda ve uzun süreli anestezide hangi komplikasyon şekillenir?",
        "secenekler": {
            "A": "Trakeanın iç çeperinde basınç nekrozu",
            "B": "Midede aşırı gaz birikmesi",
            "C": "Göz tansiyonunun düşmesi",
            "D": "Dilde kangren"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kaf aşırı şişirilirse trakeanın iç çeperinde basınç nekrozu oluşabilir (Slayt 8).",
            "celdirici_analizi": "Mukozal iskemi trakea perforasyonuna ve nekroza yol açabilir."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "orta",
        "etiketler": ["kaf_dezavantaj", "basinc_nekrozu"]
    },
    {
        "soru_id": "mcq_ekip_016",
        "soru_metni": "Tabloya göre 3 kg ağırlığındaki bir kedide kullanılması gereken endotrakeal tüpün iç çapı (internal çap) kaç mm'dir?",
        "secenekler": {
            "A": "1.5 - 2 mm",
            "B": "3 - 3.5 mm",
            "C": "5 - 6 mm",
            "D": "7 - 8 mm"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 3 kg kedi için internal çap 3 - 3.5 mm'dir (Slayt 9).",
            "celdirici_analizi": "1 kg kedi: 2.5-3; 3 kg kedi: 3-3.5; 5 kg kedi: 4-4.5 mm."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "kolay",
        "etiketler": ["cap_tablosu", "kedi"]
    },
    {
        "soru_id": "mcq_ekip_017",
        "soru_metni": "Tabloya göre 14 kg ağırlığındaki bir köpekte tercih edilmesi gereken endotrakeal tüp internal çapı kaç mm'dir?",
        "secenekler": {
            "A": "4 mm",
            "B": "6 mm",
            "C": "8 mm",
            "D": "12 mm"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; 14 kg köpekte internal çap 8 mm'dir (Slayt 9).",
            "celdirici_analizi": "Slayt 9 tablosunda 14 kg köpek için net 8 mm belirtilmiştir."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "orta",
        "etiketler": ["cap_tablosu", "kopek"]
    },
    {
        "soru_id": "mcq_ekip_018",
        "soru_metni": "Tabloya göre 400 - 600 kg canlı ağırlığındaki bir at veya sığırda kullanılacak endotrakeal tüp iç çapı kaç mm olmalıdır?",
        "secenekler": {
            "A": "10 - 12 mm",
            "B": "14 - 16 mm",
            "C": "22 - 26 mm",
            "D": "35 - 40 mm"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; 400-600 kg at ve sığırda 22-26 mm internal çap kullanılır (Slayt 9).",
            "celdirici_analizi": ">600 kg için ise 26 mm kullanılır."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "orta",
        "etiketler": ["cap_tablosu", "at_sigir"]
    },
    {
        "soru_id": "mcq_ekip_019",
        "soru_metni": "Anestezi cihazında volatil likid anesteziklerin hastaya ulaştırılmasında sistemden geçen hangi gazlar 'taşıyıcı' görevi üstlenir?",
        "secenekler": {
            "A": "Yalnızca karbondioksit",
            "B": "Oksijen ya da oksijen + nitrous oxide (N2O) karışımı",
            "C": "Saf azot gazı",
            "D": "Helyum ve argon karışımı"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; sistemden geçen oksijen veya oksijen+N2O karışımı volatil anestezikler için taşıyıcı görevi üstlenir (Slayt 10).",
            "celdirici_analizi": "Oksijen akımı olmadan gaz taşınamaz."
        },
        "slayt_no": 10,
        "zorluk_derecesi": "kolay",
        "etiketler": ["tasiyici_gaz", "oksijen"]
    },
    {
        "soru_id": "mcq_ekip_020",
        "soru_metni": "Kritik durumdaki hastalarda anestezi cihazı ile saf oksijen ventilasyonu yaptırılacağı zaman cihaz üzerinde hangi parça 'KAPALI' tutulmalıdır?",
        "secenekler": {
            "A": "Flowmetre",
            "B": "Vaporizatör",
            "C": "Oksijen tüpü",
            "D": "İnspirasyon valfi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kritik hastalarda sadece oksijen ventilasyonu yaptırılırken anestezi cihazının vaporizatörü kapalı halde tutulmalıdır (Slayt 11).",
            "celdirici_analizi": "Vaporizatör kapalı tutulmazsa kritik hastaya anestezik gaz gider."
        },
        "slayt_no": 11,
        "zorluk_derecesi": "orta",
        "etiketler": ["oksijen_ventilasyonu", "vaporizator"]
    },
    {
        "soru_id": "mcq_ekip_021",
        "soru_metni": "Anestezi hastasında Nitrous oxide (N2O) kullanılmayacak ise oksijen hangi konsantrasyonda uygulanır?",
        "secenekler": {
            "A": "%21 konsantrasyonda",
            "B": "%50 konsantrasyonda",
            "C": "%100 konsantrasyonda",
            "D": "%5 konsantrasyonda"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; N2O kullanılmayacaksa oksijen %100 konsantrasyonda uygulanır (Slayt 12).",
            "celdirici_analizi": "Oda havası %21'dir; saf O2 kaynağı %100 sağlar."
        },
        "slayt_no": 12,
        "zorluk_derecesi": "kolay",
        "etiketler": ["oksijen_konsantrasyonu"]
    },
    {
        "soru_id": "mcq_ekip_022",
        "soru_metni": "Anestezi hastasında yüksek konsantrasyonda oksijen kullanılmasının iki temel yararlı etkisi hangisinde doğru verilmiştir?",
        "secenekler": {
            "A": "Vücut ısısını artırması ve kan basıncını yükseltmesi",
            "B": "Anestezi hastasının daha yüksek oksijene gereksinim duyması ve azalan tidal volüm nedeniyle hipoksinin önlenmesi",
            "C": "Mide asiditesini nötralize etmesi ve kas spazmını çözmesi",
            "D": "Göz bebeklerini daraltması ve nabzı sıfırlaması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; anestezi hastasının oksijen ihtiyacı yüksektir ve tidal volüm azaldığı için yüksek konsantrasyon O2 hayati fayda sağlar (Slayt 12).",
            "celdirici_analizi": "Slayt 12'de iki madde halinde açıkça vurgulanmıştır."
        },
        "slayt_no": 12,
        "zorluk_derecesi": "orta",
        "etiketler": ["oksijen_yararlari", "fizyoloji"]
    },
    {
        "soru_id": "mcq_ekip_023",
        "soru_metni": "Anestezi cihazında kullanılan oksijen gaz silindirinin (tüpünün) vanası hangi yöne doğru açılarak gaz akışı başlatılır?",
        "secenekler": {
            "A": "Sağa doğru",
            "B": "Sola doğru",
            "C": "Yukarı doğru çekilerek",
            "D": "Aşağı bastırılarak"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; vananın sola doğru açılması ile anestezi cihazına gaz akışı başlar; sağa doğru kapatılır (Slayt 13).",
            "celdirici_analizi": "Tüm gaz vanalarında sola açma (saat yönü tersi), sağa kapama kuralı geçerlidir."
        },
        "slayt_no": 13,
        "zorluk_derecesi": "kolay",
        "etiketler": ["oksijen_tupu", "vana"]
    },
    {
        "soru_id": "mcq_ekip_024",
        "soru_metni": "Anestezi cihazında hastaya ulaşacak gazın dakikadaki miktar ayarının yapıldığı parça hangisidir ve gaz akışı hangi birimle sağlanır?",
        "secenekler": {
            "A": "Vaporizatör / Yüzde (%)",
            "B": "Flowmetre / Dakikada litre (L/dk)",
            "C": "Rezerv balonu / Mililitre (ml)",
            "D": "Pop-off valf / Bar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; flowmetre gaz miktarını ayarlar ve gaz akışı dakikada litre (L/dk) olarak sağlanır (Slayt 14).",
            "celdirici_analizi": "Vaporizatör konsantrasyonu (yüzde) ayarlar; flowmetre akımı (L/dk) ayarlar."
        },
        "slayt_no": 14,
        "zorluk_derecesi": "kolay",
        "etiketler": ["flowmetre", "akinti_birimi"]
    },
    {
        "soru_id": "mcq_ekip_025",
        "soru_metni": "Oksijen tankı açılmasına rağmen anestezi cihazından hastaya gazın ulaşabilmesi için cihaz üzerinde ek olarak hangi parçanın vanası açılmalıdır?",
        "secenekler": {
            "A": "Pop-off valfi",
            "B": "Flowmetre",
            "C": "Atık gaz filtresi",
            "D": "Karbondioksit kanisteri"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; tek başına oksijen tankının açılması yetmez, cihaz üzerinde bulunan flowmetrenin de vanasının açılması gereklidir (Slayt 14).",
            "celdirici_analizi": "Flowmetre hattın akış musluğudur."
        },
        "slayt_no": 14,
        "zorluk_derecesi": "kolay",
        "etiketler": ["flowmetre", "gaz_akisi"]
    },
    {
        "soru_id": "mcq_ekip_026",
        "soru_metni": "Flowmetreden gaz akışı kapatılır ise vaporizatör ve volatil anestezik maddeye ne olur?",
        "secenekler": {
            "A": "Volatil likid anestezik madde buharlaşamaz ve sisteme giremez",
            "B": "Anestezik madde kendiliğinden kaynayıp patlar",
            "C": "Konsantrasyonu %100'e çıkarak hastayı zehirler",
            "D": "Rezerv balonunu aşırı derecede şişirir"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; flowmetreden gaz akışı kapatılırsa volatil likid anestezik madde buharlaşamaz ve sisteme giremez (Slayt 15).",
            "celdirici_analizi": "Buharlaşma gaz geçişi ile sürdürülür."
        },
        "slayt_no": 15,
        "zorluk_derecesi": "orta",
        "etiketler": ["vaporizator", "buharlasma"]
    },
    {
        "soru_id": "mcq_ekip_027",
        "soru_metni": "Kedi ve yavru köpek gibi küçük cüsseli hayvanlarda kullanılan rezerv balonlarının standart hacmi ne kadardır?",
        "secenekler": {
            "A": "100 ml",
            "B": "500 ml",
            "C": "3 Litre",
            "D": "30 Litre"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; küçük cüsseli hayvanlarda (kedi, köpek yavrusu) 500 ml hacimli balonlar kullanılır (Slayt 16).",
            "celdirici_analizi": "Köpekte 1-2 L, at ve sığırda 30 L'dir."
        },
        "slayt_no": 16,
        "zorluk_derecesi": "kolay",
        "etiketler": ["rezerv_balonu", "hacim_kedi"]
    },
    {
        "soru_id": "mcq_ekip_028",
        "soru_metni": "At ve sığırlarda kullanılan anestezi rezerv balonlarının hacmi ne kadardır?",
        "secenekler": {
            "A": "2 Litre",
            "B": "5 Litre",
            "C": "10 Litre",
            "D": "30 Litre"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği doğrudur; at ve sığırlarda çok daha hacimli 30 litrelik rezerv balonları kullanılır (Slayt 16).",
            "celdirici_analizi": "Büyük hayvanların yüksek tidal volümü için 30 L zorunludur."
        },
        "slayt_no": 16,
        "zorluk_derecesi": "kolay",
        "etiketler": ["rezerv_balonu", "at_sigir"]
    },
    {
        "soru_id": "mcq_ekip_029",
        "soru_metni": "Köpeklerde sıklıkla tercih edilen rezerv balonu hacmi aşağıdakilerden hangisidir?",
        "secenekler": {
            "A": "200 ml",
            "B": "1 - 2 Litre",
            "C": "15 Litre",
            "D": "50 Litre"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; köpeklerde sıklıkla 1-2 litre hacmindeki rezerv balonları tercih edilir (Slayt 16).",
            "celdirici_analizi": "Slayt 16'nın son cümlesinde belirtilmiştir."
        },
        "slayt_no": 16,
        "zorluk_derecesi": "kolay",
        "etiketler": ["rezerv_balonu", "kopek"]
    },
    {
        "soru_id": "mcq_ekip_030",
        "soru_metni": "Anestezi sırasında rezerv balonunun hareketlerine bakılarak hangi parametreleri tayin etmek mümkün olur?",
        "secenekler": {
            "A": "Yalnızca vücut ısısını",
            "B": "Dakikadaki ventilasyon sayısını ve solunum hacmini",
            "C": "Kan şekeri ve hemoglobin değerini",
            "D": "İdrar miktarını"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; rezerv balonunun hareketine bakarak dakikadaki ventilasyon sayısı ve solunum hacmi tayin edilir (Slayt 17).",
            "celdirici_analizi": "Balon solunum derinliğini ve hızını doğrudan yansıtır."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "kolay",
        "etiketler": ["rezerv_balonu", "takip"]
    },
    {
        "soru_id": "mcq_ekip_031",
        "soru_metni": "Anestezi takibinde rezerv balonunun YETERLİ MİKTARDA HAREKET ETMEMESİ neyin kanıtıdır?",
        "secenekler": {
            "A": "Hastanın öldüğünün",
            "B": "Hastanın solunumunun bir kısmını oda havasından yaptığının (endotrakeal tüp kafının yetersiz şişirilmesine bağlı hava kaçağı olduğunun)",
            "C": "Vaporizatörün bozulduğunun",
            "D": "Oksijen tüpünün fazla dolu olduğunun"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; balonun yetersiz hareketi kafın yetersiz şişirilmesine bağlı oda havasından solunduğunu gösterir (Slayt 17).",
            "celdirici_analizi": "Kaf etrafından kaçak olunca balon yeterince inip kalkmaz."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "orta",
        "etiketler": ["rezerv_balonu", "hava_kacagi"]
    },
    {
        "soru_id": "mcq_ekip_032",
        "soru_metni": "Solunum depresyonu durumunda rezerv balonuna ılımlı basınç uygulanarak yapılan işleme ne ad verilir?",
        "secenekler": {
            "A": "Kardiyak defibrilasyon",
            "B": "Anestezist tarafından basınçlı ventilasyon yaptırılması",
            "C": "Endoskopik lavaj",
            "D": "Epidural anestezi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; rezerv balonuna ılımlı basınç uygulayarak anestezist tarafından yapay ventilasyon yaptırılır (Slayt 17, 18).",
            "celdirici_analizi": "Manuel IPPV (aralıklı pozitif basınçlı ventilasyon) sağlanır."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "kolay",
        "etiketler": ["manuel_ventilasyon", "ippv"]
    },
    {
        "soru_id": "mcq_ekip_033",
        "soru_metni": "Uzun anestezi uygulamalarında rezerv balonuna ılımlı basınç uygulanarak akciğerlerin şişirilmesi hangi patolojinin oluşmasını önler?",
        "secenekler": {
            "A": "Atelektazi",
            "B": "Amfizem",
            "C": "Pnömotoraks",
            "D": "Plevral efüzyon"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; ılımlı basınç uygulanarak atelektazinin (alveol kollapsının) oluşması önlenir (Slayt 18).",
            "celdirici_analizi": "Slayt 18'in ilk maddesinde net olarak belirtilmiştir."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "kolay",
        "etiketler": ["atelektazi", "rezerv_balonu"]
    },
    {
        "soru_id": "mcq_ekip_034",
        "soru_metni": "Genel anestezi altındaki bir hastada solunum ile inhale edilen gazın volümü (tidal volüm) yaklaşık ne oranda azalır?",
        "secenekler": {
            "A": "%5 oranında",
            "B": "%10 oranında",
            "C": "%50 oranında",
            "D": "%95 oranında"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; anestezi hastasındaki solunum ile inhale edilen gazın volümü %50 oranında azalır (Slayt 18).",
            "celdirici_analizi": "Bu nedenle aralıklı pozitif basınçla taze gazın alveollere ulaştırılması gerekir."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "orta",
        "etiketler": ["tidal_volum", "azalma_orani"]
    },
    {
        "soru_id": "mcq_ekip_035",
        "soru_metni": "Rezerv balonunun aşırı derecede şişmesi ve dolu tutulması hastada hangi tehlikeli sonuca neden olabilir?",
        "secenekler": {
            "A": "Vücut ısısının aşırı artmasına",
            "B": "Akciğer alveollerinin yırtılmasına (barotravma)",
            "C": "Midede ülser delinmesine",
            "D": "Kanda lökositlerin tükenmesine"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; aşırı derecede şiş olan rezerv balonu alveollerin yırtılmasına neden olabilir (Slayt 19).",
            "celdirici_analizi": "Yüksek devre basıncı doğrudan barotravmaya yol açar."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "kolay",
        "etiketler": ["asiri_sisme", "alveol_yirtilmasi"]
    },
    {
        "soru_id": "mcq_ekip_036",
        "soru_metni": "Rezerv balonunun aşırı doldurulmasını önlemek için sistem üzerinde hangi valf bir miktar açık bırakılmalıdır?",
        "secenekler": {
            "A": "Vaporizatör dolum kapağı",
            "B": "Atık gaz (pop-off) valfi",
            "C": "Oksijen flash valfi",
            "D": "İnspirasyon valfi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; balonun aşırı dolmasını önlemek için atık gaz (pop-off) valfi bir miktar açık bırakılmalıdır (Slayt 19).",
            "celdirici_analizi": "Pop-off valf fazla gazın tahliye kapısıdır."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "kolay",
        "etiketler": ["pop_off", "atik_gaz_valfi"]
    },
    {
        "soru_id": "mcq_ekip_037",
        "soru_metni": "Atık gaz valfinin (pop-off) tam olarak açık kalması rezerv balonunda neye yol açar?",
        "secenekler": {
            "A": "Balonun patlamasına",
            "B": "Rezerv balonunun tamamen sönmesine ve hastanın yeteri kadar nefes alamamasına",
            "C": "Anestezi gazının konsantrasyonunun iki katına çıkmasına",
            "D": "Oksijen tüpünün donmasına"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; atık gaz valfinin tam açık kalması rezerv balonunun tamamen sönmesine neden olur (Slayt 19).",
            "celdirici_analizi": "Balon tam sönerse hasta inspirasyonda gaz bulamaz."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "orta",
        "etiketler": ["balon_sonmesi", "pop_off"]
    },
    {
        "soru_id": "mcq_ekip_038",
        "soru_metni": "Hasta nefes aldığında açılan, gazın tek yönlü olarak sadece hastaya doğru yol almasını sağlayan valf hangisidir?",
        "secenekler": {
            "A": "Pop-off valfi",
            "B": "İnhalasyon valfi (İnspirasyon valfi)",
            "C": "Flash valfi",
            "D": "Kanister tahliye musluğu"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; hasta nefes aldığında inhalasyon valfi açılır ve gaz sadece hastaya doğru tek yönlü hareket eder (Slayt 20).",
            "celdirici_analizi": "İnspirasyon valfi tek yönlü bir geçiş klapesidir."
        },
        "slayt_no": 20,
        "zorluk_derecesi": "kolay",
        "etiketler": ["inhalasyon_valfi", "tek_yonlu"]
    },
    {
        "soru_id": "mcq_ekip_039",
        "soru_metni": "Ekspirasyon valfinin tek yönlü çalışmasının sisteme sağladığı en önemli katkı nedir?",
        "secenekler": {
            "A": "Ekspirasyonla atılan gazın karbondioksit tutucusundan (kanister) geçmeden hasta tarafından geri solunmasını engellemesi",
            "B": "Hastanın oksijen tüketimini sıfırlaması",
            "C": "Vaporizatördeki sıvı seviyesini artırması",
            "D": "Endotrakeal tüpün kafını otomatik şişirmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; ekspirasyon gazının karbondioksit tutucusundan geçmeden geri solunmasını engeller (Slayt 21).",
            "celdirici_analizi": "Valf gazın sadece hastadan cihaza doğru gitmesine izin verir."
        },
        "slayt_no": 21,
        "zorluk_derecesi": "orta",
        "etiketler": ["ekspirasyon_valfi", "co2_koruma"]
    },
    {
        "soru_id": "mcq_ekip_040",
        "soru_metni": "Anestezi cihazı üzerinde bulunan 'Oksijen Flash Valfi'ne (Flush) basıldığında oksijen nereye uğramadan doğrudan sisteme verilir?",
        "secenekler": {
            "A": "Basınç düşürücü regülatöre",
            "B": "Flowmetre ve vaporizatöre",
            "C": "Rezerv balonuna",
            "D": "Endotrakeal tüpe"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; flash valfe basıldığında oksijen flowmetre ve vaporizatöre gitmeden direkt olarak sisteme verilir (Slayt 22).",
            "celdirici_analizi": "Bu baypas sayesinde hatta saf oksijen hızla dolar."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "orta",
        "etiketler": ["oksijen_flash_valfi", "baypas"]
    },
    {
        "soru_id": "mcq_ekip_041",
        "soru_metni": "Aşağıdaki klinik durumlardan hangisinde Oksijen Flash Valfinin kullanılması yararlı DEĞİLDİR?",
        "secenekler": {
            "A": "Sisteme kısa sürede saf oksijen verilmesini gerektiren genel durumu kötü hastalarda",
            "B": "Rezerv balonu söndüğünde balonun kısa sürede doldurulmasında",
            "C": "Uyanma aşamasında sistemin anestezik gazlardan arındırılmasında",
            "D": "Non-rebreathing sistemlerde anestezi derinliğini anında artırmak amacıyla"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği yanlıştır; non-rebreathing sistemlerde flash valf akciğerleri patlatabileceğinden KULLANILMAMALIDIR (Slayt 22).",
            "celdirici_analizi": "A, B ve C şıkları Slayt 22'de flash valfin faydaları olarak sıralanmıştır."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "orta",
        "etiketler": ["flash_valf", "endikasyon_kontrendikasyon"]
    },
    {
        "soru_id": "mcq_ekip_042",
        "soru_metni": "Oksijen Flash Valfinin 'Non-rebreathing' sistemlerde KULLANILMAMASININ hayati nedeni nedir?",
        "secenekler": {
            "A": "Oksijen tankının anında boşalması",
            "B": "Balonun kısa sürede aşırı derecede şişmesine ve akciğerlerin bir anda zarar görmesine (barotravma) neden olabilmesi",
            "C": "Cihazın elektriğinin kesilmesi",
            "D": "Vaporizatördeki ilacın donması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; balonun aşırı şişmesine ve akciğerlerin bir anda zarar görmesine neden olabileceğinden kullanılmamalıdır (Slayt 22).",
            "celdirici_analizi": "Non-rebreathing devre hacmi çok küçüktür, yüksek akım doğrudan akciğere basar."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "zor",
        "etiketler": ["non_rebreathing", "flash_valf_yasak"]
    },
    {
        "soru_id": "mcq_ekip_043",
        "soru_metni": "Bütün anestezi cihazlarının üzerinde sistemin gazının boşaltılmasını ve basıncın düşürülmesini sağlayan valf sistemi hangisidir?",
        "secenekler": {
            "A": "Vaporizatör kontrol kadranı",
            "B": "Pop-off valf",
            "C": "İnspirasyon valfi",
            "D": "Regülatör emniyet pimi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; pop-off valf sistemin gazının boşaltılmasını ve basıncın düşürülmesini sağlar (Slayt 23).",
            "celdirici_analizi": "Sistemin basınç emniyet ve tahliye sübabıdır."
        },
        "slayt_no": 23,
        "zorluk_derecesi": "kolay",
        "etiketler": ["pop_off", "tanim"]
    },
    {
        "soru_id": "mcq_ekip_044",
        "soru_metni": "Pop-off valfinin kapalı ya da kapalıya yakın konumda tutulması halinde zorunlu kural nedir?",
        "secenekler": {
            "A": "Oksijen akışı maksimuma çıkarılmalıdır",
            "B": "Sisteme taze gaz akışı minimum seviyede sürdürülmelidir",
            "C": "Vaporizatör %5'e getirilmelidir",
            "D": "Rezerv balonu çıkarılmalıdır"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kapalı ya da kapalıya yakın tutulması halinde sisteme taze gaz akışı minimum seviyede sürdürülmelidir (Slayt 23).",
            "celdirici_analizi": "Aksi takdirde gaz sıkışarak rezerv balonunu patlatır."
        },
        "slayt_no": 23,
        "zorluk_derecesi": "orta",
        "etiketler": ["pop_off", "gaz_akisi"]
    },
    {
        "soru_id": "mcq_ekip_045",
        "soru_metni": "Anestezi sırasında Pop-off valfinin kapalı olduğu fark edilmezse hastada ne şekillenir?",
        "secenekler": {
            "A": "Hasta anında uyanır",
            "B": "Sistemde gaz basıncı aşırı artar, akciğerlerde aşırı basınç oluşur ve alveollerde yırtılmalar meydana gelir",
            "C": "Sistem vakum yaparak hastanın akciğerlerini büzer",
            "D": "Oksijen tüpü patlar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; aşırı gaz basıncı akciğerlerde aşırı basınca ve alveollerde yırtılmalara (barotravma) neden olur (Slayt 24).",
            "celdirici_analizi": "Slayt 24'te kelimesi kelimesine bu ölümcül tehlike vurgulanmıştır."
        },
        "slayt_no": 24,
        "zorluk_derecesi": "orta",
        "etiketler": ["pop_off_kapali", "alveol_yirtilmasi"]
    },
    {
        "soru_id": "mcq_ekip_046",
        "soru_metni": "Pop-off valfinin açık tutulması ile fazla gazlar nereye tahliye edilir?",
        "secenekler": {
            "A": "Vaporizatörün içine",
            "B": "Atık gaz sistemine (atık sistemine)",
            "C": "Oksijen tüpünün içine",
            "D": "Ameliyat masasının altına"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; pop-off valfin kullanılması ile atık gazların atık sistemine geçmesi sağlanır (Slayt 24).",
            "celdirici_analizi": "Atık gaz scavenging sistemine yönlendirilir."
        },
        "slayt_no": 24,
        "zorluk_derecesi": "kolay",
        "etiketler": ["pop_off", "atik_sistemi"]
    },
    {
        "soru_id": "mcq_ekip_047",
        "soru_metni": "Rebreathing sistemlerde ekspirasyon ile atılan gazlar tekrar solunmadan önce hangi parçadan geçerek karbondioksitten arındırılır?",
        "secenekler": {
            "A": "Vaporizatör",
            "B": "Karbondioksit tutucu kanister",
            "C": "Flowmetre",
            "D": "Basınç regülatörü"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ekspirasyon gazları tekrar alınmadan önce karbondioksit tutucu kanisterden geçerler (Slayt 25).",
            "celdirici_analizi": "Kanister karbondioksiti kimyasal olarak absorbe eder."
        },
        "slayt_no": 25,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kanister", "co2_tutucu"]
    },
    {
        "soru_id": "mcq_ekip_048",
        "soru_metni": "Karbondioksit tutucu kanister içinde CO2 tutma özelliğine sahip kimyasal madde olarak hangileri bulunur?",
        "secenekler": {
            "A": "Aktif kömür veya silika jel",
            "B": "Soda lime ya da baryum hidroksid lime (barium lime)",
            "C": "Sodyum bikarbonat veya potasyum klorür",
            "D": "Kalsiyum klorür ve magnezyum sülfat"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kanister içinde ya soda lime ya da baryum hidroksid lime bulunur (Slayt 25).",
            "celdirici_analizi": "Sodalime ve barium lime bazik karakterli CO2 emicilerdir."
        },
        "slayt_no": 25,
        "zorluk_derecesi": "kolay",
        "etiketler": ["sodalime", "barium_lime"]
    },
    {
        "soru_id": "mcq_ekip_049",
        "soru_metni": "Karbondioksit tutucu kanisterdeki granüllerin taze mi yoksa CO2 ile doymuş mu olduğu fiziksel olarak parmakla nasıl anlaşılır?",
        "secenekler": {
            "A": "Taze granüller parmaklar arasında kolayca ufalanıp parçalanabilir, ancak CO2 ile doymuş granüller sert ve dayanıklıdır",
            "B": "Taze olanlar demir gibi serttir, doymuş olanlar sıvılaşır",
            "C": "Her ikisi de her zaman hamur kıvamındadır",
            "D": "Parmakla dokunulduğunda taze granüller anında alev alır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; taze granüller kolayca ufalanırken CO2 ile doymuş granüller sert ve dayanıklıdır (Slayt 25).",
            "celdirici_analizi": "Karbondioksiti bağlayan kalsiyum karbonat taşlaşma gösterir."
        },
        "slayt_no": 25,
        "zorluk_derecesi": "orta",
        "etiketler": ["granul_fiziksel_test", "sodalime"]
    },
    {
        "soru_id": "mcq_ekip_050",
        "soru_metni": "Sodalime ya da barium lime granüllerinin kullanıldıkça ve karbondioksitle doydukça gösterdiği karakteristik renk değişimi hangisidir?",
        "secenekler": {
            "A": "Yeşilden kırmızıya",
            "B": "Beyazdan mavi-mora",
            "C": "Siyahtan sarıya",
            "D": "Maviden şeffafa"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; granüllerde renk değişimi kullanıldıkça mavi-mor şeklinde görülür (Slayt 25).",
            "celdirici_analizi": "Slayt 25'te parantez içinde açıkça '(kullanıldıkça mavi-mor)' olarak verilmiştir."
        },
        "slayt_no": 25,
        "zorluk_derecesi": "kolay",
        "etiketler": ["renk_degisimi", "mavi_mor"]
    },
    {
        "soru_id": "mcq_ekip_051",
        "soru_metni": "Bir hastanın anestezi sırasında kan, mukus veya kusmuk aspire etmesini önlemede en kritik anestezi ekipmanı hangisidir?",
        "secenekler": {
            "A": "Yüz maskesi",
            "B": "Kaflı endotrakeal tüp",
            "C": "Vaporizatör",
            "D": "Flowmetre"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kaflı endotrakeal tüp trakeayı tıkayarak sıvıların akciğere aspirasyonunu kesin olarak önler (Slayt 8).",
            "celdirici_analizi": "Yüz maskesi aspirasyonu engelleyemez."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "kolay",
        "etiketler": ["aspirasyon_onleme", "kaf"]
    },
    {
        "soru_id": "mcq_ekip_052",
        "soru_metni": "Anestezi devresinde 'Y' parçasının konumu ve görevi hangisinde doğru ifade edilmiştir?",
        "secenekler": {
            "A": "Oksijen tüpü ile flowmetre arasındadır / Basıncı düşürür",
            "B": "İnhalasyon ve ekspirasyon hortumları ile endotrakeal tüp arasındadır / Gaz iletimini sağlar",
            "C": "Vaporizatörün içinde yer alır / Sıvıyı ısıtır",
            "D": "Kanisterin altındadır / Su tahliyesi yapar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Y parçası solunum hortumları ile endotrakeal tüp arasında yer alır ve gaz geçişini sağlar (Slayt 4, 20).",
            "celdirici_analizi": "İnspirasyon ve ekspirasyon kollarını endotrakeal tüpe bağlar."
        },
        "slayt_no": 4,
        "zorluk_derecesi": "kolay",
        "etiketler": ["y_parcasi", "devre"]
    },
    {
        "soru_id": "mcq_ekip_053",
        "soru_metni": "Anestezi sırasında hastanın inspirasyonda oda havası soluması halinde klinik olarak ne gibi bir sorun ortaya çıkar?",
        "secenekler": {
            "A": "Anestezi anında derinleşir",
            "B": "Yeterli anestezi derinliğini sürdürmek zorlaşır ve hasta uyanma eğilimi gösterebilir",
            "C": "Vaporizatör donar",
            "D": "Kanisterdeki granüller anında erir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; hayvan oda havasından da soluyacak olursa yeterli anestezi derinliğini sürdürmek zorlaşır (Slayt 8).",
            "celdirici_analizi": "Oda havası anestezik konsantrasyonu sulandırır."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "orta",
        "etiketler": ["oda_havasi", "anestezi_derinligi"]
    },
    {
        "soru_id": "mcq_ekip_054",
        "soru_metni": "Tabloya göre 7 kg ve 9 kg ağırlığındaki köpeklerde kullanılması gereken endotrakeal tüp iç çapları sırasıyla hangileridir?",
        "secenekler": {
            "A": "7 kg: 4 mm / 9 kg: 5 mm",
            "B": "7 kg: 6 mm / 9 kg: 7 mm",
            "C": "7 kg: 8 mm / 9 kg: 9 mm",
            "D": "7 kg: 10 mm / 9 kg: 12 mm"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 7 kg köpek için 6 mm, 9 kg köpek için 7 mm iç çap kullanılır (Slayt 9).",
            "celdirici_analizi": "Slayt 9 tablosunda net olarak verilmiştir."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "kolay",
        "etiketler": ["cap_tablosu", "kopek_7_9kg"]
    },
    {
        "soru_id": "mcq_ekip_055",
        "soru_metni": "Anestezi cihazında hastaya yüksek konsantrasyonda oksijen sağlanamazsa hastada hangi klinik patoloji gelişir?",
        "secenekler": {
            "A": "Hiperoksi",
            "B": "Hipoksi",
            "C": "Alkalozis",
            "D": "Hipertermi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; artan oksijen ihtiyacı ve azalan tidal volüm hipoksiye neden olabilir (Slayt 13).",
            "celdirici_analizi": "Slayt 13'ün ilk maddesinde açıkça belirtilmiştir."
        },
        "slayt_no": 13,
        "zorluk_derecesi": "kolay",
        "etiketler": ["hipoksi", "oksijen_yetmezligi"]
    },
    {
        "soru_id": "mcq_ekip_056",
        "soru_metni": "Aşağıdakilerden hangisi anestezi sırasında rezerv balonunun sürekli gaz akış borularına göre hastaya sağladığı doğrudan bir avantajdır?",
        "secenekler": {
            "A": "Anestezi hastasının sürekli gaz akış borularına göre rezerv balonundan nefes almasının daha kolay olması",
            "B": "Hastanın gözlerini nemlendirmesi",
            "C": "Vücut ısısını 40 dereceye çıkarması",
            "D": "Kalp atımını iki katına çıkarması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; sürekli gaz akışını sağlayan borular sistemine göre rezerv balonundan nefes alması daha kolaydır (Slayt 17).",
            "celdirici_analizi": "Esnek balon solunum iş yükünü (work of breathing) azaltır."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "orta",
        "etiketler": ["rezerv_balonu", "solunum_kolayligi"]
    },
    {
        "soru_id": "mcq_ekip_057",
        "soru_metni": "Karbondioksit tutucu kanisterdeki sodalime ya da barium lime granüllerinin kullanım süresiyle ilgili hangisi DOĞRUDUR?",
        "secenekler": {
            "A": "Granüllerin kullanımı sınırsızdır, asla tükenmez",
            "B": "Granüller belirli bir kullanım süresi sonrasında karbondioksit tutma görevlerini yapamazlar ve değiştirilmeleri gerekir",
            "C": "Granüller her 5 dakikada bir mutlaka çöpe atılmalıdır",
            "D": "Granüller suyla yıkanıp kurutularak tekrar tekrar kullanılabilir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; granüller belirli bir kullanım süresi sonrasında karbondioksit tutma görevini yapamazlar (Slayt 25).",
            "celdirici_analizi": "Doygunluğa ulaştığında kimyasal bağlanma sona erer."
        },
        "slayt_no": 25,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kanister_omru", "degisim"]
    },
    {
        "soru_id": "mcq_ekip_058",
        "soru_metni": "Anestezi cihazında gaz silindirinin vanasının sağa doğru çevrilmesi ne anlama gelir?",
        "secenekler": {
            "A": "Gaz akışının hızlandırılması",
            "B": "Gazın tamamen kapatılması",
            "C": "Gazın ısıtılması",
            "D": "Gazın N2O ile karıştırılması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; vananın sağa doğru kapatılması ile gazın gelmesi tamamen kapatılır (Slayt 13).",
            "celdirici_analizi": "Sola açılır, sağa kapatılır."
        },
        "slayt_no": 13,
        "zorluk_derecesi": "kolay",
        "etiketler": ["vana", "kapama"]
    },
    {
        "soru_id": "mcq_ekip_059",
        "soru_metni": "Tabloya göre 200 - 300 kg ağırlığındaki bir tay veya sığırda kullanılacak endotrakeal tüp internal çapı kaç mm'dir?",
        "secenekler": {
            "A": "8 - 10 mm",
            "B": "14 - 16 mm",
            "C": "26 mm",
            "D": "4 - 5 mm"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 200-300 kg canlı ağırlık için internal çap 14-16 mm'dir (Slayt 9).",
            "celdirici_analizi": "Slayt 9 tablosundaki değerdir."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "orta",
        "etiketler": ["cap_tablosu", "200_300kg"]
    },
    {
        "soru_id": "mcq_ekip_060",
        "soru_metni": "İnhalasyon anestezi devresinde endotrakeal tüpün doğru olarak trakea içine yerleştirildiğinin pratik klinik kanıtı nedir?",
        "secenekler": {
            "A": "Vaporizatörün ses çıkarması",
            "B": "Rezerv balonunun yeterli ve senkron hareketi",
            "C": "Oksijen tüpünün basıncının artması",
            "D": "Kanisterin anında maviye dönmesi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; rezerv balonunun yeterli hareketi endotrakeal tüpün doğru olarak trakea içine yerleştirildiğini gösterir (Slayt 17).",
            "celdirici_analizi": "Tüp özefagusta olsaydı balon nefesle senkron inip kalkmazdı."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "kolay",
        "etiketler": ["rezerv_balonu", "dogru_entubasyon"]
    }
]

print(f"Anestezi Ekipmanları modülü hazırlandı:")
print(f"- Summary Sections: {len(SUMMARY_SECTIONS)}")
print(f"- Bilgi Kartları: {len(BILGI_KARTLARI)}")
print(f"- Açık Uçlu Sorular: {len(ACIK_UCLU_SORULAR)}")
print(f"- Çoktan Seçmeli Sorular: {len(COKTAN_SECMELI_SORULAR)}")
