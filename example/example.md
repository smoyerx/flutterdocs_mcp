# Configuration and Best Practices

Below are examples and best practices for configuring `flutterdocs_mcp` with various hosts and using it effectively.


## Host Configuration

The following host configuration examples use `flutterdocs` as the **MCP server name**, where applicable. This is the name that hosts will generally use in tools, menus, chat sessions, and invocations (e.g., slash commands).

The server name `flutterdocs` also appears in the associated [agent skill](#agent-skill) and so its use is strongly encouraged.

### GitHub Copilot in VS Code

Add the following to your `mcp.json`:

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

See the [VS Code documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) for additional details on configuring, managing, and using MCP servers with GitHub Copilot.

Usage Tips:
- Select **`Configure Tools`** in chat sessions to confirm `flutterdocs` is selected.
- Attach resources to chat sessions by selecting **`Add Context > MCP Resources`** or using the **`MCP: Browse Resources`** command and then choosing one of the resource templates associated with `flutterdocs`.
- My experience is that `GPT-5 mini` struggles with MCP servers. Some others may as well; I did not test all available models.


### MCP Inspector

[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is a tool for testing and debugging MCP servers. To use `flutterdocs_mcp` with MCP Inspector first [install Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) on your system and then run:

```bash
npx @modelcontextprotocol/inspector flutterdocs_mcp --db /path/to/flutterdocs.db
```


## Best Practices

Follow these best practices to get the most from `flutterdocs_mcp` with your AI assistant.

### Agent Skill

The most effective way to use `flutterdocs_mcp` is to install the `flutterdocs-usage` [agent skill](https://agentskills.io/home). Simply copy the contents of the file [.github/skills/flutterdocs-usage/SKILL.md](https://raw.githubusercontent.com/smoyerx/flutterdocs_mcp/refs/heads/main/.github/skills/flutterdocs-usage/SKILL.md) from this repo to your host's local skills directory.

```bash
cd /path/to/host/skills
mkdir flutterdocs-usage && cd flutterdocs-usage
curl -L -O https://raw.githubusercontent.com/smoyerx/flutterdocs_mcp/refs/heads/main/.github/skills/flutterdocs-usage/SKILL.md
```

### Prompting

With the `flutterdocs-usage` agent skill installed, AI assistants will normally consult the Flutter/Dart API documentation from `flutterdocs_mcp` when needed. You can also force assistants to search or consult this documentation by referencing `flutterdocs` in prompts or using host-specific mechanisms.

Prompt examples:
- summarize materialpageroute usage from flutterdocs
- explain flutter slivers. reference flutterdocs to verify api details.
- search flutterdocs for widgets that support nested scrolling

Host-specific mechanisms are described with the corresponding host configuration details.
