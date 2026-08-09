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

## Versions

Each hardware revision lives in its own self-contained directory:

- `v1/` — first release (built 2026-04-19): Choc switches, nice!nano v2, no display, ~110 mAh battery
- `v2/` — adds nice!view per-half display, 750 mAh battery, canonical MCU-on-top assembly

All commands below run from inside the version directory you're working on (e.g. `cd v1`).

### v2 assembly notes

- **nice!nano**: socketed via Mill-Max headers, mounted on the **F (top)** side. Bridge the F-side MCU jumpers.
- **Switches, hotswaps, diodes, JST connector, power switch, reset switch**: all on the **B (bottom)** side.
- **Battery**: 750 mAh 403450 LiPo (4 × 34 × 50 mm). Sits below the PCB inside a case cavity — case must accommodate the keep-out.
- **nice!view display**: mounted on F (top), anchored at the same point as the MCU so the display's pin row sits dead-center over the nano body. SPI uses D5/D6/D7 for CS/MOSI/SCK (custom overlay; the upstream `nice_view_adapter` would collide with the matrix columns). Charge status is read off the on-screen battery widget.

## Building

### Prerequisites

- Node.js
- OpenSCAD (for test plate STL export)
- KiCad 8 (for PCB editing)

### Generate Ergogen output

```bash
cd v1
npm install
npx ergogen . -o output --debug
```

### Generate test plate

```bash
cd v1
python3 generate_plate.py
```

Opens `output/test_plate.scad` in OpenSCAD to export STL for 3D printing.

## Project Structure

```
.github/workflows/   # ZMK firmware CI (per-version build job)
freerouting.jar      # Shared autorouter (gitignored)
v1/
  config.yaml        # Ergogen keyboard layout definition
  generate_plate.py  # Test plate generator
  footprints/        # Ergogen footprint submodules (pinned per version)
  firmware/          # ZMK shield + build matrix
  releases/          # Tagged PCB releases
  output/            # Generated files (gitignored)
```

## License

This project is licensed under [CC BY-NC-SA 4.0](LICENSE). You are free to build one for personal use, but commercial sale is not permitted.
