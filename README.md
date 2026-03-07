# Flutter/Dart Documentation for AI assistants

`flutterdocs_mcp` is an MCP server for Flutter/Dart API documentation.

## Features

- Stores documentation in a local `sqlite3` database file for fast response.
- Defines a resource URI scheme that AI assistants can predict, navigate, and understand.
- Supports both targeted documentation retrieval and full-text queries.

## Getting Started

Install the latest version of `flutterdocs_mcp`.

```bash
dart pub install flutterdocs_mcp
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

Something here.

```json
{
	"servers": {
		"FlutterDocs MCP Server": {
			"type": "stdio",
			"command": "flutterdocs_mcp",
			"args": [
				"--db",
				"~/Documents/flutterdocs.db"
			]
		}
	},
	"inputs": []
}
```
