# Slide Layout Auto-Rebalancer Skill for Autonomous Agents

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue.svg)](https://modelcontextprotocol.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](requirements.txt)

Intelligent slide layout and canvas AST optimizer. Rebalances coordinates, eliminates element collisions, enforces strict 16:9 canvas boundaries (1920x1080), and harmonizes typographic padding for automated presentation generation.

## Core Capabilities
- **Collision Elimination**: Computes 2D bounding boxes and repositions overlapping text, card, or image containers.
- **Canvas Aspect-Ratio Constraint**: Guarantees zero vertical or horizontal canvas clipping.
- **Automatic Padding & Spacing**: Balances vertical rhythm and hierarchy.

## MCP Server Integration
```bash
python mcp_server.py
```

### Available MCP Tools
- `rebalance_slide_layout`: Rebalance slide element coordinates to eliminate overlap and overflow.
