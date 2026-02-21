# convert.py PRD

convert.py is a single-file Python script for converting Flutter and Dart documentation files from HTML to markdown.

## Inputs

convert.py must accept the following command line arguments:
- Mandatory --documents {DOC_DIR} or -d {DOC_DIR}, where {DOC_DIR} is an absolute or relative path to the directory containing the HTML documentation to convert
- Mandatory --section {SECTION} or -s {SECTION}, where {SECTION} is the name of the specific documentation section to convert.
- Mandatory --output {OUTPUT_DIR} or -o {OUTPUT_DIR}, where {OUTPUT_DIR} is an absolute or relative path to the directory where the converted markdown files will be saved.
- Optional --verbose or -v, which when present enables verbose logging output.
- Optional --help or -h, which when present displays usage information.

## Outputs

convert.py must place the converted markdown files in the directory {OUTPUT_DIR}/{SECTION}

## Functional Requirements

convert.py will find all files matching the pattern {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html, where {CLASS} is the name of a documented class. If no such files exist, convert.py must print a message indicating that no files were found and exit with a zero status code.

For each HTML file {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html, convert.py must:
1. Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html to markdown.
2. Convert all {DOC_DIR}/flutter/{SECTION}/{CLASS}/*.html to markdown, if any such files exist.
3. Convert all {DOC_DIR}/snippets/{SECTION}.{CLASS}.*.dart to markdown, if any such files exist.
4. Concatenate the converted markdown files in the following order:
   a. {CLASS}-class.html
   b. All files from {CLASS}/*.html in alphabetical order.
   c. All files from snippets/{SECTION}.{CLASS}.*.dart in alphabetical order.
5. Save the concatenated markdown file as {OUTPUT_DIR}/{SECTION}/{CLASS}.md, creating any necessary directories, and overwriting any existing file with the same name.

If the --verbose or -v flag is present, convert.py must:
- Print the name of each file being processed as it is read
- Print a summary of the number of files processed in {SECTION} after all processing is complete

If convert.py completes successfully, it must print a summary indicating the number of {DOC_DIR}/flutter/{SECTION}/{CLASS}-class.html files processed and exit with a zero status code.

**Important**:
- Each HTML file must be converted to markdown by applying a series of transformations as specified in the [HTML Conversion Details](#html-conversion-details) section below.
- Each Dart snippet file must be converted to markdown as specified in the [Dart Snippet Conversion Details](#dart-snippet-conversion-details) section below.

## HTML Conversion Details

convert.py must convert an HTML file to markdown using the `html_to_markdown` package.

After conversion, convert.py must apply the following transformations to the markdown content in the order listed:
1. Remove all lines prior to the first occurence of a heading of any level (i.e., lines starting with `#`).
2. Remove from the line containing the text "1. [Flutter](index.html)" to the end of the file, if any such line exists.
3. Remove all links to other HTML files, if any, replacing them with just the link text. For example, `[SomeClass](SomeClass-class.html)` becomes `SomeClass`.

Each transformation must be implemented as a separate function to support:
- Unit testing of each transformation function.
- Future reuse of transformation functions in other scripts.
- Easy addition, removal, or reordering of transformations.

convert.py should assume and expect that all files are UTF-8 encoded.

## Dart Snippet Conversion Details

When converting Dart snippet files to markdown, convert.py must:
1. Read the contents of the Dart file.
2. Wrap the contents in a markdown header and markdown code block with syntax highlighting for Dart as follows:

````markdown
# Code Snippet

```dart
// Contents of the Dart snippet file
```
````

## html_to_markdown Usage

convert.py should follow this basic usage pattern for `html_to_markdown` which reuses parsed options when converting multiple HTML files to markdown.

```python
from html_to_markdown import ConversionOptions, convert_with_handle, create_options_handle

options_handle = create_options_handle(ConversionOptions())

for html in documents:
    markdown = convert_with_handle(html, options_handle)
```

## Error Handling

convert.py must print a clear and concise error message and exit with a non-zero status code in the following scenarios:
- Missing or invalid command line arguments.
- {DOC_DIR} does not exist or is not a directory.
- {DOC_DIR}/flutter/{SECTION} does not exist or is not a directory.
- {DOC_DIR}/snippets does not exist or is not a directory.
- {OUTPUT_DIR}/{SECTION} cannot be created or is not writable.
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
- Store tests in `make_docs/tests/convert` 
- Within the `make_docs` directory, execute tests with `uv run pytest tests/convert`

## Flutter and Dart Documentation Sample

To aid in development and testing, a small sample of Flutter and Dart documentation HTML files is provided. These sample files are in directory `make_docs/tests/convert/samples`, which represents {DOC_DIR} as used throughout this specification. Subdirectories and files within `samples` mimic the actual structure of Flutter and Dart documentation.

## Dependencies

convert.py has the following dependencies:
- Python 3.12 or later.
- `html_to_markdown` package for HTML to markdown conversion.
- Standard Python libraries for file handling, command line argument parsing, and logging.
- `uv` for project management.
- `pytest` for testing.
- Any additional dependencies must be approved and documented in this PRD before use.
