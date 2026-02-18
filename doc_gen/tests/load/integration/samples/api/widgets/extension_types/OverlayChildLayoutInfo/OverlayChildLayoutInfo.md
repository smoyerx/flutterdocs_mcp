# OverlayChildLayoutInfo extension type

The additional layout information available to the[OverlayPortal.overlayChildLayoutBuilder](mcp://flutter/api/widgets/OverlayPortal/OverlayPortal.overlayChildLayoutBuilder) callback.

on
- ([Size](mcp://flutter/api/dart-ui/Size), [Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4), [Size](mcp://flutter/api/dart-ui/Size))

## Properties

[childPaintTransform](mcp://flutter/api/widgets/OverlayChildLayoutInfo/childPaintTransform) → [Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4)
The paint transform of [OverlayPortal.child](mcp://flutter/api/widgets/OverlayPortal/child), in the target [Overlay](mcp://flutter/api/widgets/Overlay)'s
coordinates.


[childSize](mcp://flutter/api/widgets/OverlayChildLayoutInfo/childSize) → [Size](mcp://flutter/api/dart-ui/Size)
The size of [OverlayPortal.child](mcp://flutter/api/widgets/OverlayPortal/child) in its own coordinates.


[overlaySize](mcp://flutter/api/widgets/OverlayChildLayoutInfo/overlaySize) → [Size](mcp://flutter/api/dart-ui/Size)
The size of the target [Overlay](mcp://flutter/api/widgets/Overlay) in its own coordinates.
