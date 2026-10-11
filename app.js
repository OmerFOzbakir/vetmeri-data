// VetMeri - İnteraktif Veteriner Çalışma Asistanı
// Kümülatif Çoklu Modül Yönetimi

document.addEventListener('DOMContentLoaded', () => {
  const allModules = window.ALL_MODULES || {
    "sindirim": window.MODULE_DATA
  };

  const moduleSelector = document.getElementById('module-selector');
  const headerCategory = document.getElementById('header-category');
  const brandLogoIcon = document.getElementById('brand-logo-icon');
  const heroBadge = document.getElementById('hero-badge');
  const heroTitle = document.getElementById('hero-title');
  const heroDesc = document.getElementById('hero-desc');

  // Kaydedilmiş son aktif modülü yükle
  let currentModuleKey = localStorage.getItem('vetmeri_active_module') || 'monitorizasyon';
  if (!allModules[currentModuleKey] && currentModuleKey !== 'hepsi') {
    currentModuleKey = 'monitorizasyon';
  }
  if (moduleSelector) {
    moduleSelector.value = currentModuleKey;
  }

  // Aktif modül verisini al veya kümülatif havuz oluştur
  function getActiveData() {
    if (currentModuleKey === 'hepsi') {
      const anestezi = allModules['anestezi'] || {};
      const preanestezi = allModules['preanestezi'] || {};
      const sindirim = allModules['sindirim'] || {};
      const genel_anestezi = allModules['genel_anestezi'] || {};
      const ekipmanlar = allModules['ekipmanlar'] || {};
      const inhalasyon = allModules['inhalasyon'] || {};
      const monitorizasyon = allModules['monitorizasyon'] || {};
      return {
        id: 'hepsi',
        name: 'Tüm Konular (Kümülatif Havuz)',
        shortName: 'Kümülatif Soru Havuzu',
        icon: '📚',
        badge: '458 Slayt • 505 Soru • 7 Ders Bir Arada',
        kategori: 'Veteriner Hekimlik',
        alt_kategori: 'Kümülatif Sınav Hazırlığı',
        ozet: 'Anesteziye Giriş (38 Slayt), Preanestezik İlaçlar (74 Slayt), Sindirim Sistemi Hastalıkları (240 Slayt), Genel Anestezi (22 Slayt), Anestezi Ekipmanları (25 Slayt), İnhalasyon Anestezikleri (24 Slayt) ve Hasta Monitörizasyonu (35 Slayt) derslerinin tüm soru ve bilgi kartlarını içeren birleşik çalışma havuzu.',
        summarySections: [
          ...(monitorizasyon.summarySections || []).map(s => ({ ...s, title: `[Monitörizasyon] ${s.title}` })),
          ...(inhalasyon.summarySections || []).map(s => ({ ...s, title: `[İnhalasyon] ${s.title}` })),
          ...(ekipmanlar.summarySections || []).map(s => ({ ...s, title: `[Ekipmanlar] ${s.title}` })),
          ...(genel_anestezi.summarySections || []).map(s => ({ ...s, title: `[Genel Anestezi] ${s.title}` })),
          ...(sindirim.summarySections || []).map(s => ({ ...s, title: `[Sindirim] ${s.title}` })),
          ...(preanestezi.summarySections || []).map(s => ({ ...s, title: `[Preanestezi] ${s.title}` })),
          ...(anestezi.summarySections || []).map(s => ({ ...s, title: `[Anestezi] ${s.title}` }))
        ],
        bilgi_kartlari: [
          ...(monitorizasyon.bilgi_kartlari || []),
          ...(inhalasyon.bilgi_kartlari || []),
          ...(ekipmanlar.bilgi_kartlari || []),
          ...(genel_anestezi.bilgi_kartlari || []),
          ...(sindirim.bilgi_kartlari || []),
          ...(preanestezi.bilgi_kartlari || []),
          ...(anestezi.bilgi_kartlari || [])
        ],
        acik_uclu_sorular: [
          ...(monitorizasyon.acik_uclu_sorular || []),
          ...(inhalasyon.acik_uclu_sorular || []),
          ...(ekipmanlar.acik_uclu_sorular || []),
          ...(genel_anestezi.acik_uclu_sorular || []),
          ...(sindirim.acik_uclu_sorular || []),
          ...(preanestezi.acik_uclu_sorular || []),
          ...(anestezi.acik_uclu_sorular || [])
        ],
        coktan_secmeli_sorular: [
          ...(monitorizasyon.coktan_secmeli_sorular || []),
          ...(inhalasyon.coktan_secmeli_sorular || []),
          ...(ekipmanlar.coktan_secmeli_sorular || []),
          ...(genel_anestezi.coktan_secmeli_sorular || []),
          ...(sindirim.coktan_secmeli_sorular || []),
          ...(preanestezi.coktan_secmeli_sorular || []),
          ...(anestezi.coktan_secmeli_sorular || [])
        ]
      };
    }
    return allModules[currentModuleKey] || allModules['monitorizasyon'] || allModules['inhalasyon'] || allModules['ekipmanlar'] || allModules['genel_anestezi'] || allModules['sindirim'] || window.MODULE_DATA;
  }

  let activeData = getActiveData();

  // Tab Switching
  const navBtns = document.querySelectorAll('.bottom-nav .nav-item');
  const tabScreens = document.querySelectorAll('.tab-screen');

  function switchTab(tabName) {
    navBtns.forEach(btn => btn.classList.toggle('active', btn.dataset.tab === tabName));
    tabScreens.forEach(sc => sc.classList.toggle('active', sc.id === `tab-${tabName}`));
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => switchTab(btn.dataset.tab));
  });

  // UI Header & Hero Güncelleme
  function updateHeaderAndHero() {
    if (headerCategory) headerCategory.textContent = activeData.shortName || activeData.kategori;
    if (brandLogoIcon) brandLogoIcon.textContent = activeData.icon || '🐾';
    if (heroBadge) heroBadge.textContent = activeData.badge || 'Ders Notu Özeti';
    if (heroTitle) heroTitle.textContent = activeData.name || activeData.alt_kategori;
    if (heroDesc) heroDesc.textContent = activeData.ozet;
  }

  // ================= 1. TAB: ÖZET EKRANI =================
  const summaryContainer = document.getElementById('summary-sections-container');
  function renderSummary() {
    if (!summaryContainer) return;
    summaryContainer.innerHTML = '';
    const sections = activeData.summarySections || [];
    sections.forEach(sec => {
      const card = document.createElement('div');
      card.className = 'summary-section-card';
      card.innerHTML = `
        <div class="summary-section-title">
          <span>${sec.icon || '📌'}</span>
          <span>${sec.title}</span>
        </div>
        <div class="summary-bullets">
          ${(sec.points || []).map(p => `
            <div class="summary-bullet">
              <div class="bullet-dot"></div>
              <div>${p}</div>
            </div>
          `).join('')}
        </div>
      `;
      summaryContainer.appendChild(card);
    });
  }

  // ================= 2. TAB: BİLGİ KARTLARI =================
  let cards = [];
  let cardIdx = 0;
  const flipCardEl = document.getElementById('flip-card-element');
  const flashcardBox = document.getElementById('flashcard-box');
  const cardFrontText = document.getElementById('card-front-text');
  const cardBackText = document.getElementById('card-back-text');
  const cardCounter = document.getElementById('card-counter');
  const btnPrev = document.getElementById('btn-card-prev');
  const btnNext = document.getElementById('btn-card-next');
  const btnShuffle = document.getElementById('btn-card-shuffle');

  function initCards() {
    cards = [...(activeData.bilgi_kartlari || [])];
    cardIdx = 0;
    renderCard();
  }

  function renderCard() {
    if (!cards.length) {
      if (cardFrontText) cardFrontText.textContent = "Bu modülde henüz bilgi kartı bulunmuyor.";
      if (cardBackText) cardBackText.textContent = "-";
      if (cardCounter) cardCounter.textContent = "Kart 0 / 0";
      return;
    }
    if (flipCardEl) flipCardEl.classList.remove('is-flipped');
    const cur = cards[cardIdx];
    if (cardFrontText) cardFrontText.textContent = cur.on_yuz;
    if (cardBackText) cardBackText.textContent = cur.arka_yuz;
    if (cardCounter) cardCounter.textContent = `Kart ${cardIdx + 1} / ${cards.length}`;
  }

  if (flashcardBox && flipCardEl) {
    flashcardBox.onclick = () => flipCardEl.classList.toggle('is-flipped');
  }

  if (btnNext) {
    btnNext.onclick = () => {
      if (!cards.length) return;
      cardIdx = (cardIdx + 1) % cards.length;
      renderCard();
    };
  }

  if (btnPrev) {
    btnPrev.onclick = () => {
      if (!cards.length) return;
      cardIdx = (cardIdx - 1 + cards.length) % cards.length;
      renderCard();
    };
  }

  if (btnShuffle) {
    btnShuffle.onclick = () => {
      if (!cards.length) return;
      cards.sort(() => Math.random() - 0.5);
      cardIdx = 0;
      renderCard();
    };
  }

  // ================= 3. TAB: QUIZ EKRANI =================
  let quizList = [];
  let quizIdx = 0;
  let quizAnswered = false;

  const quizCounter = document.getElementById('quiz-counter');
  const quizSlidePill = document.getElementById('quiz-slide-pill');
  const quizQuestionText = document.getElementById('quiz-question-text');
  const quizOptionsContainer = document.getElementById('quiz-options-container');
  const quizFeedbackDrawer = document.getElementById('quiz-feedback-drawer');
  const feedbackResultTitle = document.getElementById('feedback-result-title');
  const feedbackSlideBadge = document.getElementById('feedback-slide-badge');
  const feedbackGeneralText = document.getElementById('feedback-general-text');
  const feedbackDistractorText = document.getElementById('feedback-distractor-text');
  const quizNextBtn = document.getElementById('quiz-next-btn');

  function initQuiz() {
    quizList = [...(activeData.coktan_secmeli_sorular || [])];
    quizIdx = 0;
    renderQuiz();
  }

  function renderQuiz() {
    quizAnswered = false;
    if (quizFeedbackDrawer) quizFeedbackDrawer.className = 'feedback-box';
    if (quizNextBtn) quizNextBtn.style.display = 'none';

    if (!quizList.length) {
      if (quizCounter) quizCounter.textContent = "Soru 0 / 0";
      if (quizQuestionText) quizQuestionText.textContent = "Bu modülde henüz soru bulunmuyor.";
      if (quizOptionsContainer) quizOptionsContainer.innerHTML = '';
      return;
    }

    const cur = quizList[quizIdx];
    const sNo = cur.slayt_no || cur.slideNumber || 1;
    if (quizCounter) quizCounter.textContent = `Soru ${quizIdx + 1} / ${quizList.length}`;
    if (quizSlidePill) quizSlidePill.textContent = `Slayt ${sNo}`;
    if (quizQuestionText) quizQuestionText.textContent = cur.soru_metni || cur.question;

    if (quizOptionsContainer) {
      quizOptionsContainer.innerHTML = '';
      const opts = cur.secenekler || cur.options || {};
      Object.keys(opts).forEach(letter => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.dataset.letter = letter;
        btn.innerHTML = `
          <div class="opt-letter">${letter}</div>
          <div style="flex:1;">${opts[letter]}</div>
        `;
        btn.onclick = () => selectOption(letter, cur);
        quizOptionsContainer.appendChild(btn);
      });
    }
  }

  function selectOption(selectedLetter, currentQ) {
    if (quizAnswered) return;
    quizAnswered = true;

    const correctAns = currentQ.dogru_cevap || currentQ.correctAnswer;
    const isCorrect = selectedLetter === correctAns;
    const btns = quizOptionsContainer.querySelectorAll('.option-btn');

    btns.forEach(btn => {
      const ltr = btn.dataset.letter;
      if (ltr === correctAns) {
        btn.classList.add('is-correct');
      }
      if (ltr === selectedLetter && !isCorrect) {
        btn.classList.add('is-wrong');
      }
    });

    const sNo = currentQ.slayt_no || currentQ.slideNumber || 1;
    if (feedbackResultTitle) feedbackResultTitle.textContent = isCorrect ? "Doğru Yanıt! 👏" : "Yanlış Yanıt!";
    if (feedbackSlideBadge) feedbackSlideBadge.textContent = `📌 Ders Notu: Slayt ${sNo}`;
    if (quizFeedbackDrawer) quizFeedbackDrawer.className = `feedback-box show ${isCorrect ? 'correct' : 'wrong'}`;

    const genDesc = currentQ.aciklama ? currentQ.aciklama.genel : (currentQ.explanation || "");
    const disDesc = currentQ.aciklama ? currentQ.aciklama.celdirici_analizi : (currentQ.distractorAnalysis || "");

    if (feedbackGeneralText) feedbackGeneralText.textContent = genDesc;
    if (feedbackDistractorText) feedbackDistractorText.innerHTML = `<strong>Çeldirici Analizi:</strong> ${disDesc}`;
    if (quizNextBtn) quizNextBtn.style.display = 'block';
  }

  if (quizNextBtn) {
    quizNextBtn.onclick = () => {
      if (!quizList.length) return;
      quizIdx = (quizIdx + 1) % quizList.length;
      renderQuiz();
    };
  }

  // ================= 4. TAB: KLASİK SORULAR =================
  let auList = [];
  let auIdx = 0;

  const auCounter = document.getElementById('au-counter');
  const auSlidePill = document.getElementById('au-slide-pill');
  const auQuestionText = document.getElementById('au-question-text');
  const btnRevealAu = document.getElementById('btn-reveal-au');
  const auAnswerBox = document.getElementById('au-answer-box');
  const auIdealAnswer = document.getElementById('au-ideal-answer');
  const auAnswerSlide = document.getElementById('au-answer-slide');
  const btnAuPrev = document.getElementById('btn-au-prev');
  const btnAuNext = document.getElementById('btn-au-next');

  function initAu() {
    auList = [...(activeData.acik_uclu_sorular || [])];
    auIdx = 0;
    renderAu();
  }

  function renderAu() {
    if (!auList.length) {
      if (auCounter) auCounter.textContent = "Klasik Soru 0 / 0";
      if (auQuestionText) auQuestionText.textContent = "Bu modülde henüz klasik soru bulunmuyor.";
      if (auIdealAnswer) auIdealAnswer.textContent = "-";
      return;
    }
    const cur = auList[auIdx];
    const sNo = cur.slayt_no || cur.slideNumber || (auIdx + 1);
    if (auCounter) auCounter.textContent = `Klasik Soru ${auIdx + 1} / ${auList.length}`;
    if (auSlidePill) auSlidePill.textContent = `Slayt ${sNo}`;
    if (auQuestionText) auQuestionText.textContent = cur.soru || cur.question;
    if (auAnswerSlide) auAnswerSlide.textContent = `📌 Slayt ${sNo}`;
    if (auIdealAnswer) auIdealAnswer.textContent = cur.ideal_cevap || cur.idealAnswer;
    if (auAnswerBox) auAnswerBox.classList.remove('show');
    if (btnRevealAu) btnRevealAu.textContent = "👁️ Cevabı Göster";
  }

  if (btnRevealAu && auAnswerBox) {
    btnRevealAu.onclick = () => {
      const isShowing = auAnswerBox.classList.toggle('show');
      btnRevealAu.textContent = isShowing ? "Cevabı Gizle" : "👁️ Cevabı Göster";
    };
  }

  if (btnAuNext) {
    btnAuNext.onclick = () => {
      if (!auList.length) return;
      auIdx = (auIdx + 1) % auList.length;
      renderAu();
    };
  }

  if (btnAuPrev) {
    btnAuPrev.onclick = () => {
      if (!auList.length) return;
      auIdx = (auIdx - 1 + auList.length) % auList.length;
      renderAu();
    };
  }

  // ================= MODÜL DEĞİŞTİRME ETKİNLİĞİ =================
  function reloadModule(newKey) {
    currentModuleKey = newKey;
    localStorage.setItem('vetmeri_active_module', newKey);
    activeData = getActiveData();

    updateHeaderAndHero();
    renderSummary();
    initCards();
    initQuiz();
    initAu();
  }

  if (moduleSelector) {
    moduleSelector.addEventListener('change', (e) => {
      reloadModule(e.target.value);
    });
  }

  // İlk yükleme
  updateHeaderAndHero();
  renderSummary();
  initCards();
  initQuiz();
  initAu();
});
