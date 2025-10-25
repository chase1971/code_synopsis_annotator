#===============================================================================
# CODE SYNOPSIS: utils.py
# SYNOPSIS_HASH: 6b15330cb38cdd71d41fe1e96b3470e6756b6db67d99893a3bf2a7e21ecdfb8d
# Generated: 2025-10-24 23:31:33
# INTENT: Utility functions and helper methods.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 270
#   Functions: 11
#   Classes: 1
#   Global Variables: 0
#
# Key Dependencies:
#   - ast
#   - os
#   - re
#   - typing
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 23:31:33
# FILE: utils.py
# IMPORTS_EXTERNAL: ast, os, re, typing
# IMPORTS_LOCAL: 
# GLOBALS: 
# FUNCTIONS: call_to_name, categorize_shared_state, enclosing_function_name, extract_hotkey_bindings, extract_open_args, format_call_name, format_file_size, get_file_info, group_functions_by_purpose, is_local_module, safe_filename
# RETURNS: call_to_name, categorize_shared_state, enclosing_function_name, extract_hotkey_bindings, extract_open_args, format_call_name, format_file_size, get_file_info, group_functions_by_purpose, is_local_module, safe_filename
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: CodeUtils
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: is_local_module,call_to_name,format_call_name,enclosing_function_name,extract_open_args,categorize_shared_state,group_functions_by_purpose,extract_hotkey_bindings,safe_filename,format_file_size,get_file_info
# STATE_VARS: mode
# STATE_MACHINES_COUNT: 1
# STATE_TRANSITIONS_COUNT: 2
# INIT_SEQUENCE: 
# INTENT: Utility functions and helper methods.
# FUNCTION_INTENTS: call_to_name=Handles to name., categorize_shared_state=Handles shared state., enclosing_function_name=Handles function name., extract_hotkey_bindings=Retrieves hotkey bindings., extract_open_args=Retrieves open args., format_call_name=Handles call name., format_file_size=Handles file size., get_file_info=Handles file info., group_functions_by_purpose=Organizes functions by purpose., is_local_module=Handles local module., safe_filename=Handles filename.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# CodeUtils.call_to_name(func_node: ast.AST) -> str
#   Convert an AST function node to a string name.
#
# CodeUtils.categorize_shared_state(globals_found: Set[str]) -> List[Tuple[str, List[str]]]
#   Categorize global variables by their likely purpose.
#
# CodeUtils.enclosing_function_name(node: ast.AST, tree: ast.AST) -> Optional[str]
#   Find the function that contains the given node.
#
# CodeUtils.extract_hotkey_bindings(code: str) -> List[str]
#   Extract hotkey bindings from source text using regex.
#
# CodeUtils.extract_open_args(call: ast.Call) -> Tuple[Optional[str], str]
#   Extract file path and mode from open() calls.
#
# CodeUtils.format_call_name(call: ast.Call) -> str
#   Format a function call for display.
#
# CodeUtils.format_file_size(size_bytes: int) -> str
#   Format file size in human-readable format.
#
# CodeUtils.get_file_info(filepath: str) -> Dict[str, Any]
#   Get basic information about a file.
#
# CodeUtils.group_functions_by_purpose(functions: Dict[str, Any]) -> Dict[str, List[str]]
#   Group functions into logical modules for refactoring suggestions.
#
# CodeUtils.is_local_module(module_name: str, dirpath: str) -> bool
#   Check if a module is local to the project.
#
# CodeUtils.safe_filename(filename: str) -> str
#   Create a safe filename by removing or replacing invalid characters.
#
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   CodeUtils (line 17):
#     - CodeUtils.is_local_module()
#     - CodeUtils.call_to_name()
#     - CodeUtils.format_call_name()
#     - CodeUtils.enclosing_function_name()
#     - CodeUtils.extract_open_args()
#     - CodeUtils.categorize_shared_state()
#     - CodeUtils.group_functions_by_purpose()
#     - CodeUtils.extract_hotkey_bindings()
#     - CodeUtils.safe_filename()
#     - CodeUtils.format_file_size()
#     - CodeUtils.get_file_info()
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - is_local_module()
#
# - call_to_name()
#
# - format_call_name()
#
# - enclosing_function_name()
#
# - extract_open_args()
#
# - categorize_shared_state()
#
# - group_functions_by_purpose()
#
# - extract_hotkey_bindings()
#
# - safe_filename()
#
# - format_file_size()
#
# - get_file_info()
#
#===============================================================================
#
# 🔄 STATE MACHINES DETECTED:
#
#   📍 mode (Mode Variable):
#      States: (values unknown)
#      Modified by: extract_open_args
#
#   🔀 Key Transitions:
#      extract_open_args(): *→value, *→kw.value.value
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
#   is_local_module() — calls module_name.replace, os.path.exists, os.path.join; returns value
#   call_to_name() — calls CodeUtils.call_to_name, isinstance; returns value
#   format_call_name() — calls CodeUtils.call_to_name, isinstance; returns value
#   enclosing_function_name() — calls any, ast.walk, isinstance; returns value
#   extract_open_args() — calls isinstance, len; returns value
#   categorize_shared_state() — calls any, cats.items, g.lower, sorted; returns value
#   group_functions_by_purpose() — calls any, append, buckets.items, f.lower, functions.keys, list; returns value
#   extract_hotkey_bindings() — calls cleaned.append, func.strip, hotkey.strip, re.findall, strip; returns value
#   safe_filename() — calls safe_name.replace; returns value
#   format_file_size() — pure/local computation; returns value
#   get_file_info() — calls CodeUtils.format_file_size, os.stat; returns value
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
"""
Utilities - Helper functions and common utilities.

This module contains utility functions and helper methods used
throughout the code synopsis annotator system.
"""

import ast
import os
from typing import Dict, List, Set, Tuple, Optional, Any


class CodeUtils:
    """
    Utility functions for code analysis and processing.
    
    This class provides helper methods for common operations
    in code analysis and processing.
    """
    
    @staticmethod
    def is_local_module(module_name: str, dirpath: str) -> bool:
        """
        Check if a module is local to the project.
        
        Args:
            module_name: Name of the module to check
            dirpath: Directory path of the project
            
        Returns:
            True if the module is local, False otherwise
        """
        if not module_name:
            return False
        candidate_py = os.path.join(dirpath, module_name.replace('.', os.sep) + '.py')
        candidate_pkg = os.path.join(dirpath, module_name.replace('.', os.sep), '__init__.py')
        return os.path.exists(candidate_py) or os.path.exists(candidate_pkg)

    @staticmethod
    def call_to_name(func_node: ast.AST) -> str:
        """
        Convert an AST function node to a string name.
        
        Args:
            func_node: AST node representing a function call
            
        Returns:
            String representation of the function call
        """
        if isinstance(func_node, ast.Name):
            return func_node.id
        if isinstance(func_node, ast.Attribute):
            base = CodeUtils.call_to_name(func_node.value)
            return f"{base}.{func_node.attr}" if base else func_node.attr
        return ""

    @staticmethod
    def format_call_name(call: ast.Call) -> str:
        """
        Format a function call for display.
        
        Args:
            call: AST Call node
            
        Returns:
            Formatted string representation of the call
        """
        if isinstance(call.func, ast.Name):
            return f"{call.func.id}()"
        if isinstance(call.func, ast.Attribute):
            chain = CodeUtils.call_to_name(call.func)
            return f"{chain}()" if chain else "<call>()"
        return "<call>()"

    @staticmethod
    def enclosing_function_name(node: ast.AST, tree: ast.AST) -> Optional[str]:
        """
        Find the function that contains the given node.
        
        Args:
            node: AST node to find the enclosing function for
            tree: Root AST tree to search in
            
        Returns:
            Name of the enclosing function, or None if not found
        """
        for func in ast.walk(tree):
            if isinstance(func, ast.FunctionDef):
                if any(node is n for n in ast.walk(func)):
                    return func.name
        return None

    @staticmethod
    def extract_open_args(call: ast.Call) -> Tuple[Optional[str], str]:
        """
        Extract file path and mode from open() calls.
        
        Args:
            call: AST Call node representing an open() call
            
        Returns:
            Tuple of (path, mode)
        """
        path, mode = None, 'r'
        if call.args and isinstance(call.args[0], ast.Constant) and isinstance(call.args[0].value, str):
            path = call.args[0].value
        if len(call.args) >= 2 and isinstance(call.args[1], ast.Constant) and isinstance(call.args[1].value, str):
            mode = call.args[1].value
        for kw in call.keywords:
            if kw.arg == 'mode' and isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
                mode = kw.value.value
        return path, mode

    @staticmethod
    def categorize_shared_state(globals_found: Set[str]) -> List[Tuple[str, List[str]]]:
        """
        Categorize global variables by their likely purpose.
        
        Args:
            globals_found: Set of global variable names
            
        Returns:
            List of tuples (category_name, variable_list)
        """
        globs = sorted(globals_found)
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

    @staticmethod
    def group_functions_by_purpose(functions: Dict[str, Any]) -> Dict[str, List[str]]:
        """
        Group functions into logical modules for refactoring suggestions.
        
        Args:
            functions: Dictionary of function names to their metadata
            
        Returns:
            Dictionary mapping module names to lists of function names
        """
        fnames = list(functions.keys())
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

    @staticmethod
    def extract_hotkey_bindings(code: str) -> List[str]:
        """
        Extract hotkey bindings from source text using regex.
        
        Args:
            code: Source code text
            
        Returns:
            List of formatted hotkey bindings
        """
        import re
        pattern = r"keyboard\.add_hotkey\(\s*([^)]+?),\s*([^)]+?)\)"
        matches = re.findall(pattern, code)
        cleaned = []
        for hotkey, func in matches:
            hotkey = hotkey.strip().strip('"\'')
            func = func.strip().strip('"\'')
            cleaned.append(f"{hotkey} → {func}")
        return cleaned

    @staticmethod
    def safe_filename(filename: str) -> str:
        """
        Create a safe filename by removing or replacing invalid characters.
        
        Args:
            filename: Original filename
            
        Returns:
            Safe filename string
        """
        invalid_chars = '<>:"/\\|?*'
        safe_name = filename
        for char in invalid_chars:
            safe_name = safe_name.replace(char, '_')
        return safe_name

    @staticmethod
    def format_file_size(size_bytes: int) -> str:
        """
        Format file size in human-readable format.
        
        Args:
            size_bytes: Size in bytes
            
        Returns:
            Formatted size string
        """
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"

    @staticmethod
    def get_file_info(filepath: str) -> Dict[str, Any]:
        """
        Get basic information about a file.
        
        Args:
            filepath: Path to the file
            
        Returns:
            Dictionary with file information
        """
        try:
            stat = os.stat(filepath)
            return {
                'size': stat.st_size,
                'size_formatted': CodeUtils.format_file_size(stat.st_size),
                'modified': stat.st_mtime,
                'created': stat.st_ctime,
                'exists': True
            }
        except OSError:
            return {
                'size': 0,
                'size_formatted': '0 B',
                'modified': 0,
                'created': 0,
                'exists': False
            }
