# databricks-mcp-client

This tool gives information about your Databricks workspace to a chat bot.

Based on MCP quickstart by Dan Liden: <https://www.danliden.com/posts/20250412-mcp-quickstart.html>

## How to use

Follow the setup guide in the post: <https://www.danliden.com/posts/20250412-mcp-quickstart.html>

Modify `claude_desktop_config.json` to contain the following:

```[json]
{
  "mcpServers": {
    "DatabricksServer": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "run",
        "--with",
        "databricks-sdk",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/bencetoth/Documents/dev/mcp-cpu-usage/dbx_connector/server.py"
      ]
    }
  }
}
```

You will have to adjust the path to the project and to uv.
