import 'dart:async';
import 'package:flutter/material.dart';
import '../data/remote_data_service.dart';
import '../data/course_repository.dart';
import '../models/study_models.dart';
import '../theme/app_theme.dart';
import 'home_screen.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _fadeAnimation;

  String _statusText = 'Dersler yükleniyor...';
  bool _hasError = false;
  List<CourseLesson>? _lessons;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 700),
    );

    _fadeAnimation = CurvedAnimation(
      parent: _controller,
      curve: Curves.easeIn,
    );

    _controller.forward();
    _loadData();
  }

  Future<void> _loadData() async {
    try {
      final lessons = await RemoteDataService.fetchLessons();
      if (mounted) {
        setState(() {
          _lessons = lessons;
          _statusText = 'Hazır! ✓';
        });
        // Kısa bir bekleme sonra geç
        await Future.delayed(const Duration(milliseconds: 600));
        if (mounted) _navigateToHome(lessons);
      }
    } catch (e) {
      // İnternet yoksa veya hata olursa yerel verilerle devam et
      if (mounted) {
        setState(() {
          _hasError = true;
          _statusText = 'Bağlantı yok, yerel veriler kullanılıyor...';
        });
        await Future.delayed(const Duration(milliseconds: 1200));
        if (mounted) _navigateToHome(CourseRepository.lessons);
      }
    }
  }

  void _navigateToHome(List<CourseLesson> lessons) {
    Navigator.of(context).pushReplacement(
      PageRouteBuilder(
        pageBuilder: (context, animation, secondaryAnimation) =>
            HomeScreen(lessons: lessons),
        transitionsBuilder: (context, animation, secondaryAnimation, child) {
          return FadeTransition(opacity: animation, child: child);
        },
        transitionDuration: const Duration(milliseconds: 300),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    return Scaffold(
      backgroundColor: AppTheme.background,
      body: SafeArea(
        child: FadeTransition(
          opacity: _fadeAnimation,
          child: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
            child: ConstrainedBox(
              constraints: BoxConstraints(
                minHeight: size.height -
                    MediaQuery.of(context).padding.top -
                    MediaQuery.of(context).padding.bottom -
                    32,
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Üst Kısım: Logo ve VetMeri Başlığı
                  Column(
                    children: [
                      const SizedBox(height: 12),
                      Container(
                        width: 72,
                        height: 72,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          border:
                              Border.all(color: AppTheme.primary, width: 2),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.black.withValues(alpha: 0.06),
                              blurRadius: 10,
                              offset: const Offset(0, 3),
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
                      const SizedBox(height: 10),
                      const Text(
                        "VetMeri",
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.w800,
                          color: AppTheme.textDark,
                          letterSpacing: -0.3,
                        ),
                      ),
                    ],
                  ),

                  const SizedBox(height: 16),

                  // Orta Kısım: Fotoğraf
                  Container(
                    constraints: BoxConstraints(
                      maxHeight: size.height * 0.50,
                      maxWidth: 320,
                    ),
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(24),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withValues(alpha: 0.08),
                          blurRadius: 20,
                          offset: const Offset(0, 6),
                        ),
                      ],
                    ),
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(24),
                      child: Image.asset(
                        "assets/images/meri_splash.png",
                        fit: BoxFit.cover,
                        width: double.infinity,
                      ),
                    ),
                  ),

                  const SizedBox(height: 20),

                  // Alt Kısım: Yükleniyor göstergesi
                  Padding(
                    padding: const EdgeInsets.only(bottom: 8),
                    child: Column(
                      children: [
                        if (!_hasError && _lessons == null)
                          const SizedBox(
                            width: 24,
                            height: 24,
                            child: CircularProgressIndicator(
                              strokeWidth: 2.5,
                              color: AppTheme.primary,
                            ),
                          ),
                        if (_hasError)
                          Icon(
                            Icons.wifi_off_rounded,
                            color: AppTheme.primary.withValues(alpha: 0.6),
                            size: 24,
                          ),
                        if (_lessons != null && !_hasError)
                          const Icon(
                            Icons.check_circle_rounded,
                            color: Colors.green,
                            size: 24,
                          ),
                        const SizedBox(height: 10),
                        Text(
                          _statusText,
                          style: TextStyle(
                            fontSize: 13,
                            color: _hasError
                                ? AppTheme.textMedium
                                : AppTheme.primary,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
