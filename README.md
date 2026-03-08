# Flutter/Dart API Documentation for AI assistants

Wraps the native Flutter/Dart API documentation in an MCP server that AI assistants can search and navigate.


## Features

- Stores documentation in a local `sqlite3` database file for fast response.
- Defines a resource URI scheme that AI assistants can predict and navigate.
- Supports both targeted documentation retrieval and full-text queries.


## Getting Started

Install the latest version of `flutterdocs_mcp`.

```bash
dart install flutterdocs_mcp
```

The install command will print a message if you need to add the install directory to your shell's path.

Fetch the latest version of the documentation database file using `curl` or `wget`.

```bash
curl -L -O https://github.com/smoyerx/flutterdocs_mcp/releases/latest/download/flutterdocs.db
```

```bash
wget --content-disposition https://github.com/smoyerx/flutterdocs_mcp/releases/latest/download/flutterdocs.db
```

Put the database file in a directory accessible by `flutterdocs_mcp`, which takes the path to the file as a command-line argument.


## Verifying Versions

The version of the `flutterdocs_mcp` executable must match that of the database file.

To check the executable version run:

```bash
flutterdocs_mcp --version
```

To check the database file version run:

```bash
flutterdocs_mcp --db-version --db </path/to/flutterdocs.db>
```


## Usage

Add `flutterdocs_mcp` to your MCP server configuration, specifying the path to the documentation database file.

For example, to use `flutterdocs_mcp` with [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) add the following to your `mcp.json`:

```json
{
	"servers": {
		"Flutter Documentation": {
			"type": "stdio",
			"command": "flutterdocs_mcp",
			"args": ["--db", "/path/to/flutterdocs.db"]
		}
	}
}
```

## Documentation Database Generation

The documentation database file is generated from the Flutter stable [offline documentation](https://api.flutter.dev/index.html) as follows:
- HTML content is convert to markdown and cleaned.
- Internal documentation links are converted to a custom URI scheme.
- Image links are converted to text indicating the image is omitted.
- DartPad interactive code links are converted to text indicating the interactive code is omitted.
- Stub entries are generated for inherited members to keep the URI scheme robust.
- Code examples (snippets) where available are appended as a new section of the documentation for classes, mixins, etc.


## URI Scheme

- Library documentation: flutter-docs://api/{library_slug}
- Entity (class, mixin, etc.) documentation: flutter-docs://api/{library_slug}/{entity}
- Member (constructor, properties, etc.) documentation: flutter-docs://api/{library_slug}/{entity}/{member}

Library slugs are used in place of library display names to form valid URIs (e.g., `dart:io` is represented by slug `dart-io`). The slugs are the same as used for the native HTML documentation.


## MCP Tools

All tools are readonly. A summary and rationale for each is forthcoming.


## MCP Resource Templates

There is a resource template for each of the URI shapes above. However, not all MCP clients make use of resource templates (e.g., VS Code does not at the time I am writing this).


## TODOs

- Develop A/B tests to quantify what (if any) benefits AI assistants derive from having local access to the complete documentation.
- Experiment with tools, resource templates (not yet widely used), and instructions to determine how best to get AI assistants the information they need efficiently.
- Automate the database file download (via the `data_assets` package) if this tool proves to be useful.


## Acknowledgements

- Flutter/Dart teams for making their excellent documentation available offline.
- Dart team for the [`dart_mcp`](https://pub.dev/packages/dart_mcp) package which makes building MCP servers a breeze.
- Developers of the [`html-to-markdown`](https://github.com/kreuzberg-dev/html-to-markdown) package which has proven robust and blazingly fast.
- Sonnet 4.5/4.6 for writing most of the code.
