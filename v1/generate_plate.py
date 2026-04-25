"""Generate a 3D-printable plate from Ergogen board outline and switch positions."""
import yaml
import math

PLATE_THICKNESS = 1.5
SWITCH_CUTOUT = 14.0

# Read board outline polygon points
with open("output/outlines/board.yaml") as f:
    board_data = yaml.safe_load(f)

# Read key positions
with open("output/points/points.yaml") as f:
    points = yaml.safe_load(f)

# Extract board polygon vertices from the YAML
# board.yaml contains the outline as a list of [x, y] points
board_points = board_data

with open("output/plate.scad", "w") as f:
    f.write("// Defiant keyboard plate - board outline with switch cutouts\n\n")
    f.write("$fn = 30;\n\n")
    f.write("difference() {\n")

    # Board outline as extruded polygon
    f.write("    // Board outline\n")
    f.write(f"    linear_extrude(height = {PLATE_THICKNESS})\n")
    f.write(f"        import(\"outlines/plate.dxf\");\n")

    f.write("}\n")

print(f"Written to output/plate.scad")
print(f"Keys: {len(points)}")
print(f"Uses output/outlines/plate.dxf (board with switch cutouts)")
print(f"Open in OpenSCAD, render (F6), export STL")
