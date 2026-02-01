# convert.py Categorizations of Documentation Files

convert.py is a script for converting Flutter and Dart documentation files from HTML to markdown. This document specifies updates to convert.py to categorize documentation files and process them accordingly.

## Definitions

- {DOC_DIR}: The root directory containing the HTML documentation files to be converted. Specified as a command line argument to convert.py.
- {SECTION}: The specific documentation section to convert (e.g., "widgets", "foundation", etc.). Specified as a command line argument to convert.py.
- {OUTPUT_DIR}: The directory where the converted markdown files will be saved. Specified as a command line argument to convert.py.

## Categorization of Documentation Files

convert.py CURRENTLY processes only class documentation files, which are identified by the presence of an HTML file named {CLASS}-class.html in the {DOC_DIR}/flutter/{SECTION} directory, where {CLASS} is the name of a documented class. In this document, we will refer to {CLASS}-class.html files as "**primary** class documentation files" because they serve as the main entry point for documentation about {CLASS}, but are not the only files that document {CLASS}.

This document specifies updates to convert.py to identify other types of primary documentation files.

## Goal for these Updates

After these updates, convert.py MUST be able to:
- Group the primary documentation files by the categories defined below.
- Process only the primary class documentation files using the CURRENT logic.

## Primary Documentation File Categories

Some primary documentation files are identified directly by their filenames, while others must be identified indirectly using additional logic.

### Directly Identified Primary Documentation Files

- Primary class documentation files: files named {CLASS}-class.html in the {DOC_DIR}/flutter/{SECTION} directory.
- Primary mixin documentation files: files named {MIXIN}-mixin.html in the {DOC_DIR}/flutter/{SECTION} directory.
- Primary constant documentation files: files named {CONSTANT}-constant.html in the {DOC_DIR}/flutter/{SECTION} directory.
- Primary library documentation files: files named {LIBRARY}-library.html in the {DOC_DIR}/flutter/{SECTION} directory.
- Primary extension type documentation files: files named {EXTENSION_TYPE}-extension-type.html in the {DOC_DIR}/flutter/{SECTION} directory.

### Indirectly Identified Primary Documentation Files

#### Simple Indirect Identification
- Primary enum documentation files: files named {ENUM}.html in the {DOC_DIR}/flutter/{SECTION} directory where there also exists a file named {ENUM}-enum-sidebar.html in the same directory.
- Primary extension documentation files: files named {EXTENSION}.html in the {DOC_DIR}/flutter/{SECTION} directory where there also exists a file named {EXTENSION}-extension-sidebar.html in the same directory.

#### Complex Indirect Identification

- First identify all files named {NAME}.html in the {DOC_DIR}/flutter/{SECTION} directory that:
   - Do NOT fit the pattern `*-sidebar.html`
   - Are NOT already categorized as one of the primary documentation file types listed above (i.e., class, mixin, constant, library, enum, extension, extension type)
- Categorize the files identfied in the previous step as follows:
   - Primary function documentation files: files named {NAME}.html where the first character of {NAME} is a **lower case** alphabetic character
   - Primary typedef documentation files: files named {NAME}.html where the first character of {NAME} is an **upper case** alphabetic character
   
## Error Handling

If convert.py encounters a potential primary documentation file that it cannot categorize it MUST print an informational message containing the filename (inverbose mode) and then ignore that file.

**Important**: Files in {DOC_DIR}/flutter/{SECTION} that fit the pattern `*-sidebar.html` are NEVER primary documentation files and MUST be ignored EXCEPT when indirectly identifying primary documentation files as specified above.


## Testing Requirements

Flutter documentation files representing all of the categories above are in the doc_gen/tests/convert/integration/samples directory to facilitate development and testing.

convert.py tests must be updated to confirm the correct categorization of primary documentation files as defined in this document.
