// Bu script, mevcut Dart data dosyalarını okuyup data.json üretir
// Çalıştırmak için: dart run tool/generate_json.dart

import 'dart:convert';
import 'dart:io';
import '../lib/data/anestezi_data.dart';
import '../lib/data/preanestezi_data.dart';

void main() {
  final lessons = [
    {
      'id': 'lesson_1',
      'title': '1. Ders: Anesteziye Giriş & Muayene',
      'subtitle': '38 Slayt • Preanestezik Değerlendirme, ASA & Fizyoloji',
      'icon': '🩺',
      'summarySections': AnesteziData.summarySections.map((s) => {
        'title': s.title,
        'icon': s.icon,
        'points': s.points,
      }).toList(),
      'flashcards': AnesteziData.flashcards.map((f) => {
        'id': f.id,
        'question': f.question,
        'answer': f.answer,
      }).toList(),
      'quizQuestions': AnesteziData.quizQuestions.map((q) => {
        'id': q.id,
        'question': q.question,
        'options': q.options,
        'correctAnswer': q.correctAnswer,
        'explanation': q.explanation,
        'distractorAnalysis': q.distractorAnalysis,
        'slideNumber': q.slideNumber,
      }).toList(),
      'openEndedQuestions': AnesteziData.openEndedQuestions.map((o) => {
        'id': o.id,
        'question': o.question,
        'idealAnswer': o.idealAnswer,
        'slideNumber': o.slideNumber,
      }).toList(),
    },
    {
      'id': 'lesson_2',
      'title': '2. Ders: Preanestezik İlaçlar & İndüksiyon',
      'subtitle': '74 Slayt • Atropin, Ksilazin, Ketamin, Tiyopental & Entübasyon',
      'icon': '💊',
      'summarySections': PreanesteziData.summarySections.map((s) => {
        'title': s.title,
        'icon': s.icon,
        'points': s.points,
      }).toList(),
      'flashcards': PreanesteziData.flashcards.map((f) => {
        'id': f.id,
        'question': f.question,
        'answer': f.answer,
      }).toList(),
      'quizQuestions': PreanesteziData.quizQuestions.map((q) => {
        'id': q.id,
        'question': q.question,
        'options': q.options,
        'correctAnswer': q.correctAnswer,
        'explanation': q.explanation,
        'distractorAnalysis': q.distractorAnalysis,
        'slideNumber': q.slideNumber,
      }).toList(),
      'openEndedQuestions': PreanesteziData.openEndedQuestions.map((o) => {
        'id': o.id,
        'question': o.question,
        'idealAnswer': o.idealAnswer,
        'slideNumber': o.slideNumber,
      }).toList(),
    },
  ];

  final output = json.encode({'lessons': lessons});
  File('data.json').writeAsStringSync(output);
  print('data.json oluşturuldu!');
}
