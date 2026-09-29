import 'package:flutter/material.dart';

class AppTheme {
  // Soft, warm, pastel palette (warm cream, soft sage, warm blush/terracotta)
  static const Color background = Color(0xFFF9F7F2);
  static const Color cardBg = Color(0xFFFFFFFF);
  static const Color primary = Color(0xFF4A7C59); // Soft elegant sage green
  static const Color primaryLight = Color(0xFFE8F1EC);
  static const Color success = Color(0xFF4A7C59);
  static const Color successLight = Color(0xFFE8F1EC);
  static const Color accent = Color(0xFFD97757); // Warm gentle terracotta / blush
  static const Color accentLight = Color(0xFFFDF0EC);
  static const Color danger = Color(0xFFC95D63);
  static const Color dangerLight = Color(0xFFFBEBED);
  
  static const Color textDark = Color(0xFF2C3539);
  static const Color textMedium = Color(0xFF5A646A);
  static const Color textLight = Color(0xFF8C969E);
  
  static const Color borderSubtle = Color(0xFFEAE5DC);

  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      scaffoldBackgroundColor: background,
      colorScheme: ColorScheme.light(
        surface: cardBg,
        primary: primary,
        secondary: accent,
        error: danger,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: background,
        elevation: 0,
        scrolledUnderElevation: 0,
        centerTitle: true,
        titleTextStyle: TextStyle(
          color: textDark,
          fontSize: 18,
          fontWeight: FontWeight.w700,
          letterSpacing: -0.2,
        ),
        iconTheme: IconThemeData(color: textDark),
      ),
      cardTheme: CardThemeData(
        color: cardBg,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: const BorderSide(color: borderSubtle, width: 1.2),
        ),
      ),
      bottomNavigationBarTheme: const BottomNavigationBarThemeData(
        backgroundColor: cardBg,
        selectedItemColor: primary,
        unselectedItemColor: textLight,
        selectedLabelStyle: TextStyle(fontWeight: FontWeight.w700, fontSize: 12),
        unselectedLabelStyle: TextStyle(fontWeight: FontWeight.w600, fontSize: 12),
        type: BottomNavigationBarType.fixed,
        elevation: 8,
      ),
    );
  }
}
