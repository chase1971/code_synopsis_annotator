#===============================================================================
# CODE SYNOPSIS: main.py
# SYNOPSIS_HASH: ec67de976d8877e80aaa2b24dabcc9a241f7c6ba6a6eea125a6f42a7e9645c64
# Generated: 2025-10-24 17:51:16
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 115
#   Functions: 3
#   Classes: 0
#   Global Variables: 9
#
# Key Dependencies:
#   - code_synopsis_annotator.behavioral_analysis
#   - code_synopsis_annotator.core_analyzer
#   - code_synopsis_annotator.file_io
#   - code_synopsis_annotator.synopsis_renderer
#   - os
#   - sys
#   - typing
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 17:51:16
# FILE: main.py
# IMPORTS_EXTERNAL: code_synopsis_annotator.behavioral_analysis, code_synopsis_annotator.core_analyzer, code_synopsis_annotator.file_io, code_synopsis_annotator.synopsis_renderer, os, sys, typing
# IMPORTS_LOCAL: 
# GLOBALS: analyzer, behavioral_analyzer, filepath, handler, renderer, result, results, success, summary
# FUNCTIONS: analyze_file, batch_analyze, main
# RETURNS: analyze_file, batch_analyze
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: 
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: main,batch_analyze
# STATE_VARS: 
# INIT_SEQUENCE: main()
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
# filepath:
#   Modified by: main, batch_analyze
#   Read by: main, analyze_file, batch_analyze
#
# handler:
#   Modified by: main, analyze_file
#   Read by: main, analyze_file
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   Timing State:
#     - renderer
#   Position State:
#     - analyzer
#     - behavioral_analyzer
#     - summary
#   Config State:
#     - filepath
#===============================================================================
#
# ⚠️ HIGH PRIORITY FUNCTIONS (Modify Multiple Globals):
#
# main() - line 22  (Returns: No)
#   Modifies: filepath, handler, success
#   Reads: filepath, handler, success
#
# analyze_file() - line 60  (Returns: Yes)
#   Modifies: analyzer, behavioral_analyzer, handler, renderer, summary
#   Reads: analyzer, behavioral_analyzer, filepath, handler, renderer, summary
#
# batch_analyze() - line 93  (Returns: Yes)
#   Modifies: filepath, result, results
#   Reads: filepath, result, results
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - main()
#   - print()
#   - len()
#   - exit()
#   - select_file_and_analyze()
#   - exists()
#   - FileIOHandler()
#   - endswith()
#   - analyze_file()
#     - print()
#     - CodeAnalyzer()
#     - BehavioralAnalyzer()
#     - get_analysis_summary()
#     - SynopsisRenderer()
#     - FileIOHandler()
#     - analyze()
#
# - batch_analyze()
#   - print()
#   - analyze_file()
#     - print()
#     - CodeAnalyzer()
#     - BehavioralAnalyzer()
#     - get_analysis_summary()
#     - SynopsisRenderer()
#     - FileIOHandler()
#     - analyze()
#
#===============================================================================
#
# 🚀 INITIALIZATION SEQUENCE:
#
#   1. main()
#===============================================================================
#
# 📊 DATA FLOW SUMMARY:
#
#   main() — reads filepath, handler, success; writes filepath, handler, success; calls FileIOHandler, filepath.endswith, handler.analyze_file, handler.select_file_and_analyze, len, os.path.exists; no return value
#   analyze_file() — reads analyzer, behavioral_analyzer, filepath, handler, renderer, summary; writes analyzer, behavioral_analyzer, handler, renderer, summary; calls BehavioralAnalyzer, CodeAnalyzer, FileIOHandler, SynopsisRenderer, analyzer.analyze, handler.get_analysis_summary; returns value
#   batch_analyze() — reads filepath, result, results; writes filepath, result, results; calls analyze_file, print; returns value
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
#   main() → FileIOHandler, analyze_file, endswith, exists, exit, len, print, select_file_and_analyze
#   analyze_file() → BehavioralAnalyzer, CodeAnalyzer, FileIOHandler, SynopsisRenderer, analyze, get_analysis_summary, print
#   batch_analyze() → analyze_file, print
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
#!/usr/bin/env python3
"""
Code Synopsis Annotator - Main Entry Point

This is the main entry point for the modularized code synopsis annotator.
It provides both command-line and interactive modes for analyzing Python files.
"""

import sys
import os
from typing import Optional

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from code_synopsis_annotator.file_io import FileIOHandler
from code_synopsis_annotator.core_analyzer import CodeAnalyzer
from code_synopsis_annotator.behavioral_analysis import BehavioralAnalyzer
from code_synopsis_annotator.synopsis_renderer import SynopsisRenderer


def main():
    """
    Main entry point for the code synopsis annotator.
    
    Supports both command-line and interactive modes:
    - Command line: python main.py <filepath>
    - Interactive: python main.py (opens file dialog)
    """
    if len(sys.argv) > 1:
        # Command line mode
        filepath = sys.argv[1]
        print(f"Code Synopsis Annotator v2.0.0")
        print(f"Analyzing file: {filepath}")
        
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' does not exist.")
            sys.exit(1)
        
        if not filepath.endswith(('.py', '.pyw')):
            print(f"Warning: File '{filepath}' may not be a Python file.")
        
        handler = FileIOHandler()
        success = handler.analyze_file(filepath)
        
        if success:
            print("Analysis completed successfully!")
        else:
            print("Analysis failed!")
            sys.exit(1)
    else:
        # Interactive mode
        print("Code Synopsis Annotator v2.0.0")
        print("Interactive mode - file dialog will open...")
        
        handler = FileIOHandler()
        handler.select_file_and_analyze()


def analyze_file(filepath: str, include_machine_block: bool = True) -> Optional[dict]:
    """
    Analyze a single file and return results.
    
    Args:
        filepath: Path to the Python file to analyze
        include_machine_block: Whether to include machine-readable data block
        
    Returns:
        Dictionary with analysis results, or None if analysis failed
    """
    try:
        analyzer = CodeAnalyzer(filepath, include_machine_block=include_machine_block)
        analyzer.analyze()
        
        behavioral_analyzer = BehavioralAnalyzer(analyzer)
        renderer = SynopsisRenderer(analyzer, behavioral_analyzer)
        
        # Get analysis summary
        handler = FileIOHandler()
        summary = handler.get_analysis_summary(analyzer)
        
        return {
            'analyzer': analyzer,
            'behavioral_analyzer': behavioral_analyzer,
            'renderer': renderer,
            'summary': summary
        }
    except Exception as e:
        print(f"Error analyzing file {filepath}: {e}")
        return None


def batch_analyze(files: list, include_machine_block: bool = True) -> dict:
    """
    Analyze multiple files in batch.
    
    Args:
        files: List of file paths to analyze
        include_machine_block: Whether to include machine-readable data block
        
    Returns:
        Dictionary with results for each file
    """
    results = {}
    
    for filepath in files:
        print(f"Processing: {filepath}")
        result = analyze_file(filepath, include_machine_block)
        results[filepath] = result
    
    return results


if __name__ == "__main__":
    main()
