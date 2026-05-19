Link: https://adk.dev/agents/workflow-agents/

### Introduction 
This section introduces "workflow agents" - specialized agents that control the execution flow of its sub-agents.

Workflow agents are specialized components in ADK designed purely for orchestrating the execution flow of sub-agents. Their primary role is to manage how and when other agents run, defining the control flow of a process.

Unlike LLM Agents, which use Large Language Models for dynamic reasoning and decision-making, Workflow Agents operate based on predefined logic. They determine the execution sequence according to their type (e.g., sequential, parallel, loop) without consulting an LLM for the orchestration itself. This results in deterministic and predictable execution patterns.

ADK provides three core workflow agent types, each implementing a distinct execution pattern:

### Types

Sequential Agents: Executes sub-agents one after another, in sequence

Loop Agents: Repeatedly executes its sub-agents until a specific termination condition is met.

Parallel Agents: Executes multiple sub-agents in parallel.

Custom Agents: Custom agents and agent-based workflows allow you to define arbitrary orchestration logic by inheriting directly from BaseAgent and implementing your own control flow. This approach allows you to create new execution patterns similar to SequentialAgent, LoopAgent, and ParallelAgent, enabling you to build highly specific and complex agentic workflows.
     - by more flexible workflow structures, including graph-based workflows and dynamic workflows. You should evaluate the capabilities of these workflow mechanisms before building a custom agent for your target workflow.