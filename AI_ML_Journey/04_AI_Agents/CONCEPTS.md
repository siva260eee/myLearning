# AI Agents

## Overview
AI Agents are autonomous systems that can perceive their environment, make decisions, and take actions to achieve specific goals. Modern AI agents leverage LLMs to understand instructions, reason about tasks, and execute complex workflows.

## Core Concepts

### 1. What is an AI Agent?

#### Definition
An AI agent is a system that:
- **Perceives**: Observes environment/inputs
- **Reasons**: Processes information and plans
- **Acts**: Takes actions to achieve goals
- **Learns**: Improves from feedback

#### Agent vs Simple AI
| Simple AI | AI Agent |
|-----------|----------|
| Single task | Multi-step workflows |
| Stateless | Maintains state/memory |
| Direct I/O | Tool usage |
| No planning | Strategic planning |

### 2. Agent Architecture

#### ReAct (Reasoning + Acting)
```
Thought: I need to find information about X
Action: search("X")
Observation: Results show...
Thought: Now I understand, I should...
Action: Final Answer
```

#### Components
1. **LLM Core**: Decision-making brain
2. **Memory**: Short-term and long-term
3. **Tools**: Functions agent can call
4. **Planner**: Task decomposition
5. **Executor**: Runs actions

### 3. Types of AI Agents

#### Simple Reflex Agents
- Condition-action rules
- No internal state
- Fast but limited

#### Model-Based Agents
- Internal world model
- Track state over time
- More flexible

#### Goal-Based Agents
- Have explicit goals
- Plan to achieve goals
- Consider future consequences

#### Utility-Based Agents
- Optimize for utility function
- Make tradeoffs
- More sophisticated

### 4. Agent Frameworks

#### LangChain
```python
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.tools import Tool

agent = initialize_agent(
    tools=[...],
    llm=OpenAI(temperature=0),
    agent="zero-shot-react-description"
)
```

**Features**:
- Chain composition
- Multiple agent types
- Memory management
- Tool integration

#### LlamaIndex
- Focus on data indexing
- Query engines
- Document agents
- RAG-focused

#### AutoGPT
- Autonomous goal pursuit
- Self-prompting
- File operations
- Web browsing

#### BabyAGI
- Task-driven autonomous agent
- Task creation and prioritization
- Simple but effective

### 5. Agent Tools

#### What are Tools?
Functions that agents can call to:
- Search the internet
- Read/write files
- Execute code
- Query databases
- Call APIs
- Perform calculations

#### Tool Definition
```python
from langchain.tools import Tool

def calculator(expression: str) -> str:
    """Useful for math calculations"""
    return str(eval(expression))

calc_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Useful for math. Input: math expression"
)
```

#### Tool Selection
Agent must:
1. Understand available tools
2. Choose appropriate tool
3. Format input correctly
4. Interpret output

### 6. Memory in Agents

#### Types of Memory

**Short-term Memory**
- Current conversation
- Recent context
- Limited by context window

**Long-term Memory**
- Vector database storage
- Semantic search
- Persistent across sessions

**Entity Memory**
- Track specific entities
- Person details, facts
- Structured information

#### Memory Implementation
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
```

### 7. Agent Planning

#### Task Decomposition
```
Complex Task
  ├── Subtask 1
  │   ├── Step 1.1
  │   └── Step 1.2
  ├── Subtask 2
  └── Subtask 3
```

#### Planning Strategies

**Forward Planning**
- Start from current state
- Plan steps to goal
- Like GPS navigation

**Backward Planning**
- Start from goal
- Work backwards
- Find prerequisites

**Hierarchical Planning**
- Break into subgoals
- Plan for each subgoal
- Combine solutions

### 8. Multi-Agent Systems

#### Why Multiple Agents?
- Specialization
- Parallel processing
- Diverse perspectives
- Robustness

#### Communication Patterns

**Cooperative**
- Agents work together
- Share information
- Common goal

**Competitive**
- Agents compete
- Adversarial setup
- Improve through competition

**Hierarchical**
- Manager-worker structure
- Delegation
- Coordination

#### Example: AutoGen (Microsoft)
```python
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

user_proxy.initiate_chat(
    assistant,
    message="Task description"
)
```

### 9. Agent Evaluation

#### Success Metrics
- **Task Completion**: Did it finish?
- **Correctness**: Is result accurate?
- **Efficiency**: Steps taken
- **Cost**: API calls, tokens used

#### Challenges
- Hallucinations
- Tool misuse
- Infinite loops
- High costs
- Unpredictability

#### Guardrails
- Maximum iterations
- Cost limits
- Output validation
- Human approval for critical actions

### 10. Advanced Concepts

#### Agent with Code Interpreter
- Generate and execute code
- Data analysis
- Visualization
- Problem solving

#### Web Agents
- Browser automation
- Navigate websites
- Extract information
- Fill forms

#### Research Agents
- Literature review
- Information synthesis
- Fact-checking
- Report generation

### 11. Prompt Engineering for Agents

#### System Prompt Structure
```
You are an AI agent that can:
1. [List capabilities]
2. [Available tools]
3. [Constraints]

When given a task:
1. Think step by step
2. Use tools when needed
3. Verify results
4. Provide final answer

Format:
Thought: [reasoning]
Action: [tool name]
Action Input: [input]
Observation: [result]
... (repeat until solved)
Final Answer: [response]
```

#### Best Practices
- Clear instructions
- Tool descriptions
- Output format examples
- Error handling guidance

### 12. Real-World Applications

#### Customer Service Agents
- Answer questions
- Route tickets
- Escalate issues
- Follow up

#### Research Assistants
- Gather information
- Summarize findings
- Generate reports
- Track sources

#### Code Assistants
- Write code
- Debug errors
- Refactor
- Generate tests

#### Personal Assistants
- Schedule management
- Email handling
- Task prioritization
- Reminders

### 13. Building Your First Agent

#### Step-by-Step
1. **Define Goal**: What should agent accomplish?
2. **Choose LLM**: GPT-4, Claude, etc.
3. **Select Tools**: What functions are needed?
4. **Design Prompts**: System and user prompts
5. **Add Memory**: If needed for context
6. **Test**: Edge cases and errors
7. **Monitor**: Costs and performance
8. **Iterate**: Improve based on results

#### Starter Template
```python
from langchain.agents import Tool, AgentExecutor
from langchain.agents import create_react_agent
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Define tools
tools = [
    Tool(
        name="Tool1",
        func=tool1_func,
        description="When to use this tool"
    )
]

# Create agent
llm = OpenAI(temperature=0)
agent = create_react_agent(llm, tools, prompt_template)

# Execute
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=10
)

result = agent_executor.invoke({"input": "Your task"})
```

### 14. Agent Security & Safety

#### Risks
- Unintended actions
- Data leaks
- Malicious use
- Resource abuse

#### Mitigation
- Sandbox execution
- Permission systems
- Audit logs
- Rate limiting
- Human-in-the-loop

### 15. Future of AI Agents

#### Trends
- More autonomous
- Better reasoning
- Multi-modal (vision, audio)
- Lower costs
- Easier to build

#### Emerging Capabilities
- Long-term projects
- Learning from feedback
- Collaboration with humans
- Creative problem solving

## Connection to MCP

AI Agents are enhanced by the Model Context Protocol (MCP), which provides:
- Standardized tool interfaces
- Secure data access
- Modular capabilities
- Cross-platform compatibility

See the `05_MCP` module to learn how MCP enables more powerful agents.

## Next Steps

1. Work through agent examples
2. Build simple agent
3. Add custom tools
4. Implement memory
5. Move to MCP module

## Resources

- LangChain Documentation
- LlamaIndex Agents
- AutoGPT Repository
- BabyAGI Repository
- Microsoft AutoGen
- OpenAI Assistants API
- Anthropic Claude with Tools
