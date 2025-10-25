#===============================================================================
# CODE SYNOPSIS: __init__.py
# SYNOPSIS_HASH: 2ff565536f107dbf5c2fe14707a1ba214cbd95863ff358cf65078c23c931b130
# Generated: 2025-10-24 19:14:51
# INTENT: Handles the target entities.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 27
#   Functions: 0
#   Classes: 0
#   Global Variables: 3
#
# Key Dependencies:
#   (Local modules):
#     * behavioral_analysis
#     * core_analyzer
#     * file_io
#     * intent_inference
#     * synopsis_renderer
#     * utils
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 19:14:51
# FILE: __init__.py
# IMPORTS_EXTERNAL: 
# IMPORTS_LOCAL: behavioral_analysis, core_analyzer, file_io, intent_inference, synopsis_renderer, utils
# GLOBALS: __all__, __author__, __version__
# FUNCTIONS: 
# RETURNS: 
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: 
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: 
# STATE_VARS: 
# INIT_SEQUENCE: 
# INTENT: Handles the target entities.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
#===============================================================================
#
# 📊 DATA FLOW SUMMARY:
#
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
"""
Code Synopsis Annotator - Modular Code Analysis Tool

A comprehensive Python code analyzer that generates detailed synopsis headers
for Python files, including function call hierarchies, state machine detection,
threading analysis, and modularization recommendations.
"""

import importlib; import sys
for m in ["core_analyzer", "behavioral_analysis", "file_io", "intent_inference", "synopsis_renderer"]:
    if m in sys.modules:
        importlib.reload(sys.modules[m])

from .core_analyzer import CodeAnalyzer
from .behavioral_analysis import BehavioralAnalyzer
from .synopsis_renderer import SynopsisRenderer
from .file_io import FileIOHandler
from .utils import CodeUtils
from .intent_inference import inject_intent  # NEW

__version__ = "2.1.0"  # bumped
__author__ = "Code Synopsis Annotator Team"

__all__ = [
    'CodeAnalyzer',
    'BehavioralAnalyzer', 
    'SynopsisRenderer',
    'FileIOHandler',
    'CodeUtils',
    'inject_intent',  # NEW
]
