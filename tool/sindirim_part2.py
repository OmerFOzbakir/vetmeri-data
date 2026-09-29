# -*- coding: utf-8 -*-
"""
Sindirim Sistemi - Çoktan Seçmeli Sorular (Bölüm 2: 46 - 90)
Kapsam: Slayt 71 - 139 (Oral Tümörler Tedavisi, Eozinofilik Granülom, Özefagitis, Yabancı Cisim, PRAA, Megaözefagus, Akut Gastrit, Sıvı Tedavisi, AHDS, Gastrik Ülser)
"""

QUESTIONS_PART2 = [
    {
        "soru_id": "mcq_sind_046",
        "soru_metni": "Ağız boşluğunda görülen Akantomatöz Ameloblastoma (Acanthomatous ameloblastoma) tümörünün tedavi ve prognozu ile ilgili hangisi DOĞRUDUR?",
        "secenekler": {
            "A": "Kemoterapiye %100 tam yanıt verir, cerrahiye asla gerek duyulmaz",
            "B": "Tek başına radyasyon tedavisine iyi yanıt verebilir ancak cerrahi olarak uzaklaştırılması tercih edilmelidir",
            "C": "Sadece diş macunu uygulamasıyla kendiliğinden geriler",
            "D": "Tümör dokusuna dokunulduğunda hemen akciğere metastaz yapar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; akantomatöz ameloblastomlar radyasyona iyi yanıt verir ancak lokal invaziv oldukları için cerrahi rezeksiyon (mandibulektomi/maksillektomi) birincil tercihtir (Slayt 76).",
            "celdirici_analizi": "Kemoterapi bu tümörlerde etkili değildir."
        },
        "slayt_no": 76,
        "zorluk_derecesi": "orta",
        "etiketler": ["oral_tumor", "ameloblastom", "tedavi"]
    },
    {
        "soru_id": "mcq_sind_047",
        "soru_metni": "Ağız boşluğu karsinomları arasında prognozu 'ÇOK KÖTÜ' olarak bildirilen anatomik yerleşim bölgeleri hangileridir?",
        "secenekler": {
            "A": "Sert damağın ön kısmı ve kesici diş etleri",
            "B": "Dil kökünü etkileyen lingual skuamöz hücreli karsinomlar ve tonsiller karsinomlar",
            "C": "Yanak içi labial mukoza papillomları",
            "D": "Genç köpeklerde görülen dudak papillomları"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; dil kökü (lingual) SCC ve tonsil karsinomları çok agresiftir, cerrahi sınır elde edilemez ve prognozu çok kötüdür (Slayt 76).",
            "celdirici_analizi": "Rostral mandibula tümörlerinde cerrahi başarı çok daha yüksektir."
        },
        "slayt_no": 76,
        "zorluk_derecesi": "orta",
        "etiketler": ["oral_tumor", "lingual_SCC", "prognoz"]
    },
    {
        "soru_id": "mcq_sind_048",
        "soru_metni": "Köpeklerde ağız boşluğu tümörlerinden olan skuamöz hücreli karsinom, akantomatöz ameloblastoma ve melanom olgularında sistemik kemoterapinin etkinliği nasıldır?",
        "secenekler": {
            "A": "Kemoterapi bu tümör tiplerinde etkili DEĞİLDİR",
            "B": "Kemoterapi tek başına tam şifa sağlar",
            "C": "Kemoterapi cerrahiden her zaman daha üstündür",
            "D": "Sadece tek doz vinkristin ile tümör tamamen yok olur"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; skuamoz hücre karsinomu, akantomatöz ameloblastoma ve melanom vakalarında kemoterapi etkili değildir (Slayt 76).",
            "celdirici_analizi": "Cerrahi rezeksiyon ve seçili olgularda radyasyon tedavisi esastır."
        },
        "slayt_no": 76,
        "zorluk_derecesi": "kolay",
        "etiketler": ["oral_tumor", "kemoterapi"]
    },
    {
        "soru_id": "mcq_sind_049",
        "soru_metni": "Feline Eozinofilik Granülom Kompleksinin 'Ülseratif formu' (indolent/rodent ülser) sıklıkla hangi yaş grubunda ve vücudun neresinde lezyon oluşturur?",
        "secenekler": {
            "A": "Yeni doğmuş yavrularda kuyruk ucunda",
            "B": "Orta yaşlı kedilerde üst dudaklarda ve özellikle canin diş hizasındaki mukozada",
            "C": "Sadece geriyatrik kedilerin kulak kepçesinde",
            "D": "Tüm yaş gruplarında sadece tırnak aralarında"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ülseratif form sıklıkla orta yaşlı kedilerde dudaklarda ve özellikle üst canin diş hizasındaki mukozada krater benzeri ülser yapar (Slayt 78).",
            "celdirici_analizi": "A, C ve D seçenekleri eozinofilik ülser yerleşimiyle bağdaşmaz."
        },
        "slayt_no": 78,
        "zorluk_derecesi": "kolay",
        "etiketler": ["eozinofilik_granulom", "ulseratif_form", "kedi"]
    },
    {
        "soru_id": "mcq_sind_050",
        "soru_metni": "Feline Eozinofilik Granülom Kompleksinin 'Eozinofilik plak formu' vücutta en sık hangi anatomik bölgeleri etkiler?",
        "secenekler": {
            "A": "Abdomen derisi ve arka bacakların medial (iç) yüzeyi",
            "B": "Burun ucu ve göz kapakları",
            "C": "Kuyruk sokumu ve perianal bölge",
            "D": "Sadece patilerin plantar taban yastıkları"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; eozinofilik plak formu deriyi tutar ve en sık abdomen derisi ile arka bacakların medial yüzeyinde kabarık plaklar yapar (Slayt 79).",
            "celdirici_analizi": "Lineer granülom ise arka bacağın posterior (arka) yüzünde kordon şeklinde görülür."
        },
        "slayt_no": 79,
        "zorluk_derecesi": "orta",
        "etiketler": ["eozinofilik_plak", "kedi_deri"]
    },
    {
        "soru_id": "mcq_sind_051",
        "soru_metni": "Genç kedilerde arka bacakların posterior (arka) hattında kordon şeklinde sarı-pembe lezyonlarla seyreden ve dil-damağı da tutabilen eozinofilik lezyon tipi hangisidir?",
        "secenekler": {
            "A": "Eozinofilik Linear Granülom",
            "B": "Ülseratif rodent form",
            "C": "Pemfigus foliaseus",
            "D": "Oral skuamöz karsinom"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; özellikle genç kedilerde arka bacağın arka kısmında çizgi/kordon tarzında uzanan lezyon 'Eozinofilik Lineer Granülom'dur (Slayt 80).",
            "celdirici_analizi": "Rodent form üst dudaktadır; pemfigus otoimmün büllöz hastalıktır."
        },
        "slayt_no": 80,
        "zorluk_derecesi": "orta",
        "etiketler": ["lineer_granulom", "kedi"]
    },
    {
        "soru_id": "mcq_sind_052",
        "soru_metni": "Feline Eozinofilik Granülom Kompleksi tanısı alan bir kedide medikal tedavide uygulanan sistemik antibiyotik ve yüksek doz kortikosteroid protokolü hangisidir?",
        "secenekler": {
            "A": "Sadece lokal antiseptik pudra uygulaması",
            "B": "Staphylococcus etkili antibiyotik (Amoksisilin-klavulanat vb.) ve Oral Prednizolon (2.2 - 4.4 mg/kg PO)",
            "C": "Tek doz penisilin ve aspirin",
            "D": "Sadece insülin enjeksiyonu ve diazepam"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; sekonder stafilokok enfeksiyonunu kontrol etmek için antibiyotik ve immün yangıyı baskılamak için yüksek doz oral prednizolon (2.2-4.4 mg/kg) uygulanır (Slayt 81).",
            "celdirici_analizi": "Aspirin kedilerde toksiktir; lokal pudra derin granülomda etkisizdir."
        },
        "slayt_no": 81,
        "zorluk_derecesi": "orta",
        "etiketler": ["eozinofilik_granulom", "tedavi", "prednizolon"]
    },
    {
        "soru_id": "mcq_sind_053",
        "soru_metni": "Kedi ve köpeklerde özefagitis (özefagus mukozası yangısı) gelişiminde en sık karşılaşılan predispoze etiyolojik faktör hangisidir?",
        "secenekler": {
            "A": "Genel anesteziye bağlı Gastroözefagal Reflü (GER)",
            "B": "Aşırı taze su içilmesi",
            "C": "Yalnızca kemik iliği yetersizliği",
            "D": "Soğuk süt tüketimi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; genel anestezi sırasında alt özefagus sfinkter tonusunun düşmesiyle mide asidinin özefagusa kaçması (GER) özefagitisin en yaygın nedenidir (Slayt 83, 85).",
            "celdirici_analizi": "Diğer şıklar özefagitis patogeneziyle ilgili değildir."
        },
        "slayt_no": 83,
        "zorluk_derecesi": "kolay",
        "etiketler": ["ozefagitis", "GER", "anestezi"]
    },
    {
        "soru_id": "mcq_sind_054",
        "soru_metni": "Özefagitisli bir hastada yutkunma sırasında şiddetli ağrı duyulması hangi tıbbi terimle ifade edilir?",
        "secenekler": {
            "A": "Disfaji",
            "B": "Odinofaji",
            "C": "Diskezi",
            "D": "Tenesmus"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ağrılı yutkunma 'Odinofaji' olarak tanımlanır ve ülseratif özefagitiste belirgindir (Slayt 84).",
            "celdirici_analizi": "Disfaji yutma güçlüğüdür; diskezi ağrılı dışkılamadır; tenesmus ıkınmadır."
        },
        "slayt_no": 84,
        "zorluk_derecesi": "kolay",
        "etiketler": ["odinofaji", "ozefagitis", "semptom"]
    },
    {
        "soru_id": "mcq_sind_055",
        "soru_metni": "Özefagitis tedavisinde kullanılan Proton Pompa İnhibitörü 'Omeprazol'ün doğru kullanım dozu ve zamanlaması hangisidir?",
        "secenekler": {
            "A": "0.1 mg/kg haftada bir yemekten sonra",
            "B": "1 mg/kg PO günde 2 kez (G2K), gıda alımından 30 dakika önce",
            "C": "10 mg/kg IV yemek sırasında",
            "D": "5 mg/kg rektal gece yatarken"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Omeprazol 1 mg/kg PO G2K olarak ve paryetal hücre proton pompalarının aktifleşeceği gıda alımından 30 dk önce verilmelidir (Slayt 91).",
            "celdirici_analizi": "Yemekten sonra verilirse biyoyararlanımı ve asit baskılama gücü düşer."
        },
        "slayt_no": 91,
        "zorluk_derecesi": "orta",
        "etiketler": ["omeprazol", "doz", "ozefagitis"]
    },
    {
        "soru_id": "mcq_sind_056",
        "soru_metni": "Özefagitis tedavisinde mukoza koruyucu olarak kullanılan Sukralfat'ın (Sucralfate) oral kullanım dozu nedir?",
        "secenekler": {
            "A": "10 - 20 g günde bir kez",
            "B": "0.5 - 1 g PO günde 3 kez (G3K)",
            "C": "0.01 g haftada bir kez",
            "D": "5 mg/kg IV enjeksiyon"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Sukralfat 0.5-1 g PO G3K olarak süspansiyon halinde uygulanır ve ülser kraterine bağlanarak mukozayı korur (Slayt 91, 97).",
            "celdirici_analizi": "Sukralfat emilmez, lokal etkilidir; IV formu kesinlikle yoktur."
        },
        "slayt_no": 91,
        "zorluk_derecesi": "orta",
        "etiketler": ["sukralfat", "doz", "mukoza_koruyucu"]
    },
    {
        "soru_id": "mcq_sind_057",
        "soru_metni": "Özefagusa yabancı bir cisim takıldığında, lümenin minimal genişleme kabiliyetine sahip olduğu en sık takılma bölgeleri hangileridir?",
        "secenekler": {
            "A": "Sadece orofarenks girişi",
            "B": "Torasik giriş, kalbin tabanı ve özefagal hiatus",
            "C": "Mide piloru ve duodenum kıvrımı",
            "D": "Sadece boynun tam ortası"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; özefagusun elastikiyetinin en az olduğu ve dış baskılara maruz kaldığı yerler: Torasik giriş (apertura thoracis cranialis), kalp tabanı ve diyaframdaki hiatus oesophageus'tur (Slayt 95).",
            "celdirici_analizi": "C şıkkı midededir; A ve D şıkları primer darlık bölgesi değildir."
        },
        "slayt_no": 95,
        "zorluk_derecesi": "orta",
        "etiketler": ["yabanci_cisim", "ozefagus_darliklari"]
    },
    {
        "soru_id": "mcq_sind_058",
        "soru_metni": "Özefagusta yabancı cisim şüphesinde toraks radyografisinde mediastinum ve/veya plevral boşlukta hava ve sıvı saptanması öncelikle neyi düşündürür?",
        "secenekler": {
            "A": "Mide ülserini",
            "B": "Özefagus perforasyonunu (yırtılmasını)",
            "C": "Diyafram rüptürünü",
            "D": "Karaciğer yetmezliğini"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; lümen dışına çıkan hava (pnömomediastinum) ve enfektif sıvı özefagus duvarının delindiğini (perforasyon) kanıtlar (Slayt 95).",
            "celdirici_analizi": "Bu olgularda baryum sülfat verilmesi kesinlikle yasaktır."
        },
        "slayt_no": 95,
        "zorluk_derecesi": "orta",
        "etiketler": ["perforasyon", "ozefagus", "radyoloji"]
    },
    {
        "soru_id": "mcq_sind_059",
        "soru_metni": "Midenin bir kısmının (özellikle kardiyanın) diyaframdaki açıklıktan göğüs boşluğuna kayması ile karakterize hastalık hangisidir?",
        "secenekler": {
            "A": "Hiatal Hernia",
            "B": "Göbek fıtığı (Hernia umbilicalis)",
            "C": "İnguinal herni",
            "D": "Perineal herni"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; midenin özefagal hiatustan toraksa girmesi Hiatal Herniadır (Slayt 98).",
            "celdirici_analizi": "B göbektir; C kasıktır; D anüs çevresidir."
        },
        "slayt_no": 98,
        "zorluk_derecesi": "kolay",
        "etiketler": ["hiatal_herni", "tanim"]
    },
    {
        "soru_id": "mcq_sind_060",
        "soru_metni": "Hiatal herni gelişimine anatomik yapılarından dolayı belirgin predispozisyonu olan köpek ırk grubu hangisidir?",
        "secenekler": {
            "A": "Tazı (Dolichocephalic) ırkları",
            "B": "Brakisefalik (Basık burunlu) ırklar",
            "C": "Mezosefalik av köpekleri",
            "D": "Kutup köpekleri (Sibirya Kurdu)"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; brakisefalik ırklarda negatif intratorakal basınç farkı ve hava yolu direnci nedeniyle hiatal herni yatkınlığı çok yüksektir (Slayt 99).",
            "celdirici_analizi": "Tazı ve av köpekleri bu anomaliye yatkın değildir."
        },
        "slayt_no": 99,
        "zorluk_derecesi": "orta",
        "etiketler": ["brakisefalik", "hiatal_herni"]
    },
    {
        "soru_id": "mcq_sind_061",
        "soru_metni": "Embriyonik sağ aortik arkın gerilemeyip kalması sonucu özefagusu bir doku halkası içinde hapsederek regürgitasyona yol açan vasküler anomali hangisidir?",
        "secenekler": {
            "A": "Persistent Sağ Aortik Ark (PRAA)",
            "B": "Patent Ductus Arteriosus (PDA)",
            "C": "Ventriküler Septal Defekt (VSD)",
            "D": "Fallot Tetralojisi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; PRAA (Persistent Right Aortic Arch) en sık tanılanan vasküler halka anomalisidir (Slayt 102).",
            "celdirici_analizi": "PDA, VSD ve Fallot intrakardiyak damarsal şant anomalileridir, özefagusu sıkıştırmazlar."
        },
        "slayt_no": 102,
        "zorluk_derecesi": "kolay",
        "etiketler": ["PRAA", "vaskuler_halka"]
    },
    {
        "soru_id": "mcq_sind_062",
        "soru_metni": "Persistent Sağ Aortik Ark (PRAA) anomalisi özellikle hangi köpek ırkında çok sık bildirilmektedir?",
        "secenekler": {
            "A": "Alman Çoban Köpeği (Alman Kurdu)",
            "B": "Chihuahua",
            "C": "Pug",
            "D": "Pomeranian"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; PRAA özellikle Alman Kurtlarında belirgin ırk predispozisyonu gösterir (Slayt 102).",
            "celdirici_analizi": "Diğer seçenekler küçük minyatür ırklardır."
        },
        "slayt_no": 102,
        "zorluk_derecesi": "kolay",
        "etiketler": ["alman_kurdu", "PRAA", "irk"]
    },
    {
        "soru_id": "mcq_sind_063",
        "soru_metni": "PRAA olgularında klinik bulgular tipik olarak yavru köpeğin hangi yaşam evresinde belirginleşmeye başlar?",
        "secenekler": {
            "A": "Anne sütü emerken yaşamın ilk 3 gününde",
            "B": "Yavrunun katı gıdayı ilk alımından kısa bir süre sonra (sütten kesilme dönemi)",
            "C": "Sadece 8 yaşından sonra geriyatrik dönemde",
            "D": "İlk kuduz aşısı yapıldıktan hemen sonra"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; sıvı anne sütü dar halkadan geçer ancak katı gıdaya geçildiğinde gıda darlığa takılır ve regürgitasyon başlar (Slayt 104).",
            "celdirici_analizi": "Sıvı beslenme sırasında darlık klinik vermeyebilir."
        },
        "slayt_no": 104,
        "zorluk_derecesi": "orta",
        "etiketler": ["PRAA", "kati_gida", "klinik"]
    },
    {
        "soru_id": "mcq_sind_064",
        "soru_metni": "Özefagusun motilitesinde azalma ile karakterize fokal veya diffüz dilatasyonuna ne ad verilir?",
        "secenekler": {
            "A": "Megaözefagus",
            "B": "Akut özefagitis",
            "C": "Disfaji",
            "D": "Özefagal fistül"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; özefagus motilitesinin çökmesi ve duvarın genişlemesi Megaözefagustur (Slayt 106).",
            "celdirici_analizi": "Özefagitis yangıdır; disfaji yutma güçlüğü semptomudur."
        },
        "slayt_no": 106,
        "zorluk_derecesi": "kolay",
        "etiketler": ["megaozefagus", "tanim"]
    },
    {
        "soru_id": "mcq_sind_065",
        "soru_metni": "Kedilerde edinsel megaözefagus olgularının yaklaşık %25'inden sorumlu tutulan kraniyal mediastinal neoplazi hangisidir?",
        "secenekler": {
            "A": "Timoma (Thymoma)",
            "B": "Tiroid adenomu",
            "C": "Akciğer fibromu",
            "D": "Özefagus papillomu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kedilerde timoma paraneoplastik myasthenia gravis ve megaözefagusun %25'inden sorumludur (Slayt 106).",
            "celdirici_analizi": "Tiroid adenomu hipertiroidi yapar; timoma timus kaynaklı tümördür."
        },
        "slayt_no": 106,
        "zorluk_derecesi": "orta",
        "etiketler": ["kedi", "timoma", "megaozefagus"]
    },
    {
        "soru_id": "mcq_sind_066",
        "soru_metni": "Köpeklerde megaözefagus etiyolojisinde yer alan endokrin hastalıklar hangileridir?",
        "secenekler": {
            "A": "Diabetes insipidus ve hiperaldosteronizm",
            "B": "Hipoadrenokortizm (Addison) ve Hipotiroidizm",
            "C": "Hiperparatiroidizm ve akromegali",
            "D": "Feokromasitoma ve insülinoma"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Addison ve hipotiroidizm kas güçsüzlüğü ve nöropati yaparak sekonder megaözefagusa yol açabilir (Slayt 106, 108).",
            "celdirici_analizi": "Diğer şıklardaki endokrinopatiler megaözefagusla doğrudan ilişkili değildir."
        },
        "slayt_no": 106,
        "zorluk_derecesi": "orta",
        "etiketler": ["addison", "hipotiroidi", "megaozefagus"]
    },
    {
        "soru_id": "mcq_sind_067",
        "soru_metni": "Köpeklerde Spirocerca lupi parazitinin özefagus duvarında granülom oluşturarak tetiklediği primer malign neoplazi hangisidir?",
        "secenekler": {
            "A": "Primer özefagus sarkomları (Fibrosarkom / Osteosarkom)",
            "B": "Benign adenomatöz polip",
            "C": "Mide adenokarsinomu",
            "D": "Pankreatik insülinoma"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; köpeklerde kronik Spirocerca lupi enfeksiyonu granülomatöz lezyonların sarkomatöz malign transformasyonuna yol açar (Slayt 112).",
            "celdirici_analizi": "B benign poliptir; C midedir; D pankreastadır."
        },
        "slayt_no": 112,
        "zorluk_derecesi": "orta",
        "etiketler": ["spirocerca_lupi", "ozefagus_sarkomu"]
    },
    {
        "soru_id": "mcq_sind_068",
        "soru_metni": "Yaşlı köpeklerde özellikle alt özefagus sfinkterinde yerleşen ve düz kas kökenli olan neoplaziler hangileridir?",
        "secenekler": {
            "A": "Leiomyomlar ve leiomyosarkomlar",
            "B": "Skuamöz hücreli karsinomlar",
            "C": "Mast hücre tümörleri",
            "D": "Histiyositomlar"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; alt özefagus sfinkterinde yaşlı köpeklerde leiomyom ve leiomyosarkomlar sıklıkla saptanır (Slayt 112).",
            "celdirici_analizi": "SCC kedilerde sıktır; mast hücresi deridedir."
        },
        "slayt_no": 112,
        "zorluk_derecesi": "orta",
        "etiketler": ["leiomyom", "alt_ozefagus_sfinkteri"]
    },
    {
        "soru_id": "mcq_sind_069",
        "soru_metni": "Kedilerde en sık karşılaşılan primer özefagus neoplazmı hangisidir?",
        "secenekler": {
            "A": "Skuamöz hücreli karsinom",
            "B": "Osteosarkom",
            "C": "Malign melanom",
            "D": "Liposarkom"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; kedilerde özefagusun en yaygın primer neoplazmı Skuamöz Hücreli Karsinomdur (Slayt 112).",
            "celdirici_analizi": "Melanom köpekte sıktır; osteosarkom kemik kaynaklıdır."
        },
        "slayt_no": 112,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kedi", "SCC", "ozefagus_tumoru"]
    },
    {
        "soru_id": "mcq_sind_070",
        "soru_metni": "Akut gastrit sağaltımında hastanın diyet kısıtlaması (oral açlık) en az ne kadar süre uygulanmalıdır?",
        "secenekler": {
            "A": "En az 24 saat",
            "B": "En fazla 2 saat",
            "C": "En az 7 gün",
            "D": "Hiç aç bırakılmaz hemen çiğ et verilir"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; mide mukozasının dinlenmesi ve kusma refleksinin yatışması için en az 24 saat oral gıda verilmemelidir (Slayt 122).",
            "celdirici_analizi": "2 saat yetersizdir; 7 gün açlık kedi ve köpekte hipoglisemi ve hepatik lipidoz riski yaratır."
        },
        "slayt_no": 122,
        "zorluk_derecesi": "kolay",
        "etiketler": ["akut_gastrit", "oral_aclik"]
    },
    {
        "soru_id": "mcq_sind_071",
        "soru_metni": "Akut gastritte 24 saatlik açlık sonrası beslenmeye başlanırken diyette hangisine DİKKAT EDİLMELİDİR?",
        "secenekler": {
            "A": "Yüksek oranda hayvansal yağ ve saf tereyağı verilmelidir",
            "B": "Yüksek protein ve yağ içeren diyetlerden sakınılmalı; sindirimi kolay, başlıca karbonhidrattan oluşan gıdalar verilmelidir",
            "C": "Doğrudan baharatlı ve tuzlu kemik suları içirilmelidir",
            "D": "Sadece kuru ve yüksek lifli granül mamalar tercih edilmelidir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; yağ ve yüksek protein mide boşalmasını geciktirir ve asit salgısını artırır; bu yüzden sindirimi kolay KH ağırlıklı diyet verilir (Slayt 122).",
            "celdirici_analizi": "A ve C şıkları mideyi aşırı irrite eder."
        },
        "slayt_no": 122,
        "zorluk_derecesi": "kolay",
        "etiketler": ["diyet", "gastrit_beslenme"]
    },
    {
        "soru_id": "mcq_sind_072",
        "soru_metni": "10-50 kg arası yetişkin bir köpeğin günlük fizyolojik idame sıvı ihtiyacı ne kadardır?",
        "secenekler": {
            "A": "10 - 20 ml/kg",
            "B": "44 - 66 ml/kg",
            "C": "100 - 150 ml/kg",
            "D": "200 - 250 ml/kg"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 10-50 kg arası köpeklerin günlük sıvı ihtiyacı 44-66 ml/kg'dır (Slayt 123).",
            "celdirici_analizi": "<5 kg küçük köpeklerde bu ihtiyaç 80 ml/kg'a kadar çıkar."
        },
        "slayt_no": 123,
        "zorluk_derecesi": "orta",
        "etiketler": ["sivi_tedavisi", "gunluk_ihtiyac"]
    },
    {
        "soru_id": "mcq_sind_073",
        "soru_metni": "Canlı ağırlığı 5 kg'dan az olan küçük köpeklerde günlük idame sıvı ihtiyacı ne kadardır?",
        "secenekler": {
            "A": "30 ml/kg",
            "B": "80 ml/kg",
            "C": "120 ml/kg",
            "D": "15 ml/kg"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; vücut yüzey alanı kütlesine göre geniş olan <5 kg küçük köpeklerde günlük ihtiyaç 80 ml/kg'dır (Slayt 123).",
            "celdirici_analizi": "Büyük köpeklerde 44-66 ml/kg iken küçüklerde 80 ml/kg'dır."
        },
        "slayt_no": 123,
        "zorluk_derecesi": "orta",
        "etiketler": ["sivi_tedavisi", "pediatrik_doz"]
    },
    {
        "soru_id": "mcq_sind_074",
        "soru_metni": "2 - 100 kg arasındaki pet hayvanları için günlük alınması gereken idame sıvı miktarını hesaplamada kullanılan formül hangisidir?",
        "secenekler": {
            "A": "(30 x Canlı Ağırlık kg) + 70 = mL/gün",
            "B": "(10 x Canlı Ağırlık kg) + 20 = mL/gün",
            "C": "(50 x Canlı Ağırlık kg) - 100 = mL/gün",
            "D": "(Canlı Ağırlık kg / 2) + 500 = mL/gün"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; klinik pratikte pet hayvanları günlük sıvı ihtiyacı (30 x CA kg) + 70 formülüyle hesaplanır (Slayt 123).",
            "celdirici_analizi": "Örneğin 10 kg bir köpekte: (30x10)+70 = 370 mL günlük temel idamedir."
        },
        "slayt_no": 123,
        "zorluk_derecesi": "orta",
        "etiketler": ["sivi_formulu", "hesaplama"]
    },
    {
        "soru_id": "mcq_sind_075",
        "soru_metni": "Rutin akut gastritli ve kusması olan hayvanlarda Na, K, Cl kayıplı metabolik asidoz tablosunda tercih edilen dengeli kristaloid solüsyon hangisidir?",
        "secenekler": {
            "A": "Saf damıtık distile su",
            "B": "Laktatlı Ringer solüsyonu",
            "C": "%20 Mannitol solüsyonu",
            "D": "%3 Hipertonik salin"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; dehidrasyon ve metabolik asidoz tablosunda laktatın karaciğerde bikarbonata dönüşmesi avantajıyla Laktatlı Ringer ilk tercihtir (Slayt 124).",
            "celdirici_analizi": "Saf su hemoliz yapar; mannitol diüretiktir; hipertonik salin sadece şokta verilir."
        },
        "slayt_no": 124,
        "zorluk_derecesi": "kolay",
        "etiketler": ["laktatli_ringer", "asidoz", "kristaloid"]
    },
    {
        "soru_id": "mcq_sind_076",
        "soru_metni": "Sık olmayan ancak yoğun kusması olan ve pilorik akışın durduğu (pilor stenozu/tıkanma) hastalarda hipokloremi, hipokalemi ve metabolik alkalozis varlığında hangi serum uygulanmalıdır?",
        "secenekler": {
            "A": "% 0.9 NaCl (Serum Fizyolojik)",
            "B": "Laktatlı Ringer",
            "C": "% 50 Konsantre Dekstroz",
            "D": "Sodyum Bikarbonat solüsyonu"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; saf HCl kusulmasına bağlı gelişen hipokloremi ve metabolik alkalozda %0.9 NaCl verilir; Cl- klor açığını kapatır ve HCO3-'ın idrarla atılmasını sağlar (Slayt 124).",
            "celdirici_analizi": "Sodyum bikarbonat veya laktatlı ringer verilirse mevcut alkalozis daha da ağırlaşır."
        },
        "slayt_no": 124,
        "zorluk_derecesi": "orta",
        "etiketler": ["serum_fizyolojik", "pilor_tikanmasi", "metabolik_alkaloz"]
    },
    {
        "soru_id": "mcq_sind_077",
        "soru_metni": "Parenteral sıvılara potasyum (KCl) eklenirken, kardiyotoksisiteyi önlemek amacıyla K+ uygulama hızı en fazla ne kadar olmalıdır?",
        "secenekler": {
            "A": "0.5 mEq/kg/saat'i geçmemelidir",
            "B": "5.0 mEq/kg/saat olmalıdır",
            "C": "Hızın hiçbir klinik önemi yoktur",
            "D": "10 mEq/kg bolus verilmelidir"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; potasyumun hızlı infüzyonu kardiyak arrest oluşturur, bu nedenle hız asla 0.5 mEq/kg/saati aşmamalı ve EKG takibi yapılmalıdır (Slayt 125).",
            "celdirici_analizi": "5 veya 10 mEq/kg hızlar anında ölümcül asistoli veya ventriküler fibrilasyon yaratır."
        },
        "slayt_no": 125,
        "zorluk_derecesi": "orta",
        "etiketler": ["potasyum", "maksimum_hiz", "EKG"]
    },
    {
        "soru_id": "mcq_sind_078",
        "soru_metni": "Akut gastrit tedavisinde fenotiyazin türevi bir antiemetik olan 'Klorpromazin'in subkutan/intramüsküler kullanım dozu nedir?",
        "secenekler": {
            "A": "0.5 mg/kg IM veya SC",
            "B": "10 mg/kg oral",
            "C": "25 mg/kg IV",
            "D": "0.001 mg/kg"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Klorpromazin 0.5 mg/kg IM veya SC (IV yolla 0.05 mg/kg) uygulanır (Slayt 126).",
            "celdirici_analizi": "Hipotansif şoktaki hayvanda vazodilatasyon yapabileceği için dikkatli olunmalıdır."
        },
        "slayt_no": 126,
        "zorluk_derecesi": "orta",
        "etiketler": ["klorpromazin", "antiemetik", "doz"]
    },
    {
        "soru_id": "mcq_sind_079",
        "soru_metni": "Akut Hemorojik Diyare Sendromunun (AHDS / HGE) etiyolojik sebebi olarak primer sorumlu tutulan mikroorganizma grubu hangisidir?",
        "secenekler": {
            "A": "Clostridium türü bakteriler",
            "B": "Candida albicans mantarları",
            "C": "Toxoplasma gondii protozoonları",
            "D": "Rabies virüsü"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; AHDS hastalığının primer sebebi olarak Clostridium türü bakteriler ve enterotoksinleri sorumlu tutulmaktadır (Slayt 127).",
            "celdirici_analizi": "B mantardır; C kedi parazitidir; D kuduzdur."
        },
        "slayt_no": 127,
        "zorluk_derecesi": "kolay",
        "etiketler": ["AHDS", "HGE", "clostridium"]
    },
    {
        "soru_id": "mcq_sind_080",
        "soru_metni": "Hemorojik gastroenteritis teriminin son yıllarda 'Akut Hemorojik Diyare Sendromu (AHDS)' olarak değiştirilmesinin histolojik gerekçesi nedir?",
        "secenekler": {
            "A": "Hastalığın mideden ziyade primer hasarının bağırsaklarda olduğunun saptanması",
            "B": "Midede hiçbir asit salgısının bulunmaması",
            "C": "Hastalığın sadece kedilerde görülüyor olması",
            "D": "Karaciğer enzimlerinin tamamen sıfırlanması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; yapılan histolojik incelemeler asıl hasarın mideden ziyade bağırsaklarda olduğunu ortaya koyduğu için hastalık AHDS olarak adlandırılmıştır (Slayt 127).",
            "celdirici_analizi": "Hastalık köpeklerde oluşur ve mukoza hasarı bağırsaktadır."
        },
        "slayt_no": 127,
        "zorluk_derecesi": "orta",
        "etiketler": ["AHDS", "patoloji", "isimlendirme"]
    },
    {
        "soru_id": "mcq_sind_081",
        "soru_metni": "Akut Hemorojik Diyare Sendromu (AHDS) özellikle hangi köpek popülasyonunu daha sık etkiler?",
        "secenekler": {
            "A": "Özellikle küçük ırk köpekleri (Minyatür ırklar)",
            "B": "Dev ırk köpekleri (Danua, Mastif)",
            "C": "Sadece av köpeklerini",
            "D": "Sadece sokak köpeklerini"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; AHDS özellikle küçük ırk köpekleri (Yorkshire, Minyatür Schnauzer/Pinscher vb.) etkiler (Slayt 127).",
            "celdirici_analizi": "GDV dev derin göğüslü ırkları tutarken, AHDS küçük ırkları tutar."
        },
        "slayt_no": 127,
        "zorluk_derecesi": "kolay",
        "etiketler": ["AHDS", "kucuk_irk"]
    },
    {
        "soru_id": "mcq_sind_082",
        "soru_metni": "AHDS'li (Akut Hemorojik Diyare Sendromlu) bir köpekte görülen tipik laboratuvar tablosu hangisidir?",
        "secenekler": {
            "A": "Düşük hematokrit (PCV <%20) ve aşırı hiperproteinemi",
            "B": "Belirgin hemokonsantrasyon (PCV > %55) ve NORMAL plazma protein konsantrasyonu",
            "C": "Aşırı lökositoz ve hipoglisemi",
            "D": "Tamamen normal kan değerleri"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; PCV > %55 iken plazma proteininin normal veya hafif düşük kalması AHDS için adeta patognomoniktir (Slayt 129).",
            "celdirici_analizi": "A şıkkı anemidir; AHDS'de ise masif plazma kaybına bağlı hemokonsantrasyon vardır."
        },
        "slayt_no": 129,
        "zorluk_derecesi": "orta",
        "etiketler": ["AHDS", "PCV", "laboratuvar"]
    },
    {
        "soru_id": "mcq_sind_083",
        "soru_metni": "AHDS sağaltımında şok, DIC ve hipovolemi ilişkili renal hasarı önlemek için en hayati tedavi basamağı hangisidir?",
        "secenekler": {
            "A": "Agresif intravenöz sıvı tedavisi",
            "B": "Sadece laksatif şurup verilmesi",
            "C": "Oral aspirin tedavisi",
            "D": "Radyoterapi uygulanması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; hipoperfüzyon, böbrek yetmezliği ve DIC gelişimini önlemek için acil ve agresif IV sıvı tedavisi hayatidir (Slayt 130).",
            "celdirici_analizi": "Aspirin koagülopatiyi ve kanamayı tetikler."
        },
        "slayt_no": 130,
        "zorluk_derecesi": "kolay",
        "etiketler": ["AHDS", "sivi_tedavisi", "acil"]
    },
    {
        "soru_id": "mcq_sind_084",
        "soru_metni": "Kronik gastrit etiyolojisinde yer alan ve kronik kullanımı doğrudan mide mukozasında hasara yol açan ilaç örneği hangisidir?",
        "secenekler": {
            "A": "Aspirin",
            "B": "B12 vitamini",
            "C": "Sukralfat",
            "D": "Fenbendazol"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; aspirinin kronik kullanımı koruyucu prostaglandinleri inhibe ederek kronik gastrit ve ülsere neden olur (Slayt 131).",
            "celdirici_analizi": "B vitamindir; C koruyucudur; D antiparaziterdir."
        },
        "slayt_no": 131,
        "zorluk_derecesi": "kolay",
        "etiketler": ["aspirin", "kronik_gastrit"]
    },
    {
        "soru_id": "mcq_sind_085",
        "soru_metni": "Kronik gastrit vakalarında kesin tanıya ulaşmak için mutlaka yapılması gereken tanısal yöntem hangisidir?",
        "secenekler": {
            "A": "Gastrik Biyopsi (Endoskopik veya cerrahi)",
            "B": "Düz karın radyografisi",
            "C": "Dışkı flotasyon muayenesi",
            "D": "Deri alerji testi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; mukozadaki inflamasyon tipini (lenfositik, eozinofilik vb.) belirlemek için kesin tanı GASTRİK BİYOPSİ ile konur (Slayt 133).",
            "celdirici_analizi": "Radyografi ve rutin kan tahlilleri kronik gastritte spesifik bulgu vermez."
        },
        "slayt_no": 133,
        "zorluk_derecesi": "orta",
        "etiketler": ["biyopsi", "kronik_gastrit", "kesin_tani"]
    },
    {
        "soru_id": "mcq_sind_086",
        "soru_metni": "Gastrik biyopsi örneğinde yoğun lenfosit ve plazma hücresi infiltrasyonu saptandığında hangi etiyoloji düşünülür ve hangi ilaç endikedir?",
        "secenekler": {
            "A": "İmmun aracılı gastritis söz konusudur; kortikosteroidler endikedir",
            "B": "Mantar enfeksiyonudur; sadece ketokonazol verilir",
            "C": "Yabancı cisim perforasyonudur; hemen acil lavman yapılır",
            "D": "Kalsiyum fazlalığıdır; kalsitonin verilir"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; lenfosit ve plazma hücre infiltrasyonu immün aracılı gastriti gösterir ve kortikosteroid tedavisi endikedir (Slayt 134).",
            "celdirici_analizi": "İmmünsüpresif dozda prednizolon tedavisi uygulanır."
        },
        "slayt_no": 134,
        "zorluk_derecesi": "orta",
        "etiketler": ["biyopsi", "kortikosteroid", "lenfositik_gastrit"]
    },
    {
        "soru_id": "mcq_sind_087",
        "soru_metni": "Köpeklerde gastrik ülser oluşumuna neden olabilen sistemik mastositozis veya gastrinoma vakalarında ülser gelişiminin temel mekanizması nedir?",
        "secenekler": {
            "A": "Gastrik hiperasidite (Aşırı histamin veya gastrin uyarısıyla aşırı HCl salgılanması)",
            "B": "Midede safra asitlerinin tamamen yok olması",
            "C": "Pepsinojen üretiminin sıfıra inmesi",
            "D": "Mide kaslarının hiç kasılamaması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; mast hücre tümörleri histamin salgılayarak, gastrinomalar ise gastrin salgılayarak aşırı gastrik hiperasidite ve derin ülserlere yol açarlar (Slayt 136, 138).",
            "celdirici_analizi": "Gastrinoma şüphesinde kanda serum gastrin konsantrasyonu ölçülmelidir."
        },
        "slayt_no": 136,
        "zorluk_derecesi": "orta",
        "etiketler": ["gastrinoma", "mastositozis", "hiperasidite"]
    },
    {
        "soru_id": "mcq_sind_088",
        "soru_metni": "Gastrik ülser teşhisinde mide mukozasındaki erozyon ve derin defektleri doğrudan gösteren en sensitif ve spesifik tanı aracı hangisidir?",
        "secenekler": {
            "A": "Endoskopi (Gastroskopi)",
            "B": "Düz karın radyografisi",
            "C": "İdrar sediment muayenesi",
            "D": "Tam kan sayımı (CBC)"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; gastrik ülserin teşhisinde en sensitif ve spesifik araç doğrudan mukozanın incelendiği Endoskopidir (Slayt 138).",
            "celdirici_analizi": "Düz grafi ülseri gösteremez; CBC sadece kan kaybına bağlı anemiyi yansıtır."
        },
        "slayt_no": 138,
        "zorluk_derecesi": "kolay",
        "etiketler": ["endoskopi", "gastrik_ulser"]
    },
    {
        "soru_id": "mcq_sind_089",
        "soru_metni": "Gastrik ülserin mide duvarını tam kat delmesi (perforasyon) durumunda şekillenen ve ölümcül olan komplikasyon hangisidir?",
        "secenekler": {
            "A": "Septik peritonitis",
            "B": "Akut pankreatik lipidoz",
            "C": "Hiatal herni",
            "D": "Kronik rinit"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; mide duvarı delindiğinde mide içeriği ve bakteriler karın boşluğuna dökülerek septik peritonitise ve ölüme yol açar (Slayt 137).",
            "celdirici_analizi": "Acil cerrahi laparotomi ve periton lavajı gerektirir."
        },
        "slayt_no": 137,
        "zorluk_derecesi": "kolay",
        "etiketler": ["perforasyon", "septik_peritonit", "ulser"]
    },
    {
        "soru_id": "mcq_sind_090",
        "soru_metni": "Gastrik ülser sağaltımında kullanılan temel medikal ajan kombinasyonu hangisinde doğru özetlenmiştir?",
        "secenekler": {
            "A": "Etiyolojik ajanın uzaklaştırılması + H2 blokörleri / Proton pompa inhibitörleri + Sukralfat",
            "B": "Aspirin + Meloksikam + Dekzametazon",
            "C": "Sadece sodyum klorür ve lavman",
            "D": "Metronidazol ve kemoterapi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; ülser tedavisinde neden olan NSAID kesilir; asit PPI/H2 ile baskılanır ve sukralfat ile krater örtülür (Slayt 139).",
            "celdirici_analizi": "B şıkkındaki NSAID ve steroidler ülseri daha da deler!"
        },
        "slayt_no": 139,
        "zorluk_derecesi": "kolay",
        "etiketler": ["ulser_tedavisi", "PPI", "sukralfat"]
    }
]

print(f"Bölüm 2 hazır: {len(QUESTIONS_PART2)} soru.")
