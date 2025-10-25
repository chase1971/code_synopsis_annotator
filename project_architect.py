#===============================================================================
# CODE SYNOPSIS: project_architect.py
# SYNOPSIS_HASH: b74f4c6e03c7a20782ee46d6ab8ad1ad9ec7f91d8da1f97893869f4596224377
# Generated: 2025-10-24 23:31:32
# INTENT: Extracts, Detects or identifies patterns in functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 197
#   Functions: 4
#   Classes: 0
#   Global Variables: 2
#
# Key Dependencies:
#   - collections
#   - datetime
#   - os
#   - re
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 23:31:32
# FILE: project_architect.py
# IMPORTS_EXTERNAL: collections, datetime, os, re
# IMPORTS_LOCAL: 
# GLOBALS: folder, path
# FUNCTIONS: build_project_summary, detect_exceptions, extract, extract_list
# RETURNS: build_project_summary, detect_exceptions, extract, extract_list
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: 
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: extract_list,detect_exceptions,build_project_summary
# STATE_VARS: path
# STATE_MACHINES_COUNT: 0
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Extracts, Detects or identifies patterns in functionality for this module.
# FUNCTION_INTENTS: build_project_summary=Constructs or generates project summary., detect_exceptions=Identifies exceptions., extract=Retrieves the target entities., extract_list=Retrieves list.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# build_project_summary(folder: str, output_path: str = None) -> str
#   Scans annotated Python files, parses the MACHINE-READABLE DATA block, and
#
# detect_exceptions(content: str) -> list[str]
#   Detect simple try/except exception handlers.
#
# extract(block: str, key: str) -> str
#   Extract value for a given key from a MACHINE-READABLE DATA block.
#
# extract_list(block: str, key: str) -> list[str]
#   Extract comma-separated list for a key.
#
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   Config State:
#     - path
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - extract_list()
#
# - detect_exceptions()
#
# - build_project_summary()
#
#===============================================================================
#
# 🔄 STATE MACHINES:
#
#   (No state machines detected.)
#
#===============================================================================
#
# 📊 DATA FLOW SUMMARY:
#
#   extract() — calls m.group, re.search, strip; returns value
#   extract_list() — calls extract, v.strip, val.split; returns value
#   detect_exceptions() — calls content.splitlines, enumerate, line.strip, result.append, split, startswith; returns value
#   build_project_summary() — reads path; writes path; calls append, data_flow.items, datetime.now, defaultdict, dependencies.items, extract; returns value
#===============================================================================
#
# 🔧 MODULARIZATION RECOMMENDATIONS:
#
# ⚠️ GLOBAL STATE: Significant global variables found.
#    1. Create a State class to hold all globals
#    2. Pass state object instead of using globals
#    3. Use getter/setter methods for thread-safe access
#
#===============================================================================
#===============================================================================
# 📞 FUNCTION CALL HIERARCHY:
#   (No intra-module function calls detected.)
#===============================================================================
# 🔄 STATE MACHINE TRANSITIONS:
#   (No *_state transitions detected.)
#===============================================================================
# ⌨️ HOTKEY BINDINGS:
#   (No keyboard hotkeys detected.)
#===============================================================================
#
# 🧩 MODULE INTEGRATION INTENT:
#   Role: Single-file code analyzer that injects a synopsis header
#   Used by: (future) system_synopsis_builder.py for folder-wide Markdown
#   Inputs: Python source file path
#   Outputs: Annotated source file (prepends this synopsis)
#===============================================================================
#
# 📝 INSTRUCTIONS FOR AI:
#   1. Preserve ALL global variable dependencies shown above
#   2. Maintain thread safety for variables accessed by multiple threads
#   3. Do NOT rename variables unless explicitly asked
#   4. Ensure all function dependencies are preserved
#   5. Keep UI-threaded calls (e.g., tk.after) on main thread or marshal via queue
#   6. Ensure hotkeys and binds still invoke the same callbacks
#===============================================================================
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
#!/usr/bin/env python3
"""
project_architect.py
Enhanced project-level architecture summarizer.

Scans annotated Python files (with MACHINE-READABLE DATA blocks)
and generates a robust PROJECT_STRUCTURE.md file that includes:
- Cross-module dependency graph
- Data flow map
- Thread/UI bindings
- File I/O summaries
- Exception handling summaries
- Schema metadata for LLM comprehension
"""

import os
import re
from datetime import datetime
from collections import defaultdict


def extract(block: str, key: str) -> str:
    """Extract value for a given key from a MACHINE-READABLE DATA block."""
    pattern = rf"{key}:(.*)"
    m = re.search(pattern, block)
    if m:
        return m.group(1).strip()
    return ""


def extract_list(block: str, key: str) -> list[str]:
    """Extract comma-separated list for a key."""
    val = extract(block, key)
    if not val:
        return []
    return [v.strip() for v in val.split(",") if v.strip()]


def detect_exceptions(content: str) -> list[str]:
    """Detect simple try/except exception handlers."""
    lines = content.splitlines()
    result = []
    for i, line in enumerate(lines):
        if line.strip().startswith("except "):
            result.append(line.strip().split(":")[0])
    return result


def build_project_summary(folder: str, output_path: str = None) -> str:
    """
    Scans annotated Python files, parses the MACHINE-READABLE DATA block, and
    compiles a system-level markdown including per-module INTENT lines.

    Adds/updates sections:
      - Module Dependency Graph (mermaid)
      - Cross-Module Data Flow Map (table)
      - Module Summaries (now includes 'Intent' if present)
      - Data Schema Summary
    """
    from collections import defaultdict
    import os
    
    # If no output path specified, write to the folder being analyzed
    if output_path is None:
        output_path = os.path.join(folder, "PROJECT_STRUCTURE.md")

    summaries = []
    dependencies = defaultdict(list)
    data_flow = defaultdict(list)

    files = []
    for root, _dirs, fnames in os.walk(folder):
        for name in fnames:
            if name.endswith((".py", ".pyw")):
                files.append(os.path.join(root, name))
    files.sort()

    for path in files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            continue

        # Pull out the MACHINE-READABLE block contents if present
        m = re.search(r"BEGIN MACHINE-READABLE DATA.*?\n(.*?)# END MACHINE-READABLE DATA",
                      content, flags=re.DOTALL)
        block = m.group(1) if m else ""

        file_name = os.path.basename(path)
        imports_local = extract(block, "IMPORTS_LOCAL")
        imports_external = extract(block, "IMPORTS_EXTERNAL")
        classes = extract(block, "CLASSES")
        functions = extract(block, "FUNCTIONS")
        globals_ = extract(block, "GLOBALS")
        threads = extract(block, "THREAD_TARGETS")
        tk_binds = extract(block, "TK_BINDS")
        hotkeys = extract(block, "HOTKEYS")
        io_reads = extract(block, "IO_READS")
        io_writes = extract(block, "IO_WRITES")
        exceptions = extract(block, "EXCEPTIONS")
        intent_line = extract(block, "INTENT")  # <=== NEW

        # Track dependencies for the mermaid graph
        if imports_local:
            for mname in [s.strip() for s in imports_local.split(",") if s.strip()]:
                dependencies[file_name].append(mname)

        # Minimal cross-flow capture
        if functions:
            data_flow[file_name].append("Functions: " + functions[:200] + ("..." if len(functions) > 200 else ""))

        summaries.append({
            "file": file_name,
            "classes": classes,
            "functions": functions,
            "globals": globals_,
            "imports_local": imports_local,
            "imports_external": imports_external,
            "io_reads": io_reads,
            "io_writes": io_writes,
            "threads": threads,
            "ui_binds": tk_binds,
            "hotkeys": hotkeys,
            "exceptions": exceptions,
            "intent": intent_line,  # <=== NEW
        })

    # Build markdown
    md = []
    md.append("# 🧩 PROJECT STRUCTURE SUMMARY")
    md.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    md.append("This document provides a full architectural map of the project.\n")

    # Mermaid dependency graph
    md.append("## 🧱 Module Dependency Graph\n")
    md.append("```mermaid")
    md.append("graph TD")
    for src, dsts in sorted(dependencies.items()):
        src_node = src
        for dst in sorted(set(dsts)):
            md.append(f"    {src_node} --> {dst}")
    md.append("```")
    md.append("")

    # Cross-Module Data Flow Map
    md.append("## 🔄 Cross-Module Data Flow Map\n")
    md.append("| Source Module | Target or Description |")
    md.append("|----------------|----------------------|")
    for mod, items in sorted(data_flow.items()):
        for desc in items:
            md.append(f"| {mod} | {desc} |")
    md.append("")

    # Module Summaries (NOW includes 'Intent')
    md.append("## 📦 Module Summaries\n")
    for s in summaries:
        md.append(f"### `{s['file']}`\n")
        if s.get("intent"):
            md.append(f"**Intent:** {s['intent']}\n")
        md.append("**Classes:** " + (s['classes'] or "_None_"))
        md.append("\n**Functions:** " + (s['functions'] or "_None_"))
        md.append("\n**Globals:** " + (s['globals'] or "_None_"))
        md.append("\n\n**Local Imports:** " + (s['imports_local'] or "_None_"))
        md.append("\n**External Imports:** " + (s['imports_external'] or "_None_"))
        md.append("\n\n#### File I/O Summary")
        md.append("\n- Reads: " + (s['io_reads'] or "_None_"))
        md.append("\n- Writes: " + (s['io_writes'] or "_None_"))
        md.append("\n\n#### Threading & UI Bindings")
        md.append("\n- Threads: " + (s['threads'] or "_None_"))
        md.append("\n- UI Binds: " + (s['ui_binds'] or "_None_"))
        md.append("\n\n#### Exception Paths")
        md.append("\n" + (s['exceptions'] or "_No exception handlers detected._"))
        md.append("\n\n---\n")

    # Data schema summary (unchanged)
    md.append("## 🧠 DATA SCHEMA SUMMARY\n")
    md.append("```json")
    md.append('{\n  "ModuleSummary": {\n    "file": "str",\n    "classes": ["list[str]"],\n    "functions": ["list[str]"],\n    "globals": ["list[str]"],\n    "imports_local": ["list[str]"],\n    "imports_external": ["list[str]"],\n    "io_reads": ["list[str]"],\n    "io_writes": ["list[str]"],\n    "threads": ["list[str]"],\n    "ui_binds": ["list[str]"],\n    "exceptions": ["list[str]"],\n    "intent": "str"\n  }\n}')
    md.append("```")

    output = "\n".join(md) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    return output_path


if __name__ == "__main__":
    folder = os.getcwd()
    print("Generating enhanced PROJECT_STRUCTURE.md ...")
    path = build_project_summary(folder)
    print(f"✅ Project summary generated: {path}")
