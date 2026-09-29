import 'package:flutter/material.dart';
import '../models/study_models.dart';
import '../theme/app_theme.dart';
import 'summary_screen.dart';
import 'flashcards_screen.dart';
import 'quiz_screen.dart';
import 'open_ended_screen.dart';

class HomeScreen extends StatefulWidget {
  final List<CourseLesson> lessons;

  const HomeScreen({super.key, required this.lessons});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentTabIndex = 0;
  int _selectedLessonIndex = 0;

  final List<String> _titles = const [
    "Ders Özeti",
    "Bilgi Kartları",
    "Konu Testi",
    "Klasik Sorular",
  ];

  @override
  Widget build(BuildContext context) {
    final activeLesson = widget.lessons[_selectedLessonIndex];

    return Scaffold(
      appBar: AppBar(
        title: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            // Kedi Logosu (Avatar)
            Container(
              width: 34,
              height: 34,
              margin: const EdgeInsets.only(right: 10),
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                border: Border.all(color: AppTheme.primary, width: 1.6),
                boxShadow: [
                  BoxShadow(
                    color: AppTheme.primary.withValues(alpha: 0.15),
                    blurRadius: 6,
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              child: ClipOval(
                child: Image.asset(
                  "assets/images/cat_logo.png",
                  fit: BoxFit.cover,
                ),
              ),
            ),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  "VetMeri",
                  style: TextStyle(
                    fontSize: 17,
                    fontWeight: FontWeight.w800,
                    color: AppTheme.textDark,
                    letterSpacing: -0.3,
                  ),
                ),
                Text(
                  _titles[_currentTabIndex],
                  style: const TextStyle(
                    fontSize: 11,
                    fontWeight: FontWeight.w600,
                    color: AppTheme.primary,
                  ),
                ),
              ],
            ),
          ],
        ),
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(56),
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
            child: Container(
              padding: const EdgeInsets.all(4),
              decoration: BoxDecoration(
                color: const Color(0xFFF0EDE6),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: AppTheme.borderSubtle),
              ),
              child: Row(
                children: List.generate(widget.lessons.length, (index) {
                  final lesson = widget.lessons[index];
                  final isSelected = _selectedLessonIndex == index;

                  // Kısa etiket: icon + title'ın ilk kısmı
                  final shortLabel = lesson.title.length > 20
                      ? '${lesson.title.substring(0, 20)}…'
                      : lesson.title;

                  return Expanded(
                    child: GestureDetector(
                      onTap: () {
                        if (_selectedLessonIndex != index) {
                          setState(() {
                            _selectedLessonIndex = index;
                            _currentTabIndex = 0;
                          });
                        }
                      },
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 200),
                        padding: const EdgeInsets.symmetric(vertical: 8),
                        decoration: BoxDecoration(
                          color: isSelected ? Colors.white : Colors.transparent,
                          borderRadius: BorderRadius.circular(12),
                          boxShadow: isSelected
                              ? [
                                  BoxShadow(
                                    color: Colors.black.withValues(alpha: 0.05),
                                    blurRadius: 6,
                                    offset: const Offset(0, 2),
                                  ),
                                ]
                              : null,
                        ),
                        alignment: Alignment.center,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Text(
                              lesson.icon,
                              style: const TextStyle(fontSize: 13),
                            ),
                            const SizedBox(width: 6),
                            Flexible(
                              child: Text(
                                shortLabel,
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                                style: TextStyle(
                                  fontSize: 12,
                                  fontWeight: isSelected
                                      ? FontWeight.w800
                                      : FontWeight.w600,
                                  color: isSelected
                                      ? AppTheme.primary
                                      : AppTheme.textMedium,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  );
                }),
              ),
            ),
          ),
        ),
      ),
      body: IndexedStack(
        key: ValueKey("lesson_$_selectedLessonIndex"),
        index: _currentTabIndex,
        children: [
          SummaryScreen(lesson: activeLesson),
          FlashcardsScreen(lesson: activeLesson),
          QuizScreen(lesson: activeLesson),
          OpenEndedScreen(lesson: activeLesson),
        ],
      ),
      bottomNavigationBar: Container(
        decoration: const BoxDecoration(
          border: Border(
            top: BorderSide(color: AppTheme.borderSubtle, width: 1),
          ),
        ),
        child: BottomNavigationBar(
          currentIndex: _currentTabIndex,
          onTap: (index) {
            setState(() {
              _currentTabIndex = index;
            });
          },
          items: const [
            BottomNavigationBarItem(
              icon: Icon(Icons.menu_book_rounded),
              activeIcon: Icon(Icons.menu_book_rounded),
              label: "Özet",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.style_outlined),
              activeIcon: Icon(Icons.style_rounded),
              label: "Kartlar",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.check_circle_outline_rounded),
              activeIcon: Icon(Icons.check_circle_rounded),
              label: "Test",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.edit_note_rounded),
              activeIcon: Icon(Icons.edit_note_rounded),
              label: "Klasik",
            ),
          ],
        ),
      ),
    );
  }
}
