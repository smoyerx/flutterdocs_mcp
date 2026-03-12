## Using flutterdocs_mcp

Below are examples for configuring `flutterdocs_mcp` with various hosts.


### VS Code

To use `flutterdocs_mcp` with [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers), add the following to your `mcp.json`:

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

### MCP Inspector

[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is a tool for testing and debugging MCP servers. To use `flutterdocs_mcp` with MCP Inspector first [install Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) on your system and then run:

```bash
npx @modelcontextprotocol/inspector flutterdocs_mcp -- --db /path/to/flutterdocs.db
```
