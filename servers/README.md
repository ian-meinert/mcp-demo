# Medicare MCP Server

This directory contains the Medicare MCP server and related modules for serving, analyzing, and answering questions about Medicare datasets and documents.

## Structure

- `medicare_server.py`: Main entry point for the Medicare MCP server, exposing resources, tools, and prompts.
- `datasets.py`: Utilities for fetching datasets, reading documents, and listing available files.
- `decorators.py`: Decorators for access control and other shared logic.

## Key Features

- Exposes Medicare datasets as resources (e.g., nursing home, deficit reduction datasets)
- Provides tools for row counts, column listing, and column summarization
- Supports document access and search in the `documents/medicare` folder
- Includes prompts to guide agents in using the server effectively

## Usage

From the project root, run:

```
uv run mcp dev servers/medicare_server.py
```

Or, if you need to set the Python path:

```
PYTHONPATH=. uv run mcp dev servers/medicare_server.py
```

## Adding Datasets or Documents

- To add a new dataset, update `datasets.py` with the new dataset ID.
- To add a new document, place the file in `documents/medicare/`.

## Agent Guidance

- Use the `explain_tool_resource_flow` prompt for an overview of how to combine tools and resources.
- Use `list_medicare_datasets` and `list_medicare_documents` to discover available data.

---
For more details, see the code comments and prompts in `medicare_server.py`.
