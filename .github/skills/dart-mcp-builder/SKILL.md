---
name: dart-mcp-builder
description: Guide to implementing a Dart-based MCP (Model Context Protocol) server using the `dart_mcp` package. Use when answering questions about, planning, implementing, testing, or debugging the MCP server component of this project.
---

# Dart MCP Server Guide

This skill provides guidance, references, and examples for building and maintaining a Dart-based MCP (Model Context Protocol) server using the `dart_mcp` package. It is intended to be used when answering questions about, planning, implementing, testing, or debugging the MCP server component of this project.

Both MCP server and client references are provided. Client references support developing a test client for the MCP server, which can be useful for integration testing and debugging.

Links in this skill reference `dart_mcp` version `0.4.1`, which is the latest version at the time of this writing. If a newer version becomes available, the links can be updated by replacing `dart_mcp-v0.4.1` with the appropriate version number in the URLs.

## Overview (`README.md`)

- `dart_mcp` package overview: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/README.md

## MCP Server Resources

Resources for building an MCP server with `dart_mcp`. Only resources for the MCP features relevant to this project are included (e.g., completions, elicitation, prompts, roots are excluded).

### Base Class

`MCPServer` is the base class to extend when building an MCP server: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/lib/src/server/server.dart

### Feature Mixins

For each MCP server feature (tools, resources, etc.), there is a mixin that can be added to `MCPServer` to implement that feature, along with associated enums and extension types.

#### Tools Mixin (`ToolsSupport`)

- `ToolsSupport` mixin: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/lib/src/server/tools_support.dart
- Related enums and extension types: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/lib/src/api/tools.dart

#### Resources Mixin (`ResourcesSupport`)

- `ResourcesSupport` mixin: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/lib/src/server/resources_support.dart
- Related enums and extension types: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/lib/src/api/resources.dart

#### Logging Mixin (`LoggingSupport`)

- `LoggingSupport` mixin: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/lib/src/server/logging_support.dart
- Related enums and extension types: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/lib/src/api/logging.dart

### Server Feature Examples

- Server tools example: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/example/tools_server.dart
- Server resources example: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/example/resources_server.dart

### Complete MCP File System Server Example

A basic file server built with `dart_mcp`: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/mcp_examples/bin/file_system_server.dart


## MCP Client Resources

Resources for building an MCP client with `dart_mcp`. A client is required for MCP server testing only.

### Base Class

`MCPClient` is the base class to extend when building an MCP client: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/lib/src/client/client.dart

### Client Examples

- Client tool invocation example: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/example/tools_client.dart
- Client resource access example: https://raw.githubusercontent.com/dart-lang/ai/dart_mcp-v0.4.1/pkgs/dart_mcp/example/resources_client.dart

## How to Use These References

When implementing or debugging an MCP server feature, fetch and read the `README.md` link, `MCPServer` class link, and relevant feature and feature example links (e.g., `ToolsSupport` and related enum/extension-type links, server tools example link).

When implementing or debugging an MCP client feature (for testing), fetch and read the `README.md` link, `MCPClient` class link, and relevant feature example links (e.g., client tool invocation example link).
