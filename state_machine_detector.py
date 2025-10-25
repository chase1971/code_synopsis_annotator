#===============================================================================
# CODE SYNOPSIS: state_machine_detector.py
# SYNOPSIS_HASH: 7d9bc9441f74e2eae9e52d33cfbd11d16df3d45f3682dfa1704e1b2a599c11e0
# Generated: 2025-10-25 13:00:59
# INTENT: Generates, Renders functionality for this module.
#===============================================================================
#
# OVERVIEW:
#   Total Lines: 559
#   Functions: 18
#   Classes: 4
#   Global Variables: 20
#
# Key Dependencies:
#   - ast
#   - collections
#   - dataclasses
#   - re
#   - typing
#
#===============================================================================
# ════════════════════
# BEGIN MACHINE-READABLE DATA (for automated processing)
# ════════════════════
# SYNOPSIS_ANNOTATED: YES
# LAST_ANALYZED: 2025-10-25 13:00:59
# FILE: state_machine_detector.py
# IMPORTS_EXTERNAL: ast, collections, dataclasses, re, typing
# IMPORTS_LOCAL: 
# GLOBALS: STATE_VARIABLE_PATTERNS, analyzer, comparisons, condition, detector, from_state, line_number, name, primary_variable, readers, related_variables, results, states, test_code, to_state, transitions, trigger_function, values, var_type, writers
# FUNCTIONS: __init__, _analyze_transitions, _build_function_map, _classify_state_variable, _detect_guards, _detect_state_variables, _extract_name, _extract_value, _get_enclosing_function, _group_into_state_machines, _infer_source_states, _matches_variable, detect, detect_state_machines, generate_mermaid_diagram, generate_state_machine_diagram, render_state_machine_summary, render_summary
# RETURNS: _classify_state_variable, _extract_name, _extract_value, _get_enclosing_function, _infer_source_states, _matches_variable, detect, detect_state_machines, generate_mermaid_diagram, generate_state_machine_diagram, render_state_machine_summary, render_summary
# THREAD_TARGETS: 
# HOTKEYS: 
# TK_BINDS: 
# COMMAND_BINDS: 
# CLASSES: StateMachine, StateMachineDetector, StateTransition, StateVariable
# IO_READS: 
# IO_WRITES: 
# CALLGRAPH_ROOTS: detect_state_machines,generate_state_machine_diagram,render_state_machine_summary,__init__,detect,_build_function_map,_detect_state_variables,_classify_state_variable,_analyze_transitions,_detect_guards,_group_into_state_machines,_matches_variable,_extract_value,_extract_name,_get_enclosing_function,_infer_source_states,generate_mermaid_diagram,render_summary
# STATE_VARS: STATE_VARIABLE_PATTERNS,clean_state,detector,from_state,states,to_state,var_type
# STATE_MACHINES_COUNT: 3
# STATE_TRANSITIONS_COUNT: 0
# INIT_SEQUENCE: 
# INTENT: Generates, Renders functionality for this module.
# FUNCTION_INTENTS: __init__=Updates internal state., _analyze_transitions=Analyze state transitions (assignments to state variables)., _build_function_map=Build a map of function names to their AST nodes., _classify_state_variable=Classify if a variable name represents state., _detect_guards=Detect guard conditions (if statements checking state)., _detect_state_variables=Detect variables that represent state., _extract_name=Extract a variable name from an AST node., _extract_value=Extract a constant value from an AST node., _get_enclosing_function=Find the name of the function enclosing this node., _group_into_state_machines=Group related state variables into state machines., _infer_source_states=Infer possible source states by looking at preceding if conditions., _matches_variable=Check if a state value relates to a variable., detect=Run full state machine detection pipeline., detect_state_machines=Detect state machines in the given analyzer's code., generate_mermaid_diagram=Generate a Mermaid state diagram for detected state machines., generate_state_machine_diagram=Generate a Mermaid state diagram for detected state machines., render_state_machine_summary=Render a text summary of detected state machines for synopsis header., render_summary=Render a text summary of detected state machines.
# END MACHINE-READABLE DATA
# ════════════════════
#===============================================================================
#
# 📝 FUNCTION SIGNATURES:
#
# StateMachineDetector.__init__(self, analyzer) -> None
#   Initialize with a CodeAnalyzer instance.
#
# StateMachineDetector._analyze_transitions(self) -> None
#   Analyze state transitions (assignments to state variables).
#
# StateMachineDetector._build_function_map(self) -> None
#   Build a map of function names to their AST nodes.
#
# StateMachineDetector._classify_state_variable(self, var_name: str) -> Optional[str]
#   Classify if a variable name represents state.
#
# StateMachineDetector._detect_guards(self) -> None
#   Detect guard conditions (if statements checking state).
#
# StateMachineDetector._detect_state_variables(self) -> None
#   Detect variables that represent state.
#
# StateMachineDetector._extract_name(self, node: ast.AST) -> Optional[str]
#   Extract a variable name from an AST node.
#
# StateMachineDetector._extract_value(self, node: ast.AST) -> Optional[str]
#   Extract a constant value from an AST node.
#
# StateMachineDetector._get_enclosing_function(self, node: ast.AST) -> Optional[str]
#   Find the name of the function enclosing this node.
#
# StateMachineDetector._group_into_state_machines(self) -> None
#   Group related state variables into state machines.
#
# StateMachineDetector._infer_source_states(self, func_node: ast.FunctionDef, var_name: str, assignment_node: ast.Assign) -> List[str]
#   Infer possible source states by looking at preceding if conditions.
#
# StateMachineDetector._matches_variable(self, state_value: str, var_name: str) -> bool
#   Check if a state value relates to a variable.
#
# StateMachineDetector.detect(self) -> Dict[str, any]
#   Run full state machine detection pipeline.
#
# StateMachineDetector.generate_mermaid_diagram(self) -> str
#   Generate a Mermaid state diagram for detected state machines.
#
# StateMachineDetector.render_summary(self) -> List[str]
#   Render a text summary of detected state machines.
#
# detect_state_machines(analyzer) -> Dict[str, any]
#   Detect state machines in the given analyzer's code.
#
# generate_state_machine_diagram(analyzer) -> str
#   Generate a Mermaid state diagram for detected state machines.
#
# render_state_machine_summary(analyzer) -> List[str]
#   Render a text summary of detected state machines for synopsis header.
#
#===============================================================================
#
# 🧱 CLASSES FOUND:
#
#   StateVariable (line 64):
#   StateTransition (line 75):
#   StateMachine (line 85):
#   StateMachineDetector (line 93):
#     - StateMachineDetector.__init__()
#     - StateMachineDetector.detect()
#     - StateMachineDetector._build_function_map()
#     - StateMachineDetector._detect_state_variables()
#     - StateMachineDetector._classify_state_variable()
#     - StateMachineDetector._analyze_transitions()
#     - StateMachineDetector._detect_guards()
#     - StateMachineDetector._group_into_state_machines()
#     - StateMachineDetector._matches_variable()
#     - StateMachineDetector._extract_value()
#     - StateMachineDetector._extract_name()
#     - StateMachineDetector._get_enclosing_function()
#     - StateMachineDetector._infer_source_states()
#     - StateMachineDetector.generate_mermaid_diagram()
#     - StateMachineDetector.render_summary()
#===============================================================================
#
# CRITICAL GLOBAL VARIABLES:
#
# detector:
#   Modified by: detect_state_machines, generate_state_machine_diagram, render_state_machine_summary
#   Read by: detect_state_machines, generate_state_machine_diagram, render_state_machine_summary
#
# from_state:
#   Modified by: _analyze_transitions, generate_mermaid_diagram
#   Read by: _analyze_transitions, generate_mermaid_diagram
#
# var_type:
#   Modified by: _detect_state_variables, _classify_state_variable
#   Read by: _detect_state_variables, _classify_state_variable
#
# to_state:
#   Modified by: _analyze_transitions, generate_mermaid_diagram
#   Read by: _analyze_transitions, generate_mermaid_diagram
#
#===============================================================================
#
# SHARED STATE CATEGORIES:
#
#   Control State:
#     - STATE_VARIABLE_PATTERNS
#     - from_state
#     - states
#     - to_state
#   Position State:
#     - analyzer
#     - primary_variable
#     - var_type
#===============================================================================
#
# 🧠 FUNCTION BEHAVIORAL SUMMARIES:
#
#
#===============================================================================
#
# FUNCTION CALL HIERARCHY (depth-limited):
#
# - detect_state_machines()
#
# - generate_state_machine_diagram()
#
# - render_state_machine_summary()
#
# - __init__()
#
# - detect()
#
# - _build_function_map()
#
# - _detect_state_variables()
#
# - _classify_state_variable()
#
# - _analyze_transitions()
#
# - _detect_guards()
#
# - _group_into_state_machines()
#
# - _matches_variable()
#
# - _extract_value()
#
# - _extract_name()
#
# - _get_enclosing_function()
#
# - _infer_source_states()
#
# - generate_mermaid_diagram()
#
# - render_summary()
#
#===============================================================================
#
# 🔄 STATE MACHINES DETECTED:
#
#   📍 clean_state (State Variable):
#      States: (values unknown)
#      Modified by: generate_mermaid_diagram
#      Checked by: generate_mermaid_diagram
#
#   📍 from_state (State Variable):
#      States: *
#      Modified by: _analyze_transitions, generate_mermaid_diagram
#      Checked by: _analyze_transitions, generate_mermaid_diagram
#
#   📍 to_state (State Variable):
#      States: (values unknown)
#      Modified by: _analyze_transitions, generate_mermaid_diagram
#      Checked by: _analyze_transitions, generate_mermaid_diagram
#
#
#===============================================================================
#
# 🔄 STATE MACHINE DIAGRAMS:
#
# ```mermaid
# stateDiagram-v2
#     [*] --> Unknown
#     [*] --> *
#     [*] --> Unknown
# ```
#
#
# 📊 DATA FLOW SUMMARY:
#
#   detect() — calls self._analyze_transitions, self._build_function_map, self._detect_guards, self._detect_state_variables, self._group_into_state_machines; returns value
#   _build_function_map() — calls ast.walk, isinstance; no return value
#   _detect_state_variables() — reads var_type; writes var_type; calls StateVariable, ast.walk, isinstance, self._classify_state_variable, self._get_enclosing_function, str; no return value
#   _classify_state_variable() — reads STATE_VARIABLE_PATTERNS, var_type; writes var_type; calls STATE_VARIABLE_PATTERNS.items, re.match; returns value
#   _analyze_transitions() — reads from_state, to_state; writes from_state, to_state; calls StateTransition, ast.walk, isinstance, self._extract_value, self._infer_source_states, self.function_contexts.items; no return value
#   _detect_guards() — calls ast.walk, comparisons.add, isinstance, readers.add, self._extract_name, self._extract_value; no return value
#   _group_into_state_machines() — reads states; writes states; calls StateMachine, self._matches_variable, self.state_machines.append, self.state_variables.items; no return value
#   _matches_variable() — pure/local computation; returns value
#   _extract_value() — calls isinstance, self._extract_name, str; returns value
#   _extract_name() — calls isinstance, join, parts.append, reversed; returns value
#   _get_enclosing_function() — calls any, ast.walk, self.function_contexts.items; returns value
#   _infer_source_states() — calls any, ast.walk, checked_values.append, isinstance, self._extract_name, self._extract_value; returns value
#   generate_mermaid_diagram() — reads from_state, to_state; writes from_state, to_state; calls join, lines.append, list, replace, sorted, state.replace; returns value
#   render_summary() — calls append, defaultdict, get, join, len, lines.append; returns value
#   detect_state_machines() — reads detector; writes detector; calls StateMachineDetector, detector.detect; returns value
#   generate_state_machine_diagram() — reads detector; writes detector; calls StateMachineDetector, detector.detect, detector.generate_mermaid_diagram; returns value
#   render_state_machine_summary() — reads detector; writes detector; calls StateMachineDetector, detector.detect, detector.render_summary; returns value
#   __init__() — calls ast.parse; no return value
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
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
# === END SYNOPSIS HEADER ===
"""
State Machine Detector - AST-based state machine pattern detection

This module detects state machine patterns in Python code by analyzing:
1. State variables (variables ending in _state, mode, paused, etc.)
2. State transitions (assignments to state variables)
3. Guard conditions (if statements checking state)
4. Transition triggers (functions that change state)

Works on ANY Python project with state machines, not just specific codebases.
"""

import ast
import re
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict
from dataclasses import dataclass, field


# ============================================================================
# STATE VARIABLE DETECTION PATTERNS
# ============================================================================

STATE_VARIABLE_PATTERNS = {
    # Explicit state variables
    r'.*_state$': 'explicit_state',
    r'.*State$': 'explicit_state',
    r'.*STATUS$': 'status',
    
    # Mode variables
    r'^mode$': 'mode',
    r'.*_mode$': 'mode',
    r'.*Mode$': 'mode',
    
    # Grace period / cooldown states (CHECK BEFORE general boolean patterns)
    r'.*cooldown.*': 'temporal_state',
    r'.*grace.*': 'temporal_state',
    r'.*_timeout$': 'temporal_state',
    r'.*_deadline$': 'temporal_state',
    
    # Boolean state flags
    r'^paused$': 'boolean_state',
    r'^running$': 'boolean_state',
    r'^enabled$': 'boolean_state',
    r'^active$': 'boolean_state',
    r'^locked$': 'boolean_state',
    r'^stopped$': 'boolean_state',
    r'^started$': 'boolean_state',
    r'.*_paused$': 'boolean_state',
    r'.*_running$': 'boolean_state',
    r'.*_enabled$': 'boolean_state',
    r'.*_active$': 'boolean_state',
    r'.*_locked$': 'boolean_state',
}


@dataclass
class StateVariable:
    """Represents a detected state variable."""
    name: str
    var_type: str  # 'explicit_state', 'mode', 'boolean_state', 'status', 'temporal_state'
    values: Set[str] = field(default_factory=set)  # Possible values
    writers: Set[str] = field(default_factory=set)  # Functions that modify it
    readers: Set[str] = field(default_factory=set)  # Functions that read it
    comparisons: Set[str] = field(default_factory=set)  # Values compared against


@dataclass
class StateTransition:
    """Represents a state transition."""
    from_state: str
    to_state: str
    trigger_function: str
    condition: Optional[str] = None  # Guard condition
    line_number: int = 0


@dataclass
class StateMachine:
    """Represents a detected state machine."""
    primary_variable: str
    states: Set[str] = field(default_factory=set)
    transitions: List[StateTransition] = field(default_factory=list)
    related_variables: Set[str] = field(default_factory=set)


class StateMachineDetector:
    """
    Detects state machine patterns in Python AST.
    
    This is designed to integrate with CodeAnalyzer as a behavioral analysis component.
    """
    
    def __init__(self, analyzer):
        """
        Initialize with a CodeAnalyzer instance.
        
        Args:
            analyzer: CodeAnalyzer instance with parsed AST
        """
        self.analyzer = analyzer
        self.tree = analyzer.tree
        
        # Detection results
        self.state_variables: Dict[str, StateVariable] = {}
        self.state_machines: List[StateMachine] = []
        self.transitions: List[StateTransition] = []
        
        # Helper tracking
        self.function_contexts: Dict[str, ast.FunctionDef] = {}  # func_name -> node
        self.current_function: Optional[str] = None
    
    def detect(self) -> Dict[str, any]:
        """
        Run full state machine detection pipeline.
        
        Returns:
            Dictionary with detection results
        """
        # Step 1: Build function context map
        self._build_function_map()
        
        # Step 2: Detect state variables
        self._detect_state_variables()
        
        # Step 3: Analyze state transitions
        self._analyze_transitions()
        
        # Step 4: Detect guard conditions
        self._detect_guards()
        
        # Step 5: Group into state machines
        self._group_into_state_machines()
        
        return {
            'state_variables': self.state_variables,
            'state_machines': self.state_machines,
            'transitions': self.transitions
        }
    
    def _build_function_map(self):
        """Build a map of function names to their AST nodes."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                self.function_contexts[node.name] = node
    
    def _detect_state_variables(self):
        """Detect variables that represent state."""
        # Check global variables and assignments
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id
                        var_type = self._classify_state_variable(var_name)
                        
                        if var_type:
                            if var_name not in self.state_variables:
                                self.state_variables[var_name] = StateVariable(
                                    name=var_name,
                                    var_type=var_type
                                )
                            
                            # Track the value being assigned
                            if isinstance(node.value, ast.Constant):
                                self.state_variables[var_name].values.add(str(node.value.value))
                            elif isinstance(node.value, ast.Name):
                                self.state_variables[var_name].values.add(node.value.id)
                            elif isinstance(node.value, ast.Num):  # Python 3.7 compatibility
                                self.state_variables[var_name].values.add(str(node.value.n))
                            elif isinstance(node.value, ast.Str):  # Python 3.7 compatibility
                                self.state_variables[var_name].values.add(node.value.s)
                            
                            # Track which function modifies it
                            enclosing = self._get_enclosing_function(node)
                            if enclosing:
                                self.state_variables[var_name].writers.add(enclosing)
    
    def _classify_state_variable(self, var_name: str) -> Optional[str]:
        """Classify if a variable name represents state."""
        for pattern, var_type in STATE_VARIABLE_PATTERNS.items():
            if re.match(pattern, var_name, re.IGNORECASE):
                return var_type
        return None
    
    def _analyze_transitions(self):
        """Analyze state transitions (assignments to state variables)."""
        for func_name, func_node in self.function_contexts.items():
            # Find assignments within this function
            for node in ast.walk(func_node):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id in self.state_variables:
                            var_name = target.id
                            
                            # Determine the target state
                            to_state = self._extract_value(node.value)
                            
                            if to_state:
                                # Try to determine the source state from context
                                from_states = self._infer_source_states(func_node, var_name, node)
                                
                                for from_state in from_states:
                                    transition = StateTransition(
                                        from_state=from_state,
                                        to_state=to_state,
                                        trigger_function=func_name,
                                        line_number=node.lineno
                                    )
                                    self.transitions.append(transition)
    
    def _detect_guards(self):
        """Detect guard conditions (if statements checking state)."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.If) or isinstance(node, ast.Compare):
                # Look for comparisons involving state variables
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Compare):
                        left_name = self._extract_name(sub.left)
                        
                        if left_name and left_name in self.state_variables:
                            # Extract compared values
                            for comparator in sub.comparators:
                                value = self._extract_value(comparator)
                                if value:
                                    self.state_variables[left_name].comparisons.add(value)
                            
                            # Track which function reads this state
                            enclosing = self._get_enclosing_function(node)
                            if enclosing:
                                self.state_variables[left_name].readers.add(enclosing)
    
    def _group_into_state_machines(self):
        """Group related state variables into state machines."""
        # For now, treat each state variable as its own state machine
        # In the future, could cluster related variables
        for var_name, var_data in self.state_variables.items():
            if var_data.var_type in ['explicit_state', 'mode', 'status']:
                # This is likely a primary state machine variable
                states = var_data.values | var_data.comparisons
                
                # Find transitions for this variable
                related_transitions = [
                    t for t in self.transitions 
                    if self._matches_variable(t.from_state, var_name) or 
                       self._matches_variable(t.to_state, var_name)
                ]
                
                machine = StateMachine(
                    primary_variable=var_name,
                    states=states,
                    transitions=related_transitions
                )
                self.state_machines.append(machine)
    
    def _matches_variable(self, state_value: str, var_name: str) -> bool:
        """Check if a state value relates to a variable."""
        # Simple heuristic: if variable is in analyzer's state_vars
        return var_name in self.analyzer.state_vars
    
    def _extract_value(self, node: ast.AST) -> Optional[str]:
        """Extract a constant value from an AST node."""
        if isinstance(node, ast.Constant):
            return str(node.value)
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Num):  # Python 3.7 compatibility
            return str(node.n)
        elif isinstance(node, ast.Str):  # Python 3.7 compatibility
            return node.s
        elif isinstance(node, ast.Attribute):
            return self._extract_name(node)
        return None
    
    def _extract_name(self, node: ast.AST) -> Optional[str]:
        """Extract a variable name from an AST node."""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            parts = []
            current = node
            while isinstance(current, ast.Attribute):
                parts.append(current.attr)
                current = current.value
            if isinstance(current, ast.Name):
                parts.append(current.id)
            return '.'.join(reversed(parts))
        return None
    
    def _get_enclosing_function(self, node: ast.AST) -> Optional[str]:
        """Find the name of the function enclosing this node."""
        for func_name, func_node in self.function_contexts.items():
            if any(n is node for n in ast.walk(func_node)):
                return func_name
        return None
    
    def _infer_source_states(self, func_node: ast.FunctionDef, var_name: str, assignment_node: ast.Assign) -> List[str]:
        """
        Infer possible source states by looking at preceding if conditions.
        
        This is a heuristic approach - looks for if statements checking the variable
        before the assignment.
        """
        source_states = ['*']  # Default: any state
        
        # Look for if conditions in the function
        for node in ast.walk(func_node):
            if isinstance(node, ast.If):
                # Check if this if statement checks our variable
                condition_checks_var = False
                checked_values = []
                
                for sub in ast.walk(node.test):
                    if isinstance(sub, ast.Compare):
                        left_name = self._extract_name(sub.left)
                        if left_name == var_name:
                            condition_checks_var = True
                            # Extract the compared value
                            for comp in sub.comparators:
                                val = self._extract_value(comp)
                                if val:
                                    checked_values.append(val)
                
                if condition_checks_var and checked_values:
                    # Check if our assignment is within this if block
                    if any(n is assignment_node for n in ast.walk(node)):
                        source_states = checked_values
                        break
        
        return source_states if source_states != ['*'] else ['*']
    
    def generate_mermaid_diagram(self) -> str:
        """
        Generate a Mermaid state diagram for detected state machines.
        
        Returns:
            Mermaid diagram as a string
        """
        if not self.state_machines:
            return ""
        
        lines = ["# ```mermaid", "# stateDiagram-v2"]
        
        for machine in self.state_machines:
            lines.append(f"#     [*] --> {list(machine.states)[0] if machine.states else 'Unknown'}")
            
            # Add all states
            for state in sorted(machine.states):
                # Clean state name for Mermaid
                clean_state = state.replace(' ', '_').replace('=', '_').replace('"', '').replace("'", '')
                if clean_state not in ['True', 'False', '*']:
                    lines.append(f"#     state \"{state}\" as {clean_state}")
            
            # Add transitions
            for transition in machine.transitions:
                from_state = transition.from_state.replace(' ', '_').replace('=', '_')
                to_state = transition.to_state.replace(' ', '_').replace('=', '_')
                trigger = transition.trigger_function
                
                if from_state == '*':
                    # Transition from any state
                    lines.append(f"#     {to_state} --> {to_state}: {trigger}()")
                else:
                    condition_str = f" [{transition.condition}]" if transition.condition else ""
                    lines.append(f"#     {from_state} --> {to_state}: {trigger}(){condition_str}")
        
        lines.append("# ```")
        return '\n'.join(lines)
    
    def render_summary(self) -> List[str]:
        """
        Render a text summary of detected state machines.
        
        Returns:
            List of summary lines formatted for synopsis header
        """
        if not self.state_variables:
            return ["#", "# 🔄 STATE MACHINES:", "#", "#   (No state machines detected.)", "#"]
        
        lines = ["#", "# 🔄 STATE MACHINES DETECTED:", "#"]
        
        for var_name, var_data in sorted(self.state_variables.items()):
            var_type_label = {
                'explicit_state': 'State Variable',
                'mode': 'Mode Variable',
                'boolean_state': 'Boolean State',
                'status': 'Status Variable',
                'temporal_state': 'Temporal State'
            }.get(var_data.var_type, 'State')
            
            all_values = sorted(var_data.values | var_data.comparisons)
            if all_values:
                values_str = ' → '.join(all_values)
            else:
                values_str = '(values unknown)'
            
            lines.append(f"#   📍 {var_name} ({var_type_label}):")
            lines.append(f"#      States: {values_str}")
            
            if var_data.writers:
                writers_str = ', '.join(sorted(list(var_data.writers))[:5])
                if len(var_data.writers) > 5:
                    writers_str += f", +{len(var_data.writers)-5} more"
                lines.append(f"#      Modified by: {writers_str}")
            
            if var_data.readers:
                readers_str = ', '.join(sorted(list(var_data.readers))[:5])
                if len(var_data.readers) > 5:
                    readers_str += f", +{len(var_data.readers)-5} more"
                lines.append(f"#      Checked by: {readers_str}")
            
            lines.append("#")
        
        # Add transition summary
        if self.transitions:
            lines.append("#   🔀 Key Transitions:")
            # Group transitions by trigger function
            transitions_by_func = defaultdict(list)
            for t in self.transitions:
                transitions_by_func[t.trigger_function].append(t)
            
            for func, trans_list in sorted(transitions_by_func.items())[:10]:
                trans_strs = [f"{t.from_state}→{t.to_state}" for t in trans_list[:3]]
                trans_summary = ', '.join(trans_strs)
                if len(trans_list) > 3:
                    trans_summary += f", +{len(trans_list)-3} more"
                lines.append(f"#      {func}(): {trans_summary}")
            
            if len(transitions_by_func) > 10:
                lines.append(f"#      ... +{len(transitions_by_func)-10} more functions")
        
        lines.append("#")
        return lines


# ============================================================================
# INTEGRATION FUNCTIONS
# ============================================================================

def detect_state_machines(analyzer) -> Dict[str, any]:
    """
    Detect state machines in the given analyzer's code.
    
    This is the main entry point for integration with CodeAnalyzer.
    
    Args:
        analyzer: CodeAnalyzer instance
        
    Returns:
        Dictionary with state machine detection results
    """
    detector = StateMachineDetector(analyzer)
    return detector.detect()


def generate_state_machine_diagram(analyzer) -> str:
    """
    Generate a Mermaid state diagram for detected state machines.
    
    Args:
        analyzer: CodeAnalyzer instance
        
    Returns:
        Mermaid diagram as a string
    """
    detector = StateMachineDetector(analyzer)
    detector.detect()
    return detector.generate_mermaid_diagram()


def render_state_machine_summary(analyzer) -> List[str]:
    """
    Render a text summary of detected state machines for synopsis header.
    
    Args:
        analyzer: CodeAnalyzer instance
        
    Returns:
        List of formatted summary lines
    """
    detector = StateMachineDetector(analyzer)
    detector.detect()
    return detector.render_summary()


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("State Machine Detector - Unit Test")
    print("=" * 70)
    
    # Create a simple test case
    test_code = """
mode = 1
paused = False
running = True

def toggle_pause():
    global paused
    if not paused:
        paused = True
    else:
        paused = False

def switch_mode():
    global mode
    if mode == 1:
        mode = 2
    elif mode == 2:
        mode = 1

def start_running():
    global running
    running = True
    paused = False
"""
    
    # Mock analyzer
    class MockAnalyzer:
        def __init__(self, code):
            self.tree = ast.parse(code)
            self.state_vars = {}
            self.globals_found = {'mode', 'paused', 'running'}
            self.functions = {}
    
    analyzer = MockAnalyzer(test_code)
    detector = StateMachineDetector(analyzer)
    results = detector.detect()
    
    print(f"\nDetected {len(results['state_variables'])} state variables:")
    for var_name, var_data in results['state_variables'].items():
        print(f"  - {var_name}: {var_data.var_type}")
        print(f"    Values: {var_data.values}")
        print(f"    Writers: {var_data.writers}")
    
    print(f"\nDetected {len(results['transitions'])} transitions")
    
    print("\n" + "=" * 70)
    print("Summary Output:")
    print("=" * 70)
    for line in detector.render_summary():
        try:
            print(line)
        except UnicodeEncodeError:
            # Handle Unicode characters for Windows console
            print(line.encode('ascii', 'replace').decode('ascii'))
    
    print("\n" + "=" * 70)
    print("Mermaid Diagram:")
    print("=" * 70)
    print(detector.generate_mermaid_diagram())
