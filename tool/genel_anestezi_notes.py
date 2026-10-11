# -*- coding: utf-8 -*-
"""
VetMeri - 4. Ders: Genel Anestezi & Anestezi Dönemleri
Kapsam: 22 Slayt (Genel Anestezi, İndüksiyon, İdame, Uyanma, Dönem I-IV, Planlar 1-4, Solunum, Sirkülasyon, Göz ve Diğer Refleksler)
"""

METADATA = {
    "id": "genel_anestezi",
    "name": "4. Ders: Genel Anestezi & Anestezi Dönemleri",
    "shortName": "Genel Anestezi",
    "icon": "💉",
    "badge": "22 Slayt • 4 Dönem, Planlar, İndüksiyon & İntraoperatif Refleksler",
    "kategori": "Veteriner Cerrahi ve Anesteziyoloji",
    "alt_kategori": "Genel Anestezi İlkeleri, Anestezi Evreleri ve Refleks Takibi",
    "ozet": "Bu eğitim modülü; genel anestezi kavramını, enjektabl ve inhalasyon anesteziklerinin karşılaştırmasını, indüksiyon, idame ve uyanma evrelerini, Guedel sınıflamasına göre anestezinin 4 dönemini (I. Analjezi, II. Eksitasyon, III. Cerrahi Anestezi [1, 2, 3 ve 4. Planlar], IV. Bulbar Paralizi/Agoni) ve intraoperatif solunum, sirkülasyon, göz ve koruyucu refleks parametrelerini eksiksiz kapsamaktadır.",
    "kilit_noktalar": [
        "Genel anestezi; ağrı hissinin kalkması, bilinçsizlik, nispeten reflekslerin kalkması ile karakterize kontrollü ve reverzibl şuursuzluk halidir (Slayt 1).",
        "İnhalasyon indüksiyonu intravenöz anesteziye göre çok daha güvenlidir ve tekrarlayan enjeksiyon zorunluluğunu ortadan kaldırır (Slayt 1).",
        "Anestezide ekspiratorik kaslar aktifleşir, inspirasyon sonunda inspiratuvar kas tonusu aniden durur ve ekspirasyon süresi belirgin uzar (Slayt 2).",
        "Atlarda periyodik solunum görülür; hayvan 2, 3 hatta 4 soluk aldıktan sonra uzun süreli bir duraklama (apne) periyoduna girer (Slayt 2).",
        "Premedikasyondan sonra indüksiyon için IM yolla en az 10 dakika, SC yolla en az 20 dakika beklenilmelidir (Slayt 3).",
        "Genel anestezinin fiilen başladığı an yutkunma refleksinin ortadan kalkması ile karakterizedir (Slayt 3).",
        "Kısa süreli barbitüratlarda (tiyopental) hastanın vücudunda ilaç olmasına rağmen anestezik etkinin sonlanması, ilacın vücut yağlarına absorbe olması (redistribüsyon) iledir (Slayt 5).",
        "II. Dönemde (Eksitasyon) bilinçsizlik başlar ancak TÜM REFLEKSLER MEVCUTTUR VE HATTA ARTABİLİR; bu dönem derinlik hızla artırılarak en kısa sürede geçilmelidir (Slayt 8).",
        "III. Dönem 1. Planda yutkunma azaldığı için endotrakeal tüp kolayca takılabilir fakat cerrahi tolere edilemez (Slayt 9).",
        "İdeal cerrahi anestezi seviyesi III. Dönem 2. Plandır; cerrahiye tepki yoktur, göz küresi merkezdedir, pupilla hafif dilatedir (Slayt 10, 13).",
        "III. Dönem 3. Planda refleksler TAMAMEN ORTADAN KALKAR, CRT uzar ve solunum mekanik ventilatör veya rezerv balonla desteklenmelidir (Slayt 11).",
        "III. Dönem 4. Planda pupilla aşırı dilate ve ışık refleksi tamamen kayıptır, lakrimal salgı durduğu için kornea kurur, arrest riski çok yüksektir (Slayt 12).",
        "Anestezik doz aşımında solunum tamamen abdominal (paradoksal) hale gelir; inspirasyonda abdomen şişerken toraks kollabe olur (Slayt 15).",
        "Atlarda genel anestezinin 2. döneminde ve yüzeysel cerrahi anestezide nistagmus görülür; lakrimasyon ise anestezinin yüzeysel olduğunu kanıtlar (Slayt 17, 19).",
        "Atlarda KORNEAL REFLEKS derin anestezi döneminde bile mevcudiyetini korur (Slayt 19).",
        "Kedilerde yutkunma ve laringeal refleks orta düzey anestezi oluşana kadar direnebilir (Slayt 20).",
        "Atlarda anal sfinkterin gevşemesi relaksasyonun iyi bir göstergesidir; derinleştikçe dışkı görünür, derinde mekanik uyarılara yanıtsızlaşır (Slayt 20).",
        "Köpeklerde çene eklemi özellikle barbitürat anestezisinde 2'den 3'e geçerken rahatça açılır; ağzın tamamen açılmasına karşı tepki 3. dönemde kaybolur (Slayt 21).",
        "Kedi, kobay ve tavşanlarda kulağın sıkılmasıyla baş sallama tepkisi (pinna refleksi) cerrahi anestezi oluştuğunda tamamen ortadan kalkar (Slayt 22)."
    ]
}

SUMMARY_SECTIONS = [
    {
        "title": "1. Genel Anestezi Tanımı & İlaç Sınıfları",
        "icon": "💉",
        "points": [
            "Genel Anestezi Tanımı: Ağrı hissinin ortadan kaldırılması (analjezi), bilinçsizlik (hipnoz/narkoz), nispeten refleks cevaplarının ortadan kalkması ile karakterize olan kontrollü ve reverzibl (geri dönüşümlü) şuursuzluk halidir (Slayt 1).",
            "Anestezik İlaç Grupları: Enjektabl anestezikler, inhalasyon anestezikleri ya da bunların dengeli kombinasyonları (balanslı anestezi) kullanılır (Slayt 1).",
            "Enjektabl Ajanlar: Barbitüratlar (Tiyopental), Sikloheksaminler (Ketamin), Propofol (Slayt 1).",
            "İnhalasyon Ajanları: Halotan (Halothane), İzofluran (Isoflurane), Sevofluran (Sevoflurane), Azot protoksit (N2O) (Slayt 1).",
            "İnhalasyonun Üstünlüğü: İntravenöz anestezi ile karşılaştırıldığında inhalasyon yolu ile anestezi indüksiyonu ve idamesi çok daha güvenlidir; derinlik anlık ayarlanabilir ve tekrarlayan enjeksiyon zorunluluğunu ortadan kaldırır (Slayt 1)."
        ]
    },
    {
        "title": "2. Solunum Değişiklikleri & Tür Özellikleri",
        "icon": "🫁",
        "points": [
            "Solunum Farkı: Anestezideki hayvanın solunumu, uyanık hayvana kıyasla tamamen farklı dinamiklere sahiptir (Slayt 2).",
            "Mekanik Değişim: Ekspiratorik kaslar aktif hale gelirken, inspirasyonun sonunda inspiratorik kas tonusu aniden durur ve ekspirasyon süresi oldukça uzar. Bu durum solunum ritminin düzenli sürmesini engeller (Slayt 2).",
            "Atlarda Periyodik Solunum: Atlara özgü karakteristik bir patern olarak, hayvan 2, 3 hatta 4 kez soluduktan sonra bir duraklama dönemi (apne fazı) oluşur ve uzun süre nefes almadığı gözlenir (Slayt 2).",
            "Akciğer Kapasitesi (FRC): Genel anestezinin her türünde akciğerlerin fonksiyonel rezidüel kapasitesi azalır; bu azalmanın şiddeti hayvanın masadaki yatış pozisyonuna (dorsal, lateral, sternal) göre değişkenlik gösterir (Slayt 2)."
        ]
    },
    {
        "title": "3. İndüksiyon, İdame & Uyanma Evreleri",
        "icon": "⏱️",
        "points": [
            "İndüksiyon: Hastada bilincin kaybolup bilinçsizlik halinin başladığı ve anesteziye giriş periyodudur. Genellikle premedikasyon sonrası uygulanır (Slayt 3).",
            "Premedikasyon Bekleme Süresi: Tam etkinin oturması için indüksiyondan önce intramusküler (IM) uygulamalarda en az 10 dakika, subkutan (SC) uygulamalarda en az 20 dakika beklenilmelidir (Slayt 3).",
            "İndüksiyon Eksitasyonu: Başlangıçta hafif motor eksitasyon görülebilir ancak yerini hızla gevşeme ve bilinçsizliğe bırakır. Genel anestezinin fiili başlangıcı yutkunma refleksinin kaybolması ile karakterizedir (Slayt 3).",
            "İdame: İndüksiyonu takiben anestezinin stabil seviyede sürdürüldüğü dönemdir; tüm cerrahi operasyonlar ve manipülasyonlar bu evrede gerçekleştirilir (Slayt 4).",
            "Uyanma Mekanizmaları: Beyindeki anestezik madde konsantrasyonu azaldığında uyanma başlar. Enjektabl ilaçlar karaciğer enzimleri ile metabolize olup böbrek/üriner yolla atılır. Kısa süreli barbitüratlar (tiyopental) vücut yağlarına absorbe olarak (redistribüsyon) beyinden çekilir ve etkisi biter. İnhalasyon ajanları ise beyinden kana, kandan alveollere geçerek solunumla atılır (Slayt 5)."
        ]
    },
    {
        "title": "4. Anestezi Dönemleri: I. ve II. Dönem (Eksitasyon)",
        "icon": "⚡",
        "points": [
            "I. Dönem (Analjezi/İstemli Hareket): Enjektabl veya gaz uygulamasıyla başlar. Hayvanın bilinci yerindedir ancak davranışlarda uyumsuzluk (ataksi) görülür. Ağrı hissi azalır, solunum, kalp fonksiyonları ve tüm refleksler tamamen normaldir (Slayt 7).",
            "II. Dönem (Eksitasyon/Deliryum): Bilinç kaybı başlar. Tüm refleksler MEVCUTTUR ve hatta abartılı şekilde ARTABİLİR. Çiğneme ve yutkunma hareketleri sürer (Slayt 8).",
            "II. Dönem Semptomları: Pupilla dilatedir ancak ışığa daralır. Ekstremitelerde çırpınma, bağırma ve kaçma çabası gözlenir. Solunum düzensizdir ve hayvan nefesini tutabilir (apne) (Slayt 8).",
            "Kritik Klinik İlke: II. Dönem hasta ve hekim güvenliği açısından tehlikeli olduğundan anestezinin derinliği hızla artırılarak en kısa sürede 3. döneme geçilmelidir. Dönem sonunda kas gevşemesi, solunum ve reflekslerde azalma başlar (Slayt 8)."
        ]
    },
    {
        "title": "5. III. Dönem (Cerrahi Anestezi) - Plan 1 & Plan 2",
        "icon": "🎯",
        "points": [
            "III. Dönem Genel: Cerrahi anestezi dönemidir. Anestezi derinliği 1. plandan 4. plana doğru artar (Slayt 9).",
            "1. Plan (Yüzeysel Cerrahi): Solunum düzenli hale gelir, istem dışı ekstremite hareketleri azalır. Göz küresi ventrale ve iç açıya kayar. Pupilla kısmen küçülür, ışık yanıtı azalır. Yutkunma refleksi oldukça azaldığı için endotrakeal tüp kolaylıkla takılabilir (entübasyon). Ancak palpebral refleks hala mevcuttur ve cerrahi işlemler tolere edilemez (ağrı ve kımıldanma olur) (Slayt 9).",
            "2. Plan (Orta Cerrahi - İDEAL DÖNEM): Hastada cerrahi işlemlere karşı hiçbir motor tepki oluşmaz; hasta bilinçsiz ve hareketsizdir. Cerrahi uyarılar nabız ve solunumu hafif artırabilir (Slayt 10).",
            "Plan 2 Göz ve Refleks Tablosu: Göz küresi MERKEZDEDİR (santral). Pupilla hafifçe dilate, ışık yanıtı azalmıştır. Solunum düzenli ve yüzeyseldir. Kalp hızı ve kan basıncı hafif azalmıştır. İskelet kasları relaksedir. Pedal ve palpebral refleksler azalmış ya da tamamen kaybolmuştur (Slayt 10)."
        ]
    },
    {
        "title": "6. III. Dönem Plan 3, Plan 4 & IV. Dönem (Toksik)",
        "icon": "⚠️",
        "points": [
            "3. Plan (Derin Cerrahi): Cerrahi işlemler için oldukça derin bir seviyedir. Solunum ve dolaşımda belirgin depresyon gelişir. Solunum sayısı belirgin düşer; hastayı mekanik ventilatör veya rezerv balonla solutmak şarttır. CRT uzar. Pupilla orta derecede dilatedir. Tüm refleksler TAMAMEN ORTADAN KALKMIŞTIR (Slayt 11).",
            "4. Plan (Aşırı Derin Anestezi / Doz Aşımı): Solunum bozulmuş ve düzensizdir. Pupilla aşırı dilate (paralitik midriyazis) ve ışık refleksi tamamen kayıptır. Lakrimal sekresyon durduğundan kornea kurur. Kas tonusu sıfırlanır, mukozalar solgun, CRT uzamıştır. Kardiyak ve respiratuvar arrest tehlikesi kapıdadır (Slayt 12).",
            "IV. Dönem (Bulbar Paralizi / Agoni): Solunum tamamen durur (apne), ardından dolaşım sistemi çöker ve dakikalar içinde ölüm gerçekleşir. Acil resüsitasyon (KPR) şarttır (Slayt 13).",
            "Klinik Hedef: İdeal anestezi dönemi cerrahinin hissedilmediği III. Dönem 2. Plandır; kardiyovasküler ve solunum depresyonundan kaçınmak için anestezinin derinleşmesine asla izin verilmemelidir (Slayt 13)."
        ]
    },
    {
        "title": "7. İntraoperatif Solunum & Sirkülasyon Bulguları",
        "icon": "📈",
        "points": [
            "Dönemlere Göre Solunum: Sedasyonsuz 1. dönemde hayvan bilinçli nefes tutabilir. 2. dönemde depresyonla solunum düzensizleşir. 3. dönemde solunum yeniden düzenli hale gelir. Barbitürat indüksiyonunda 3. dönemin hemen başında solunum depresyonu tipiktir (Slayt 14).",
            "Paradoksal Abdominal Solunum (Doz Aşımı): Anestezik doz aşımında solunum tamamen abdominal hale gelir. İnspirasyonda diyafram kasılması abdomeni aşırı şişirirken toraks kollabe olur (içe çöker). Ekspirasyonda ise tam tersine diyafram kranial yer değiştirerek toraksı genişletir. Doz aşımı sürerse solunum durur (Slayt 15).",
            "Sirkülasyon Takibi: 1. ve 2. dönemde nabız kuvvetli hissedilir ve genelde taşikardiktir; 2. dönemde aritmi gelişebilir. 3. dönemde pulzasyon düzenli hale gelir ve hafif hızlı seyreder (Slayt 16)."
        ]
    },
    {
        "title": "8. İntraoperatif Göz & Koruyucu Refleksler",
        "icon": "👁️",
        "points": [
            "At Anestezisinde Nistagmus: Atlarda genel anestezinin 2. döneminde ve yüzeysel cerrahi anestezide nistagmus (göz titremesi) görülür. Ayrıca lakrimasyon (gözyaşı) atlarda anestezinin yüzeysel olduğunu gösterir (Slayt 17, 19).",
            "Kedi ve Köpekte Göz Pozisyonu: Yüzeysel ve orta cerrahi anestezide göz küresi aşağıya (ventrale) doğru kayar ve 3. göz kapağı korneanın medialini örter. Anestezi derinleştikçe göz tekrar merkeze (santral) gelir (Slayt 17).",
            "Palpebral vs Korneal Refleks: Göz kapaklarının medial açısına dokunarak palpebral refleks; korneanın medialine dokunarak korneal refleks ölçülür. Korneal refleks palpebralden kısa süre sonra kaybolur. ÖNEMLİ KURAL: Atlarda korneal refleks derin anestezide bile MEVCUTTUR (Slayt 19).",
            "Yutkunma & Kusma: 3. dönemde ortadan kalkar (Kedilerde yutkunma ve laringeal refleks orta düzeye kadar sürebilir) (Slayt 20).",
            "At Anal Sfinkteri: 2. dönemde sfinkter sıkıdır. Anestezi derinleştikçe sfinkter gevşer, rektumda dışkı görünür; derin anestezide mekanik uyarıya yanıtsızlaşır (mükemmel relaksasyon kriteri) (Slayt 20).",
            "Çene Tonusu & Pedal/Pinna Refleksleri: Köpekte ağzın pasif açılabilmesi derinlik kriteridir; barbitüratta 2'den 3'e geçerken çene rahatça açılır, 3. dönemde tepki kaybolur (Slayt 21). Pedal refleks (parmaklar arası ağrı) orta anesteziye geçişte kaybolur. Kedi/kobay/tavşanda kulak sıkma refleksi cerrahi anestezide tamamen kaybolur (Slayt 22)."
        ]
    }
]

BILGI_KARTLARI = [
    {
        "kart_id": "gkart_001",
        "on_yuz": "Genel anestezinin temel klinik tanımı hangi unsurları içerir?",
        "arka_yuz": "Ağrı hissinin ortadan kaldırılması (analjezi), bilinçsizlik, nispeten refleks cevaplarının ortadan kalkması ile karakterize olan kontrollü ve reverzibl (geri dönüşümlü) şuursuzluk halidir (Slayt 1)."
    },
    {
        "kart_id": "gkart_002",
        "on_yuz": "Genel anestezide kullanılan enjektabl ve inhalasyon anestezikleri nelerdir?",
        "arka_yuz": "Enjektabl: Barbitüratlar (tiyopental), sikloheksaminler (ketamin), propofol. İnhalasyon: Halotan, izofluran, sevofluran ve N2O (azot protoksit) (Slayt 1)."
    },
    {
        "kart_id": "gkart_003",
        "on_yuz": "İnhalasyon indüksiyonunun intravenöz anesteziye göre temel üstünlüğü nedir?",
        "arka_yuz": "İnhalasyon yolu ile anestezi indüksiyonu ve yönetimi çok daha güvenlidir, derinlik hızla kontrol edilir ve hastaya tekrarlayan enjeksiyonlar yapma zorunluluğunu ortadan kaldırır (Slayt 1)."
    },
    {
        "kart_id": "gkart_004",
        "on_yuz": "Genel anestezi altındaki bir hayvanın solunum mekaniğinde ne tür değişiklikler meydana gelir?",
        "arka_yuz": "Ekspiratorik kaslar aktifleşir, inspirasyon sonunda inspiratuvar kas tonusu aniden durur, ekspirasyon süresi oldukça uzar ve solunumun düzenli sürmesi engellenir (Slayt 2)."
    },
    {
        "kart_id": "gkart_005",
        "on_yuz": "Atlarda anestezi sırasında görülen 'periyodik solunum' paterni nasıldır?",
        "arka_yuz": "At solunumu 2, 3 hatta 4 kez aldıktan sonra belirgin bir duraklama dönemi (apne) oluşur ve hayvanın uzun süre nefes almadığı gözlenir (Slayt 2)."
    },
    {
        "kart_id": "gkart_006",
        "on_yuz": "Anestezide akciğer fonksiyonel rezidüel kapasitesindeki azalma neye göre değişkenlik gösterir?",
        "arka_yuz": "Genel anestezinin her türünde fonksiyonel kapasite azalır ve bu azalma oranı hastanın operasyon masasındaki yatış pozisyonuna göre değişir (Slayt 2)."
    },
    {
        "kart_id": "gkart_007",
        "on_yuz": "İndüksiyon nedir ve premedikasyondan sonra ne kadar süre beklenmelidir?",
        "arka_yuz": "Bilincin kaybolup hastanın anesteziye girdiği dönemdir. Premedikasyonun tam etkisi için IM enjeksiyon sonrası en az 10 dakika, SC enjeksiyon sonrası en az 20 dakika beklenmelidir (Slayt 3)."
    },
    {
        "kart_id": "gkart_008",
        "on_yuz": "Genel anestezinin fiilen başladığını gösteren en belirgin refleks bulgusu nedir?",
        "arka_yuz": "Yutkunma refleksinin ortadan kalkması genel anestezinin başladığını karakterize eder (Slayt 3)."
    },
    {
        "kart_id": "gkart_009",
        "on_yuz": "Anestezinin idame döneminde şekillenen fizyolojik durumlar nelerdir?",
        "arka_yuz": "Stabil anestezi derinliği, analjezi, iskelet kaslarında gevşeme, istemli hareketlerin yokluğu, refleks kaybı, orta derecede solunum ve KVS depresyonu (Slayt 4)."
    },
    {
        "kart_id": "gkart_0010",
        "on_yuz": "Tiyopental gibi kısa süreli barbitüratlarda etkinin hızla sonlanmasının mekanizması nedir?",
        "arka_yuz": "Beyindeki ilaç miktarı azalırken, ilaç vücut yağ dokuları tarafından absorbe edilir (redistribüsyon). Vücutta ilaç bulunmasına rağmen beyin konsantrasyonu düştüğü için anestezi biter (Slayt 5)."
    },
    {
        "kart_id": "gkart_0011",
        "on_yuz": "İnhalasyon anesteziklerinin vücudu terk etme ve uyanma mekanizması nasıldır?",
        "arka_yuz": "Solunum yoluyla terk eder; anestezik moleküller beyinden kana, kandan da alveollere geçerek ekspirasyon havasıyla vücuttan atılır (Slayt 5)."
    },
    {
        "kart_id": "gkart_0012",
        "on_yuz": "Anestezinin I. Dönemindeki temel klinik ve refleks bulguları nelerdir?",
        "arka_yuz": "Bilinç yerindedir ancak davranışlarda uyumsuzluk (ataksi) başlar. Ağrıya hassasiyet azalır. Solunum, kalp fonksiyonları normaldir ve tüm refleksler mevcuttur (Slayt 7)."
    },
    {
        "kart_id": "gkart_0013",
        "on_yuz": "Anestezinin II. Döneminde (Eksitasyon) refleksler ve pupilla nasıldır?",
        "arka_yuz": "Bilinçsizlik başlar; TÜM REFLEKSLER MEVCUTTUR ve hatta artabilir, çiğneme/yutkunma vardır. Pupilla dilatedir ancak ışığa daralma yanıtı verir (Slayt 8)."
    },
    {
        "kart_id": "gkart_0014",
        "on_yuz": "II. Dönemde hastada görülen motor belirtiler nelerdir ve klinik yaklaşım ne olmalıdır?",
        "arka_yuz": "Ekstremitelerde hareketler, bağırma, çabalama ve düzensiz solunum/nefes tutma görülür. Anestezi derinliği mümkün olduğunca hızlı artırılarak 3. döneme hızla geçilmelidir (Slayt 8)."
    },
    {
        "kart_id": "gkart_0015",
        "on_yuz": "III. Dönem 1. Planda endotrakeal entübasyon neden yapılabilir ancak ameliyat neden yapılamaz?",
        "arka_yuz": "Yutkunma refleksi oldukça azaldığı için endotrakeal tüp kolayca takılabilir. Ancak palpebral refleks mevcuttur, bilinçsizlik başlasa da cerrahi tolere edilemez, ağrı duyulur ve kımıldanma olur (Slayt 9)."
    },
    {
        "kart_id": "gkart_0016",
        "on_yuz": "III. Dönem 1. Planda göz küresi pozisyonu nasıldır?",
        "arka_yuz": "Göz küresi ventrale (aşağıya) ve gözün iç açısına (mediale) doğru kayar (Slayt 9)."
    },
    {
        "kart_id": "gkart_0017",
        "on_yuz": "Cerrahi operasyonlar için ideal kabul edilen III. Dönem 2. Planın göz ve refleks tablosu nasıldır?",
        "arka_yuz": "Göz küresi merkezdedir. Pupilla hafifçe dilate ve ışık yanıtı azalmıştır. Pedal ve palpebral refleksler azalmış ya da kaybolmuştur. İskelet kasları relaksedir (Slayt 10)."
    },
    {
        "kart_id": "gkart_0018",
        "on_yuz": "III. Dönem 3. Planda solunum yönetimi ve refleks durumu nasıldır?",
        "arka_yuz": "Solunum sayısı belirgin düşer, rezerv balon veya mekanik ventilatör desteği zorunludur. CRT uzar. Refleksler tamamen ortadan kalkmıştır, ileri derecede kas gevşemesi vardır (Slayt 11)."
    },
    {
        "kart_id": "gkart_0019",
        "on_yuz": "III. Dönem 4. Planda (aşırı derin anestezi) pupilla ve kornea nasıldır?",
        "arka_yuz": "Pupilla iyice dilatedir ve ışığa karşı refleksi hiç kalmamıştır (fiks midriyazis). Lakrimal sekresyon azlığından dolayı kornea kuru hale gelmiştir (Slayt 12)."
    },
    {
        "kart_id": "gkart_0020",
        "on_yuz": "IV. Dönemde ne meydana gelir ve acil müdahale nedir?",
        "arka_yuz": "Solunum durur (apne), takiben sirkülasyon çöker ve ölüm şekillenir. Hastayı kurtarmak için acilen kardiyopulmoner resüsitasyon (KPR) uygulanmalıdır (Slayt 13)."
    },
    {
        "kart_id": "gkart_0021",
        "on_yuz": "Anestezide barbitürat indüksiyonu yapıldığında 3. dönemin başında ne gözlenir?",
        "arka_yuz": "Premedikasyonda veya indüksiyonda barbitürat kullanılmışsa, 3. dönemin başında belirgin solunum depresyonu görülür (Slayt 14)."
    },
    {
        "kart_id": "gkart_0022",
        "on_yuz": "Anestezik doz aşımında gelişen paradoksal solunumun mekanizması nedir?",
        "arka_yuz": "Solunum tamamen abdominal hale gelir. İnspirasyonda diyafram kasılmasıyla abdomen şişerken toraks kollabe olur; ekspirasyonda diyafram öne kayıp toraks genişler (Slayt 15)."
    },
    {
        "kart_id": "gkart_0023",
        "on_yuz": "Anestezi dönemlerinde sirkülasyon ve nabız nasıl seyreder, aritmi hangi dönemde görülür?",
        "arka_yuz": "1. ve 2. dönemde nabız kuvvetli ve hızlıdır; aritmi 2. dönemde görülebilir. 3. dönemde ise pulzasyon düzenli ve hafif derecede hızlıdır (Slayt 16)."
    },
    {
        "kart_id": "gkart_0024",
        "on_yuz": "Atlarda anestezi takibinde nistagmus ve lakrimasyon ne anlama gelir?",
        "arka_yuz": "Atlarda 2. dönemde ve yüzeysel cerrahi anestezide nistagmus görülür. Lakrimasyon (gözyaşı akışı) ise anestezinin yüzeysel olduğunu kanıtlar; derin anestezide lakrimasyon olmaz (Slayt 17, 19)."
    },
    {
        "kart_id": "gkart_0025",
        "on_yuz": "Köpek ve kedilerde cerrahi anestezi ilerledikçe göz küresi ve 3. göz kapağı nasıldır?",
        "arka_yuz": "Yüzeysel/orta cerrahi anestezide göz küresi aşağı doğru kayar, kapaklar kapalıdır ve 3. göz kapağı korneanın medialini örter (Slayt 17)."
    },
    {
        "kart_id": "gkart_0026",
        "on_yuz": "Atlarda korneal refleksin diğer türlerden en kritik farkı nedir?",
        "arka_yuz": "Diğer türlerde orta/derin anestezide kaybolurken, ATLARDA korneal refleks derin anestezi döneminde bile hala mevcuttur (Slayt 19)."
    },
    {
        "kart_id": "gkart_0027",
        "on_yuz": "Kedilerde yutkunma ve laringeal refleks hangi aşamaya kadar direnebilir?",
        "arka_yuz": "Genel kural olarak yutkunma 3. dönemde kalksa da kedilerde yutkunma ve laringeal refleks orta düzey anestezi oluşana kadar sürebilir (Slayt 20)."
    },
    {
        "kart_id": "gkart_0028",
        "on_yuz": "Atlarda anal sfinkter tonusu anestezi derinliği hakkında nasıl bilgi verir?",
        "arka_yuz": "2. dönemde sfinkter sıkıdır. Anestezi derinleştikçe gevşer ve dışkı görünür hale gelir. Derin anestezide mekanik uyarılara tamamen yanıtsız kalır; mükemmel bir kas gevşemesi göstergesidir (Slayt 20)."
    },
    {
        "kart_id": "gkart_0029",
        "on_yuz": "Köpeklerde çene eklemi tonusu ve ağız açılması anestezi takibinde nasıl yorumlanır?",
        "arka_yuz": "2. dönemden 3. döneme geçerken çene eklemi özellikle barbitürat anestezisinde rahatlıkla açılır. Ağzın tamamen açılmasına karşı direnç tepkisi 3. dönemde kaybolur (Slayt 21)."
    },
    {
        "kart_id": "gkart_0030",
        "on_yuz": "Pedal refleks ve kulak refleksi (pinna) anestezi derinliğinde nasıl değerlendirilir?",
        "arka_yuz": "Pedal refleks (ekstremite fleksiyonu/parmak arası ağrı) yüzeyselden orta anesteziye geçişte kaybolur. Kedi, kobay ve tavşanda kulağın sıkılmasıyla baş sallama tepkisi cerrahi anestezide tamamen kaybolur (Slayt 22)."
    }
]

ACIK_UCLU_SORULAR = [
    {
        "soru_id": "au_gan_001",
        "soru": "Genel anestezi kavramını oluşturan 4 temel unsuru tanımlayarak, intravenöz anesteziye kıyasla inhalasyon indüksiyonunun klinik avantajlarını açıklayınız.",
        "ideal_cevap": "Genel anestezi; 1) Ağrı hissinin kalkması (analjezi), 2) Bilinçsizlik/hipnoz, 3) Refleks cevaplarının nispeten kalkması ve 4) Kontrollü, reverzibl (geri dönüşümlü) bir şuursuzluk hali olarak tanımlanır. İnhalasyon yolu ile indüksiyon, intravenöz enjeksiyonlara göre çok daha güvenlidir; anestezik derinlik gaz konsantrasyonuyla anlık olarak ayarlanabilir, eliminasyonu solunumla hızlıdır ve hastaya tekrarlayan enjeksiyonlar yapma zorunluluğunu ve birikici toksisite riskini ortadan kaldırır.",
        "degerlendirme_kriteri": "Cevapta [analjezi, bilinçsizlik, reflekslerin kalkması, reverzibl şuursuzluk, inhalasyonun güvenliği, tekrarlayan enjeksiyon zorunluluğunun kalkması] unsurları yer almalıdır.",
        "slayt_no": 1
    },
    {
        "soru_id": "au_gan_002",
        "soru": "Anestezi altındaki bir hastanın solunum mekaniğinde meydana gelen değişimleri ve atlarda görülen periyodik solunum paternini izah ediniz.",
        "ideal_cevap": "Anestezide uyanık hayvandan farklı olarak ekspiratorik kaslar aktif hale gelir. İnspirasyonun sonunda inspiratorik kasların tonusu aniden durur ve ekspirasyon süresi oldukça uzar; bu da solunumun düzenli sürmesini engeller. Ayrıca fonksiyonel rezidüel kapasite (FRC) yatış pozisyonuna bağlı olarak azalır. Atlarda ise karakteristik periyodik solunum oluşur: Hayvan 2, 3 hatta 4 soluk peş peşe aldıktan sonra uzun bir duraklama (apne) periyoduna girer ve uzun süre nefes almaz.",
        "degerlendirme_kriteri": "Cevapta [ekspiratorik kas aktivitesi, inspiratuvar tonus ani durması, ekspirasyon süresinin uzaması, FRC azalması, atlarda 2-4 soluk sonrası duraklama/apne] kavramları bulunmalıdır.",
        "slayt_no": 2
    },
    {
        "soru_id": "au_gan_003",
        "soru": "İndüksiyon öncesinde premedikasyon uygulamasının tam etkisinin oluşması için IM ve SC yollarda beklenmesi gereken asgari süreleri ve genel anestezinin fiili başlama kriterini yazınız.",
        "ideal_cevap": "Premedikasyon uygulamasından sonra tam etkinin oluşması için indüksiyon öncesinde: İntramusküler (IM) uygulamalardan sonra en az 10 dakika, subkutan (SC) uygulamalardan sonra ise en az 20 dakika beklenilmelidir. Genel anestezinin fiilen başlaması ise koruyucu reflekslerden yutkunma refleksinin ortadan kalkması ile karakterizedir.",
        "degerlendirme_kriteri": "Cevapta [IM en az 10 dk, SC en az 20 dk, yutkunma refleksinin kaybolması] eksiksiz yer almalıdır.",
        "slayt_no": 3
    },
    {
        "soru_id": "au_gan_004",
        "soru": "Tiyopental gibi kısa süreli barbitürat anestezisinde uyanmanın neden karaciğer metabolizmasından önce redistribüsyonla gerçekleştiğini açıklayınız.",
        "ideal_cevap": "Kısa süreli barbitüratlar (tiyopental) yüksek lipofilik özelliğe sahiptir. İntravenöz enjeksiyonu takiben hızla iyi perfüze olan beyne geçer ve anestezi oluşturur. Ancak çok kısa süre içinde beyindeki ilaç konsantrasyonu düşerken, ilaç damarlanması daha zayıf fakat kapasitesi yüksek vücut yağ dokuları tarafından absorbe edilir (redistribüsyon). Böylece hastanın vücudunda henüz metabolize edilmemiş anestezik madde bulunmasına rağmen, beyindeki konsantrasyon eşiğin altına indiği için anestezi etkisi hızla sonlanır ve uyanma başlar.",
        "degerlendirme_kriteri": "Cevapta [lipofilik yapı, beyinden çekilme, vücut yağlarına absorpsiyon/redistribüsyon, vücutta ilaç olmasına rağmen beyin konsantrasyonunun düşmesi] yer almalıdır.",
        "slayt_no": 5
    },
    {
        "soru_id": "au_gan_005",
        "soru": "Anestezinin II. Döneminin (Eksitasyon) klinik belirtilerini, refleks tablosunu ve bu dönemin hızla geçilmesi kuralının hayati gerekçesini açıklayınız.",
        "ideal_cevap": "II. Dönemde bilinç kaybı başlar ancak tüm refleksler mevcuttur ve hatta hiperrefleksi şeklinde artabilir; çiğneme ve yutkunma sürer. Pupilla dilatedir fakat ışık refleksi mevcuttur. Ekstremitelerde istemsiz hareketler, çırpınma, bağırma ve kaçma çabası görülür; solunum düzensizleşir ve apne nöbetleri oluşabilir. Bu dönem taşiaritmi, travma, laringospazm ve sempatik deşarj riski taşıdığı için anestezinin derinliği mümkün olan en kısa sürede artırılarak hızla 3. döneme geçilmelidir.",
        "degerlendirme_kriteri": "Cevapta [bilinçsizlik, reflekslerin artması, çiğneme/yutkunma, pupilla dilatasyonu/ışık yanıtı, bağırma/hareket, düzensiz solunum, derinliğin hızla artırılması zorunluluğu] bulunmalıdır.",
        "slayt_no": 8
    },
    {
        "soru_id": "au_gan_006",
        "soru": "III. Dönem 1. Planda endotrakeal entübasyonun mümkün olmasına karşılık cerrahi müdahalenin neden tolere edilemediğini fizyolojik bulgularla açıklayınız.",
        "ideal_cevap": "III. Dönem 1. Planda yutkunma refleksi oldukça azaldığı için laringeal direnç kırılır ve endotrakeal tüp farenks/trakeaya kolaylıkla uygulanabilir. Ancak palpebral refleks hala mevcuttur, duyusal korteks ve nosiseptif yollar tam suprese olmamıştır. Bu dönemde operasyona başlanırsa hasta ağrılı cerrahi uyaranı hisseder; istemli/istemsiz kımıldanmalar, solunum ve kalp hızında sıçramalar meydana gelir, bu nedenle cerrahi tolere edilemez.",
        "degerlendirme_kriteri": "Cevapta [yutkunma refleksinin azalması, endotrakeal tüp takılabilmesi, palpebral refleksin sürmesi, ağrı duyulması, kımıldanma ve cerrahinin tolere edilememesi] yer almalıdır.",
        "slayt_no": 9
    },
    {
        "soru_id": "au_gan_007",
        "soru": "Cerrahi operasyonların gerçekleştirildiği ideal evre olan III. Dönem 2. Planın solunum, kardiyovasküler, göz ve refleks parametrelerini yazınız.",
        "ideal_cevap": "1) Solunum: Düzenli ve yüzeyseldir. 2) Kardiyovasküler: Kalp frekansı ve kan basıncı hafif derecede azalmıştır. 3) Göz: Göz küresi merkezdedir (santral), pupilla hafifçe dilatedir, ışığa cevabı azalmıştır. 4) Refleksler ve Kas: İskelet kas tonusu azalmış ve relaksasyon oluşmuştur; pedal ve palpebral refleksler azalmış ya da tamamen kaybolmuştur. Hasta bilinçsiz ve hareketsizdir, cerrahiye motor tepki vermez.",
        "degerlendirme_kriteri": "Cevapta [düzenli/yüzeysel solunum, hafif nabız/basınç düşüşü, göz küresi merkezde, hafif dilate pupilla, pedal ve palpebral refleks kaybı, kas gevşemesi] bulunmalıdır.",
        "slayt_no": 10
    },
    {
        "soru_id": "au_gan_008",
        "soru": "III. Dönem 3. Planda ortaya çıkan kardiyorespiratuvar depresyonu ve uygulanması zorunlu solunum destek yöntemini açıklayınız.",
        "ideal_cevap": "III. Dönem 3. Plan birçok cerrahi için oldukça derin bir anestezidir. Solunum sayısı belirgin şekilde azalır, tidal hacim düşer; bu nedenle hastayı mutlaka rezerv balon ile manuel olarak veya mekanik ventilatörle ventile ederek desteklemek şarttır. Sirkülasyonda ciddi depresyon oluşur, kapiller dolma süresi (CRT) uzar. Pupillanın ışığa yanıtı yok denecek kadar azalır, tüm refleksler tamamen ortadan kalkar ve ileri derecede kas atonisi şekillenir.",
        "degerlendirme_kriteri": "Cevapta [oldukça derin anestezi, solunum sayısı düşüşü, rezerv balon/ventilatör desteği zorunluluğu, CRT uzaması, tüm reflekslerin tamamen kalkması] yer almalıdır.",
        "slayt_no": 11
    },
    {
        "soru_id": "au_gan_009",
        "soru": "III. Dönem 4. Plan (Aşırı Derin / Doz Aşımı) ile IV. Dönem (Bulbar Paralizi) arasındaki klinik farkları ve ölümcül riskleri açıklayınız.",
        "ideal_cevap": "III. Dönem 4. Planda solunum ileri derecede düzensiz ve yetersizdir, pupilla paralitik dilate olup ışık refleksi sıfırdır, lakrimal salgı durduğundan kornea kurur, kas tonusu tamamen yok olmuş ve mukozalar solgundur; kardiyak/solunum arresti an meselesidir. IV. Dönemde ise solunum tamamen durmuş (apne), dolaşım çökmüş ve klinik ölüm şekillenmiştir; acil KPR yapılmazsa beyin ölümü gerçekleşir. İdeal anestezi seviyesi ise hastanın ağrı duymadığı III. Dönem 2. Plandır.",
        "degerlendirme_kriteri": "Cevapta [Plan 4'te düzensiz solunum, fiks dilate pupilla, kornea kuruluğu; Dönem IV'te solunumun tamamen durması, dolaşım çöküşü, ölüm, acil resüsitasyon] bulunmalıdır.",
        "slayt_no": 12
    },
    {
        "soru_id": "au_gan_010",
        "soru": "Anestezik doz aşımında şekillenen paradoksal torakoabdominal solunum mekanizmasını ve diyafram hareketlerini detaylandırınız.",
        "ideal_cevap": "Doz aşımında interkostal kaslar felç olduğundan solunum tamamen abdominal karaktere bürünür. Diyaframatik kontraksiyonlar sırasında inspirasyonda abdomen aşırı şişkin hale gelirken negatif intratorasik basınç dengesizliğiyle toraks kollabe olur (içe çöker). Ekspirasyonda ise tam tersine diyaframın anteriore doğru yer değiştirmesiyle toraks genişler. Doz aşımı sürdükçe diyafram hareketleri zayıflar, hasta soluk veremez ve solunum arresti gelişir.",
        "degerlendirme_kriteri": "Cevapta [tamamen abdominal solunum, inspirasyonda abdomen şişmesi/toraks kollapsı, ekspirasyonda diyafram kranial hareketi ve toraks genişlemesi, diyafram zayıflaması ve arrest] yer almalıdır.",
        "slayt_no": 15
    },
    {
        "soru_id": "au_gan_011",
        "soru": "Genel anestezi dönemlerine göre nabız ve kardiyak ritim değişikliklerini (aritmi zamanlaması dahil) özetleyiniz.",
        "ideal_cevap": "Anestezinin 1. ve 2. dönemlerinde sempatik tonus ve eksitasyon etkisiyle pulzasyon kuvvetli hissedilir ve genel olarak taşikardiktir (hızlıdır). Aritmiler en sık 2. dönemde (eksitasyon fazında) ortaya çıkar. 3. döneme (cerrahi evre) geçildiğinde ise pulzasyon düzenli bir ritme kavuşur ve fizyolojik sınırlarda hafif derecede hızlı seyreder.",
        "degerlendirme_kriteri": "Cevapta [1 ve 2. dönemde kuvvetli ve hızlı nabız, 2. dönemde aritmi riski, 3. dönemde düzenli ve hafif hızlı nabız] belirtilmelidir.",
        "slayt_no": 16
    },
    {
        "soru_id": "au_gan_012",
        "soru": "At anestezisinde nistagmus ve lakrimasyonun klinik anlamı nedir? Bu bulgular anestezi derinliği hakkında hekime ne söyler?",
        "ideal_cevap": "Atlarda göz hareketleri hayati öneme sahiptir. Atlarda genel anestezinin 2. döneminde ve yüzeysel cerrahi anestezi döneminde belirgin 'nistagmus' (göz küresi titremesi) görülür; bu durum anestezinin henüz yeterince derinleşmediğini gösterir. Ayrıca atlarda lakrimasyon (gözyaşı akması) anestezinin yüzeysel olduğunun açık kanıtıdır; zira derin anestezi dönemlerinde lakrimal sekresyon tamamen durur.",
        "degerlendirme_kriteri": "Cevapta [2. dönem ve yüzeysel anestezide nistagmus, lakrimasyonun yüzeysel anestezi göstergesi olması, derinde lakrimasyonun olmaması] yer almalıdır.",
        "slayt_no": 17
    },
    {
        "soru_id": "au_gan_013",
        "soru": "Kedi ve köpeklerde yüzeysel-orta cerrahi anestezide göz küresi pozisyonu, göz kapakları ve 3. göz kapağının durumunu açıklayınız.",
        "ideal_cevap": "Kedi ve köpeklerde yüzeysel ya da orta düzeydeki cerrahi anestezi döneminde göz küresi genellikle aşağıya (ventrale) ve mediale doğru yer değiştirir. Bu dönemde göz kapakları genellikle kapalıdır ve 3. göz kapağı (harder/membrana nictitans) pasif olarak korneanın medial kısmını örter. Cerrahi anestezi derinleştikçe göz küresi tekrar santrale (merkeze) döner ve palpebral refleks gittikçe söner.",
        "degerlendirme_kriteri": "Cevapta [göz küresinin ventrale/aşağı kayması, göz kapaklarının kapalı olması, 3. göz kapağının korneanın medialini örtmesi, derinde santrale dönüş] yer almalıdır.",
        "slayt_no": 17
    },
    {
        "soru_id": "au_gan_014",
        "soru": "Premedikasyonda kullanılan atropin ve morfinin pupilla boyutuna etkisini ve derin anestezideki pupilla dilatasyonunun klinik anlamını açıklayınız.",
        "ideal_cevap": "Atropin gibi parasempatolitikler pupillada genişlemeye (midriyazis); morfin gibi opioidler ise türe özgü olarak miyozis veya midriyazise yol açarak anestezik derinlik takibini maskeleyebilir. Normal anestezi seyrinde pupilla 2. dönemde dilate, sonra kontrakte olur. Ancak derin anestezi döneminde (Plan 4) gelişen belirgin pupilla dilatasyonu anestezik doz aşımını ve hipoksik beyin sapı depresyonunu işaret eden çok tehlikeli bir bulgudur.",
        "degerlendirme_kriteri": "Cevapta [atropin/morfinin pupillayı etkilemesi, 2. dönemde dilatasyon sonra kontraksiyon, derin anestezide dilatasyonun doz aşımı göstergesi olması] bulunmalıdır.",
        "slayt_no": 18
    },
    {
        "soru_id": "au_gan_015",
        "soru": "Palpebral ve korneal reflekslerin muayene yöntemini açıklayarak, atlarda korneal refleksin diğer hayvan türlerinden farkını yazınız.",
        "ideal_cevap": "Palpebral refleks göz kapaklarının medial açısına (kantus) hafifçe dokunularak; korneal refleks ise korneanın medial açısına nazikçe dokunularak test edilir. Normalde orta-derin anestezide palpebral refleks kaybolduktan kısa süre sonra korneal refleks de silinir. Ancak ATLARDA korneal refleks derin anestezi döneminde dahi mevcuttur; bu nedenle atlarda korneal refleksin tamamen kaybolması ölümcül bir doz aşımını (Plan 4 veya Dönem IV) gösterir.",
        "degerlendirme_kriteri": "Cevapta [medial açıya dokunma, korneal refleksin palpebralden sonra kaybolması, atlarda derin anestezide bile korneal refleksin mevcudiyeti] yer almalıdır.",
        "slayt_no": 19
    },
    {
        "soru_id": "au_gan_016",
        "soru": "Kedilerde yutkunma ve laringeal refleksin anestezi dönemlerindeki özel seyrini ve endotrakeal entübasyon açısından önemini yazınız.",
        "ideal_cevap": "Genel kural olarak yutkunma ve kusma refleksleri 3. dönemin başında (Plan 1) kaybolur. Ancak kedilerde yutkunma ve özellikle laringeal refleksler diğer türlere göre çok daha inatçıdır ve orta düzey anestezi (Plan 2) oluşana kadar sürebilir. Bu durum kedilerde laringospazm riskini artırdığı için, entübasyon öncesinde larinkse lokal anestezik (lidokain sprey) uygulanması ve yeterli anestezi derinliği sağlanması şarttır.",
        "degerlendirme_kriteri": "Cevapta [yutkunmanın normalde 3. dönemde kalkması, kedilerde orta düzeye kadar sürebilmesi, laringeal refleks hassasiyeti/laringospazm] yer almalıdır.",
        "slayt_no": 20
    },
    {
        "soru_id": "au_gan_017",
        "soru": "Atlarda anal sfinkter tonusunun anestezi dönemlerine göre değişimini ve kas relaksasyonu göstergesi olarak değerini açıklayınız.",
        "ideal_cevap": "Atlarda anal sfinkterin gevşemesi sistemik kas relaksasyonunun en güvenilir göstergelerindendir. Anestezinin 2. döneminde sfinkter oldukça sıkı ve kasılıdır. Anestezi derinleştikçe sfinkter gevşemeye başlar ve anal kanal içinde dışkı görünür hale gelir. Anal sfinkterdeki bu gevşeme anestezi boyunca sürer ve derin anestezi döneminde sfinkter mekanik uyarılara dahi cevap veremez hale gelir.",
        "degerlendirme_kriteri": "Cevapta [2. dönemde sıkı sfinkter, derinleştikçe gevşeme ve dışkı görünmesi, derin anestezide mekanik uyarıya yanıtsızlık, relaksasyon göstergesi] yer almalıdır.",
        "slayt_no": 20
    },
    {
        "soru_id": "au_gan_018",
        "soru": "Köpeklerde çene kas tonusu ve ağzın pasif açılabilmesinin anestezi derinliği takibindeki klinik önemini barbitürat anestezisi bağlamında açıklayınız.",
        "ideal_cevap": "Köpeklerde ağzın hekim tarafından pasif olarak açılabilmesi ve çene direncinin değerlendirilmesi anestezi derinliğinin en pratik kriterlerindendir. Köpekte 2. dönemden 3. döneme geçildiğinde çene eklemi özellikle barbitürat anestezisinde rahatlıkla ve dirençsiz açılır. Ağzın tamamen açılmasına karşı gösterilen direnç ve ısırma refleksi 3. dönemde tamamen kaybolur.",
        "degerlendirme_kriteri": "Cevapta [pasif ağız açılması, 2'den 3'e geçerken çene ekleminin barbitüratta rahat açılması, açılmaya karşı tepkinin 3. dönemde kaybolması] bulunmalıdır.",
        "slayt_no": 21
    },
    {
        "soru_id": "au_gan_019",
        "soru": "Köpek, kedi ve ratlarda pedal refleks (parmak arası ağrılı uyaran) muayenesinin evrelere göre seyrini açıklayınız.",
        "ideal_cevap": "Pedal refleks; ekstremitenin parmaklar arası deri bölgesinin forseps veya parmakla sıkılması (ağrılı uyaran) sonucu ekstremitede fleksiyon yanıtı oluşmasıdır. Köpek, kedi ve ratlarda anestezinin derinliğini belirlemede sıklıkla kullanılır. Bu fleksiyon refleksi yüzeysel anestezi seviyesinde (Plan 1) korunurken, yüzeysel anesteziden orta derecede anesteziye (Plan 2) geçişte tamamen kaybolur.",
        "degerlendirme_kriteri": "Cevapta [ekstremite fleksiyonu, parmaklar arası ağrılı uyaran, yüzeyselden orta anesteziye geçişte kaybolması] yer almalıdır.",
        "slayt_no": 22
    },
    {
        "soru_id": "au_gan_020",
        "soru": "Kedi, kobay ve tavşanlarda anestezi derinliğini test etmek için kullanılan kulak refleksi (pinna refleksi) protokolünü ve cerrahi anestezi ile ilişkisini açıklayınız.",
        "ideal_cevap": "Kedi, kobay ve tavşanlarda kulak kepçesinin (pinna) parmakla hafifçe sıkılması veya uyarılması sonrasında hayvanda başın hızla sallanması şeklinde karakteristik bir tepki oluşur. Bu refleks anestezi derinliğinin tespiti için rutin kullanılır. Hayvanda cerrahi anestezi (III. Dönem 2. Plan) tam olarak oluştuğunda kulağın sıkılmasına karşı hiçbir baş sallama tepkisi oluşmaz.",
        "degerlendirme_kriteri": "Cevapta [kulağın sıkılması, baş sallama tepkisi, cerrahi anestezide tepkinin tamamen kaybolması, kedi/kobay/tavşan türleri] yer almalıdır.",
        "slayt_no": 22
    }
]

COKTAN_SECMELI_SORULAR = [
    {
        "soru_id": "mcq_gan_001",
        "soru_metni": "Genel anestezinin tanımıyla ilgili aşağıdaki ifadelerden hangisi doğru DEĞİLDİR?",
        "secenekler": {
            "A": "Ağrı hissinin tamamen ortadan kaldırılması ile karakterizedir",
            "B": "Kontrollü ve geri dönüşümlü (reverzibl) bir şuursuzluk halidir",
            "C": "Refleks cevaplarının nispeten ortadan kalkması gözlenir",
            "D": "Kardiyorespiratuvar fonksiyonların kalıcı olarak durdurulmasını hedefler"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği yanlıştır; genel anestezi kalıcı bir durdurma değil, kontrollü, güvenli ve reverzibl (geri dönüşümlü) bir durumdur (Slayt 1).",
            "celdirici_analizi": "A, B ve C seçenekleri slayt 1'de yer alan genel anestezinin resmi tanım maddeleridir."
        },
        "slayt_no": 1,
        "zorluk_derecesi": "kolay",
        "etiketler": ["genel_anestezi", "tanim"]
    },
    {
        "soru_id": "mcq_gan_002",
        "soru_metni": "Aşağıdaki anestezik maddelerden hangisi 'Enjektabl anestezikler' grubunda yer alır?",
        "secenekler": {
            "A": "Halotan",
            "B": "Tiyopental (Thiopental)",
            "C": "İzofluran",
            "D": "Sevofluran"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Tiyopental bir barbitürat olup enjektabl anesteziktir (Slayt 1).",
            "celdirici_analizi": "A, C ve D şıkları inhalasyon (gaz) anestezikleridir."
        },
        "slayt_no": 1,
        "zorluk_derecesi": "kolay",
        "etiketler": ["farmakoloji", "enjektabl"]
    },
    {
        "soru_id": "mcq_gan_003",
        "soru_metni": "İntravenöz anestezi ile karşılaştırıldığında, inhalasyon yolu ile anestezi indüksiyonunun en önemli avantajı hangisidir?",
        "secenekler": {
            "A": "Daha ucuz ekipman gerektirmesi",
            "B": "Çok daha güvenli olması ve birkaç defa enjeksiyon yapma zorunluluğunu ortadan kaldırması",
            "C": "Solunum sistemine hiçbir etkisi olmaması",
            "D": "Premedikasyona olan ihtiyacı tamamen kaldırması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; inhalasyon indüksiyonu çok daha güvenlidir ve tekrarlayan enjeksiyon zorunluluğunu kaldırır (Slayt 1).",
            "celdirici_analizi": "A şıkkı yanlıştır (cihaz maliyetlidir); C ve D şıkları bilimsel olarak hatalıdır."
        },
        "slayt_no": 1,
        "zorluk_derecesi": "kolay",
        "etiketler": ["inhalasyon", "avantaj"]
    },
    {
        "soru_id": "mcq_gan_004",
        "soru_metni": "Genel anestezi altındaki bir hayvanda solunum mekaniğinde meydana gelen değişimlerle ilgili hangisi doğrudur?",
        "secenekler": {
            "A": "İnspirasyon süresi ekspirasyona göre 3 kat uzar",
            "B": "Ekspiratorik kaslar aktif hale gelirken, ekspirasyon süresi oldukça uzar",
            "C": "İnspiratorik kas tonusu hiçbir zaman kesintiye uğramaz",
            "D": "Solunum ritmi tamamen spontan ve kusursuz düzenli kalır"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; ekspiratorik kaslar aktifleşir, inspirasyon sonunda inspiratuvar tonus aniden durur ve ekspirasyon belirgin uzar (Slayt 2).",
            "celdirici_analizi": "A şıkkı tersidir (ekspirasyon uzar); C ve D şıkları slayt 2 ile çelişmektedir."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "orta",
        "etiketler": ["fizyoloji", "solunum"]
    },
    {
        "soru_id": "mcq_gan_005",
        "soru_metni": "Atlarda anestezi sırasında 2, 3 hatta 4 solunum aldıktan sonra uzun süreli duraklama (apne) ile karakterize olan solunum tipine ne ad verilir?",
        "secenekler": {
            "A": "Kussmaul solunumu",
            "B": "Biot solunumu",
            "C": "Periyodik solunum",
            "D": "Paradoksal solunum"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; atlarda bu özel duruma 'periyodik solunum' denir (Slayt 2).",
            "celdirici_analizi": "Kussmaul asidozda, Biot menenjitte görülür; paradoksal solunum doz aşımında diyafram-toraks uyumsuzluğudur."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "kolay",
        "etiketler": ["at", "solunum"]
    },
    {
        "soru_id": "mcq_gan_006",
        "soru_metni": "Genel anestezinin her türünde akciğerlerin fonksiyonel kapasitesindeki (FRC) azalma oranı temel olarak hangisine göre değişir?",
        "secenekler": {
            "A": "Hayvanın ırkına göre",
            "B": "Hayvanın yatış pozisyonuna göre",
            "C": "Operasyon odasının sıcaklığına göre",
            "D": "Kullanılan endotrakeal tüpün markasına göre"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; fonksiyonel kapasite azalması hayvanın yatış pozisyonuna (dorsal, lateral vb.) göre değişir (Slayt 2).",
            "celdirici_analizi": "A, C ve D seçenekleri doğrudan belirleyici faktörler değildir."
        },
        "slayt_no": 2,
        "zorluk_derecesi": "kolay",
        "etiketler": ["akciger", "pozisyon"]
    },
    {
        "soru_id": "mcq_gan_007",
        "soru_metni": "Hastada bilincin kaybolup bilinçsizlik halinin başladığı ve hastanın anesteziye girdiği döneme ne ad verilir?",
        "secenekler": {
            "A": "Premedikasyon",
            "B": "İndüksiyon",
            "C": "İdame",
            "D": "Reanimasyon"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; bilincin kaybolup anesteziye giriş dönemine indüksiyon denir (Slayt 3).",
            "celdirici_analizi": "Premedikasyon hazırlıktır; idame sürdürmedir; reanimasyon canlandırmadır."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "kolay",
        "etiketler": ["induksiyon", "tanim"]
    },
    {
        "soru_id": "mcq_gan_008",
        "soru_metni": "Premedikasyon uygulamasından sonra tam etkinin oluşması için indüksiyon öncesinde intramusküler (IM) ve subkutan (SC) yollarda en az ne kadar süre beklenilmelidir?",
        "secenekler": {
            "A": "IM en az 2 dk, SC en az 5 dk",
            "B": "IM en az 10 dk, SC en az 20 dk",
            "C": "IM en az 30 dk, SC en az 60 dk",
            "D": "Beklemeye gerek yoktur, anında indüksiyona geçilir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; IM uygulamadan sonra en az 10 dk, SC uygulamadan sonra en az 20 dk beklenmelidir (Slayt 3).",
            "celdirici_analizi": "Diğer süreler yetersiz veya gereksiz uzundur."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "orta",
        "etiketler": ["premedikasyon", "sure"]
    },
    {
        "soru_id": "mcq_gan_009",
        "soru_metni": "Genel anestezinin fiilen başladığını gösteren en temel refleksif kriter hangisidir?",
        "secenekler": {
            "A": "Patella refleksinin kaybolması",
            "B": "Pupillanın tamamen daralması",
            "C": "Yutkunma refleksinin ortadan kalkması",
            "D": "Kulak refleksinin şiddetlenmesi"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; genel anestezinin başlaması yutkunma refleksinin ortadan kalkması ile karakterizedir (Slayt 3).",
            "celdirici_analizi": "A, B ve D şıkları başlangıç işareti değildir."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "kolay",
        "etiketler": ["refleks", "yutkunma"]
    },
    {
        "soru_id": "mcq_gan_010",
        "soru_metni": "Operasyonun ve diğer cerrahi manipülasyonların gerçekleştirildiği, anestezinin stabil seviyede seyrettiği periyot hangisidir?",
        "secenekler": {
            "A": "İndüksiyon dönemi",
            "B": "İdame dönemi",
            "C": "Sedasyon fazı",
            "D": "Uyanma dönemi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; operasyon ve manipülasyonlar idame döneminde yapılır (Slayt 4).",
            "celdirici_analizi": "İndüksiyon giriş; uyanma çıkış evresidir."
        },
        "slayt_no": 4,
        "zorluk_derecesi": "kolay",
        "etiketler": ["idame", "operasyon"]
    },
    {
        "soru_id": "mcq_gan_011",
        "soru_metni": "Anestezinin idame döneminde derinliğin aşırı artması ve tablonun kötüye gitmesi fark edilmezse ne şekillenir?",
        "secenekler": {
            "A": "Hipertermi ve hipertansiyon",
            "B": "Respiratorik ve kardiyak arrest",
            "C": "Şiddetli kusma ve spazm",
            "D": "Ani uyanma ve saldırganlık"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; derinleşme fark edilmezse solunum ve kardiyak arrest şekillenir (Slayt 4).",
            "celdirici_analizi": "A, C ve D derin anestezi arrest tablosuyla uyuşmaz."
        },
        "slayt_no": 4,
        "zorluk_derecesi": "kolay",
        "etiketler": ["idame", "arrest"]
    },
    {
        "soru_id": "mcq_gan_012",
        "soru_metni": "Kısa süreli barbitüratlarda (tiyopental), vücutta anestezik madde bulunmasına rağmen anestezi etkisinin hızla ortadan kalkmasının sebebi nedir?",
        "secenekler": {
            "A": "İlacın akciğerlerden ekspirasyonla anında atılması",
            "B": "İlacın vücut yağları tarafından absorbe edilmesi (redistribüsyon)",
            "C": "Mideden kusma yoluyla dışarı atılması",
            "D": "Tüm ilacın dakikalar içinde böbrekten idrarla süzülmesi"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kısa süreli barbitüratlar beyinden çekilerek vücut yağ dokularına absorbe olur (redistribüsyon) (Slayt 5).",
            "celdirici_analizi": "Barbitürat gaz değildir (A elenir); yağda tutulum nedeniyle metabolizma/atılım sonradan yavaş tamamlanır."
        },
        "slayt_no": 5,
        "zorluk_derecesi": "orta",
        "etiketler": ["farmakokinetik", "barbiturat"]
    },
    {
        "soru_id": "mcq_gan_013",
        "soru_metni": "İnhalasyon anesteziklerinin anesteziden uyanma sırasında vücudu terk etme sırası hangisinde doğru verilmiştir?",
        "secenekler": {
            "A": "Karaciğer -> Safra -> Dışkı",
            "B": "Böbrek -> İdrar -> Üretra",
            "C": "Beyin -> Kan -> Alveoller -> Solunum yolu",
            "D": "Yağ dokusu -> Kas -> Deri"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; moleküller beyni terk eder, kana geçer, kandan alveollere geçerek solunumla atılır (Slayt 5).",
            "celdirici_analizi": "İnhalasyon ilaçları temel olarak pulmoner yolla elimine edilir."
        },
        "slayt_no": 5,
        "zorluk_derecesi": "kolay",
        "etiketler": ["inhalasyon", "eliminasyon"]
    },
    {
        "soru_id": "mcq_gan_014",
        "soru_metni": "Anestezinin I. Dönemi ile ilgili aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "secenekler": {
            "A": "Hasta tamamen bilinçsizdir ve tüm refleksler kaybolmuştur",
            "B": "Hayvanın bilinci yerindedir, ancak davranışlarda uyumsuzluk başlar ve ağrıya hassasiyet azalır",
            "C": "Cerrahi müdahaleler bu dönemde güvenle yapılır",
            "D": "Pupillalar aşırı dilate ve ışık refleksi kayıptır"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; I. dönemde bilinç yerindedir, davranış uyumsuzluğu başlar, ağrı hassasiyeti azalır, refleksler ve yaşamsal fonksiyonlar normaldir (Slayt 7).",
            "celdirici_analizi": "A ve D derin anesteziye aittir; C şıkkında cerrahi henüz yapılamaz."
        },
        "slayt_no": 7,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem1", "klinik"]
    },
    {
        "soru_id": "mcq_gan_015",
        "soru_metni": "Anestezinin II. Döneminde (Eksitasyon) reflekslerin durumu nasıldır?",
        "secenekler": {
            "A": "Tüm refleksler tamamen ortadan kalkmıştır",
            "B": "Sadece patella refleksi mevcuttur",
            "C": "Tüm refleksler hala mevcuttur, hatta bu reflekslerde artma meydana gelebilir",
            "D": "Korneal refleks kaybolmuş, yutkunma durmuştur"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; II. dönemde tüm refleksler mevcuttur ve hatta artabilir (hiperrefleksi) (Slayt 8).",
            "celdirici_analizi": "Refleksler II. dönemde sönmez; aksine çabalama ve refleks artışı tipiktir."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem2", "refleks"]
    },
    {
        "soru_id": "mcq_gan_016",
        "soru_metni": "Aşağıdaki klinik tablolardan hangisi anestezinin II. Dönemine özgüdür?",
        "secenekler": {
            "A": "Ekstremitelerde hareketler, bağırma, çabalama ve düzensiz solunum/nefes tutma",
            "B": "Tam kas relaksasyonu ve düzenli derin solunum",
            "C": "Göz küresinin santralde fiksasyonu ve kornea kuruluğu",
            "D": "Kalp durması ve apne"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; II. dönem eksitasyon, bağırma, çabalama ve düzensiz solunumla bilinir (Slayt 8).",
            "celdirici_analizi": "B seçeneği cerrahi döneme, C ve D aşırı derin döneme aittir."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "kolay",
        "etiketler": ["donem2", "semptom"]
    },
    {
        "soru_id": "mcq_gan_017",
        "soru_metni": "Anestezi uygulamasında II. Dönemle karşılaşıldığında hekimin temel stratejisi ne olmalıdır?",
        "secenekler": {
            "A": "Anesteziyi hemen sonlandırıp hastayı uyandırmak",
            "B": "Anestezinin derinliğini mümkün olduğunca kısa sürede arttırarak 3. döneme geçmek",
            "C": "Cerrahi insizyona hemen başlamak",
            "D": "Hastayı mekanik ventilatöre bağlayıp hiçbir ilaç vermemek"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; bu süreyi kısaltmak için derinlik mümkün olduğunca kısa sürede artırılarak 3. döneme geçilmelidir (Slayt 8).",
            "celdirici_analizi": "II. dönemde ameliyat yapılmaz (C); eksitasyonda beklemek veya kesmek tehlikelidir."
        },
        "slayt_no": 8,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem2", "yonetim"]
    },
    {
        "soru_id": "mcq_gan_018",
        "soru_metni": "III. Dönem 1. Planda endotrakeal tüpün kolaylıkla uygulanabilmesinin (entübasyonun) temel nedeni nedir?",
        "secenekler": {
            "A": "Tüm kasların tamamen felç olması",
            "B": "Yutkunma refleksinin oldukça azalmış olması",
            "C": "Korneal refleksin tamamen kaybolması",
            "D": "Göz kapaklarının tamamen yapışması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; yutkunma refleksi oldukça azaldığı için endotrakeal tüp kolaylıkla takılabilir (Slayt 9).",
            "celdirici_analizi": "Plan 1'de kaslar tam felç değildir; korneal refleks mevcuttur."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem3_plan1", "entubasyon"]
    },
    {
        "soru_id": "mcq_gan_019",
        "soru_metni": "III. Dönem 1. Planda göz küresi pozisyonu nasıldır?",
        "secenekler": {
            "A": "Göz küresi merkezdedir (santral)",
            "B": "Göz küresi ventrale ve gözün iç açısına doğru kayar",
            "C": "Göz küresi dorsale ve dış açıya fiksasyondadır",
            "D": "Göz küresi sürekli hızlı nistagmus halindedir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; göz küresi ventrale ve iç açıya kayar (Slayt 9).",
            "celdirici_analizi": "Plan 2 ve 3'te göz küresi merkeze gelir."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem3_plan1", "goz"]
    },
    {
        "soru_id": "mcq_gan_020",
        "soru_metni": "III. Dönem 1. Planda operasyona başlanırsa hastada ne gözlenir?",
        "secenekler": {
            "A": "Hiçbir tepki vermez, mükemmel tolere eder",
            "B": "Hasta derin komaya girer",
            "C": "Cerrahi müdahale tolere edilemez, ağrı duyulur ve kımıldanmalar görülebilir",
            "D": "Kalp anında durur"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; cerrahi tolere edilemez, ağrı duyulur ve kımıldanmalar görülür (Slayt 9).",
            "celdirici_analizi": "Plan 1 yüzeyseldir, ameliyat için Plan 2'ye geçilmelidir."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "kolay",
        "etiketler": ["donem3_plan1", "cerrahi"]
    },
    {
        "soru_id": "mcq_gan_021",
        "soru_metni": "Cerrahi işlemler için ideal orta düzey anestezi sağlayan III. Dönem 2. Planda göz küresi ve pupilla durumu nasıldır?",
        "secenekler": {
            "A": "Göz küresi merkezdedir, pupilla hafifçe dilate haldedir ve ışık yanıtı azalmıştır",
            "B": "Göz küresi ventrale kaymıştır, pupilla aşırı derecede daralmıştır",
            "C": "Göz küresi dışarı fırlamıştır, pupilla fiks midriyazistedir",
            "D": "Göz küresi sürekli nistagmus gösterir, pupilla ışığa aşırı duyarlıdır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; Plan 2'de göz küresi merkezdedir, pupilla hafifçe dilatedir ve ışığa yanıtı azalmıştır (Slayt 10).",
            "celdirici_analizi": "Ventrale kayma Plan 1'dedir; aşırı fiks midriyazis Plan 4'tedir."
        },
        "slayt_no": 10,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem3_plan2", "pupilla"]
    },
    {
        "soru_id": "mcq_gan_022",
        "soru_metni": "III. Dönem 2. Planda (Orta düzey anestezi) reflekslerin durumu hangisinde doğru özetlenmiştir?",
        "secenekler": {
            "A": "Tüm refleksler hiperaktif haldedir",
            "B": "Pedal ve palpebral refleksler azalmış ya da kaybolmuştur",
            "C": "Korneal refleks tamamen yok olmuş, solunum durmuştur",
            "D": "Yutkunma refleksi artmıştır"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; pedal ve palpebral refleksler azalmış ya da kaybolmuştur (Slayt 10).",
            "celdirici_analizi": "A şıkkı Dönem II'dir; C şıkkı Dönem IV/Plan 4'tür."
        },
        "slayt_no": 10,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem3_plan2", "refleks"]
    },
    {
        "soru_id": "mcq_gan_023",
        "soru_metni": "III. Dönem 3. Plan ile ilgili aşağıdaki klinik ifadelerden hangisi DOĞRUDUR?",
        "secenekler": {
            "A": "Yüzeysel anestezi seviyesidir, hasta operasyona tepki verir",
            "B": "Birçok cerrahi müdahale için oldukça derin anestezidir; solunumu rezerv balonu veya ventilatörle desteklemek gerekir",
            "C": "Refleksler aşırı artmıştır ve kaslar sertleşmiştir",
            "D": "Kapiller dolma süresi (CRT) kısalır ve nabız hızlanır"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; Plan 3 oldukça derindir, solunumu rezerv balon/ventilatörle desteklemek gerekir, CRT uzar (Slayt 11).",
            "celdirici_analizi": "A, C ve D seçenekleri Plan 3 bulgularının tam tersidir."
        },
        "slayt_no": 11,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem3_plan3", "solunum"]
    },
    {
        "soru_id": "mcq_gan_024",
        "soru_metni": "III. Dönem 3. Planda refleksler ve iskelet kas tonusu ne durumdadır?",
        "secenekler": {
            "A": "Refleksler tamamen ortadan kalkmıştır ve iskelet kaslarında gevşeme ileri derecededir",
            "B": "Refleksler korunmuştur ancak kaslar tetaniktir",
            "C": "Yalnızca pedal refleks mevcuttur",
            "D": "Palpebral refleks belirgin olarak artmıştır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; refleksler tamamen kalkmıştır ve iskelet kaslarında ileri derece gevşeme vardır (Slayt 11).",
            "celdirici_analizi": "Plan 3'te hiçbir refleks kalmaz, kas relaksasyonu en üst düzeydedir."
        },
        "slayt_no": 11,
        "zorluk_derecesi": "kolay",
        "etiketler": ["donem3_plan3", "kas"]
    },
    {
        "soru_id": "mcq_gan_025",
        "soru_metni": "III. Dönem 4. Planda (aşırı derin anestezi) göz muayenesinde saptanan patognomonik bulgu hangisidir?",
        "secenekler": {
            "A": "Pupilla aşırı daralmış (miyozis) ve nistagmus vardır",
            "B": "Pupilla iyice dilate olmuş, ışığa karşı refleksi hiç kalmamış ve lakrimal sekresyon azlığından kornea kuru hale gelmiştir",
            "C": "Göz küresi ventrale kaymış ve lakrimasyon çok artmıştır",
            "D": "Korneal refleks aşırı şiddetlenmiştir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; pupilla iyice dilatedir (ışık refleksi yok), lakrimal salgı durduğu için kornea kurumuştur (Slayt 12).",
            "celdirici_analizi": "Lakrimasyon ve ventrale kayma yüzeysel dönemlere aittir."
        },
        "slayt_no": 12,
        "zorluk_derecesi": "orta",
        "etiketler": ["donem3_plan4", "goz"]
    },
    {
        "soru_id": "mcq_gan_026",
        "soru_metni": "Anestezinin IV. Döneminde gelişen olaylar zinciri hangisinde doğru sıralanmıştır?",
        "secenekler": {
            "A": "Solunum ortadan kalkar -> Sirkülasyon tamamen bozulur -> Ölüm şekillenir",
            "B": "Kalp hızlanır -> Kaslar kasılır -> Hasta aniden uyanır",
            "C": "Kusma başlar -> Refleksler artar -> Cerrahiye hazır hale gelir",
            "D": "Tansiyon yükselir -> Solunum derinleşir -> Bilinç yerine gelir"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; solunum durur, takiben sirkülasyon çöker ve ölüm şekillenir, acil resüsitasyon gerekir (Slayt 13).",
            "celdirici_analizi": "IV. dönem bulbar felç/toksik evredir."
        },
        "slayt_no": 13,
        "zorluk_derecesi": "kolay",
        "etiketler": ["donem4", "arrest"]
    },
    {
        "soru_id": "mcq_gan_027",
        "soru_metni": "Genel anestezi uygulamasında hedeflenen 'İdeal anestezi dönemi' aşağıdakilerden hangisidir?",
        "secenekler": {
            "A": "I. Dönem",
            "B": "II. Dönem",
            "C": "III. Dönem (Özellikle 2. Plan - hastanın cerrahi müdahaleyi hissetmediği dönem)",
            "D": "IV. Dönem"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; ideal dönem hastanın cerrahiyi hissetmediği ve stabil olduğu III. Dönem 2. Plandır (Slayt 10, 13).",
            "celdirici_analizi": "I ağrılıdır; II eksitasyondur; IV ölüm evresidir."
        },
        "slayt_no": 13,
        "zorluk_derecesi": "kolay",
        "etiketler": ["ideal_anestezi", "klinik"]
    },
    {
        "soru_id": "mcq_gan_028",
        "soru_metni": "Hayvanda sedasyon uygulanmamış ise anestezinin 1. döneminde solunumla ilgili hangi davranış görülebilir?",
        "secenekler": {
            "A": "Hayvan bilinçli olarak solunumunu tutabilir",
            "B": "Solunum tamamen durur",
            "C": "Paradoksal solunum başlar",
            "D": "Solunum hızı dakikada 200'ü aşar"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; sedasyonsuz 1. dönemde hayvan bilinçli olarak solunumunu tutabilir (Slayt 14).",
            "celdirici_analizi": "Bilinçli solunum tutma bilincin korunduğu 1. döneme özgüdür."
        },
        "slayt_no": 14,
        "zorluk_derecesi": "orta",
        "etiketler": ["solunum", "donem1"]
    },
    {
        "soru_id": "mcq_gan_029",
        "soru_metni": "Premedikasyonda ya da indüksiyonda barbitürat uygulanan hastalarda, hangi evrenin başında solunum depresyonu görülmesi karakteristiktir?",
        "secenekler": {
            "A": "1. dönemin başında",
            "B": "2. dönemin sonunda",
            "C": "3. dönemin başında",
            "D": "Uyanma döneminin sonunda"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; barbitürat uygulandıysa 3. dönemin başında solunum depresyonu görülür (Slayt 14).",
            "celdirici_analizi": "Barbitüratların solunum merkezini suprese edici etkisi 3. dönemin başında belirginleşir."
        },
        "slayt_no": 14,
        "zorluk_derecesi": "orta",
        "etiketler": ["barbiturat", "solunum_depresyonu"]
    },
    {
        "soru_id": "mcq_gan_030",
        "soru_metni": "Anestezik doz aşımı durumunda solunum paterninin aldığı şekil ve toraks-abdomen ilişkisi hangisinde doğru tarif edilmiştir?",
        "secenekler": {
            "A": "Solunum tamamen torasiktir, abdomen hiç hareket etmez",
            "B": "Solunum tamamen abdominal hale gelir; inspirasyonda abdomen şişerken toraks kollabe olur",
            "C": "İnspirasyonda toraks aşırı genişler, ekspirasyon tamamen durur",
            "D": "Solunum dakika sayısı 3 katına çıkar"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; doz aşımında solunum abdominaldir, inspirasyonda abdomen şişer toraks kollabe olur, ekspirasyonda tersi olur (Slayt 15).",
            "celdirici_analizi": "Bu durum paradoksal solunumdur ve doz aşımının tipik işaretidir."
        },
        "slayt_no": 15,
        "zorluk_derecesi": "zor",
        "etiketler": ["doz_asimi", "abdominal_solunum"]
    },
    {
        "soru_id": "mcq_gan_031",
        "soru_metni": "Anestezi dönemlerinde sirkülasyon takibinde 'Aritmi' riski en çok hangi dönemde bazen görülebilir?",
        "secenekler": {
            "A": "I. Dönem",
            "B": "II. Dönem",
            "C": "III. Dönem 2. Plan",
            "D": "Uyanmadan 2 saat sonra"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; aritmi 2. dönemde bazen görülebilir (Slayt 16).",
            "celdirici_analizi": "II. dönemde sempatik fırtına ve katekolamin salgısı aritmiyi tetikler."
        },
        "slayt_no": 16,
        "zorluk_derecesi": "orta",
        "etiketler": ["aritmi", "donem2"]
    },
    {
        "soru_id": "mcq_gan_032",
        "soru_metni": "III. Dönemde kardiyovasküler sistemde pulzasyonun genel karakteri nasıldır?",
        "secenekler": {
            "A": "Pulzasyon düzenli hale gelmiştir ve genellikle hafif derecede hızlıdır",
            "B": "Nabız tamamen kaybolmuştur",
            "C": "Dakikada 10-15 vuruya kadar düşmüş ve aritmiktir",
            "D": "Şiddetli filiform ve düzensizdir"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; 3. dönemde pulzasyon düzenlidir ve genellikle hafif derecede hızlıdır (Slayt 16).",
            "celdirici_analizi": "3. dönem stabil cerrahi evredir, ritim düzenlidir."
        },
        "slayt_no": 16,
        "zorluk_derecesi": "orta",
        "etiketler": ["pulzasyon", "donem3"]
    },
    {
        "soru_id": "mcq_gan_033",
        "soru_metni": "Atlarda genel anestezinin 2. döneminde ve yüzeysel cerrahi anestezi döneminde gözlerde görülen karakteristik hareket hangisidir?",
        "secenekler": {
            "A": "Strabismus (şaşılık)",
            "B": "Nistagmus (göz küresi titremesi)",
            "C": "Ekzoftalmus",
            "D": "Pitozis"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; atlarda 2. dönemde ve yüzeysel cerrahi anestezide nistagmus görülür (Slayt 17).",
            "celdirici_analizi": "At anestezisinde nistagmus anestezinin henüz yeterince derin olmadığını gösterir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "kolay",
        "etiketler": ["at", "nistagmus"]
    },
    {
        "soru_id": "mcq_gan_034",
        "soru_metni": "Köpek ve kedilerde yüzeysel ya da orta düzeydeki cerrahi anestezi döneminde göz küresinin konumu nasıldır?",
        "secenekler": {
            "A": "Tamamen yukarıya (dorsale) bakar",
            "B": "Genellikle aşağıya (ventrale) doğru yer değiştirir",
            "C": "Sürekli dairesel rotasyon yapar",
            "D": "Hiç hareket etmeksizin fiks santraldedir"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; köpek ve kedilerde yüzeysel/orta cerrahi anestezide göz küresi genellikle aşağıya doğru yer değiştirir (Slayt 17).",
            "celdirici_analizi": "Aşağı kayma ve 3. göz kapağının medial korneayı örtmesi tipiktir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "orta",
        "etiketler": ["kedi_kopek", "goz_pozisyonu"]
    },
    {
        "soru_id": "mcq_gan_035",
        "soru_metni": "Aşağıdaki ilaçlardan hangileri premedikasyonda kullanıldığında pupillanın boyutunu doğrudan etkileyerek anestezi takibini yanıltabilir?",
        "secenekler": {
            "A": "Penisilin ve Amoksisilin",
            "B": "Atropin ve Morfin",
            "C": "Furosemid ve Spironolakton",
            "D": "Dekstroz ve Ringer Laktat"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; premedikasyonda kullanılan atropin ve morfin gibi ilaçlar pupillanın boyutunu etkilerler (Slayt 18).",
            "celdirici_analizi": "Atropin midriyazis, morfin ise türe göre miyozis/midriyazis yapar."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "kolay",
        "etiketler": ["farmakoloji", "pupilla"]
    },
    {
        "soru_id": "mcq_gan_036",
        "soru_metni": "Pupillanın evrelere göre dinamikleriyle ilgili aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "secenekler": {
            "A": "2. dönemde daralır, 3. dönemde aşırı genişler",
            "B": "2. dönemde dilate haldedir, daha sonra kontrakte hale gelir; derin anestezideki dilatasyon doz aşımını gösterir",
            "C": "Işık uyarısına karşılık pupilla kontraksiyon refleksi derin anestezide en güçlü halini alır",
            "D": "Anestezinin hiçbir evresinde pupilla boyutu değişmez"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 2. dönemde dilatedir, sonra kontrakte olur; derin anestezideki dilatasyon doz aşımını gösterir (Slayt 18).",
            "celdirici_analizi": "Derin anestezide fiks dilatasyon (paralitik midriyazis) doz aşımıdır."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "orta",
        "etiketler": ["pupilla", "dinamik"]
    },
    {
        "soru_id": "mcq_gan_037",
        "soru_metni": "Yüzeysel anesteziden orta döneme (Plan 2) geçildiğinde pupillada hangi refleks yanıtı ortadan kalkar?",
        "secenekler": {
            "A": "Işık uyarısına karşılık pupillanın kontraksiyon refleksi",
            "B": "Karanlıkta genişleme refleksi",
            "C": "Akomodasyon refleksi",
            "D": "Konsensüel refleks"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; yüzeysel anesteziden orta döneme geçildiğinde ışık uyarısına karşılık pupillanın kontraksiyon refleksi ortadan kalkar (Slayt 18).",
            "celdirici_analizi": "Işık uyarısına daralma yanıtı kaybolur veya belirgin azalır."
        },
        "slayt_no": 18,
        "zorluk_derecesi": "orta",
        "etiketler": ["pupilla", "isik_refleksi"]
    },
    {
        "soru_id": "mcq_gan_038",
        "soru_metni": "Atlarda anestezi takibinde 'lakrimasyon' (gözyaşı salgılanması) saptanması hekime neyi gösterir?",
        "secenekler": {
            "A": "Anestezinin aşırı derin olduğunu ve arrest tehlikesini",
            "B": "Anestezinin yüzeysel olduğunu",
            "C": "Gözde akut glokom şekillendiğini",
            "D": "Hastanın öldüğünü"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; atlarda lakrimasyon anestezinin yüzeysel olduğunu gösterir (derin anestezide lakrimasyon gözlenmez) (Slayt 19).",
            "celdirici_analizi": "Derin anestezi döneminde lakrimasyon tamamen durur."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "kolay",
        "etiketler": ["at", "lakrimasyon"]
    },
    {
        "soru_id": "mcq_gan_039",
        "soru_metni": "Göz kapaklarının medial açısına hafifçe dokunularak tespit edilen refleks hangisidir?",
        "secenekler": {
            "A": "Korneal refleks",
            "B": "Palpebral refleks",
            "C": "Pupilla ışık refleksi",
            "D": "Okulokardiyak refleks"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; göz kapaklarının medial açısına dokunarak palpebral refleks tespit edilir (Slayt 19).",
            "celdirici_analizi": "Korneanın medialine dokunulduğunda ise korneal refleks ölçülür."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "kolay",
        "etiketler": ["palpebral_refleks", "muayene"]
    },
    {
        "soru_id": "mcq_gan_040",
        "soru_metni": "Korneal refleks ile ilgili aşağıdaki klinik kurallardan hangisi ATLAR için hayati bir istisnadır?",
        "secenekler": {
            "A": "Atlarda korneal refleks hiçbir zaman oluşmaz",
            "B": "Atlarda korneal refleks derin anestezi döneminde bile hala mevcuttur",
            "C": "Atlarda korneal refleks 1. dönemde hemen kaybolur",
            "D": "Atlarda sadece sol gözde mevcuttur"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; atlarda korneal refleks derin anestezi döneminde bile hala mevcuttur (Slayt 19).",
            "celdirici_analizi": "Diğer türlerde orta-derinde kaybolurken, atlarda derin anestezide bile korunması tipik bir sınav bilgisidir."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "zor",
        "etiketler": ["at", "korneal_refleks"]
    },
    {
        "soru_id": "mcq_gan_041",
        "soru_metni": "Yutkunma ve kusma refleksleri kural olarak genel anestezinin hangi döneminde ortadan kalkar?",
        "secenekler": {
            "A": "1. dönemde",
            "B": "2. dönemde",
            "C": "3. dönemde",
            "D": "4. dönemde"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; yutkunma ve kusma refleksi 3. dönemde ortadan kalkar (Slayt 20).",
            "celdirici_analizi": "Yutkunmanın kalkması 3. döneme (cerrahi evre) geçişin tescilidir."
        },
        "slayt_no": 20,
        "zorluk_derecesi": "kolay",
        "etiketler": ["yutkunma", "kusma_refleksi"]
    },
    {
        "soru_id": "mcq_gan_042",
        "soru_metni": "Kedilerde yutkunma ve laryngeal refleksin anestezi altındaki özelliği hangisidir?",
        "secenekler": {
            "A": "1. dönemde tamamen kaybolur",
            "B": "Orta düzey anestezi oluşana kadar sürebilir",
            "C": "Asla kaybolmaz, ölüm anında bile vardır",
            "D": "Kedilerde laryngeal refleks bulunmaz"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kedilerde yutkunma ve laryngeal refleks orta düzey anestezi oluşana kadar sürebilir (Slayt 20).",
            "celdirici_analizi": "Bu nedenle kedilerde entübasyon sırasında laringospazm riski yüksektir."
        },
        "slayt_no": 20,
        "zorluk_derecesi": "orta",
        "etiketler": ["kedi", "laryngeal_refleks"]
    },
    {
        "soru_id": "mcq_gan_043",
        "soru_metni": "Atlarda relaksasyonun (kas gevşemesinin) iyi bir göstergesi olarak kabul edilen refleks parametresi hangisidir?",
        "secenekler": {
            "A": "Anal sfinkterin gevşemesi",
            "B": "Kulakların dikleşmesi",
            "C": "Dilin içeri çekilmesi",
            "D": "Kuyruğun havaya kalkması"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; atlarda anal sfinkterin gevşemesi bu hayvanlarda relaksasyonun iyi bir göstergesidir (Slayt 20).",
            "celdirici_analizi": "Sfinkter derinleştikçe gevşer, dışkı görünür, derinde mekanik uyarıya yanıtsızlaşır."
        },
        "slayt_no": 20,
        "zorluk_derecesi": "orta",
        "etiketler": ["at", "anal_sfinkter"]
    },
    {
        "soru_id": "mcq_gan_044",
        "soru_metni": "Atlarda anal sfinkter tonusunun evrelere göre seyriyle ilgili hangisi DOĞRUDUR?",
        "secenekler": {
            "A": "2. dönemde gevşektir, 3. dönemde aşırı kasılır",
            "B": "2. dönemde sfinkter sıkı bir haldedir; anestezi derinleştikçe gevşer, anal kanalda dışkı görünür ve derin anestezide mekanik uyarılara cevapsız kalır",
            "C": "Anal sfinkter tonusu anestezi derinliğinden hiç etkilenmez",
            "D": "Yalnızca indüksiyonda dışkılama olur, sonra sfinkter kapanır"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 2. dönemde sıkıdır, derinleştikçe gevşer ve dışkı görünür, derinde mekanik uyarılara cevapsız kalır (Slayt 20).",
            "celdirici_analizi": "Slayt 20'de kelimesi kelimesine bu seyir anlatılmaktadır."
        },
        "slayt_no": 20,
        "zorluk_derecesi": "orta",
        "etiketler": ["at", "sfinkter_dinamik"]
    },
    {
        "soru_id": "mcq_gan_045",
        "soru_metni": "Köpeklerde 2. dönemden 3. döneme geçildiğinde çene ekleminin rahatlıkla açılması özellikle hangi anestezik kullanımında belirgindir?",
        "secenekler": {
            "A": "Ketamin anestezisi",
            "B": "Barbitürat anestezisi",
            "C": "Ksilazin sedasyonu",
            "D": "Morfin uygulaması"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; 2. dönemden 3. döneme geçildiğinde çene eklemi özellikle barbitürat anestezisinde rahatlıkla açılır (Slayt 21).",
            "celdirici_analizi": "Ketamin çene kaslarında tonus artışı ve sertlik yapabilirken barbitürat tam relaksasyon sağlar."
        },
        "slayt_no": 21,
        "zorluk_derecesi": "orta",
        "etiketler": ["kopek", "cene_eklemi", "barbiturat"]
    },
    {
        "soru_id": "mcq_gan_046",
        "soru_metni": "Köpeklerde ağzın tamamen açılmasına karşı gösterilen direnç tepkisi anestezinin hangi döneminde kaybolur?",
        "secenekler": {
            "A": "1. dönemde",
            "B": "2. dönemde",
            "C": "3. dönemde",
            "D": "Uyanma döneminde"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; ağzın tamamen açılmasına karşı tepki anestezinin 3. döneminde kaybolur (Slayt 21).",
            "celdirici_analizi": "3. dönemde çene direnci tamamen kırılır."
        },
        "slayt_no": 21,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kopek", "cene_tonusu"]
    },
    {
        "soru_id": "mcq_gan_047",
        "soru_metni": "Köpek, kedi ve ratlarda ekstremitelerin fleksiyonuna ya da parmaklar arası bölgenin ağrılı uyarımına tepki (pedal refleks) ne zaman kaybolur?",
        "secenekler": {
            "A": "Premedikasyon yapılır yapılmaz",
            "B": "Yüzeysel anesteziden orta derecede anesteziye geçişte",
            "C": "Yalnızca 4. dönemde kalp durduğunda",
            "D": "Hiçbir zaman kaybolmaz"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; pedal refleks yüzeysel anesteziden orta derecede anesteziye (Plan 2) geçişte kaybolur (Slayt 22).",
            "celdirici_analizi": "Pedal refleksin kaybolması hastanın cerrahiye hazır olduğunun göstergesidir."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "orta",
        "etiketler": ["pedal_refleks", "derinlik"]
    },
    {
        "soru_id": "mcq_gan_048",
        "soru_metni": "Kedi, kobay ve tavşanlarda kulağın sıkılması sonrasında başın sallanması şeklinde oluşan tepki (kulak/pinna refleksi) ne zaman ortadan kalkar?",
        "secenekler": {
            "A": "Hayvan ameliyathaneye alındığında",
            "B": "Cerrahi anestezi oluştuğunda",
            "C": "Hayvan uyandıktan sonra",
            "D": "Sadece ölüm gerçekleştikten 1 saat sonra"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; cerrahi anestezi oluştuğunda kulağın sıkılmasına karşı herhangi bir tepki oluşmaz (Slayt 22).",
            "celdirici_analizi": "Pinna refleksi kedi, kobay ve tavşanda cerrahi derinliğin hassas testidir."
        },
        "slayt_no": 22,
        "zorluk_derecesi": "kolay",
        "etiketler": ["kulak_refleksi", "kedi_kobay_tavsan"]
    },
    {
        "soru_id": "mcq_gan_049",
        "soru_metni": "Endotrakeal entübasyon uygulamasının anestezinin III. Dönem 1. Planında güvenle yapılabilmesi ancak ameliyatın yapılamaması hangi iki refleks durumunun sonucudur?",
        "secenekler": {
            "A": "Yutkunma refleksinin azalmış olması (tüp takılır) / Palpebral refleks ve ağrı duyusunun sürmesi (ameliyat yapılamaz)",
            "B": "Korneal refleksin artması / Kalp atımının durması",
            "C": "Pupillanın tamamen körleşmesi / Diyaframın felç olması",
            "D": "Pedal refleksin aşırı artması / Dilin şişmesi"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; yutkunma azaldığı için tüp takılır, ancak palpebral refleks mevcut olup ağrı duyulduğu için cerrahi tolere edilemez (Slayt 9).",
            "celdirici_analizi": "Slayt 9'daki kritik klinik ayrımın mantığıdır."
        },
        "slayt_no": 9,
        "zorluk_derecesi": "zor",
        "etiketler": ["entubasyon", "plan1", "refleksler"]
    },
    {
        "soru_id": "mcq_gan_050",
        "soru_metni": "Aşağıdaki klinik tablolardan hangisi III. Dönem 4. Plandaki bir hastada DOĞRUDUR?",
        "secenekler": {
            "A": "Göz küresi ventrale kaymıştır ve gözyaşı çok fazladır",
            "B": "Kasların tonusu tamamen yok olmuştur, kornea kurudur, CRT uzamıştır ve kardiyak arrest riski vardır",
            "C": "Solunum son derece düzenli ve derinleşmiştir",
            "D": "Hasta hafif cerrahi uyaranlara karşı ekstremitelerini çeker"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; kas tonusu sıfır, kornea kuru, CRT uzamış, mukozalar solgun ve arrest riski vardır (Slayt 12).",
            "celdirici_analizi": "A, C ve D şıkları hafif veya orta düzey anestezi bulgularıdır."
        },
        "slayt_no": 12,
        "zorluk_derecesi": "orta",
        "etiketler": ["plan4", "doz_asimi"]
    },
    {
        "soru_id": "mcq_gan_051",
        "soru_metni": "Genel anestezide 'Anestezinin başlaması reflekslerin ortadan kalkması (yutkunma) ile karakterizedir' ifadesi sunumun hangi slaytında vurgulanmaktadır?",
        "secenekler": {
            "A": "Slayt 1",
            "B": "Slayt 3",
            "C": "Slayt 13",
            "D": "Slayt 22"
        },
        "dogru_cevap": "B",
        "aciklama": {
            "genel": "B seçeneği doğrudur; indüksiyon konusu anlatılırken Slayt 3'ün son maddesinde bu kural belirtilmektedir (Slayt 3).",
            "celdirici_analizi": "Slayt 3 indüksiyon ve anestezinin başlamasını anlatır."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "orta",
        "etiketler": ["slayt_bilgisi", "yutkunma"]
    },
    {
        "soru_id": "mcq_gan_052",
        "soru_metni": "Atlarda anestezi takibinde korneal refleks ile palpebral refleksin karşılaştırılmasına ilişkin hangisi doğrudur?",
        "secenekler": {
            "A": "Palpebral refleks derin anestezide kalırken, korneal refleks hemen kaybolur",
            "B": "Her iki refleks de 1. dönemde tamamen kaybolur",
            "C": "Palpebral refleks orta derecede derin anestezide oldukça azalır ya da yok olurken, korneal refleks derin anestezide bile hala mevcuttur",
            "D": "Atlarda palpebral ve korneal refleks hiçbir zaman tespit edilemez"
        },
        "dogru_cevap": "C",
        "aciklama": {
            "genel": "C seçeneği doğrudur; palpebral refleks orta derecede derin anestezide azalır/yok olur, ancak atlarda korneal refleks derin anestezide bile hala mevcuttur (Slayt 19).",
            "celdirici_analizi": "Slayt 19'daki net fizyolojik ayrımdır."
        },
        "slayt_no": 19,
        "zorluk_derecesi": "zor",
        "etiketler": ["at", "korneal_vs_palpebral"]
    },
    {
        "soru_id": "mcq_gan_053",
        "soru_metni": "Genel anestezi indüksiyonunun başında hayvanlarda geçici olarak oluşabilen motor huzursuzluk hali aşağıdakilerden hangisidir?",
        "secenekler": {
            "A": "Eksitasyon",
            "B": "Katalepsi",
            "C": "Senkop",
            "D": "Koma"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; indüksiyonun başlangıcında hayvanlarda eksitasyon oluşabilir, ardından gevşeme ve bilinçsizlik alır (Slayt 3).",
            "celdirici_analizi": "Katalepsi dissosiyatiflere özgüdür; senkop bayılmadır; koma patolojiktir."
        },
        "slayt_no": 3,
        "zorluk_derecesi": "kolay",
        "etiketler": ["eksitasyon", "induksiyon"]
    },
    {
        "soru_id": "mcq_gan_054",
        "soru_metni": "Enjektabl anestezik ilaçların vücuttan nihai atılım yolu esas olarak hangisidir?",
        "secenekler": {
            "A": "Karaciğer enzimleri tarafından metabolize edilip böbrek/üriner sistem yoluyla atılır",
            "B": "Tamamen tükürük bezlerinden salgılanır",
            "C": "Yalnızca deri yoluyla terle atılır",
            "D": "Alveollerden gaz fazında solunarak atılır"
        },
        "dogru_cevap": "A",
        "aciklama": {
            "genel": "A seçeneği doğrudur; karaciğer enzimleri tarafından metabolize edilir ve metabolitler üriner sistemle vücut dışına atılır (Slayt 5).",
            "celdirici_analizi": "Alveollerden atılım inhalasyon anesteziklerine aittir."
        },
        "slayt_no": 5,
        "zorluk_derecesi": "kolay",
        "etiketler": ["enjektabl", "eliminasyon"]
    },
    {
        "soru_id": "mcq_gan_055",
        "soru_metni": "Anestezide göz işaretleri olarak aşağıdakilerden hangisi rutin klinik değerlendirmeye ALINMAZ?",
        "secenekler": {
            "A": "Gözün pozisyonu ve hareketleri",
            "B": "Pupilla ölçüleri ve ışığa karşı tepkisi",
            "C": "Lakrimasyon, palpebral, korneal ve konjuktival refleksler",
            "D": "İrisin renginin genetik analizi"
        },
        "dogru_cevap": "D",
        "aciklama": {
            "genel": "D seçeneği anestezi derinliği takibinde bir kriter değildir (Slayt 17).",
            "celdirici_analizi": "A, B ve C seçeneklerinin tümü slayt 17'de sıralanan temel göz parametreleridir."
        },
        "slayt_no": 17,
        "zorluk_derecesi": "kolay",
        "etiketler": ["goz_isaretleri", "muayene"]
    }
]

print(f"Genel Anestezi modülü hazırlandı:")
print(f"- Summary Sections: {len(SUMMARY_SECTIONS)}")
print(f"- Bilgi Kartları: {len(BILGI_KARTLARI)}")
print(f"- Açık Uçlu Sorular: {len(ACIK_UCLU_SORULAR)}")
print(f"- Çoktan Seçmeli Sorular: {len(COKTAN_SECMELI_SORULAR)}")
