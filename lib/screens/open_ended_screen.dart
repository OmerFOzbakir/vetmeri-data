import 'package:flutter/material.dart';
import '../models/study_models.dart';
import '../theme/app_theme.dart';

class OpenEndedScreen extends StatefulWidget {
  final CourseLesson lesson;

  const OpenEndedScreen({
    super.key,
    required this.lesson,
  });

  @override
  State<OpenEndedScreen> createState() => _OpenEndedScreenState();
}

class _OpenEndedScreenState extends State<OpenEndedScreen> {
  late List<OpenEndedQuestionItem> _questions;
  int _currentIndex = 0;
  bool _showAnswer = false;

  @override
  void initState() {
    super.initState();
    _questions = List.from(widget.lesson.openEndedQuestions);
  }

  @override
  void didUpdateWidget(covariant OpenEndedScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.lesson.id != widget.lesson.id) {
      setState(() {
        _questions = List.from(widget.lesson.openEndedQuestions);
        _currentIndex = 0;
        _showAnswer = false;
      });
    }
  }

  void _nextQuestion() {
    setState(() {
      _showAnswer = false;
      _currentIndex = (_currentIndex + 1) % _questions.length;
    });
  }

  void _prevQuestion() {
    setState(() {
      _showAnswer = false;
      _currentIndex = (_currentIndex - 1 + _questions.length) % _questions.length;
    });
  }

  void _toggleAnswer() {
    setState(() {
      _showAnswer = !_showAnswer;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_questions.isEmpty) {
      return const Center(child: Text("Bu derste henüz klasik soru bulunmuyor."));
    }

    final question = _questions[_currentIndex];

    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
      children: [
        // Soru Sayacı & Slayt
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              "Klasik Soru ${_currentIndex + 1} / ${_questions.length}",
              style: const TextStyle(
                fontSize: 14.5,
                fontWeight: FontWeight.w700,
                color: AppTheme.textMedium,
              ),
            ),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
              decoration: BoxDecoration(
                color: const Color(0xFFF0EDE6),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Text(
                "Slayt ${question.slideNumber}",
                style: const TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.w700,
                  color: AppTheme.textMedium,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 14),

        // Soru Kartı
        Container(
          padding: const EdgeInsets.all(22),
          decoration: BoxDecoration(
            color: AppTheme.cardBg,
            borderRadius: BorderRadius.circular(22),
            border: Border.all(color: AppTheme.borderSubtle),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withValues(alpha: 0.03),
                blurRadius: 14,
                offset: const Offset(0, 4),
              )
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: AppTheme.primaryLight,
                  borderRadius: BorderRadius.circular(10),
                ),
                child: const Text(
                  "Sınav Sorusu",
                  style: TextStyle(
                    fontSize: 11.5,
                    fontWeight: FontWeight.w700,
                    color: AppTheme.primary,
                  ),
                ),
              ),
              const SizedBox(height: 14),
              Text(
                question.question,
                style: const TextStyle(
                  fontSize: 16.5,
                  fontWeight: FontWeight.w700,
                  color: AppTheme.textDark,
                  height: 1.45,
                ),
              ),
            ],
          ),
        ),

        const SizedBox(height: 16),

        // Cevabı Göster / Gizle Butonu
        InkWell(
          onTap: _toggleAnswer,
          borderRadius: BorderRadius.circular(18),
          child: Container(
            padding: const EdgeInsets.symmetric(vertical: 15),
            decoration: BoxDecoration(
              color: _showAnswer ? const Color(0xFFF3F7F4) : AppTheme.primaryLight,
              borderRadius: BorderRadius.circular(18),
              border: Border.all(
                color: _showAnswer ? AppTheme.primary : AppTheme.primary.withValues(alpha: 0.3),
              ),
            ),
            alignment: Alignment.center,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  _showAnswer ? Icons.visibility_off_outlined : Icons.visibility_outlined,
                  size: 20,
                  color: AppTheme.primary,
                ),
                const SizedBox(width: 8),
                Text(
                  _showAnswer ? "Cevabı Gizle" : "Cevabı Göster",
                  style: const TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w700,
                    color: AppTheme.primary,
                  ),
                ),
              ],
            ),
          ),
        ),

        // Açılan İdeal Cevap Kartı
        if (_showAnswer) ...[
          const SizedBox(height: 16),
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(22),
              border: Border.all(color: AppTheme.primary.withValues(alpha: 0.35), width: 1.4),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.03),
                  blurRadius: 14,
                  offset: const Offset(0, 4),
                )
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: AppTheme.primaryLight,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: const Text(
                        "İdeal Sınav Yanıtı",
                        style: TextStyle(
                          fontSize: 11.5,
                          fontWeight: FontWeight.w700,
                          color: AppTheme.primary,
                        ),
                      ),
                    ),
                    Text(
                      "📌 Slayt ${question.slideNumber}",
                      style: const TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        color: AppTheme.primary,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 14),
                Text(
                  question.idealAnswer,
                  style: const TextStyle(
                    fontSize: 14.5,
                    fontWeight: FontWeight.w500,
                    color: AppTheme.textDark,
                    height: 1.6,
                  ),
                ),
              ],
            ),
          ),
        ],

        const SizedBox(height: 20),

        // Navigasyon Butonları
        Row(
          children: [
            Expanded(
              child: OutlinedButton.icon(
                onPressed: _prevQuestion,
                icon: const Icon(Icons.arrow_back_rounded, size: 18),
                label: const Text("Önceki"),
                style: OutlinedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  side: const BorderSide(color: AppTheme.borderSubtle),
                  foregroundColor: AppTheme.textDark,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                ),
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: ElevatedButton.icon(
                onPressed: _nextQuestion,
                icon: const Icon(Icons.arrow_forward_rounded, size: 18),
                label: const Text("Sonraki"),
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  backgroundColor: AppTheme.primary,
                  foregroundColor: Colors.white,
                  elevation: 0,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 24),
      ],
    );
  }
}
