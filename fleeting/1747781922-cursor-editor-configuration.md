---
id: 1747781922-cursor-editor-configuration
aliases:
  - cursor-editor-configuration
tags: []
---

# cursor-editor-configuration

Here we will see how to configure the cursor editor for a great development experience. In addition to that we will se configurations to improve neovim integration with AI based workflows.

## MCP integration

MCP (Model Context Protocol) is a communication protocol that allows for **LLM-based agents** to fetch context from third-party services and resources. It exposes to the agent a series of tools that it can use to gather, process, and integrate relevant information seamlessly, enabling more efficient and intelligent workflows.

### configure the [Atlasian integration](https://www.pulsemcp.com/servers/sooperset-atlassian)!

First, create a directory to store the **MCP** code in your machine. That can be easily done with a `mkdir -p ~/.mcphub/servers`. Once the directory is created, clone the MCP repository into it using `git clone https://github.com/sooperset/mcp-atlassian.git ~/.mcphub/servers/mcp-atlassian`. After cloning, navigate to the directory, you can check detailed setup instructions in the `README.md` file.

Then you can open cursor's settings and go to the MCP tab:

![](data/cursor-tutorial-1.png)

After clicking on create it will present to you a `.json` file with all MCP related configuration. Add the following entry to the `mcpServers` key:

```json
    "mcp-atlassian": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "CONFLUENCE_URL",
        "-e", "CONFLUENCE_USERNAME",
        "-e", "CONFLUENCE_API_TOKEN",
        "-e", "JIRA_URL",
        "-e", "JIRA_USERNAME",
        "-e", "JIRA_API_TOKEN",
        "ghcr.io/sooperset/mcp-atlassian:latest"
      ],
      "env": {
        "CONFLUENCE_URL": "https://<your-company>.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "<your-login-email>",
        "CONFLUENCE_API_TOKEN": "<atlasian-api-key>",
        "JIRA_URL": "https://<your-company>.atlassian.net",
        "JIRA_USERNAME": "<your-login-email>",
        "JIRA_API_TOKEN": "<atlasian-api-key>"
      }
    }
```

> Note: You can find the **Atlassian** api token through [this link](https://id.atlassian.com/manage-profile/security/api-tokens)

After the addition to the `mcp.json` file, you will be able to make questions and include **Jira** context:

![](data/cursor-tutorial-2.png)
Other good options:

- [github](https://github.com/github/github-mcp-server)
- [google calendar](https://www.pulsemcp.com/servers/nspady-google-calendar)
- [python repl](https://www.pulsemcp.com/servers/tynan-daly-python-repl)

If you install too much tools, it may show a warning: "You have X tools from enabled servers. Too many tools can degrade performance, and some models may not repsect more than Y tools". In this case you should change the configuration of the mcp-server to only expose the tools you will need. You can do this by clicking in the tools to disable then:

### Configuring rules

Something interesting that cursor offers is the ability to determine rules, which will be run against your prompts and will perform actions based on the content.
