/// An MCP server for Flutter and Dart API documentation.
///
/// This library exposes [FlutterDocsMcpServer], which implements an MCP server
/// that serves Flutter/Dart API documentation over the stdio transport.
///
/// ## Activation
///
/// ```
/// dart install flutterdocs_mcp
/// flutterdocs_mcp --db /path/to/flutterdocs.db
/// ```
library;

export 'src/server.dart';
