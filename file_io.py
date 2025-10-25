#===============================================================================
# CODE SYNOPSIS: file_io.py
# SYNOPSIS_HASH: 9b39106631e2ed65800fec0578f1e5fb43c5c4666a9e7838c22495239182518b
# Generated: 2025-10-25 13:00:59
# INTENT: Creates and manages user interface components. Creates various components.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 216
#   Functions: 7
#   Classes: 1
#   Global Variables: 0
#
# Key Dependencies:
#   - os
#   - sys
#   - time
#   - tkinter
#   - traceback
#   - typing
#   (Local modules):
#     * behavioral_analysis
#     * core_analyzer
#     * synopsis_renderer
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-25 13:00:59
# FILE: file_io.py
# IMPORTS_EXTERNAL: os, sys, time, tkinter, traceback, typing
# IMPORTS_LOCAL: behavioral_analysis, core_analyzer, synopsis_renderer
# GLOBALS: 
# FUNCTIONS: __init__, analyze_file, batch_analyze_files, create_annotated_file, get_analysis_summary, main, select_file_and_analyze
# RETURNS: analyze_file, batch_analyze_files, get_analysis_summary
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: FileIOHandler
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: main,__init__,create_annotated_file,select_file_and_analyze,analyze_file,batch_analyze_files,get_analysis_summary
# STATE_VARS: 
# STATE_MACHINES_COUNT: 0
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Creates and manages user interface components. Creates various components.
# FUNCTION_INTENTS: __init__=Initialize the file I/O handler., analyze_file=Analyze a specific file and create annotated version., batch_analyze_files=Analyze multiple files in batch., create_annotated_file=Create an annotated file with synopsis header., get_analysis_summary=Get a summary of analysis results., main=Main entry point for the application., select_file_and_analyze=Select a file and run the complete analysis workflow.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# FileIOHandler.__init__(self) -> None
#   Initialize the file I/O handler.
#
# FileIOHandler.analyze_file(self, filepath: str) -> bool
#   Analyze a specific file and create annotated version.
#
# FileIOHandler.batch_analyze_files(self, filepaths: list) -> dict
#   Analyze multiple files in batch.
#
# FileIOHandler.create_annotated_file(self, analyzer: CodeAnalyzer, output_path: str) -> None
#   Create an annotated file with synopsis header.
#
# FileIOHandler.get_analysis_summary(self, analyzer: CodeAnalyzer) -> dict
#   Get a summary of analysis results.
#
# FileIOHandler.select_file_and_analyze(self) -> None
#   Select a file and run the complete analysis workflow.
#
# main() -> None
#   Main entry point for the application.
#
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   FileIOHandler (line 27):
#     - FileIOHandler.__init__()
#     - FileIOHandler.create_annotated_file()
#     - FileIOHandler.select_file_and_analyze()
#     - FileIOHandler.analyze_file()
#     - FileIOHandler.batch_analyze_files()
#     - FileIOHandler.get_analysis_summary()
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - main()
#
# - __init__()
#
# - create_annotated_file()
#
# - select_file_and_analyze()
#
# - analyze_file()
#
# - batch_analyze_files()
#
# - get_analysis_summary()
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
#   __init__() — pure/local computation; no return value
#   create_annotated_file() — calls BehavioralAnalyzer, Exception, SynopsisRenderer, f.write, open, renderer.generate_synopsis_header; no return value
#   select_file_and_analyze() — calls CodeAnalyzer, analyzer.analyze, filedialog.askopenfilename, input, len, messagebox.showerror; no return value
#   analyze_file() — calls CodeAnalyzer, analyzer.analyze, print, self.create_annotated_file; returns value
#   batch_analyze_files() — calls print, self.analyze_file; returns value
#   get_analysis_summary() — calls len; returns value
#   main() — calls FileIOHandler, handler.analyze_file, handler.select_file_and_analyze, len, print, sys.exit; no return value
#===============================================================================
#
# 🔧 MODULARIZATION RECOMMENDATIONS:
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
"""
File I/O Handler - File operations and UI interactions.

This module handles file operations, UI interactions, and the main
entry point for the code synopsis annotator application.
"""

import os
import sys
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Optional

from .core_analyzer import CodeAnalyzer
from .behavioral_analysis import BehavioralAnalyzer
from .synopsis_renderer import SynopsisRenderer


class FileIOHandler:
    """
    Handles file I/O operations and UI interactions.
    
    This class manages file operations, user interface interactions,
    and coordinates the analysis workflow.
    """
    
    def __init__(self):
        """Initialize the file I/O handler."""
        pass
    
    def create_annotated_file(self, analyzer: CodeAnalyzer, output_path: str):
        """Create an annotated file with synopsis header."""
        behavioral_analyzer = BehavioralAnalyzer(analyzer)
        renderer = SynopsisRenderer(analyzer, behavioral_analyzer)
        
        synopsis_header = renderer.generate_synopsis_header()
        annotated_code = synopsis_header + analyzer.code
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(annotated_code)
        except PermissionError as e:
            raise Exception(f"Permission error writing file: {e}")

    def select_file_and_analyze(self):
        """Select a file and run the complete analysis workflow."""
        try:
            root = tk.Tk()
            root.withdraw()
            root.lift()
            root.attributes('-topmost', True)
            root.focus_force()
            root.update()
            
            filepath = filedialog.askopenfilename(
                title="Select Python file to analyze",
                filetypes=[("Python files", "*.py *.pyw"), ("All files", "*.*")]
            )
            print(f"File selected: {filepath}")
            
            if filepath:
                time.sleep(0.3)
            else:
                print("No file selected - dialog was cancelled")
        except Exception as e:
            print(f"Error in file selection: {e}")
            import traceback
            traceback.print_exc()
            return

        if not filepath:
            messagebox.showinfo("Cancelled", "No file selected. Exiting.")
            return

        try:
            # Run analysis
            analyzer = CodeAnalyzer(filepath, include_machine_block=True)
            analyzer.analyze()
            
            # Create annotated file
            self.create_annotated_file(analyzer, filepath)
            
            # Show success message
            messagebox.showinfo(
                "Success!",
                (
                    f"Synopsis added to {os.path.basename(filepath)}!\n\n"
                    f"Functions: {len(analyzer.functions)}\n"
                    f"Classes: {len(analyzer.classes)}\n"
                    f"Globals: {len(analyzer.globals_found)}\n"
                    f"Threads: {len(analyzer.threads_found)}\n"
                )
            )
            
            # Open file in default editor
            try:
                if os.name == 'nt':
                    os.system(f'notepad "{filepath}"')
                elif os.name == 'posix':
                    os.system(f'open "{filepath}"' if sys.platform == 'darwin' else f'xdg-open "{filepath}"')
            except Exception:
                pass
            
            print("\n" + "="*50)
            print("ANALYSIS COMPLETE!")
            print("="*50)
            print(f"File processed: {os.path.basename(filepath)}")
            print("The synopsis has been added to your file.")
            
            try:
                input("Press Enter to exit...")
            except Exception:
                pass
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n\n{str(e)}")

    def analyze_file(self, filepath: str) -> bool:
        """
        Analyze a specific file and create annotated version.
        
        Args:
            filepath: Path to the Python file to analyze
            
        Returns:
            True if analysis was successful, False otherwise
        """
        try:
            print(f"Analyzing file: {filepath}")
            
            # Run analysis
            analyzer = CodeAnalyzer(filepath, include_machine_block=True)
            analyzer.analyze()
            
            # Create annotated file
            self.create_annotated_file(analyzer, filepath)
            
            print("Analysis complete!")
            return True
            
        except Exception as e:
            print(f"Error analyzing file {filepath}: {e}")
            return False

    def batch_analyze_files(self, filepaths: list) -> dict:
        """
        Analyze multiple files in batch.
        
        Args:
            filepaths: List of file paths to analyze
            
        Returns:
            Dictionary with results for each file
        """
        results = {}
        
        for filepath in filepaths:
            print(f"Processing: {filepath}")
            results[filepath] = self.analyze_file(filepath)
        
        return results

    def get_analysis_summary(self, analyzer: CodeAnalyzer) -> dict:
        """
        Get a summary of analysis results.
        
        Args:
            analyzer: The CodeAnalyzer instance
            
        Returns:
            Dictionary with analysis summary
        """
        return {
            'filename': analyzer.filename,
            'functions': len(analyzer.functions),
            'classes': len(analyzer.classes),
            'globals': len(analyzer.globals_found),
            'threads': len(analyzer.threads_found),
            'imports_external': len(analyzer.imports_external),
            'imports_local': len(analyzer.imports_local),
            'io_reads': len(analyzer.io_reads),
            'io_writes': len(analyzer.io_writes),
            'call_roots': len(analyzer.call_roots),
            'state_vars': len(analyzer.state_vars),
            'ui_after_users': len(analyzer.ui_after_users)
        }


def main():
    """Main entry point for the application."""
    if len(sys.argv) > 1:
        # Command line mode
        filepath = sys.argv[1]
        print(f"Using file from command line: {filepath}")
        
        handler = FileIOHandler()
        success = handler.analyze_file(filepath)
        
        if not success:
            sys.exit(1)
    else:
        # Interactive mode
        handler = FileIOHandler()
        handler.select_file_and_analyze()


if __name__ == "__main__":
    main()
