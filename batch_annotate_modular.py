#===============================================================================
# CODE SYNOPSIS: batch_annotate_modular.py
# SYNOPSIS_HASH: 973fcfa02948997d80767afa493a0f313b075408a57094bbbb0f7720ed288fe5
# Generated: 2025-10-24 22:17:09
# INTENT: Manages external processes. Processes various components.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 398
#   Functions: 23
#   Classes: 1
#   Global Variables: 44
#
# Key Dependencies:
#   - argparse
#   - datetime
#   - glob
#   - hashlib
#   - os
#   - pathlib
#   - shutil
#   - subprocess
#   - sys
#   - threading
#   - tkinter
#   (Local modules):
#     * behavioral_analysis
#     * core_analyzer
#     * intent_inference
#     * project_architect
#     * synopsis_renderer
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 22:17:09
# FILE: batch_annotate_modular.py
# IMPORTS_EXTERNAL: argparse, datetime, glob, hashlib, os, pathlib, shutil, subprocess, sys, threading, tkinter
# IMPORTS_LOCAL: behavioral_analysis, core_analyzer, intent_inference, project_architect, synopsis_renderer
# GLOBALS: ANNOTATOR_VERSION, HEADER_BOUNDARY, all_files, analyzer, app, args, backup_dir, backup_path, base_dir, behavioral_analyzer, btn_frame, category, code_body, code_hash, current_code, current_hash, duration, file, files, folder, frame, has_synopsis, header, header_lines, insert_at, lines, msg, opts, output, parser, path, rel_path, renderer, results, root, skip_patterns, start, stored_hash, synopsis_header, t, total, total_time, up_to_date, versioned_content
# FUNCTIONS: __init__, _build_ui, _process_folder, _process_single, _run, compute_code_hash, extract_existing_hash, find_python_files, format_duration, generate_markdown, get_code_body, is_up_to_date, log, make_backup, open_folder, open_folder_in_explorer, process_batch, process_single_file, run_batch, run_in_thread, run_single, select_file, select_folder
# RETURNS: compute_code_hash, extract_existing_hash, find_python_files, format_duration, get_code_body, is_up_to_date, make_backup, process_batch, process_single_file
# THREAD_TARGETS: fn
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: AnnotatorGUI
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: __init__,_build_ui,open_folder,log,select_file,select_folder,run_in_thread,run_single,run_batch,generate_markdown,_process_single,_process_folder,_run
# STATE_VARS: 
# STATE_MACHINES_COUNT: 0
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Manages external processes. Processes various components.
# FUNCTION_INTENTS: __init__=Handles the target entities., _build_ui=Constructs or generates ui., _process_folder=Handles or executes folder., _process_single=Handles or executes single., _run=Handles the target entities., compute_code_hash=Handles code hash., extract_existing_hash=Retrieves existing hash., find_python_files=Locates or gathers python files., format_duration=Handles duration., generate_markdown=Handles markdown., get_code_body=Handles code body., is_up_to_date=Handles up to date., log=Handles the target entities., make_backup=Handles backup., open_folder=Handles folder., open_folder_in_explorer=Handles folder in explorer., process_batch=Handles or executes batch., process_single_file=Handles or executes single file., run_batch=Handles batch., run_in_thread=Handles in thread., run_single=Handles single., select_file=Handles file., select_folder=Handles folder.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# AnnotatorGUI.__init__(self, root) -> None
#
# AnnotatorGUI._build_ui(self) -> None
#
# AnnotatorGUI._process_folder(self, folder) -> None
#
# AnnotatorGUI._process_single(self, path) -> None
#
# AnnotatorGUI.generate_markdown(self) -> None
#
# AnnotatorGUI.log(self, msg, tag = None) -> None
#
# AnnotatorGUI.open_folder(self) -> None
#
# AnnotatorGUI.run_batch(self) -> None
#
# AnnotatorGUI.run_in_thread(self, fn) -> None
#
# AnnotatorGUI.run_single(self) -> None
#
# AnnotatorGUI.select_file(self) -> None
#
# AnnotatorGUI.select_folder(self) -> None
#
# compute_code_hash(code_text: str) -> str
#
# extract_existing_hash(file_path: str) -> None
#
# find_python_files(directory_path, recursive = False, skip_patterns = None) -> None
#
# format_duration(seconds) -> None
#
# get_code_body(file_path: str) -> None
#
# is_up_to_date(file_path) -> None
#
# make_backup(file_path) -> None
#
# open_folder_in_explorer(path) -> None
#   Open folder in file explorer (cross-platform).
#
# process_batch(files, dry_run = False, backup = True, skip_annotated = False) -> None
#
# process_single_file(file_path, dry_run = False, backup = True) -> None
#
#===============================================================================
#
# ⚡️ THREADING MODEL (CRITICAL)
#
# Threads Found:
#   - fn()
#
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   AnnotatorGUI (line 224):
#     - AnnotatorGUI.__init__()
#     - AnnotatorGUI._build_ui()
#     - AnnotatorGUI.open_folder()
#     - AnnotatorGUI.log()
#     - AnnotatorGUI.select_file()
#     - AnnotatorGUI.select_folder()
#     - AnnotatorGUI.run_in_thread()
#     - AnnotatorGUI.run_single()
#     - AnnotatorGUI.run_batch()
#     - AnnotatorGUI.generate_markdown()
#     - AnnotatorGUI._process_single()
#     - AnnotatorGUI._process_folder()
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
# path:
#   Modified by: find_python_files, open_folder, run_single, run_batch
#   Read by: find_python_files, open_folder_in_explorer, open_folder, run_single, run_batch, _process_single
#
# folder:
#   Modified by: open_folder_in_explorer, select_folder, generate_markdown
#   Read by: open_folder_in_explorer, select_folder, generate_markdown, _process_folder, _run
#
# msg:
#   Modified by: process_single_file, process_batch, _process_single
#   Read by: process_single_file, process_batch, log, _process_single
#
# files:
#   Modified by: find_python_files, _process_folder
#   Read by: find_python_files, process_batch, _process_folder
#
# output:
#   Modified by: generate_markdown, _run
#   Read by: generate_markdown, _run
#
# start:
#   Modified by: process_single_file, process_batch
#   Read by: process_single_file, process_batch
#
# results:
#   Modified by: process_batch, _process_folder
#   Read by: process_batch, _process_folder
#
# category:
#   Modified by: process_single_file, process_batch
#   Read by: process_single_file, process_batch
#
# root:
#   Modified by: find_python_files
#   Read by: find_python_files, __init__
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   UI State:
#     - root
#   Timing State:
#     - duration
#     - renderer
#     - start
#     - total_time
#   Position State:
#     - HEADER_BOUNDARY
#     - analyzer
#     - behavioral_analyzer
#     - category
#     - code_body
#     - has_synopsis
#     - synopsis_header
#   Config State:
#     - all_files
#     - backup_path
#     - file
#     - files
#     - path
#     - rel_path
#===============================================================================
#
# ⚠️ HIGH PRIORITY FUNCTIONS (Modify Multiple Globals):
#
# make_backup() - line 70  (Returns: Yes)
#   Modifies: backup_dir, backup_path, base_dir
#   Reads: backup_dir, backup_path, base_dir
#
# is_up_to_date() - line 79  (Returns: Yes)
#   Modifies: current_code, current_hash, stored_hash
#   Reads: current_code, current_hash, stored_hash
#
# find_python_files() - line 88  (Returns: Yes)
#   Modifies: all_files, files, path, root, skip_patterns
#   Reads: all_files, files, path, root, skip_patterns
#
# process_single_file() - line 146  (Returns: Yes)
#   Modifies: analyzer, behavioral_analyzer, category, code_body, code_hash, duration, has_synopsis, header_lines
#   Reads: HEADER_BOUNDARY, analyzer, behavioral_analyzer, category, code_body, code_hash, duration, has_synopsis
#
# process_batch() - line 199  (Returns: Yes)
#   Modifies: category, msg, rel_path, results, start, total_time
#   Reads: category, files, msg, rel_path, results, start, total_time
#
# _build_ui() - line 241  (Returns: No)
#   Modifies: btn_frame, frame, opts
#   Reads: btn_frame, frame, opts
#
# _process_folder() - line 342  (Returns: No)
#   Modifies: files, results, total
#   Reads: files, folder, results, total
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
# - _build_ui()
#
# - open_folder()
#
# - log()
#
# - select_file()
#
# - select_folder()
#
# - run_in_thread()
#
# - run_single()
#
# - run_batch()
#
# - generate_markdown()
#
# - _process_single()
#
# - _process_folder()
#
# - _run()
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
#   compute_code_hash() — reads ANNOTATOR_VERSION, versioned_content; writes versioned_content; calls hashlib.sha256, hexdigest, versioned_content.encode; returns value
#   extract_existing_hash() — reads header; writes header; calls f.read, header.splitlines, line.split, line.strip, open, startswith; returns value
#   get_code_body() — reads HEADER_BOUNDARY, lines; writes lines; calls enumerate, f.readlines, join, line.strip, open; returns value
#   make_backup() — reads backup_dir, backup_path, base_dir; writes backup_dir, backup_path, base_dir; calls os.makedirs, os.path.basename, os.path.dirname, os.path.join, shutil.copy2; returns value
#   is_up_to_date() — reads current_code, current_hash, stored_hash; writes current_code, current_hash, stored_hash; calls compute_code_hash, extract_existing_hash, get_code_body; returns value
#   find_python_files() — reads all_files, files, path, root, skip_patterns; writes all_files, files, path, root, skip_patterns; calls any, d.startswith, filename.endswith, filename.startswith, files.append, glob.glob; returns value
#   format_duration() — calls divmod, int; returns value
#   open_folder_in_explorer() — reads folder, path; writes folder; calls messagebox.showerror, os.path.dirname, os.path.exists, os.path.isdir, os.startfile, subprocess.Popen; no return value
#   process_single_file() — reads HEADER_BOUNDARY, analyzer, behavioral_analyzer, category, code_body, code_hash; writes analyzer, behavioral_analyzer, category, code_body, code_hash, duration; calls BehavioralAnalyzer, CodeAnalyzer, SynopsisRenderer, analyzer.analyze, any, compute_code_hash; returns value
#   process_batch() — reads category, files, msg, rel_path, results, start; writes category, msg, rel_path, results, start, total_time; calls append, datetime.now, enumerate, format_duration, is_up_to_date, len; returns value
#   __init__() — reads root; calls self._build_ui, self.log, self.root.configure, self.root.geometry, self.root.resizable, self.root.title; no return value
#   _build_ui() — reads btn_frame, frame, opts; writes btn_frame, frame, opts; calls btn_frame.pack, frame.pack, opts.pack, pack, scrolledtext.ScrolledText, self.log_box.config; no return value
#   open_folder() — reads path; writes path; calls messagebox.showerror, open_folder_in_explorer, self.path_var.get, strip; no return value
#   log() — reads msg, t; writes t; calls datetime.now, self.log_box.config, self.log_box.insert, self.log_box.see, self.root.update_idletasks, strftime; no return value
#   select_file() — reads file; writes file; calls filedialog.askopenfilename, self.log, self.path_var.set; no return value
#   select_folder() — reads folder; writes folder; calls filedialog.askdirectory, self.log, self.path_var.set; no return value
#   run_in_thread() — calls start, threading.Thread; no return value
#   run_single() — reads path; writes path; calls messagebox.showerror, os.path.isfile, self._process_single, self.path_var.get, self.run_in_thread, strip; no return value
#   run_batch() — reads path; writes path; calls messagebox.showerror, os.path.isdir, self._process_folder, self.path_var.get, self.run_in_thread, strip; no return value
#   generate_markdown() — reads folder, output; writes folder, output; calls build_project_summary, messagebox.showerror, os.path.isdir, self.log, self.path_var.get, self.run_in_thread; no return value
#   _run() — reads folder, output; writes output; calls build_project_summary, self.log; no return value
#   _process_single() — reads msg, path; writes msg; calls format_duration, process_single_file, self.backup_var.get, self.dry_run_var.get, self.log; no return value
#   _process_folder() — reads files, folder, results, total; writes files, results, total; calls find_python_files, len, process_batch, results.values, self.backup_var.get, self.dry_run_var.get; no return value
#===============================================================================
#
# 🔧 MODULARIZATION RECOMMENDATIONS:
#
# ⚠️ THREADING: Multiple threads access shared state.
#    1. Keep thread functions with their state variables
#    2. Add proper locking if splitting state
#    3. Ensure thread-safe access to shared resources
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
#!/usr/bin/env python3
# =============================================================================
# BATCH ANNOTATE MODULAR - DARK MODE GUI + FOLDER OPEN + PROJECT SUMMARY
# =============================================================================

import os
import sys
import glob
import argparse
import threading
import hashlib
import shutil
import subprocess
import tkinter as tk

# Version of annotation system - increment when logic changes
ANNOTATOR_VERSION = "2.1.0"
from tkinter import filedialog, scrolledtext, messagebox
from datetime import datetime
from pathlib import Path

try:
    from core_analyzer import CodeAnalyzer
    from behavioral_analysis import BehavioralAnalyzer
    from synopsis_renderer import SynopsisRenderer
    from intent_inference import inject_intent
    from project_architect import build_project_summary  # NEW
except ImportError as e:
    print("ERROR: Cannot import required modules")
    print(f"Error details: {e}")
    sys.exit(1)


HEADER_BOUNDARY = "# === END SYNOPSIS HEADER ==="


# =============================================================================
# Utility Functions
# =============================================================================
def compute_code_hash(code_text: str) -> str:
    versioned_content = f"{code_text}||ANNOTATOR_V{ANNOTATOR_VERSION}"
    return hashlib.sha256(versioned_content.encode("utf-8")).hexdigest()


def extract_existing_hash(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            header = f.read(1000)
        for line in header.splitlines():
            if line.strip().startswith("# SYNOPSIS_HASH:"):
                return line.split(":", 1)[1].strip()
        return None
    except Exception:
        return None


def strip_all_annotations(file_path):
    """Completely remove all existing synopsis annotations from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        if not lines or not lines[0].startswith('#' + '=' * 79):
            return content  # No annotations to strip
        
        # Find the end of the synopsis header
        synopsis_end = 0
        found_end_marker = False
        for i, line in enumerate(lines):
            if line.startswith('#' + '=' * 79):
                found_end_marker = True
                synopsis_end = i + 1
            elif found_end_marker and line and not line.startswith('#'):
                # Found the start of actual code
                while synopsis_end < len(lines) and not lines[synopsis_end].strip():
                    synopsis_end += 1
                break
        
        if synopsis_end > 0:
            return '\n'.join(lines[synopsis_end:])
        return content
    except Exception:
        return content


def get_code_body(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.strip() == HEADER_BOUNDARY:
                return "".join(lines[i + 1 :])
        return "".join(lines)
    except Exception:
        return ""


def make_backup(file_path):
    base_dir = os.path.dirname(file_path)
    backup_dir = os.path.join(base_dir, "__backups__")
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, os.path.basename(file_path) + ".backup")
    shutil.copy2(file_path, backup_path)
    return backup_path


def is_up_to_date(file_path):
    stored_hash = extract_existing_hash(file_path)
    if not stored_hash:
        return False
    current_code = get_code_body(file_path)
    current_hash = compute_code_hash(current_code)
    return stored_hash == current_hash


def find_python_files(directory_path, recursive=False, skip_patterns=None):
    skip_patterns = skip_patterns or []
    files = []
    if recursive:
        for root, dirs, filenames in os.walk(directory_path):
            dirs[:] = [
                d
                for d in dirs
                if not d.startswith(".")
                and d not in ["__pycache__", "venv", "env", "node_modules"]
            ]
            for filename in filenames:
                if filename.endswith((".py", ".pyw")):
                    path = os.path.join(root, filename)
                    if not any(filename.startswith(p.rstrip("*")) for p in skip_patterns):
                        files.append(path)
    else:
        all_files = glob.glob(os.path.join(directory_path, "*.py")) + glob.glob(
            os.path.join(directory_path, "*.pyw")
        )
        files = [
            f
            for f in all_files
            if not any(os.path.basename(f).startswith(p.rstrip("*")) for p in skip_patterns)
        ]
    return sorted(files)


def format_duration(seconds):
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    else:
        m, s = divmod(int(seconds), 60)
        return f"{m}m {s}s"


def open_folder_in_explorer(path):
    """Open folder in file explorer (cross-platform)."""
    if not os.path.exists(path):
        messagebox.showerror("Error", "Folder does not exist.")
        return
    folder = path if os.path.isdir(path) else os.path.dirname(path)
    try:
        if sys.platform.startswith("darwin"):
            subprocess.Popen(["open", folder])
        elif os.name == "nt":
            os.startfile(folder)
        elif os.name == "posix":
            subprocess.Popen(["xdg-open", folder])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open folder: {e}")


# =============================================================================
# Core Processing
# =============================================================================
def process_single_file(file_path, dry_run=False, backup=True, force_rewrite=False):
    start = datetime.now()
    try:
        if not os.path.exists(file_path):
            return False, "File missing", "error", 0

        has_synopsis = extract_existing_hash(file_path)
        up_to_date = is_up_to_date(file_path)

        # Handle force rewrite - always process if enabled
        if force_rewrite and has_synopsis:
            if dry_run:
                return True, "Would force rewrite annotations", "updated", 0
            # Strip all existing annotations first
            stripped_content = strip_all_annotations(file_path)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(stripped_content)
        elif up_to_date and not force_rewrite:
            return True, "Skipped (up-to-date)", "unchanged", 0

        if dry_run and not force_rewrite:
            msg = "Would process new file" if not has_synopsis else "Would re-annotate (hash changed)"
            category = "new" if not has_synopsis else "updated"
            return True, msg, category, 0

        if backup:
            make_backup(file_path)

        # Create shared state for this analysis
        from analyzer_state import new_state
        state = new_state()
        
        analyzer = CodeAnalyzer(file_path, state, include_machine_block=True)
        analyzer.analyze()
        behavioral_analyzer = BehavioralAnalyzer(analyzer, state)
        renderer = SynopsisRenderer(analyzer, behavioral_analyzer, state)
        synopsis_header = renderer.generate_synopsis_header()

        # Inject INTENT (human-readable + machine-readable)
        synopsis_header = inject_intent(synopsis_header, analyzer, behavioral_analyzer)

        code_body = analyzer.code
        code_hash = compute_code_hash(code_body)
        header_lines = synopsis_header.strip().splitlines()

        # Ensure SYNOPSIS_HASH is up-to-date
        header_lines = [ln for ln in header_lines if not ln.strip().startswith("# SYNOPSIS_HASH:")]
        insert_at = 2 if len(header_lines) >= 2 else min(2, len(header_lines))
        header_lines.insert(insert_at, f"# SYNOPSIS_HASH: {code_hash}")
        if not any(ln.strip() == HEADER_BOUNDARY for ln in header_lines):
            header_lines.append(HEADER_BOUNDARY)
        synopsis_header = "\n".join(header_lines) + "\n"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(synopsis_header + code_body)

        category = "new" if not has_synopsis else "updated"
        msg = "Annotated new file" if not has_synopsis else "Re-annotated (out-of-date)"
        duration = (datetime.now() - start).total_seconds()
        return True, msg, category, duration

    except Exception as e:
        return False, f"Error: {e}", "errors", 0


def process_batch(files, dry_run=False, backup=True, skip_annotated=False, force_rewrite=False):
    results = {"updated": [], "new": [], "unchanged": [], "errors": []}
    start = datetime.now()

    for i, file_path in enumerate(files, 1):
        rel_path = os.path.relpath(file_path)
        print(f"[{i}/{len(files)}] {rel_path}")

        if skip_annotated and is_up_to_date(file_path) and not force_rewrite:
            print("  ⊘ Skipped (up-to-date)")
            results["unchanged"].append(rel_path)
            continue

        success, msg, category, dur = process_single_file(file_path, dry_run, backup, force_rewrite)
        print(f"  {'OK' if success else 'ERROR'} {msg} ({format_duration(dur)})")
        results[category].append(rel_path)

    total_time = (datetime.now() - start).total_seconds()
    print(f"Total time: {format_duration(total_time)}")
    return results


# =============================================================================
# GUI
# =============================================================================
class AnnotatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Code Synopsis Annotator")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.path_var = tk.StringVar()
        self.recursive_var = tk.BooleanVar(value=False)
        self.skip_annotated_var = tk.BooleanVar(value=True)
        self.force_rewrite_var = tk.BooleanVar(value=False)
        self.backup_var = tk.BooleanVar(value=True)
        self.dry_run_var = tk.BooleanVar(value=False)

        self._build_ui()
        self.log("Ready to annotate files.", "section")

    def _build_ui(self):
        tk.Label(self.root, text="Path (File or Folder):", fg="#ffffff", bg="#1e1e1e", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.pack(fill="x", padx=10)
        tk.Entry(frame, textvariable=self.path_var, width=80, font=("Consolas", 10), bg="#252526", fg="#ffffff", insertbackground="#ffffff").pack(side="left", fill="x", expand=True)
        tk.Button(frame, text="Browse File", command=self.select_file, width=12, bg="#0078D7", fg="white").pack(side="left", padx=5)
        tk.Button(frame, text="Browse Folder", command=self.select_folder, width=12, bg="#0078D7", fg="white").pack(side="left", padx=5)
        tk.Button(frame, text="Open Folder", command=self.open_folder, width=12, bg="#5A5A5A", fg="white").pack(side="left", padx=5)

        opts = tk.LabelFrame(self.root, text="Options", fg="#ffffff", bg="#2d2d2d", padx=10, pady=5)
        opts.pack(fill="x", padx=10, pady=10)
        for label, var in [
            ("Recursive", self.recursive_var),
            ("Skip Annotated", self.skip_annotated_var),
            ("Force Rewrite", self.force_rewrite_var),
            ("Create Backups", self.backup_var),
            ("Dry Run (Preview)", self.dry_run_var),
        ]:
            tk.Checkbutton(opts, text=label, variable=var, bg="#2d2d2d", fg="#ffffff", selectcolor="#3c3c3c").pack(side="left")

        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Run Annotator (Single File)", command=self.run_single, width=25, bg="#0078D7", fg="white").pack(side="left", padx=10)
        tk.Button(btn_frame, text="Run Batch (Folder)", command=self.run_batch, width=25, bg="#28A745", fg="white").pack(side="left", padx=10)
        tk.Button(btn_frame, text="Generate Project Markdown", command=self.generate_markdown, width=30, bg="#AA5500", fg="white").pack(side="left", padx=10)

        tk.Label(self.root, text="Log Output:", fg="#ffffff", bg="#1e1e1e", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(15, 0))
        self.log_box = scrolledtext.ScrolledText(self.root, wrap="word", width=110, height=24, font=("Consolas", 9), bg="#252526", fg="#ffffff", insertbackground="#ffffff")
        self.log_box.pack(padx=10, pady=(0, 10))
        self.log_box.config(state="disabled")

        self.log_box.tag_config("updated", foreground="#00cc66")
        self.log_box.tag_config("new", foreground="#3399ff")
        self.log_box.tag_config("unchanged", foreground="#aaaaaa")
        self.log_box.tag_config("error", foreground="#ff5555")
        self.log_box.tag_config("section", foreground="#ffffff", font=("Segoe UI", 10, "bold"))

    def open_folder(self):
        path = self.path_var.get().strip()
        if not path:
            messagebox.showerror("Error", "No path selected.")
            return
        open_folder_in_explorer(path)

    def log(self, msg, tag=None):
        self.log_box.config(state="normal")
        t = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert(tk.END, f"[{t}] {msg}\n", tag)
        self.log_box.see(tk.END)
        self.log_box.config(state="disabled")
        self.root.update_idletasks()

    def select_file(self):
        file = filedialog.askopenfilename(filetypes=[("Python files", "*.py;*.pyw")])
        if file:
            self.path_var.set(file)
            self.log(f"Selected file: {file}", "new")

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_var.set(folder)
            self.log(f"Selected folder: {folder}", "new")

    def run_in_thread(self, fn):
        threading.Thread(target=fn, daemon=True).start()

    def run_single(self):
        path = self.path_var.get().strip()
        if not path or not os.path.isfile(path):
            messagebox.showerror("Error", "Please select a valid Python file.")
            return
        self.run_in_thread(lambda: self._process_single(path))

    def run_batch(self):
        path = self.path_var.get().strip()
        if not path or not os.path.isdir(path):
            messagebox.showerror("Error", "Please select a valid folder.")
            return
        self.run_in_thread(lambda: self._process_folder(path))

    def generate_markdown(self):
        folder = self.path_var.get().strip()
        if not folder or not os.path.isdir(folder):
            messagebox.showerror("Error", "Please select a valid folder.")
            return

        def _run():
            self.log(f"Generating PROJECT_STRUCTURE.md for: {folder}", "section")
            try:
                output = build_project_summary(folder)
                self.log(f"✓ Project summary written to {output}", "updated")
            except Exception as e:
                self.log(f"✗ Error generating summary: {e}", "error")

        self.run_in_thread(_run)

    def _process_single(self, path):
        self.log(f"Processing: {path}", "section")
        success, msg, cat, dur = process_single_file(path, self.dry_run_var.get(), self.backup_var.get(), self.force_rewrite_var.get())
        self.log(f"{'OK' if success else 'ERROR'} {msg} ({format_duration(dur)})", cat)

    def _process_folder(self, folder):
        self.log(f"Scanning folder: {folder}", "section")
        files = find_python_files(folder, self.recursive_var.get())
        if not files:
            self.log("No Python files found.", "error")
            return
        self.log(f"Found {len(files)} file(s). Beginning batch...", "section")

        results = process_batch(files, self.dry_run_var.get(), self.backup_var.get(), self.skip_annotated_var.get(), self.force_rewrite_var.get())

        for group, color, title in [
            ("updated", "updated", "==== UPDATED SYNOPSES ===="),
            ("new", "new", "==== NEWLY ANNOTATED ===="),
            ("unchanged", "unchanged", "==== UNCHANGED FILES ===="),
            ("errors", "error", "==== ERRORS ===="),
        ]:
            if results[group]:
                self.log(title, "section")
                for f in results[group]:
                    self.log(f"  {f}", color)

        total = sum(len(v) for v in results.values())
        self.log(
            f"\nSummary: {len(results['updated'])} updated, {len(results['new'])} new, "
            f"{len(results['unchanged'])} unchanged, {len(results['errors'])} errors "
            f"({total} total files)\n",
            "section",
        )


# =============================================================================
# Entry Point
# =============================================================================
if __name__ == "__main__":
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument("path")
        parser.add_argument("-r", "--recursive", action="store_true")
        parser.add_argument("--skip-annotated", action="store_true")
        parser.add_argument("--no-backup", action="store_true")
        parser.add_argument("--dry-run", action="store_true")
        parser.add_argument("--markdown", action="store_true", help="Generate PROJECT_STRUCTURE.md after processing")
        args = parser.parse_args()

        if os.path.isfile(args.path):
            process_single_file(args.path, args.dry_run, not args.no_backup)
        elif os.path.isdir(args.path):
            files = find_python_files(args.path, args.recursive)
            process_batch(files, args.dry_run, not args.no_backup, args.skip_annotated)
            if args.markdown:
                build_project_summary(args.path)
        else:
            print(f"Invalid path: {args.path}")
    else:
        root = tk.Tk()
        app = AnnotatorGUI(root)
        root.mainloop()
