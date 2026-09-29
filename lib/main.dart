import 'package:flutter/material.dart';
import 'screens/splash_screen.dart';
import 'theme/app_theme.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const VetMeriApp());
}

class VetMeriApp extends StatelessWidget {
  const VetMeriApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'VetMeri',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      home: const SplashScreen(),
    );
  }
}
