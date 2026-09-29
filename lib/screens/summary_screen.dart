import 'package:flutter/material.dart';
import '../models/study_models.dart';
import '../theme/app_theme.dart';

class SummaryScreen extends StatelessWidget {
  final CourseLesson lesson;

  const SummaryScreen({
    super.key,
    required this.lesson,
  });

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
      children: [
        // Hero Module Card
        Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: AppTheme.cardBg,
            borderRadius: BorderRadius.circular(22),
            border: Border.all(color: AppTheme.borderSubtle),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withValues(alpha: 0.03),
                blurRadius: 16,
                offset: const Offset(0, 4),
              )
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                    decoration: BoxDecoration(
                      color: AppTheme.primaryLight,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Text(
                      lesson.title.split(":").first.trim(),
                      style: const TextStyle(
                        color: AppTheme.primary,
                        fontWeight: FontWeight.w700,
                        fontSize: 12,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text(
                    "${lesson.summarySections.length} Konu Bölümü",
                    style: const TextStyle(
                      color: AppTheme.textMedium,
                      fontSize: 12,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 10),
              Text(
                lesson.title,
                style: const TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.w800,
                  color: AppTheme.textDark,
                  height: 1.3,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                lesson.subtitle,
                style: const TextStyle(
                  fontSize: 13.5,
                  color: AppTheme.textMedium,
                  height: 1.55,
                ),
              ),
            ],
          ),
        ),

        const SizedBox(height: 20),
        const Padding(
          padding: EdgeInsets.only(left: 4, bottom: 12),
          child: Text(
            "Konu Başlıkları & Kritik Bilgiler",
            style: TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.w800,
              color: AppTheme.textDark,
            ),
          ),
        ),

        // Expanded Sections
        ...lesson.summarySections.map((section) => _buildSectionCard(section)),
        const SizedBox(height: 24),
      ],
    );
  }

  Widget _buildSectionCard(KeyPointSection section) {
    return Container(
      margin: const EdgeInsets.only(bottom: 14),
      child: Material(
        color: AppTheme.cardBg,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: const BorderSide(color: AppTheme.borderSubtle),
        ),
        child: Theme(
          data: ThemeData().copyWith(dividerColor: Colors.transparent),
          child: ExpansionTile(
            initiallyExpanded: false,
            tilePadding: const EdgeInsets.symmetric(horizontal: 18, vertical: 4),
            leading: Container(
              width: 38,
              height: 38,
              decoration: BoxDecoration(
                color: AppTheme.primaryLight,
                borderRadius: BorderRadius.circular(12),
              ),
              alignment: Alignment.center,
              child: Text(
                section.icon,
                style: const TextStyle(fontSize: 18),
              ),
            ),
            title: Text(
              section.title,
              style: const TextStyle(
                fontWeight: FontWeight.w700,
                fontSize: 15,
                color: AppTheme.textDark,
              ),
            ),
            children: [
              Padding(
                padding: const EdgeInsets.fromLTRB(18, 0, 18, 18),
                child: Column(
                  children: section.points.map((point) {
                    final parts = point.split(":");
                    final hasColon = parts.length > 1;
                    final prefix = hasColon ? parts[0] : null;
                    final rest = hasColon ? parts.sublist(1).join(":") : point;

                    return Padding(
                      padding: const EdgeInsets.only(bottom: 10),
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Container(
                            margin: const EdgeInsets.only(top: 6, right: 10),
                            width: 6,
                            height: 6,
                            decoration: const BoxDecoration(
                              color: AppTheme.primary,
                              shape: BoxShape.circle,
                            ),
                          ),
                          Expanded(
                            child: RichText(
                              text: TextSpan(
                                style: const TextStyle(
                                  fontSize: 13.5,
                                  color: AppTheme.textDark,
                                  height: 1.5,
                                  fontFamily: 'Segoe UI',
                                ),
                                children: [
                                  if (prefix != null)
                                    TextSpan(
                                      text: "$prefix: ",
                                      style: const TextStyle(
                                        fontWeight: FontWeight.w700,
                                        color: AppTheme.primary,
                                      ),
                                    ),
                                  TextSpan(
                                    text: rest.trim(),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ],
                      ),
                    );
                  }).toList(),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
