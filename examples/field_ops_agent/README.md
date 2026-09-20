# Field Operations Assistant Example

## Overview
A field technician submits unstructured job notes (and optionally photos). The assistant parses the notes, creates a structured job record, generates follow‑up tasks, and drafts a customer update.

## Workflow Diagram
```
[Technician] --> Submit notes/photos --> [FieldOps Agent]
    |
    | parses
    v
[Parsed Data] --> Create JobRecord (JSON) --> Store in DB
    |
    | generate
    v
[Follow‑Up Tasks] --> Queue for execution (order parts, schedule visit, etc.)
    |
    | draft
    v
[Customer Email] --> Send to client
```

## Features
- **Dataclasses** for `JobReport`, `FollowUpTask`, `FieldNote`
- **Robust parsing** tolerant of noisy free‑text
- **Template‑based** generation of a markdown job report and customer email
- **CLI runnable**: `python3 workflow.py` prints the full pipeline output

## Getting Started
```sh
cd examples/field_ops_agent  # from the repository root
python3 workflow.py
```

## Acceptance Criteria
- All required files present
- Script runs without errors on the provided sample notes
- Demonstrates parsing, structuring, task generation, and customer communication
