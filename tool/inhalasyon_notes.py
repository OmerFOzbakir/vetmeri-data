# -*- coding: utf-8 -*-
"""
VetMeri - 6. Ders: İnhalasyon Anesteziklerinin Özellikleri
Kapsam: 24 Slayt (Alım-Dağılım-Atılım, Beyin Parsiyel Basıncı, MAC Tanımı ve Güç İlişkisi, Uygulama Teknikleri [Açık, Yarı Açık, Fanus, Entübasyon],
İdeal Anestezik Özellikleri, Eter, N2O, Halotan, Enfluran, İzofluran, Sevofluran, Desfluran)
"""

METADATA = {
    "id": "inhalasyon",
    "name": "6. Ders: İnhalasyon Anestezikleri & Farmakolojisi",
    "shortName": "İnhalasyon Anestezikleri",
    "icon": "🌬️",
    "badge": "24 Slayt • MAC, Alım-Atılım, Halotan, İzofluran & Sevofluran",
    "kategori": "Veteriner Cerrahi ve Anesteziyoloji",
    "alt_kategori": "İnhalasyon Ajanları, Farmakokinetik, MAC ve Karşılaştırmalı Farmakoloji",
    "ozet": "Bu eğitim modülü; inhalasyon anesteziklerinin vücuda alım, beyne difüzyon ve akciğerlerden atılım mekanizmalarını, MAC (Minimum Alveoler Konsantrasyon) kavramını ve anestezik güçle ters orantısını, uygulama tekniklerini (açık, yarı açık, fanus, endotrakeal entübasyon) ve klinik kullanımda yer alan tüm anestezik ajanların (Eter, N2O, Halotan, Enfluran, İzofluran, Sevofluran, Desfluran) farmakolojik özelliklerini, avantajlarını ve organ toksisitelerini kapsamaktadır.",
    "kilit_noktalar": [
        "İnhalasyon anestezikleri vücuda akciğer yoluyla girer ve büyük oranda metabolize olmadan yine akciğer yolu ile vücuttan atılırlar; en büyük avantajları anestezi derinliğinin anlık olarak kolayca değiştirilebilmesidir (Slayt 2).",
        "Anestezi derinliği doğrudan beyindeki anestezik maddenin parsiyel basıncı ile doğru orantılıdır; kalpten çıkan kanın 1/6'sı beyne gittiği ve beyin lipoidden zengin olduğu için anestezikler hızla gri cevher üzerine etki eder (Slayt 4, 7).",
        "İndüksiyonda beyinde yoğunluğu çabuk artırmak için yüksek konsantrasyon verilir; istenilen seviyeye ulaşınca doz aşımını önlemek için idame dozuna düşülür (Slayt 8).",
        "Atılımda saf oksijen verilmesiyle olaylar tersine döner; gaz alveollerden atmosfere atılır, kandan alveollere ve beyinden kana difüzyonla beyin anestezikten kurtulur (Slayt 9).",
        "MAC (Minimum Alveoler Konsantrasyon), bireylerin %50'sinde ağrılı uyarana karşı kas hareketini önleyen alveoler konsantrasyondur; MAC ile anestezik GÜÇ TERS ORANTILIDIR (Slayt 10).",
        "Metoksifluran MAC değeri en küçük olan en güçlü ajan; N2O (nitrous oxide) ise MAC değeri en yüksek olan en zayıf ajandır (Slayt 10).",
        "Açık ve yarı açık damlatma yöntemleri ile anestezi kutusu küçük/lab hayvanlarında kullanılırken, modern veteriner cerrahide altın standart endotrakeal entübasyon aracılığıyla anestezidir (Slayt 11-15).",
        "Dietil eter kan/gaz erime katsayısı çok yüksek olduğundan indüksiyon ve uyanması oldukça yavaştır; patlayıcı ve solunum yollarına aşırı irritandır (Slayt 17).",
        "Nitrous oxide (N2O) yanıcı değildir; zayıf anesteziktir ancak güçlü analjeziktir, O2 ile 1:1 kullanılır, kan/gaz katsayısı çok düşük olduğundan çok hızlı etki eder ve tek başına cerrahi anestezi oluşturamaz (Slayt 18).",
        "Halotan güçlüdür (MAC 0.74), mukozaları irrite etmez ancak serebral kan akımını artırıp BOS emilimini azaltarak intrakraniyal basıncı artırır; %20-40 karaciğerde metabolize olduğu için hepatopatilerde kontrendikedir (Slayt 19).",
        "İzofluran veteriner sahada en yaygın ajandır; düşük kan/gaz katsayısıyla hızlı indüksiyon ve uyanma sağlar; BOS emilimini artırarak kafa içi basıncı DÜŞÜRÜR; bu nedenle kafa travması ve beyin operasyonlarında İLK TERCİHTİR; metabolize olma oranı sadece %0.2'dir (Slayt 21, 22).",
        "Sevofluran tatlı kokuludur, solunum yollarını irrite etmez; bu sayede özellikle MASKE İLE İNDÜKSİYONDA rahatlıkla kullanılır, %5 metabolize olur (Slayt 23).",
        "Desfluran kanda çözünürlüğü en düşük olduğundan EN HIZLI indüksiyon ve uyanmayı sağlar; ancak keskin kokusu, irritasyonu, taşikardi yapması ve pahalı olması dezavantajıdır (Slayt 24)."
    ]
}

SUMMARY_SECTIONS = [
    {
        "title": "1. İnhalasyon Anestezisi Prensipleri & Tarihçe",
        "icon": "📜",
        "points": [
            "Giriş & Eliminasyon Yolu: İnhalasyon anestezikleri akciğerlerden solunarak girer ve büyük oranda karaciğerde metabolize olmadan yine akciğerler yoluyla değişmeden ekspirasyonla atılır (Slayt 2).",
            "Temel Klinik Üstünlük: Enjektabl anesteziklere kıyasla en belirgin avantajı, vaporizatör ayarıyla anestezi derinliğinin saniyeler içinde kolayca artırılıp azaltılabilmesidir (Slayt 2).",
            "150 Yıllık Gelişim: N2O ve eter ilk olarak diş çekimlerinde kullanılmış; kloroform solunum depresyonu, siklopropan patlama riski yaratmıştır (Slayt 3).",
            "Halotan Öncesi & Sonrası: 1951'de halotanın keşfi modern anesteziyi başlatmıştır; metoksifluran ise güçlü analjezi ve kas gevşemesi sağlasa da renal ve hepatik toksisitesi nedeniyle terk edilmiştir (Slayt 3)."
        ]
    },
    {
        "title": "2. Alım, Dağılım ve Beyin Parsiyel Basıncı",
        "icon": "🧠",
        "points": [
            "Hedef Organ ve Parsiyel Basınç: İnhalasyon anestezisinde amaç, anestezik gazın beyinde belirli bir parsiyel basınca ulaşması ve MSS'de arzu edilen depresyonu oluşturmasıdır. Anestezi derinliği doğrudan beyindeki parsiyel basınçla orantılıdır (Slayt 4).",
            "Dağılımı Etkileyen Faktörler: MAC değeri, fiziksel/kimyasal özellikler, absorbsiyon hızı, uygulanan konsantrasyon, pulmoner kan akışı, kardiyak debi, doku perfüzyonu ve yağ oranı alım ve atılımı doğrudan etkiler (Slayt 5).",
            "Alveol-Kan-Doku Gradyenti: İnspirasyon havasından yoğunluk farkıyla alveollere, alveollerden kana, kandan da dokulara difüzyon zinciri gerçekleşir (Slayt 6).",
            "Beyin Perfüzyonu & Gri Cevher: Kalpten çıkan kanın 1/6'sı beyne gittiği için anestezik çok kısa sürede beyne ulaşır. Beyin dokusu lipoidden zengindir ve anestezikler özellikle gri cevher üzerine etki ederek anesteziyi şekillendirir (Slayt 7)."
        ]
    },
    {
        "title": "3. İndüksiyon, Doz Aşımı & Uyanma Dinamikleri",
        "icon": "🔄",
        "points": [
            "Hızlı İndüksiyon Kuralı: İnhalasyon anestezisinin çabuk oluşması için başlangıçta beyin gaz yoğunluğunu hızla artırmak amacıyla yüksek konsantrasyonda gaz verilir (Slayt 8).",
            "İdameye Geçiş & Doz Aşımı: Beyinde yoğunluk arttıkça gaz alımı yavaşlar. Aynı yüksek konsantrasyonda devam edilirse beyindeki yoğunluk tehlikeli boyutlara ulaşır (Doz Aşımı). İstenen derinliğe ulaşılınca doz idame seviyesine düşürülür (Slayt 8).",
            "Uyanma (Eliminasyon) Mekanizması: Saf oksijen inhale ettirildiğinde alveollerdeki anestezik ekspirasyonla atmosfere atılır. Yoğunluk gradyenti tersine döner: Kandan alveollere, beyinden de kana difüzyon başlar. Beyindeki gaz düzeyi kritik eşiğin altına indiğinde hasta uyanır (Slayt 9)."
        ]
    },
    {
        "title": "4. Minimum Alveoler Konsantrasyon (MAC) & Güç",
        "icon": "⚖️",
        "points": [
            "MAC Tanımı: Test edilen bireylerin %50'sinde standart ağrılı uyarıya karşı motor kas kontraksiyonunu önleyen anestezik maddenin alveoler konsantrasyonudur (100 hastanın 50'sinde cerrahi anestezi oluşturan doz) (Slayt 10).",
            "Ters Orantı Kuralı: MAC değeri ile anestezik maddenin potansiyeli (gücü) TERS ORANTILIDIR! MAC değeri ne kadar küçükse, anestezik o kadar güçlüdür (Slayt 10).",
            "En Güçlü vs En Zayıf: Metoksifluran MAC değeri en küçük olan en güçlü ajandır. N2O (azot protoksit) ise MAC değeri en yüksek olan en zayıf genel anesteziktir (Slayt 10)."
        ]
    },
    {
        "title": "5. İnhalasyon Anestezisi Uygulama Teknikleri",
        "icon": "😷",
        "points": [
            "I. Açık Damlatma Yöntemi: Sıvı anestezik gazlı komprese damlatılarak hayvanın ağız ve burnunu kapatacak şekilde tutulur; buhar solutulur (Slayt 11, 12).",
            "II. Yarı Açık Damlatma Yöntemi: Dip kısmında soluk alma delikleri olan maske içine gaz kompres konur; daha çok eterle kısa süreli anestezi için kullanılmıştır (Slayt 13).",
            "III. Anestezi Kutusu ve Cam Fanus: Küçük laboratuvar hayvanlarında (fare, sıçan) kutu içine sıvı püskürtülerek veya gazlı beze emdirilerek buhar solutulur (Slayt 14).",
            "IV. Endotrakeal Entübasyon: Trakeaya tüp yerleştirilerek anestezi cihazına bağlanır; spontan veya mekanik ventilasyonla gaz solutulur. Modern veteriner cerrahide altın standarttır. Küçüklerde maske ile indüksiyon da yapılabilir (Slayt 15)."
        ]
    },
    {
        "title": "6. İdeal İnhalasyon Anesteziği & Tarihsel Ajanlar (Eter, N2O)",
        "icon": "✨",
        "points": [
            "İdeal Anestezik Kriterleri: Solunum yollarına irritan olmamalı, kötü kokmamalı, hızlı indüksiyon/uyanma sağlamalı, yan etkisi ve toksisitesi minimal olmalı, ucuz, alev almaz/patlamaz olmalı, diğer ilaçlarla geçimli olmalıdır (Slayt 16).",
            "Dietil Eter: İlk anesteziklerdendir. Patlayıcıdır. Kan/gaz erime katsayısı çok yüksek olduğundan indüksiyon ve uyanması OLDUKÇA YAVAŞTIR. Bulantı/kusma ve solunum yolu irritasyonu yapar (Slayt 17).",
            "Nitrous Oxide (N2O): Yanıcı/patlayıcı değildir. Güçlü analjeziktir. Oksijenle 1:1 oranında (%50-%50) kullanılır. Kan/gaz katsayısı çok düşük olduğundan çok hızlı etki eder ve çabuk uyanma sağlar. Tek başına cerrahi anestezi oluşturamaz; diğer ajanların etkisini artırmak (MAC azaltmak) için kombine edilir (Slayt 18)."
        ]
    },
    {
        "title": "7. Halotan & Enfluran Karşılaştırması",
        "icon": "🧪",
        "points": [
            "Halotan Özellikleri: Güçlüdür (MAC 0.74), yanmaz/patlamaz. Analjezisi zayıf, kas gevşetmesi ortadır. Mukozaları irrite etmez (Slayt 19).",
            "Halotan Kontrendikasyonları: Serebral kan akımını artırıp BOS emilimini azaltarak intrakraniyal basıncı artırır; kafa travmasında ve gebelerde önerilmez. %20-40 oranında karaciğerde metabolize olduğundan karaciğer hastalarında KULLANILMAZ (Slayt 19).",
            "Enfluran: İzofluranın izomeridir. Hızlı indüksiyon ve uyanma sağlar. Serebral kan akımını halotandan daha fazla artırır; intrakraniyal basınç artışında kontrendikedir. Önemli derecede solunum depresyonu yapar; karaciğerde %2-5 metabolize olur (Slayt 20)."
        ]
    },
    {
        "title": "8. Modern Ajanlar: İzofluran, Sevofluran & Desfluran",
        "icon": "🌟",
        "points": [
            "İzofluran (Altın Standart): Veteriner sahada en yaygın ajandır. Keskin kokuludur. Düşük kan/gaz katsayısıyla hızlı indüksiyon, hızlı uyanma ve mükemmel kas gevşemesi sağlar. Metabolizma oranı sadece %0.2'dir (Slayt 21).",
            "İzofluran & Beyin Cerrahisi: BOS emilimini artırıp yapımını artırmadığı için kafa içi basıncı ve BOS hacmini DÜŞÜRÜR! Bu nedenle kafa travması, beyin tümörü ve kranial operasyonlarda İLK TERCİHTİR (Slayt 22).",
            "Sevofluran: TATLI KOKULUDUR, solunum yollarını irrite etmez. Bu nedenle MASKE İLE İNDÜKSİYONDA mükemmeldir. Çok hızlı indüksiyon ve uyanma sağlar. İntrakraniyal basıncı izoflurana göre daha stabil tutar, %5 metabolize olur (Slayt 23).",
            "Desfluran: Kanda çözünürlüğü en düşük olduğundan EN HIZLI indüksiyon ve uyanmayı sağlar. Ancak anestezik gücü düşüktür, keskin kokuludur, taşikardi ve solunum yolu irritasyonu yapabilir, pahalıdır (Slayt 24)."
        ]
    }
]

BILGI_KARTLARI = [
    {
        "kart_id": "ikart_001",
        "on_yuz": "İnhalasyon anesteziklerinin enjektabl anesteziklerden temel farmakokinetik farkı nedir?",
        "arka_yuz": "Vücuda akciğer yolu ile girerler ve büyük bir oranda karaciğerde metabolize olmadan yine akciğer yolu ile değişmeden vücuttan atılırlar (Slayt 2)."
    },
    {
        "kart_id": "ikart_002",
        "on_yuz": "Klinik pratikte inhalasyon anesteziklerinin tercih edilmesinin en belirgin avantajı nedir?",
        "arka_yuz": "Anestezi derinliğinin vaporizatör ayarıyla anlık ve kolayca değiştirilebilmesidir (Slayt 2)."
    },
    {
        "kart_id": "ikart_003",
        "on_yuz": "Modern anesteziyolojinin miladı kabul edilen 1951 yılında keşfedilen inhalasyon anesteziği hangisidir?",
        "arka_yuz": "Halotandır (Halothane) (Slayt 3)."
    },
    {
        "kart_id": "ikart_004",
        "on_yuz": "İnhalasyon anestezisinde temel amaç nedir ve anestezi derinliği ne ile doğrudan orantılıdır?",
        "arka_yuz": "Amaç anestezik maddenin beyinde belirli bir parsiyel basınca ulaşmasıdır; anestezi derinliği doğrudan beyindeki anestezik maddenin parsiyel basıncı ile orantılıdır (Slayt 4)."
    },
    {
        "kart_id": "ikart_005",
        "on_yuz": "İnhalasyon anesteziklerinin beyne çok kısa sürede ulaşıp etki göstermesinin fizyolojik nedeni nedir?",
        "arka_yuz": "Kalpten çıkan kanın 1/6'sının doğrudan beyne gitmesi ve beyin dokusunun lipoidden zengin olmasıdır (Slayt 7)."
    },
    {
        "kart_id": "ikart_006",
        "on_yuz": "İnhalasyon anestezikleri beyinde özellikle hangi doku bileşeni üzerine etki ederek anestezi oluşturur?",
        "arka_yuz": "Beyinde gri cevher (substantia grisea) üzerine etki ederek anestezi oluşturur (Slayt 7)."
    },
    {
        "kart_id": "ikart_007",
        "on_yuz": "İndüksiyon başlangıcında neden yüksek yoğunlukta anestezik gaz kullanılır ve sonrasında ne yapılır?",
        "arka_yuz": "Beyindeki gaz yoğunluğunu çabuk artırmak için yüksek verilir; istenen seviyeye ulaşınca doz aşımını önlemek için doz azaltılarak idame seviyesinde tutulur (Slayt 8)."
    },
    {
        "kart_id": "ikart_008",
        "on_yuz": "Anesteziden uyanma sürecinde saf oksijen verilmesinin fizyolojik rolü nedir?",
        "arka_yuz": "Alveollerdeki gazı ekspirasyonla temizler; yoğunluk gradyenti tersine dönerek gaz kandan alveollere, beyinden de kana difüze olur ve beyin gazdan arınarak uyanır (Slayt 9)."
    },
    {
        "kart_id": "ikart_009",
        "on_yuz": "Minimum Alveoler Konsantrasyon (MAC) ne demektir?",
        "arka_yuz": "Bireylerin %50'sinde ağrılı uyarıya karşı kas kontraksiyonu oluşmasını önleyen anestezik maddenin alveoler konsantrasyon oranıdır (%50'de anestezi oluşturan güç dozu) (Slayt 10)."
    },
    {
        "kart_id": "ikart_010",
        "on_yuz": "MAC değeri ile anesteziklerin gücü (potansiyeli) arasında nasıl bir bağıntı vardır?",
        "arka_yuz": "MAC değeri ile anesteziklerin gücü TERS ORANTILIDIR; MAC değeri ne kadar küçükse anestezik madde o kadar güçlüdür (Slayt 10)."
    },
    {
        "kart_id": "ikart_011",
        "on_yuz": "MAC değeri en küçük olan en güçlü ve MAC değeri en yüksek olan en zayıf anestezikler hangileridir?",
        "arka_yuz": "En güçlü anestezik Metoksifluran (en küçük MAC); en zayıf anestezik ise N2O'dur (en yüksek MAC) (Slayt 10)."
    },
    {
        "kart_id": "ikart_012",
        "on_yuz": "İnhalasyon anesteziklerinin 4 temel uygulanma tekniği nelerdir?",
        "arka_yuz": "1) Açık Damlatma, 2) Yarı Açık Damlatma, 3) Anestezi Kutusu ve Cam Fanus, 4) Endotrakeal Entübasyon (Slayt 11)."
    },
    {
        "kart_id": "ikart_013",
        "on_yuz": "Anestezi kutusu ve cam fanus yöntemi sıklıkla hangi hasta grubunda kullanılır?",
        "arka_yuz": "Küçük laboratuvar hayvanlarının (kemirgenler vb.) anestezisinde uygulanır (Slayt 14)."
    },
    {
        "kart_id": "ikart_014",
        "on_yuz": "Modern veteriner cerrahide kullanılan en güvenilir ve standart inhalasyon uygulama tekniği hangisidir?",
        "arka_yuz": "Endotrakeal entübasyon aracılığı ile anestezi uygulamasıdır (Slayt 15)."
    },
    {
        "kart_id": "ikart_015",
        "on_yuz": "İdeal bir inhalasyon anesteziğinin taşıması gereken temel özellikler nelerdir?",
        "arka_yuz": "İrritan olmamalı, kötü kokmamalı, hızlı indüksiyon/uyanma sağlamalı, toksik olmamalı, yanıcı/patlayıcı olmamalı, ucuz olmalı ve diğer ilaçlarla geçimli olmalıdır (Slayt 16)."
    },
    {
        "kart_id": "ikart_016",
        "on_yuz": "Dietil eterin (eter) indüksiyon ve uyanmasının oldukça yavaş olmasının nedeni nedir?",
        "arka_yuz": "Kan/gaz erime katsayısının çok yüksek olmasıdır (Slayt 17)."
    },
    {
        "kart_id": "ikart_017",
        "on_yuz": "Dietil eterin günümüzde kullanılmamasının temel nedenleri nelerdir?",
        "arka_yuz": "Solunum yolları için oldukça irritan olması, bulantı/kusma yapması ve yanıcı/patlayıcı olmasıdır (Slayt 17)."
    },
    {
        "kart_id": "ikart_018",
        "on_yuz": "Nitrous oxide (N2O) veteriner anestezide temel olarak hangi etkisinden dolayı kullanılır?",
        "arka_yuz": "Güçlü analjezik özelliğinden dolayı kullanılır; diğer ajanların etkisini artırır (Slayt 18)."
    },
    {
        "kart_id": "ikart_019",
        "on_yuz": "Nitrous oxide (N2O) pratik kullanımda oksijen ile hangi oranda karıştırılır?",
        "arka_yuz": "Oksijen ile 1:1 oranında (%50 O2 - %50 N2O) kullanılır (Slayt 18)."
    },
    {
        "kart_id": "ikart_020",
        "on_yuz": "Nitrous oxide tek başına cerrahi anestezi oluşturabilir mi?",
        "arka_yuz": "Hayır, tek başına kullanılması ile cerrahi anestezi oluşturulması mümkün değildir; anestezik gücü en düşüktür (Slayt 18)."
    },
    {
        "kart_id": "ikart_021",
        "on_yuz": "Halotanın MAC değeri nedir, mukozalarda irritasyon yapar mı?",
        "arka_yuz": "MAC değeri 0.74'tür (güçlüdür); mukoz membranlarda irritasyon oluşturmaz ve sekresyona neden olmaz (Slayt 19)."
    },
    {
        "kart_id": "ikart_022",
        "on_yuz": "Halotanın kafa içi basıncı artmış hayvanlarda ve kafa travmalarında önerilmeme nedeni nedir?",
        "arka_yuz": "Serebral kan akışını artırır ve BOS emilimini azaltarak intrakraniyal basınçta tehlikeli artışa neden olur (Slayt 19)."
    },
    {
        "kart_id": "ikart_023",
        "on_yuz": "Halotanın karaciğer hastalıklarında kontrendike olmasının metabolik nedeni nedir?",
        "arka_yuz": "%20 - 40 gibi yüksek oranda karaciğerde metabolize olmasından dolayı karaciğer hastalıklarında kullanılmaz (Slayt 19)."
    },
    {
        "kart_id": "ikart_024",
        "on_yuz": "Enfluran ile halotan serebral kan akımı açısından karşılaştırıldığında hangisi daha risklidir?",
        "arka_yuz": "Enfluran serebral kan akımını halotandan daha fazla artırır; intrakraniyal basınç artışı varsa kesinlikle kullanılmamalıdır (Slayt 20)."
    },
    {
        "kart_id": "ikart_025",
        "on_yuz": "İzofluranın indüksiyonda maskeyle kullanılmasını sınırlayan fiziksel özelliği nedir?",
        "arka_yuz": "Keskin ve batıcı kokusudur (Slayt 21)."
    },
    {
        "kart_id": "ikart_026",
        "on_yuz": "Veteriner anestezide Enfluran yerine İzofluran tercih edilmesinin 2 temel gerekçesi nedir?",
        "arka_yuz": "1) Kaslarda miyorelaksan etkisinin daha fazla olması, 2) Daha düşük kan:gaz katsayısı sayesinde çok kısa sürede uyanma sağlamasıdır (Slayt 21)."
    },
    {
        "kart_id": "ikart_027",
        "on_yuz": "Kafa travması geçiren veya beyin tümörü olan hayvanlarda neden İzofluran ilk tercihtir?",
        "arka_yuz": "İzofluran serebrospinal sıvı (BOS) emilimini artırır ancak yapımını artırmaz; bu sayede kafa içi basıncı ve BOS hacmini azaltır (Slayt 22)."
    },
    {
        "kart_id": "ikart_028",
        "on_yuz": "İzofluranın karaciğerde metabolize olma oranı ne kadardır?",
        "arka_yuz": "Sadece %0.2'dir (organ toksisitesi son derece düşüktür) (Slayt 22)."
    },
    {
        "kart_id": "ikart_029",
        "on_yuz": "Sevofluranın özellikle maske ile indüksiyonda rahatlıkla kullanılmasını sağlayan özelliği nedir?",
        "arka_yuz": "Tatlı kokulu olması ve solunum yollarını irrite etmemesidir (Slayt 23)."
    },
    {
        "kart_id": "ikart_030",
        "on_yuz": "Anestezikler içinde en hızlı indüksiyon ve uyanmayı sağlayan Desfluranın dezavantajları nelerdir?",
        "arka_yuz": "Anestezik gücünün düşük olması, keskin kokusu, solunum yolu irritasyonu, taşikardi yapabilmesi ve pahalı fiyatıdır (Slayt 24)."
    }
]

ACIK_UCLU_SORULAR = [
    {
        "soru_id": "au_inh_001",
        "soru": "İnhalasyon anesteziklerinin enjektabl anesteziklere kıyasla farmakokinetik üstünlüklerini ve klinik kullanım kolaylığını açıklayınız.",
        "ideal_cevap": "Enjektabl anestezikler vücuda verildikten sonra eliminasyonları tamamen karaciğer metabolizmasına ve renal atılıma bağımlıdır; bu nedenle doz aşımında ilacı geri çekmek zordur. İnhalasyon anestezikleri ise akciğer yoluyla alınıp büyük oranda metabolize olmadan yine akciğerlerden ekspirasyonla atılır. En büyük klinik avantajı anestezi derinliğinin vaporizatör kadranı ile saniyeler içinde artırılıp azaltılabilmesi ve ilacın kesilmesiyle hastanın dakikalar içinde hızla uyanabilmesidir.",
        "degerlendirme_kriteri": "Cevapta [akciğerden giriş/çıkış, metabolize olmadan atılma, derinliğin anlık ayarlanabilmesi, hızlı geri dönüşümlülük] yer almalıdır.",
        "slayt_no": 2
    },
    {
        "soru_id": "au_inh_002",
        "soru": "İnhalasyon anestezisinde genel anestezi derinliğini doğrudan belirleyen faktörü ve bu faktörün beyin anatomisi/kan akımı ile ilişkisini açıklayınız.",
        "ideal_cevap": "Genel anestezi derinliği, doğrudan doğruya beyin dokusundaki anestezik maddenin parsiyel basıncı ile doğru orantılıdır. Kalpten çıkan kardiyak debinin yaklaşık 1/6'sı doğrudan beyne gittiği için kanda yükselen anestezik gaz hızla serebral dolaşıma ulaşır. Beyin dokusu lipoid bakımından oldukça zengindir; lipofilik özellikteki anestezik gazlar hızla kandan beyin dokusuna diffüze olur ve özellikle gri cevher (substantia grisea) nöronlarını deprese ederek anesteziyi oluşturur.",
        "degerlendirme_kriteri": "Cevapta [beyindeki parsiyel basınç, kalpten çıkan kanın 1/6'sı beyne gitmesi, lipoid zenginliği, gri cevher üzerine etki] bulunmalıdır.",
        "slayt_no": 4
    },
    {
        "soru_id": "au_inh_003",
        "soru": "İnhalasyon anestezisinde solunum havasından dokulara gaz geçişinin konsantrasyon gradyenti basamaklarını sırasıyla açıklayınız.",
        "ideal_cevap": "1) İnhalasyon başladığında inspirasyon havasındaki gaz yoğunluğu alveollerden fazla olduğu için solunum havasından alveollere doğru gaz akımı gerçekleşir. 2) Alveollerde biriken gazın yoğunluğu kandan yüksek olduğu için gaz alveol kapiller membranından kana diffüze olur ve kandaki konsantrasyon yükselir. 3) Kanda gaz yoğunluğu artıp periferik dokularda henüz bulunmadığı için kandan dokulara ve özellikle yüksek perfüze beyne difüzyon gerçekleşir.",
        "degerlendirme_kriteri": "Cevapta [inspirasyon havası -> alveol -> kan -> doku/beyin konsantrasyon gradyenti difüzyonu] basamakları sıralanmalıdır.",
        "slayt_no": 6
    },
    {
        "soru_id": "au_inh_004",
        "soru": "İnhalasyon indüksiyonunda neden başlangıçta yüksek gaz konsantrasyonu verilir ve sonrasında dozun idameye düşürülmemesi halinde ne şekillenir?",
        "ideal_cevap": "İnhalasyon anestezisinin çabuk oluşması için beyin dokusundaki gaz yoğunluğunun hızla eşik değere ulaştırılması gerekir; bu amaçla indüksiyonun başında yüksek yoğunlukta anestezik gaz solutulur. Dokularda gaz yoğunluğu arttıkça difüzyon yavaşlar. Eğer hasta istenen anestezi evresine ulaştıktan sonra gaz konsantrasyonu düşürülmeyip yüksek tutulmaya devam edilirse; alveol, kan ve beyindeki yoğunluk toksik seviyelere tırmanarak ölümcül 'doz aşımı' ve kardiyorespiratuvar arrest oluşturur. Bu nedenle stabil seviyeye gelince doz idameye çekilir.",
        "degerlendirme_kriteri": "Cevapta [beyin yoğunluğunu hızla artırma, indüksiyonda yüksek doz, istenen seviyede dozu azaltma/idame, azaltılmazsa doz aşımı/arrest] yer almalıdır.",
        "slayt_no": 8
    },
    {
        "soru_id": "au_inh_005",
        "soru": "Anestezi sonunda hastaya saf oksijen verilmesiyle gerçekleşen uyanma (eliminasyon) sürecinin basamaklarını açıklayınız.",
        "ideal_cevap": "Saf oksijen verilmeye başlandığında alveollerdeki anestezik gaz ekspirasyonla atmosfere atılır ve alveoler yoğunluk aniden düşer. Yoğunluk farkı tersine döndüğü için bu kez kandan alveollere doğru gaz difüzyonu gerçekleşir ve kandaki konsantrasyon hızla azalır. Ardından dokulardan ve özellikle beyin dokusundan gaz kana doğru diffüze olur. Sonuçta beyindeki anestezik konsantrasyonu kritik eşiğin altına iner ve beyin anestezik etkiden kurtularak uyanma gerçekleşir.",
        "degerlendirme_kriteri": "Cevapta [saf oksijenle alveollerin temizlenmesi, kandan alveole difüzyon, beyinden kana difüzyon, beyin konsantrasyonunun düşmesi ve uyanma] basamakları yer almalıdır.",
        "slayt_no": 9
    },
    {
        "soru_id": "au_inh_006",
        "soru": "Minimum Alveoler Konsantrasyon (MAC) kavramını tanımlayarak, MAC değeri ile anestezik gücün ilişkisini Metoksifluran ve N2O üzerinden açıklayınız.",
        "ideal_cevap": "MAC; standart bir zararlı (ağrılı) uyarana karşı test edilen bireylerin %50'sinde kas kontraksiyonu (motor yanıt) oluşmasını önleyen alveoler anestezik konsantrasyondur. Kısaca 100 denekten 50'sinde genel anestezi oluşturan güç göstergesidir. MAC değeri ile anestezik güç ters orantılıdır; yani MAC değeri ne kadar küçükse anestezik o kadar güçlüdür. Metoksifluran en küçük MAC değerine sahip olduğu için en güçlü genel anesteziktir. N2O ise MAC değeri en yüksek (%100'ün üzerinde) anestezik olduğu için anestezik gücü en zayıf olandır.",
        "degerlendirme_kriteri": "Cevapta [%50 bireyde ağrıya karşı kas yanıtını önleyen alveol dozu tanımı, MAC ile gücün ters orantılı olması, Metoksifluranın en düşük MAC/en güçlü olması, N2O'nun en yüksek MAC/en zayıf olması] bulunmalıdır.",
        "slayt_no": 10
    },
    {
        "soru_id": "au_inh_007",
        "soru": "Açık ve yarı açık damlatma yöntemlerinin uygulama farklarını ve günümüzde neden terk edildiklerini açıklayınız.",
        "ideal_cevap": "Açık damlatma yönteminde sıvı anestezik (genelde eter) gazlı beze damlatılıp doğrudan hayvanın ağız-burnu kapatılarak solutulur. Yarı açık yöntemde ise anestezik emdirilmiş bez delikli özel bir maske içine yerleştirilir ve hayvan maskeden solur. Günümüzde bu yöntemlerin terk edilme nedenleri: Anestezi derinliğinin hassas kontrol edilememesi, aşırı gaz israfı ve ameliyathane havasına toksik gaz yayılması, personelin maruziyeti, modern anestezi makineleri ve vaporizatörlerin geliştirilmiş olmasıdır.",
        "degerlendirme_kriteri": "Cevapta [açık damlatmada beze doğrudan dökülme, yarı açıkta delikli maske kullanımı, kontrolsüz derinlik, personel/çevre kontaminasyonu, modern makinelerin varlığı] yer almalıdır.",
        "slayt_no": 13
    },
    {
        "soru_id": "au_inh_008",
        "soru": "Endotrakeal entübasyon tekniğinin açık ve maskeli inhalasyon yöntemlerine kıyasla cerrahi ve anestezi güvenliği açısından üstünlüklerini yazınız.",
        "ideal_cevap": "Endotrakeal entübasyon; trakeaya yerleştirilen kaflı tüp sayesinde hava yolunu mutlak güvenceye alır. Avantajları: 1) Solunum depresyonu veya arrest durumunda mekanik ventilatör veya rezerv balonu ile pozitif basınçlı yapay solunum yaptırılmasına imkan tanır. 2) Regürgitasyon ve kusmuk aspirasyonunu kesin olarak önler. 3) Anestezi gazının ameliyathaneye sızmasını engelleyerek personeli korur. 4) Ölü boşluğu azaltır ve anestezi derinliğinin hassas kontrolünü sağlar.",
        "degerlendirme_kriteri": "Cevapta [hava yolu güvenliği, yapay/mekanik ventilasyon imkanı, aspirasyon önleme, personel güvenliği, hassas derinlik kontrolü] bulunmalıdır.",
        "slayt_no": 15
    },
    {
        "soru_id": "au_inh_009",
        "soru": "İdeal bir inhalasyon anesteziğinde aranan 6 temel farmakolojik ve fiziksel özelliği yazınız.",
        "ideal_cevap": "1) Solunum yolları için irritan olmamalı ve kötü kokmamalıdır. 2) Hızlı indüksiyon ve uyanma sağlamalıdır. 3) Kardiyovasküler ve solunumsal yan etkileri minimal olmalı veya hiç bulunmamalıdır. 4) Organ toksisitesi (hepatotoksisite, nefrotoksisite) olmamalıdır. 5) Yanıcı ve patlayıcı olmamalıdır. 6) Ucuz olmalı ve premedikasyon ilaçları ile geçimli olmalıdır.",
        "degerlendirme_kriteri": "Cevapta [irritan/kokusuz olmama, hızlı indüksiyon/uyanma, minimal yan etki, toksik olmama, yanmaz/patlamaz olma, ucuzluk/geçimlilik] maddeleri yer almalıdır.",
        "slayt_no": 16
    },
    {
        "soru_id": "au_inh_010",
        "soru": "Dietil eterin kan/gaz erime katsayısının yüksek olmasının klinik sonuçlarını ve günümüzde ameliyathanelerde kullanılmamasının nedenlerini açıklayınız.",
        "ideal_cevap": "Kan/gaz erime katsayısının çok yüksek olması, eterin kanda aşırı derecede çözünmesi demektir; bu durum kandaki parsiyel basıncın ve dolayısıyla beyindeki konsantrasyonun çok yavaş yükselmesine, atılırken de kandan çok yavaş temizlenmesine yol açar. Sonuç olarak indüksiyon ve anesteziden uyanma son derece yavaştır. Kullanılmama nedenleri: Solunum yollarına aşırı irritan olması, indüksiyon ve uyanmada şiddetli bulantı/kusma yapması ve ameliyathanelerdeki elektrikli aletlerle temasında patlama riski taşımasıdır.",
        "degerlendirme_kriteri": "Cevapta [yüksek kan/gaz katsayısı, çok yavaş indüksiyon ve uyanma, solunum yolu irritasyonu, bulantı/kusma, patlama riski] yer almalıdır.",
        "slayt_no": 17
    },
    {
        "soru_id": "au_inh_011",
        "soru": "Nitrous oxide (N2O) gazının anestezi gücünü, analjezik etkisini, oksijenle karışım oranını ve tek başına kullanılamama gerekçesini açıklayınız.",
        "ideal_cevap": "Nitrous oxide'in anestezik gücü son derece düşüktür (MAC değeri >%100'dür), bu nedenle tek başına cerrahi anestezi oluşturması imkansızdır. Ancak çok güçlü bir analjeziktir. Hipoksiyi önlemek amacıyla pratik kullanımda daima oksijen ile 1:1 oranında (%50 O2 + %50 N2O) karıştırılarak uygulanır. Kan/gaz erime katsayısı çok düşük olduğu için kanda ve beyinde süratle yükselir ve hızla terk eder. Genellikle diğer güçlü inhalasyon anestezikleriyle kombine edilerek onların gereksinim duyulan dozunu (MAC) azaltmak amacıyla kullanılır.",
        "degerlendirme_kriteri": "Cevapta [düşük anestezik güç, güçlü analjezi, O2 ile 1:1 oran, düşük kan/gaz katsayısı, diğer ajanların dozunu azaltma/kombinasyon] bulunmalıdır.",
        "slayt_no": 18
    },
    {
        "soru_id": "au_inh_012",
        "soru": "Halotanın intrakraniyal basınç (KİB) ve karaciğer üzerindeki patofizyolojik etkilerini açıklayarak, hangi hasta gruplarında kontrendike olduğunu belirtiniz.",
        "ideal_cevap": "Halotan serebral damarlarda vazodilatasyon yaparak serebral kan akışını artırır ve eş zamanlı olarak serebrospinal sıvının (BOS) emilimini azaltır; bu durum kafa içinde sıvı birikmesine ve intrakraniyal basıncın tehlikeli şekilde yükselmesine neden olur. Bu yüzden kafa travması ve beyin tümörü olanlarda önerilmez. Ayrıca halotan %20-40 gibi çok yüksek bir oranda karaciğerde metabolize edilir; hepatotoksik metabolitleri nedeniyle karaciğer hastalarında kesinlikle kontrendikedir. Uterusu gevşettiği için gebelerde de tavsiye edilmez.",
        "degerlendirme_kriteri": "Cevapta [serebral kan akımı artışı, BOS emilimi azalması, intrakraniyal basınç artışı, %20-40 karaciğer metabolizması, karaciğer hastalarında kontrendike olma] yer almalıdır.",
        "slayt_no": 19
    },
    {
        "soru_id": "au_inh_013",
        "soru": "Enfluranın serebral kan akımı ve solunum sistemi üzerindeki etkilerini halotan ile karşılaştırarak açıklayınız.",
        "ideal_cevap": "Enfluran, izofluranın izomeridir. Serebral kan akımını halotandan bile daha fazla artırır; bu nedenle intrakraniyal basınç artışı şüphesi olan hastalarda kullanımı kesinlikle sakıncalıdır. Ayrıca solunum sistemi üzerinde önemli derecede solunum depresyonu meydana getirir. Karaciğerde metabolize olma oranı ise %2-5 arasındadır (halotana göre daha düşüktür).",
        "degerlendirme_kriteri": "Cevapta [izofluran izomeri, serebral kan akımını halotandan daha çok artırması, KİB artışında kullanılmaması, belirgin solunum depresyonu, %2-5 karaciğer metabolizması] yer almalıdır.",
        "slayt_no": 20
    },
    {
        "soru_id": "au_inh_014",
        "soru": "İzofluranın veteriner hekimlikte en yaygın kullanılan inhalasyon anesteziği olmasını sağlayan temel avantajları ve indüksiyondaki tek kısıtlayıcı yönünü açıklayınız.",
        "ideal_cevap": "Avantajları: Kandaki eriyebilirliğinin (kan/gaz katsayısı) düşük olması sayesinde indüksiyon ve anesteziden uyanma çok hızlıdır; anestezi derinliği kolayca kontrol edilir; çok iyi düzeyde iskelet kası gevşemesi (miyorelaksasyon) sağlar; karaciğerde metabolizma oranı sadece %0.2 olduğundan organ toksisitesi ihmal edilebilir düzeydedir. Tek kısıtlayıcı yönü: Keskin ve batıcı bir kokuya sahip olmasıdır; bu nedenle maske ile indüksiyonda hayvanlarda nefes tutma ve ajitasyona yol açabilir.",
        "degerlendirme_kriteri": "Cevapta [düşük kan/gaz katsayısı, hızlı etki ve uyanma, mükemmel kas gevşemesi, %0.2 metabolizma, kısıtlayıcı faktör olarak keskin koku] bulunmalıdır.",
        "slayt_no": 21
    },
    {
        "soru_id": "au_inh_015",
        "soru": "İzofluranın beyin omurilik sıvısı (BOS) dinamikleri üzerindeki etkisini açıklayarak, kafa travmalı hastalarda neden ilk tercih olduğunu yazınız.",
        "ideal_cevap": "Halotanın aksine İzofluran, serebrospinal sıvı (BOS) emilimini artırır ancak BOS yapımını artırmaz. Bu spesifik mekanizma sayesinde kafa içi basınçta (intrakraniyal basınç) ve serebrospinal sıvı hacminde belirgin bir azalma meydana getirir. Bu eşsiz özelliği nedeniyle kafa travması geçiren, kafa içi basıncı yüksek olan veya beyin tümörü/operasyonu geçirecek hayvanlarda güvenle tercih edilen ideal anestezik maddedir.",
        "degerlendirme_kriteri": "Cevapta [BOS emilimini artırma, yapımını artırmama, kafa içi basıncı ve BOS hacmini azaltma, kafa travması ve beyin cerrahisinde ilk tercih olma] yer almalıdır.",
        "slayt_no": 22
    },
    {
        "soru_id": "au_inh_016",
        "soru": "Sevofluranın koku ve hava yolu irritasyonu açısından izoflurandan farkını ve bu durumun maske indüksiyonuna yansımasını açıklayınız.",
        "ideal_cevap": "İzofluran keskin ve tahriş edici kokusu nedeniyle maske indüksiyonunda solunum tutma ve rahatsızlık yaratırken; Sevofluran tatlı kokuludur ve solunum yollarını kesinlikle irrite etmez. Bu mükemmel özelliği sayesinde hayvanlarda maske aracılığı ile anestezi indüksiyonu yapılmasında hiçbir dirençle karşılaşılmadan rahatlıkla ve güvenle kullanılır. Kanda eriyebilirliği de çok düşük olduğundan uyanma ve indüksiyon süresi son derece kısadır.",
        "degerlendirme_kriteri": "Cevapta [tatlı kokulu olma, solunum yollarını irrite etmeme, maske ile indüksiyonda rahat kullanım, düşük kanda eriyebilirlik] yer almalıdır.",
        "slayt_no": 23
    },
    {
        "soru_id": "au_inh_017",
        "soru": "Sevofluranın intrakraniyal basınç ve karaciğer metabolizması profilini özetleyiniz.",
        "ideal_cevap": "Sevofluran, intrakraniyal basıncı izoflurana göre daha stabil ve dengeli tutar; serebral hemodinamiyi bozmaz. Karaciğerde metabolize olma oranı yaklaşık %5'tir (halotanın %20-40'lık oranına kıyasla oldukça güvenlidir). Yanıcı ve patlayıcı değildir.",
        "degerlendirme_kriteri": "Cevapta [intrakraniyal basıncı stabil tutma, karaciğerde %5 metabolize olma, yanmaz/patlamaz olma] belirtilmelidir.",
        "slayt_no": 23
    },
    {
        "soru_id": "au_inh_018",
        "soru": "Desfluranın en hızlı indüksiyon ve uyanma sağlayan ajan olmasına karşılık veteriner hekimlikte kullanımını kısıtlayan dezavantajlarını yazınız.",
        "ideal_cevap": "Desfluran kanda çözünürlüğü en düşük ajan olduğu için tüm anestezikler içinde en hızlı indüksiyon ve uyanmayı sağlar. Ancak dezavantajları: 1) Anestezik gücünün düşük olması (yüksek MAC gerektirir), 2) Keskin ve aşırı irritan kokusu olması, 3) Yüksek konsantrasyonlarda verildiğinde sempatik stimülasyonla taşikardiye ve solunum yollarında spazm/irritasyona yol açması, 4) Çok pahalı olması ve özel elektrikli ısıtmalı vaporizatör gerektirmesidir.",
        "degerlendirme_kriteri": "Cevapta [en hızlı indüksiyon/uyanma, düşük güç/yüksek MAC, keskin koku, solunum irritasyonu ve taşikardi, yüksek fiyat] yer almalıdır.",
        "slayt_no": 24
    },
    {
        "soru_id": "au_inh_019",
        "soru": "İnhalasyon anesteziklerinin karaciğerde metabolize olma oranlarını (Halotan, Enfluran, Sevofluran, İzofluran) büyükten küçüğe sıralayarak hepatotoksisite riskini karşılaştırınız.",
        "ideal_cevap": "Metabolize olma oranları: 1) Halotan: %20 - 40 (en yüksek metabolizma ve en yüksek hepatotoksisite riski), 2) Sevofluran: %5, 3) Enfluran: %2 - 5, 4) İzofluran: %0.2 (en düşük metabolizma, neredeyse sıfır hepatotoksisite). Bu sıralama nedeniyle karaciğer yetmezliği olan veya karaciğer fonksiyonları riskli hastalarda halotan kesinlikle kullanılmazken izofluran en güvenli seçenektir.",
        "degerlendirme_kriteri": "Cevapta [Halotan %20-40, Sevofluran %5, Enfluran %2-5, İzofluran %0.2 sıralaması ve karaciğer güvenliği] bulunmalıdır.",
        "slayt_no": 19
    },
    {
        "soru_id": "au_inh_020",
        "soru": "Küçük laboratuvar hayvanlarında anestezi kutusu ve cam fanus kullanımının uygulama adımlarını ve güvenlik önlemini açıklayınız.",
        "ideal_cevap": "Uygulama: Kemirgen veya laboratuvar hayvanının yerleştirileceği kapalı şeffaf bir kutu/fanus içerisine sıvı anestezik madde ya bir enjektörle püskürtülür ya da gazlı bir beze emdirilerek tabana yerleştirilir. Kutu içinde buharlaşan anestezik gazı hayvan solur ve anesteziye girer. Güvenlik önlemi: Hayvanın derisi veya mukozasının sıvı anestezik madde ile doğrudan temas etmesini engellemek için gazlı bez tel bir ızgara altına konulmalı ve derinlik sürekli gözle takip edilerek aşırı maruziyet önlenmelidir.",
        "degerlendirme_kriteri": "Cevapta [sıvı anesteziğin kutuya püskürtülmesi veya beze emdirilmesi, gazın solunması, hayvanın sıvıya doğrudan temasının önlenmesi, görsel takip] yer almalıdır.",
        "slayt_no": 14
    }
]

COKTAN_SECMELI_SORULAR = [
    {
        "soru_id": "mcq_inh_001",
        "soru_metni": "İnhalasyon anesteziklerinin enjektabl anestezik maddelerden en temel farmakokinetik farkı aşağıdakilerden hangisidir?",
        "secenekler": {
            "A": "Vücuda sadece damar içi yolla girip safra ile atılmaları",
            "B": "Vücuda akciğer yolu ile girip büyük bir oranda metabolize olmadan yine akciğer yolu ile atılmaları",
            "C": "Vücutta tamamen yağa dönüşerek kalıcı olmaları",
            "D": "Sadece böbrek tubuluslarından aktif salgılanmaları"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; inhalasyon anestezikleri vücuda akciğerle girer ve büyük oranda metabolize olmadan akciğerle atılır (Slayt 2).",
            "celdirici_analizi": "A, C ve D seçenekleri inhalasyon anesteziklerinin temel fizyolojisine aykırıdır."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "kolay",
        "etiketler": ["farmakokinetik", "akciger_atilim"]
    },
    {
        "soru_id": "mcq_inh_002",
        "soru_metni": "Veteriner hekimlikte inhalasyon anesteziklerinin yaygın olarak kullanılmasının en belirgin klinik avantajı nedir?",
        "secenekler": {
            "A": "Hiçbir ekipman ve cihaza ihtiyaç duymamaları",
            "B": "Anestezi derinliğinin kolayca değiştirilebilmesi",
            "C": "Hastanın kalp atımını her zaman sıfırlaması",
            "D": "Enjeksiyonlara göre 100 kat daha ucuz olmaları"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; en belirgin avantajı ve yaygın kullanılma nedeni anestezi derinliğinin kolayca değiştirilebilmesidir (Slayt 2).",
            "celdirici_analizi": "Cihaz gerektirirler (A yanlış); derinlik kontrolü en büyük avantajdır."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "kolay",
        "etiketler": ["klinik_avantaj", "derinlik_kontrolu"]
    },
    {
        "soru_id": "mcq_inh_003",
        "soru_metni": "1951 yılında keşfedilerek hızlı indüksiyon ve uyanma sağlayan, modern inhalasyon anesteziyolojisinin miladı kabul edilen anestezik hangisidir?",
        "secenekler": {
            "A": "Dietil eter",
            "B": "Halotan (Halothane)",
            "C": "Kloroform",
            "D": "Siklopropan"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 1951 yılında halotanın keşfi cerrahi müdahalelerde devrim yaratmıştır (Slayt 3).",
            "celdirici_analizi": "Eter ve kloroform 19. yüzyılda; halotan ise 1951'de keşfedilmiştir."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "orta",
        "etiketler": ["tarihce", "halotan"]
    },
    {
        "soru_id": "mcq_inh_004",
        "soru_metni": "Eter gibi açık damlatma ile uygulanması mümkün olan ancak renal ve hepatik toksisitesi nedeniyle terk edilen anestezik hangisidir?",
        "secenekler": {
            "A": "Metoksifluran (Methoxyflurane)",
            "B": "Sevofluran",
            "C": "Azot protoksit",
            "D": "Desfluran"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Methoxyflurane eter gibi uygulanabilirken renal ve hepatik toksisiteye sahiptir (Slayt 3).",
            "celdirici_analizi": "Halotan özel cihaz gerektirirken metoksifluran eter gibi damlatılabiliyordu."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "orta",
        "etiketler": ["metoksifluran", "toksisite"]
    },
    {
        "soru_id": "mcq_inh_005",
        "soru_metni": "Genel anestezide anestezi derinliği doğrudan aşağıdakilerden hangisi ile orantılıdır?",
        "secenekler": {
            "A": "Kandaki eritrosit sayısı ile",
            "B": "Beyindeki anestezik maddenin parsiyel basıncı ile",
            "C": "Midedeki gıda miktarı ile",
            "D": "Oda havasının nem oranı ile"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; anestezi derinliği direkt olarak beyindeki anestezik maddenin parsiyel basıncı ile orantılıdır (Slayt 4).",
            "celdirici_analizi": "Slayt 4'te net olarak vurgulanmış fizyolojik temel kuraldır."
        },
        "slayt_no": 4,
        "zorluk_derecesi": "kolay",
        "etiketler": ["parsiyel_basinc", "anestezi_derinligi"]
    },
    {
        "soru_id": "mcq_inh_006",
        "soru_metni": "Aşağıdakilerden hangisi inhalasyon anesteziklerinin vücuda alınması ve dağılımını etkileyen faktörlerden biri DEĞİLDİR?",
        "secenekler": {
            "A": "Minimum alveoller konsantrasyon (MAC)",
            "B": "Pulmoner kan akışı ve kardiyak output",
            "C": "Dokulardaki yağ oranı ve perfüzyon",
            "D": "Hayvanın tüy rengi ve kulak yapısı"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği anestezi dağılımını etkilemez (Slayt 5).",
            "celdirici_analizi": "A, B ve C seçenekleri slayt 5'te sıralanan temel fizyolojik ve farmakolojik belirleyicilerdir."
        },
        "slayt_no": 5,
        "zorluk_derecesi": "kolay",
        "etiketler": ["dagilim_faktorleri"]
    },
    {
        "soru_id": "mcq_inh_007",
        "soru_metni": "İnhalasyon anesteziği solutulmaya başlandığında gazın vücut kompartımanlarına geçiş sırası hangisinde doğru verilmiştir?",
        "secenekler": {
            "A": "Doku -> Kan -> Alveol -> Solunum havası",
            "B": "Solunum havası -> Alveoller -> Kan -> Dokular (Beyin)",
            "C": "Mide -> Karaciğer -> Kalp -> Akciğer",
            "D": "Deri -> Kas -> Kemik -> Beyin"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; yoğunluk gradyentiyle solunum havasından alveollere, alveollerden kana, kandan dokulara/beyne difüzyon olur (Slayt 6).",
            "celdirici_analizi": "Slayt 6'da bu ardışık difüzyon zinciri adım adım anlatılmaktadır."
        },
        "slayt_no": 6,
        "zorluk_derecesi": "kolay",
        "etiketler": ["difuzyon_zinciri", "gecis_sirasi"]
    },
    {
        "soru_id": "mcq_inh_008",
        "soru_metni": "Kalpten çıkan kanın yaklaşık kaçta kaçı doğrudan beyne gittiği için anestezik madde beyinde çok kısa sürede etkisini gösterir?",
        "secenekler": {
            "A": "1/2'si",
            "B": "1/6'sı",
            "C": "1/20'si",
            "D": "1/50'si",
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kalpten çıkan kanın 1/6'sı beyne gittiği için kısa sürede beyinde yoğunluk artar (Slayt 7).",
            "celdirici_analizi": "Slayt 7'nin ilk cümlesinde 'Kalpten çıkan kanın 1/6'sı beyine gittiği için...' ifadesi yer alır."
        },
        "slayt_no": 7,
        "zorluk_derecesi": "orta",
        "etiketler": ["beyin_kan_akimi", "fizyoloji"]
    },
    {
        "soru_id": "mcq_inh_009",
        "soru_metni": "İnhalasyon anestezikleri lipoidden zengin olan beyin dokusunda özellikle hangi yapı üzerine etki ederek anesteziyi şekillendirir?",
        "secenekler": {
            "A": "Gri cevher",
            "B": "Beyin ventrikülleri",
            "C": "Duramater",
            "D": "Hipofiz sapı"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; anestezikler beyinde gri cevher üzerine etki ederek anestezi oluşturur (Slayt 7).",
            "celdirici_analizi": "Nöron gövdelerinin bulunduğu gri cevher anesteziklerin primer etki sahasıdır."
        },
        "slayt_no": 7,
        "zorluk_derecesi": "orta",
        "etiketler": ["gri_cevher", "etki_yeri"]
    },
    {
        "soru_id": "mcq_inh_010",
        "soru_metni": "Genel anestezi istenilen seviyeye ulaştıktan sonra aynı yüksek yoğunlukta anestezik uygulanmaya devam edilirse ne meydana gelir?",
        "secenekler": {
            "A": "Hasta kendiliğinden uyanır",
            "B": "Alveollerdeki, kandaki ve beyindeki yoğunluk tehlikeli boyutlara ulaşarak doz aşımı şekillenir",
            "C": "Vaporizatördeki sıvı donar",
            "D": "Oksijen tüpü patlar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; yüksek yoğunluk sürdürülürse beyindeki yoğunluk tehlikeli boyutlara ulaşır ve doz aşımı oluşur (Slayt 8).",
            "celdirici_analizi": "Bu nedenle genel anestezi oturunca doz idame seviyesine düşürülür."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "kolay",
        "etiketler": ["doz_asimi", "idame"]
    },
    {
        "soru_id": "mcq_inh_011",
        "soru_metni": "Anesteziden uyanma sürecinde hastaya saf oksijen solutulmaya başlandığında gerçekleşen olaylar zinciri hangisinde doğrudur?",
        "secenekler": {
            "A": "Gaz böbreklere çöker ve idrarla atılır",
            "B": "Alveollerden gaz atılır -> Kandan alveollere difüzyon olur -> Dokulardan/beyinden kana difüzyon olur ve hasta uyanır",
            "C": "Beyin gazı hapseder ve hasta kalıcı uyur",
            "D": "Kandaki gaz yoğunluğu aniden iki katına çıkar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; atılımda olaylar tersine döner, alveolden kandan ve beyinden gaz temizlenir (Slayt 9).",
            "celdirici_analizi": "Slayt 9'da uyanma dinamikleri bu sıra ile açıklanmıştır."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "orta",
        "etiketler": ["uyanma_dinamikleri", "eliminasyon"]
    },
    {
        "soru_id": "mcq_inh_012",
        "soru_metni": "Bireylerin %50'sinde ağrılı uyarıya karşı kas kontraksiyonu oluşmasını önleyen anestezik maddenin alveoler konsantrasyon oranına ne ad verilir?",
        "secenekler": {
            "A": "Tidal Volüm (TV)",
            "B": "Minimum Alveoler Konsantrasyon (MAC)",
            "C": "Fonksiyonel Rezidüel Kapasite (FRC)",
            "D": "Kardiyak İndeks (CI)"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; bu tanım Minimum Alveoller Konsantrasyona (MAC) aittir (Slayt 10).",
            "celdirici_analizi": "MAC genel anesteziklerin gücünü belirleyen standart farmakolojik parametredir."
        },
        "slayt_no": 10,
        "zorluk_derecesi": "kolay",
        "etiketler": ["mac_tanimi", "farmakoloji"]
    },
    {
        "soru_id": "mcq_inh_013",
        "soru_metni": "İnhalasyon anesteziklerinde 'MAC değeri' ile 'anesteziklerin gücü' arasındaki matematiksel ilişki nasıldır?",
        "secenekler": {
            "A": "Doğru orantılıdır (MAC büyüdükçe güç artar)",
            "B": "Ters orantılıdır (MAC küçüldükçe güç artar)",
            "C": "Aralarında hiçbir ilişki yoktur",
            "D": "Sadece atlarda doğru orantılı, diğer türlerde bağımsızdır"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; MAC değeriyle anesteziklerin gücü TERS ORANTILIDIR (Slayt 10).",
            "celdirici_analizi": "Daha düşük konsantrasyonda anestezi oluşturan ajan daha güçlüdür."
        },
        "slayt_no": 10,
        "zorluk_derecesi": "kolay",
        "etiketler": ["mac_guc_iliskisi", "ters_oranti"]
    },
    {
        "soru_id": "mcq_inh_014",
        "soru_metni": "Aşağıdaki inhalasyon anesteziklerinden hangisi MAC DEĞERİ EN KÜÇÜK olan ve dolayısıyla EN GÜÇLÜ kabul edilen maddedir?",
        "secenekler": {
            "A": "Nitrous oxide (N2O)",
            "B": "Metoksifluran",
            "C": "Desfluran",
            "D": "Sevofluran"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Metoksifluran MAC değeri en küçük, en güçlü genel anestezik maddedir (Slayt 10).",
            "celdirici_analizi": "N2O ise MAC değeri en büyük ve en zayıf olandır."
        },
        "slayt_no": 10,
        "zorluk_derecesi": "orta",
        "etiketler": ["metoksifluran", "en_guclu"]
    },
    {
        "soru_id": "mcq_inh_015",
        "soru_metni": "MAC değeri en yüksek olan ve bu nedenle tek başına cerrahi anestezi oluşturamayan EN ZAYIF genel anestezik madde hangisidir?",
        "secenekler": {
            "A": "Halotan",
            "B": "İzofluran",
            "C": "Nitrous oxide (N2O)",
            "D": "Metoksifluran"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; N2O MAC değeri en yüksek, en zayıf genel anestezik maddedir (Slayt 10).",
            "celdirici_analizi": "Slayt 10'da açıkça vurgulanmıştır."
        },
        "slayt_no": 10,
        "zorluk_derecesi": "kolay",
        "etiketler": ["n2o", "en_zayif"]
    },
    {
        "soru_id": "mcq_inh_016",
        "soru_metni": "Gaz komprese damlatılan sıvı anesteziğin doğrudan hayvanın ağız ve burnunu kapatacak şekilde tutulmasıyla uygulanan yöntem hangisidir?",
        "secenekler": {
            "A": "Açık Damlatma Yöntemi",
            "B": "Yarı Açık Damlatma Yöntemi",
            "C": "Endotrakeal Entübasyon",
            "D": "Anestezi Kutusu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; gaz komprese damlatılıp ağız burun kapatılarak uygulanması Açık Damlatma Yöntemidir (Slayt 12).",
            "celdirici_analizi": "Maske kullanılmaz, sadece kompres tutulur."
        },
        "slayt_no": 12,
        "zorluk_derecesi": "kolay",
        "etiketler": ["acik_damlatma", "teknik"]
    },
    {
        "soru_id": "mcq_inh_017",
        "soru_metni": "Dip kısmında hayvanın soluk almasını sağlayacak delikler bulunan bir maske içerisine gaz kompres yerleştirilerek yapılan yöntem hangisidir?",
        "secenekler": {
            "A": "Açık Damlatma",
            "B": "Yarı Açık Damlatma Yöntemi",
            "C": "Kapalı Devre Entübasyon",
            "D": "Cam Fanus"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; delikli maske içine gaz kompres konulması Yarı Açık Damlatma Yöntemidir (Slayt 13).",
            "celdirici_analizi": "Slayt 13'te bu teknik ayrıntılı tarif edilmiştir."
        },
        "slayt_no": 13,
        "zorluk_derecesi": "kolay",
        "etiketler": ["yari_acik_damlatma", "teknik"]
    },
    {
        "soru_id": "mcq_inh_018",
        "soru_metni": "Anestezi kutusu ve cam fanus yöntemi sıklıkla hangi hasta grubunun anestezisi için tercih edilir?",
        "secenekler": {
            "A": "Yarış atları",
            "B": "Süt sığırları",
            "C": "Küçük laboratuvar hayvanları",
            "D": "Büyük ırk köpekler"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; anestezi kutusu ve cam fanus küçük laboratuvar hayvanlarının anestezisinde uygulanır (Slayt 14).",
            "celdirici_analizi": "Kemirgenler kutu içine konularak buhar solutulur."
        },
        "slayt_no": 14,
        "zorluk_derecesi": "kolay",
        "etiketler": ["anestezi_kutusu", "lab_hayvani"]
    },
    {
        "soru_id": "mcq_inh_019",
        "soru_metni": "Hayvanın trakeası içerisine tüp yerleştirilerek anestezi cihazı ile bağlantı kurulması esasına dayanan yöntem hangisidir?",
        "secenekler": {
            "A": "Açık Damlatma Yöntemi",
            "B": "Endotrakeal Entübasyon Aracılığı ile Anestezi",
            "C": "Anestezi Kutusu",
            "D": "Damla infüzyonu"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; trakeaya tüp yerleştirilip cihazla solutulması Endotrakeal Entübasyon yöntemidir (Slayt 15).",
            "celdirici_analizi": "Modern anestezinin temelidir."
        },
        "slayt_no": 15,
        "zorluk_derecesi": "kolay",
        "etiketler": ["entubasyon", "standart"]
    },
    {
        "soru_id": "mcq_inh_020",
        "soru_metni": "Aşağıdakilerden hangisi ideal bir inhalasyon anesteziğinde bulunması gereken özelliklerden biri DEĞİLDİR?",
        "secenekler": {
            "A": "Solunum yolları için irritan olmamalı ve kötü kokmamalı",
            "B": "Hızlı indüksiyon ve uyanma sağlamalı",
            "C": "Yanıcı ve patlayıcı olmalı",
            "D": "Toksik olmamalı ve ucuz olmalı"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği yanlıştır; ideal anesteziğin yanıcı ve patlayıcı OLMAMASI gerekir (Slayt 16).",
            "celdirici_analizi": "A, B ve D şıkları ideal anesteziğin aranan özellikleridir."
        },
        "slayt_no": 16,
        "zorluk_derecesi": "kolay",
        "etiketler": ["ideal_anestezik", "ozellikler"]
    },
    {
        "soru_id": "mcq_inh_021",
        "soru_metni": "İlk kullanılan anesteziklerden olan Dietil eterin ameliyathanelerde patlamalara neden olabilen fiziksel tehlikesi nedir?",
        "secenekler": {
            "A": "Radyoaktif olması",
            "B": "Elektrikli aletlerin olduğu ortamlarda yanıcı ve patlayıcı olması",
            "C": "Oksijenle birleşince donması",
            "D": "Yüksek basınca dayanıksız olması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; elektrikli aletlerin olduğu ortamlarda kullanılması patlamalara neden olabilir (Slayt 17).",
            "celdirici_analizi": "Elektrokoter ve elektrikli cerrahi aletler eter buharını ateşleyebilir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "kolay",
        "etiketler": ["dietil_eter", "patlama_riski"]
    },
    {
        "soru_id": "mcq_inh_022",
        "soru_metni": "Dietil eterin indüksiyonunun ve uyanmasının OLDUKÇA YAVAŞ olmasının fiziko-kimyasal nedeni nedir?",
        "secenekler": {
            "A": "Molekül ağırlığının sıfır olması",
            "B": "Kan/gaz erime katsayısının çok yüksek olması",
            "C": "Kanda hiç çözünmemesi",
            "D": "Akciğerlerden hiç emilmemesi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kan/gaz erime katsayısı çok yüksek olduğu için indüksiyon ve uyanma oldukça yavaştır (Slayt 17).",
            "celdirici_analizi": "Kanda aşırı çözündüğü için beyne geçişi ve temizlenmesi gecikir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "orta",
        "etiketler": ["dietil_eter", "kan_gaz_katsayisi"]
    },
    {
        "soru_id": "mcq_inh_023",
        "soru_metni": "Nitrous oxide (N2O) ile ilgili aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "secenekler": {
            "A": "Aşırı derecede yanıcı ve patlayıcıdır",
            "B": "Yanıcı ve patlayıcı değildir; veteriner anestezide güçlü analjezik özelliğinden dolayı kullanılır",
            "C": "Tek başına en derin cerrahi anesteziyi sağlar",
            "D": "Kan/gaz erime katsayısı çok yüksek olduğundan uyanması günler sürer"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; N2O yanıcı/patlayıcı değildir, analjeziktir ve diğer ajanların etkisini artırır (Slayt 18).",
            "celdirici_analizi": "A, C ve D şıkları N2O özelliklerinin tam tersidir."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "orta",
        "etiketler": ["n2o", "ozellikler"]
    },
    {
        "soru_id": "mcq_inh_024",
        "soru_metni": "Nitrous oxide (N2O) gazının pratik veteriner cerrahi kullanımında oksijen ile karışım oranı nasıldır?",
        "secenekler": {
            "A": "1:1 oranında (%50 O2 - %50 N2O)",
            "B": "1:10 oranında (%10 O2 - %90 N2O)",
            "C": "Saf N2O (%100 N2O)",
            "D": "1:50 oranında"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; pratik kullanımda oksijen ile 1:1 oranında kullanılır (Slayt 18).",
            "celdirici_analizi": "Hipoksiyi önlemek için oksijen oranı en az %50 tutulmalıdır."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "kolay",
        "etiketler": ["n2o", "oksijen_orani"]
    },
    {
        "soru_id": "mcq_inh_025",
        "soru_metni": "Halotanın (Halothane) MAC değeri ve analjezik özelliği hangisinde doğru verilmiştir?",
        "secenekler": {
            "A": "MAC 100 / Çok güçlü analjezik",
            "B": "MAC 0.74 (güçlü bir anestezik) / Analjezik özelliği iyi değildir",
            "C": "MAC 5.0 / Analjezisi yoktur",
            "D": "MAC 0.01 / Kusursuz analjeziktir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Halotan güçlüdür (MAC 0.74) ancak analjezik özelliği iyi değildir (Slayt 19).",
            "celdirici_analizi": "Slayt 19'da 'Güçlü bir inhalasyon anesteziğidir (MAC 0.74)... analjezik özelliği iyi değildir' denilmiştir."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "orta",
        "etiketler": ["halotan", "mac_074"]
    },
    {
        "soru_id": "mcq_inh_026",
        "soru_metni": "Halotan uygulanması serebral kan akımı ve beyin omurilik sıvısı (BOS) üzerinde nasıl bir etki oluşturur?",
        "secenekler": {
            "A": "Serebral kan akışını azaltır ve BOS emilimini artırır",
            "B": "Serebral kan akışını arttırır ve BOS emilimini azaltarak intrakraniyal basınçta artmaya neden olur",
            "C": "Beyin damarlarını tamamen büzer",
            "D": "BOS yapımını tamamen durdurur"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; halotan serebral kan akışını artırır ve BOS emilimini azaltarak kafa içi basıncı artırır (Slayt 19).",
            "celdirici_analizi": "Bu nedenle kafa travmasında tavsiye edilmez."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "zor",
        "etiketler": ["halotan", "intrakraniyal_basinc"]
    },
    {
        "soru_id": "mcq_inh_027",
        "soru_metni": "Halotanın karaciğer hastalıklarında KULLANILMAMASININ temel nedeni nedir?",
        "secenekler": {
            "A": "%20 - 40 oranında karaciğerde metabolize olması",
            "B": "Karaciğere hiç uğramaması",
            "C": "Safra kesesini patlatması",
            "D": "Karaciğer enzimlerini tamamen yok etmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; %20-40 oranında karaciğerde metabolize olmasından dolayı karaciğer hastalıklarında kullanılmaz (Slayt 19).",
            "celdirici_analizi": "Yüksek metabolizma oranı halotan hepatiti riskini doğurur."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "orta",
        "etiketler": ["halotan", "karaciger_metabolizma"]
    },
    {
        "soru_id": "mcq_inh_028",
        "soru_metni": "1970-1980 yıllarında sıklıkla kullanılmış olan, İzofluranın izomeri olan ve serebral kan akımını halotandan daha fazla artıran anestezik hangisidir?",
        "secenekler": {
            "A": "Enflurane (Enfluran)",
            "B": "Metoksifluran",
            "C": "Sevofluran",
            "D": "Dietil eter"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Enfluran izofluranın izomeridir ve serebral akımı halotandan çok artırır (Slayt 20).",
            "celdirici_analizi": "Slayt 20'de özellikleri sıralanmıştır."
        },
        "slayt_no": 20,
        "zorluk_derecesi": "orta",
        "etiketler": ["enfluran", "izofluran_izomeri"]
    },
    {
        "soru_id": "mcq_inh_029",
        "soru_metni": "İzofluranın (Isoflurane) maske ile indüksiyonda kullanılmasını sınırlandıran fiziksel özelliği nedir?",
        "secenekler": {
            "A": "Tatlı kokusu",
            "B": "Keskin kokusu",
            "C": "Kokusuz olması",
            "D": "Sarı renkli duman çıkarması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; keskin kokusu indüksiyonda kullanılmasını sınırlar (Slayt 21).",
            "celdirici_analizi": "Keskin koku hayvanlarda solunum tutma refleksi başlatır."
        },
        "slayt_no": 21,
        "zorluk_derecesi": "kolay",
        "etiketler": ["izofluran", "keskin_koku"]
    },
    {
        "soru_id": "mcq_inh_030",
        "soru_metni": "Veteriner cerrahide Enfluran yerine İzofluran kullanılmasının iki temel gerekçesi hangisinde verilmiştir?",
        "secenekler": {
            "A": "Daha ucuz olması ve sarı renkli olması",
            "B": "Kaslarda miyorelaksan etkisinin daha fazla olması ve daha düşük kan:gaz katsayısından dolayı kısa sürede uyanma sağlaması",
            "C": "Böbrekten hiç atılmaması ve kalbi hızlandırması",
            "D": "Sadece atlarda kullanılabilmesi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kas gevşetici etkisinin fazla olması ve düşük kan:gaz katsayısıyla hızlı uyanma sağlamasıdır (Slayt 21).",
            "celdirici_analizi": "Slayt 21'in son paragrafında açıkça belirtilmiştir."
        },
        "slayt_no": 21,
        "zorluk_derecesi": "orta",
        "etiketler": ["izofluran_ustunlukleri", "enfluran_karsilastirma"]
    },
    {
        "soru_id": "mcq_inh_031",
        "soru_metni": "Kafa travması geçiren, beyin tümörü olan veya intrakraniyal basıncı yüksek hayvanlarda İzofluranın TERCİH EDİLMESİNİN nedeni nedir?",
        "secenekler": {
            "A": "Serebrospinal sıvı (BOS) emilimini arttırması ancak yapımını arttırmayarak kafa içi basıncı azaltması",
            "B": "Beyin dokusunu tamamen dondurması",
            "C": "Serebral kan akımını 5 katına çıkarması",
            "D": "Kafatası kemiklerini esnetmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; BOS emilimini artırır yapımını artırmaz, bu nedenle kafa içi basınç ve BOS hacminde azalma yapar (Slayt 22).",
            "celdirici_analizi": "Slayt 22'de kırmızıyla vurgulanmış kritik klinik endikasyondur."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "zor",
        "etiketler": ["izofluran", "kafa_travmasi", "bos_emilimi"]
    },
    {
        "soru_id": "mcq_inh_032",
        "soru_metni": "İzofluranın vücutta (karaciğerde) metabolize olma oranı yaklaşık ne kadardır?",
        "secenekler": {
            "A": "%50",
            "B": "%20 - 40",
            "C": "%5",
            "D": "%0.2"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği doğrudur; İzofluranın metabolize olma oranı sadece %0.2'dir (Slayt 22).",
            "celdirici_analizi": "Neredeyse tamamen akciğerlerden değişmeden atılır."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "orta",
        "etiketler": ["izofluran", "metabolizma_orani"]
    },
    {
        "soru_id": "mcq_inh_033",
        "soru_metni": "Tatlı kokulu olan, solunum yollarını irrite etmeyen ve bu sayede maske ile indüksiyonda rahatlıkla tercih edilen anestezik hangisidir?",
        "secenekler": {
            "A": "Sevoflurane (Sevofluran)",
            "B": "Dietil eter",
            "C": "Halotan",
            "D": "Desfluran"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Sevofluran tatlı kokuludur ve solunum yollarını irrite etmez, indüksiyonda çok rahattır (Slayt 23).",
            "celdirici_analizi": "İzofluran ve desfluran keskin kokuluyken sevofluran tatlı kokuludur."
        },
        "slayt_no": 23,
        "zorluk_derecesi": "kolay",
        "etiketler": ["sevofluran", "tatli_koku", "induksiyon"]
    },
    {
        "soru_id": "mcq_inh_034",
        "soru_metni": "Sevofluranın intrakraniyal basınç ve karaciğer metabolizması ile ilgili özellikleri hangisinde doğru verilmiştir?",
        "secenekler": {
            "A": "İntrakraniyal basıncı aşırı yükseltir / %50 metabolize olur",
            "B": "İntrakraniyal basıncı izoflurana göre daha stabil tutar / Karaciğerde %5'i metabolize olur",
            "C": "BOS yapımını durdurur / %90 metabolize olur",
            "D": "Yalnızca böbrekte metabolize olur"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; intrakraniyal basıncı izoflurana göre daha stabil tutar, karaciğerde %5'i metabolize olur (Slayt 23).",
            "celdirici_analizi": "Slayt 23'te açıkça belirtilmiştir."
        },
        "slayt_no": 23,
        "zorluk_derecesi": "orta",
        "etiketler": ["sevofluran", "metabolizma_kib"]
    },
    {
        "soru_id": "mcq_inh_035",
        "soru_metni": "Kanda çözünebilirliği çok düşük olduğu için anestezik ajanlar içinde 'EN HIZLI İNDÜKSİYON VE UYANMA' sağlayan madde hangisidir?",
        "secenekler": {
            "A": "Dietil eter",
            "B": "Halotan",
            "C": "Desflurane (Desfluran)",
            "D": "Metoksifluran"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; Desfluran kanda çözünürlüğü çok düşük olduğundan en hızlı indüksiyon ve uyanmayı sağlar (Slayt 24).",
            "celdirici_analizi": "Slayt 24'ün ilk cümlesinde belirtilmiştir."
        },
        "slayt_no": 24,
        "zorluk_derecesi": "kolay",
        "etiketler": ["desfluran", "en_hizli_uyanma"]
    },
    {
        "soru_id": "mcq_inh_036",
        "soru_metni": "Aşağıdakilerden hangisi Desfluranın klinik kullanımını sınırlandıran temel dezavantajlarından biridir?",
        "secenekler": {
            "A": "Anestezik gücünün düşük olması, keskin kokusu, taşikardi/solunum irritasyonu yapabilmesi ve pahalı fiyatı",
            "B": "Aşırı yavaş uyanma sağlaması",
            "C": "Karaciğerde %80 metabolize olması",
            "D": "Sadece oda havasıyla solutulabilmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; anestezik gücü düşük, keskin kokulu, irritan, taşikardi yapabilen ve pahalı bir ajandır (Slayt 24).",
            "celdirici_analizi": "B, C ve D seçenekleri desfluranın özellikleriyle çelişir."
        },
        "slayt_no": 24,
        "zorluk_derecesi": "orta",
        "etiketler": ["desfluran", "dezavantajlar"]
    },
    {
        "soru_id": "mcq_inh_037",
        "soru_metni": "İnhalasyon anesteziklerinden hangisi yüksek konsantrasyonlarda verildiğinde taşikardiye ve solunum yollarında belirgin irritasyona neden olabilir?",
        "secenekler": {
            "A": "Sevofluran",
            "B": "Desfluran",
            "C": "Halotan",
            "D": "Azot protoksit"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Desfluran yüksek konsantrasyonda taşikardiye ve solunum yolu irritasyonuna yol açabilir (Slayt 24).",
            "celdirici_analizi": "Slayt 24'ün 3. maddesinde belirtilmiştir."
        },
        "slayt_no": 24,
        "zorluk_derecesi": "orta",
        "etiketler": ["desfluran", "tasikardi"]
    },
    {
        "soru_id": "mcq_inh_038",
        "soru_metni": "Aşağıdaki anesteziklerden hangisi yanıcı ve patlayıcı özelliğe sahip olduğu için günümüzde ameliyathanelerde terk edilmiştir?",
        "secenekler": {
            "A": "Halotan",
            "B": "İzofluran",
            "C": "Dietil eter",
            "D": "Sevofluran"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; Dietil eter yanıcı ve patlayıcıdır (Slayt 17).",
            "celdirici_analizi": "Halotan, izofluran ve sevofluran yanıcı ve patlayıcı değildir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "kolay",
        "etiketler": ["dietil_eter", "yanici_patlayici"]
    },
    {
        "soru_id": "mcq_inh_039",
        "soru_metni": "Veteriner hekimlikte anestezik derinliğin takibinde MAC değerinin 1.3 katı (1.3 x MAC) genellikle neyi ifade eder?",
        "secenekler": {
            "A": "Ölümcül doz sınırını",
            "B": "Cerrahi anestezi derinliğini (hastaların %95'inde cerrahi kesiye yanıtı önleyen dozu)",
            "C": "Uyanma anını",
            "D": "Premedikasyon öncesi dozu"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 1 MAC hastaların %50'sinde, 1.3 - 1.5 MAC ise cerrahi işlemler için gereken güvenli derinliği sağlar (Slayt 10).",
            "celdirici_analizi": "1 MAC cerrahi için tek başına yetersiz kalabilir, 1.3 MAC cerrahi standarttır."
        },
        "slayt_no": 10,
        "zorluk_derecesi": "orta",
        "etiketler": ["mac", "cerrahi_derinlik"]
    },
    {
        "soru_id": "mcq_inh_040",
        "soru_metni": "Hangi inhalasyon anesteziği gebe hayvanlarda uterus gevşemesi ve fetal risk nedeniyle tavsiye edilmez?",
        "secenekler": {
            "A": "Halothane",
            "B": "Metoksifluran",
            "C": "Sevofluran",
            "D": "Azot protoksit"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; gebe hayvanlarda ve kafa içi basıncı artmış olanlarda Halotan kullanımı tavsiye edilmez (Slayt 19).",
            "celdirici_analizi": "Slayt 19'da açıkça 'Gebe hayvanlarda... kullanımı tavsiye edilmez' denilmiştir."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "orta",
        "etiketler": ["halotan", "gebelik"]
    },
    {
        "soru_id": "mcq_inh_041",
        "soru_metni": "İnhalasyon anesteziklerinin alım ve dağılımında dokulardaki yağ oranının rolü nedir?",
        "secenekler": {
            "A": "Hiçbir etkisi yoktur",
            "B": "Lipofilik olan anestezik gazlar yağ dokusunda depolanabilir ve bu durum dağılım ile uyanma süresini etkiler",
            "C": "Yağ dokusu gazı imha eder",
            "D": "Yağ oranı yüksekse anestezi asla oluşmaz"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; dokulardaki yağ oranı anestezik maddenin alımını, dokulara dağılımını ve vücuttan atılmasını etkiler (Slayt 5).",
            "celdirici_analizi": "Lipofilik anestezikler yağda tutularak redistribüsyon gösterir."
        },
        "slayt_no": 5,
        "zorluk_derecesi": "orta",
        "etiketler": ["yag_orani", "dagilim"]
    },
    {
        "soru_id": "mcq_inh_042",
        "soru_metni": "İnhalasyon anestezisinde 'Anestezi derinliğinin kontrol edilmesi kolaydır' ifadesi özellikle hangi iki modern ajan için en belirgindir?",
        "secenekler": {
            "A": "Eter ve Kloroform",
            "B": "İzofluran ve Sevofluran",
            "C": "Siklopropan ve Metoksifluran",
            "D": "Azot protoksit ve Eter"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; düşük kan/gaz çözünürlükleri sayesinde İzofluran ve Sevofluran ile derinlik kontrolü son derece kolay ve hızlıdır (Slayt 21, 23).",
            "celdirici_analizi": "Modern ajanların en büyük konforudur."
        },
        "slayt_no": 21,
        "zorluk_derecesi": "kolay",
        "etiketler": ["izofluran_sevofluran", "kontrol_kolayligi"]
    },
    {
        "soru_id": "mcq_inh_043",
        "soru_metni": "Aşağıdaki inhalasyon ajanlarından hangisinin karaciğerde metabolize olma oranı EN DÜŞÜKTÜR?",
        "secenekler": {
            "A": "Halotan (%20-40)",
            "B": "Sevofluran (%5)",
            "C": "Enfluran (%2-5)",
            "D": "İzofluran (%0.2)"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği doğrudur; İzofluran sadece %0.2 metabolize olma oranı ile açık ara en düşük orana sahiptir (Slayt 22).",
            "celdirici_analizi": "Halotan %20-40, Sevofluran %5, Enfluran %2-5'tir."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "kolay",
        "etiketler": ["metabolizma_karsilastirma"]
    },
    {
        "soru_id": "mcq_inh_044",
        "soru_metni": "Mukoz membranlarda irritasyon oluşturmayan ve sekresyona neden olmayan güçlü ajan hangisidir?",
        "secenekler": {
            "A": "Halothane",
            "B": "Dietil eter",
            "C": "Desfluran",
            "D": "Kloroform"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Halotan mukoz membranlarda irritasyon oluşturmaz ve sekresyona neden olmaz (Slayt 19).",
            "celdirici_analizi": "Eter ve desfluran irritandır; halotan mukozayı tahriş etmez."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "orta",
        "etiketler": ["halotan", "irritasyon_yapmaz"]
    },
    {
        "soru_id": "mcq_inh_045",
        "soru_metni": "Küçük hayvanlarda anestezi cihazına monte edilebilen maskeler kullanılarak hangi işlem sağlanabilir?",
        "secenekler": {
            "A": "Anestezinin indüksiyonunun sağlanması ya da kısa süreli genel anestezi oluşturulması",
            "B": "Yalnızca kan sayımı yapılması",
            "C": "Diş çekimi operasyonunun 5 saat sürdürülmesi",
            "D": "Hayvanın vücut ağırlığının ölçülmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; maskelerle indüksiyon veya kısa süreli anestezi sağlanır (Slayt 15).",
            "celdirici_analizi": "Slayt 15'in son cümlesinde belirtilmiştir."
        },
        "slayt_no": 15,
        "zorluk_derecesi": "kolay",
        "etiketler": ["maske_induksiyonu", "kucuk_hayvan"]
    },
    {
        "soru_id": "mcq_inh_046",
        "soru_metni": "İnhalasyon anesteziğinde 'kan/gaz erime katsayısının çok düşük olması' ne anlama gelir?",
        "secenekler": {
            "A": "Anesteziğin kanda çok fazla çözünüp uyanmanın saatler sürmesi",
            "B": "Anesteziğin kanda az çözünerek kanda ve beyinde parsiyel basıncının süratle yükselmesi ve uyanmanın da çok çabuk olması",
            "C": "Anesteziğin sadece suda erimesi",
            "D": "Anesteziğin damarları tıkaması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; düşük kan/gaz katsayısı hızlı indüksiyon ve hızlı uyanma demektir (Slayt 18, 21, 24).",
            "celdirici_analizi": "Kanda az eriyen gaz hızla beyne geçer ve kandan hızla atılır."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "orta",
        "etiketler": ["kan_gaz_katsayisi", "fizyoloji"]
    },
    {
        "soru_id": "mcq_inh_047",
        "soru_metni": "Aşağıdakilerden hangisi N2O'nun diğer inhalasyon anestezikleriyle kombine edilmesinin temel klinik gerekçesidir?",
        "secenekler": {
            "A": "Onların etkilerini arttırıcı (MAC değerlerini düşürücü) özelliğe sahip olması",
            "B": "Onların fiyatını artırmak",
            "C": "Vaporizatörün ısınmasını sağlamak",
            "D": "Kanisterdeki sodalime'ı korumak"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; diğer anesteziklerle kombine kullanılır ve onların etkilerini artırıcı özelliğe sahiptir (Slayt 18).",
            "celdirici_analizi": "İkinci gaz etkisi ve MAC azaltıcı sinerji sağlar."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "kolay",
        "etiketler": ["n2o", "kombinasyon"]
    },
    {
        "soru_id": "mcq_inh_048",
        "soru_metni": "İzofluran anestezisinde iskelet kaslarının durumu nasıldır?",
        "secenekler": {
            "A": "Aşırı derecede sertleşir ve kasılır (rijidite)",
            "B": "Çok iyi düzeyde kas gevşemesi (miyorelaksasyon) meydana gelir",
            "C": "Tetanik kramplar başlar",
            "D": "Kas tonusu hiç değişmez"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; İzofluran anestezisi ile çok iyi düzeyde kas gevşemesi meydana gelir (Slayt 21).",
            "celdirici_analizi": "Cerrahi rahatlık sağlayan güçlü miyorelaksan etkisi vardır."
        },
        "slayt_no": 21,
        "zorluk_derecesi": "kolay",
        "etiketler": ["izofluran", "kas_gevsemesi"]
    },
    {
        "soru_id": "mcq_inh_049",
        "soru_metni": "Sevofluran kanda eriyebilirliğinin çok düşük olması sayesinde ne sağlar?",
        "secenekler": {
            "A": "Kısa sürede indüksiyon ve uyanma sağlar",
            "B": "Uyanmayı 24 saat geciktirir",
            "C": "Kandaki trombositleri tüketir",
            "D": "Kan basıncını iki katına çıkarır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kanda eriyebilirliği çok düşük olduğu için kısa sürede indüksiyon ve uyanma sağlar (Slayt 23).",
            "celdirici_analizi": "Slayt 23'te açıkça belirtilmiştir."
        },
        "slayt_no": 23,
        "zorluk_derecesi": "kolay",
        "etiketler": ["sevofluran", "hizli_induksiyon"]
    },
    {
        "soru_id": "mcq_inh_050",
        "soru_metni": "Solunum yollarındaki irritasyonundan dolayı diğer modern ajanlara kıyasla veteriner pratikte daha az sıklıkla kullanılan ajan hangisidir?",
        "secenekler": {
            "A": "Desflurane",
            "B": "Sevoflurane",
            "C": "İsoflurane",
            "D": "Nitrous oxide"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; solunum yollarındaki irritasyonundan dolayı Desfluran daha az sıklıkla kullanılır (Slayt 24).",
            "celdirici_analizi": "Slayt 24'ün son cümlesinde ifade edilmiştir."
        },
        "slayt_no": 24,
        "zorluk_derecesi": "kolay",
        "etiketler": ["desfluran", "az_kullanilma"]
    },
    {
        "soru_id": "mcq_inh_051",
        "soru_metni": "İnhalasyon anesteziklerinin vücuttan atılımında (uyanmada) rol oynayan en temel organ hangisidir?",
        "secenekler": {
            "A": "Böbrekler",
            "B": "Karaciğer",
            "C": "Akciğerler",
            "D": "Deri"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; inhalasyon anestezikleri büyük oranda metabolize olmadan akciğer yolu ile atılır (Slayt 2, 9).",
            "celdirici_analizi": "Solunum yolu ile eliminasyon temel prensiptir."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "kolay",
        "etiketler": ["eliminasyon", "akciger"]
    },
    {
        "soru_id": "mcq_inh_052",
        "soru_metni": "Aşağıdaki anesteziklerden hangisi insan hekimliğinde kullanımı azalmasına rağmen günümüzde veteriner sahada 'en yaygın' kullanılan ajandır?",
        "secenekler": {
            "A": "İsoflurane",
            "B": "Eter",
            "C": "Kloroform",
            "D": "Siklopropan"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; insan hekimliğinde kullanımı azalmış ancak veteriner sahada yaygın olarak kullanılır (Slayt 21).",
            "celdirici_analizi": "Slayt 21'in ilk cümlesidir."
        },
        "slayt_no": 21,
        "zorluk_derecesi": "kolay",
        "etiketler": ["izofluran", "veteriner_sahada_yaygin"]
    },
    {
        "soru_id": "mcq_inh_053",
        "soru_metni": "İndüksiyon ve uyanma dönemlerinde şiddetli bulantı ve kusmaya neden olabilen tarihsel inhalasyon anesteziği hangisidir?",
        "secenekler": {
            "A": "Dietil eter",
            "B": "Sevofluran",
            "C": "İzofluran",
            "D": "Desfluran"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Dietil eter indüksiyon ve uyanma dönemlerinde bulantı ve kusmaya neden olabilir (Slayt 17).",
            "celdirici_analizi": "Slayt 17'de eterin klasik komplikasyonu olarak verilmiştir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "orta",
        "etiketler": ["dietil_eter", "kusma"]
    },
    {
        "soru_id": "mcq_inh_054",
        "soru_metni": "Halotan metabolitleri vücuttan hangi yolla atılır?",
        "secenekler": {
            "A": "İdrar ile",
            "B": "Tükürük ile",
            "C": "Ter ile",
            "D": "Safra taşı olarak"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; karaciğerde metabolize olan halotanın metabolitleri idrar ile atılır (Slayt 19).",
            "celdirici_analizi": "Slayt 19'un son cümlesinde 'Oluşan metabolitler idrar ile atılır' ifadesi mevcuttur."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "orta",
        "etiketler": ["halotan", "idrar_atilim"]
    },
    {
        "soru_id": "mcq_inh_055",
        "soru_metni": "Aşağıdaki anestezik gazlardan hangisi solunum havasında tek başına %80 konsantrasyonda verilse dahi cerrahi anestezi oluşturamaz?",
        "secenekler": {
            "A": "İzofluran",
            "B": "Halotan",
            "C": "Nitrous oxide (N2O)",
            "D": "Sevofluran"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; N2O tek başına kullanılması ile cerrahi anestezi oluşturulması mümkün değildir (Slayt 18).",
            "celdirici_analizi": "MAC değeri hayvanlarda %100'ün üzerindedir."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "orta",
        "etiketler": ["n2o", "yetersiz_derinlik"]
    },
    {
        "soru_id": "mcq_inh_056",
        "soru_metni": "Anestezi gazı akciğerlere ulaştığında difüzyonun yönünü ve hızını belirleyen temel fiziksel etmen nedir?",
        "secenekler": {
            "A": "Alveol ile kandaki gaz parsiyel basınç (yoğunluk) farkı",
            "B": "Hastanın boyu",
            "C": "Odanın aydınlığı",
            "D": "Cihazın markası"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; alveol ile kandaki parsiyel basınç farkı difüzyonun yönünü ve akışını tayin eder (Slayt 6).",
            "celdirici_analizi": "Gaz yüksek parsiyel basınçtan düşük olana diffüze olur."
        },
        "slayt_no": 6,
        "zorluk_derecesi": "kolay",
        "etiketler": ["parsiyel_basinc_farki", "difuzyon"]
    },
    {
        "soru_id": "mcq_inh_057",
        "soru_metni": "Halotanın keşfedildiği 1951 yılından önce yapılan cerrahi müdahalelerde karşılaşılan temel sorunlar nelerdi?",
        "secenekler": {
            "A": "İleri derecede kardiyovasküler depresyon ve hepatik fonksiyonlarda kötüleşme",
            "B": "Hastaların hiç uyuyamaması",
            "C": "Kemik erimesi",
            "D": "Göz tansiyonu artışı"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; halotan öncesi kardiyovasküler depresyon ve karaciğer fonksiyonlarında kötüleşme sıktı (Slayt 3).",
            "celdirici_analizi": "Kloroform ve eterin ağır yan etkileri yaşanıyordu."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "orta",
        "etiketler": ["tarihce", "halotan_oncesi"]
    },
    {
        "soru_id": "mcq_inh_058",
        "soru_metni": "İnhalasyon anesteziğinde 'akciğerlere dönen venöz kanın yeniden gaz ile yüklenmesi' döngüsü ne zaman yavaşlar?",
        "secenekler": {
            "A": "Hasta su içtiğinde",
            "B": "Dokularda ve beyinde anestezik yoğunluğu arttıkça (doygunluğa yaklaştıkça)",
            "C": "Oksijen tüpü değiştirildiğinde",
            "D": "Göz damlası damlatıldığında"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; dokularda ve beyinde anestezik yoğunluğu arttıkça anestezik alımı yavaşlar (Slayt 7, 8).",
            "celdirici_analizi": "Konsantrasyon gradyenti azaldıkça alım hızı düşer."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "orta",
        "etiketler": ["gaz_alimi_yavaslama", "doygunluk"]
    },
    {
        "soru_id": "mcq_inh_059",
        "soru_metni": "Sevofluran ile İzofluran intrakraniyal basınç (KİB) açısından kıyaslandığında Sevofluranın özelliği nedir?",
        "secenekler": {
            "A": "Kafa içi basıncı izoflurana göre daha stabil tutar",
            "B": "Kafa içi basıncı halotandan 10 kat fazla artırır",
            "C": "BOS dolaşımını felç eder",
            "D": "Beyin kanamasını başlatır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; İntrakraniyal basıncı izoflurane göre daha stabil tutar (Slayt 23).",
            "celdirici_analizi": "Slayt 23'te kelimesi kelimesine bu cümle yer alır."
        },
        "slayt_no": 23,
        "zorluk_derecesi": "orta",
        "etiketler": ["sevofluran", "kib_stabilite"]
    },
    {
        "soru_id": "mcq_inh_060",
        "soru_metni": "Aşağıdaki eşleştirmelerden hangisi 'Anestezik Madde - Karakteristik Özellik' açısından DOĞRUDUR?",
        "secenekler": {
            "A": "Sevofluran - Keskin kokulu, irritan",
            "B": "İzofluran - Kafa travmasında tercih edilir, %0.2 metabolize olur",
            "C": "Dietil eter - Çok hızlı indüksiyon, patlayıcı değil",
            "D": "N2O - En güçlü cerrahi anestezik"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; İzofluran kafa travmasında tercih edilir ve metabolize olma oranı %0.2'dir (Slayt 21, 22).",
            "celdirici_analizi": "Sevofluran tatlı kokuludur; eter patlayıcı ve yavaştır; N2O en zayıftır."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "orta",
        "etiketler": ["eslestirme", "ozet"]
    }
]

print(f"İnhalasyon Anestezikleri modülü hazırlandı:")
print(f"- Summary Sections: {len(SUMMARY_SECTIONS)}")
print(f"- Bilgi Kartları: {len(BILGI_KARTLARI)}")
print(f"- Açık Uçlu Sorular: {len(ACIK_UCLU_SORULAR)}")
print(f"- Çoktan Seçmeli Sorular: {len(COKTAN_SECMELI_SORULAR)}")
