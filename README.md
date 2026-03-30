# Defiant

A 36-key wireless split keyboard inspired by the ZSA Voyager and GEIST Totem.

## Design Goals

- 36 keys (5 columns x 3 rows + 1 side key + 2 thumb keys per half)
- MX key spacing (19.05mm)
- Choc switches with hotswap sockets
- Wireless split via Seeed XIAO nRF52840
- ZMK firmware
- 3D printed case
- Ergogen-generated PCB

## Layout

The main matrix uses a Voyager-inspired column stagger with a Totem-style outer side key. The thumb cluster is a 2-key rotated cluster.

## Building

### Prerequisites

- Node.js
- OpenSCAD (for test plate STL export)
- KiCad 8 (for PCB editing)

### Generate Ergogen output

```bash
npm install
npx ergogen config.yaml -o output --debug
```

### Generate test plate

```bash
python3 generate_plate.py
```

Opens `output/test_plate.scad` in OpenSCAD to export STL for 3D printing.

## Project Structure

```
config.yaml          # Ergogen keyboard layout definition
generate_plate.py    # Test plate generator (reads Ergogen output)
output/              # Generated files (not tracked in git)
```

## License

This project is licensed under [CC BY-NC-SA 4.0](LICENSE). You are free to build one for personal use, but commercial sale is not permitted.
