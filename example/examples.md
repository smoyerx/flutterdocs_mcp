## Using flutterdocs_mcp

Below are examples for configuring `flutterdocs_mcp` with various hosts.


### VS Code

To use `flutterdocs_mcp` with [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) add the following to your `mcp.json`:

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
