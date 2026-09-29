import 'package:flutter/material.dart';
import '../models/study_models.dart';
import '../theme/app_theme.dart';

class QuizScreen extends StatefulWidget {
  final CourseLesson lesson;

  const QuizScreen({
    super.key,
    required this.lesson,
  });

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  late List<QuizQuestionItem> _questions;
  int _currentIndex = 0;
  String? _selectedOption;
  bool _hasAnswered = false;

  @override
  void initState() {
    super.initState();
    _questions = List.from(widget.lesson.quizQuestions);
  }

  @override
  void didUpdateWidget(covariant QuizScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.lesson.id != widget.lesson.id) {
      setState(() {
        _questions = List.from(widget.lesson.quizQuestions);
        _currentIndex = 0;
        _selectedOption = null;
        _hasAnswered = false;
      });
    }
  }

  void _onOptionSelected(String letter) {
    if (_hasAnswered) return;
    setState(() {
      _selectedOption = letter;
      _hasAnswered = true;
    });
  }

  void _nextQuestion() {
    if (_currentIndex < _questions.length - 1) {
      setState(() {
        _currentIndex++;
        _selectedOption = null;
        _hasAnswered = false;
      });
    } else {
      // Başa dön
      setState(() {
        _currentIndex = 0;
        _selectedOption = null;
        _hasAnswered = false;
      });
    }
  }

  void _prevQuestion() {
    if (_currentIndex > 0) {
      setState(() {
        _currentIndex--;
        _selectedOption = null;
        _hasAnswered = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_questions.isEmpty) {
      return const Center(child: Text("Bu derste henüz soru bulunmuyor."));
    }

    final question = _questions[_currentIndex];

    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
      children: [
        // Soru Numarası
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              "Soru ${_currentIndex + 1} / ${_questions.length}",
              style: const TextStyle(
                fontSize: 15,
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

        // Soru Metni Kartı
        Container(
          padding: const EdgeInsets.all(20),
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
          child: Text(
            question.question,
            style: const TextStyle(
              fontSize: 16.5,
              fontWeight: FontWeight.w700,
              color: AppTheme.textDark,
              height: 1.45,
            ),
          ),
        ),

        const SizedBox(height: 16),

        // Şıklar
        ...question.options.entries.map((entry) {
          final letter = entry.key;
          final text = entry.value;
          final isSelected = _selectedOption == letter;
          final isCorrect = letter == question.correctAnswer;

          Color cardBg = AppTheme.cardBg;
          Color borderColor = AppTheme.borderSubtle;
          Color textColor = AppTheme.textDark;
          Color badgeBg = const Color(0xFFF0EDE6);
          Color badgeText = AppTheme.textDark;

          if (_hasAnswered) {
            if (isCorrect) {
              cardBg = const Color(0xFFEBF5EE);
              borderColor = AppTheme.success;
              textColor = const Color(0xFF1B4D2E);
              badgeBg = AppTheme.success;
              badgeText = Colors.white;
            } else if (isSelected) {
              cardBg = const Color(0xFFFDF2F0);
              borderColor = AppTheme.danger;
              textColor = const Color(0xFF6B1D14);
              badgeBg = AppTheme.danger;
              badgeText = Colors.white;
            }
          } else if (isSelected) {
            borderColor = AppTheme.primary;
          }

          return Container(
            margin: const EdgeInsets.only(bottom: 12),
            child: InkWell(
              onTap: () => _onOptionSelected(letter),
              borderRadius: BorderRadius.circular(18),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                decoration: BoxDecoration(
                  color: cardBg,
                  borderRadius: BorderRadius.circular(18),
                  border: Border.all(color: borderColor, width: isSelected || (_hasAnswered && isCorrect) ? 1.8 : 1),
                ),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Container(
                      width: 28,
                      height: 28,
                      margin: const EdgeInsets.only(right: 12, top: 1),
                      decoration: BoxDecoration(
                        color: badgeBg,
                        borderRadius: BorderRadius.circular(8),
                      ),
                      alignment: Alignment.center,
                      child: Text(
                        letter,
                        style: TextStyle(
                          fontSize: 13,
                          fontWeight: FontWeight.w800,
                          color: badgeText,
                        ),
                      ),
                    ),
                    Expanded(
                      child: Text(
                        text,
                        style: TextStyle(
                          fontSize: 14.5,
                          fontWeight: FontWeight.w500,
                          color: textColor,
                          height: 1.4,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        }),

        // Açıklama & Çeldirici Analizi Kartı
        if (_hasAnswered) ...[
          const SizedBox(height: 10),
          Container(
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              color: const Color(0xFFFAF6F0),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: AppTheme.accent.withValues(alpha: 0.3)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Icon(
                      _selectedOption == question.correctAnswer
                          ? Icons.check_circle_rounded
                          : Icons.info_outline_rounded,
                      size: 20,
                      color: _selectedOption == question.correctAnswer
                          ? AppTheme.success
                          : AppTheme.accent,
                    ),
                    const SizedBox(width: 8),
                    Text(
                      _selectedOption == question.correctAnswer ? "Doğru Yanıt" : "Yanıt Açıklaması",
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w700,
                        color: _selectedOption == question.correctAnswer
                            ? AppTheme.success
                            : AppTheme.accent,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 10),
                Text(
                  question.explanation,
                  style: const TextStyle(
                    fontSize: 13.5,
                    color: AppTheme.textDark,
                    height: 1.5,
                  ),
                ),
                const SizedBox(height: 10),
                Text(
                  question.distractorAnalysis,
                  style: const TextStyle(
                    fontSize: 13,
                    color: AppTheme.textMedium,
                    fontStyle: FontStyle.italic,
                    height: 1.45,
                  ),
                ),
                const SizedBox(height: 12),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(color: AppTheme.borderSubtle),
                  ),
                  child: Text(
                    "📌 Ders Notu: Slayt ${question.slideNumber}",
                    style: const TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w700,
                      color: AppTheme.primary,
                    ),
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
            if (_currentIndex > 0) ...[
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
            ],
            Expanded(
              child: ElevatedButton.icon(
                onPressed: _nextQuestion,
                icon: const Icon(Icons.arrow_forward_rounded, size: 18),
                label: Text(
                  _currentIndex == _questions.length - 1 ? "Başa Dön" : "Sonraki Soru",
                ),
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
