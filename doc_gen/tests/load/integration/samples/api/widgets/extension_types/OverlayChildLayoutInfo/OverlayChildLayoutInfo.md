# OverlayChildLayoutInfo extension type

The additional layout information available to the[OverlayPortal.overlayChildLayoutBuilder](flutter-docs://api/widgets/OverlayPortal/OverlayPortal.overlayChildLayoutBuilder) callback.

on
- ([Size](flutter-docs://api/dart-ui/Size), [Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4), [Size](flutter-docs://api/dart-ui/Size))

## Properties

[childPaintTransform](flutter-docs://api/widgets/OverlayChildLayoutInfo/childPaintTransform) → [Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4)
The paint transform of [OverlayPortal.child](flutter-docs://api/widgets/OverlayPortal/child), in the target [Overlay](flutter-docs://api/widgets/Overlay)'s
coordinates.


[childSize](flutter-docs://api/widgets/OverlayChildLayoutInfo/childSize) → [Size](flutter-docs://api/dart-ui/Size)
The size of [OverlayPortal.child](flutter-docs://api/widgets/OverlayPortal/child) in its own coordinates.


[overlaySize](flutter-docs://api/widgets/OverlayChildLayoutInfo/overlaySize) → [Size](flutter-docs://api/dart-ui/Size)
The size of the target [Overlay](flutter-docs://api/widgets/Overlay) in its own coordinates.
