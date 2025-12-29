# convert.py Update

convert.py is a single-file Python script for converting Flutter and Dart documentation files from HTML to markdown. The convert.py script is located in the doc_gen directory of this repository.

This document specifies a set of changes to convert.py to enhance its functionality, improve code organization, and ensure maintainability.

## Definitions

- {DOC_DIR}: The root directory containing the HTML documentation files to be converted. Specified as a command line argument.
- {SECTION}: The specific documentation section to convert (e.g., "widgets", "foundation", etc.). Specified as a command line argument.
- {OUTPUT_DIR}: The directory where the converted markdown files will be saved. Specified as a command line argument.

## Class Documentation Processing

The following describes changes to to how convert.py processes class documentation files, which are identified by the presence of an HTML file named {CLASS}-class.html in the {DOC_DIR}/flutter/{SECTION} directory, where {CLASS} is the name of a documented class.

**Important**:
- The changes described below only apply to processing class documentation files.
- The code for convert.py MUST be structured so that it can be extened to process other types of documentation files in the future without significant refactoring.

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
- When saving any converted markdown file, convert.py MUST create any necessary directories and overwrite any existing file with the same name

#### Step 1: Process the Class File

- Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html to markdown
- Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/{CLASS}.md
- Retain the converted markdown content in memory for use in subsequent steps, which refer to this converted markdown content as {CLASS}.md content

#### Step 2: Process Constructor Files

Scan the constructors section (`## Constructors`) of the {CLASS}.md content for lines that **start** with `[{CONSTRUCTOR}](mcp://flutter/api/{SECTION}/{CLASS}/{CONSTRUCTOR})`, where {CONSTRUCTOR} is the name of a constructor documented for the class. For each such line found:
- Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{CONSTRUCTOR}.html to markdown
- Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/constructors/{CONSTRUCTOR}.md

convert.py MUST print an informational message and continue processing if it:
- Does not find a constructors section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the constructors section of the {CLASS}.md content

convert.py MUST print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern in the constructors section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{CONSTRUCTOR}.html does not exist

#### Step 3: Process or Generate Property Files

Scan the properties section (`## Properties`) of the {CLASS}.md content for lines that **start** with `[{PROPERTY}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{PROPERTY})`, where {PROPERTY} is the name of a property documented for {CLASS}. For each such line found:
- If {SOME_SECTION} is equal to {SECTION} and {SOME_CLASS} is equal to {CLASS} this is a **native** (not inherited) property of {CLASS}:
   - Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{PROPERTY}.html to markdown
   - Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/properties/native/{PROPERTY}.md
- If {SOME_SECTION} is not equal to {SECTION} or {SOME_CLASS} is not equal to {CLASS} this is an **inherited** property of {CLASS}:
   - Capture the {RESULT_TYPE} for the property which is on the same line as the property link, starts with the first non-whitespace charater following the unicode rightwards arrow, and is terminated by a whitespace character or the end of the line
   - Capture the {DESCRIPTION} for the property which is the non-blank lines immediately following the line containing the property link
   - Generate a markdown file as described below and save it as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/properties/inherited/{SOME_SECTION}-{SOME_CLASS}-{PROPERTY}.md

Use the following template to generate the markdown file for an inherited property:
````markdown
# {PROPERTY} property

{RESULT_TYPE} {PROPERTY}

{DESCRIPTION}

This property is inherited from [{SOME_CLASS}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}).
See further details at [{PROPERTY}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{PROPERTY}).
````

convert.py MUST print an informational message and continue processing if it:
- Does not find a properties section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the properties section of the {CLASS}.md content

convert.py MUST print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern for **native** properties in the properties section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{PROPERTY}.html does not exist
- Finds a line matching the specified pattern for **inherited** properties in the properties section of the {CLASS}.md content but is unable to capture the {RESULT_TYPE} or {DESCRIPTION} for the property

#### Step 4: Process or Generate Method Files

Scan the methods section (`## Methods`) of the {CLASS}.md content for lines that **start** with `[{METHOD}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{METHOD})`, where {METHOD} is the name of a method documented for {CLASS}. For each such line found:
- If {SOME_SECTION} is equal to {SECTION} and {SOME_CLASS} is equal to {CLASS} this is a **native** (not inherited) method of {CLASS}:
   - Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html to markdown
   - Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/methods/native/{METHOD}.md
- If {SOME_SECTION} is not equal to {SECTION} or {SOME_CLASS} is not equal to {CLASS} this is an **inherited** method of {CLASS}:
   - Capture the {RESULT_TYPE} for the method which is on the same line as the method link, starts with the first non-whitespace charater following the unicode rightwards arrow, and is terminated by a whitespace character or the end of the line
   - Capture the {DESCRIPTION} for the method which is the non-blank lines immediately following the line containing the method link
   - Generate a markdown file as described below and save it as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/methods/inherited/{SOME_SECTION}-{SOME_CLASS}-{METHOD}.md

Use the following template to generate the markdown file for an inherited method:
````markdown
# {METHOD} method

{RESULT_TYPE} {METHOD}(/* See {SOME_CLASS} documentation for parameters */)

{DESCRIPTION}

This method is inherited from [{SOME_CLASS}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}).
See further details at [{METHOD}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{METHOD}).
````

convert.py MUST print an informational message and continue processing if it:
- Does not find a methods section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the methods section of the {CLASS}.md content

convert.py MUST print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern for **native** methods in the methods section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html does not exist
- Finds a line matching the specified pattern for **inherited** methods in the methods section of the {CLASS}.md content but is unable to capture the {RESULT_TYPE} or {DESCRIPTION} for the method

#### Step 5: Process or Generate Operator Files

Scan the operators section (`## Operators`) of the {CLASS}.md content for lines that **start** with `[{OPERATOR_SYMBOL}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{OPERATOR})`, where {OPERATOR} is the name of an operator documented for {CLASS}. For each such line found:
- If {SOME_SECTION} is equal to {SECTION} and {SOME_CLASS} is equal to {CLASS} this is a **native** (not inherited) operator of {CLASS}:
   - Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{OPERATOR}.html to markdown
   - Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/operators/native/{OPERATOR}.md
- If {SOME_SECTION} is not equal to {SECTION} or {SOME_CLASS} is not equal to {CLASS} this is an **inherited** operator of {CLASS}:
   - Capture the {RESULT_TYPE} for the operator which is on the same line as the operator link, starts with the first non-whitespace charater following the unicode rightwards arrow, and is terminated by a whitespace character or the end of the line
   - Capture the {DESCRIPTION} for the operator which is the non-blank lines immediately following the line containing the operator link
   - Generate a markdown file as described below and save it as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/operators/inherited/{SOME_SECTION}-{SOME_CLASS}-{OPERATOR}.md

Use the following template to generate the markdown file for an inherited operator:
````markdown
# {OPERATOR_SYMBOL} ({OPERATOR}) method

{RESULT_TYPE} {OPERATOR_SYMBOL}(/* See {SOME_CLASS} documentation for parameters */)

{DESCRIPTION}

This operator is inherited from [{SOME_CLASS}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}).
See further details at [{OPERATOR_SYMBOL}](mcp://flutter/api/{SOME_SECTION}/{SOME_CLASS}/{OPERATOR}).
````

convert.py MUST print an informational message and continue processing if it:
- Does not find a operators section in the {CLASS}.md content
- Finds no lines matching the specified pattern in the operators section of the {CLASS}.md content

convert.py MUST print an error message and exit with a non-zero status code if it:
- Finds a line matching the specified pattern for **native** operators in the operators section of the {CLASS}.md content but the corresponding HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}/{OPERATOR}.html does not exist
- Finds a line matching the specified pattern for **inherited** operators in the operators section of the {CLASS}.md content but is unable to capture the {RESULT_TYPE} or {DESCRIPTION} for the operator

#### Step 6: Process Code Snippet Files

For each Dart code snippet file matching the pattern {DOC_DIR}/snippets/{SECTION}.{CLASS}.*.dart:
- Convert the Dart snippet file to markdown
- Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/snippets/{FILENAME}.md, where {FILENAME} is the original Dart filename without the .dart extension

convert.py MUST continue processing without printing any messages if no such files exist.

## HTML Conversion Details

convert.py currently converts HTML files to markdown using the `html_to_markdown` package and MUST continue to do so after the updates specified in this document.

convert.py MUST be updated to apply the following categories of transformations to the markdown content generated by `html_to_markdown`.

convert.py MUST apply transaformations in the following order:
- Cleanup Transformations
- Link Transformations

### Cleanup Transformations

Cleanup transformations remove unwanted content from the markdown content.

convert.py MUST apply the following cleanup transformations to the markdown content in the order listed:
1. Remove all lines prior to the first occurence of a heading of any level (i.e., lines starting with `#`).
2. Remove from the line containing the text "1. [Flutter](index.html)" to the end of the file, if any such line exists.
3. Remove lines that contain only whitespace and exactly one occurence of exactly one of the following strings:
   - "const"
   - "final"
   - "no setterinherited"
   - "finalinherited"
   - "inherited"
   - `[*link*](# "Copy link to clipboard")`

Cleanup transformations MUST be implemented so that they are:
- Easy to unit test individually
- Easy to extend in the future by adding, removing, or reordering transformations

### Link Transformations

Link transformation modify links in the markdown content to:
- Create a consistent URI naming scheme for links to other markdown files in the converted documentation set
- Replace links to resources that are not included in the converted documentation set with a meaningful alternative to avoid confusing LLM and human readers

convert.py MUST apply the following link transformations to the markdown content in the order listed:
1. Replace all links of the form `[{CLASS_NAME}]({SECTION_NAME}/{CLASS_NAME}-class.html)` with `[{CLASS_NAME}](mcp://flutter/api/{SECTION_NAME}/{CLASS_NAME}`, where `{SECTION_NAME}/{CLASS_NAME}-class.html` MUST be a relative URI.
2. Replace all links of the form `[{MEMBER}]({SECTION}/{CLASS}/{MEMBER}.html)` with `[{MEMBER}](mcp://flutter/api/{SECTION}/{CLASS}/{MEMBER})`, where `{SECTION}/{CLASS}/{MEMBER}.html` MUST be a relative URI.
3. Replace all links of the form `![{Link Text}]({IMAGE_PATH})` with `[Image: {Link Text}]`, where {IMAGE_PATH} is any URI (relative or absolute)
4. Replace all links of the form `[{Link Text}]({EXTERNAL_URI})` with `[Note: Interative sample omitted]`, where {EXTERNAL_URI} MUST contain the substring "dartpad.dev"

Link transformations MUST be implemented so that they are:
- Easy to unit test individually
- Easy to extend in the future by adding, removing, or reordering transformations

convert.py MUST print an informaitonal message and continue processing if it encounters a link with a relative URI that does not match any of the patterns specified above.


## Dart Snippet Conversion Details

convert.py MUST be updated to convert a Dart code snippet file {DOC_DIR}/snippets/{SECTION}.{CLASS}.*.dart o markdown as follows:
1. Read the contents of the Dart file.
2. Wrap the contents in a markdown header and markdown code block with syntax highlighting for Dart as follows:

````markdown
# Code Snippet for {CLASS} in {SECTION}

```dart
// Contents of the Dart snippet file
```
````

## html_to_markdown Usage

convert.py MUST continue to follow this basic usage pattern for `html_to_markdown` which reuses parsed options when converting multiple HTML files to markdown.

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
