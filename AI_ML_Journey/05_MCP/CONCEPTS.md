# Model Context Protocol (MCP)

## Overview
The Model Context Protocol (MCP) is an open protocol that standardizes how AI applications connect to data sources and tools. Think of it as "USB for AI" - providing a universal way to plug different capabilities into AI systems.

## Why MCP?

### The Problem Before MCP
- Every AI app had custom integrations
- Redundant code for similar features
- Difficult to share capabilities
- Security concerns
- Maintenance nightmare

### MCP Solution
- **Standard interface**: One protocol for all
- **Reusable servers**: Write once, use anywhere
- **Secure**: Built-in security model
- **Extensible**: Easy to add new capabilities
- **Open**: Community-driven, vendor-neutral

## Core Concepts

### 1. MCP Architecture

```
┌─────────────────┐
│   AI Assistant  │  (Claude, ChatGPT, Custom)
│    (MCP Host)   │
└────────┬────────┘
         │ MCP Protocol
         │
┌────────┴────────────────────┐
│                             │
│  ┌─────────────┐  ┌───────────────┐  ┌──────────────┐
│  │ MCP Server  │  │  MCP Server   │  │  MCP Server  │
│  │  (Files)    │  │  (Database)   │  │   (Web)      │
│  └─────────────┘  └───────────────┘  └──────────────┘
│
└─────────────────────────────┘
```

#### Components

**MCP Host** (Client)
- AI application (Claude Desktop, IDE)
- Connects to MCP servers
- Makes requests
- Receives responses

**MCP Server**
- Provides specific capabilities
- Exposes tools, resources, prompts
- Can run locally or remotely
- Implements MCP protocol

**MCP Protocol**
- Standardized communication
- JSON-RPC based
- Request/response model
- Bidirectional

### 2. MCP Primitives

#### Resources
- Data sources agent can read
- Examples: Files, databases, APIs
- Read-only or read-write

```typescript
{
  uri: "file:///path/to/document.txt",
  mimeType: "text/plain",
  text: "Content here..."
}
```

#### Prompts
- Reusable prompt templates
- With variables
- Examples: Code review, summarization

```typescript
{
  name: "code_review",
  arguments: {
    code: "...",
    language: "python"
  }
}
```

#### Tools
- Functions agent can call
- Like LangChain tools but standardized
- Examples: Calculator, web search, API calls

```typescript
{
  name: "search_web",
  description: "Search the web",
  inputSchema: {
    type: "object",
    properties: {
      query: { type: "string" }
    }
  }
}
```

### 3. Building MCP Servers

#### Server Structure
```
my-mcp-server/
  ├── src/
  │   └── index.ts        # Main server code
  ├── package.json        # Dependencies
  ├── tsconfig.json       # TypeScript config
  └── README.md           # Documentation
```

#### Basic Server Template (TypeScript)
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "my-server",
  version: "1.0.0",
}, {
  capabilities: {
    tools: {},
    resources: {},
  },
});

// Register a tool
server.setRequestHandler(
  "tools/call",
  async (request) => {
    const { name, arguments: args } = request.params;
    
    if (name === "my_tool") {
      // Tool logic here
      return {
        content: [
          {
            type: "text",
            text: "Result from tool"
          }
        ]
      };
    }
  }
);

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

#### Python Server Template
```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("my-server")

@app.tool()
async def my_tool(arg1: str) -> list[TextContent]:
    """Tool description"""
    result = f"Processed: {arg1}"
    return [TextContent(type="text", text=result)]

if __name__ == "__main__":
    stdio_server(app)
```

### 4. Common MCP Server Types

#### File System Server
- Read/write files
- Navigate directories
- Search files

#### Database Server
- Query databases
- Execute SQL
- Schema inspection

#### Web Server
- Fetch web pages
- Search APIs
- Web scraping

#### API Integration Server
- Call external APIs
- GitHub, Slack, etc.
- OAuth handling

#### Memory Server
- Store conversation history
- Retrieve relevant context
- Vector search

### 5. Connecting to MCP Servers

#### Claude Desktop Configuration
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "node",
      "args": ["/path/to/server/index.js"]
    },
    "database": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {
        "DB_URL": "postgresql://..."
      }
    }
  }
}
```

#### Custom Client
```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["path/to/server.js"],
});

const client = new Client({
  name: "my-client",
  version: "1.0.0",
});

await client.connect(transport);

// List available tools
const tools = await client.listTools();

// Call a tool
const result = await client.callTool({
  name: "my_tool",
  arguments: { param: "value" }
});
```

### 6. Security Model

#### Principles
- **Least privilege**: Only necessary permissions
- **Explicit consent**: User approves capabilities
- **Sandboxing**: Isolated execution
- **Audit logs**: Track all actions

#### Security Features
- Path restrictions for file access
- API key management
- Rate limiting
- Input validation
- Output sanitization

### 7. MCP vs Other Approaches

#### MCP vs LangChain Tools
| MCP | LangChain |
|-----|-----------|
| Protocol | Framework |
| Language-agnostic | Python/JS |
| Reusable servers | Per-app tools |
| Standardized | Custom implementations |

#### When to Use MCP
- ✅ Building reusable capabilities
- ✅ Need cross-app compatibility
- ✅ Want standard security model
- ✅ Long-term maintainability

#### When to Use LangChain
- ✅ Quick prototypes
- ✅ Python-only projects
- ✅ Need LangChain ecosystem
- ✅ Custom complex chains

### 8. MCP Ecosystem

#### Official Servers
- **Filesystem**: File operations
- **GitHub**: Repository access
- **Google Drive**: Cloud storage
- **Postgres**: Database queries
- **Slack**: Team communication

#### Community Servers
- Growing ecosystem
- Various data sources
- Specialized tools
- Domain-specific

#### Building for the Ecosystem
1. Clear documentation
2. TypeScript types
3. Error handling
4. Security considerations
5. Publish to npm/PyPI
6. Add to MCP registry

### 9. Advanced Features

#### Streaming
- Real-time updates
- Progress indicators
- Long-running operations

#### Sampling
- Server can request completions
- Agentic servers
- Interactive workflows

#### Multiple Transports
- stdio (local)
- HTTP/SSE (remote)
- WebSocket (bidirectional)

### 10. Testing MCP Servers

#### Unit Tests
```typescript
import { describe, it, expect } from 'vitest';
import { MyServer } from './server';

describe('MyServer', () => {
  it('should handle tool call', async () => {
    const server = new MyServer();
    const result = await server.handleToolCall({
      name: 'my_tool',
      arguments: { input: 'test' }
    });
    expect(result).toBeDefined();
  });
});
```

#### Integration Tests
- Start server
- Connect client
- Call tools
- Verify responses

#### Inspector Tool
- Official MCP inspector
- Debug server interactions
- Test tools manually
- View protocol messages

### 11. Deployment

#### Local Deployment
- User's machine
- Claude Desktop
- VS Code extension
- Simple setup

#### Remote Deployment
- Cloud hosting
- Docker containers
- API gateway
- Scalable

#### Example Dockerfile
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["node", "dist/index.js"]
```

### 12. Best Practices

#### Server Development
- Clear tool descriptions
- Comprehensive error handling
- Input validation
- Efficient operations
- Good logging

#### Security
- Validate all inputs
- Sanitize outputs
- Use environment variables for secrets
- Implement rate limiting
- Audit important operations

#### Performance
- Cache when possible
- Minimize external calls
- Stream large responses
- Timeout long operations

#### Documentation
- Clear README
- Tool descriptions
- Usage examples
- Configuration guide

### 13. Real-World Use Cases

#### Development Workflow
- Code search
- Git operations
- Deploy applications
- Monitor services

#### Data Analysis
- Query databases
- Generate reports
- Visualize data
- Export results

#### Content Management
- Create/edit documents
- Search knowledge base
- Update wikis
- Manage media

#### Automation
- Schedule tasks
- Send notifications
- Process workflows
- Integrate services

### 14. Building Your First MCP Server

#### Project: Simple Calculator Server

```typescript
// calculator-server.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "calculator",
  version: "1.0.0",
}, {
  capabilities: {
    tools: {},
  },
});

server.setRequestHandler("tools/list", async () => {
  return {
    tools: [
      {
        name: "calculate",
        description: "Perform mathematical calculations",
        inputSchema: {
          type: "object",
          properties: {
            expression: {
              type: "string",
              description: "Math expression to evaluate"
            }
          },
          required: ["expression"]
        }
      }
    ]
  };
});

server.setRequestHandler("tools/call", async (request) => {
  if (request.params.name === "calculate") {
    try {
      const result = eval(request.params.arguments.expression);
      return {
        content: [
          {
            type: "text",
            text: `Result: ${result}`
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error: ${error.message}`
          }
        ],
        isError: true
      };
    }
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

### 15. Future of MCP

#### Roadmap
- More transport options
- Enhanced security features
- Better debugging tools
- Richer protocol features
- Growing ecosystem

#### Community
- Open source
- Active development
- Contributions welcome
- Discord community

## Connection to AI Agents

MCP makes AI agents more powerful by:
- **Standardized tools**: Easier tool integration
- **Reusable capabilities**: Share across agents
- **Secure access**: Built-in security
- **Maintainable**: One server, many agents

## Next Steps

1. Install MCP SDK
2. Build simple server
3. Connect to Claude Desktop
4. Create custom tools
5. Build a complete project

## Resources

- Official MCP Documentation
- MCP Specification
- MCP GitHub Repository
- Example Servers
- Community Discord
- Tutorial Videos
- MCP Inspector Tool
