#===============================================================================
# CODE SYNOPSIS: intent_inference.py
# SYNOPSIS_HASH: 911266d3019f276ed09ba7ed2971df99ae3ba72f2ee77bab570162c1e5359ce3
# Generated: 2025-10-24 23:31:32
# INTENT: Generates functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 229
#   Functions: 8
#   Classes: 0
#   Global Variables: 3
#
# Key Dependencies:
#   - __future__
#   - re
#   - typing
#   (Local modules):
#     * intent_enhancer_v2
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 23:31:32
# FILE: intent_inference.py
# IMPORTS_EXTERNAL: __future__, re, typing
# IMPORTS_LOCAL: intent_enhancer_v2
# GLOBALS: ACTION_MAP, DEFAULT_MODULE_INTENT, DEFAULT_VERB
# FUNCTIONS: _infer_verb, _insert_human_readable_intent, _insert_machine_block_kv, _noun_phrase_from, _split_ident, generate_module_intent, infer_function_intent, inject_intent
# RETURNS: _infer_verb, _insert_human_readable_intent, _insert_machine_block_kv, _noun_phrase_from, _split_ident, generate_module_intent, infer_function_intent, inject_intent
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: 
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: inject_intent
# STATE_VARS: ACTION_MAP,DEFAULT_MODULE_INTENT,DEFAULT_VERB
# STATE_MACHINES_COUNT: 0
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Generates functionality for this module.
# FUNCTION_INTENTS: _infer_verb=Handles verb., _insert_human_readable_intent=Handles human readable intent., _insert_machine_block_kv=Handles machine block kv., _noun_phrase_from=Handles phrase from., _split_ident=Handles ident., generate_module_intent=Handles module intent., infer_function_intent=Handles function intent., inject_intent=Handles intent.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# _infer_verb(tokens: List[str]) -> Tuple[str, str]
#
# _insert_human_readable_intent(header_text: str, human_intent: str) -> str
#   Insert a '# INTENT: ...' line near the top (after SYNOPSIS_HASH if present).
#
# _insert_machine_block_kv(header_text: str, key: str, value: str) -> str
#   Insert or update a key: value inside the MACHINE-READABLE DATA block.
#
# _noun_phrase_from(tokens: List[str], skip_first: bool = True) -> str
#
# _split_ident(name: str) -> List[str]
#
# generate_module_intent(analyzer) -> str
#   Use function names and imports to synthesize a short module purpose line.
#
# infer_function_intent(func_name: str) -> str
#
# inject_intent(header_text: str, analyzer, behavioral_analyzer) -> str
#   Public entry point. Returns a NEW header string with:
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
#     - DEFAULT_MODULE_INTENT
#     - DEFAULT_VERB
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - inject_intent()
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
#   _split_ident() — calls c.lower, flat.append, flat.extend, p.lower, re.findall, re.split; returns value
#   _infer_verb() — reads ACTION_MAP, DEFAULT_VERB; calls ACTION_MAP.get; returns value
#   _noun_phrase_from() — reads ACTION_MAP; calls join, len; returns value
#   infer_function_intent() — calls _infer_verb, _noun_phrase_from, _split_ident; returns value
#   generate_module_intent() — reads DEFAULT_MODULE_INTENT; calls _infer_verb, _noun_phrase_from, _split_ident, dict.fromkeys, generate_smart_intent, getattr; returns value
#   _insert_human_readable_intent() — calls enumerate, header_text.splitlines, join, len, lines.insert, ln.strip; returns value
#   _insert_machine_block_kv() — calls block.replace, block_start.start, end.end, re.escape, re.search, re.sub; returns value
#   inject_intent() — calls _insert_human_readable_intent, _insert_machine_block_kv, fn_intents.append, fname.replace, generate_module_intent, infer_function_intent; returns value
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
#!/usr/bin/env python3
# =============================================================================
# INTENT INFERENCE (deterministic, no-LLM)
# =============================================================================
"""
Generates concise natural-language 'intent' strings for modules and functions
based on static signals already produced by your analyzers.

Integration:
- Called from batch_annotate_modular.process_single_file() AFTER the synopsis
  header is generated by SynopsisRenderer.
- Injects:
    1) A human-readable "# INTENT: ..." line near the top of the header, and
    2) "INTENT: ..." and "FUNCTION_INTENTS: ..." inside the
       BEGIN MACHINE-READABLE DATA block, so project_architect can extract it.
"""

from __future__ import annotations
from typing import Dict, List, Tuple
import re

ACTION_MAP = {
    "analyze": "Examines and summarizes",
    "build": "Constructs or generates",
    "detect": "Identifies",
    "extract": "Retrieves",
    "find": "Locates or gathers",
    "render": "Produces or displays",
    "group": "Organizes",
    "summarize": "Condenses results of",
    "process": "Handles or executes",
    "load": "Retrieves and prepares",
    "save": "Stores or outputs",
    "parse": "Parses",
    "read": "Reads",
    "write": "Writes",
}

# Fallbacks if we can't infer a verb from a function/method name.
DEFAULT_VERB = "Handles"
DEFAULT_MODULE_INTENT = (
    "Provides functionality related to code structure analysis and summary generation."
)


def _split_ident(name: str) -> List[str]:
    # snake_case or mixedCase → tokens
    parts = re.split(r"[_\W]+", name)
    flat: List[str] = []
    for p in parts:
        if not p:
            continue
        # split camelCase tokens
        camel = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)|\d+", p)
        if camel:
            flat.extend([c.lower() for c in camel])
        else:
            flat.append(p.lower())
    return [t for t in flat if t]


def _infer_verb(tokens: List[str]) -> Tuple[str, str]:
    if not tokens:
        return DEFAULT_VERB, ""
    head = tokens[0]
    phrase = ACTION_MAP.get(head)
    if phrase:
        return phrase, head
    # look ahead a couple tokens
    for t in tokens[:3]:
        phrase = ACTION_MAP.get(t)
        if phrase:
            return phrase, t
    return DEFAULT_VERB, ""


def _noun_phrase_from(tokens: List[str], skip_first: bool = True) -> str:
    if skip_first and tokens:
        tokens = tokens[1:]
    tokens = [t for t in tokens if t not in ACTION_MAP]
    if not tokens:
        return "the target entities"
    # keep it short
    if len(tokens) > 5:
        tokens = tokens[:5]
    return " ".join(tokens)


def infer_function_intent(func_name: str) -> str:
    tokens = _split_ident(func_name)
    verb_phrase, _ = _infer_verb(tokens)
    obj_phrase = _noun_phrase_from(tokens, skip_first=True)
    # shape final sentence
    return f"{verb_phrase} {obj_phrase}."


def generate_module_intent(analyzer) -> str:
    """
    Use function names and imports to synthesize a short module purpose line.
    """
    # USE ENHANCED INTENT GENERATOR
    try:
        from intent_enhancer_v2 import generate_smart_intent
        return generate_smart_intent(analyzer)
    except ImportError:
        pass  # Fall back to original implementation below
    
    # Original implementation (fallback)
    func_names = sorted((analyzer.functions or {}).keys())
    if not func_names:
        # fall back to file name
        base = (getattr(analyzer, "filename", None) or "").replace(".py", "")
        tokens = _split_ident(base) if base else []
        if tokens:
            verb_phrase, _ = _infer_verb(tokens)
            obj_phrase = _noun_phrase_from(tokens, skip_first=True)
            return f"{verb_phrase} {obj_phrase}."
        return DEFAULT_MODULE_INTENT

    # Build a small bag-of-words from function names
    intents = [infer_function_intent(n) for n in func_names[:10]]
    # Try to compress a coherent line based on the top verbs
    verbs = []
    for n in func_names[:6]:
        v, _ = _infer_verb(_split_ident(n))
        verbs.append(v.split()[0].lower())
    verbs = [v for v in verbs if v]
    if verbs:
        verbs = list(dict.fromkeys(verbs))  # preserve order, dedupe
        head = ", ".join(verbs[:3])
        return f"{head.capitalize()} core behaviors for this module, derived from its primary routines."

    # Fallback: join a couple of intents
    if intents:
        # Strip trailing periods and join
        short = "; ".join([s[:-1] if s.endswith(".") else s for s in intents[:2]])
        return short + "."
    return DEFAULT_MODULE_INTENT


def _insert_human_readable_intent(header_text: str, human_intent: str) -> str:
    """
    Insert a '# INTENT: ...' line near the top (after SYNOPSIS_HASH if present).
    """
    lines = header_text.splitlines()
    # Find an anchor (SYNOPSIS_HASH or Generated line)
    insert_at = None
    for i, ln in enumerate(lines[:40]):
        if ln.strip().startswith("# SYNOPSIS_HASH:"):
            insert_at = i + 1
            break
    if insert_at is None:
        for i, ln in enumerate(lines[:40]):
            if ln.strip().startswith("# Generated:"):
                insert_at = i + 1
                break
    if insert_at is None:
        insert_at = min(3, len(lines))
    lines.insert(insert_at, f"# INTENT: {human_intent}")
    return "\n".join(lines)


def _insert_machine_block_kv(header_text: str, key: str, value: str) -> str:
    """
    Insert or update a key: value inside the MACHINE-READABLE DATA block.
    If block not found, no-op (return original).
    """
    block_start = re.search(r"BEGIN MACHINE-READABLE DATA.*", header_text)
    if not block_start:
        return header_text

    # Find the 'END MACHINE-READABLE DATA' boundary
    end = re.search(r"END MACHINE-READABLE DATA", header_text)
    if not end:
        return header_text

    start_idx = block_start.start()
    end_idx = end.end()

    before = header_text[:start_idx]
    block = header_text[start_idx:end_idx]
    after = header_text[end_idx:]

    # If key exists, replace; else, append at the end of block (before END)
    if re.search(rf"^{re.escape(key)}:", block, flags=re.MULTILINE):
        block = re.sub(rf"^{re.escape(key)}:.*$",
                       f"{key}: {value}", block, flags=re.MULTILINE)
    else:
        block = block.replace("END MACHINE-READABLE DATA", f"{key}: {value}\n# END MACHINE-READABLE DATA")

    return before + block + after


def inject_intent(header_text: str, analyzer, behavioral_analyzer) -> str:
    """
    Public entry point. Returns a NEW header string with:
      - '# INTENT: ...' (human-readable)
      - 'INTENT: ...' (inside MACHINE-READABLE block)
      - 'FUNCTION_INTENTS: name1=..., name2=...' (inside MACHINE-READABLE block)
    """
    # 1) Module-level human-readable
    module_intent = generate_module_intent(analyzer)

    updated = _insert_human_readable_intent(header_text, module_intent)

    # 2) Machine-readable INTENT (single line)
    updated = _insert_machine_block_kv(updated, "INTENT", module_intent)

    # 3) Machine-readable FUNCTION_INTENTS (compact kv-list)
    fn_intents: List[str] = []
    for fname in sorted((analyzer.functions or {}).keys()):
        try:
            intent = infer_function_intent(fname)
            # sanitize separators
            safe_name = fname.replace(",", "_").replace("=", "_")
            safe_intent = intent.replace(",", ";")
            fn_intents.append(f"{safe_name}={safe_intent}")
        except Exception:
            # avoid blocking due to any odd names
            continue

    if fn_intents:
        updated = _insert_machine_block_kv(updated, "FUNCTION_INTENTS", ", ".join(fn_intents))

    return updated
