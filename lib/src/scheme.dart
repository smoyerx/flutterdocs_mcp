/// URI scheme constants and helpers for Flutter/Dart documentation URIs.
///
/// All `flutter-docs://api/...` URIs share the prefix [kApiPrefix]. The three
/// URI shapes are:
/// - `flutter-docs://api/{library_slug}` — library index
/// - `flutter-docs://api/{library_slug}/{entity}` — entity documentation
/// - `flutter-docs://api/{library_slug}/{entity}/{member}` — member documentation
const kScheme = 'flutter-docs';
const kApiPrefix = 'flutter-docs://api/';

/// Splits a `flutter-docs://api/...` URI into decoded path segments.
///
/// Returns `null` if [uri] does not start with [kApiPrefix] or has no path
/// after the prefix.
List<String>? apiSegments(String uri) {
  if (!uri.startsWith(kApiPrefix)) return null;
  final path = uri.substring(kApiPrefix.length);
  if (path.isEmpty) return null;
  return path.split('/').map(Uri.decodeComponent).toList();
}
