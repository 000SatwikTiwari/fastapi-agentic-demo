# FastAPI Notes Service (Demo Project)

This is a small FastAPI project that implements a basic Notes API.

The purpose of this project is **not** to be production complete, but to act as a realistic codebase for experimenting with development workflows using Claude Code CLI in a git-based environment.

## Features

- Create a note
- List all notes
- Get a note by ID

## Missing / Intentionally Incomplete

This project is intentionally incomplete and has areas that can be improved:

- No update note endpoint
- No delete note endpoint
- No persistent storage (in-memory only)
- No validation for edge cases
- No tests for error scenarios
- No logging
- No proper project structure separation

These gaps are intentional and will be used as tasks for Claude Code.

## Run the project

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
