class KeyPointSection {
  final String title;
  final String icon;
  final List<String> points;

  const KeyPointSection({
    required this.title,
    required this.icon,
    required this.points,
  });

  factory KeyPointSection.fromJson(Map<String, dynamic> json) {
    return KeyPointSection(
      title: json['title'] as String,
      icon: json['icon'] as String,
      points: List<String>.from(json['points'] as List),
    );
  }
}

class FlashcardItem {
  final String id;
  final String question;
  final String answer;

  const FlashcardItem({
    required this.id,
    required this.question,
    required this.answer,
  });

  factory FlashcardItem.fromJson(Map<String, dynamic> json) {
    return FlashcardItem(
      id: json['id'] as String,
      question: json['question'] as String,
      answer: json['answer'] as String,
    );
  }
}

class QuizQuestionItem {
  final String id;
  final String question;
  final Map<String, String> options;
  final String correctAnswer;
  final String explanation;
  final String distractorAnalysis;
  final int slideNumber;

  const QuizQuestionItem({
    required this.id,
    required this.question,
    required this.options,
    required this.correctAnswer,
    required this.explanation,
    required this.distractorAnalysis,
    required this.slideNumber,
  });

  factory QuizQuestionItem.fromJson(Map<String, dynamic> json) {
    return QuizQuestionItem(
      id: json['id'] as String,
      question: json['question'] as String,
      options: Map<String, String>.from(json['options'] as Map),
      correctAnswer: json['correctAnswer'] as String,
      explanation: json['explanation'] as String,
      distractorAnalysis: json['distractorAnalysis'] as String,
      slideNumber: (json['slideNumber'] as num).toInt(),
    );
  }
}

class OpenEndedQuestionItem {
  final String id;
  final String question;
  final String idealAnswer;
  final int slideNumber;

  const OpenEndedQuestionItem({
    required this.id,
    required this.question,
    required this.idealAnswer,
    required this.slideNumber,
  });

  factory OpenEndedQuestionItem.fromJson(Map<String, dynamic> json) {
    return OpenEndedQuestionItem(
      id: json['id'] as String,
      question: json['question'] as String,
      idealAnswer: json['idealAnswer'] as String,
      slideNumber: (json['slideNumber'] as num).toInt(),
    );
  }
}

class CourseLesson {
  final String id;
  final String title;
  final String subtitle;
  final String icon;
  final List<KeyPointSection> summarySections;
  final List<FlashcardItem> flashcards;
  final List<QuizQuestionItem> quizQuestions;
  final List<OpenEndedQuestionItem> openEndedQuestions;

  const CourseLesson({
    required this.id,
    required this.title,
    required this.subtitle,
    required this.icon,
    required this.summarySections,
    required this.flashcards,
    required this.quizQuestions,
    required this.openEndedQuestions,
  });

  factory CourseLesson.fromJson(Map<String, dynamic> json) {
    return CourseLesson(
      id: json['id'] as String,
      title: json['title'] as String,
      subtitle: json['subtitle'] as String,
      icon: json['icon'] as String,
      summarySections: (json['summarySections'] as List)
          .map((e) => KeyPointSection.fromJson(e as Map<String, dynamic>))
          .toList(),
      flashcards: (json['flashcards'] as List)
          .map((e) => FlashcardItem.fromJson(e as Map<String, dynamic>))
          .toList(),
      quizQuestions: (json['quizQuestions'] as List)
          .map((e) => QuizQuestionItem.fromJson(e as Map<String, dynamic>))
          .toList(),
      openEndedQuestions: (json['openEndedQuestions'] as List)
          .map((e) => OpenEndedQuestionItem.fromJson(e as Map<String, dynamic>))
          .toList(),
    );
  }
}
