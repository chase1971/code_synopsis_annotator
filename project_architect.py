#===============================================================================
# CODE SYNOPSIS: project_architect.py
# SYNOPSIS_HASH: fc193f686c66e89d67b02d9b6987b3b847dd72475c00c1e251076a17a3ad4bc6
# Generated: 2025-10-25 13:00:59
# INTENT: Generates, Extracts functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 588
#   Functions: 9
#   Classes: 0
#   Global Variables: 2
#
# Key Dependencies:
#   - collections
#   - datetime
#   - os
#   - re
#   (Local modules):
#     * state_tracker
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-25 13:00:59
# FILE: project_architect.py
# IMPORTS_EXTERNAL: collections, datetime, os, re
# IMPORTS_LOCAL: state_tracker
# GLOBALS: folder, path
# FUNCTIONS: build_project_summary, detect_exceptions, extract, extract_function_signatures_from_content, extract_list, generate_application_overview, generate_detailed_shared_state_table, generate_entry_points_section, parse_function_intents
# RETURNS: build_project_summary, detect_exceptions, extract, extract_function_signatures_from_content, extract_list, generate_application_overview, generate_detailed_shared_state_table, generate_entry_points_section, parse_function_intents
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: 
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: extract_list,detect_exceptions,build_project_summary
# STATE_VARS: path
# STATE_MACHINES_COUNT: 0
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Generates, Extracts functionality for this module.
# FUNCTION_INTENTS: build_project_summary=Scans annotated Python files; parses the MACHINE-READABLE DATA block; and., detect_exceptions=Detect simple try/except exception handlers., extract=Extract value for a given key from a MACHINE-READABLE DATA block., extract_function_signatures_from_content=Extract function signatures from the FUNCTION SIGNATURES section., extract_list=Extract comma-separated list for a key., generate_application_overview=Generate an Application Overview section based on module intents and key components., generate_detailed_shared_state_table=Generate a detailed Shared State Table using state_tracker functions., generate_entry_points_section=Generate an Entry Points section showing how the application starts and flows., parse_function_intents=Parse function intents from the FUNCTION_INTENTS string.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# build_project_summary(folder: str, output_path: str = None) -> str
#   Scans annotated Python files, parses the MACHINE-READABLE DATA block, and
#
# detect_exceptions(content: str) -> list[str]
#   Detect simple try/except exception handlers.
#
# extract(block: str, key: str) -> str
#   Extract value for a given key from a MACHINE-READABLE DATA block.
#
# extract_function_signatures_from_content(content: str) -> list[str]
#   Extract function signatures from the FUNCTION SIGNATURES section.
#
# extract_list(block: str, key: str) -> list[str]
#   Extract comma-separated list for a key.
#
# generate_application_overview(summaries: list[dict]) -> list[str]
#   Generate an Application Overview section based on module intents and key components.
#
# generate_detailed_shared_state_table(folder: str) -> list[str]
#   Generate a detailed Shared State Table using state_tracker functions.
#
# generate_entry_points_section(summaries: list[dict]) -> list[str]
#   Generate an Entry Points section showing how the application starts and flows.
#
# parse_function_intents(function_intents_str: str) -> dict[str, str]
#   Parse function intents from the FUNCTION_INTENTS string.
#
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   Config State:
#     - path
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - extract_list()
#
# - detect_exceptions()
#
# - build_project_summary()
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
#   extract() — calls m.group, re.search, strip; returns value
#   extract_list() — calls extract, v.strip, val.split; returns value
#   extract_function_signatures_from_content() — calls line.startswith, line.strip, match.group, re.search, section_content.split, signature.startswith; returns value
#   parse_function_intents() — calls func_name.strip, function_intents_str.split, intent.strip, part.split, part.strip; returns value
#   generate_application_overview() — calls core_analyzers.append, file_name.lower, intent.lower, join, key_features.add, len; returns value
#   generate_entry_points_section() — calls any, batch_files.append, batch_funcs.append, f.strip, file_name.endswith, file_name.lower; returns value
#   generate_detailed_shared_state_table() — calls build_state_table, globals_dict.items, join, lines.append, rel.get, sorted; returns value
#   detect_exceptions() — calls content.splitlines, enumerate, line.strip, result.append, split, startswith; returns value
#   build_project_summary() — reads path; writes path; calls append, data_flow.items, datetime.now, defaultdict, dependencies.items, extract; returns value
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
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
#!/usr/bin/env python3
"""
project_architect.py
Enhanced project-level architecture summarizer.

Scans annotated Python files (with MACHINE-READABLE DATA blocks)
and generates a robust PROJECT_STRUCTURE.md file that includes:
- Cross-module dependency graph
- Data flow map
- Thread/UI bindings
- File I/O summaries
- Exception handling summaries
- Schema metadata for LLM comprehension
"""

import os
import re
from datetime import datetime
from collections import defaultdict

# Import state tracker functions for detailed state table
try:
    from .state_tracker import build_state_table
except ImportError:
    from state_tracker import build_state_table


def extract(block: str, key: str) -> str:
    """Extract value for a given key from a MACHINE-READABLE DATA block."""
    pattern = rf"{key}:(.*)"
    m = re.search(pattern, block)
    if m:
        return m.group(1).strip()
    return ""


def extract_list(block: str, key: str) -> list[str]:
    """Extract comma-separated list for a key."""
    val = extract(block, key)
    if not val:
        return []
    return [v.strip() for v in val.split(",") if v.strip()]


def extract_function_signatures_from_content(content: str) -> list[str]:
    """Extract function signatures from the FUNCTION SIGNATURES section."""
    signatures = []
    
    # Look for the FUNCTION SIGNATURES section
    pattern = r"# 📝 FUNCTION SIGNATURES:.*?\n(.*?)#" + "=" * 79
    match = re.search(pattern, content, flags=re.DOTALL)
    
    if match:
        section_content = match.group(1)
        lines = section_content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Look for function signature lines (start with # function_name(...)
            if line.startswith('# ') and '(' in line and ')' in line:
                # Remove the leading '# ' and clean up
                signature = line[2:].strip()
                if signature and not signature.startswith('#'):
                    signatures.append(signature)
    
    return signatures


def parse_function_intents(function_intents_str: str) -> dict[str, str]:
    """Parse function intents from the FUNCTION_INTENTS string."""
    intents = {}
    
    if not function_intents_str:
        return intents
    
    # Split by comma and parse each function=intent pair
    parts = function_intents_str.split(',')
    for part in parts:
        part = part.strip()
        if '=' in part:
            func_name, intent = part.split('=', 1)
            func_name = func_name.strip()
            intent = intent.strip()
            intents[func_name] = intent
    
    return intents


def generate_application_overview(summaries: list[dict]) -> list[str]:
    """Generate an Application Overview section based on module intents and key components."""
    lines = []
    
    # Find main entry points and core modules
    main_modules = []
    core_analyzers = []
    ui_modules = []
    utility_modules = []
    
    for summary in summaries:
        file_name = summary.get('file_name', summary.get('file', 'unknown.py'))
        intent = summary.get('intent', '')
        classes = summary.get('classes', '')
        functions = summary.get('functions', '')
        
        # Categorize modules by their purpose
        if 'main' in file_name.lower() or 'entry' in file_name.lower():
            main_modules.append((file_name, intent))
        elif 'analyzer' in file_name.lower() or 'analysis' in file_name.lower():
            core_analyzers.append((file_name, intent))
        elif 'ui' in file_name.lower() or 'interface' in file_name.lower() or 'render' in file_name.lower():
            ui_modules.append((file_name, intent))
        elif 'util' in file_name.lower() or 'helper' in file_name.lower():
            utility_modules.append((file_name, intent))
    
    # Generate overview content
    lines.append("## 🚀 APPLICATION OVERVIEW")
    lines.append("")
    
    # Project purpose (dynamically inferred from module intents and architecture)
    lines.append("### Purpose")
    
    # Analyze module intents to determine the actual project purpose
    purpose_intents = []
    for summary in summaries:
        intent = summary.get('intent', '').strip()
        if intent and intent not in purpose_intents:
            purpose_intents.append(intent)
    
    # Generate intelligent purpose description based on project analysis
    has_d2l = any('d2l' in summary.get('file_name', summary.get('file', '')).lower() for summary in summaries)
    has_automation = any('automation' in summary.get('intent', '').lower() or 'browser' in summary.get('intent', '').lower() for summary in summaries)
    has_csv = any('csv' in summary.get('intent', '').lower() for summary in summaries)
    has_gui = any('gui' in summary.get('file_name', summary.get('file', '')).lower() for summary in summaries)
    
    if has_d2l:
        lines.append("This application is a **D2L Course Management Automation Tool** that automates assignment date updates in the Desire2Learn (D2L) learning management system using browser automation.")
        lines.append("")
        lines.append("**Key Capabilities:**")
        if has_automation:
            lines.append("- Browser automation for D2L course management")
        if has_csv:
            lines.append("- Bulk CSV-based assignment date updates")
        if has_gui:
            lines.append("- User-friendly GUI interface for course navigation")
        lines.append("- Persistent login session management")
        lines.append("- Automated assignment date modification")
    elif purpose_intents:
        lines.append(f"This application is designed to: {purpose_intents[0]}")
        if len(purpose_intents) > 1:
            lines.append("")
            lines.append("**Key Capabilities:**")
            for intent in purpose_intents[1:4]:  # Show up to 3 additional intents
                lines.append(f"- {intent}")
    else:
        # Fallback if no intents found
        lines.append("This application provides functionality across multiple modules with specialized components.")
    
    lines.append("")
    
    # Key Components
    lines.append("### Key Components")
    
    if main_modules:
        lines.append("- **Entry Points**: " + ", ".join([f"`{name}`" for name, _ in main_modules]))
    
    if core_analyzers:
        lines.append("- **Core Analysis**: " + ", ".join([f"`{name}`" for name, _ in core_analyzers]))
    
    if ui_modules:
        lines.append("- **User Interface**: " + ", ".join([f"`{name}`" for name, _ in ui_modules]))
    
    if utility_modules:
        lines.append("- **Utilities**: " + ", ".join([f"`{name}`" for name, _ in utility_modules]))
    
    lines.append("")
    
    # Architecture Summary
    total_files = len(summaries)
    total_functions = sum(len(summary.get('functions', '').split(',')) if summary.get('functions') else 0 for summary in summaries)
    total_classes = sum(len(summary.get('classes', '').split(',')) if summary.get('classes') else 0 for summary in summaries)
    
    lines.append("### Architecture Summary")
    lines.append(f"- **Total Modules**: {total_files}")
    lines.append(f"- **Total Functions**: {total_functions}")
    lines.append(f"- **Total Classes**: {total_classes}")
    lines.append("")
    
    # Key Features (inferred from function intents and module analysis)
    key_features = set()
    for summary in summaries:
        function_intents = summary.get('function_intents', '')
        if function_intents:
            parsed_intents = parse_function_intents(function_intents)
            for intent in parsed_intents.values():
                if 'analyze' in intent.lower():
                    key_features.add("Code Analysis")
                elif 'render' in intent.lower() or 'display' in intent.lower():
                    key_features.add("Documentation Generation")
                elif 'detect' in intent.lower():
                    key_features.add("Pattern Detection")
                elif 'extract' in intent.lower():
                    key_features.add("Data Extraction")
                elif 'generate' in intent.lower():
                    key_features.add("Content Generation")
    
    # Add project-specific features based on actual module analysis
    for summary in summaries:
        file_name = summary.get('file_name', summary.get('file', '')).lower()
        intent = summary.get('intent', '').lower()
        
        # D2L-specific features
        if 'd2l' in file_name or 'assignment' in intent or 'date' in intent:
            key_features.add("D2L Course Management")
            key_features.add("Assignment Date Automation")
        if 'browser' in intent or 'selenium' in intent or 'playwright' in intent:
            key_features.add("Browser Automation")
        if 'csv' in intent or 'process' in intent:
            key_features.add("CSV Data Processing")
        if 'gui' in file_name or 'interface' in intent:
            key_features.add("User Interface")
        if 'login' in intent or 'session' in intent:
            key_features.add("Session Management")
    
    if key_features:
        lines.append("### Key Features")
        for feature in sorted(key_features):
            lines.append(f"- {feature}")
        lines.append("")
    
    # Add Project-Specific Examples Section
    lines.append("### 📄 Project Structure & Examples")
    
    # Find a representative module to show as an example
    example_module = None
    for summary in summaries:
        if summary.get('functions') and len(summary.get('functions', '').split(',')) > 0:
            example_module = summary
            break
    
    if example_module:
        module_name = example_module.get('file_name', 'example.py')
        module_intent = example_module.get('intent', 'Provides core functionality')
        functions = example_module.get('functions', '').split(',')[:3]  # Show first 3 functions
        
        lines.append(f"**Example Module: `{module_name}`**")
        lines.append(f"*Purpose: {module_intent}*")
        lines.append("")
        
        if functions:
            lines.append("**Key Functions:**")
            for func in functions:
                if func.strip():
                    lines.append(f"- `{func.strip()}`")
            lines.append("")
        
        # Show actual function signatures if available
        if example_module.get('function_signatures'):
            lines.append("**Function Signatures:**")
            lines.append("```python")
            signatures = example_module.get('function_signatures', [])
            if isinstance(signatures, str):
                signatures = signatures.split('\n')[:5]
            elif isinstance(signatures, list):
                signatures = signatures[:5]
            for sig in signatures:
                if sig and str(sig).strip():
                    lines.append(str(sig).strip())
            lines.append("```")
            lines.append("")
    else:
        lines.append("This project contains multiple modules with specialized functionality.")
        lines.append("")
    
    # Show project statistics
    lines.append("**Project Statistics:**")
    lines.append(f"- **Total Modules**: {len(summaries)}")
    lines.append(f"- **Total Functions**: {sum(len(summary.get('functions', '').split(',')) if summary.get('functions') else 0 for summary in summaries)}")
    lines.append(f"- **Total Classes**: {sum(len(summary.get('classes', '').split(',')) if summary.get('classes') else 0 for summary in summaries)}")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    
    return lines


def generate_entry_points_section(summaries: list[dict]) -> list[str]:
    """Generate an Entry Points section showing how the application starts and flows."""
    lines = []
    
    # Find main entry points
    main_files = []
    batch_files = []
    utility_scripts = []
    
    for summary in summaries:
        file_name = summary.get('file_name', summary.get('file', 'unknown.py'))
        intent = summary.get('intent', '')
        functions = summary.get('functions', '')
        
        # Categorize by file name and function patterns
        if 'main' in file_name.lower():
            main_files.append((file_name, intent, functions))
        elif 'batch' in file_name.lower():
            batch_files.append((file_name, intent, functions))
        elif file_name.endswith('.py') and not any(x in file_name.lower() for x in ['test', '__init__', 'config']):
            # Check if it has main-like functions or is a standalone script
            if ('main' in functions.lower() or 'run' in functions.lower() or 'start' in functions.lower() or 
                'architect' in file_name.lower() or 'project' in file_name.lower()):
                utility_scripts.append((file_name, intent, functions))
    
    lines.append("## 🚪 ENTRY POINTS")
    lines.append("")
    
    # Primary Entry Points
    if main_files:
        lines.append("### Primary Entry Points")
        for file_name, intent, functions in main_files:
            lines.append(f"- **`{file_name}`**: {intent}")
            # Extract main functions
            main_funcs = []
            if functions:
                func_list = [f.strip() for f in functions.split(',') if f.strip()]
                for func in func_list:
                    if func in ['main', 'run', 'start', 'execute']:
                        main_funcs.append(func)
            if main_funcs:
                lines.append(f"  - Entry functions: `{', '.join(main_funcs)}()`")
        lines.append("")
    
    # Batch Processing Entry Points
    if batch_files:
        lines.append("### Batch Processing Entry Points")
        for file_name, intent, functions in batch_files:
            lines.append(f"- **`{file_name}`**: {intent}")
            # Extract batch functions
            batch_funcs = []
            if functions:
                func_list = [f.strip() for f in functions.split(',') if f.strip()]
                for func in func_list:
                    if 'batch' in func.lower() or 'process' in func.lower():
                        batch_funcs.append(func)
            if batch_funcs:
                lines.append(f"  - Batch functions: `{', '.join(batch_funcs)}()`")
        lines.append("")
    
    # Utility Scripts
    if utility_scripts:
        lines.append("### Utility Scripts")
        for file_name, intent, functions in utility_scripts:
            lines.append(f"- **`{file_name}`**: {intent}")
        lines.append("")
    
    # Execution Flow (dynamically generated based on project type)
    lines.append("### Execution Flow")
    
    # Detect project type and generate appropriate flow
    has_d2l = any('d2l' in summary.get('file_name', summary.get('file', '')).lower() for summary in summaries)
    has_gui = any('gui' in summary.get('file_name', summary.get('file', '')).lower() for summary in summaries)
    has_csv = any('csv' in summary.get('intent', '').lower() for summary in summaries)
    
    if has_d2l:
        lines.append("1. **Start**: Launch the D2L automation tool")
        if has_gui:
            lines.append("2. **GUI Launch**: Open the user interface for course selection")
        lines.append("3. **Login**: Authenticate with D2L learning management system")
        lines.append("4. **Course Selection**: Navigate to the target course")
        if has_csv:
            lines.append("5. **CSV Processing**: Load and parse assignment data from CSV file")
            lines.append("6. **Date Updates**: Automate assignment date modifications")
        lines.append("7. **Completion**: Verify updates and close browser session")
    else:
        # Generic flow for non-D2L projects
        lines.append("1. **Start**: Run the main application")
        lines.append("2. **Initialization**: Load configuration and dependencies")
        lines.append("3. **Processing**: Execute core functionality")
        lines.append("4. **Output**: Generate results or complete tasks")
    lines.append("")
    
    # Command Line Usage (dynamically generated based on project)
    lines.append("### Command Line Usage")
    lines.append("```bash")
    
    if has_d2l:
        if has_gui:
            lines.append("# Launch GUI interface")
            lines.append("python D2L_Gui.py")
            lines.append("")
        lines.append("# Run D2L date processing")
        lines.append("python d2l_date_processing_new.py")
        lines.append("")
        lines.append("# Run Playwright automation")
        lines.append("python d2l_playwright_processor.py")
    else:
        # Generic commands for non-D2L projects
        main_files = [f for f in summaries if 'main' in f.get('file_name', f.get('file', '')).lower()]
        if main_files:
            main_file = main_files[0].get('file_name', main_files[0].get('file', 'main.py'))
            lines.append(f"# Run main application")
            lines.append(f"python {main_file}")
        else:
            lines.append("# Run the application")
            lines.append("python <main_script.py>")
    
    lines.append("```")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    
    return lines


def generate_detailed_shared_state_table(folder: str) -> list[str]:
    """Generate a detailed Shared State Table using state_tracker functions."""
    lines = []
    
    try:
        # Use the state_tracker to build the detailed state table
        state_map = build_state_table(folder)
        
        if not state_map:
            return lines
        
        lines.append("## 🔄 SHARED STATE TABLE")
        lines.append("")
        lines.append("| File | Variable | Modified By | Read By |")
        lines.append("|------|----------|-------------|---------|")
        
        # Generate the detailed table with Modified By | Read By
        # Only show variables that have actual tracking data
        for file_name, globals_dict in sorted(state_map.items()):
            for var, rel in sorted(globals_dict.items()):
                mods = ", ".join(rel.get("modified_by", [])) or "-"
                reads = ", ".join(rel.get("read_by", [])) or "-"
                
                # Filter out variables with no tracking data
                if mods != "-" or reads != "-":
                    lines.append(f"| {file_name} | `{var}` | {mods} | {reads} |")
        
        lines.append("")
        lines.append("---")
        lines.append("")
        
    except Exception as e:
        # Fallback if state_tracker fails
        lines.append("## 🔄 SHARED STATE TABLE")
        lines.append("")
        lines.append("_State tracking unavailable._")
        lines.append("")
    
    return lines


def detect_exceptions(content: str) -> list[str]:
    """Detect simple try/except exception handlers."""
    lines = content.splitlines()
    result = []
    for i, line in enumerate(lines):
        if line.strip().startswith("except "):
            result.append(line.strip().split(":")[0])
    return result


def build_project_summary(folder: str, output_path: str = None) -> str:
    """
    Scans annotated Python files, parses the MACHINE-READABLE DATA block, and
    compiles a system-level markdown including per-module INTENT lines.

    Adds/updates sections:
      - Module Dependency Graph (mermaid)
      - Cross-Module Data Flow Map (table)
      - Module Summaries (now includes 'Intent' if present)
      - Data Schema Summary
    """
    from collections import defaultdict
    import os
    
    # If no output path specified, write to the folder being analyzed
    if output_path is None:
        output_path = os.path.join(folder, "PROJECT_STRUCTURE.md")

    summaries = []
    dependencies = defaultdict(list)
    data_flow = defaultdict(list)

    files = []
    for root, _dirs, fnames in os.walk(folder):
        for name in fnames:
            if name.endswith((".py", ".pyw")):
                files.append(os.path.join(root, name))
    files.sort()

    for path in files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            continue

        # Pull out the MACHINE-READABLE block contents if present
        m = re.search(r"BEGIN MACHINE-READABLE DATA.*?\n(.*?)# END MACHINE-READABLE DATA",
                      content, flags=re.DOTALL)
        block = m.group(1) if m else ""

        file_name = os.path.basename(path)
        imports_local = extract(block, "IMPORTS_LOCAL")
        imports_external = extract(block, "IMPORTS_EXTERNAL")
        classes = extract(block, "CLASSES")
        functions = extract(block, "FUNCTIONS")
        globals_ = extract(block, "GLOBALS")
        threads = extract(block, "THREAD_TARGETS")
        tk_binds = extract(block, "TK_BINDS")
        hotkeys = extract(block, "HOTKEYS")
        exceptions = extract(block, "EXCEPTIONS")
        io_reads = extract(block, "IO_READS")
        io_writes = extract(block, "IO_WRITES")
        intent_line = extract(block, "INTENT")  # <=== NEW
        function_intents = extract(block, "FUNCTION_INTENTS")  # <=== NEW
        
        # Extract function signatures from the FUNCTION SIGNATURES section
        function_signatures = extract_function_signatures_from_content(content)

        # Track dependencies for the mermaid graph
        if imports_local:
            for mname in [s.strip() for s in imports_local.split(",") if s.strip()]:
                dependencies[file_name].append(mname)

        # Minimal cross-flow capture
        if functions:
            data_flow[file_name].append("Functions: " + functions[:200] + ("..." if len(functions) > 200 else ""))

        summaries.append({
            "file": file_name,
            "classes": classes,
            "functions": functions,
            "globals": globals_,
            "imports_local": imports_local,
            "imports_external": imports_external,
            "io_reads": io_reads,
            "io_writes": io_writes,
            "threads": threads,
            "ui_binds": hotkeys,
            "hotkeys": hotkeys,
            "exceptions": exceptions,
            "intent": intent_line,  # <=== NEW
            "function_signatures": function_signatures,  # <=== NEW
            "function_intents": function_intents,  # <=== NEW
        })

    # Build markdown
    md = []
    md.append("# 🧩 PROJECT STRUCTURE SUMMARY")
    md.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Add Application Overview section
    md.extend(generate_application_overview(summaries))
    
    # Add Entry Points section
    md.extend(generate_entry_points_section(summaries))
    
    # Add Detailed Shared State Table section
    md.extend(generate_detailed_shared_state_table(folder))
    
    md.append("This document provides a full architectural map of the project.\n")

    # Mermaid dependency graph
    md.append("## 🧱 Module Dependency Graph\n")
    md.append("```mermaid")
    md.append("graph TD")
    for src, dsts in sorted(dependencies.items()):
        src_node = src
        for dst in sorted(set(dsts)):
            md.append(f"    {src_node} --> {dst}")
    md.append("```")
    md.append("")

    # Cross-Module Data Flow Map
    md.append("## 🔄 Cross-Module Data Flow Map\n")
    md.append("| Source Module | Target or Description |")
    md.append("|----------------|----------------------|")
    for mod, items in sorted(data_flow.items()):
        for desc in items:
            md.append(f"| {mod} | {desc} |")
    md.append("")

    # Module Summaries (NOW includes 'Intent' and 'Function Signatures')
    md.append("## 📦 Module Summaries\n")
    for s in summaries:
        md.append(f"### `{s['file']}`\n")
        if s.get("intent"):
            md.append(f"**Intent:** {s['intent']}\n")
        md.append("**Classes:** " + (s['classes'] or "_None_"))
        md.append("\n**Functions:** " + (s['functions'] or "_None_"))
        md.append("\n**Globals:** " + (s['globals'] or "_None_"))
        md.append("\n\n**Local Imports:** " + (s['imports_local'] or "_None_"))
        md.append("\n**External Imports:** " + (s['imports_external'] or "_None_"))
        
        # Add Function Signatures section
        if s.get("function_signatures"):
            md.append("\n\n#### 📝 Function Signatures")
            for sig in s['function_signatures']:
                md.append(f"\n- `{sig}`")
        else:
            md.append("\n\n#### 📝 Function Signatures")
            md.append("\n_No function signatures available._")
        
        # Add Function Intents section
        if s.get("function_intents"):
            parsed_intents = parse_function_intents(s['function_intents'])
            if parsed_intents:
                md.append("\n\n#### 🎯 Function Intents")
                for func_name, intent in sorted(parsed_intents.items()):
                    md.append(f"\n- **{func_name}()**: {intent}")
            else:
                md.append("\n\n#### 🎯 Function Intents")
                md.append("\n_No function intents available._")
        else:
            md.append("\n\n#### 🎯 Function Intents")
            md.append("\n_No function intents available._")
        
        md.append("\n\n#### File I/O Summary")
        md.append("\n- Reads: " + (s['io_reads'] or "_None_"))
        md.append("\n- Writes: " + (s['io_writes'] or "_None_"))
        md.append("\n\n#### Threading & UI Bindings")
        md.append("\n- Threads: " + (s['threads'] or "_None_"))
        md.append("\n- UI Binds: " + (s['ui_binds'] or "_None_"))
        md.append("\n\n#### Exception Paths")
        if s['exceptions']:
            md.append("\n" + s['exceptions'])
        else:
            md.append("\n_No exception handlers detected._")
        md.append("\n\n---\n")

    # Data schema summary (unchanged)
    md.append("## 🧠 DATA SCHEMA SUMMARY\n")
    md.append("```json")
    md.append('{\n  "ModuleSummary": {\n    "file": "str",\n    "classes": ["list[str]"],\n    "functions": ["list[str]"],\n    "globals": ["list[str]"],\n    "imports_local": ["list[str]"],\n    "imports_external": ["list[str]"],\n    "io_reads": ["list[str]"],\n    "io_writes": ["list[str]"],\n    "threads": ["list[str]"],\n    "ui_binds": ["list[str]"],\n    "exceptions": ["list[str]"],\n    "intent": "str",\n    "function_signatures": ["list[str]"],\n    "function_intents": "str"\n  }\n}')
    md.append("```")

    output = "\n".join(md) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    return output_path


if __name__ == "__main__":
    folder = os.getcwd()
    print("Generating enhanced PROJECT_STRUCTURE.md ...")
    path = build_project_summary(folder)
    print(f"Project summary generated: {path}")
