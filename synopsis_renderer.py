#===============================================================================
# CODE SYNOPSIS: synopsis_renderer.py
# SYNOPSIS_HASH: dc7ad39cd77c4de137007d4115783d15ff6fbd2438513a34b293892f8df2cdd5
# Generated: 2025-10-24 22:17:09
# INTENT: Generates functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 446
#   Functions: 18
#   Classes: 1
#   Global Variables: 28
#
# Key Dependencies:
#   - datetime
#   - typing
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 22:17:09
# FILE: synopsis_renderer.py
# IMPORTS_EXTERNAL: datetime, typing
# IMPORTS_LOCAL: 
# GLOBALS: args_str, behavior, critical, critical_vars, diagram, docstring, first_line, high_priority, inputs, intent, io_lines, joined, lines, outputs, parts, r, readers, reads, returns_str, rr, rv, rw, state_cats, summary, thr, w, writers, writes
# FUNCTIONS: __init__, _render_classes, _render_critical_globals, _render_data_flow_summary, _render_function_behavioral_summaries, _render_function_dependencies, _render_function_signatures, _render_high_priority_functions, _render_hotkeys, _render_integration_intent, _render_io_summary, _render_modularization_recommendations, _render_patch_additions, _render_shared_state, _render_state_machine_diagrams, _render_thread_interactions, _render_threading_analysis, generate_synopsis_header
# RETURNS: _render_classes, _render_critical_globals, _render_data_flow_summary, _render_function_behavioral_summaries, _render_function_dependencies, _render_function_signatures, _render_high_priority_functions, _render_hotkeys, _render_integration_intent, _render_io_summary, _render_modularization_recommendations, _render_patch_additions, _render_shared_state, _render_state_machine_diagrams, _render_thread_interactions, _render_threading_analysis, generate_synopsis_header
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: SynopsisRenderer
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: __init__,generate_synopsis_header,_render_state_machine_diagrams,_render_function_signatures,_render_threading_analysis,_render_thread_interactions,_render_classes,_render_critical_globals,_render_shared_state,_render_hotkeys,_render_high_priority_functions,_render_function_dependencies,_render_function_behavioral_summaries,_render_io_summary,_render_data_flow_summary,_render_modularization_recommendations,_render_patch_additions,_render_integration_intent
# STATE_VARS: 
# STATE_MACHINES_COUNT: 0
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Generates functionality for this module.
# FUNCTION_INTENTS: __init__=Handles the target entities., _render_classes=Produces or displays classes., _render_critical_globals=Produces or displays critical globals., _render_data_flow_summary=Produces or displays data flow summary., _render_function_behavioral_summaries=Produces or displays function behavioral summaries., _render_function_dependencies=Produces or displays function dependencies., _render_function_signatures=Produces or displays function signatures., _render_high_priority_functions=Produces or displays high priority functions., _render_hotkeys=Produces or displays hotkeys., _render_integration_intent=Produces or displays integration intent., _render_io_summary=Produces or displays io summary., _render_modularization_recommendations=Produces or displays modularization recommendations., _render_patch_additions=Produces or displays patch additions., _render_shared_state=Produces or displays shared state., _render_state_machine_diagrams=Produces or displays state machine diagrams., _render_thread_interactions=Produces or displays thread interactions., _render_threading_analysis=Produces or displays threading analysis., generate_synopsis_header=Handles synopsis header.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# SynopsisRenderer.__init__(self, analyzer, behavioral_analyzer) -> None
#   Initialize with references to analyzers.
#
# SynopsisRenderer._render_classes(self) -> List[str]
#   Render classes section.
#
# SynopsisRenderer._render_critical_globals(self) -> List[str]
#   Render critical global variables section.
#
# SynopsisRenderer._render_data_flow_summary(self) -> List[str]
#   Render semantic data flow summary.
#
# SynopsisRenderer._render_function_behavioral_summaries(self) -> List[str]
#   Render function behavioral summaries section.
#
# SynopsisRenderer._render_function_dependencies(self) -> List[str]
#   Render function dependencies section.
#
# SynopsisRenderer._render_function_signatures(self) -> List[str]
#   Render function signatures with type hints and docstrings.
#
# SynopsisRenderer._render_high_priority_functions(self) -> List[str]
#   Render high priority functions section.
#
# SynopsisRenderer._render_hotkeys(self) -> List[str]
#   Render hotkey bindings section.
#
# SynopsisRenderer._render_integration_intent(self) -> List[str]
#   Render integration intent and AI instructions.
#
# SynopsisRenderer._render_io_summary(self) -> List[str]
#   Render external I/O summary.
#
# SynopsisRenderer._render_modularization_recommendations(self) -> List[str]
#   Render modularization recommendations.
#
# SynopsisRenderer._render_patch_additions(self) -> List[str]
#   Render patch additions for refined behavioral analysis.
#
# SynopsisRenderer._render_shared_state(self) -> List[str]
#   Render shared state categories.
#
# SynopsisRenderer._render_state_machine_diagrams(self) -> List[str]
#   Render Mermaid state machine diagrams if available.
#
# SynopsisRenderer._render_thread_interactions(self) -> List[str]
#   Render thread interaction map.
#
# SynopsisRenderer._render_threading_analysis(self) -> List[str]
#   Render threading analysis section.
#
# SynopsisRenderer.generate_synopsis_header(self) -> str
#   Generate the complete synopsis header.
#
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   SynopsisRenderer (line 12):
#     - SynopsisRenderer.__init__()
#     - SynopsisRenderer.generate_synopsis_header()
#     - SynopsisRenderer._render_state_machine_diagrams()
#     - SynopsisRenderer._render_function_signatures()
#     - SynopsisRenderer._render_threading_analysis()
#     - SynopsisRenderer._render_thread_interactions()
#     - SynopsisRenderer._render_classes()
#     - SynopsisRenderer._render_critical_globals()
#     - SynopsisRenderer._render_shared_state()
#     - SynopsisRenderer._render_hotkeys()
#     - SynopsisRenderer._render_high_priority_functions()
#     - SynopsisRenderer._render_function_dependencies()
#     - SynopsisRenderer._render_function_behavioral_summaries()
#     - SynopsisRenderer._render_io_summary()
#     - SynopsisRenderer._render_data_flow_summary()
#     - SynopsisRenderer._render_modularization_recommendations()
#     - SynopsisRenderer._render_patch_additions()
#     - SynopsisRenderer._render_integration_intent()
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
# lines:
#   Modified by: generate_synopsis_header, _render_state_machine_diagrams, _render_function_signatures, _render_threading_analysis, _render_thread_interactions, _render_classes +10 more
#   Read by: generate_synopsis_header, _render_state_machine_diagrams, _render_function_signatures, _render_threading_analysis, _render_thread_interactions, _render_classes +10 more
#
# rv:
#   Modified by: _render_high_priority_functions, _render_data_flow_summary
#   Read by: _render_high_priority_functions, _render_data_flow_summary
#
# writes:
#   Modified by: _render_threading_analysis, _render_high_priority_functions
#   Read by: _render_threading_analysis, _render_high_priority_functions
#
# reads:
#   Modified by: _render_threading_analysis, _render_high_priority_functions
#   Read by: _render_threading_analysis, _render_high_priority_functions
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   Control State:
#     - state_cats
#   Position State:
#     - high_priority
#     - summary
#===============================================================================
#
# ⚠️ HIGH PRIORITY FUNCTIONS (Modify Multiple Globals):
#
# _render_function_signatures() - line 138  (Returns: Yes)
#   Modifies: args_str, docstring, first_line, lines, returns_str
#   Reads: args_str, docstring, first_line, lines, returns_str
#
# _render_threading_analysis() - line 163  (Returns: Yes)
#   Modifies: lines, reads, writes
#   Reads: lines, reads, writes
#
# _render_critical_globals() - line 211  (Returns: Yes)
#   Modifies: critical_vars, lines, r, readers, thr, w, writers
#   Reads: critical_vars, lines, r, readers, thr, w, writers
#
# _render_high_priority_functions() - line 271  (Returns: Yes)
#   Modifies: high_priority, lines, reads, rv, writes
#   Reads: high_priority, lines, reads, rv, writes
#
# _render_function_behavioral_summaries() - line 306  (Returns: Yes)
#   Modifies: behavior, inputs, intent, lines, outputs
#   Reads: behavior, inputs, intent, lines, outputs
#
# _render_data_flow_summary() - line 337  (Returns: Yes)
#   Modifies: lines, parts, rr, rv, rw, summary
#   Reads: lines, parts, rr, rv, rw, summary
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
# - generate_synopsis_header()
#
# - _render_state_machine_diagrams()
#
# - _render_function_signatures()
#
# - _render_threading_analysis()
#
# - _render_thread_interactions()
#
# - _render_classes()
#
# - _render_critical_globals()
#
# - _render_shared_state()
#
# - _render_hotkeys()
#
# - _render_high_priority_functions()
#
# - _render_function_dependencies()
#
# - _render_function_behavioral_summaries()
#
# - _render_io_summary()
#
# - _render_data_flow_summary()
#
# - _render_modularization_recommendations()
#
# - _render_patch_additions()
#
# - _render_integration_intent()
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
#   generate_synopsis_header() — reads lines; writes lines; calls datetime.now, join, len, lines.append, lines.extend, self._render_classes; returns value
#   _render_state_machine_diagrams() — reads diagram, lines; writes diagram, lines; calls hasattr, lines.append, self.analyzer.state_machine_detector.generate_mermaid_diagram; returns value
#   _render_function_signatures() — reads args_str, docstring, first_line, lines, returns_str; writes args_str, docstring, first_line, lines, returns_str; calls docstring.split, join, lines.append, self.analyzer.function_signatures.items, sig_data.get, sorted; returns value
#   _render_threading_analysis() — reads lines, reads, writes; writes lines, reads, writes; calls join, lines.append, lines.extend, sorted; returns value
#   _render_thread_interactions() — reads lines; writes lines; calls join, lines.append, self.analyzer.thread_interactions.items, sorted; returns value
#   _render_classes() — reads lines; writes lines; calls lines.append, self.analyzer.classes.items, sorted; returns value
#   _render_critical_globals() — reads critical_vars, lines, r, readers, thr, w; writes critical_vars, lines, r, readers, thr, w; calls critical_vars.append, critical_vars.sort, join, len, lines.append, self.analyzer.functions.items; returns value
#   _render_shared_state() — reads lines, state_cats; writes lines, state_cats; calls len, lines.append, self.behavioral_analyzer.categorize_shared_state; returns value
#   _render_hotkeys() — reads lines; writes lines; calls lines.append; returns value
#   _render_high_priority_functions() — reads high_priority, lines, reads, rv, writes; writes high_priority, lines, reads, rv, writes; calls func_data.get, join, lines.append, self.behavioral_analyzer.analyze_high_priority_functions, sorted; returns value
#   _render_function_dependencies() — reads critical, lines; writes critical, lines; calls len, lines.append, self.behavioral_analyzer.analyze_function_dependencies, sorted; returns value
#   _render_function_behavioral_summaries() — reads behavior, inputs, intent, lines, outputs; writes behavior, inputs, intent, lines, outputs; calls behavior.get, fdata.get, join, lines.append, self.analyzer.functions.items, sorted; returns value
#   _render_io_summary() — reads io_lines, lines; writes io_lines, lines; calls io_lines.append, join, lines.append, sorted; returns value
#   _render_data_flow_summary() — reads lines, parts, rr, rv, rw, summary; writes lines, parts, rr, rv, rw, summary; calls fdata.get, join, lines.append, list, parts.append, self.analyzer.functions.items; returns value
#   _render_modularization_recommendations() — reads lines; writes lines; calls len, lines.append, lines.extend; returns value
#   _render_patch_additions() — reads joined, lines; writes joined, lines; calls getattr, items, join, lines.append, lines.extend, self.analyzer.call_graph.items; returns value
#   _render_integration_intent() — pure/local computation; returns value
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
Synopsis Renderer - Generate formatted synopsis headers.

This module handles the generation of comprehensive synopsis headers
with detailed analysis results, formatting, and modularization recommendations.
"""

from datetime import datetime
from typing import Dict, List, Set, Tuple


class SynopsisRenderer:
    """
    Renders comprehensive synopsis headers from analysis results.
    
    This class handles the formatting and generation of detailed synopsis
    headers that include all analysis results in a readable format.
    """
    
    def __init__(self, analyzer, behavioral_analyzer, state=None):
        """Initialize with references to analyzers and optional shared state."""
        self.analyzer = analyzer
        self.behavioral_analyzer = behavioral_analyzer
        # Use shared state if provided, otherwise use analyzer's state
        if state is not None:
            self.state = state
        else:
            self.state = getattr(analyzer, 'state', None)
    
    def generate_synopsis_header(self) -> str:
        """Generate the complete synopsis header."""
        lines: List[str] = [
            "#" + "=" * 79,
            f"# CODE SYNOPSIS: {self.analyzer.filename}",
            f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "#" + "=" * 79,
            "#",
            "# OVERVIEW:",
            f"#   Total Lines: {len(self.analyzer.code.splitlines())}",
            f"#   Functions: {len(self.analyzer.functions)}",
            f"#   Classes: {len(self.analyzer.classes)}",
            f"#   Global Variables: {len(self.analyzer.globals_found)}",
            "#",
            "# Key Dependencies:",
        ]
        
        # Add external dependencies
        for imp in sorted(set(self.analyzer.imports_external))[:20]:
            if imp:
                lines.append(f"#   - {imp}")
        
        # Add local dependencies
        if self.analyzer.imports_local:
            lines.append("#   (Local modules):")
            for imp in sorted(self.analyzer.imports_local)[:20]:
                lines.append(f"#     * {imp}")
        lines.append("#")
        lines.append("#" + "=" * 79)

        # Add machine-readable block if requested
        if self.analyzer.include_machine_block:
            lines.extend(self.behavioral_analyzer.build_machine_block())
            lines.append("#" + "=" * 79)

        # NEW: Add function signatures
        lines.extend(self._render_function_signatures())

        # Add threading analysis
        lines.extend(self._render_threading_analysis())
        
        # Add thread interaction map
        lines.extend(self._render_thread_interactions())
        
        # Add classes
        lines.extend(self._render_classes())
        
        # Add critical globals
        lines.extend(self._render_critical_globals())
        
        # Add shared state categories
        lines.extend(self._render_shared_state())
        
        # Add hotkeys
        lines.extend(self._render_hotkeys())
        
        # Add high priority functions
        lines.extend(self._render_high_priority_functions())
        
        # Add function dependencies
        lines.extend(self._render_function_dependencies())
        
        # Add function behavioral summaries
        lines.extend(self._render_function_behavioral_summaries())
        
        # Add behavioral analysis
        lines.extend(self.behavioral_analyzer.generate_behavioral_summary())
        
        # Add state machine diagrams if available
        lines.extend(self._render_state_machine_diagrams())
        
        # Add external I/O summary
        lines.extend(self._render_io_summary())
        
        # Add data flow summary
        lines.extend(self._render_data_flow_summary())
        
        # Add modularization recommendations
        lines.extend(self._render_modularization_recommendations())
        
        # Add patch additions
        lines.extend(self._render_patch_additions())
        
        # Add integration intent and AI instructions
        lines.extend(self._render_integration_intent())
        
        return "\n".join(lines)

    # =========================================================================
    # NEW: STATE MACHINE DIAGRAM RENDERING
    # =========================================================================
    
    def _render_state_machine_diagrams(self) -> List[str]:
        """Render Mermaid state machine diagrams if available."""
        if not hasattr(self.analyzer, 'state_machine_detector') or not self.analyzer.state_machine_detector:
            return []
        
        try:
            diagram = self.analyzer.state_machine_detector.generate_mermaid_diagram()
            if diagram:
                lines = ["#", "# 🔄 STATE MACHINE DIAGRAMS:", "#"]
                lines.append(diagram)
                lines.append("#")
                return lines
        except Exception:
            pass
        
        return []
    
    # =========================================================================
    # NEW: FUNCTION SIGNATURE RENDERING
    # =========================================================================
    
    def _render_function_signatures(self) -> List[str]:
        """Render function signatures with type hints and docstrings."""
        if not self.analyzer.function_signatures:
            return []
        
        lines = ["#", "# 📝 FUNCTION SIGNATURES:", "#"]
        
        for func_name, sig_data in sorted(self.analyzer.function_signatures.items()):
            args_str = ", ".join(sig_data.get("args", []))
            returns_str = sig_data.get("returns", "None")
            docstring = sig_data.get("docstring", "")
            
            # Render signature
            lines.append(f"# {func_name}({args_str}) -> {returns_str}")
            
            # Add first line of docstring if available
            if docstring:
                first_line = docstring.split('\n')[0].strip()
                if first_line:
                    lines.append(f"#   {first_line}")
            lines.append("#")
        
        lines.append("#" + "=" * 79)
        return lines

    def _render_threading_analysis(self) -> List[str]:
        """Render threading analysis section."""
        if not self.analyzer.threads_found:
            return []
        
        lines = [
            "#",
            "# \u26A1\uFE0F THREADING MODEL (CRITICAL)",
            "#",
            "# Threads Found:",
        ]
        for t in self.analyzer.threads_found:
            lines.append(f"#   - {t}()")
            if t in self.analyzer.functions:
                reads = self.analyzer.functions[t]['reads'] & self.analyzer.globals_found
                writes = self.analyzer.functions[t]['writes'] & self.analyzer.globals_found
                if reads or writes:
                    lines.append(f"#     Accesses globals: {', '.join(sorted(reads | writes)[:12])}")
        lines.extend(["#", "#" + "=" * 79])
        return lines

    def _render_thread_interactions(self) -> List[str]:
        """Render thread interaction map."""
        if not self.analyzer.thread_interactions:
            return []
        
        lines = ["#", "# \u2699\uFE0F THREAD INTERACTION MAP:", "#"]
        for t, v in sorted(self.analyzer.thread_interactions.items()):
            lines.append(f"#   {t}():")
            lines.append(f"#     Reads: {', '.join(v['reads']) or 'None'}")
            lines.append(f"#     Writes: {', '.join(v['writes']) or 'None'}")
            lines.append("#")
        lines.append("#" + "=" * 79)
        return lines

    def _render_classes(self) -> List[str]:
        """Render classes section."""
        if not self.analyzer.classes:
            return []
        
        lines = ["#", "# \U0001F9F1 CLASSES FOUND:", "#"]  # 🧱
        for cname, meta in sorted(self.analyzer.classes.items(), key=lambda kv: kv[1]['line']):
            lines.append(f"#   {cname} (line {meta['line']}):")
            for m in meta["methods"]:
                lines.append(f"#     - {cname}.{m}()")
        lines.append("#" + "=" * 79)
        return lines

    def _render_critical_globals(self) -> List[str]:
        """Render critical global variables section."""
        if not self.analyzer.globals_found:
            return []
        
        lines = ["#", "# CRITICAL GLOBAL VARIABLES:", "#"]
        critical_vars = []
        for var in self.analyzer.globals_found:
            readers = [f for f, data in self.analyzer.functions.items() if var in data['reads']]
            writers = [f for f, data in self.analyzer.functions.items() if var in data['writes']]
            if len(readers) + len(writers) > 2:
                critical_vars.append((var, readers, writers))
        
        critical_vars.sort(key=lambda x: len(x[1]) + len(x[2]), reverse=True)
        for var, readers, writers in critical_vars[:20]:
            lines.append(f"# {var}:")
            if writers:
                w = ', '.join(writers[:6]) + (f" +{len(writers)-6} more" if len(writers) > 6 else '')
                lines.append(f"#   Modified by: {w}")
            if readers:
                r = ', '.join(readers[:6]) + (f" +{len(readers)-6} more" if len(readers) > 6 else '')
                lines.append(f"#   Read by: {r}")
            thr = [t for t in self.analyzer.threads_found if t in readers or t in writers]
            if thr:
                lines.append(f"#   \u26A0\uFE0F THREAD ACCESS: {', '.join(thr)}")
            lines.append("#")
        lines.append("#" + "=" * 79)
        return lines

    def _render_shared_state(self) -> List[str]:
        """Render shared state categories."""
        state_cats = self.behavioral_analyzer.categorize_shared_state()
        if not state_cats:
            return []
        
        lines = ["#", "# SHARED STATE CATEGORIES:", "#"]
        for name, vars_ in state_cats:
            lines.append(f"#   {name}:")
            for v in vars_[:20]:
                lines.append(f"#     - {v}")
            if len(vars_) > 20:
                lines.append(f"#     ... +{len(vars_) - 20} more")
        lines.append("#" + "=" * 79)
        return lines

    def _render_hotkeys(self) -> List[str]:
        """Render hotkey bindings section."""
        if not (self.analyzer.hotkeys_found or self.analyzer.hotkeys_tkbind or self.analyzer.hotkeys_command_bind):
            return []
        
        lines = ["#", "# HOTKEY / UI BINDINGS:", "#"]
        for hk, cb in self.analyzer.hotkeys_found:
            lines.append(f"#   keyboard: {hk} \u2192 {cb}()")
        for ev, cb in self.analyzer.hotkeys_tkbind:
            lines.append(f"#   tk.bind: {ev} \u2192 {cb}()")
        for kind, cb in self.analyzer.hotkeys_command_bind:
            lines.append(f"#   {kind}: \u2192 {cb}()")
        lines.append("#" + "=" * 79)
        return lines

    def _render_high_priority_functions(self) -> List[str]:
        """Render high priority functions section."""
        high_priority = self.behavioral_analyzer.analyze_high_priority_functions()
        if not high_priority:
            return []
        
        lines = ["#", "# \u26A0\uFE0F HIGH PRIORITY FUNCTIONS (Modify Multiple Globals):", "#"]
        for func_name, func_data, reads, writes in high_priority[:12]:
            rv = "Yes" if func_data.get('returns_value') else "No"
            lines.append(f"# {func_name}() - line {func_data['line']}  (Returns: {rv})")
            if writes:
                lines.append(f"#   Modifies: {', '.join(sorted(writes)[:8])}")
            if reads:
                lines.append(f"#   Reads: {', '.join(sorted(reads)[:8])}")
            lines.append("#")
        lines.append("#" + "=" * 79)
        return lines

    def _render_function_dependencies(self) -> List[str]:
        """Render function dependencies section."""
        critical = self.behavioral_analyzer.analyze_function_dependencies()
        if not critical:
            return []
        
        lines = ["#", "# \U0001F517 FUNCTION DEPENDENCIES (high fan-out):", "#"]  # 🔗
        for f, cs in critical[:10]:
            lines.append(f"# {f}() calls:")
            for c in sorted(cs)[:8]:
                lines.append(f"#   - {c}()")
            if len(cs) > 8:
                lines.append(f"#   ... and {len(cs)-8} more")
            lines.append("#")
        lines.append("#" + "=" * 79)
        return lines

    def _render_function_behavioral_summaries(self) -> List[str]:
        """Render function behavioral summaries section."""
        lines = ["#", "# 🧠 FUNCTION BEHAVIORAL SUMMARIES:", "#"]
        for fname, fdata in sorted(self.analyzer.functions.items()):
            behavior = fdata.get("behavior", {})
            if behavior:
                intent = behavior.get("intent", "")
                inputs = ", ".join(behavior.get("inputs", []))
                outputs = ", ".join(behavior.get("outputs", []))
                lines.append(f"# - **{fname}**({inputs}) → {outputs} - {intent}")
        lines.append("#")
        lines.append("#" + "=" * 79)
        return lines

    def _render_io_summary(self) -> List[str]:
        """Render external I/O summary."""
        io_lines = []
        if self.analyzer.io_reads:
            io_lines.append("Reads: " + ', '.join(sorted(self.analyzer.io_reads))[:400])
        if self.analyzer.io_writes:
            io_lines.append("Writes: " + ', '.join(sorted(self.analyzer.io_writes))[:400])
        
        if not io_lines:
            return []
        
        lines = ["#", "# \U0001F50C EXTERNAL I/O SUMMARY:", "#"]  # 🔌
        for l in io_lines:
            lines.append(f"#   {l}")
        lines.append("#" + "=" * 79)
        return lines

    def _render_data_flow_summary(self) -> List[str]:
        """Render semantic data flow summary."""
        lines = ["#", "# \U0001F4CA DATA FLOW SUMMARY:", "#"]  # 📊
        for fname, fdata in sorted(self.analyzer.functions.items(), key=lambda kv: kv[1]['line']):
            rw = fdata['writes'] & self.analyzer.globals_found
            rr = fdata['reads'] & self.analyzer.globals_found
            rv = "returns value" if fdata.get('returns_value') else "no return value"
            parts = []
            if rr:
                parts.append(f"reads {', '.join(sorted(list(rr))[:6])}")
            if rw:
                parts.append(f"writes {', '.join(sorted(list(rw))[:6])}")
            if fdata['calls']:
                parts.append(f"calls {', '.join(sorted(list(fdata['calls']))[:6])}")
            summary = "; ".join(parts) if parts else "pure/local computation"
            lines.append(f"#   {fname}() — {summary}; {rv}")
        lines.append("#" + "=" * 79)
        return lines

    def _render_modularization_recommendations(self) -> List[str]:
        """Render modularization recommendations."""
        lines = ["#", "# \U0001F527 MODULARIZATION RECOMMENDATIONS:", "#"]  # 🔧
        
        if self.analyzer.threads_found:
            lines.extend([
                "# \u26A0\uFE0F THREADING: Multiple threads access shared state.",
                "#    1. Keep thread functions with their state variables",
                "#    2. Add proper locking if splitting state",
                "#    3. Ensure thread-safe access to shared resources", "#"
            ])
        
        if self.analyzer.globals_found:
            lines.extend([
                "# \u26A0\uFE0F GLOBAL STATE: Significant global variables found.",
                "#    1. Create a State class to hold all globals",
                "#    2. Pass state object instead of using globals",
                "#    3. Use getter/setter methods for thread-safe access", "#"
            ])
        
        if len(self.analyzer.functions) > 10 or len(self.analyzer.globals_found) > 5 or self.analyzer.threads_found:
            lines.extend([
                "# When modularizing, consider splitting by:",
                "#   - Separate state management from business logic",
                "#   - Group related functions into modules",
                "#   - Separate UI code from core logic"
            ])
        
        lines.append("#" + "=" * 79)
        return lines

    def _render_patch_additions(self) -> List[str]:
        """Render patch additions for refined behavioral analysis."""
        lines = [
            "#===============================================================================",
            "# 📞 FUNCTION CALL HIERARCHY:"
        ]
        
        for func, callees in self.analyzer.call_graph.items():
            joined = ", ".join(sorted(callees))
            lines.append(f"#   {func}() → {joined}")
        if not self.analyzer.call_graph:
            lines.append("#   (No intra-module function calls detected.)")

        lines.extend([
            "#===============================================================================",
            "# 🔄 STATE MACHINE TRANSITIONS:"
        ])
        
        for var, states in getattr(self.analyzer, 'state_transitions', {}).items():
            joined = ", ".join(sorted(states))
            lines.append(f"#   {var}: transitions between {joined}")
        if not getattr(self.analyzer, 'state_transitions', {}):
            lines.append("#   (No *_state transitions detected.)")

        lines.extend([
            "#===============================================================================",
            "# ⌨️ HOTKEY BINDINGS:"
        ])
        
        if self.analyzer.hotkeys_pretty:
            for bind in self.analyzer.hotkeys_pretty:
                lines.append(f"#   {bind}")
        else:
            lines.append("#   (No keyboard hotkeys detected.)")
        
        lines.append("#" + "=" * 79)
        return lines

    def _render_integration_intent(self) -> List[str]:
        """Render integration intent and AI instructions."""
        return [
            "#",
            "# \U0001F9E9 MODULE INTEGRATION INTENT:",  # 🧩
            "#   Role: Single-file code analyzer that injects a synopsis header",
            "#   Used by: (future) system_synopsis_builder.py for folder-wide Markdown",
            "#   Inputs: Python source file path",
            "#   Outputs: Annotated source file (prepends this synopsis)",
            "#" + "=" * 79,
            "#",
            "# \U0001F4DD INSTRUCTIONS FOR AI:",
            "#   1. Preserve ALL global variable dependencies shown above",
            "#   2. Maintain thread safety for variables accessed by multiple threads",
            "#   3. Do NOT rename variables unless explicitly asked",
            "#   4. Ensure all function dependencies are preserved",
            "#   5. Keep UI-threaded calls (e.g., tk.after) on main thread or marshal via queue",
            "#   6. Ensure hotkeys and binds still invoke the same callbacks",
            "#" + "=" * 79,
            "",
            "",
        ]