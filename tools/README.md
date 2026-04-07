# StudyFrog Development Tools

This directory contains tools for analyzing and maintaining the StudyFrog codebase according to established design principles.

## Tools

### code_investigator.py

A Python script that investigates the StudyFrog codebase and reports violations of the established code design principles:

#### Design Principles Checked

1. **Function-Oriented Design**
   - Pure functions with single responsibilities
   - No hidden side effects or state modification
   - Clear, predictable behavior

2. **Minimal Nesting**
   - Maximum 2-3 levels of function nesting
   - Flat structures for better testability
   - Early returns and guard clauses

3. **Single Purpose Methods**
   - Each function has one specific outcome
   - Clear, descriptive naming
   - No multiple responsibilities per function

4. **Pure Data Storage**
   - Storage functions only handle data persistence
   - No business logic embedded in storage layer
   - Object instantiations only in models/ directory

#### Violations Detected

- **Excessive Nesting**: Functions or control structures nested beyond 3 levels
- **Long Functions**: Functions exceeding 50 lines of code
- **Object Instantiation Outside Models**: Creating model objects outside models/ directory
- **Complex Function Calls**: Function calls with too many arguments (>5)
- **Complex Assignments**: Multiple variable assignments on single line (>3)
- **Syntax Errors**: Invalid Python syntax

#### Usage

```bash
# Basic usage - investigate entire project
python tools/code_investigator.py /path/to/studyfrog

# Generate report file
python tools/code_investigator.py /path/to/studyfrog --output investigation_report.txt

# Filter by severity level
python tools/code_investigator.py /path/to/studyfrog --severity error

# Help
python tools/code_investigator.py --help
```

#### Output

The investigator generates a comprehensive report including:

- **Summary Statistics**: Total files analyzed, violations by severity and type
- **Detailed Violations**: File-by-file breakdown with line numbers and descriptions
- **Code Snippets**: Actual code that violates principles
- **Recommendations**: Specific actions to fix identified issues

#### Integration with Development

1. **Pre-commit Hook**: Add as pre-commit hook to automatically check code
2. **CI/CD Pipeline**: Integrate into continuous integration
3. **Code Review**: Use reports to guide code review discussions
4. **Refactoring**: Prioritize fixes based on violation severity

#### Example Report Output

```
================================================================================
STUDYFROG CODE INVESTIGATION REPORT
================================================================================

SUMMARY:
----------------------------------------
Total files analyzed: 45
Total violations found: 12
  ERROR: 3
  WARNING: 9

VIOLATIONS BY TYPE:
----------------------------------------
  excessive_nesting: 3
  long_function: 2
  object_instantiation_outside_models: 4
  complex_function_call: 3

DETAILED VIOLATIONS:
----------------------------------------
FILE: /path/to/studyfrog/src/gui/views/create_view.py
----------------------------------------
  Line 156: excessive_nesting
    If statement nesting level 4 exceeds maximum of 3
    Code: if user_input and validation_result:
        if user_input and validation_result:

FILE: /path/to/studyfrog/src/gui/logic/create_view_logic.py
----------------------------------------
  Line 89: object_instantiation_outside_models
    Object instantiation of 'FlashcardModel' outside models/ directory
    Code: flashcard = FlashcardModel(
        front=front_text,
        back=back_text
    )

RECOMMENDATIONS:
----------------------------------------
1. Fix all ERROR level violations immediately
2. Reduce nesting depth in complex functions
3. Split large functions into smaller, single-purpose functions
4. Move object instantiations to models/ directory

================================================================================
Report generated on: 2026-04-06 11:30:15
================================================================================
```

## Contributing

When adding new analysis tools to this directory:

1. **Follow the same design principles** as the main codebase
2. **Include comprehensive documentation** with usage examples
3. **Add error handling** for robustness
4. **Consider performance** for large codebases
5. **Make tools configurable** through command-line arguments

## Future Tools

Potential tools to add in the future:

- **Performance Profiler**: Analyze function performance and complexity
- **Dependency Mapper**: Visualize import dependencies and circular imports
- **Test Coverage Analyzer**: Ensure comprehensive test coverage
- **Documentation Generator**: Auto-generate documentation from code
- **Refactoring Assistant**: Suggest code improvements automatically

These tools help maintain the high code quality standards established in the StudyFrog project.
