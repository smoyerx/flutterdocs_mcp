# convert.py Additional Link Transformations

convert.py is a script for converting Flutter and Dart documentation files from HTML to markdown.

This document specifies updates to convert.py to apply additional link transformations beyond those already implemented in transformations.py (e.g., transform_class_links(), transform_member_links(), etc.).

## Definitions

- {SECTION}: The name of a section in the Flutter/Dart documentation (e.g., "widgets", "foundation", "material", etc.).

## Additional Link Transformations

The link transformation functions below MUST be added to transformations.py and called from apply_transformations() in the order required to achieve the expected outcome.

### Link Transformation: transform_mixin_links()

Replace all links of the form `[{MIXIN_NAME}]({SECTION}/{MIXIN_NAME}-mixin.html)` with `[{MIXIN_NAME}](mcp://flutter/api/{SECTION}/{MIXIN_NAME}`, where `{SECTION}/{MIXIN_NAME}-mixin.html` MUST be a relative URI.

**Important**:
- {MIXIN_NAME} must not include a path separator, otherwise it is not a match.
- {SECTION} must not include a path separator, otherwise it is not a match.

### Link Transformation: transform_constant_links()

Replace all links of the form `[{CONSTANT_NAME}]({SECTION}/{CONSTANT_NAME}-constant.html)` with `[{CONSTANT_NAME}](mcp://flutter/api/{SECTION}/{CONSTANT_NAME}`, where `{SECTION}/{CONSTANT_NAME}-constant.html` MUST be a relative URI.

**Important**:
- {CONSTANT_NAME} must not include a path separator, otherwise it is not a match.
- {SECTION} must not include a path separator, otherwise it is not a match.
- This new function transforms links to root documentation files for constants. This is different from the existing transform_enum_constant_links() function which transforms links to constant members of enums.

### Link Transformation: transform_extension_type_links()

Replace all links of the form `[{EXTENSION_TYPE_NAME}]({SECTION}/{EXTENSION_TYPE_NAME}-extension-type.html)` with `[{EXTENSION_TYPE_NAME}](mcp://flutter/api/{SECTION}/{EXTENSION_TYPE_NAME}`, where `{SECTION}/{EXTENSION_TYPE_NAME}-extension-type.html` MUST be a relative URI.

**Important**:
- {EXTENSION_TYPE_NAME} must not include a path separator, otherwise it is not a match.
- {SECTION} must not include a path separator, otherwise it is not a match.

### Link Transformation: transform_other_root_links()

Replace all links of the form `[{ROOT_DOC_NAME}]({SECTION}/{ROOT_DOC_NAME}.html)` with `[{ROOT_DOC_NAME}](mcp://flutter/api/{SECTION}/{ROOT_DOC_NAME})`, where `{SECTION}/{ROOT_DOC_NAME}.html` MUST be a relative URI.

**Important**:
- {ROOT_DOC_NAME} must not include a path separator, otherwise it is not a match.
- {SECTION} must not include a path separator, otherwise it is not a match.
- This transformation handles links to all **root** documentation files EXCEPT for classes, mixins, constants, and extension types which are handled by the other transformations specified above or already implemented (classes). This transformation must be applied **AFTER** those since it is more general and would otherwise transform links that should be transformed by the other functions.

## Ordering of Link Transformations

Within apply_transformations(), the link transformation functions MUST be called in the following order:
1. transform_class_links() - already implemented
2. transform_mixin_links() - new function specified above
3. transform_constant_links() - new function specified above
4. transform_extension_type_links() - new function specified above
5. transform_other_root_links() - new function specified above
6. transform_enum_constant_links() - already implemented
7. transform_member_links() - already implemented
8. transform_image_links() - already implemented
9. transform_dartpad_links() - already implemented
10. fix_link_spacing() - already implemented

**Important**: As part of the implementation of these new transformations you MUST confirm there are no conflicts in the ordering; i.e., more specific transformations precede more general transformations such that all transformations are applied correctly.

## Additional Validation Work

- Review the existing function transform_class_links() to confirm {CLASS_NAME} and {SECTION} cannot include path separators, and update the implementation if needed to ensure this.
- Review the existing function transform_enum_constant_links() to confirm {CONSTANT}, {SECTION}, and {ENUM} cannot include path separators, and update the implementation if needed to ensure this.
- Review the existing function transform_member_links() to confirm {MEMBER}, {SECTION}, and {ENTITY} cannot include path separators, and update the implementation if needed to ensure this.

## Error Handling

No additional error handling is required for these updates.

## Testing Requirements

Unit tests MUST be added for each of the new link transformation functions specified above. Each unit test MUST verify correct behavior with various input scenarios, including but not limited to:
- Links that match the expected pattern and should be transformed.
- Links that do not match the expected pattern and should NOT be transformed.
  
## Other Notes

- The markdown text being transformed does not reference `*-sidebar.html` files so no special handling is needed to exclude those from these transformations.
- Follow the established patterns in transformations.py and patterns.py for implementing these new functions.
- Follow the established unit testing patterns in test_transformations.py for implementing unit tests for these new functions.
