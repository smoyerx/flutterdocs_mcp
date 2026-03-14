## Using flutterdocs_mcp

Below are examples and tips for configuring `flutterdocs_mcp` with various hosts and using it effectively.


### VS Code

To use `flutterdocs_mcp` with [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers), add the following to your `mcp.json`:

```json
{
	"servers": {
		"flutterdocs": {
			"type": "stdio",
			"command": "flutterdocs_mcp",
			"args": ["--db", "/path/to/flutterdocs.db"]
		}
	}
}
```

The **MCP server name** is `flutterdocs` as configured above. This is the name that will appear in VS Code tools and that should be used in chat sessions.

Tips:
- Thoroughly review the VS Code documentation on [configuring, managing, and using](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) MCP servers.
- Select **`Configure Tools`** in chat sessions to confirm the MCP server name is selected.
- Reference the MCP server name in chat sessions to ensure the agent uses it to formulate responses.
	- `summarize materialpageroute usage from flutterdocs`
	- `explain flutter slivers. reference flutterdocs to verify api details.`
- Attach resources to chat sessions by selecting **`Add Context > MCP Resources`** or using the **`MCP: Browse Resources`** command and then choosing one of the resource templates associated with the MCP server name.
- My experience is that `GPT-5 mini` struggles with MCP servers. Some others may as well; I did not test all available models.


### MCP Inspector

[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is a tool for testing and debugging MCP servers. To use `flutterdocs_mcp` with MCP Inspector first [install Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) on your system and then run:

```bash
npx @modelcontextprotocol/inspector flutterdocs_mcp -- --db /path/to/flutterdocs.db
```
