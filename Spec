OPRMT v1.0 Specification
Open Prompt Markup Template
Version: 1.0.0
Status: Release Candidate
Date: November 17, 2025
Document: OPRMT_v1_Specification.md
1. Introduction
1.1 Purpose
OPRMT (Open Prompt Format) is a standardized format for structuring, sharing, and executing AI prompts across different platforms and language models. This specification defines the syntax, semantics, and best practices for creating portable, maintainable, and executable prompt templates.
1.2 Goals
Portability: Prompts written in OPRMT should work across different AI platforms with minimal modification
Reusability: Enable prompt templates that can be easily shared and adapted
Maintainability: Provide clear structure for complex, multi-part prompts
Interoperability: Support integration with various AI systems and workflows
Version Control: Enable effective tracking of prompt changes over time
1.3 Scope
This specification covers:
File format and structure
Metadata requirements
Variable substitution syntax
Conditional logic
Template composition
Execution semantics
Validation rules
2. File Format
2.1 File Extension
OPRMT files use the .oprmt extension.
2.2 Character Encoding
All OPRMT files MUST be encoded in UTF-8 without BOM (Byte Order Mark).
2.3 File Structure
An OPRMT file consists of three main sections:
---
[METADATA]
---
[TEMPLATE]
---
[EXAMPLES] (optional)
---
3. Metadata Section
3.1 Required Fields
The metadata section uses YAML syntax and MUST include:
version: "1.0"
name: "Prompt Name"
description: "Brief description of prompt purpose"
author: "Author name or organization"
created: "2025-11-17"
3.2 Optional Fields
modified: "2025-11-17"
tags: ["category", "use-case", "domain"]
model_hints: ["gpt-4", "claude-3", "gemini"]
parameters:
  - name: "param_name"
    type: "string|number|boolean|array|object"
    required: true|false
    default: "default_value"
    description: "Parameter description"
variables:
  - name: "var_name"
    description: "Variable purpose"
    example: "Example value"
license: "MIT|Apache-2.0|CC-BY-4.0|Proprietary"
3.3 Field Definitions
version: OPRMT specification version (MUST be "1.0" for this spec)
name: Human-readable prompt name (max 100 characters)
description: Detailed explanation of prompt purpose (max 500 characters)
author: Creator identification
created: ISO 8601 date (YYYY-MM-DD)
modified: ISO 8601 date of last modification
tags: Array of classification tags
model_hints: Suggested compatible AI models
parameters: Configurable inputs for the template
variables: Dynamic placeholders used in template
license: Usage and distribution terms
4. Template Section
4.1 Basic Syntax
The template section contains the actual prompt text with optional variable substitution and logic.
You are an expert {{role}}.

Your task is to {{task}}.
4.2 Variable Substitution
Variables are enclosed in double curly braces: {{variable_name}}
Rules:
Variable names MUST match [a-zA-Z_][a-zA-Z0-9_]*
Variables MUST be declared in metadata variables or parameters
Undefined variables SHOULD trigger a warning during validation
4.3 Conditional Logic
4.3.1 If Statements
{{#if condition}}
Content shown when condition is true
{{/if}}
4.3.2 If-Else Statements
{{#if condition}}
Content when true
{{#else}}
Content when false
{{/if}}
4.3.3 Conditional Operators
{{#if var}} - True if var is defined and not empty/false/0
{{#unless var}} - Inverse of if
Comparison operators not supported in v.1.0 (reserved for future versions)
4.4 Loops
4.4.1 Each Loop
{{#each items}}
- {{this}}
{{/each}}
4.4.2 Loop Context
Inside loops:
{{this}} references current item
{{@index}} provides zero-based index
{{@first}} is true for first iteration
{{@last}} is true for last iteration
4.5 Comments
Comments are ignored during execution:
{{! This is a comment }}

{{!-- 
Multi-line comment
Useful for documentation
--}}
4.6 Escaping
To include literal curly braces:
Use \{{literal}} to show {{literal}}
5. Examples Section
5.1 Purpose
The optional examples section demonstrates prompt usage with sample inputs and expected outputs.
5.2 Format
examples:
  - input:
      role: "Python developer"
      task: "write a function to sort a list"
    output: |
      Expected response format or sample output
  - input:
      role: "Marketing specialist"
      task: "create a tagline for a coffee shop"
    output: |
      Sample marketing tagline response
6. Complete Example
---
version: "1.0"
name: "Code Review Assistant"
description: "Reviews code for best practices, bugs, and improvements"
author: "DevTools Team"
created: "2025-11-17"
tags: ["coding", "review", "quality"]
parameters:
  - name: "language"
    type: "string"
    required: true
    description: "Programming language of the code"
  - name: "focus_areas"
    type: "array"
    required: false
    default: ["security", "performance", "readability"]
    description: "Specific aspects to focus on"
variables:
  - name: "code"
    description: "The code to review"
    example: "function add(a, b) { return a + b; }"
license: "MIT"
---
You are an expert {{language}} code reviewer.

Review the following code for:
{{#each focus_areas}}
- {{this}}
{{/each}}

Code to review:
```{{language}}
{{code}}
Provide:
Overall assessment
Specific issues found
Suggested improvements
Security considerations
{{#if security_critical}}
Pay special attention to security vulnerabilities and potential exploits.
{{/if}}
examples:
input:
language: "python"
code: "def calc(x,y): return eval(x+y)"
focus_areas: ["security", "best practices"]
security_critical: true
output: |
Critical security issue: Use of eval() allows arbitrary code execution.
Never use eval() with user input...
---

## 7. Validation Rules

### 7.1 Structural Validation

- File MUST contain metadata section
- File MUST contain template section
- Sections MUST be separated by `---`
- Metadata MUST be valid YAML

### 7.2 Metadata Validation

- All required fields MUST be present
- `version` MUST be "1.0"
- `created` and `modified` MUST be valid ISO 8601 dates
- Parameter types MUST be valid (string, number, boolean, array, object)

### 7.3 Template Validation

- All variables MUST be declared in metadata
- Opening tags MUST have matching closing tags
- Nested conditionals MUST be properly structured
- Loop variables MUST reference array/iterable parameters

### 7.4 Warning Conditions

Validators SHOULD warn about:
- Unused declared variables
- Undeclared variables in template
- Missing examples section
- Missing license field
- Very long templates (>5000 characters)

---

## 8. Execution Model

### 8.1 Processing Steps

1. **Parse**: Load and parse OPRMT file
2. **Validate**: Check structure and syntax
3. **Bind**: Map parameter values to variables
4. **Render**: Process conditionals and loops
5. **Substitute**: Replace variables with values
6. **Execute**: Send rendered prompt to AI model

### 8.2 Parameter Binding

Parameters can be bound from:
- Command-line arguments
- Configuration files
- Environment variables
- Interactive prompts
- API calls

### 8.3 Error Handling

Implementations MUST handle:
- Missing required parameters (MUST error)
- Type mismatches (MUST error)
- Undefined variables (SHOULD warn)
- Malformed syntax (MUST error)

---

## 9. Best Practices

### 9.1 Template Design

- Keep prompts focused and single-purpose
- Use clear, descriptive variable names
- Provide meaningful default values
- Document expected parameter formats
- Include diverse examples

### 9.2 Variable Naming

- Use lowercase with underscores: `user_input`, `max_tokens`
- Avoid abbreviations unless industry-standard
- Be consistent within a template

### 9.3 Documentation

- Write clear descriptions for all parameters
- Explain expected input formats
- Provide context for complex logic
- Include usage examples

### 9.4 Versioning

- Update `modified` date on changes
- Use semantic versioning in `name` for major changes
- Document breaking changes in description

---

## 10. Security Considerations

### 10.1 Input Validation

- Sanitize user inputs before substitution
- Validate parameter types strictly
- Limit string lengths to prevent injection
- Escape special characters as needed

### 10.2 Prompt Injection

- Be aware of prompt injection vulnerabilities
- Use clear delimiters around user input
- Consider using XML/JSON structure for complex inputs
- Validate that substituted values don't break structure

### 10.3 Sensitive Data

- Never include API keys or credentials in templates
- Use environment variables for secrets
- Document which parameters may contain PII
- Consider encryption for sensitive parameters

---

## 11. Interoperability

### 11.1 Model Compatibility

OPRMT is model-agnostic but implementations MAY:
- Use `model_hints` to optimize rendering
- Adjust token limits based on target model
- Transform syntax for model-specific features

### 11.2 Tool Integration

OPRMT files should integrate with:
- Version control systems (Git)
- CI/CD pipelines
- Prompt management platforms
- IDE extensions
- CLI tools

---

## 12. Future Considerations

Reserved for future versions:

- Advanced conditionals (comparison operators)
- Partial templates (includes/imports)
- Built-in functions (string manipulation, date formatting)
- Schema validation for complex objects
- Multi-language support (i18n)
- Prompt chaining and composition
- Performance hints and optimization directives

---

## 13. References

### 13.1 Related Standards

- YAML 1.2 Specification
- ISO 8601 Date Format
- Semantic Versioning 2.0.0
- Handlebars Template Syntax

### 13.2 Resources

- OPRMT GitHub Repository (hypothetical)
- Community Examples Library
- Validator Tools
- IDE Extensions

---

## Appendix A: Grammar

```ebnf
oprmt_file ::= metadata_section template_section [examples_section]

metadata_section ::= "---" NEWLINE yaml_content "---" NEWLINE

template_section ::= text_with_variables ["---" NEWLINE]

examples_section ::= yaml_examples

text_with_variables ::= (TEXT | variable | conditional | loop | comment)*

variable ::= "{{" IDENTIFIER "}}"

conditional ::= "{{#if" IDENTIFIER "}}" text_with_variables ["{{#else}}" text_with_variables] "{{/if}}"

loop ::= "{{#each" IDENTIFIER "}}" text_with_variables "{{/each}}"

comment ::= "{{!" TEXT "!}}" | "{{!--" TEXT "--}}"
Appendix B: MIME Type
Proposed MIME type: application/vnd.oprmt+yaml
Appendix C: Change Log
Version 1.0 (2025-11-17)
Initial specification release
Core metadata structure
Variable substitution syntax
Basic conditionals and loops
Examples format
Validation rules
License
This specification document is released under CC-BY-4.0 (Creative Commons Attribution 4.0 International).
End of Specification
