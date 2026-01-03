# convert.py Update

convert.py is a single-file Python script for converting Flutter and Dart documentation files from HTML to markdown. The convert.py script is located in the doc_gen directory of this repository.

This document specifies a set of changes to convert.py to enhance its functionality, improve code organization, and ensure maintainability.

**Note**: It is NOT a goal to maintain backward compatibility with any previous version of convert.py. The changes specified in this document may significantly alter or replace existing functionality.

## Definitions

- {DOC_DIR}: The root directory containing the HTML documentation files to be converted. Specified as a command line argument.
- {SECTION}: The specific documentation section to convert (e.g., "widgets", "foundation", etc.). Specified as a command line argument.
- {OUTPUT_DIR}: The directory where the converted markdown files will be saved. Specified as a command line argument.

## Class Documentation Processing

The following describes changes to to how convert.py processes class documentation files, which are identified by the presence of an HTML file named {CLASS}-class.html in the {DOC_DIR}/flutter/{SECTION} directory, where {CLASS} is the name of a documented class.

**Important**:
- The changes described below only apply to processing class documentation files, which are the only type of documentation files that convert.py currently processes.
- In the future, convert.py MAY be extended to process other types of documentation files (e.g., Material Design constants, Flutter guides, etc.). To accommodate this possibility, the changes described below are structured to isolate class documentation file processing from any future processing of other types of documentation files and the updated convert.py MUST be implemented accordingly.
- Do NOT preserve any existing behavior of convert.py that is **updated** or **changed** by this document.
- DO preserve any existing behavior of convert.py that is **not** updated or changed by this document.
- DO preserve the overall structure and organization of convert.py as a single-file script.

### CURRENT Class Documentation File Processing Behavior

For each class HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html, convert.py CURRENTLY does the following:
1. Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html to markdown.
2. Convert all {DOC_DIR}/flutter/{SECTION}/{CLASS}/*.html to markdown, if any such files exist.
3. Convert all {DOC_DIR}/snippets/{SECTION}.{CLASS}.*.dart to markdown, if any such files exist.
4. Concatenate the converted markdown files in the following order:
   a. {CLASS}-class.html
   b. All files from {CLASS}/*.html in alphabetical order.
   c. All files from snippets/{SECTION}.{CLASS}.*.dart in alphabetical order.
5. Save the concatenated markdown file as {OUTPUT_DIR}/{SECTION}/{CLASS}.md, creating any necessary directories, and overwriting any existing file with the same name.

In all cases where an HTML file is converted to markdown, convert.py CURRENTLY applies several transformations after the initial conversion.

### UPDATED Class Documentation File Processing Behavior

convert.py must be UPDATED to implement the steps below for processing each class documentation file {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html. If no such files exist, convert.py MUST print a message indicating that no files were found and exit with a zero status code.

**Important**:
- When converting any HTML file to markdown, convert.py MUST apply the transformations specified in the [HTML Conversion Details](#html-conversion-details) section
- When converting any Dart code snippet file to markdown, convert.py MUST apply the transformations specified in the [Dart Snippet Conversion Details](#dart-snippet-conversion-details) section
- When instructed to scan markdown content for lines that **start** with a specific pattern, convert.py MUST ignore leading whitespace characters before the start of the pattern
- When instructed to scan markdown content within a specified section, convert.py MUST only consider lines that appear after the heading for that section (e.g., `## Constructors`) and before the heading for the next section of the same or higher level (e.g., `## Properties` or `# Another Section`)
- When saving any converted markdown file, convert.py MUST create any necessary directories and overwrite any existing file with the same name
- **Distinguishing member definitions from inline references**: Multi-line descriptions for properties, methods, and operators may contain inline references to other members that happen to start a new line. Member definitions can be distinguished from inline references by the presence of a type signature indicator (the unicode rightwards arrow → or U+2192) somewhere on the same line as the member link. Links without arrows on the same line are inline references and should be ignored during member scanning

#### Step 1: Process the Class File

- Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html to markdown
- Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/{CLASS}.md
- Retain the converted markdown content in memory for use in subsequent steps, which refer to this converted markdown content as {CLASS}.md content

#### Step 2: Process Constructor Files

Scan the constructors section (`## Constructors`) of the {CLASS}.md content for lines that **start** with `[{CONSTRUCTOR}](mcp://flutter/api/{SECTION}/{CLASS}/{CONSTRUCTOR})`, where {CONSTRUCTOR} is the name of a constructor documented for the class. For each such line found:
- Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{CONSTRUCTOR}.html to markdown
- Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/constructors/{CONSTRUCTOR}.md

**Note**: Constructor definitions are followed by parameter lists in parentheses, not by arrows and return types, since constructors return instances of the class implicitly. Any link matching the pattern above in the Constructors section should be treated as a constructor definition regardless of whether an arrow appears on the line

convert.py MUST print an informational message (when in verbose mode) and continue processing if it:
- Does not find a constructors section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the constructors section of the {CLASS}.md content

convert.py MUST always print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern in the constructors section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{CONSTRUCTOR}.html does not exist
- Finds a constructor link with a URI scheme that does not match the specified pattern

#### Step 3: Process or Generate Property Files

Scan the properties section (`## Properties`) of the {CLASS}.md content for lines that **start** with `[{PROPERTY}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{PROPERTY})`, where {PROPERTY} is the name of a property documented for {CLASS}. 

**Note**: Property definitions always have an arrow (→) followed by the property type on the same line as the property link. This distinguishes property definitions from inline references to properties that may appear in multi-line descriptions. Only match lines that contain an arrow.

For each such line found:
- If {SOME_SECTION} is equal to {SECTION} and {SOME_CLASS} is equal to {CLASS} this is a **native** (not inherited) property of {CLASS}:
   - Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{PROPERTY}.html to markdown
   - Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/properties/native/{PROPERTY}.md
- If {SOME_SECTION} is not equal to {SECTION} or {SOME_CLASS} is not equal to {CLASS} this is an **inherited** property of {CLASS}:
   - Capture the {RESULT_TYPE} for the property which is on the same line as the property link, starts with the first non-whitespace character following the unicode rightwards arrow (U+2192), and is terminated by a whitespace character or the end of the line
   - Capture the {DESCRIPTION} for the property which is all lines starting with the line immediately following the property link line and ending at the first blank line
   - Generate a markdown file for the inherited property using the template defined below
   - Save the generated markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/properties/inherited/{SOME_SECTION}-{SOME_CLASS}-{PROPERTY}.md

convert.py MUST print an informational message (when in verbose mode) and continue processing if it:
- Does not find a properties section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the properties section of the {CLASS}.md content

convert.py MUST always print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern for **native** properties in the properties section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{PROPERTY}.html does not exist
- Finds a line matching the specified pattern for **inherited** properties in the properties section of the {CLASS}.md content but is unable to capture the {RESULT_TYPE} or {DESCRIPTION} for the property
- Finds a property link with a URI scheme that does not match the specified pattern

##### Template for Inherited Property Markdown File
````markdown
# {PROPERTY} property

{RESULT_TYPE} {PROPERTY}

{DESCRIPTION}

This property is inherited from [{SOME_CLASS}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}).
See further details at [{PROPERTY}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{PROPERTY}).
````

#### Step 4: Process or Generate Method Files

Scan the methods section (`## Methods`) of the {CLASS}.md content for lines that **start** with `[{METHOD}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{METHOD})`, where {METHOD} is the name of a method documented for {CLASS}.

**Note**: Method definitions always have an arrow (→) followed by the return type somewhere on the same line as the method link (the arrow appears after the parameter list). This distinguishes method definitions from inline references to methods that may appear in multi-line descriptions. Only match lines that contain an arrow.

For each such line found:
- If {SOME_SECTION} is equal to {SECTION} and {SOME_CLASS} is equal to {CLASS} this is a **native** (not inherited) method of {CLASS}:
   - Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html to markdown
   - Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/methods/native/{METHOD}.md
- If {SOME_SECTION} is not equal to {SECTION} or {SOME_CLASS} is not equal to {CLASS} this is an **inherited** method of {CLASS}:
   - Capture the {RESULT_TYPE} for the method which is on the same line as the method link, starts with the first non-whitespace character following the unicode rightwards arrow (U+2192), and is terminated by a whitespace character or the end of the line
   - Capture the {DESCRIPTION} for the method which is all lines starting with the line immediately following the method link line and ending at the first blank line
   - Generate a markdown file for the inherited method using the template defined below
   - Save the generated markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/methods/inherited/{SOME_SECTION}-{SOME_CLASS}-{METHOD}.md

convert.py MUST print an informational message (when in verbose mode) and continue processing if it:
- Does not find a methods section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the methods section of the {CLASS}.md content

convert.py MUST always print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern for **native** methods in the methods section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html does not exist
- Finds a line matching the specified pattern for **inherited** methods in the methods section of the {CLASS}.md content but is unable to capture the {RESULT_TYPE} or {DESCRIPTION} for the method
- Finds a method link with a URI scheme that does not match the specified pattern

##### Template for Inherited Method Markdown File
````markdown
# {METHOD} method

{RESULT_TYPE} {METHOD}(/* See {SOME_CLASS} documentation for parameters */)

{DESCRIPTION}

This method is inherited from [{SOME_CLASS}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}).
See further details at [{METHOD}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{METHOD}).
````

#### Step 5: Process or Generate Operator Files

**Note**: In this section
- {OPERATOR_SYMBOL} refers to the link text for an operator, e.g., `operator ==`
- {OPERATOR} refers to the URI text for an operator, e.g., `operator_equals`
- The text for {OPERATOR_SYMBOL} and {OPERATOR} are in the {CLASS}.md content and so no programmatic mapping between the two is required

Scan the operators section (`## Operators`) of the {CLASS}.md content for lines that **start** with `[{OPERATOR_SYMBOL}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{OPERATOR})`, where {OPERATOR} is the name of an operator documented for {CLASS}.

**Note**: Operator definitions always have an arrow (→) followed by the return type somewhere on the same line as the operator link (the arrow appears after the parameter list). This distinguishes operator definitions from inline references to operators that may appear in multi-line descriptions. Only match lines that contain an arrow.

For each such line found:
- If {SOME_SECTION} is equal to {SECTION} and {SOME_CLASS} is equal to {CLASS} this is a **native** (not inherited) operator of {CLASS}:
   - Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{OPERATOR}.html to markdown
   - Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/operators/native/{OPERATOR}.md
- If {SOME_SECTION} is not equal to {SECTION} or {SOME_CLASS} is not equal to {CLASS} this is an **inherited** operator of {CLASS}:
   - Capture the {RESULT_TYPE} for the operator which is on the same line as the operator link, starts with the first non-whitespace character following the unicode rightwards arrow (U+2192), and is terminated by a whitespace character or the end of the line
   - Capture the {DESCRIPTION} for the operator which is all lines starting with the line immediately following the operator link line and ending at the first blank line
   - Generate a markdown file for the inherited operator using the template defined below
   - Save the generated markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/operators/inherited/{SOME_SECTION}-{SOME_CLASS}-{OPERATOR}.md

convert.py MUST print an informational message (when in verbose mode) and continue processing if it:
- Does not find a operators section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the operators section of the {CLASS}.md content

convert.py MUST always print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern for **native** operators in the operators section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{OPERATOR}.html does not exist
- Finds a line matching the specified pattern for **inherited** operators in the operators section of the {CLASS}.md content but is unable to capture the {RESULT_TYPE} or {DESCRIPTION} for the operator
- Finds an operator link with a URI scheme that does not match the specified pattern

##### Template for Inherited Operator Markdown File
````markdown
# {OPERATOR_SYMBOL} ({OPERATOR}) method

{RESULT_TYPE} {OPERATOR_SYMBOL}(/* See {SOME_CLASS} documentation for parameters */)

{DESCRIPTION}

This operator is inherited from [{SOME_CLASS}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}).
See further details at [{OPERATOR_SYMBOL}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{OPERATOR}).
````

#### Step 6: Process Static Method Files

**Note**:
- Static methods have no inherited variant since static members belong to the declaring class only.
- Many classes do not have any static methods.

Scan the static methods section (`## Static Methods`) of the {CLASS}.md content for lines that **start** with `[{METHOD}](mcp://flutter/api/{SECTION}/{CLASS}/{METHOD})`, where {METHOD} is the name of a static method documented for {CLASS}. For each such line found:
- Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html to markdown
- Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/statics/{METHOD}.md

convert.py MUST continue processing without printing any messages if it:
- Does not find a static methods section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the static methods section of the {CLASS}.md content

convert.py MUST always print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern for static methods in the static methods section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html does not exist
- Finds a static method link with a URI scheme that does not match the specified pattern


#### Step 7: Process Code Snippet Files

For each Dart code snippet file matching the pattern {DOC_DIR}/snippets/{SECTION}.{CLASS}.*.dart:
- Convert the Dart snippet file to markdown
- Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/snippets/{SHORT_NAME}.md, where {SHORT_NAME} is the original Dart filename without the `{SECTION}.{CLASS}.` prefix and without the `.dart` extension

convert.py MUST continue processing without printing any messages if no such files exist.

## HTML Conversion Details

convert.py currently converts HTML files to markdown using the `html_to_markdown` package and MUST continue to do so after the updates specified in this document.

convert.py MUST be updated to apply the following categories of transformations to the markdown content generated by `html_to_markdown` in the order:
- Cleanup Transformations
- Link Transformations

### Cleanup Transformations

Cleanup transformations remove unwanted or extraneous text from the markdown content.

convert.py MUST apply the following cleanup transformations to the markdown content in the order listed:
1. Remove all lines prior to the first occurrence of a heading of any level (i.e., lines starting with `#`).
   - This is remove_header() in the current implementation of convert.py, which MUST be retained unchanged
2. Remove from the line containing the text "1. [Flutter](index.html)" to the end of the file, if any such line exists
   - This is remove_footer() in the current implementation of convert.py, which MUST be retained unchanged
3. Remove lines that contain only whitespace **and** exactly one occurrence of exactly one of the following strings:
   - "const"
   - "final"
   - "no setterinherited"
   - "finalinherited"
   - "inherited"
   - `[*link*](# "Copy link to clipboard")`

**Important**:
- The last element in the list above (`[*link*](# "Copy link to clipboard")`) is a literal string and NOT a regular expression pattern
- remove_html_links() in the current implementation of convert.py MUST be removed and NOT retained
- Cleanup transformations MUST be implemented so that they are easy to unit test individually, similar to the current implementation of convert.py.

### Link Transformations

Link transformation modify links in the markdown content to:
- Create a consistent URI naming scheme for links to other markdown files in the converted documentation set
- Replace links to resources that are not included in the converted documentation set with a meaningful alternative to avoid confusing LLM and human readers

convert.py MUST apply the following link transformations to the markdown content in the order listed:
1. Replace all links of the form `[{CLASS_NAME}]({SECTION_NAME}/{CLASS_NAME}-class.html)` with `[{CLASS_NAME}](mcp://flutter/api/{SECTION_NAME}/{CLASS_NAME}`, where `{SECTION_NAME}/{CLASS_NAME}-class.html` MUST be a relative URI.
2. Replace all links of the form `[{MEMBER}]({SECTION}/{CLASS}/{MEMBER}.html)` with `[{MEMBER}](mcp://flutter/api/{SECTION}/{CLASS}/{MEMBER})`, where `{SECTION}/{CLASS}/{MEMBER}.html` MUST be a relative URI.
3. Replace all links of the form `![{Link Text}]({IMAGE_PATH})` with `[Note: Image {Link Text} omitted]`, where {IMAGE_PATH} is any URI (relative or absolute)
4. Replace all links of the form `[{Link Text}]({EXTERNAL_URI})` with `[Note: Interactive sample omitted]`, where {EXTERNAL_URI} MUST contain the substring "dartpad.dev"

Link transformations MUST be implemented so that they are easy to unit test individually, similar to the current implementation of cleanup transformations in convert.py.

convert.py MUST print an informational message (when in verbose mode) and continue processing if it encounters a link with a relative URI that does not match any of the patterns specified above.


## Dart Snippet Conversion Details

convert.py MUST be updated to convert a Dart code snippet file {DOC_DIR}/snippets/{SECTION}.{CLASS}.*.dart to markdown as follows:
1. Read the contents of the Dart file.
2. Wrap the contents in a markdown header and markdown code block with syntax highlighting for Dart as follows:

````markdown
# Code Snippet for {CLASS} in {SECTION}

```dart
// Contents of the Dart snippet file
```
````

## html_to_markdown Usage

convert.py MUST **continue** to follow this basic usage pattern for `html_to_markdown` which reuses parsed options to increase efficiency when converting multiple HTML files to markdown.

```python
from html_to_markdown import ConversionOptions, ConversionOptionsHandle, convert_with_handle, create_options_handle

options_handle = create_options_handle(ConversionOptions())

for html in documents:
    markdown = convert_with_handle(html, options_handle)
```

## Error Handling

convert.py MUST continue or be updated to print a clear and concise error message and exit with a non-zero status code in the following scenarios:
- Missing or invalid command line arguments.
- {DOC_DIR} does not exist or is not a directory.
- {DOC_DIR}/flutter/{SECTION} does not exist or is not a directory.
- {DOC_DIR}/snippets does not exist or is not a directory.
- {OUTPUT_DIR}/api/{SECTION} cannot be created or is not writable. Note: this is the only UPDATE in this list.
- Any HTML file that is expected to be converted does not exist.
- Any unexpected error during file reading, writing, or conversion.

## Logging and Verbose Mode

- Where this specification requires convert.py to print an informaitional message use logging.info()
- Where this specification requires convert.py to print an error message use logging.error()
- convert.py MUST include a command line argument `--verbose` that enables verbose logging when specified. When in verbose mode, convert.py MUST print informational messages as specified throughout this document.
- convert.py MUST always print error messages regardless of whether verbose mode is enabled.

## Performance Requirements

convert.py is not performance critical. Files should be processed sequentially for simplicity and readability. However, convert.py should handle large documentation sets (e.g., thousands of files) without excessive memory usage or crashes.

## Testing Requirements

convert.py must include the following tests:
- Unit tests for each transformation function, verifying correct behavior with various input scenarios.
- Integration tests that simulate the full conversion process with a small set of sample HTML files, verifying correct output markdown files.
- Error handling tests that verify appropriate error messages and exit codes for various failure scenarios.

Test fixtures:
- Sample HTML files representing Flutter and Dart documentation, as described in the [Flutter and Dart Documentation Sample](#flutter-and-dart-documentation-sample) section below.

Test organization and execution:
- Store tests in `doc_gen/tests/convert` 
- Within the `doc_gen` directory, execute tests with `uv run pytest tests/convert`

**Note**: Testing MUST adhere to the following guidelines:
- Preserve the existing organization of test files in the `doc_gen/tests/convert` directory
- Update existing tests as necessary to accommodate the changes specified in this document
- Add new tests as necessary to cover all new functionality specified in this document

## Flutter and Dart Documentation Sample

To aid in development and testing, a small sample of Flutter and Dart documentation HTML files is provided. These sample files are in directory `doc_gen/tests/convert/samples`, which represents {DOC_DIR} as used throughout this specification. Subdirectories and files within `samples` mimic the actual structure of Flutter and Dart documentation.

## Dependencies

convert.py has the following dependencies:
- Python 3.12 or later.
- `html_to_markdown` package for HTML to markdown conversion.
- Standard Python libraries for file handling, command line argument parsing, and logging.
- `uv` for project management.
- `pytest` for testing.
- Any additional dependencies must be approved and documented in this PRD before use.
