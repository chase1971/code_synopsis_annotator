#===============================================================================
# CODE SYNOPSIS: core_analyzer.py
# SYNOPSIS_HASH: c248c511bb0949e1e7beb2063b59143dc58c96566086e1e0d5c179934d7fd37a
# Generated: 2025-10-24 22:17:09
# INTENT: Locates or discovers, Extracts functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 511
#   Functions: 29
#   Classes: 1
#   Global Variables: 37
#
# Key Dependencies:
#   - ast
#   - collections
#   - os
#   - typing
#   - warnings
#   (Local modules):
#     * state_machine_detector
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 22:17:09
# FILE: core_analyzer.py
# IMPORTS_EXTERNAL: ast, collections, os, typing, warnings
# IMPORTS_LOCAL: state_machine_detector
# GLOBALS: args, callee, candidate_pkg, candidate_py, cb, defaults_list, detector, enclosing, event, extra_calls, extra_transitions, found_end_marker, fullname, func, func_key, funcname, hk, info, kwarg_str, lines, methods, mode, module, node, parts, path, posonly, pretty, reads, regular_args, result, results, return_type, synopsis_end, transitions, vararg_str, writes
# FUNCTIONS: __init__, _call_to_name, _enclosing_function_name, _extract_open_args, _format_call_name, _is_local_module, _render_arg, _safe_unparse, analyze, analyze_classes, analyze_functions, build_call_graph, detect_state_machines, detect_ui_after_usage, extract_call_graph, extract_function_signatures, extract_hotkey_bindings, extract_state_transitions, find_file_io, find_globals, find_hotkeys_and_ui_binds, find_imports, find_threading, infer_function_behavior, parse_code, process_function, read_file, strip_existing_synopsis, summarize_initialization_sequence
# RETURNS: _call_to_name, _enclosing_function_name, _extract_open_args, _format_call_name, _is_local_module, _render_arg, _safe_unparse, extract_call_graph, extract_hotkey_bindings, extract_state_transitions, infer_function_behavior, read_file, strip_existing_synopsis
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: CodeAnalyzer
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: __init__,read_file,strip_existing_synopsis,parse_code,analyze,find_globals,analyze_classes,analyze_functions,_is_local_module,find_imports,find_threading,find_hotkeys_and_ui_binds,find_file_io,_extract_open_args,build_call_graph,detect_state_machines,detect_ui_after_usage,summarize_initialization_sequence,_call_to_name,_format_call_name,_enclosing_function_name,extract_call_graph,extract_state_transitions,extract_hotkey_bindings,infer_function_behavior,_safe_unparse,_render_arg,extract_function_signatures
# STATE_VARS: mode
# STATE_MACHINES_COUNT: 1
# STATE_TRANSITIONS_COUNT: 1
# INIT_SEQUENCE: 
# INTENT: Locates or discovers, Extracts functionality for this module.
# FUNCTION_INTENTS: __init__=Handles the target entities., _call_to_name=Handles to name., _enclosing_function_name=Handles function name., _extract_open_args=Retrieves open args., _format_call_name=Handles call name., _is_local_module=Handles local module., _render_arg=Produces or displays arg., _safe_unparse=Handles unparse., analyze=Examines and summarizes the target entities., analyze_classes=Examines and summarizes classes., analyze_functions=Examines and summarizes functions., build_call_graph=Constructs or generates call graph., detect_state_machines=Identifies state machines., detect_ui_after_usage=Identifies ui after usage., extract_call_graph=Retrieves call graph., extract_function_signatures=Retrieves function signatures., extract_hotkey_bindings=Retrieves hotkey bindings., extract_state_transitions=Retrieves state transitions., find_file_io=Locates or gathers file io., find_globals=Locates or gathers globals., find_hotkeys_and_ui_binds=Locates or gathers hotkeys and ui binds., find_imports=Locates or gathers imports., find_threading=Locates or gathers threading., infer_function_behavior=Handles function behavior., parse_code=Parses code., process_function=Handles or executes function., read_file=Reads file., strip_existing_synopsis=Handles existing synopsis., summarize_initialization_sequence=Condenses results of initialization sequence.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# CodeAnalyzer.__init__(self, filepath: str, *, include_machine_block: bool = True) -> None
#   Initialize the analyzer with a file path.
#
# CodeAnalyzer._call_to_name(self, func_node) -> str
#   Convert a call function node to a string name.
#
# CodeAnalyzer._enclosing_function_name(self, node: ast.AST) -> Optional[str]
#   Find the name of the function enclosing this node.
#
# CodeAnalyzer._extract_open_args(self, call_node: ast.Call) -> Tuple[Optional[str], str]
#   Extract file path and mode from open() call.
#
# CodeAnalyzer._format_call_name(self, call_node: ast.Call) -> str
#   Format a call node as a string.
#
# CodeAnalyzer._is_local_module(self, module_name: str) -> bool
#   Check if a module is local to the project.
#
# CodeAnalyzer._render_arg(self, arg: ast.arg, default: Optional[ast.AST]) -> str
#   Render a function argument with its annotation and default.
#
# CodeAnalyzer._safe_unparse(self, node: Optional[ast.AST]) -> str
#   Safely convert AST node to string, avoiding heavy operations.
#
# CodeAnalyzer.analyze(self) -> None
#   Run the complete analysis pipeline.
#
# CodeAnalyzer.analyze_classes(self) -> None
#   Analyze class definitions and their methods.
#
# CodeAnalyzer.analyze_functions(self) -> None
#   Analyze function definitions and their behavior.
#
# CodeAnalyzer.build_call_graph(self) -> None
#   Build a call graph of function calls.
#
# CodeAnalyzer.detect_state_machines(self) -> None
#   Detect state machine patterns using StateMachineDetector.
#
# CodeAnalyzer.detect_ui_after_usage(self) -> None
#   Detect usage of UI after callbacks.
#
# CodeAnalyzer.extract_call_graph(self, tree: ast.AST) -> Dict[str, Set[str]]
#   Extract call graph from AST.
#
# CodeAnalyzer.extract_function_signatures(self) -> None
#   Extract function signatures with type hints and defaults.
#
# CodeAnalyzer.extract_hotkey_bindings(self) -> List[str]
#   Extract hotkey bindings in a pretty format.
#
# CodeAnalyzer.extract_state_transitions(self, tree: ast.AST) -> Dict[str, Set[str]]
#   Extract state transitions from AST.
#
# CodeAnalyzer.find_file_io(self) -> None
#   Find file I/O operations.
#
# CodeAnalyzer.find_globals(self) -> None
#   Find all global variable assignments.
#
# CodeAnalyzer.find_hotkeys_and_ui_binds(self) -> None
#   Find hotkey and UI binding patterns.
#
# CodeAnalyzer.find_imports(self) -> None
#   Find and categorize imports.
#
# CodeAnalyzer.find_threading(self) -> None
#   Find threading usage and interactions.
#
# CodeAnalyzer.infer_function_behavior(self, func_name: str) -> Dict[str, object]
#   Infer behavioral intent of a function.
#
# CodeAnalyzer.parse_code(self) -> None
#   Parse the Python code into an AST.
#
# CodeAnalyzer.read_file(self) -> str
#   Read the source file.
#
# CodeAnalyzer.strip_existing_synopsis(self, code: str) -> str
#   Remove existing synopsis headers from code.
#
# CodeAnalyzer.summarize_initialization_sequence(self) -> None
#   Summarize module initialization sequence.
#
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   CodeAnalyzer (line 18):
#     - CodeAnalyzer.__init__()
#     - CodeAnalyzer.read_file()
#     - CodeAnalyzer.strip_existing_synopsis()
#     - CodeAnalyzer.parse_code()
#     - CodeAnalyzer.analyze()
#     - CodeAnalyzer.find_globals()
#     - CodeAnalyzer.analyze_classes()
#     - CodeAnalyzer.analyze_functions()
#     - CodeAnalyzer._is_local_module()
#     - CodeAnalyzer.find_imports()
#     - CodeAnalyzer.find_threading()
#     - CodeAnalyzer.find_hotkeys_and_ui_binds()
#     - CodeAnalyzer.find_file_io()
#     - CodeAnalyzer._extract_open_args()
#     - CodeAnalyzer.build_call_graph()
#     - CodeAnalyzer.detect_state_machines()
#     - CodeAnalyzer.detect_ui_after_usage()
#     - CodeAnalyzer.summarize_initialization_sequence()
#     - CodeAnalyzer._call_to_name()
#     - CodeAnalyzer._format_call_name()
#     - CodeAnalyzer._enclosing_function_name()
#     - CodeAnalyzer.extract_call_graph()
#     - CodeAnalyzer.extract_state_transitions()
#     - CodeAnalyzer.extract_hotkey_bindings()
#     - CodeAnalyzer.infer_function_behavior()
#     - CodeAnalyzer._safe_unparse()
#     - CodeAnalyzer._render_arg()
#     - CodeAnalyzer.extract_function_signatures()
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
# node:
#   Modified by: find_globals, analyze_classes, analyze_functions, find_imports, find_threading, find_hotkeys_and_ui_binds +6 more
#   Read by: find_globals, analyze_classes, analyze_functions, find_imports, find_threading, find_hotkeys_and_ui_binds +8 more
#
# parts:
#   Modified by: _call_to_name, extract_function_signatures, process_function
#   Read by: _call_to_name, extract_function_signatures, process_function
#
# func_key:
#   Modified by: extract_function_signatures, process_function
#   Read by: extract_function_signatures, process_function
#
# defaults_list:
#   Modified by: extract_function_signatures, process_function
#   Read by: extract_function_signatures, process_function
#
# vararg_str:
#   Modified by: extract_function_signatures, process_function
#   Read by: extract_function_signatures, process_function
#
# path:
#   Modified by: find_file_io, _extract_open_args
#   Read by: find_file_io, _extract_open_args
#
# hk:
#   Modified by: find_hotkeys_and_ui_binds, extract_hotkey_bindings
#   Read by: find_hotkeys_and_ui_binds, extract_hotkey_bindings
#
# regular_args:
#   Modified by: extract_function_signatures, process_function
#   Read by: extract_function_signatures, process_function
#
# callee:
#   Modified by: analyze_functions, build_call_graph
#   Read by: analyze_functions, build_call_graph
#
# cb:
#   Modified by: find_hotkeys_and_ui_binds, extract_hotkey_bindings
#   Read by: find_hotkeys_and_ui_binds, extract_hotkey_bindings
#
# result:
#   Modified by: _safe_unparse, _render_arg
#   Read by: _safe_unparse, _render_arg
#
# mode:
#   Modified by: find_file_io, _extract_open_args
#   Read by: find_file_io, _extract_open_args
#
# args:
#   Modified by: extract_function_signatures, process_function
#   Read by: extract_function_signatures, process_function
#
# funcname:
#   Modified by: find_hotkeys_and_ui_binds, detect_ui_after_usage
#   Read by: find_hotkeys_and_ui_binds, detect_ui_after_usage
#
# kwarg_str:
#   Modified by: extract_function_signatures, process_function
#   Read by: extract_function_signatures, process_function
#
# return_type:
#   Modified by: extract_function_signatures, process_function
#   Read by: extract_function_signatures, process_function
#
# func:
#   Modified by: find_threading, _enclosing_function_name
#   Read by: find_threading, _enclosing_function_name
#
# posonly:
#   Modified by: extract_function_signatures, process_function
#   Read by: extract_function_signatures, process_function
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   Control State:
#     - mode
#   Timing State:
#     - found_end_marker
#     - synopsis_end
#   Position State:
#     - candidate_py
#     - extra_calls
#     - extra_transitions
#     - func_key
#     - posonly
#     - pretty
#     - return_type
#     - synopsis_end
#   Config State:
#     - path
#===============================================================================
#
# ⚠️ HIGH PRIORITY FUNCTIONS (Modify Multiple Globals):
#
# strip_existing_synopsis() - line 86  (Returns: Yes)
#   Modifies: found_end_marker, lines, synopsis_end
#   Reads: found_end_marker, lines, synopsis_end
#
# analyze_functions() - line 160  (Returns: No)
#   Modifies: callee, info, node
#   Reads: callee, info, node
#
# find_threading() - line 209  (Returns: No)
#   Modifies: func, node, reads, writes
#   Reads: func, node, reads, writes
#
# find_hotkeys_and_ui_binds() - line 225  (Returns: No)
#   Modifies: cb, event, funcname, hk, node
#   Reads: cb, event, funcname, hk, node
#
# find_file_io() - line 257  (Returns: No)
#   Modifies: fullname, mode, node, path
#   Reads: fullname, mode, node, path
#
# detect_ui_after_usage() - line 332  (Returns: No)
#   Modifies: enclosing, funcname, node
#   Reads: enclosing, funcname, node
#
# extract_hotkey_bindings() - line 390  (Returns: Yes)
#   Modifies: cb, hk, pretty
#   Reads: cb, hk, pretty
#
# extract_function_signatures() - line 446  (Returns: No)
#   Modifies: args, defaults_list, func_key, kwarg_str, node, parts, posonly, regular_args
#   Reads: args, defaults_list, func_key, kwarg_str, node, parts, posonly, regular_args
#
# process_function() - line 454  (Returns: No)
#   Modifies: args, defaults_list, func_key, kwarg_str, parts, posonly, regular_args, return_type
#   Reads: args, defaults_list, func_key, kwarg_str, parts, posonly, regular_args, return_type
#
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - __init__()
#
# - read_file()
#
# - strip_existing_synopsis()
#
# - parse_code()
#
# - analyze()
#
# - find_globals()
#
# - analyze_classes()
#
# - analyze_functions()
#
# - _is_local_module()
#
# - find_imports()
#
# - find_threading()
#
# - find_hotkeys_and_ui_binds()
#
# - find_file_io()
#
# - _extract_open_args()
#
# - build_call_graph()
#
# - detect_state_machines()
#
# - detect_ui_after_usage()
#
# - summarize_initialization_sequence()
#
# - _call_to_name()
#
# - _format_call_name()
#
# - _enclosing_function_name()
#
# - extract_call_graph()
#
# - extract_state_transitions()
#
# - extract_hotkey_bindings()
#
# - infer_function_behavior()
#
# - _safe_unparse()
#
# - _render_arg()
#
# - extract_function_signatures()
#
#===============================================================================
#
# 🔄 STATE MACHINES DETECTED:
#
#   📍 mode (Mode Variable):
#      States: r
#      Modified by: _extract_open_args
#
#   🔀 Key Transitions:
#      _extract_open_args(): *→r
#
#===============================================================================
#
# 🔄 STATE MACHINE DIAGRAMS:
#
# ```mermaid
# stateDiagram-v2
#     [*] --> r
#     state "r" as r
# ```
#
#
# 📊 DATA FLOW SUMMARY:
#
#   __init__() — calls defaultdict, os.path.abspath, os.path.basename, os.path.dirname, self.parse_code, self.read_file; no return value
#   read_file() — calls Exception, f.read, open; returns value
#   strip_existing_synopsis() — reads found_end_marker, lines, synopsis_end; writes found_end_marker, lines, synopsis_end; calls code.split, enumerate, join, len, line.startswith, startswith; returns value
#   parse_code() — calls Exception, ast.parse; no return value
#   analyze() — reads extra_calls, extra_transitions; writes extra_calls, extra_transitions; calls extra_calls.items, extra_transitions.items, self.analyze_classes, self.analyze_functions, self.build_call_graph, self.detect_state_machines; no return value
#   find_globals() — reads node; writes node; calls ast.walk, isinstance, self.globals_found.add; no return value
#   analyze_classes() — reads methods, node; writes methods, node; calls isinstance; no return value
#   analyze_functions() — reads callee, info, node; writes callee, info, node; calls add, ast.walk, isinstance, self._call_to_name, set; no return value
#   _is_local_module() — reads candidate_pkg, candidate_py; writes candidate_pkg, candidate_py; calls module_name.replace, os.path.exists, os.path.join; returns value
#   find_imports() — reads module, node; writes module, node; calls add, ast.walk, getattr, isinstance, self._is_local_module, self.imports.append; no return value
#   find_threading() — reads func, node, reads, writes; writes func, node, reads, writes; calls ast.walk, isinstance, self.threads_found.append, sorted; no return value
#   find_hotkeys_and_ui_binds() — reads cb, event, funcname, hk, node; writes cb, event, funcname, hk, node; calls ast.walk, funcname.endswith, isinstance, len, self._call_to_name, self.hotkeys_command_bind.append; no return value
#   find_file_io() — reads fullname, mode, node, path; writes fullname, mode, node, path; calls add, any, ast.walk, fullname.endswith, isinstance, self._call_to_name; no return value
#   _extract_open_args() — reads mode, path; writes mode, path; calls isinstance, len, str; returns value
#   build_call_graph() — reads callee; writes callee; calls add, self.functions.items; no return value
#   detect_state_machines() — reads detector, results; writes detector, results; calls StateMachineDetector, detector.detect, items, set, update, warnings.warn; no return value
#   detect_ui_after_usage() — reads enclosing, funcname, node; writes enclosing, funcname, node; calls ast.walk, funcname.endswith, isinstance, self._call_to_name, self._enclosing_function_name, self.ui_after_users.add; no return value
#   summarize_initialization_sequence() — reads node; writes node; calls isinstance, self._call_to_name, self.init_sequence.append; no return value
#   _call_to_name() — reads node, parts; writes node, parts; calls isinstance, join, parts.append, reversed; returns value
#   _format_call_name() — calls self._call_to_name; returns value
#   _enclosing_function_name() — reads func, node; writes func; calls any, ast.walk, isinstance; returns value
#   extract_call_graph() — calls self.call_graph.items, v.copy; returns value
#   extract_state_transitions() — reads node, transitions; writes node, transitions; calls add, ast.walk, defaultdict, isinstance, str, target.id.endswith; returns value
#   extract_hotkey_bindings() — reads cb, hk, pretty; writes cb, hk, pretty; calls pretty.append; returns value
#   infer_function_behavior() — pure/local computation; returns value
#   _safe_unparse() — reads node, result; writes result; calls ast.unparse, isinstance, len; returns value
#   _render_arg() — reads result; writes result; calls self._safe_unparse; returns value
#   extract_function_signatures() — reads args, defaults_list, func_key, kwarg_str, node, parts; writes args, defaults_list, func_key, kwarg_str, node, parts; calls ast.get_docstring, getattr, isinstance, len, list, parts.append; no return value
#   process_function() — reads args, defaults_list, func_key, kwarg_str, parts, posonly; writes args, defaults_list, func_key, kwarg_str, parts, posonly; calls ast.get_docstring, getattr, len, list, parts.append, self._render_arg; no return value
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
"""
Core Code Analyzer - Main analysis engine for Python code.

This module contains the primary CodeAnalyzer class that orchestrates
the analysis of Python source code and coordinates with other modules.
"""

import ast
import os
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict
try:
    from .state_machine_detector import StateMachineDetector  # NEW
except ImportError:
    from state_machine_detector import StateMachineDetector  # Fallback for direct execution


class CodeAnalyzer:
    """
    Main code analyzer that coordinates analysis of Python source files.
    
    This class serves as the central orchestrator, managing the analysis
    process and coordinating with specialized analysis modules.
    """
    
    def __init__(self, filepath: str, state=None, *, include_machine_block: bool = True):
        """Initialize the analyzer with a file path and optional shared state."""
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.dirpath = os.path.dirname(os.path.abspath(filepath))
        self.include_machine_block = include_machine_block
        
        # Use shared state if provided, otherwise create local state
        if state is not None:
            self.state = state
        else:
            from .analyzer_state import new_state
            self.state = new_state()

        # Core analysis stores
        self.globals_found: Set[str] = set()
        self.functions: Dict[str, Dict[str, object]] = {}
        self.classes: Dict[str, Dict[str, object]] = {}

        # Imports
        self.imports: List[str] = []
        self.imports_external: Set[str] = set()
        self.imports_local: Set[str] = set()

        # Concurrency / hotkeys
        self.threads_found: List[str] = []
        self.thread_interactions: Dict[str, Dict[str, List[str]]] = {}
        self.hotkeys_found: List[Tuple[str, str]] = []  # (binding, callback)
        self.hotkeys_tkbind: List[Tuple[str, str]] = []  # (event, callback)
        self.hotkeys_command_bind: List[Tuple[str, str]] = []  # (widget?, callback)

        # File I/O
        self.io_reads: Set[str] = set()
        self.io_writes: Set[str] = set()

        # Behavioral layers
        self.call_graph: Dict[str, Set[str]] = defaultdict(set)  # caller -> {callees}
        self.called_by: Dict[str, Set[str]] = defaultdict(set)   # callee -> {callers}
        self.call_roots: List[str] = []                          # functions not called by others
        self.state_vars: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: {"values": set(), "writers": set(), "readers": set()})
        self.state_comparisons: Dict[str, Set[str]] = defaultdict(set)  # var -> {value}
        self.init_sequence: List[str] = []
        self.ui_after_users: Set[str] = set()  # functions that call tk.after
        self.hotkeys_pretty: List[str] = []

        # NEW: Function signatures
        self.function_signatures: Dict[str, Dict[str, any]] = {}
        
        # ADD THESE LINES:
        # State machine detection results
        self.state_machine_results: Optional[Dict[str, any]] = None
        self.state_machine_detector: Optional[StateMachineDetector] = None

        # Parse the code
        self.original_code = self.read_file()
        self.code = self.strip_existing_synopsis(self.original_code)
        self.tree: ast.AST = None
        self.parse_code()

    def read_file(self) -> str:
        """Read the source file."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise Exception(f"Could not read file: {e}")

    def strip_existing_synopsis(self, code: str) -> str:
        """Remove existing synopsis headers from code."""
        lines = code.split('\n')
        if lines and lines[0].startswith('#' + '=' * 79):
            synopsis_end = 0
            found_end_marker = False
            for i, line in enumerate(lines):
                if line.startswith('#' + '=' * 79):
                    found_end_marker = True
                    synopsis_end = i + 1
                elif found_end_marker and line and not line.startswith('#'):
                    while synopsis_end < len(lines) and not lines[synopsis_end].strip():
                        synopsis_end += 1
                    break
            if synopsis_end > 0:
                return '\n'.join(lines[synopsis_end:])
        return code

    def parse_code(self):
        """Parse the Python code into an AST."""
        try:
            self.tree = ast.parse(self.code, filename=self.filename)
        except SyntaxError as e:
            raise Exception(f"Syntax error in code: {e}")

    def analyze(self):
        """Run the complete analysis pipeline."""
        # Basic analysis
        self.find_globals()
        self.analyze_classes()
        self.analyze_functions()
        self.find_imports()
        self.find_threading()
        self.find_hotkeys_and_ui_binds()
        self.find_file_io()
        self.build_call_graph()
        
        # Behavioral analysis
        self.detect_state_machines()
        self.detect_ui_after_usage()
        self.summarize_initialization_sequence()

        # Additional behavioral analysis
        extra_calls = self.extract_call_graph(self.tree)
        for caller, callees in extra_calls.items():
            self.call_graph[caller].update(callees)

        extra_transitions = self.extract_state_transitions(self.tree)
        for var, vals in extra_transitions.items():
            self.state_vars[var]["values"].update(vals)

        self.hotkeys_pretty = self.extract_hotkey_bindings()

        # NEW: Extract function signatures (added feature)
        self.extract_function_signatures()

    def find_globals(self):
        """Find all global variable assignments."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        self.globals_found.add(target.id)

    def analyze_classes(self):
        """Analyze class definitions and their methods."""
        for node in self.tree.body:
            if isinstance(node, ast.ClassDef):
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                self.classes[node.name] = {
                    'line': node.lineno,
                    'methods': methods
                }

    def analyze_functions(self):
        """Analyze function definitions and their behavior."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                info = {
                    'line': node.lineno,
                    'reads': set(),
                    'writes': set(),
                    'calls': set(),
                    'returns_value': False
                }
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Name):
                        if isinstance(sub.ctx, ast.Store):
                            info['writes'].add(sub.id)
                        elif isinstance(sub.ctx, ast.Load):
                            info['reads'].add(sub.id)
                    elif isinstance(sub, ast.Call):
                        callee = self._call_to_name(sub.func)
                        if callee:
                            info['calls'].add(callee)
                    elif isinstance(sub, ast.Return) and sub.value is not None:
                        info['returns_value'] = True
                self.functions[node.name] = info

    def _is_local_module(self, module_name: str) -> bool:
        """Check if a module is local to the project."""
        if not module_name:
            return False
        candidate_py = os.path.join(self.dirpath, module_name.replace('.', os.sep) + '.py')
        candidate_pkg = os.path.join(self.dirpath, module_name.replace('.', os.sep), '__init__.py')
        return os.path.exists(candidate_py) or os.path.exists(candidate_pkg)

    def find_imports(self):
        """Find and categorize imports."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.imports.append(alias.name)
                    (self.imports_local if self._is_local_module(alias.name) else self.imports_external).add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                if getattr(node, 'level', 0) and node.level > 0:
                    self.imports_local.add(module or ".")
                else:
                    (self.imports_local if self._is_local_module(module) else self.imports_external).add(module or "*")
                for alias in node.names:
                    self.imports.append(f"{module}.{alias.name}" if module else alias.name)

    def find_threading(self):
        """Find threading usage and interactions."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name) and node.func.value.id == 'threading' and node.func.attr == 'Thread':
                    for kw in node.keywords:
                        if kw.arg == 'target' and isinstance(kw.value, ast.Name):
                            func = kw.value.id
                            self.threads_found.append(func)
                            if func in self.functions:
                                reads = self.functions[func]['reads'] & self.globals_found
                                writes = self.functions[func]['writes'] & self.globals_found
                                self.thread_interactions[func] = {
                                    'reads': sorted(reads), 'writes': sorted(writes)
                                }

    def find_hotkeys_and_ui_binds(self):
        """Find hotkey and UI binding patterns."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call):
                funcname = self._call_to_name(node.func)
                # Keyboard library
                if funcname == 'keyboard.add_hotkey':
                    if node.args and isinstance(node.args[0], ast.Constant):
                        hk = str(node.args[0].value)
                        cb = None
                        if len(node.args) > 1 and isinstance(node.args[1], ast.Name):
                            cb = node.args[1].id
                        for kw in node.keywords:
                            if kw.arg == 'callback' and isinstance(kw.value, ast.Name):
                                cb = kw.value.id
                        if hk and cb:
                            self.hotkeys_found.append((hk, cb))
                # Tkinter .bind("<Key>", callback)
                if funcname.endswith('.bind'):
                    if node.args and isinstance(node.args[0], ast.Constant):
                        event = str(node.args[0].value)
                        cb = None
                        if len(node.args) > 1 and isinstance(node.args[1], ast.Name):
                            cb = node.args[1].id
                        if event and cb:
                            self.hotkeys_tkbind.append((event, cb))
                # widget.config(command=callback)
                if funcname.endswith('.config'):
                    for kw in node.keywords:
                        if kw.arg == 'command' and isinstance(kw.value, ast.Name):
                            self.hotkeys_command_bind.append(('widget.command', kw.value.id))

    def find_file_io(self):
        """Find file I/O operations."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'open':
                    path, mode = self._extract_open_args(node)
                    if path:
                        (self.io_writes if any(m in mode for m in ('w', 'a', 'x', '+')) else self.io_reads).add(path)
                if isinstance(node.func, ast.Attribute):
                    fullname = self._call_to_name(node.func)
                    if fullname.endswith('json.load'):
                        self.io_reads.add('json.load(...)')
                    elif fullname.endswith('json.dump'):
                        self.io_writes.add('json.dump(...)')

    def _extract_open_args(self, call_node: ast.Call) -> Tuple[Optional[str], str]:
        """Extract file path and mode from open() call."""
        path = None
        mode = "r"
        if call_node.args:
            if isinstance(call_node.args[0], ast.Constant):
                path = str(call_node.args[0].value)
            if len(call_node.args) > 1 and isinstance(call_node.args[1], ast.Constant):
                mode = str(call_node.args[1].value)
        for kw in call_node.keywords:
            if kw.arg == "file" and isinstance(kw.value, ast.Constant):
                path = str(kw.value.value)
            if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                mode = str(kw.value.value)
        return path, mode

    def build_call_graph(self):
        """Build a call graph of function calls."""
        for func_name, func_info in self.functions.items():
            for callee in func_info['calls']:
                self.called_by[callee].add(func_name)
        self.call_roots = [f for f in self.functions if f not in self.called_by]

    def detect_state_machines(self):
        """Detect state machine patterns using StateMachineDetector."""
        try:
            detector = StateMachineDetector(self)
            results = detector.detect()
            
            # Store results in analyzer
            self.state_machine_results = results
            self.state_machine_detector = detector
            
            # Update existing state_vars with enhanced detection
            for var_name, var_data in results['state_variables'].items():
                if var_name not in self.state_vars:
                    self.state_vars[var_name] = {
                        "values": var_data.values,
                        "writers": var_data.writers,
                        "readers": var_data.readers
                    }
                else:
                    # Merge with existing detection
                    self.state_vars[var_name]["values"].update(var_data.values)
                    self.state_vars[var_name]["writers"].update(var_data.writers)
                    self.state_vars[var_name]["readers"].update(var_data.readers)
            
            # Also update state_comparisons
            for var_name, var_data in results['state_variables'].items():
                if var_data.comparisons:
                    if var_name not in self.state_comparisons:
                        self.state_comparisons[var_name] = set()
                    self.state_comparisons[var_name].update(var_data.comparisons)
        except Exception as e:
            # Graceful fallback - don't break if state machine detection fails
            import warnings
            warnings.warn(f"State machine detection failed: {e}")
            self.state_machine_results = None
            self.state_machine_detector = None

    def detect_ui_after_usage(self):
        """Detect usage of UI after callbacks."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call):
                funcname = self._call_to_name(node.func)
                if funcname.endswith('.after'):
                    enclosing = self._enclosing_function_name(node)
                    if enclosing:
                        self.ui_after_users.add(enclosing)

    def summarize_initialization_sequence(self):
        """Summarize module initialization sequence."""
        for node in self.tree.body:
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                self.init_sequence.append(self._call_to_name(node.value.func))

    def _call_to_name(self, func_node) -> str:
        """Convert a call function node to a string name."""
        if isinstance(func_node, ast.Name):
            return func_node.id
        elif isinstance(func_node, ast.Attribute):
            parts = []
            node = func_node
            while isinstance(node, ast.Attribute):
                parts.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name):
                parts.append(node.id)
            return '.'.join(reversed(parts))
        return ""

    def _format_call_name(self, call_node: ast.Call) -> str:
        """Format a call node as a string."""
        return self._call_to_name(call_node.func)

    def _enclosing_function_name(self, node: ast.AST) -> Optional[str]:
        """Find the name of the function enclosing this node."""
        for func in ast.walk(self.tree):
            if isinstance(func, ast.FunctionDef):
                if any(n is node for n in ast.walk(func)):
                    return func.name
        return None

    def extract_call_graph(self, tree: ast.AST) -> Dict[str, Set[str]]:
        """Extract call graph from AST."""
        return {k: v.copy() for k, v in self.call_graph.items()}

    def extract_state_transitions(self, tree: ast.AST) -> Dict[str, Set[str]]:
        """Extract state transitions from AST."""
        transitions = defaultdict(set)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                        if target.id.endswith('_state') or target.id.endswith('State'):
                            transitions[target.id].add(str(node.value.value))
        return transitions

    def extract_hotkey_bindings(self) -> List[str]:
        """Extract hotkey bindings in a pretty format."""
        pretty = []
        for hk, cb in self.hotkeys_found:
            pretty.append(f"keyboard: {hk} → {cb}()")
        for ev, cb in self.hotkeys_tkbind:
            pretty.append(f"tk.bind: {ev} → {cb}()")
        for kind, cb in self.hotkeys_command_bind:
            pretty.append(f"{kind}: → {cb}()")
        return pretty

    def infer_function_behavior(self, func_name: str) -> Dict[str, object]:
        """Infer behavioral intent of a function."""
        if func_name not in self.functions:
            return {}
        return {}

    # =========================================================================
    # NEW: FUNCTION SIGNATURE EXTRACTION
    # =========================================================================
    
    def _safe_unparse(self, node: Optional[ast.AST]) -> str:
        """Safely convert AST node to string, avoiding heavy operations."""
        if node is None:
            return "None"
        
        # Simplify complex expressions
        if isinstance(node, (ast.Lambda, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            return "<complex>"
        if isinstance(node, ast.List):
            return "<list>"
        if isinstance(node, ast.Dict):
            return "<dict>"
        if isinstance(node, ast.Set):
            return "<set>"
        if isinstance(node, ast.Tuple):
            return "<tuple>"
        
        try:
            result = ast.unparse(node)
            # Truncate if too long
            if len(result) > 80:
                return result[:77] + "..."
            return result
        except:
            return "<?>"
    
    def _render_arg(self, arg: ast.arg, default: Optional[ast.AST]) -> str:
        """Render a function argument with its annotation and default."""
        result = arg.arg
        if arg.annotation:
            result += f": {self._safe_unparse(arg.annotation)}"
        if default is not None:
            result += f" = {self._safe_unparse(default)}"
        return result
    
    def extract_function_signatures(self):
        """
        Extract function signatures with type hints and defaults.
        Stores them in self.function_signatures.
        """
        if not isinstance(self.tree, ast.Module):
            return
        
        def process_function(fn: ast.FunctionDef, class_name: Optional[str] = None):
            """Process a single function definition."""
            args = fn.args
            parts = []
            
            # Position-only arguments (Python 3.8+)
            posonly = getattr(args, "posonlyargs", [])
            if posonly:
                for arg in posonly:
                    parts.append(self._render_arg(arg, None))
                parts.append("/")
            
            # Regular arguments with defaults
            regular_args = list(args.args)
            defaults_list = [None] * (len(regular_args) - len(args.defaults)) + list(args.defaults)
            for arg, default in zip(regular_args, defaults_list):
                parts.append(self._render_arg(arg, default))
            
            # *args
            if args.vararg:
                vararg_str = f"*{args.vararg.arg}"
                if args.vararg.annotation:
                    vararg_str += f": {self._safe_unparse(args.vararg.annotation)}"
                parts.append(vararg_str)
            elif args.kwonlyargs:
                parts.append("*")
            
            # Keyword-only arguments
            for kw_arg, default in zip(args.kwonlyargs, args.kw_defaults):
                parts.append(self._render_arg(kw_arg, default))
            
            # **kwargs
            if args.kwarg:
                kwarg_str = f"**{args.kwarg.arg}"
                if args.kwarg.annotation:
                    kwarg_str += f": {self._safe_unparse(args.kwarg.annotation)}"
                parts.append(kwarg_str)
            
            # Return type
            return_type = self._safe_unparse(fn.returns) if fn.returns else "None"
            
            # Store the signature
            func_key = f"{class_name}.{fn.name}" if class_name else fn.name
            self.function_signatures[func_key] = {
                "args": parts,
                "returns": return_type,
                "docstring": ast.get_docstring(fn) or ""
            }
        
        # Process top-level functions
        for node in self.tree.body:
            if isinstance(node, ast.FunctionDef):
                process_function(node)
            elif isinstance(node, ast.ClassDef):
                # Process methods
                for sub in node.body:
                    if isinstance(sub, ast.FunctionDef):
                        process_function(sub, node.name)