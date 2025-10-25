#===============================================================================
# CODE SYNOPSIS: state_tracker.py
# SYNOPSIS_HASH: d0cf4c4fbc1951aafd926b9bee9ae549fd2e88a06f7f2662594e44e4a3713734
# Generated: 2025-10-25 13:00:59
# INTENT: Loads and manages configuration settings. Extracts various components.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 289
#   Functions: 8
#   Classes: 0
#   Global Variables: 10
#
# Key Dependencies:
#   - datetime
#   - json
#   - os
#   - pathlib
#   - re
#   - typing
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-25 13:00:59
# FILE: state_tracker.py
# IMPORTS_EXTERNAL: datetime, json, os, pathlib, re, typing
# IMPORTS_LOCAL: 
# GLOBALS: BEGIN_MARK, BULLET_RE, CRIT_GLOBALS_HEADER, END_MARK, KEY_ALIASES, KEY_LINE_RE, VAR_HEADER_RE, folder, out_md, state
# FUNCTIONS: _strip_comment_prefix, append_to_project_structure, build_state_table, extract_blocks, extract_critical_globals, generate_state_markdown, merge_file_state_from_text, parse_block
# RETURNS: _strip_comment_prefix, build_state_table, extract_blocks, extract_critical_globals, generate_state_markdown, merge_file_state_from_text, parse_block
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: 
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: _strip_comment_prefix,build_state_table,generate_state_markdown,append_to_project_structure
# STATE_VARS: BEGIN_MARK,BULLET_RE,CRIT_GLOBALS_HEADER,END_MARK,KEY_ALIASES,KEY_LINE_RE,VAR_HEADER_RE,state
# STATE_MACHINES_COUNT: 1
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Loads and manages configuration settings. Extracts various components.
# FUNCTION_INTENTS: _strip_comment_prefix=Remove leading '# ' or '#' and return trimmed content., append_to_project_structure=Append the shared-state section to PROJECT_STRUCTURE., build_state_table=Walk the folder and build:., extract_blocks=All MACHINE-READABLE DATA blocks from a file's content., extract_critical_globals=Parse the 'CRITICAL GLOBAL VARIABLES' section from a synopsis header., generate_state_markdown=Create markdown for the Shared State Table., merge_file_state_from_text=Parse both MACHINE-READABLE and CRITICAL GLOBAL VARIABLES sections., parse_block=Parse one MACHINE-READABLE block into:.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# _strip_comment_prefix(line: str) -> str
#   Remove leading '# ' or '#' and return trimmed content.
#
# append_to_project_structure(project_folder: str, shared_state_md: str) -> None
#   Append the shared-state section to PROJECT_STRUCTURE.md.
#
# build_state_table(folder: str) -> Dict[str, Dict[str, Dict[str, List[str]]]]
#   Walk the folder and build:
#
# extract_blocks(text: str) -> List[str]
#   Return all MACHINE-READABLE DATA blocks from a file's content.
#
# extract_critical_globals(text: str) -> Dict[str, Dict[str, Set[str]]]
#   Parse the 'CRITICAL GLOBAL VARIABLES' section from a synopsis header.
#
# generate_state_markdown(state_map: Dict[str, Dict[str, Dict[str, List[str]]]], output_path: str = None) -> str
#   Create markdown for the Shared State Table.
#
# merge_file_state_from_text(file_path: str) -> Dict[str, Dict[str, Set[str]]]
#   Parse both MACHINE-READABLE and CRITICAL GLOBAL VARIABLES sections.
#
# parse_block(block: str) -> Dict[str, Dict[str, Set[str]]]
#   Parse one MACHINE-READABLE block into:
#
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   Control State:
#     - state
#   Timing State:
#     - END_MARK
#   Position State:
#     - KEY_ALIASES
#     - KEY_LINE_RE
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - _strip_comment_prefix()
#
# - build_state_table()
#
# - generate_state_markdown()
#
# - append_to_project_structure()
#
#===============================================================================
#
# 🔄 STATE MACHINES DETECTED:
#
#   📍 state (State Variable):
#      States: (values unknown)
#
#
#===============================================================================
#
# 🔄 STATE MACHINE DIAGRAMS:
#
# ```mermaid
# stateDiagram-v2
#     [*] --> Unknown
# ```
#
#
# 📊 DATA FLOW SUMMARY:
#
#   _strip_comment_prefix() — calls line.lstrip, line.startswith, line.strip; returns value
#   extract_blocks() — reads BEGIN_MARK, END_MARK; calls blocks.append, current.append, join, text.splitlines; returns value
#   parse_block() — reads BULLET_RE, KEY_ALIASES, KEY_LINE_RE, VAR_HEADER_RE; calls BULLET_RE.match, KEY_ALIASES.get, KEY_LINE_RE.match, VAR_HEADER_RE.match, add, block.splitlines; returns value
#   merge_file_state_from_text() — calls Path, crit_rels.items, extract_blocks, extract_critical_globals, merged.setdefault, parse_block; returns value
#   extract_critical_globals() — reads CRIT_GLOBALS_HEADER, KEY_ALIASES, KEY_LINE_RE, VAR_HEADER_RE; calls CRIT_GLOBALS_HEADER.search, KEY_ALIASES.get, KEY_LINE_RE.match, VAR_HEADER_RE.match, ln.strip, lower; returns value
#   build_state_table() — calls f.endswith, merge_file_state_from_text, os.path.join, os.walk, rels.items, rr.get; returns value
#   generate_state_markdown() — calls Path, datetime.now, globals_dict.items, join, lines.append, rel.get; returns value
#   append_to_project_structure() — calls Path, f.write, ps_path.exists, ps_path.open, ps_path.write_text; no return value
#===============================================================================
#
# 🔧 MODULARIZATION RECOMMENDATIONS:
#
# ⚠️ GLOBAL STATE: Significant global variables found.
#    1. Create a State class to hold all globals
#    2. Pass state object instead of using globals
#    3. Use getter/setter methods for thread-safe access
#
# When modularizing, consider splitting by:
#   - Separate state management from business logic
#   - Group related functions into modules
#   - Separate UI code from core logic
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
#!/usr/bin/env python3
# =============================================================================
# STATE TRACKER (ROBUST PARSER)
# =============================================================================
# Purpose:
#   Robustly extract global variable "Modified by" / "Read by" relations
#   from MACHINE-READABLE DATA blocks in annotated .py/.pyw files.
#
#   Supports flexible formats:
#     - CSV lines:
#         #   Modified by: f1, f2
#         #   Read by: g1, g2
#     - Bulleted lists:
#         #   Modified by:
#         #     - f1
#         #     - f2
#
#   Normalizes to keys: writers (Modified by) and readers (Read by).
#   Generates a Markdown table; can append directly to PROJECT_STRUCTURE.md.
# =============================================================================

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple

# -------------- Block and header markers --------------
BEGIN_MARK = "BEGIN MACHINE-READABLE DATA"
END_MARK = "END MACHINE-READABLE DATA"

# A line that defines a variable header inside the block, e.g.:
#   # paused:
VAR_HEADER_RE = re.compile(r"^\s*#\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*$")

# A key line that starts a CSV or a section, e.g.:
#   #   Modified by: f1, f2
#   #   Read by:
#     - f1
KEY_LINE_RE = re.compile(r"^\s*#\s*(Modified by|Read by)\s*:\s*(.*)$", re.IGNORECASE)

# A bullet entry, e.g.:
#   #     - f1
BULLET_RE = re.compile(r"^\s*#\s*[-*]\s*(\S.*)$")

# Accept legacy synonyms
KEY_ALIASES = {
    "modified by": "writers",
    "read by": "readers",
    # fallbacks if some files wrote 'writes/reads'
    "writers": "writers",
    "writes": "writers",
    "readers": "readers",
    "reads": "readers",
}

def _strip_comment_prefix(line: str) -> str:
    """Remove leading '# ' or '#' and return trimmed content."""
    line = line.lstrip()
    if line.startswith("#"):
        line = line[1:]
    return line.strip()

def extract_blocks(text: str) -> List[str]:
    """Return all MACHINE-READABLE DATA blocks from a file's content."""
    blocks: List[str] = []
    lines = text.splitlines()
    in_block = False
    current: List[str] = []
    for ln in lines:
        if BEGIN_MARK in ln:
            in_block = True
            current = []
            continue
        if END_MARK in ln and in_block:
            in_block = False
            blocks.append("\n".join(current))
            current = []
            continue
        if in_block:
            current.append(ln)
    return blocks

def parse_block(block: str) -> Dict[str, Dict[str, Set[str]]]:
    """
    Parse one MACHINE-READABLE block into:
      { var_name: { "writers": set(...), "readers": set(...) } }
    """
    rels: Dict[str, Dict[str, Set[str]]] = {}
    lines = block.splitlines()
    current_var = None
    pending_key = None  # "writers" or "readers" when reading bullet section

    for raw in lines:
        # Detect variable header: "# paused:"
        m_var = VAR_HEADER_RE.match(raw)
        if m_var:
            current_var = m_var.group(1)
            rels.setdefault(current_var, {"writers": set(), "readers": set()})
            pending_key = None
            continue

        # If there's no current var, skip until we find one
        if not current_var:
            continue

        # Detect key line: "#   Modified by: f1, f2"  OR start of section "#   Read by:"
        m_key = KEY_LINE_RE.match(raw)
        if m_key:
            key_raw = m_key.group(1).strip().lower()
            value = m_key.group(2).strip()
            norm_key = KEY_ALIASES.get(key_raw, None)
            if not norm_key:
                # Try direct fallback if already normalized
                norm_key = KEY_ALIASES.get(key_raw.lower(), None)
            if not norm_key:
                # Unknown key; skip
                pending_key = None
                continue

            if value:
                # CSV values on same line
                parts = [p.strip() for p in value.split(",") if p.strip()]
                rels[current_var][norm_key].update(parts)
                pending_key = None
            else:
                # Start bullet capture mode
                pending_key = norm_key
            continue

        # Capture bullet entries if we're in a section
        if pending_key:
            m_b = BULLET_RE.match(raw)
            if m_b:
                entry = m_b.group(1).strip()
                # Stop if this looks like a new header (defensive)
                if entry.endswith(":"):
                    pending_key = None
                else:
                    rels[current_var][pending_key].add(entry)
                continue

        # If line is blank or unrelated, continue scanning
        # (We rely on new VAR_HEADER_RE to reset current_var/pending_key)

    return rels

def merge_file_state_from_text(file_path: str) -> Dict[str, Dict[str, Set[str]]]:
    """Parse both MACHINE-READABLE and CRITICAL GLOBAL VARIABLES sections."""
    try:
        text = Path(file_path).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return {}

    merged: Dict[str, Dict[str, Set[str]]] = {}

    # 1️⃣ Machine-readable data blocks
    for block in extract_blocks(text):
        rels = parse_block(block)
        for var, rr in rels.items():
            merged.setdefault(var, {"writers": set(), "readers": set()})
            merged[var]["writers"].update(rr.get("writers", set()))
            merged[var]["readers"].update(rr.get("readers", set()))

    # 2️⃣ Critical Globals section
    crit_rels = extract_critical_globals(text)
    for var, rr in crit_rels.items():
        merged.setdefault(var, {"writers": set(), "readers": set()})
        merged[var]["writers"].update(rr.get("writers", set()))
        merged[var]["readers"].update(rr.get("readers", set()))

    return merged

CRIT_GLOBALS_HEADER = re.compile(r"^#\s*CRITICAL GLOBAL VARIABLES", re.IGNORECASE)

def extract_critical_globals(text: str) -> Dict[str, Dict[str, Set[str]]]:
    """
    Parse the 'CRITICAL GLOBAL VARIABLES' section from a synopsis header.
    Expected format:
        # CRITICAL GLOBAL VARIABLES
        # paused:
        #   Modified by: unified_pause_toggle, dwell_click
        #   Read by: toggle_lock_pause
    """
    rels: Dict[str, Dict[str, Set[str]]] = {}
    lines = text.splitlines()
    in_section = False
    current_var = None

    for ln in lines:
        if CRIT_GLOBALS_HEADER.search(ln):
            in_section = True
            continue
        if in_section and ln.strip().startswith("# ==="):
            # Reached a boundary or end of header
            break
        if not in_section:
            continue

        # Match variable headers like "# paused:"
        m_var = VAR_HEADER_RE.match(ln)
        if m_var:
            current_var = m_var.group(1)
            rels.setdefault(current_var, {"writers": set(), "readers": set()})
            continue

        # Match key/value lines
        m_key = KEY_LINE_RE.match(ln)
        if m_key and current_var:
            key_raw = m_key.group(1).strip().lower()
            val = m_key.group(2).strip()
            norm_key = KEY_ALIASES.get(key_raw, None)
            if not norm_key:
                continue
            if val:
                rels[current_var][norm_key].update(
                    [p.strip() for p in val.split(",") if p.strip()]
                )
    return rels

def build_state_table(folder: str) -> Dict[str, Dict[str, Dict[str, List[str]]]]:
    """
    Walk the folder and build:
      { file_name: { var: {"modified_by": [...], "read_by": [...] } } }
    """
    state_map: Dict[str, Dict[str, Dict[str, List[str]]]] = {}
    for root, _, files in os.walk(folder):
        for f in files:
            if not (f.endswith(".py") or f.endswith(".pyw")):
                continue
            fp = os.path.join(root, f)
            rels = merge_file_state_from_text(fp)
            if not rels:
                continue
            # normalize to lists and legacy keys for table
            normalized: Dict[str, Dict[str, List[str]]] = {}
            for var, rr in rels.items():
                writers = sorted(rr.get("writers", set()))
                readers = sorted(rr.get("readers", set()))
                normalized[var] = {
                    "modified_by": writers,
                    "read_by": readers,
                }
            if normalized:
                state_map[f] = normalized
    return state_map

def generate_state_markdown(
    state_map: Dict[str, Dict[str, Dict[str, List[str]]]],
    output_path: str = None
) -> str:
    """Create markdown for the Shared State Table."""
    lines: List[str] = [
        "# 🧩 SHARED STATE TABLE",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "| File | Variable | Modified By | Read By |",
        "|------|-----------|-------------|---------|",
    ]
    for file_name, globals_dict in sorted(state_map.items()):
        for var, rel in sorted(globals_dict.items()):
            mods = ", ".join(rel.get("modified_by", [])) or "-"
            reads = ", ".join(rel.get("read_by", [])) or "-"
            lines.append(f"| {file_name} | `{var}` | {mods} | {reads} |")
    md = "\n".join(lines)
    if output_path:
        Path(output_path).write_text(md, encoding="utf-8")
    return md

def append_to_project_structure(project_folder: str, shared_state_md: str):
    """Append the shared-state section to PROJECT_STRUCTURE.md."""
    ps_path = Path(project_folder) / "PROJECT_STRUCTURE.md"
    if not ps_path.exists():
        # Create if missing
        ps_path.write_text("# Project Structure\n\n", encoding="utf-8")
    with ps_path.open("a", encoding="utf-8") as f:
        f.write("\n\n---\n\n")
        f.write(shared_state_md)

if __name__ == "__main__":
    folder = str(Path(__file__).parent)
    state = build_state_table(folder)
    out_md = generate_state_markdown(state)  # no separate file; we'll append
    append_to_project_structure(folder, out_md)
    print("✅ Shared state appended to PROJECT_STRUCTURE.md")