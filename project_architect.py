#===============================================================================
# CODE SYNOPSIS: project_architect.py
# SYNOPSIS_HASH: b74f4c6e03c7a20782ee46d6ab8ad1ad9ec7f91d8da1f97893869f4596224377
# Generated: 2025-10-24 23:31:32
# INTENT: Extracts, Detects or identifies patterns in functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 197
#   Functions: 4
#   Classes: 0
#   Global Variables: 2
#
# Key Dependencies:
#   - collections
#   - datetime
#   - os
#   - re
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-24 23:31:32
# FILE: project_architect.py
# IMPORTS_EXTERNAL: collections, datetime, os, re
# IMPORTS_LOCAL: 
# GLOBALS: folder, path
# FUNCTIONS: build_project_summary, detect_exceptions, extract, extract_list
# RETURNS: build_project_summary, detect_exceptions, extract, extract_list
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
# INTENT: Extracts, Detects or identifies patterns in functionality for this module.
# FUNCTION_INTENTS: build_project_summary=Constructs or generates project summary., detect_exceptions=Identifies exceptions., extract=Retrieves the target entities., extract_list=Retrieves list.
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
# extract_list(block: str, key: str) -> list[str]
#   Extract comma-separated list for a key.
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
        file_name = summary['file']
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
    
    # Project purpose (inferred from main modules and overall architecture)
    lines.append("### Purpose")
    lines.append("This application is a **Code Synopsis Annotator** that automatically analyzes Python codebases and generates comprehensive documentation headers. It provides:")
    lines.append("- **Automated Code Analysis**: Extracts function signatures, dependencies, and behavioral patterns")
    lines.append("- **Intelligent Documentation**: Generates detailed synopsis headers with function intents and signatures")
    lines.append("- **Project Architecture Mapping**: Creates high-level project structure documentation")
    lines.append("- **LLM-Optimized Output**: Formats information for optimal AI/LLM comprehension")
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
    
    # Add additional features based on module names and architecture
    key_features.add("Function Signature Extraction")
    key_features.add("State Machine Detection")
    key_features.add("Threading Analysis")
    key_features.add("Dependency Mapping")
    key_features.add("Behavioral Analysis")
    
    if key_features:
        lines.append("### Key Features")
        for feature in sorted(key_features):
            lines.append(f"- {feature}")
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
        file_name = summary['file']
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
    
    # Execution Flow
    lines.append("### Execution Flow")
    lines.append("1. **Start**: Run `python main.py` or `python main.py <filepath>`")
    lines.append("2. **Analysis**: Core analyzer processes the Python file")
    lines.append("3. **Behavioral Analysis**: Extracts patterns and intents")
    lines.append("4. **Rendering**: Generates synopsis headers")
    lines.append("5. **Output**: Creates annotated file with documentation")
    lines.append("")
    
    # Command Line Usage
    lines.append("### Command Line Usage")
    lines.append("```bash")
    lines.append("# Interactive mode (file dialog)")
    lines.append("python main.py")
    lines.append("")
    lines.append("# Direct file analysis")
    lines.append("python main.py path/to/file.py")
    lines.append("")
    lines.append("# Batch processing")
    lines.append("python batch_annotate_modular.py")
    lines.append("")
    lines.append("# Generate project structure")
    lines.append("python project_architect.py")
    lines.append("```")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    
    return lines


def generate_shared_state_table(summaries: list[dict]) -> list[str]:
    """Generate a Shared State Table showing state variables and their relationships."""
    lines = []
    
    # Collect shared state information from all modules
    shared_state_vars = {}
    state_categories = {}
    
    for summary in summaries:
        file_name = summary['file']
        globals_ = summary.get('globals', '')
        intent = summary.get('intent', '')
        
        # Extract global variables
        if globals_ and globals_ != '_None_':
            global_list = [g.strip() for g in globals_.split(',') if g.strip()]
            for var in global_list:
                if var not in shared_state_vars:
                    shared_state_vars[var] = {
                        'modules': [],
                        'intents': [],
                        'category': 'Unknown'
                    }
                shared_state_vars[var]['modules'].append(file_name)
                shared_state_vars[var]['intents'].append(intent)
                
                # Categorize state variables
                var_lower = var.lower()
                if 'state' in var_lower or 'mode' in var_lower:
                    shared_state_vars[var]['category'] = 'State Management'
                elif 'config' in var_lower or 'setting' in var_lower:
                    shared_state_vars[var]['category'] = 'Configuration'
                elif 'cache' in var_lower or 'buffer' in var_lower:
                    shared_state_vars[var]['category'] = 'Caching'
                elif 'lock' in var_lower or 'mutex' in var_lower:
                    shared_state_vars[var]['category'] = 'Synchronization'
                elif 'path' in var_lower or 'dir' in var_lower:
                    shared_state_vars[var]['category'] = 'File System'
                else:
                    shared_state_vars[var]['category'] = 'Data'
    
    if not shared_state_vars:
        return lines
    
    lines.append("## 🔄 SHARED STATE TABLE")
    lines.append("")
    
    # Group by category
    categories = {}
    for var, info in shared_state_vars.items():
        category = info['category']
        if category not in categories:
            categories[category] = []
        categories[category].append((var, info))
    
    # Generate table for each category
    for category, vars_list in sorted(categories.items()):
        lines.append(f"### {category}")
        lines.append("")
        lines.append("| Variable | Modules | Purpose |")
        lines.append("|----------|---------|---------|")
        
        for var, info in sorted(vars_list):
            modules_str = ", ".join(info['modules'][:3])  # Limit to first 3 modules
            if len(info['modules']) > 3:
                modules_str += f" (+{len(info['modules'])-3} more)"
            
            # Get purpose from intents
            purpose = "Unknown"
            if info['intents']:
                # Use the first non-empty intent
                for intent in info['intents']:
                    if intent and intent.strip():
                        purpose = intent
                        break
            
            lines.append(f"| `{var}` | {modules_str} | {purpose} |")
        
        lines.append("")
    
    # Add state relationships
    lines.append("### State Relationships")
    lines.append("")
    
    # Find modules that share state
    state_connections = {}
    for var, info in shared_state_vars.items():
        if len(info['modules']) > 1:
            modules = sorted(info['modules'])
            for i in range(len(modules)):
                for j in range(i+1, len(modules)):
                    key = tuple(sorted([modules[i], modules[j]]))
                    if key not in state_connections:
                        state_connections[key] = []
                    state_connections[key].append(var)
    
    if state_connections:
        lines.append("**Modules with Shared State:**")
        for (mod1, mod2), vars_list in sorted(state_connections.items()):
            vars_str = ", ".join([f"`{v}`" for v in vars_list[:5]])
            if len(vars_list) > 5:
                vars_str += f" (+{len(vars_list)-5} more)"
            lines.append(f"- `{mod1}` ↔ `{mod2}`: {vars_str}")
        lines.append("")
    
    # Add threading considerations
    threaded_modules = []
    for summary in summaries:
        if summary.get('threads') and summary.get('threads') != '_None_':
            threaded_modules.append(summary['file'])
    
    if threaded_modules:
        lines.append("### Threading Considerations")
        lines.append("")
        lines.append("**Threaded Modules:** " + ", ".join([f"`{m}`" for m in threaded_modules]))
        lines.append("")
        lines.append("⚠️ **Warning**: The following modules use threading and may access shared state concurrently:")
        for module in threaded_modules:
            lines.append(f"- `{module}`")
        lines.append("")
    
    lines.append("---")
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
        io_reads = extract(block, "IO_READS")
        io_writes = extract(block, "IO_WRITES")
        exceptions = extract(block, "EXCEPTIONS")
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
            "ui_binds": tk_binds,
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
    
    # Add Shared State Table section
    md.extend(generate_shared_state_table(summaries))
    
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
        md.append("\n" + (s['exceptions'] or "_No exception handlers detected._"))
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
