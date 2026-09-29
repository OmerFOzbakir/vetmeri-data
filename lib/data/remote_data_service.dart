import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/study_models.dart';

class RemoteDataService {
  // GitHub Pages'deki data.json URL'i
  // Bu URL'i GitHub'a yükledikten sonra gerçek URL ile güncelleyeceğiz
  static const String _dataUrl =
      'https://raw.githubusercontent.com/OmerFOzbakir/vetmeri-data/main/data.json';

  static Future<List<CourseLesson>> fetchLessons() async {
    final response = await http.get(Uri.parse(_dataUrl)).timeout(
      const Duration(seconds: 15),
    );

    if (response.statusCode != 200) {
      throw Exception('Sunucudan veri alınamadı: ${response.statusCode}');
    }

    final Map<String, dynamic> jsonData = json.decode(
      utf8.decode(response.bodyBytes),
    );

    final List<dynamic> lessonsJson = jsonData['lessons'] as List;
    return lessonsJson
        .map((e) => CourseLesson.fromJson(e as Map<String, dynamic>))
        .toList();
  }
}
