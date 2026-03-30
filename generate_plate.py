"""Generate a thin test plate OpenSCAD file from Ergogen points output."""
import yaml

PLATE_THICKNESS = 1.5
SWITCH_CUTOUT = 14.0
PLATE_PADDING = 8.0

with open("output/points/points.yaml") as f:
    points = yaml.safe_load(f)

keys = []
for name, data in points.items():
    keys.append((data["x"], data["y"], data["r"]))

# Bounding box
import math
all_x, all_y = [], []
for kx, ky, kr in keys:
    rad = math.radians(kr)
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    for dx, dy in [(-9.525, -9.525), (9.525, -9.525), (9.525, 9.525), (-9.525, 9.525)]:
        all_x.append(dx * cos_a - dy * sin_a + kx)
        all_y.append(dx * sin_a + dy * cos_a + ky)

min_x = min(all_x) - PLATE_PADDING
max_x = max(all_x) + PLATE_PADDING
min_y = min(all_y) - PLATE_PADDING
max_y = max(all_y) + PLATE_PADDING

with open("output/test_plate.scad", "w") as f:
    f.write("// Defiant keyboard test plate - generated from Ergogen points\n\n")
    f.write("$fn = 20;\n\n")
    f.write("difference() {\n")
    f.write(f"    translate([{min_x:.4f}, {min_y:.4f}, 0])\n")
    f.write(f"        cube([{max_x - min_x:.4f}, {max_y - min_y:.4f}, {PLATE_THICKNESS}]);\n\n")
    for name, data in points.items():
        kx, ky, kr = data["x"], data["y"], data["r"]
        f.write(f"    // {name}\n")
        f.write(f"    translate([{kx}, {ky}, -0.5])\n")
        f.write(f"        rotate([0, 0, {kr}])\n")
        f.write(f"            translate([{-SWITCH_CUTOUT/2}, {-SWITCH_CUTOUT/2}, 0])\n")
        f.write(f"                cube([{SWITCH_CUTOUT}, {SWITCH_CUTOUT}, {PLATE_THICKNESS + 1}]);\n")
    f.write("}\n")

print(f"Written to output/test_plate.scad")
print(f"Plate dimensions: {max_x - min_x:.1f} x {max_y - min_y:.1f} x {PLATE_THICKNESS} mm")
print(f"Keys: {len(keys)}")
