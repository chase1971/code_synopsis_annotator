#===============================================================================
# CODE SYNOPSIS: core_analyzer.py
# SYNOPSIS_HASH: 7c819df3414d2638773a80dabc6d5208fc2c9d6b2a4e1e429b8d18f19c631365
# Generated: 2025-10-25 13:00:59
# INTENT: Locates or discovers, Extracts functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 769
#   Functions: 50
#   Classes: 3
#   Global Variables: 0
#
# Key Dependencies:
#   - ast
#   - collections
#   - os
#   - typing
#   - warnings
#   (Local modules):
#     * analyzer_state
#     * state_machine_detector
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-25 13:00:59
# FILE: core_analyzer.py
# IMPORTS_EXTERNAL: ast, collections, os, typing, warnings
# IMPORTS_LOCAL: analyzer_state, state_machine_detector
# GLOBALS: 
# FUNCTIONS: __init__, _analyze_function_accesses, _call_to_name, _collect_params, _enclosing_function_name, _enter_func, _exit_func, _extract_open_args, _format_call_name, _is_local_module, _is_true_global, _names_in_target, _render_arg, _safe_unparse, analyze, analyze_classes, analyze_functions, build_call_graph, build_symbol_indexes, detect_state_machines, detect_ui_after_usage, extract_call_graph, extract_function_signatures, extract_hotkey_bindings, extract_state_transitions, find_file_io, find_globals, find_hotkeys_and_ui_binds, find_imports, find_threading, infer_function_behavior, map_global_accesses, parse_code, process_function, read_file, strip_existing_synopsis, summarize_initialization_sequence, visit_AnnAssign, visit_Assign, visit_AsyncFunctionDef, visit_AugAssign, visit_ExceptHandler, visit_For, visit_FunctionDef, visit_Global, visit_Import, visit_ImportFrom, visit_Name, visit_Nonlocal, visit_With
# RETURNS: _call_to_name, _collect_params, _enclosing_function_name, _extract_open_args, _format_call_name, _is_local_module, _is_true_global, _names_in_target, _render_arg, _safe_unparse, extract_call_graph, extract_hotkey_bindings, extract_state_transitions, infer_function_behavior, read_file, strip_existing_synopsis
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: CodeAnalyzer, GlobalAccessVisitor, ScopeIndexer
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: __init__,visit_Assign,visit_AnnAssign,visit_AugAssign,visit_Import,visit_ImportFrom,visit_FunctionDef,visit_AsyncFunctionDef,_enter_func,_exit_func,_collect_params,visit_Name,visit_For,visit_With,visit_ExceptHandler,visit_Global,visit_Nonlocal,_is_true_global,read_file,strip_existing_synopsis,parse_code,analyze,build_symbol_indexes,_analyze_function_accesses,find_globals,analyze_classes,analyze_functions,map_global_accesses,_is_local_module,find_imports
# STATE_VARS: mode
# STATE_MACHINES_COUNT: 1
# STATE_TRANSITIONS_COUNT: 1
# INIT_SEQUENCE: 
# INTENT: Locates or discovers, Extracts functionality for this module.
# FUNCTION_INTENTS: __init__=Initialize the analyzer with a file path and optional shared state., _analyze_function_accesses=Populate reads/writes for a function using scope indexes., _call_to_name=Convert a call function node to a string name., _collect_params=Iterates and processes items., _enclosing_function_name=Find the name of the function enclosing this node., _enter_func=Handles func., _exit_func=Handles func., _extract_open_args=Extract file path and mode from open() call., _format_call_name=Format a call node as a string., _is_local_module=Check if a module is local to the project., _is_true_global=Returns validation result., _names_in_target=Extract all simple names bound by an assignment/target expression., _render_arg=Render a function argument with its annotation and default., _safe_unparse=Safely convert AST node to string; avoiding heavy operations., analyze=Run the complete analysis pipeline., analyze_classes=Analyze class definitions and their methods., analyze_functions=Analyze function definitions and their behavior., build_call_graph=Build a call graph of function calls., build_symbol_indexes=Build scope indexes for this file's AST., detect_state_machines=Detect state machine patterns using StateMachineDetector., detect_ui_after_usage=Detect usage of UI after callbacks., extract_call_graph=Extract call graph from AST., extract_function_signatures=Extract function signatures with type hints and defaults., extract_hotkey_bindings=Extract hotkey bindings in a pretty format., extract_state_transitions=Extract state transitions from AST., find_file_io=Find file I/O operations., find_globals=Find all global variable assignments and references using proper scope analysis., find_hotkeys_and_ui_binds=Find hotkey and UI binding patterns., find_imports=Find and categorize imports., find_threading=Find threading usage and interactions., infer_function_behavior=Infer behavioral intent of a function., map_global_accesses=Map which functions read and write each global variable., parse_code=Parse the Python code into an AST., process_function=Process a single function definition., read_file=Read the source file., strip_existing_synopsis=Remove existing synopsis headers from code., summarize_initialization_sequence=Summarize module initialization sequence., visit_AnnAssign=Handles ann assign., visit_Assign=Iterates and processes items., visit_AsyncFunctionDef=Handles async function def., visit_AugAssign=Handles aug assign., visit_ExceptHandler=Handles except handler., visit_For=Iterates and processes items., visit_FunctionDef=Handles function def., visit_Global=Handles global., visit_Import=Iterates and processes items., visit_ImportFrom=Iterates and processes items., visit_Name=Orchestrates multiple operations., visit_Nonlocal=Handles nonlocal., visit_With=Iterates and processes items.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# CodeAnalyzer.__init__(self, filepath: str, state = None, *, include_machine_block: bool = True) -> None
#   Initialize the analyzer with a file path and optional shared state.
#
# CodeAnalyzer._analyze_function_accesses(self, func_node: ast.AST, func_name: str) -> None
#   Populate reads/writes for a function using scope indexes.
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
# CodeAnalyzer.build_symbol_indexes(self) -> None
#   Build scope indexes for this file's AST.
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
#   Find all global variable assignments and references using proper scope analysis.
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
# CodeAnalyzer.map_global_accesses(self) -> None
#   Map which functions read and write each global variable.
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
# GlobalAccessVisitor.__init__(self, module_assigned: Set[str], module_imported: Set[str], func_params: Set[str], func_locals: Set[str], func_globals_declared: Set[str]) -> None
#
# GlobalAccessVisitor._is_true_global(self, name: str) -> bool
#
# GlobalAccessVisitor.visit_Name(self, node: ast.Name) -> None
#
# ScopeIndexer.__init__(self) -> None
#
# ScopeIndexer._collect_params(self, node: ast.AST) -> Set[str]
#
# ScopeIndexer._enter_func(self, name: str, node: ast.AST) -> None
#
# ScopeIndexer._exit_func(self) -> None
#
# ScopeIndexer.visit_AnnAssign(self, node: ast.AnnAssign) -> None
#
# ScopeIndexer.visit_Assign(self, node: ast.Assign) -> None
#
# ScopeIndexer.visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None
#
# ScopeIndexer.visit_AugAssign(self, node: ast.AugAssign) -> None
#
# ScopeIndexer.visit_ExceptHandler(self, node: ast.ExceptHandler) -> None
#
# ScopeIndexer.visit_For(self, node: ast.For) -> None
#
# ScopeIndexer.visit_FunctionDef(self, node: ast.FunctionDef) -> None
#
# ScopeIndexer.visit_Global(self, node: ast.Global) -> None
#
# ScopeIndexer.visit_Import(self, node: ast.Import) -> None
#
# ScopeIndexer.visit_ImportFrom(self, node: ast.ImportFrom) -> None
#
# ScopeIndexer.visit_Name(self, node: ast.Name) -> None
#
# ScopeIndexer.visit_Nonlocal(self, node: ast.Nonlocal) -> None
#
# ScopeIndexer.visit_With(self, node: ast.With) -> None
#
# _names_in_target(target: ast.AST) -> Set[str]
#   Extract all simple names bound by an assignment/target expression.
#
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   ScopeIndexer (line 27):
#     - ScopeIndexer.__init__()
#     - ScopeIndexer.visit_Assign()
#     - ScopeIndexer.visit_AnnAssign()
#     - ScopeIndexer.visit_AugAssign()
#     - ScopeIndexer.visit_Import()
#     - ScopeIndexer.visit_ImportFrom()
#     - ScopeIndexer.visit_FunctionDef()
#     - ScopeIndexer.visit_AsyncFunctionDef()
#     - ScopeIndexer._enter_func()
#     - ScopeIndexer._exit_func()
#     - ScopeIndexer._collect_params()
#     - ScopeIndexer.visit_Name()
#     - ScopeIndexer.visit_For()
#     - ScopeIndexer.visit_With()
#     - ScopeIndexer.visit_ExceptHandler()
#     - ScopeIndexer.visit_Global()
#     - ScopeIndexer.visit_Nonlocal()
#   GlobalAccessVisitor (line 158):
#     - GlobalAccessVisitor.__init__()
#     - GlobalAccessVisitor._is_true_global()
#     - GlobalAccessVisitor.visit_Name()
#   CodeAnalyzer (line 202):
#     - CodeAnalyzer.__init__()
#     - CodeAnalyzer.read_file()
#     - CodeAnalyzer.strip_existing_synopsis()
#     - CodeAnalyzer.parse_code()
#     - CodeAnalyzer.analyze()
#     - CodeAnalyzer.build_symbol_indexes()
#     - CodeAnalyzer._analyze_function_accesses()
#     - CodeAnalyzer.find_globals()
#     - CodeAnalyzer.analyze_classes()
#     - CodeAnalyzer.analyze_functions()
#     - CodeAnalyzer.map_global_accesses()
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
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - __init__()
#
# - visit_Assign()
#
# - visit_AnnAssign()
#
# - visit_AugAssign()
#
# - visit_Import()
#
# - visit_ImportFrom()
#
# - visit_FunctionDef()
#
# - visit_AsyncFunctionDef()
#
# - _enter_func()
#
# - _exit_func()
#
# - _collect_params()
#
# - visit_Name()
#
# - visit_For()
#
# - visit_With()
#
# - visit_ExceptHandler()
#
# - visit_Global()
#
# - visit_Nonlocal()
#
# - _is_true_global()
#
# - read_file()
#
# - strip_existing_synopsis()
#
# - parse_code()
#
# - analyze()
#
# - build_symbol_indexes()
#
# - _analyze_function_accesses()
#
# - find_globals()
#
# - analyze_classes()
#
# - analyze_functions()
#
# - map_global_accesses()
#
# - _is_local_module()
#
# - find_imports()
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
#   visit_Assign() — calls isinstance, self.generic_visit, self.module_assigned.add; no return value
#   visit_AnnAssign() — calls isinstance, self.generic_visit, self.module_assigned.add; no return value
#   visit_AugAssign() — calls isinstance, self.generic_visit, self.module_assigned.add; no return value
#   visit_Import() — calls alias.name.split, self.generic_visit, self.module_imported.add; no return value
#   visit_ImportFrom() — calls self.generic_visit, self.module_imported.add; no return value
#   visit_FunctionDef() — calls self._enter_func, self._exit_func, self.generic_visit; no return value
#   visit_AsyncFunctionDef() — calls self._enter_func, self._exit_func, self.generic_visit; no return value
#   _enter_func() — calls self._collect_params, self._func_stack.append, set; no return value
#   _exit_func() — calls self._func_stack.pop; no return value
#   _collect_params() — calls isinstance, params.add, set; returns value
#   visit_For() — calls _names_in_target, add, self.generic_visit; no return value
#   visit_With() — calls _names_in_target, add, self.generic_visit; no return value
#   visit_ExceptHandler() — calls add, self.generic_visit; no return value
#   visit_Global() — calls self.generic_visit, update; no return value
#   visit_Nonlocal() — calls self.generic_visit, update; no return value
#   _names_in_target() — calls _names_in_target, isinstance, names.add, names.update, set; returns value
#   _is_true_global() — calls name.startswith; returns value
#   visit_Name() — calls isinstance, self._is_true_global, self.generic_visit, self.reads.add, self.writes.add; no return value
#   __init__() — calls defaultdict, new_state, os.path.abspath, os.path.basename, os.path.dirname, self.parse_code; no return value
#   read_file() — calls Exception, f.read, open; returns value
#   strip_existing_synopsis() — calls code.split, enumerate, join, len, line.startswith, startswith; returns value
#   parse_code() — calls Exception, ast.parse; no return value
#   analyze() — calls extra_calls.items, extra_transitions.items, self.analyze_classes, self.analyze_functions, self.build_call_graph, self.build_symbol_indexes; no return value
#   build_symbol_indexes() — calls ScopeIndexer, self.scope_idx.visit; no return value
#   _analyze_function_accesses() — calls GlobalAccessVisitor, gav.visit, self.functions.setdefault, self.scope_idx.func_globals_declared.get, self.scope_idx.func_locals.get, self.scope_idx.func_params.get; no return value
#   find_globals() — calls ScopeIndexer, indexer.visit; no return value
#   analyze_classes() — calls isinstance; no return value
#   analyze_functions() — calls add, ast.walk, get, isinstance, self._analyze_function_accesses, self._call_to_name; no return value
#   map_global_accesses() — calls add, func_info.get, self.functions.items, self.shared_state_map.items, set, update; no return value
#   _is_local_module() — calls module_name.replace, os.path.exists, os.path.join; returns value
#   find_imports() — calls add, ast.walk, getattr, isinstance, self._is_local_module, self.imports.append; no return value
#   find_threading() — calls ast.walk, isinstance, self.threads_found.append, sorted; no return value
#   find_hotkeys_and_ui_binds() — calls ast.walk, funcname.endswith, isinstance, len, self._call_to_name, self.hotkeys_command_bind.append; no return value
#   find_file_io() — calls add, any, ast.walk, fullname.endswith, isinstance, self._call_to_name; no return value
#   _extract_open_args() — calls isinstance, len, str; returns value
#   build_call_graph() — calls add, self.functions.items; no return value
#   detect_state_machines() — calls StateMachineDetector, detector.detect, items, set, update, warnings.warn; no return value
#   detect_ui_after_usage() — calls ast.walk, funcname.endswith, isinstance, self._call_to_name, self._enclosing_function_name, self.ui_after_users.add; no return value
#   summarize_initialization_sequence() — calls isinstance, self._call_to_name, self.init_sequence.append; no return value
#   _call_to_name() — calls isinstance, join, parts.append, reversed; returns value
#   _format_call_name() — calls self._call_to_name; returns value
#   _enclosing_function_name() — calls any, ast.walk, isinstance; returns value
#   extract_call_graph() — calls self.call_graph.items, v.copy; returns value
#   extract_state_transitions() — calls add, ast.walk, defaultdict, isinstance, str, target.id.endswith; returns value
#   extract_hotkey_bindings() — calls pretty.append; returns value
#   infer_function_behavior() — pure/local computation; returns value
#   _safe_unparse() — calls ast.unparse, isinstance, len; returns value
#   _render_arg() — calls self._safe_unparse; returns value
#   extract_function_signatures() — calls ast.get_docstring, getattr, isinstance, len, list, parts.append; no return value
#   process_function() — calls ast.get_docstring, getattr, len, list, parts.append, self._render_arg; no return value
#===============================================================================
#
# 🔧 MODULARIZATION RECOMMENDATIONS:
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
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
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


# =============================================================================
# SCOPE & ACCESS ANALYZERS
# =============================================================================
class ScopeIndexer(ast.NodeVisitor):
    """
    Builds symbol indexes:
      - module_assigned: names assigned at module level
      - module_imported: names imported at module level (to exclude)
      - func_params/locals/globals_declared: per-function local symbols
    """
    def __init__(self):
        self.module_assigned: Set[str] = set()
        self.module_imported: Set[str] = set()
        self.func_params: Dict[str, Set[str]] = {}
        self.func_locals: Dict[str, Set[str]] = {}
        self.func_globals_declared: Dict[str, Set[str]] = {}
        self.func_nonlocals_declared: Dict[str, Set[str]] = {}
        self._func_stack: List[str] = []  # qualified names if you have nesting

    # ---------- Module-level ----------
    def visit_Assign(self, node: ast.Assign):
        if not self._func_stack:  # at module scope
            for t in node.targets:
                if isinstance(t, ast.Name):
                    self.module_assigned.add(t.id)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign):
        if not self._func_stack and isinstance(node.target, ast.Name):
            self.module_assigned.add(node.target.id)
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign):
        if not self._func_stack and isinstance(node.target, ast.Name):
            self.module_assigned.add(node.target.id)
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import):
        if not self._func_stack:
            for alias in node.names:
                if alias.asname:
                    self.module_imported.add(alias.asname)
                else:
                    # 'import pkg.subpkg' exposes 'pkg' in module scope
                    self.module_imported.add(alias.name.split(".")[0])
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        if not self._func_stack:
            for alias in node.names:
                self.module_imported.add(alias.asname or alias.name)
        self.generic_visit(node)

    # ---------- Functions & inner scopes ----------
    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._enter_func(node.name, node)
        self.generic_visit(node)
        self._exit_func()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self._enter_func(node.name, node)
        self.generic_visit(node)
        self._exit_func()

    def _enter_func(self, name: str, node: ast.AST):
        self._func_stack.append(name)
        self.func_params[name] = self._collect_params(node)
        self.func_locals[name] = set()
        self.func_globals_declared[name] = set()
        self.func_nonlocals_declared[name] = set()

    def _exit_func(self):
        self._func_stack.pop()

    def _collect_params(self, node: ast.AST) -> Set[str]:
        params: Set[str] = set()
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            a = node.args
            for arg in (a.posonlyargs + a.args + a.kwonlyargs):
                params.add(arg.arg)
            if a.vararg:
                params.add(a.vararg.arg)
            if a.kwarg:
                params.add(a.kwarg.arg)
        return params

    # locals via assignment/targets inside a function
    def visit_Name(self, node: ast.Name):
        if self._func_stack and isinstance(node.ctx, ast.Store):
            self.func_locals[self._func_stack[-1]].add(node.id)
        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        if self._func_stack:
            for name in _names_in_target(node.target):
                self.func_locals[self._func_stack[-1]].add(name)
        self.generic_visit(node)

    def visit_With(self, node: ast.With):
        if self._func_stack:
            for item in node.items:
                if item.optional_vars is not None:
                    for name in _names_in_target(item.optional_vars):
                        self.func_locals[self._func_stack[-1]].add(name)
        self.generic_visit(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler):
        if self._func_stack and node.name:
            self.func_locals[self._func_stack[-1]].add(node.name)
        self.generic_visit(node)

    def visit_Global(self, node: ast.Global):
        if self._func_stack:
            self.func_globals_declared[self._func_stack[-1]].update(node.names)
        self.generic_visit(node)

    def visit_Nonlocal(self, node: ast.Nonlocal):
        if self._func_stack:
            self.func_nonlocals_declared[self._func_stack[-1]].update(node.names)
        self.generic_visit(node)


def _names_in_target(target: ast.AST) -> Set[str]:
    """Extract all simple names bound by an assignment/target expression."""
    names: Set[str] = set()
    if isinstance(target, ast.Name):
        names.add(target.id)
    elif isinstance(target, (ast.Tuple, ast.List)):
        for elt in target.elts:
            names.update(_names_in_target(elt))
    # ignore attributes/subscripts—they don't bind simple names
    return names


class GlobalAccessVisitor(ast.NodeVisitor):
    """
    Tracks reads/writes of *true globals* in a function, given:
      - module_assigned (module-level vars)
      - module_imported (module-level imports, excluded)
      - func_params, func_locals, func_globals_declared/nonlocals
    """
    def __init__(self,
                 module_assigned: Set[str],
                 module_imported: Set[str],
                 func_params: Set[str],
                 func_locals: Set[str],
                 func_globals_declared: Set[str]):
        self.module_assigned = set(module_assigned)
        self.module_imported = set(module_imported)
        self.func_params = set(func_params)
        self.func_locals = set(func_locals)
        self.func_globals_declared = set(func_globals_declared)

        self.reads: Set[str] = set()
        self.writes: Set[str] = set()

    def _is_true_global(self, name: str) -> bool:
        if name.startswith("__"):
            return False
        if name in self.func_params:
            return False
        if name in self.module_imported:
            return False
        # Treat as global if either declared global in this function
        # OR it's a module-level assigned name.
        # Note: Don't exclude func_locals here because variables declared as global
        # are both in func_locals (due to assignment) and func_globals_declared
        return (name in self.func_globals_declared) or (name in self.module_assigned)

    def visit_Name(self, node: ast.Name):
        if self._is_true_global(node.id):
            if isinstance(node.ctx, ast.Load):
                self.reads.add(node.id)
            elif isinstance(node.ctx, ast.Store):
                self.writes.add(node.id)
        self.generic_visit(node)


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
        
        # Exception handling
        self.exception_handlers: List[Dict[str, object]] = []

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
        # Build symbol indexes first
        self.build_symbol_indexes()
        
        # Basic analysis
        self.find_globals()
        self.analyze_classes()
        self.analyze_functions()
        self.find_imports()
        self.find_threading()
        self.find_hotkeys_and_ui_binds()
        self.find_exception_handlers()
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
        
        # NEW: Map which functions read/write each global
        self.map_global_accesses()

    def build_symbol_indexes(self):
        """Build scope indexes for this file's AST."""
        self.scope_idx = ScopeIndexer()
        self.scope_idx.visit(self.tree)

    def _analyze_function_accesses(self, func_node: ast.AST, func_name: str):
        """Populate reads/writes for a function using scope indexes."""
        params = self.scope_idx.func_params.get(func_name, set())
        locals_ = self.scope_idx.func_locals.get(func_name, set())
        decl_globals = self.scope_idx.func_globals_declared.get(func_name, set())
        gav = GlobalAccessVisitor(
            module_assigned=self.scope_idx.module_assigned,
            module_imported=self.scope_idx.module_imported,
            func_params=params,
            func_locals=locals_,
            func_globals_declared=decl_globals
        )
        gav.visit(func_node)
        self.functions.setdefault(func_name, {})
        self.functions[func_name]["reads"] = gav.reads
        self.functions[func_name]["writes"] = gav.writes
        self.functions[func_name]["ast_node"] = func_node

    def find_globals(self):
        """Find all global variable assignments and references using proper scope analysis."""
        # Use the new ScopeIndexer for accurate scope analysis
        indexer = ScopeIndexer()
        indexer.visit(self.tree)
        
        # Store the scope information for use in analyze_functions
        self.scope_indexer = indexer
        
        # The globals_found will be determined by the GlobalAccessVisitor
        # when it analyzes each function with proper scope context
        self.globals_found = indexer.module_assigned

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
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                info = {
                    'line': node.lineno,
                    'reads': set(),
                    'writes': set(),
                    'calls': set(),
                    'returns_value': False
                }
                
                # ============================================================================
                # DETECT GLOBAL READS / WRITES INSIDE THIS FUNCTION
                # ============================================================================
                # Use the new enhanced function access analysis
                self._analyze_function_accesses(node, node.name)
                func_name = node.name
                
                # Preserve reads/writes from scope analysis
                existing_reads = self.functions.get(func_name, {}).get("reads", set())
                existing_writes = self.functions.get(func_name, {}).get("writes", set())
                info["reads"] = existing_reads
                info["writes"] = existing_writes
                
                # Still need to track calls and return values
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Call):
                        callee = self._call_to_name(sub.func)
                        if callee:
                            info['calls'].add(callee)
                    elif isinstance(sub, ast.Return) and sub.value is not None:
                        info['returns_value'] = True
                        
                self.functions[func_name] = info
                self.functions[func_name]["ast_node"] = node

    def map_global_accesses(self):
        """Map which functions read and write each global variable."""
        self.shared_state_map: Dict[str, Dict[str, Set[str]]] = {}
        
        for func_name, func_info in self.functions.items():
            for var in func_info.get("reads", set()) | func_info.get("writes", set()):
                if var not in self.shared_state_map:
                    self.shared_state_map[var] = {"readers": set(), "writers": set()}
                
                if var in func_info.get("reads", set()):
                    self.shared_state_map[var]["readers"].add(func_name)
                if var in func_info.get("writes", set()):
                    self.shared_state_map[var]["writers"].add(func_name)
        
        # Merge with existing state_vars
        for var, access_info in self.shared_state_map.items():
            if var not in self.state_vars:
                self.state_vars[var] = {"values": set(), "writers": set(), "readers": set()}
            self.state_vars[var]["writers"].update(access_info["writers"])
            self.state_vars[var]["readers"].update(access_info["readers"])

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
                        
                        # Handle direct function reference
                        if len(node.args) > 1 and isinstance(node.args[1], ast.Name):
                            cb = node.args[1].id
                        
                        # Handle lambda expressions - NEW!
                        elif len(node.args) > 1 and isinstance(node.args[1], ast.Lambda):
                            # Try to extract the actual function being called inside lambda
                            lambda_body = node.args[1].body
                            if isinstance(lambda_body, ast.Call):
                                # Get the function being called in the lambda
                                cb = self._call_to_name(lambda_body.func)
                                # If it's something like main_root.after(0, func), get the final func
                                if lambda_body.args:
                                    for arg in lambda_body.args:
                                        if isinstance(arg, ast.Name):
                                            cb = arg.id
                                            break
                        
                        # Handle keyword argument (callback=...)
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

    def find_exception_handlers(self):
        """Find try-except blocks and what they handle."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Try):
                # Extract what exceptions are caught
                exception_types = []
                for handler in node.handlers:
                    if handler.type:
                        # Specific exception like "except ValueError:"
                        if isinstance(handler.type, ast.Name):
                            exception_types.append(handler.type.id)
                        elif isinstance(handler.type, ast.Attribute):
                            exception_types.append(self._call_to_name(handler.type))
                        elif isinstance(handler.type, ast.Tuple):
                            # Multiple exceptions like "except (ValueError, TypeError):"
                            for exc in handler.type.elts:
                                if isinstance(exc, ast.Name):
                                    exception_types.append(exc.id)
                                elif isinstance(exc, ast.Attribute):
                                    exception_types.append(self._call_to_name(exc))
                    else:
                        # Bare "except:" catches everything
                        exception_types.append("all exceptions")
                
                # Store exception handler info
                handler_info = {
                    'line': node.lineno,
                    'catches': exception_types if exception_types else ['all exceptions']
                }
                self.exception_handlers.append(handler_info)

    def find_file_io(self):
        """Find file I/O operations."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call):
                # Handle open() calls (existing logic)
                if isinstance(node.func, ast.Name) and node.func.id == 'open':
                    path, mode = self._extract_open_args(node)
                    if path:
                        (self.io_writes if any(m in mode for m in ('w', 'a', 'x', '+')) else self.io_reads).add(path)
                
                # Handle attribute-based calls (expanded logic)
                if isinstance(node.func, ast.Attribute):
                    fullname = self._call_to_name(node.func)
                    
                    # JSON operations (existing)
                    if fullname.endswith('json.load'):
                        self.io_reads.add('json.load(...)')
                    elif fullname.endswith('json.dump'):
                        self.io_writes.add('json.dump(...)')
                    
                    # File system operations (NEW)
                    elif fullname == 'os.path.exists':
                        path = self._extract_string_arg(node.args[0]) if node.args else 'unknown'
                        self.io_reads.add(path)
                    elif fullname == 'os.remove':
                        path = self._extract_string_arg(node.args[0]) if node.args else 'unknown'
                        self.io_writes.add(f"removes {path}")
                    elif fullname == 'os.unlink':
                        path = self._extract_string_arg(node.args[0]) if node.args else 'unknown'
                        self.io_writes.add(f"removes {path}")
                    elif fullname == 'os.rename':
                        old_path = self._extract_string_arg(node.args[0]) if len(node.args) > 0 else 'unknown'
                        new_path = self._extract_string_arg(node.args[1]) if len(node.args) > 1 else 'unknown'
                        self.io_writes.add(f"renames {old_path} to {new_path}")
                    
                    # Image operations (NEW)
                    elif fullname == 'Image.open':
                        path = self._extract_string_arg(node.args[0]) if node.args else 'unknown'
                        self.io_reads.add(path)
                    
                    # Pickle operations (NEW)
                    elif fullname.endswith('pickle.load'):
                        path = self._extract_string_arg(node.args[0]) if node.args else 'unknown'
                        self.io_reads.add(path)
                    elif fullname.endswith('pickle.dump'):
                        path = self._extract_string_arg(node.args[1]) if len(node.args) > 1 else 'unknown'
                        self.io_writes.add(path)

    def _extract_string_arg(self, arg_node: ast.AST) -> str:
        """Extract string value from an AST argument node."""
        if isinstance(arg_node, ast.Constant) and isinstance(arg_node.value, str):
            return str(arg_node.value)
        elif isinstance(arg_node, ast.Str):  # Python < 3.8 compatibility
            return str(arg_node.s)
        return "unknown"

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