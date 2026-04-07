#!/usr/bin/env python3
"""
StudyFrog Code Investigator

This script investigates the StudyFrog codebase and reports violations of the established code design principles:
- Function-oriented design
- Minimal nesting (max 2-3 levels)
- Single purpose methods
- No objects apart from pure data storage (models.py only)
- etc.

Author: StudyFrog Development Team
Date: 2026-04-06
"""

from __future__ import annotations

import ast
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass
from collections import defaultdict

# Add src directory to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from studyfrog.constants.files import FLASHCARDS_DB_JSON, STACKS_DB_JSON


@dataclass
class Violation:
    """Represents a code violation found during investigation."""

    file_path: str
    line_number: int
    column: int
    violation_type: str
    description: str
    code_snippet: str
    severity: str  # 'error', 'warning', 'info'

    def to_dict(self) -> dict:
        return {
            "file_path": self.file_path,
            "line_number": self.line_number,
            "column": self.column,
            "violation_type": self.violation_type,
            "description": self.description,
            "code_snippet": self.code_snippet,
            "severity": self.severity,
        }


@dataclass
class InvestigationReport:
    """Summary report of all violations found."""

    violations: List[Violation]
    summary: Dict[str, int]
    files_analyzed: List[str]

    def add_violation(self, violation: Violation) -> None:
        self.violations.append(violation)

        # Update summary
        key = f"{violation.severity}_{violation.violation_type}"
        self.summary[key] = self.summary.get(key, 0) + 1

    def get_violations_by_severity(self) -> Dict[str, List[Violation]]:
        result = defaultdict(list)
        for violation in self.violations:
            result[violation.severity].append(violation)
        return dict(result)

    def get_violations_by_type(self) -> Dict[str, List[Violation]]:
        result = defaultdict(list)
        for violation in self.violations:
            result[violation.violation_type].append(violation)
        return dict(result)


class CodeInvestigator(ast.NodeVisitor):
    """AST visitor to investigate code for design principle violations."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.violations: List[Violation] = []
        self.current_function_stack: List[str] = []
        self.imports: Set[str] = set()
        self.class_definitions: Set[str] = set()
        self.nesting_level: int = 0
        self.max_nesting_level: int = 0

    def visit_Import(self, node: ast.Import) -> Any:
        """Track all imports."""
        for alias in node.names:
            if isinstance(node.module, ast.Name):
                self.imports.add(node.module.id)
            else:
                self.imports.add(str(node.module))
        return self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        """Track class definitions."""
        self.class_definitions.add(node.name)
        return self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        """Analyze function definitions for violations."""
        old_nesting = self.nesting_level
        self.nesting_level += 1
        self.current_function_stack.append(node.name)

        # Check function length
        if hasattr(node, "end_lineno") and hasattr(node, "lineno"):
            lines_in_function = node.end_lineno - node.lineno
            if lines_in_function > 50:
                self.add_violation(
                    Violation(
                        file_path=self.file_path,
                        line_number=node.lineno,
                        column=node.col_offset,
                        violation_type="long_function",
                        description=f"Function '{node.name}' is too long ({lines_in_function} lines, max 50)",
                        code_snippet=self._get_function_signature(node),
                        severity="warning",
                    )
                )

        # Visit function body
        self.generic_visit(node)

        self.nesting_level = old_nesting
        self.current_function_stack.pop()
        return None

    def visit_If(self, node: ast.If) -> Any:
        """Track if statement nesting."""
        old_nesting = self.nesting_level
        self.nesting_level += 1

        # Check for excessive nesting
        if self.nesting_level > 3:
            self.add_violation(
                Violation(
                    file_path=self.file_path,
                    line_number=node.lineno,
                    column=node.col_offset,
                    violation_type="excessive_nesting",
                    description=f"Nesting level {self.nesting_level} exceeds maximum of 3",
                    code_snippet=self._get_code_snippet(node),
                    severity="error",
                )
            )

        self.max_nesting_level = max(self.max_nesting_level, self.nesting_level)
        result = self.generic_visit(node)
        self.nesting_level = old_nesting
        return result

    def visit_For(self, node: ast.For) -> Any:
        """Track for loop nesting."""
        old_nesting = self.nesting_level
        self.nesting_level += 1

        # Check for excessive nesting
        if self.nesting_level > 3:
            self.add_violation(
                Violation(
                    file_path=self.file_path,
                    line_number=node.lineno,
                    column=node.col_offset,
                    violation_type="excessive_nesting",
                    description=f"For loop nesting level {self.nesting_level} exceeds maximum of 3",
                    code_snippet=self._get_code_snippet(node),
                    severity="error",
                )
            )

        self.max_nesting_level = max(self.max_nesting_level, self.nesting_level)
        result = self.generic_visit(node)
        self.nesting_level = old_nesting
        return result

    def visit_While(self, node: ast.While) -> Any:
        """Track while loop nesting."""
        old_nesting = self.nesting_level
        self.nesting_level += 1

        # Check for excessive nesting
        if self.nesting_level > 3:
            self.add_violation(
                Violation(
                    file_path=self.file_path,
                    line_number=node.lineno,
                    column=node.col_offset,
                    violation_type="excessive_nesting",
                    description=f"While loop nesting level {self.nesting_level} exceeds maximum of 3",
                    code_snippet=self._get_code_snippet(node),
                    severity="error",
                )
            )

        self.max_nesting_level = max(self.max_nesting_level, self.nesting_level)
        result = self.generic_visit(node)
        self.nesting_level = old_nesting
        return result

    def visit_Try(self, node: ast.Try) -> Any:
        """Track try-except block nesting."""
        old_nesting = self.nesting_level
        self.nesting_level += 1

        # Check for excessive nesting
        if self.nesting_level > 3:
            self.add_violation(
                Violation(
                    file_path=self.file_path,
                    line_number=node.lineno,
                    column=node.col_offset,
                    violation_type="excessive_nesting",
                    description=f"Try-except block nesting level {self.nesting_level} exceeds maximum of 3",
                    code_snippet=self._get_code_snippet(node),
                    severity="error",
                )
            )

        self.max_nesting_level = max(self.max_nesting_level, self.nesting_level)
        result = self.generic_visit(node)
        self.nesting_level = old_nesting
        return result

    def visit_Call(self, node: ast.Call) -> Any:
        """Check function calls for design principle violations."""
        # Check for object instantiation outside models/
        if isinstance(node.func, ast.Name):
            func_name = node.func.id

            # Check if instantiating classes not in models/
            if (
                func_name in ["FlashcardModel", "StackModel", "QuestionModel"]
                and not self._is_in_models_file()
            ):
                self.add_violation(
                    Violation(
                        file_path=self.file_path,
                        line_number=node.lineno,
                        column=node.col_offset,
                        violation_type="object_instantiation_outside_models",
                        description=f"Object instantiation of '{func_name}' outside models/ directory",
                        code_snippet=self._get_code_snippet(node),
                        severity="error",
                    )
                )

            # Check for complex function calls (too many arguments)
            if len(node.args) > 5:
                self.add_violation(
                    Violation(
                        file_path=self.file_path,
                        line_number=node.lineno,
                        column=node.col_offset,
                        violation_type="complex_function_call",
                        description=f"Function call with too many arguments ({len(node.args)}), max 5",
                        code_snippet=self._get_code_snippet(node),
                        severity="warning",
                    )
                )

        return self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> Any:
        """Check assignments for violations."""
        # Check for multiple assignment on one line
        if len(node.targets) > 3:
            self.add_violation(
                Violation(
                    file_path=self.file_path,
                    line_number=node.lineno,
                    column=node.col_offset,
                    violation_type="complex_assignment",
                    description=f"Multiple assignment ({len(node.targets)} variables) on single line",
                    code_snippet=self._get_code_snippet(node),
                    severity="warning",
                )
            )

        return self.generic_visit(node)

    def _is_in_models_file(self) -> bool:
        """Check if current file is in models/ directory."""
        return "models.py" in self.file_path

    def _get_function_signature(self, node: ast.FunctionDef) -> str:
        """Extract function signature for reporting."""
        args = []
        for arg in node.args.args:
            if arg.annotation:
                args.append(f"{arg.arg}: {ast.unparse(arg.annotation).eval()}")
            else:
                args.append(arg.arg)

        returns = ""
        if node.returns:
            returns = f" -> {ast.unparse(node.returns).eval()}"

        return f"def {node.name}({', '.join(args)}){returns}:"

    def _get_code_snippet(self, node: ast.AST) -> str:
        """Extract code snippet for reporting."""
        try:
            if hasattr(node, "lineno"):
                with open(self.file_path, "r") as f:
                    lines = f.readlines()
                    start_line = max(0, node.lineno - 1)
                    end_line = min(len(lines), node.lineno + 2)
                    return "\n".join(lines[start_line:end_line])
        except Exception:
            return f"Code at line {node.lineno}"
        except:
            return "Code snippet unavailable"


class ProjectInvestigator:
    """Main investigator class for the entire project."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.report = InvestigationReport(violations=[], summary={}, files_analyzed=[])

    def investigate_file(self, file_path: Path) -> None:
        """Investigate a single Python file for violations."""
        if not file_path.exists() or not file_path.suffix == ".py":
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            try:
                tree = ast.parse(content, filename=str(file_path))
                investigator = CodeInvestigator(str(file_path))
                investigator.visit(tree)
                self.report.files_analyzed.append(str(file_path))

                # Add all violations found
                for violation in investigator.violations:
                    self.report.add_violation(violation)

            except SyntaxError as e:
                # Add syntax error as violation
                self.report.add_violation(
                    Violation(
                        file_path=str(file_path),
                        line_number=e.lineno or 0,
                        column=e.offset or 0,
                        violation_type="syntax_error",
                        description=f"Syntax error: {e.msg}",
                        code_snippet=e.text or "",
                        severity="error",
                    )
                )
                self.report.files_analyzed.append(str(file_path))

        except Exception as e:
            print(f"Error investigating {file_path}: {e}")

    def investigate_project(self) -> InvestigationReport:
        """Investigate the entire project for violations."""
        print(f"Investigating project in: {self.project_root}")

        # Find all Python files
        python_files = []
        for root, dirs, files in os.walk(self.project_root):
            # Skip hidden directories and common non-source dirs
            dirs[:] = [
                d
                for d in dirs
                if not d.startswith(".") and d not in ["__pycache__", "venv", ".git"]
            ]

            for file in files:
                if file.endswith(".py"):
                    python_files.append(Path(root) / file)

        # Investigate each file
        for file_path in python_files:
            self.investigate_file(file_path)

        return self.report

    def generate_report(self, output_file: Optional[Path] = None) -> str:
        """Generate a comprehensive report of violations."""
        report_lines = []

        # Header
        report_lines.append("=" * 80)
        report_lines.append("STUDYFROG CODE INVESTIGATION REPORT")
        report_lines.append("=" * 80)
        report_lines.append("")

        # Summary
        report_lines.append("SUMMARY:")
        report_lines.append("-" * 40)
        total_violations = len(self.report.violations)
        report_lines.append(f"Total files analyzed: {len(self.report.files_analyzed)}")
        report_lines.append(f"Total violations found: {total_violations}")

        if total_violations > 0:
            violations_by_severity = self.report.get_violations_by_severity()
            for severity, violations in violations_by_severity.items():
                report_lines.append(f"  {severity.upper()}: {len(violations)}")

        report_lines.append("")

        # Violations by type
        if total_violations > 0:
            violations_by_type = self.report.get_violations_by_type()
            report_lines.append("VIOLATIONS BY TYPE:")
            report_lines.append("-" * 40)

            for violation_type, violations in violations_by_type.items():
                report_lines.append(f"  {violation_type}: {len(violations)}")
                if len(violations) <= 5:  # Show details for types with few violations
                    for violation in violations:
                        report_lines.append(f"    File: {violation.file_path}")
                        report_lines.append(f"    Line: {violation.line_number}")
                        report_lines.append(f"    {violation.description}")
                        report_lines.append("")

        report_lines.append("")

        # Detailed violations
        if total_violations > 0:
            report_lines.append("DETAILED VIOLATIONS:")
            report_lines.append("-" * 40)

            # Group violations by file
            violations_by_file = defaultdict(list)
            for violation in self.report.violations:
                violations_by_file[violation.file_path].append(violation)

            for file_path, file_violations in violations_by_file.items():
                if len(file_violations) > 0:
                    report_lines.append(f"FILE: {file_path}")
                    report_lines.append("-" * len(file_path))

                    for violation in file_violations:
                        report_lines.append(
                            f"  Line {violation.line_number}: {violation.violation_type}"
                        )
                        report_lines.append(f"    {violation.description}")
                        if violation.severity == "error":
                            report_lines.append(f"    Code: {violation.code_snippet}")
                        report_lines.append("")

        report_lines.append("")

        # Recommendations
        if total_violations > 0:
            report_lines.append("RECOMMENDATIONS:")
            report_lines.append("-" * 40)

            error_count = len([v for v in self.report.violations if v.severity == "error"])
            warning_count = len([v for v in self.report.violations if v.severity == "warning"])

            if error_count > 0:
                report_lines.append("1. Fix all ERROR level violations immediately")
                report_lines.append("2. Reduce nesting depth in complex functions")
                report_lines.append(
                    "3. Split large functions into smaller, single-purpose functions"
                )
                report_lines.append("4. Move object instantiations to models/ directory")

            if warning_count > 0:
                report_lines.append("1. Review WARNING level violations for potential improvements")
                report_lines.append("2. Consider reducing function complexity")
                report_lines.append("3. Ensure all functions have clear, single purposes")

        report_lines.append("")

        # Footer
        report_lines.append("=" * 80)
        report_lines.append(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 80)

        report_text = "\n".join(report_lines)

        # Save to file if specified
        if output_file:
            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(report_text)
                print(f"Report saved to: {output_file}")
            except Exception as e:
                print(f"Error saving report: {e}")

        return report_text


def main():
    """Main entry point for the code investigator."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Investigate StudyFrog code for design principle violations"
    )
    parser.add_argument(
        "project_root", type=str, default=".", help="Root directory of the StudyFrog project"
    )
    parser.add_argument(
        "--output", "-o", type=str, help="Output file for the report (default: print to console)"
    )
    parser.add_argument(
        "--severity",
        "-s",
        choices=["error", "warning", "info", "all"],
        default="all",
        help="Minimum severity level to report (default: all)",
    )

    args = parser.parse_args()

    # Validate project root
    project_root = Path(args.project_root).resolve()
    if not project_root.exists():
        print(f"Error: Project root {project_root} does not exist")
        return 1

    # Investigate project
    investigator = ProjectInvestigator(project_root)
    report = investigator.investigate_project()

    # Filter by severity if specified
    if args.severity != "all":
        severity_filter = {"error": 0, "warning": 1, "info": 2}[args.severity]
        filtered_violations = []
        for violation in report.violations:
            severity_value = {"error": 0, "warning": 1, "info": 2}[violation.severity]
            if severity_value >= severity_filter:
                filtered_violations.append(violation)

        report.violations = filtered_violations

        # Recreate summary
        report.summary = {}
        for violation in filtered_violations:
            key = f"{violation.severity}_{violation.violation_type}"
            report.summary[key] = report.summary.get(key, 0) + 1

    # Generate report
    output_file = Path(args.output) if args.output else None
    report_text = investigator.generate_report(output_file)

    if not output_file:
        print(report_text)

    return 0 if len([v for v in report.violations if v.severity == "error"]) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
