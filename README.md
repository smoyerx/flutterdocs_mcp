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

## Documentation Database

The documentation database file is generated from the Flutter stable [offline documentation](https://api.flutter.dev/index.html) as follows:
- HTML content is convert to markdown and cleaned.
- Internal documentation links are converted to a custom URI scheme.
- Image links are converted to text indicating the image is omitted.
- DartPad interactive code links are converted to text indicating the interactive code is omitted.
- Stubs (for inherited members)...
- Code examples (snippets)...


## URI Scheme


## TODOs

- Develop A/B tests to quantify what (if any) benefits AI assistants derive from having local access to the complete documentation.
- Experiment with tools, resource templates (not yet widely used), and instructions to get AI assistants the information they need efficiently.
- Automate the database file download (via the `data_assets` package) if this tool proves to be useful.


## Acknowledgements

