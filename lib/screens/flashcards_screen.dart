import 'dart:math';
import 'package:flutter/material.dart';
import '../models/study_models.dart';
import '../theme/app_theme.dart';

class FlashcardsScreen extends StatefulWidget {
  final CourseLesson lesson;

  const FlashcardsScreen({
    super.key,
    required this.lesson,
  });

  @override
  State<FlashcardsScreen> createState() => _FlashcardsScreenState();
}

class _FlashcardsScreenState extends State<FlashcardsScreen> with SingleTickerProviderStateMixin {
  late List<FlashcardItem> _cards;
  int _currentIndex = 0;
  bool _showBack = false;

  late AnimationController _flipController;
  late Animation<double> _flipAnimation;

  @override
  void initState() {
    super.initState();
    _cards = List.from(widget.lesson.flashcards);
    _flipController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 350),
    );
    _flipAnimation = Tween<double>(begin: 0, end: 1).animate(
      CurvedAnimation(parent: _flipController, curve: Curves.easeInOut),
    );
  }

  @override
  void didUpdateWidget(covariant FlashcardsScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.lesson.id != widget.lesson.id) {
      if (_showBack) {
        _flipController.reset();
        _showBack = false;
      }
      setState(() {
        _cards = List.from(widget.lesson.flashcards);
        _currentIndex = 0;
      });
    }
  }

  @override
  void dispose() {
    _flipController.dispose();
    super.dispose();
  }

  void _toggleFlip() {
    if (_showBack) {
      _flipController.reverse();
    } else {
      _flipController.forward();
    }
    setState(() {
      _showBack = !_showBack;
    });
  }

  void _nextCard() {
    if (_showBack) {
      _flipController.reverse();
      _showBack = false;
    }
    setState(() {
      _currentIndex = (_currentIndex + 1) % _cards.length;
    });
  }

  void _prevCard() {
    if (_showBack) {
      _flipController.reverse();
      _showBack = false;
    }
    setState(() {
      _currentIndex = (_currentIndex - 1 + _cards.length) % _cards.length;
    });
  }

  void _shuffleCards() {
    if (_showBack) {
      _flipController.reverse();
      _showBack = false;
    }
    setState(() {
      _cards.shuffle(Random());
      _currentIndex = 0;
    });
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: const Text(
          "Kartlar karıştırıldı",
          style: TextStyle(fontWeight: FontWeight.w600),
        ),
        duration: const Duration(milliseconds: 1000),
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        backgroundColor: AppTheme.primary,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    if (_cards.isEmpty) {
      return const Center(child: Text("Bu derste henüz kart bulunmuyor."));
    }

    final card = _cards[_currentIndex];

    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
      children: [
        // Soru Sayacı & Karıştır Butonu
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              "Kart ${_currentIndex + 1} / ${_cards.length}",
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: AppTheme.textMedium,
              ),
            ),
            IconButton(
              onPressed: _shuffleCards,
              icon: const Icon(Icons.shuffle_rounded),
              tooltip: "Karıştır",
              color: AppTheme.primary,
            ),
          ],
        ),
        const SizedBox(height: 12),

        // Flip Card
        GestureDetector(
          onTap: _toggleFlip,
          child: AnimatedBuilder(
            animation: _flipAnimation,
            builder: (context, child) {
              final angle = _flipAnimation.value * pi;
              final isUnder = angle > pi / 2;

              return Transform(
                transform: Matrix4.identity()
                  ..setEntry(3, 2, 0.001) // perspective
                  ..rotateY(angle),
                alignment: Alignment.center,
                child: isUnder
                    ? Transform(
                        transform: Matrix4.identity()..rotateY(pi),
                        alignment: Alignment.center,
                        child: _buildCardFace(
                          title: "Cevap",
                          content: card.answer,
                          isAnswer: true,
                        ),
                      )
                    : _buildCardFace(
                        title: "Soru",
                        content: card.question,
                        isAnswer: false,
                      ),
              );
            },
          ),
        ),

        const SizedBox(height: 14),
        const Center(
          child: Text(
            "Cevabı görmek için karta dokunun",
            style: TextStyle(
              fontSize: 12.5,
              color: AppTheme.textLight,
              fontStyle: FontStyle.italic,
            ),
          ),
        ),

        const SizedBox(height: 20),

        // Navigasyon Butonları: Sadece Önceki ve Sonraki
        Row(
          children: [
            Expanded(
              child: OutlinedButton.icon(
                onPressed: _prevCard,
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
                onPressed: _nextCard,
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

  Widget _buildCardFace({
    required String title,
    required String content,
    required bool isAnswer,
  }) {
    return Container(
      width: double.infinity,
      constraints: const BoxConstraints(minHeight: 280),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: isAnswer ? const Color(0xFFF3F7F4) : AppTheme.cardBg,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(
          color: isAnswer ? AppTheme.primary.withValues(alpha: 0.35) : AppTheme.borderSubtle,
          width: isAnswer ? 1.5 : 1,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.04),
            blurRadius: 18,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
            decoration: BoxDecoration(
              color: isAnswer ? AppTheme.primaryLight : const Color(0xFFF0EDE6),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Text(
              title,
              style: TextStyle(
                fontSize: 12,
                fontWeight: FontWeight.w700,
                color: isAnswer ? AppTheme.primary : AppTheme.textMedium,
              ),
            ),
          ),
          const SizedBox(height: 20),
          Text(
            content,
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: isAnswer ? 15.5 : 17,
              fontWeight: isAnswer ? FontWeight.w500 : FontWeight.w700,
              color: AppTheme.textDark,
              height: 1.55,
            ),
          ),
        ],
      ),
    );
  }
}
