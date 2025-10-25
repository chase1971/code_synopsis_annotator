#===============================================================================
# CODE SYNOPSIS: behavioral_analysis.py
# SYNOPSIS_HASH: 1f9b87f9fbfe23973b5584bd0c57481648373074f3231a79340e9fc4d991850d
# Generated: 2025-10-24 17:51:16
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 208
#   Functions: 11
#   Classes: 1
#   Global Variables: 24
#
# Key Dependencies:
#   - ast
#   - collections
#   - datetime
#   - typing
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 17:51:16
# FILE: behavioral_analysis.py
# IMPORTS_EXTERNAL: ast, collections, datetime, typing
# IMPORTS_LOCAL: 
# GLOBALS: assigned, buckets, call_roots, cats, children, critical, fanout, fnames, globs, gr, gw, high_priority, indent, init_seq, lines, lname, readers, sm, state_keys, trans, ts, ui_after, vals, writers
# FUNCTIONS: __init__, analyze_function_dependencies, analyze_high_priority_functions, build_machine_block, categorize_shared_state, dfs, generate_behavioral_summary, group_modules_generic, render_call_hierarchy, render_state_machines, render_ui_after_usage
# RETURNS: analyze_function_dependencies, analyze_high_priority_functions, build_machine_block, categorize_shared_state, generate_behavioral_summary, group_modules_generic, render_call_hierarchy, render_state_machines, render_ui_after_usage
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: BehavioralAnalyzer
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: __init__,build_machine_block,categorize_shared_state,group_modules_generic,analyze_high_priority_functions,analyze_function_dependencies,generate_behavioral_summary
# STATE_VARS: 
# INIT_SEQUENCE: 
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   BehavioralAnalyzer (line 14):
#     - BehavioralAnalyzer.__init__()
#     - BehavioralAnalyzer.render_call_hierarchy()
#     - BehavioralAnalyzer.render_state_machines()
#     - BehavioralAnalyzer.render_ui_after_usage()
#     - BehavioralAnalyzer.build_machine_block()
#     - BehavioralAnalyzer.categorize_shared_state()
#     - BehavioralAnalyzer.group_modules_generic()
#     - BehavioralAnalyzer.analyze_high_priority_functions()
#     - BehavioralAnalyzer.analyze_function_dependencies()
#     - BehavioralAnalyzer.generate_behavioral_summary()
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
# lines:
#   Modified by: render_call_hierarchy, render_state_machines, render_ui_after_usage, build_machine_block, generate_behavioral_summary
#   Read by: render_call_hierarchy, render_state_machines, render_ui_after_usage, build_machine_block, generate_behavioral_summary, dfs
#
# indent:
#   Modified by: render_call_hierarchy, dfs
#   Read by: render_call_hierarchy, dfs
#
# children:
#   Modified by: render_call_hierarchy, dfs
#   Read by: render_call_hierarchy, dfs
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   UI State:
#     - call_roots
#     - ui_after
#   Control State:
#     - state_keys
#   Position State:
#     - high_priority
#     - state_keys
#===============================================================================
#
# ⚠️ HIGH PRIORITY FUNCTIONS (Modify Multiple Globals):
#
# render_call_hierarchy() - line 26  (Returns: Yes)
#   Modifies: children, indent, lines
#   Reads: children, indent, lines
#
# render_state_machines() - line 51  (Returns: Yes)
#   Modifies: lines, readers, trans, vals, writers
#   Reads: lines, readers, trans, vals, writers
#
# build_machine_block() - line 80  (Returns: Yes)
#   Modifies: call_roots, init_seq, lines, state_keys, ts
#   Reads: call_roots, init_seq, lines, state_keys, ts
#
# group_modules_generic() - line 128  (Returns: Yes)
#   Modifies: assigned, buckets, fnames, lname
#   Reads: assigned, buckets, fnames, lname
#
# analyze_high_priority_functions() - line 162  (Returns: Yes)
#   Modifies: gr, gw, high_priority
#   Reads: gr, gw, high_priority
#
# generate_behavioral_summary() - line 179  (Returns: Yes)
#   Modifies: lines, sm, ui_after
#   Reads: lines, sm, ui_after
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - __init__()
#
# - build_machine_block()
#   - items()
#   - now()
#   - sorted()
#   - get()
#   - strftime()
#   - keys()
#   - join()
#
# - categorize_shared_state()
#   - lower()
#   - items()
#   - sorted()
#   - any()
#
# - group_modules_generic()
#   - items()
#   - list()
#   - append()
#   - any()
#   - keys()
#   - lower()
#
# - analyze_high_priority_functions()
#   - items()
#   - append()
#   - sorted()
#   - len()
#
# - analyze_function_dependencies()
#   - items()
#   - sorted()
#   - len()
#
# - generate_behavioral_summary()
#   - enumerate()
#   - append()
#   - len()
#   - extend()
#   - render_call_hierarchy()
#     - append()
#     - sorted()
#     - get()
#     - len()
#     - dfs()
#       - append()
#       - sorted()
#       - get()
#       - len()
#       - dfs()  (cycle)
#   - render_state_machines()
#     - items()
#     - list()
#     - set()
#     - append()
#     - sorted()
#     - get()
#     - len()
#     - join()
#   - render_ui_after_usage()
#     - append()
#     - sorted()
#
#===============================================================================
#
# 📊 DATA FLOW SUMMARY:
#
#   __init__() — pure/local computation; no return value
#   render_call_hierarchy() — reads children, indent, lines; writes children, indent, lines; calls dfs, len, lines.append, self.analyzer.call_graph.get, self.analyzer.functions.get, sorted; returns value
#   dfs() — reads children, indent, lines; writes children, indent; calls dfs, len, lines.append, self.analyzer.call_graph.get, self.analyzer.functions.get, sorted; no return value
#   render_state_machines() — reads lines, readers, trans, vals, writers; writes lines, readers, trans, vals, writers; calls join, len, lines.append, list, self.analyzer.state_comparisons.get, self.analyzer.state_vars.items; returns value
#   render_ui_after_usage() — reads lines; writes lines; calls lines.append, sorted; returns value
#   build_machine_block() — reads call_roots, init_seq, lines, state_keys, ts; writes call_roots, init_seq, lines, state_keys, ts; calls d.get, datetime.now, join, self.analyzer.classes.keys, self.analyzer.functions.items, self.analyzer.functions.keys; returns value
#   categorize_shared_state() — reads cats, globs; writes cats, globs; calls any, cats.items, g.lower, sorted; returns value
#   group_modules_generic() — reads assigned, buckets, fnames, lname; writes assigned, buckets, fnames, lname; calls any, append, buckets.items, f.lower, list, self.analyzer.functions.keys; returns value
#   analyze_high_priority_functions() — reads gr, gw, high_priority; writes gr, gw, high_priority; calls high_priority.append, len, self.analyzer.functions.items, sorted; returns value
#   analyze_function_dependencies() — reads critical, fanout; writes critical, fanout; calls fanout.items, len, self.analyzer.call_graph.items, sorted; returns value
#   generate_behavioral_summary() — reads lines, sm, ui_after; writes lines, sm, ui_after; calls enumerate, len, lines.append, lines.extend, self.render_call_hierarchy, self.render_state_machines; returns value
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
#   render_call_hierarchy() → append, dfs, get, len, sorted
#   render_state_machines() → append, get, items, join, len, list, set, sorted
#   render_ui_after_usage() → append, sorted
#   build_machine_block() → get, items, join, keys, now, sorted, strftime
#   categorize_shared_state() → any, items, lower, sorted
#   group_modules_generic() → any, append, items, keys, list, lower
#   analyze_high_priority_functions() → append, items, len, sorted
#   analyze_function_dependencies() → items, len, sorted
#   generate_behavioral_summary() → append, enumerate, extend, len, render_call_hierarchy, render_state_machines, render_ui_after_usage
#   dfs() → append, dfs, get, len, sorted
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
"""
Behavioral Analysis Module - Advanced code behavior detection.

This module contains specialized analysis for detecting complex behavioral
patterns in Python code, including state machines, call hierarchies,
and UI threading dependencies.
"""

import ast
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict


class BehavioralAnalyzer:
    """
    Specialized analyzer for detecting behavioral patterns in code.
    
    This class focuses on advanced behavioral analysis including state machines,
    call hierarchies, threading patterns, and UI dependencies.
    """
    
    def __init__(self, analyzer):
        """Initialize with reference to main analyzer."""
        self.analyzer = analyzer
    
    def render_call_hierarchy(self, max_depth: int = 3, max_children: int = 8) -> List[str]:
        """Render a depth-limited call hierarchy."""
        lines: List[str] = ["#", "# FUNCTION CALL HIERARCHY (depth-limited):", "#"]

        def dfs(node: str, depth: int, path: Tuple[str, ...]):
            if depth > max_depth:
                return
            indent = '  ' * depth
            lines.append(f"# {indent}- {node}()")
            children = sorted(self.analyzer.call_graph.get(node, []), 
                            key=lambda n: self.analyzer.functions.get(n, {'line': 0})['line'])
            if len(children) > max_children:
                children = children[:max_children]
                lines.append(f"# {indent}  ... +more")
            for ch in children:
                if ch in path:  # cycle guard
                    lines.append(f"# {indent}  - {ch}()  (cycle)")
                    continue
                dfs(ch, depth + 1, path + (ch,))

        for root in self.analyzer.call_roots[:30]:
            dfs(root, 0, (root,))
            lines.append("#")
        return lines

    def render_state_machines(self) -> List[str]:
        """Render detected state machines."""
        if not self.analyzer.state_vars:
            return []
        lines = ["#", "# STATE MACHINES (heuristic):", "#"]
        for var, meta in sorted(self.analyzer.state_vars.items()):
            vals = sorted(list(meta['values'] | self.analyzer.state_comparisons.get(var, set())))
            writers = ', '.join(sorted(list(meta['writers']))[:6])
            readers = ', '.join(sorted(list(meta['readers']))[:6])
            trans = ' → '.join(vals) if len(vals) >= 2 else ', '.join(vals)
            lines.append(f"#   {var}: {trans if trans else '(values unknown)'}")
            if writers:
                lines.append(f"#     Set by: {writers}")
            if readers:
                lines.append(f"#     Checked by: {readers}")
        lines.append("#")
        return lines

    def render_ui_after_usage(self) -> List[str]:
        """Render UI threading dependencies."""
        if not self.analyzer.ui_after_users:
            return []
        lines = ["#", "# UI/THREADING DEPENDENCIES (tk.after usage):", "#"]
        for f in sorted(self.analyzer.ui_after_users, 
                       key=lambda n: self.analyzer.functions[n]['line']):
            lines.append(f"#   - {f}() calls .after(...) → keep on main/UI thread or marshal via queue")
        lines.append("#")
        return lines

    def build_machine_block(self) -> List[str]:
        """Build the machine-readable data block."""
        from datetime import datetime
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        state_keys = ','.join(sorted(self.analyzer.state_vars.keys()))
        call_roots = ','.join(self.analyzer.call_roots[:30])
        init_seq = '; '.join(self.analyzer.init_sequence[:20])
        lines = [
            "# " + "\u2550" * 20,
            "# BEGIN MACHINE-READABLE DATA (for automated processing)",
            "# " + "\u2550" * 20,
            f"# SYNOPSIS_ANNOTATED: YES",
            f"# LAST_ANALYZED: {ts}",
            f"# FILE: {self.analyzer.filename}",
            f"# IMPORTS_EXTERNAL: {', '.join(sorted(x for x in self.analyzer.imports_external if x))}",
            f"# IMPORTS_LOCAL: {', '.join(sorted(x for x in self.analyzer.imports_local if x))}",
            f"# GLOBALS: {', '.join(sorted(self.analyzer.globals_found))}",
            f"# FUNCTIONS: {', '.join(sorted(self.analyzer.functions.keys()))}",
            f"# RETURNS: {', '.join(sorted([f for f, d in self.analyzer.functions.items() if d.get('returns_value')]))}",
            f"# THREAD_TARGETS: {', '.join(sorted(self.analyzer.threads_found))}",
            f"# HOTKEYS: {', '.join([hk for hk, _ in self.analyzer.hotkeys_found])}",
            f"# TK_BINDS: {', '.join([ev for ev, _ in self.analyzer.hotkeys_tkbind])}",
            f"# COMMAND_BINDS: {', '.join([cb for _, cb in self.analyzer.hotkeys_command_bind])}",
            f"# CLASSES: {', '.join(sorted(self.analyzer.classes.keys()))}",
            f"# IO_READS: {', '.join(sorted(self.analyzer.io_reads))}",
            f"# IO_WRITES: {', '.join(sorted(self.analyzer.io_writes))}",
            f"# CALLGRAPH_ROOTS: {call_roots}",
            f"# STATE_VARS: {state_keys}",
            f"# INIT_SEQUENCE: {init_seq}",
            "# END MACHINE-READABLE DATA",
            "# " + "\u2550" * 20,
        ]
        return lines

    def categorize_shared_state(self) -> List[Tuple[str, List[str]]]:
        """Categorize global variables by their likely purpose."""
        globs = sorted(self.analyzer.globals_found)
        if not globs:
            return []
        cats = {
            "UI State": [g for g in globs if any(s in g.lower() for s in ("ui", "window", "dialog", "label", "overlay", "widget", "root", "canvas"))],
            "Control State": [g for g in globs if any(s in g.lower() for s in ("mode", "pause", "run", "state", "enabled", "flag", "active", "status"))],
            "Timing State": [g for g in globs if any(s in g.lower() for s in ("time", "cooldown", "start", "end", "elapsed", "duration", "deadline", "timeout"))],
            "Position State": [g for g in globs if any(s in g.lower() for s in ("pos", "position", "x", "y", "drag", "cursor", "mouse", "offset"))],
            "Config State": [g for g in globs if any(s in g for s in ("CONFIG", "SETTINGS", "OPTION", "THRESHOLD", "DEFAULT", "PATH", "FILE")) or any(s in g.lower() for s in ("config", "setting", "threshold", "path", "file"))],
        }
        return [(k, v) for k, v in cats.items() if v]

    def group_modules_generic(self) -> Dict[str, List[str]]:
        """Group functions into logical modules for refactoring suggestions."""
        fnames = list(self.analyzer.functions.keys())
        buckets = {
            "config_manager.py": [],
            "io_files.py": [],
            "concurrency.py": [],
            "ui_layer.py": [],
            "networking.py": [],
            "cli_interface.py": [],
            "core_logic.py": [],
            "utilities.py": [],
        }
        for f in fnames:
            lname = f.lower()
            assigned = False
            if any(k in lname for k in ("config", "setting", "load_config", "save_config")):
                buckets["config_manager.py"].append(f); assigned = True
            if not assigned and any(k in lname for k in ("read", "write", "save", "load", "open", "export", "import", "serialize", "deserialize")):
                buckets["io_files.py"].append(f); assigned = True
            if not assigned and any(k in lname for k in ("thread", "lock", "mutex", "queue", "worker", "producer", "consumer", "async", "await", "pool")):
                buckets["concurrency.py"].append(f); assigned = True
            if not assigned and any(k in lname for k in ("ui", "gui", "window", "dialog", "overlay", "widget", "label", "button", "canvas")):
                buckets["ui_layer.py"].append(f); assigned = True
            if not assigned and any(k in lname for k in ("http", "https", "socket", "request", "response", "server", "client", "api", "fetch", "post", "get")):
                buckets["networking.py"].append(f); assigned = True
            if not assigned and any(k in lname for k in ("main", "entry", "arg", "argv", "cli", "parse_args")):
                buckets["cli_interface.py"].append(f); assigned = True
            if not assigned and any(k in lname for k in ("util", "helper", "common", "format", "parse", "validate", "calc", "compute")):
                buckets["utilities.py"].append(f); assigned = True
            if not assigned:
                buckets["core_logic.py"].append(f)
        return {k: v for k, v in buckets.items() if v}

    def analyze_high_priority_functions(self) -> List[Tuple[str, Dict, Set[str], Set[str]]]:
        """Identify functions that modify multiple globals or are thread targets."""
        high_priority = []
        for func_name, func_data in self.analyzer.functions.items():
            gw = func_data['writes'] & self.analyzer.globals_found
            gr = func_data['reads'] & self.analyzer.globals_found
            if len(gw) > 2 or (len(gw) > 0 and func_name in self.analyzer.threads_found):
                high_priority.append((func_name, func_data, gr, gw))
        return sorted(high_priority, key=lambda it: it[1]['line'])

    def analyze_function_dependencies(self) -> List[Tuple[str, List[str]]]:
        """Analyze functions with high fan-out (calling many other functions)."""
        fanout = {f: [c for c in cs if c in self.analyzer.functions] 
                 for f, cs in self.analyzer.call_graph.items()}
        critical = [(f, cs) for f, cs in fanout.items() if len(cs) > 3]
        return sorted(critical, key=lambda x: len(x[1]), reverse=True)

    def generate_behavioral_summary(self) -> List[str]:
        """Generate a comprehensive behavioral analysis summary."""
        lines = []
        
        # Function Call Hierarchy
        lines.extend(self.render_call_hierarchy(max_depth=3, max_children=8))
        lines.append("#" + "=" * 79)

        # State Machines
        sm = self.render_state_machines()
        if sm:
            lines.extend(sm)
            lines.append("#" + "=" * 79)

        # UI/Threading dependencies
        ui_after = self.render_ui_after_usage()
        if ui_after:
            lines.extend(ui_after)
            lines.append("#" + "=" * 79)

        # Initialization Sequence
        if self.analyzer.init_sequence:
            lines.extend(["#", "# \U0001F680 INITIALIZATION SEQUENCE:", "#"])  # 🚀
            for i, step in enumerate(self.analyzer.init_sequence[:20], 1):
                lines.append(f"#   {i}. {step}")
            if len(self.analyzer.init_sequence) > 20:
                lines.append(f"#   ... +{len(self.analyzer.init_sequence)-20} more")
            lines.append("#" + "=" * 79)

        return lines
