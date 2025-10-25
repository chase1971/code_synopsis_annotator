#===============================================================================
# CODE SYNOPSIS: analyzer_state.py
# SYNOPSIS_HASH: 418a74841d19b7536e76c5a289c79a69e15dc286954980d4668d1b6300446a8e
# Generated: 2025-10-25 11:18:38
# INTENT: Loads and manages configuration settings.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 159
#   Functions: 7
#   Classes: 1
#   Global Variables: 21
#
# Key Dependencies:
#   - __future__
#   - dataclasses
#   - datetime
#   - json
#   - threading
#   - typing
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-25 11:18:38
# FILE: analyzer_state.py
# IMPORTS_EXTERNAL: __future__, dataclasses, datetime, json, threading, typing
# IMPORTS_LOCAL: 
# GLOBALS: _lock, classes, config_state, exceptions, functions, generated_at, globals, hotkeys, imports_external, imports_local, io_reads, io_writes, notes, position_state, project_path, state, state_cats, threads, timing_state, ui_binds, version
# FUNCTIONS: clear, merge, new_state, summary, to_dict, to_json, update
# RETURNS: new_state, summary, to_dict
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: AnalyzerState
# IO_READS: 
# IO_WRITES: json.dump(...)
# CALLGRAPH_ROOTS: new_state,merge,clear,to_dict,to_json,summary
# STATE_VARS: state
# STATE_MACHINES_COUNT: 1
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Loads and manages configuration settings.
# FUNCTION_INTENTS: clear=Handles the target entities., merge=Handles the target entities., new_state=Handles state., summary=Handles the target entities., to_dict=Handles dict., to_json=Handles json., update=Handles the target entities.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# AnalyzerState.clear(self) -> None
#   Reset all mutable fields.
#
# AnalyzerState.merge(self, other: AnalyzerState) -> None
#   Merge another AnalyzerState into this one.
#
# AnalyzerState.summary(self) -> str
#   Return a brief string summary for debugging or logging.
#
# AnalyzerState.to_dict(self) -> Dict[str, Any]
#   Return a plain dictionary suitable for JSON serialization.
#
# AnalyzerState.to_json(self, path: str) -> None
#   Serialize the state to a JSON file.
#
# AnalyzerState.update(self, key: str, value: Any) -> None
#   Thread-safe generic update helper.
#
# new_state(project_path: Optional[str] = None) -> AnalyzerState
#   Factory to create a fresh state with an optional project path.
#
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   AnalyzerState (line 31):
#     - AnalyzerState.update()
#     - AnalyzerState.merge()
#     - AnalyzerState.clear()
#     - AnalyzerState.to_dict()
#     - AnalyzerState.to_json()
#     - AnalyzerState.summary()
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   UI State:
#     - ui_binds
#   Control State:
#     - config_state
#     - position_state
#     - state
#     - state_cats
#     - timing_state
#   Position State:
#     - exceptions
#     - hotkeys
#     - imports_external
#     - position_state
#   Config State:
#     - config_state
#     - project_path
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - new_state()
#
# - merge()
#
# - clear()
#
# - to_dict()
#
# - to_json()
#
# - summary()
#
#===============================================================================
#
# 🔄 STATE MACHINES DETECTED:
#
#   📍 state (State Variable):
#      States: (values unknown)
#
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
# 🔌 EXTERNAL I/O SUMMARY:
#
#   Writes: json.dump(...)
#===============================================================================
#
# 📊 DATA FLOW SUMMARY:
#
#   update() — calls AttributeError, TypeError, current.add, current.append, current.extend, current.update; no return value
#   merge() — calls extend, getattr, isinstance, k.startswith, other.__dict__.items, setattr; no return value
#   clear() — calls isinstance, self.__dict__.items, v.clear; no return value
#   to_dict() — calls datetime.datetime.now, isinstance, isoformat, k.startswith, list, self.__dict__.items; returns value
#   to_json() — calls json.dump, open, self.to_dict; no return value
#   summary() — calls len; returns value
#   new_state() — calls AnalyzerState; returns value
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
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
#!/usr/bin/env python3
# =============================================================================
# ANALYZER STATE REGISTRY
# =============================================================================
# Purpose:
#   Provides a unified, thread-safe data container for all analysis modules.
#   Used by core_analyzer, behavioral_analysis, synopsis_renderer, etc.
#
#   Every analyzer instance should receive a reference to the same
#   AnalyzerState object, allowing synchronized accumulation of data
#   across modules and consistent project-wide reasoning.
#
# =============================================================================

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Set, Any, Optional
import threading
import json
import datetime


# =============================================================================
# THREAD-SAFE STATE CONTAINER
# =============================================================================

@dataclass
class AnalyzerState:
    """Shared registry of all discovered data across analyzers."""

    # --- Core Analysis Data ---
    functions: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    classes: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    globals: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    threads: Set[str] = field(default_factory=set)
    ui_binds: Set[str] = field(default_factory=set)
    hotkeys: Set[str] = field(default_factory=set)
    io_reads: Set[str] = field(default_factory=set)
    io_writes: Set[str] = field(default_factory=set)
    imports_local: Set[str] = field(default_factory=set)
    imports_external: Set[str] = field(default_factory=set)
    exceptions: Set[str] = field(default_factory=set)
    state_cats: Dict[str, List[str]] = field(default_factory=dict)
    timing_state: Dict[str, Any] = field(default_factory=dict)
    config_state: Dict[str, Any] = field(default_factory=dict)
    position_state: Dict[str, Any] = field(default_factory=dict)

    # --- Metadata ---
    project_path: Optional[str] = None
    generated_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    version: str = "1.0.0"
    notes: List[str] = field(default_factory=list)

    # Internal lock for thread safety
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False, compare=False)

    # =========================================================================
    # CORE METHODS
    # =========================================================================

    def update(self, key: str, value: Any):
        """Thread-safe generic update helper."""
        with self._lock:
            if hasattr(self, key):
                current = getattr(self, key)
                if isinstance(current, set):
                    if isinstance(value, (list, set)):
                        current.update(value)
                    else:
                        current.add(value)
                elif isinstance(current, dict):
                    if isinstance(value, dict):
                        current.update(value)
                    else:
                        raise TypeError(f"Expected dict for update of {key}")
                elif isinstance(current, list):
                    if isinstance(value, list):
                        current.extend(value)
                    else:
                        current.append(value)
                else:
                    setattr(self, key, value)
            else:
                raise AttributeError(f"No such field '{key}' in AnalyzerState")

    def merge(self, other: AnalyzerState):
        """Merge another AnalyzerState into this one."""
        with self._lock:
            for k, v in other.__dict__.items():
                if k.startswith("_"):
                    continue
                if isinstance(v, set):
                    getattr(self, k).update(v)
                elif isinstance(v, list):
                    getattr(self, k).extend(v)
                elif isinstance(v, dict):
                    getattr(self, k).update(v)
                elif v is not None:
                    setattr(self, k, v)

    def clear(self):
        """Reset all mutable fields."""
        with self._lock:
            for k, v in self.__dict__.items():
                if isinstance(v, (dict, list, set)):
                    v.clear()

    def to_dict(self) -> Dict[str, Any]:
        """Return a plain dictionary suitable for JSON serialization."""
        d = {}
        for k, v in self.__dict__.items():
            if k.startswith("_"):
                continue  # Skip private fields like _lock
            if isinstance(v, set):
                d[k] = list(v)
            elif isinstance(v, dict):
                d[k] = v.copy()
            elif isinstance(v, list):
                d[k] = v.copy()
            else:
                d[k] = v
        d["generated_at"] = datetime.datetime.now().isoformat()
        return d

    def to_json(self, path: str):
        """Serialize the state to a JSON file."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)

    def summary(self) -> str:
        """Return a brief string summary for debugging or logging."""
        return (
            f"AnalyzerState: {len(self.functions)} funcs, {len(self.classes)} classes, "
            f"{len(self.globals)} globals, {len(self.threads)} threads, "
            f"{len(self.ui_binds)} ui binds, {len(self.exceptions)} exceptions"
        )


# =============================================================================
# HELPER UTILITIES
# =============================================================================

def new_state(project_path: Optional[str] = None) -> AnalyzerState:
    """Factory to create a fresh state with an optional project path."""
    return AnalyzerState(project_path=project_path)


# =============================================================================
# USAGE EXAMPLE
# =============================================================================
if __name__ == "__main__":
    state = AnalyzerState(project_path="C:/Projects/Annotator")
    state.update("globals", {"paused": {"module": "dwell.pyw", "type": "bool"}})
    state.update("threads", {"dwell_click", "overlay_loop"})
    print(state.summary())
    state.to_json("analysis_state.json")
