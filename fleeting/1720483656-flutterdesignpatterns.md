---
id: 1720483656-flutterdesignpatterns
aliases:
  - flutter_design_patterns
tags: []
---

# FLUTTER DESIGN PATTERNS

This is a collection of design patterns that will assist flutter developers in creating maintainable and scalable **dart** code.

## 📑 Singleton Pattern

Is a way of centralizing class instances in an app-wide context. All instances of a singleton class are reference to the same object.
For database connections, network request handlers, and shared data, like themes, singletons are useful. A great example is **web sockte connections**. Here is how it is done:

```dart
class SettingsManager {
  static final SettingsManager _instance = SettingsManager._internal();
  factory SettingsManager() => _instance;
  SettingsManager._internal();

  ThemeData _themeData = ThemeData.light();

  void switchTheme() {
    _themeData = _themeData.brightness == Brightness.light ? ThemeData.dark() : ThemeData.light();
  }

  ThemeData getTheme() => _themeData;
}
```
