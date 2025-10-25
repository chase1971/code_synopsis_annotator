#===============================================================================
# CODE SYNOPSIS: intent_inference.py
# SYNOPSIS_HASH: f4045c35d5b9c59acb5366d27dee71deba345aca4f1bf6c0346de459c08286ff
# Generated: 2025-10-25 13:00:59
# INTENT: Generates functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 382
#   Functions: 10
#   Classes: 0
#   Global Variables: 3
#
# Key Dependencies:
#   - __future__
#   - ast
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
# LAST_ANALYZED: 2025-10-25 13:00:59
# FILE: intent_inference.py
# IMPORTS_EXTERNAL: __future__, ast, re, typing
# IMPORTS_LOCAL: intent_enhancer_v2
# GLOBALS: ACTION_MAP, DEFAULT_MODULE_INTENT, DEFAULT_VERB
# FUNCTIONS: _analyze_function_body, _enhance_with_type_hints, _infer_verb, _insert_human_readable_intent, _insert_machine_block_kv, _noun_phrase_from, _split_ident, generate_module_intent, infer_function_intent, inject_intent
# RETURNS: _analyze_function_body, _enhance_with_type_hints, _infer_verb, _insert_human_readable_intent, _insert_machine_block_kv, _noun_phrase_from, _split_ident, generate_module_intent, infer_function_intent, inject_intent
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
# FUNCTION_INTENTS: _analyze_function_body=Infer intent from function body patterns., _enhance_with_type_hints=Enhance intent using return type hints., _infer_verb=Iterates and processes items., _insert_human_readable_intent=Insert a '# INTENT:., _insert_machine_block_kv=Insert or update a key: value inside the MACHINE-READABLE DATA block., _noun_phrase_from=Returns string representation., _split_ident=Iterates and processes items., generate_module_intent=Use function names and imports to synthesize a short module purpose line., infer_function_intent=Generate function intent using priority cascade:., inject_intent=Public entry point.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# _analyze_function_body(func_node: ast.FunctionDef) -> str
#   Infer intent from function body patterns.
#
# _enhance_with_type_hints(func_name: str, func_node: ast.FunctionDef) -> str
#   Enhance intent using return type hints.
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
# infer_function_intent(func_name: str, func_node: ast.FunctionDef = None) -> str
#   Generate function intent using priority cascade:
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
#   _analyze_function_body() — calls any, ast.walk, hasattr, isinstance, len, sum; returns value
#   _enhance_with_type_hints() — calls ast.unparse, func_name.startswith, return_type.startswith; returns value
#   infer_function_intent() — calls _analyze_function_body, _enhance_with_type_hints, _infer_verb, _noun_phrase_from, _split_ident, ast.get_docstring; returns value
#   generate_module_intent() — reads DEFAULT_MODULE_INTENT; calls _infer_verb, _noun_phrase_from, _split_ident, dict.fromkeys, generate_smart_intent, getattr; returns value
#   _insert_human_readable_intent() — calls enumerate, header_text.splitlines, join, len, lines.insert, ln.strip; returns value
#   _insert_machine_block_kv() — calls block.replace, block_start.start, end.end, re.escape, re.search, re.sub; returns value
#   inject_intent() — calls _insert_human_readable_intent, _insert_machine_block_kv, analyzer.functions.get, fn_intents.append, fname.replace, func_data.get; returns value
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
import ast

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


def _get_all_calls(func_node: ast.FunctionDef) -> List[str]:
    """Extract all function/method calls from a function body."""
    calls = []
    for node in ast.walk(func_node):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                # Build full method name like 'os.path.exists'
                parts = []
                n = node.func
                while isinstance(n, ast.Attribute):
                    parts.append(n.attr)
                    n = n.value
                if isinstance(n, ast.Name):
                    parts.append(n.id)
                calls.append('.'.join(reversed(parts)))
    return calls


def _check_api_patterns(func_node: ast.FunctionDef) -> str:
    """Check for specific API patterns to infer more accurate intents with combination patterns."""
    if not func_node or not func_node.body:
        return None
    
    calls = _get_all_calls(func_node)
    call_set = set(calls)
    
    # COMBINATION PATTERNS (check these FIRST for multi-purpose functions)
    
    # Window creation + keyboard simulation (like show_arrow_overlay) - HIGHEST PRIORITY
    if (any(pattern in call_set for pattern in ['Toplevel', 'tk.Toplevel', 'geometry']) and
        any(pattern in call_set for pattern in ['keyboard.press', 'keyboard.release'])):
        return "Creates GUI window with keyboard input capabilities"
    
    # File operations + UI operations (like watch_for_signals)
    if (any(pattern in call_set for pattern in ['os.path.exists', 'os.remove']) and
        any(pattern in call_set for pattern in ['after', 'deiconify', 'withdraw'])):
        return "Manages file-based event signals and UI updates"
    
    # Mouse + Keyboard combination (like poll function) - LOWER PRIORITY
    if ('pyautogui.position' in call_set and 
        any(pattern in call_set for pattern in ['keyboard.press', 'keyboard.release'])):
        return "Processes mouse position for keyboard control"
    
    # File operations + threading
    if (any(pattern in call_set for pattern in ['os.path.exists', 'os.remove']) and
        any(pattern in call_set for pattern in ['time.sleep', 'threading.Thread'])):
        return "Monitors file system events in background thread"
    
    # INDIVIDUAL PATTERNS (fallback for single-purpose functions)
    
    # PRIORITY 1: Window/GUI Creation (strongest signal - beats everything else)
    if any(pattern in call_set for pattern in ['Toplevel', 'tk.Toplevel', 'geometry', 'attributes', 'overrideredirect']):
        if any(pattern in call_set for pattern in ['withdraw', 'deiconify']):
            return "Controls window visibility and display"
        elif any(pattern in call_set for pattern in ['configure', 'pack', 'grid']):
            return "Configures and arranges GUI components"
        else:
            return "Creates and manages GUI window"
    
    # PRIORITY 2: File System Operations (strong signal)
    if any(pattern in call_set for pattern in ['os.path.exists', 'os.remove', 'os.unlink']):
        if any(pattern in call_set for pattern in ['os.remove', 'os.unlink']):
            return "Manages file system state and operations"
        elif any(pattern in call_set for pattern in ['os.path.exists']):
            return "Checks file or directory existence"
        else:
            return "Manages file system state and operations"
    
    # PRIORITY 3: Threading Patterns (strong signal)
    if any(pattern in call_set for pattern in ['threading.Thread', 'Thread']):
        return "Creates and manages background threads"
    if any(pattern in call_set for pattern in ['time.sleep']):
        return "Pauses execution for specified duration"
    
    # PRIORITY 4: Image/Media Processing (strong signal)
    if any(pattern in call_set for pattern in ['Image.open', 'ImageTk.PhotoImage']):
        return "Loads and processes image data"
    if any(pattern in call_set for pattern in ['Image.open']):
        return "Opens and loads image files"
    
    # PRIORITY 5: Network/HTTP Operations (strong signal)
    if any(pattern in call_set for pattern in ['requests.get', 'requests.post', 'requests.put']):
        return "Performs HTTP network requests"
    if any(pattern in call_set for pattern in ['requests.get']):
        return "Retrieves data from web services"
    
    # PRIORITY 6: System/OS Operations (strong signal)
    if any(pattern in call_set for pattern in ['ctypes.windll', 'GetForegroundWindow', 'SetForegroundWindow']):
        if any(pattern in call_set for pattern in ['GetForegroundWindow']):
            return "Gets the currently active window handle"
        elif any(pattern in call_set for pattern in ['SetForegroundWindow']):
            return "Brings a window to the foreground"
        else:
            return "Interacts with Windows system APIs"
    
    # PRIORITY 7: Mouse Control (distinguish read vs. write)
    if any(pattern in call_set for pattern in ['pyautogui.click', 'pyautogui.moveTo', 'pyautogui.drag']):
        return "Controls mouse programmatically"
    elif any(pattern in call_set for pattern in ['pyautogui.position']):
        return "Reads mouse cursor position"
    
    # PRIORITY 8: Input Simulation (only if no higher priority matches)
    if any(pattern in call_set for pattern in ['keyboard.press', 'keyboard.release']):
        return "Simulates keyboard input events"
    
    # PRIORITY 9: UI Event Handling (lower priority - often incidental)
    if any(pattern in call_set for pattern in ['after', 'bind', 'configure']):
        if any(pattern in call_set for pattern in ['after']):
            return "Schedules delayed UI operations"
        else:
            return "Manages UI event handling and updates"
    
    # PRIORITY 10: Data Processing (lower priority)
    if any(pattern in call_set for pattern in ['json.load', 'json.dump']):
        if any(pattern in call_set for pattern in ['json.load']):
            return "Loads and parses JSON data"
        elif any(pattern in call_set for pattern in ['json.dump']):
            return "Saves data in JSON format"
        else:
            return "Handles JSON data serialization"
    
    # PRIORITY 11: Mathematical/Computational (lowest priority - often incidental)
    if any(pattern in call_set for pattern in ['max', 'min', 'sum', 'len']):
        return "Performs mathematical calculations"
    
    return None


def _analyze_function_body(func_node: ast.FunctionDef) -> str:
    """Infer intent from function body patterns."""
    
    if not func_node or not func_node.body:
        return None
    
    body = func_node.body
    
    # NEW: Check API-specific patterns first (high confidence)
    api_intent = _check_api_patterns(func_node)
    if api_intent:
        return api_intent
    
    # Pattern 1: Single return statement (getter/calculator)
    if len(body) == 1 and isinstance(body[0], ast.Return):
        return "Returns computed value"
    
    # Pattern 2: File operations (legacy - now handled by API patterns)
    has_open = False
    is_writing = False
    for node in ast.walk(func_node):
        if isinstance(node, ast.Call):
            func_name = None
            if hasattr(node.func, 'id'):
                func_name = node.func.id
            
            if func_name == 'open':
                has_open = True
                # Check for 'w' mode
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        if 'w' in arg.value or 'a' in arg.value:
                            is_writing = True
    
    if has_open:
        return "Writes data to file" if is_writing else "Reads data from file"
    
    # Pattern 3: JSON operations (legacy - now handled by API patterns)
    for node in ast.walk(func_node):
        if isinstance(node, ast.Call) and hasattr(node.func, 'attr'):
            if hasattr(node.func, 'value') and hasattr(node.func.value, 'id'):
                if node.func.value.id == 'json':
                    if node.func.attr == 'dump':
                        return "Serializes data to JSON format"
                    elif node.func.attr == 'load':
                        return "Deserializes data from JSON format"
    
    # Pattern 4: Loops (iteration/processing) - FALLBACK with better context
    has_loop = any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(func_node))
    if has_loop:
        # Try to be more specific about what kind of iteration
        calls = _get_all_calls(func_node)
        if any('print' in call for call in calls):
            return "Iterates and displays items"
        elif any('append' in call or 'add' in call for call in calls):
            return "Iterates and builds collection"
        else:
            return "Iterates and processes items"
    
    # Pattern 5: Many function calls (orchestration) - FALLBACK
    call_count = sum(1 for node in ast.walk(func_node) if isinstance(node, ast.Call))
    if call_count > 5:
        return "Orchestrates multiple operations"
    
    # Pattern 6: Assignments (state modification)
    has_assign = any(isinstance(node, ast.Assign) for node in ast.walk(func_node))
    if has_assign and len(body) < 5:
        return "Updates internal state"
    
    return None


def _enhance_with_type_hints(func_name: str, func_node: ast.FunctionDef) -> str:
    """Enhance intent using return type hints."""
    
    if not func_node or not func_node.returns:
        return None
    
    try:
        return_type = ast.unparse(func_node.returns)
    except:
        return None
    
    # Boolean returns
    if return_type == "bool":
        if func_name.startswith("is_") or func_name.startswith("has_"):
            return f"Checks condition"
        return "Returns validation result"
    
    # String returns
    if return_type in ["str", "String"]:
        return "Returns string representation"
    
    # None returns (void functions that perform actions)
    if return_type == "None":
        if "update" in func_name or "set" in func_name or "modify" in func_name:
            return "Modifies state"
        if "save" in func_name or "write" in func_name or "store" in func_name:
            return "Persists data"
        if "clear" in func_name or "reset" in func_name:
            return "Resets state"
        if "add" in func_name or "append" in func_name:
            return "Adds item"
        if "remove" in func_name or "delete" in func_name:
            return "Removes item"
    
    # Collection returns
    if return_type.startswith("Dict") or return_type.startswith("dict"):
        return "Returns dictionary of data"
    
    if return_type.startswith("List") or return_type.startswith("list"):
        return "Returns list of items"
    
    return None


def infer_function_intent(func_name: str, func_node: ast.FunctionDef = None) -> str:
    """
    Generate function intent using priority cascade:
    1. Docstring (best quality)
    2. Function body analysis (good quality)
    3. Type hints (decent quality)
    4. Name-based generation (fallback)
    """
    
    if func_node:
        # PRIORITY 1: Use docstring if present
        try:
            docstring = ast.get_docstring(func_node)
            if docstring:
                # Use first sentence only
                first_sentence = docstring.split('.')[0].split('\n')[0].strip()
                # Clean up common prefixes
                for prefix in ["This function ", "This method ", "This ", "Returns ", "Return "]:
                    if first_sentence.startswith(prefix):
                        first_sentence = first_sentence[len(prefix):]
                        break
                # Capitalize first letter
                if first_sentence:
                    first_sentence = first_sentence[0].upper() + first_sentence[1:]
                    return first_sentence + "."
        except:
            pass
        
        # PRIORITY 2: Analyze function body
        try:
            body_intent = _analyze_function_body(func_node)
            if body_intent:
                return body_intent + "."
        except:
            pass
        
        # PRIORITY 3: Use type hints
        try:
            type_intent = _enhance_with_type_hints(func_name, func_node)
            if type_intent:
                return type_intent + "."
        except:
            pass
    
    # PRIORITY 4: Try enhanced patterns from intent_enhancer_v2
    try:
        from intent_enhancer_v2 import FUNCTION_PATTERNS
        import re
        for pattern, description in FUNCTION_PATTERNS.items():
            if re.match(pattern, func_name):
                return description + "."
    except ImportError:
        pass
    
    # PRIORITY 5: Fall back to name-based generation (current behavior)
    tokens = _split_ident(func_name)
    verb_phrase, _ = _infer_verb(tokens)
    obj_phrase = _noun_phrase_from(tokens, skip_first=True)
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
            func_data = analyzer.functions.get(fname, {})
            func_node = func_data.get('ast_node') if isinstance(func_data, dict) else None
            intent = infer_function_intent(fname, func_node)
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
