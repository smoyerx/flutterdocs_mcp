# Flutter/Dart API Documentation for AI assistants

Wraps the offline Flutter/Dart API documentation in an MCP server that AI assistants can navigate and search.


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
curl -L -O https://github.com/smoyerx/flutterdocs_mcp/releases/latest/download/flutterdocs.db.gz
```

```bash
wget --content-disposition https://github.com/smoyerx/flutterdocs_mcp/releases/latest/download/flutterdocs.db.gz
```

Unzip the database file and place it in a directory accessible by `flutterdocs_mcp`, which takes the path to the file as a command-line argument.

```bash
gunzip flutterdocs.db.gz
```


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

Add `flutterdocs_mcp` to your host configuration, specifying the path to the documentation database file.

For example, to use `flutterdocs_mcp` with [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) add the following to your `mcp.json`:

```json
{
	"servers": {
		"Flutter API Documentation": {
			"type": "stdio",
			"command": "flutterdocs_mcp",
			"args": ["--db", "/path/to/flutterdocs.db"]
		}
	}
}
```

See [examples](example/examples.md) for configuring `flutterdocs_mcp` with various hosts.

## Documentation Database Generation

The documentation database file is generated from the Flutter stable [offline documentation](https://api.flutter.dev/index.html) as follows:
- HTML content is convert to markdown and sanitized.
- Internal documentation links are converted to a custom URI scheme.
- Image links are converted to text indicating the image is omitted.
- DartPad interactive code links are converted to text indicating the interactive code is omitted.
- Stub entries are generated for inherited members to keep the URI scheme robust.
- Code examples (snippets), where available, are appended as a new section of the documentation for classes, mixins, etc.


## MCP Server Operational Details

Below is a summary of how `flutterdocs_mcp` operates as an MCP server. You do not need to know any of this to use it, but it's here for those who are interested.

### URI Scheme

- Library documentation: flutter-docs://api/{library_slug}
- Entity (class, mixin, etc.) documentation: flutter-docs://api/{library_slug}/{entity}
- Member (constructor, properties, etc.) documentation: flutter-docs://api/{library_slug}/{entity}/{member}

Library slugs are used in place of library display names to form valid URIs (e.g., `dart:io` uses slug `dart-io`). The slugs are the same as used for the native HTML documentation. AI assistants can access the mapping from library display name to slug using the `listLibraries` tool.


### Tools

- `listLibraries`: lists slugs and display names for all available library documentation.
- `searchDocumentation`: performs a full-text search across all the library documentation.
- `lookupEntity`: resolves entity (class, mixin, etc.) identifier names.
- `lookupMember`: resolves member (constructor, property, method, etc.) identifier names.
- `getDocumentation`: fetches documentation for the specified URI.

The `lookupEntity` and `lookupMember` tools return arrays of `[library_slug, entity, category]` or `[library_slug, entity, member, category]` tuples, respectively, for constructing URIs to use with the `getDocumentation` tool or resource templates.


### Resource Templates

There is a resource template for each of the URI shapes above: `libraryIndex`, `entityDocumentation`, and `memberDocumentation`. They can be used instead of the `getDocumentation` tool.

Not all MCP hosts use resource templates. For example, VS Code does not at the time of writing.


## Motivation

There are several other MCP server projects for Flutter/Dart documentation, including:
- [Context7](https://context7.com/), which is a widely-used MCP documentation service that includes various Flutter documentation sets in its inventory.
- [flutter-mcp](https://github.com/adamsmaka/flutter-mcp), which is built with the [FastMCP](https://gofastmcp.com/getting-started/welcome) Python library and fetches/caches online Flutter documentation.
- [flutter_mcp_2](https://github.com/dvillegastech/flutter_mcp_2), which is built with JavaScript and also fetches/caches online Flutter documentation.

My motivations for creating `flutterdocs_mcp` were to:
- Store all documentation locally for fast full-text search across all libraries.
- Eliminate first-time load delays.
- Avoid in-line conversion from HTML to markdown.
- Implement in `Dart` using `dart_mcp` for native hosting on `pub.dev`.


## TODOs

- Develop A/B tests to quantify what (if any) benefits AI assistants derive from having local access to the documentation.
- Experiment with tools, resource templates, and associated instructions to determine how best to get AI assistants the information they need efficiently.
- Define a `flutterdocs_mcp` skill to determine if additional instructions, beyond those built into the server, improves performance or accuracy.
- Add Flutter/Dart guides within a flutter-docs://guide/... URI space.
- Support pagination for `searchDocumentation`.
- Automate the database file download via the `data_assets` package.


## Contribute Your Feedback

At this early state, I am not yet prepared to accept PRs for `flutterdocs_mcp`. However, any [feedback or data](CONTRIBUTING.md) that you can provide is greatly appreciated!

With LLMs being released or updated at an accelerating rate, its not clear that having the most up-to-date documentation will meaningly improve the performance of AI assistants. But I am interested in finding out.


## Acknowledgements

- Flutter/Dart teams for making their excellent documentation available offline.
- Dart team for the [`dart_mcp`](https://pub.dev/packages/dart_mcp) package which makes building MCP servers a breeze.
- Developers of the [`html-to-markdown`](https://github.com/kreuzberg-dev/html-to-markdown) package which has proven robust and blazingly fast.
- Sonnet 4.5/4.6 for writing most of the code. Yes, I reviewed it (OK, the tests not so much).
