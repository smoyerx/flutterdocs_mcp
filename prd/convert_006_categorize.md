# convert.py Categorizations of Documentation Files

convert.py is a script for converting Flutter and Dart documentation files from HTML to markdown. This document specifies updates to convert.py to categorize documentation files and process them accordingly.

## Definitions

- {DOC_DIR}: The root directory containing the HTML documentation files to be converted. Specified as a command line argument to convert.py.
- {SECTION}: The specific documentation section to convert (e.g., "widgets", "foundation", etc.). Specified as a command line argument to convert.py.

## Categorization of Documentation Files

convert.py CURRENTLY processes only class documentation files, which are identified by the presence of an HTML file named {CLASS}-class.html in the {DOC_DIR}/flutter/{SECTION} directory, where {CLASS} is the name of a documented class. In this document, we will refer to {CLASS}-class.html files as "**root** class documentation files" because they serve as the main entry point for documentation about {CLASS}, but are not the only files that document {CLASS}.

This document specifies updates to convert.py to identify other types of root documentation files.

## Root Documentation File Categories

Some root documentation files are identified directly by their filenames, while others must be identified indirectly using additional logic.

### Directly Identified Root Documentation Files

- Root class documentation files: files named {CLASS}-class.html in the {DOC_DIR}/flutter/{SECTION} directory.
- Root mixin documentation files: files named {MIXIN}-mixin.html in the {DOC_DIR}/flutter/{SECTION} directory.
- Root constant documentation files: files named {CONSTANT}-constant.html in the {DOC_DIR}/flutter/{SECTION} directory.
- Root library documentation files: files named {LIBRARY}-library.html in the {DOC_DIR}/flutter/{SECTION} directory.
- Root extension type documentation files: files named {EXTENSION_TYPE}-extension-type.html in the {DOC_DIR}/flutter/{SECTION} directory.

### Indirectly Identified Root Documentation Files

#### Simple Indirect Identification
- Root enum documentation files: files named {ENUM}.html in the {DOC_DIR}/flutter/{SECTION} directory where there also exists a file named {ENUM}-enum-sidebar.html in the same directory.
- Root extension documentation files: files named {EXTENSION}.html in the {DOC_DIR}/flutter/{SECTION} directory where there also exists a file named {EXTENSION}-extension-sidebar.html in the same directory.

#### Complex Indirect Identification

- First identify all files named {NAME}.html in the {DOC_DIR}/flutter/{SECTION} directory that:
   - Do NOT fit the pattern `*-sidebar.html`
   - Are NOT already categorized as one of the root documentation file types listed above (i.e., class, mixin, constant, library, enum, extension, extension type)
- Categorize the files identified in the previous step as follows:
   - Root function documentation files: files named {NAME}.html where the first character of {NAME} is a **lower case** alphabetic character
   - Root typedef documentation files: files named {NAME}.html where the first character of {NAME} is an **upper case** alphabetic character
   
## Error Handling

If convert.py encounters a potential root documentation file ({DOC_DIR}/flutter/{SECTION}/*.html) that it cannot categorize as specified above it MUST print an informational message containing the filename (in verbose mode) and then ignore that file.

**Important**: Files in {DOC_DIR}/flutter/{SECTION} that fit the pattern `*-sidebar.html` are NEVER root documentation files and MUST be ignored EXCEPT when indirectly identifying root documentation files as specified above.

## Update convert.py

convert.py MUST be updated to implement the categorization logic specified in this document. The existing logic for processing root class documentation files MUST remain unchanged.

Currently, convert.cli calls find_class_files() to identify root class documentation files, and then calls process_class() to process each.

After these updates, convert.cli MUST:
- Call a new function to identify all root documentation files in {DOC_DIR}/flutter/{SECTION}, categorize them according to the logic specified in this document, and return a dictionary mapping categories to lists of files.
- Call process_class() only for root class documentation files identified in the previous step.
- Call a new function to process each of the other categories of root documentation files (one function per category), where each of these new functions simply returns without performing any processing. Continue using the established naming convention of process_{CATEGORY}() for these new functions.

## Testing Requirements

convert.py tests must be updated to confirm the correct categorization of root documentation files in doc_gen/tests/convert/integration/samples/flutter/material and doc_gen/tests/convert/integration/samples/flutter/widgets as specified below.

Categorization of root documentation files in doc_gen/tests/convert/integration/samples/flutter/material:
- Root class documentation files: InkWell-class.html, ListTile-class.html
- Root mixin documentation files: BaseSliderTrackShape-mixin.html, MaterialStateMixins-mixin.html
- Root constant documentation files: accelerateEasing-constant.html, kBottomNavigationBarHeight-constant.html
- Root library documentation files: material-library.html
- Root enum documentation files: HourFormat.html, StretchMode.html
- Root function documentation files: showBottomSheet.html, showMenu.html
- Root typedef documentation files: DrawerCallback.html

Categorization of root documentation files in doc_gen/tests/convert/integration/samples/flutter/widgets:
- Root class documentation files: State-class.html, Text-class.html
- Root extension documentation files: WidgetStateOperators.html
- Root extension type documentation files: OverlayChildLayoutInfo-extension-type.html
