import '../models/study_models.dart';
import 'anestezi_data.dart';
import 'preanestezi_data.dart';

class CourseRepository {
  static final List<CourseLesson> lessons = [
    const CourseLesson(
      id: "lesson_1",
      title: "1. Ders: Anesteziye Giriş & Muayene",
      subtitle: "38 Slayt • Preanestezik Değerlendirme, ASA & Fizyoloji",
      icon: "🩺",
      summarySections: AnesteziData.summarySections,
      flashcards: AnesteziData.flashcards,
      quizQuestions: AnesteziData.quizQuestions,
      openEndedQuestions: AnesteziData.openEndedQuestions,
    ),
    const CourseLesson(
      id: "lesson_2",
      title: "2. Ders: Preanestezik İlaçlar & İndüksiyon",
      subtitle: "74 Slayt • Atropin, Ksilazin, Ketamin, Tiyopental & Entübasyon",
      icon: "💊",
      summarySections: PreanesteziData.summarySections,
      flashcards: PreanesteziData.flashcards,
      quizQuestions: PreanesteziData.quizQuestions,
      openEndedQuestions: PreanesteziData.openEndedQuestions,
    ),
  ];
}
