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
			"args": [
				"--db",
				"~/Documents/flutterdocs.db"
			]
		}
	},
	"inputs": []
}
```
