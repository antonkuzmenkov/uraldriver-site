#!/usr/bin/env python3
"""
Генерация картинок для uraldriver.ru через Gemini Imagen 3 API.

Установка:
    pip install google-genai pillow

Использование:
    export GEMINI_API_KEY="AIzaSy..."  # https://aistudio.google.com/app/apikey
    python3 scripts/generate_images.py

Стоимость: $0.04 / картинка × 5 = $0.20
Время: ~30 секунд
"""

import os
import sys
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("ERROR: pip install google-genai", file=sys.stderr)
    sys.exit(1)

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("ERROR: export GEMINI_API_KEY=AIzaSy... (https://aistudio.google.com/app/apikey)", file=sys.stderr)
    sys.exit(1)

OUT_DIR = Path(__file__).parent.parent / "static" / "img" / "v3_2"
OUT_DIR.mkdir(parents=True, exist_ok=True)

STYLE = (
    "aerospace HUD telemetry interface, dark background #0d1525, "
    "neon accents (cyan #3aa0ff, green #7dffb3, red #ff6b6b, amber #f5b400), "
    "thin 2px lines with subtle glow, monospace font (JetBrains Mono / Roboto Mono), "
    "thin dashed grid #1f3358, light grey text #a8b9d6, "
    "minimalist 2D infographic, no photorealism, no 3D, "
    "all text in Latin only (no Cyrillic), 16:9 aspect ratio. "
)

IMAGES = [
    ("05_starship_matrix.png", STYLE + (
        "Title 'STARSHIP vs URAL-DRIVER // MARKET POSITIONING'. "
        "2x2 matrix: X-axis 'Cargo type' (sensitive payloads -> bulk commodities), "
        "Y-axis 'Mission cadence' (one-shot -> continuous flow). "
        "Bottom-left quadrant: 'STARSHIP TERRITORY' (people, telescopes, complex satellites) in amber. "
        "Top-right quadrant: 'URAL-DRIVER ZONE' (water, LOX, metals, propellant) in cyan-green. "
        "Bottom caption: 'Starship = freight truck. Ural-Driver = railway. Different infrastructure, not competitors.'"
    )),
    ("06_roadmap_7_phases.png", STYLE + (
        "Title 'URAL-DRIVER ROADMAP // 7 PHASES, 2026-2055+'. "
        "Horizontal timeline diagram. Each phase is a colored block on time axis: "
        "Phase 0 Concept (2026-2028) $0.12B grey, "
        "Phase 0.5 Prometheus-RF Lab (2027-2030) $300-450M cyan with star 'highest ROI', "
        "Phase 1 Demonstrator (2028-2033) $2.5B light-blue, "
        "Phase 2 Construction (2033-2040) $18B green, "
        "Phase 3 Flight tests (2040-2045) $7B amber, "
        "Phase 4 Earth ops (2045+) OPEX orange, "
        "Phase 5 Lunar mass driver (2045+) $11-16B purple with moon icon. "
        "Top right: 'TOTAL CAPEX = $30B Earth + $11-16B RUS Lunar share'."
    )),
    ("07_velocity_waterfall.png", STYLE + (
        "Title 'VELOCITY WATERFALL // TUNNEL TO ORBIT'. "
        "Waterfall chart: X-axis stages of flight, Y-axis velocity 0 to 8 km/s. "
        "Stages with bars and km/s values: "
        "T+0 start 0, "
        "T+32 end of LSM +2.5 = 2.5 km/s (cyan large bar), "
        "Helium buffer drag -0.05 = 2.45 (red mini bar), "
        "Membrane+FAV losses -0.15 = 2.30 (red mini bar), "
        "Atmosphere drag (1700m to 30km) -0.80 = 1.50 (red bar), "
        "Scramjet boost Mach 7-22 +5.00 = 6.50 (green large bar), "
        "Final solid stage +1.30 = 7.80 km/s (green bar), "
        "Target LEO orbit 7.80 (horizontal dashed line). "
        "Numerical values above each bar."
    )),
    ("08_gun_detail_v3_2.png", STYLE + (
        "Title 'MUZZLE INTERFACE // HELIUM BUFFER + KEVLAR + FAV'. "
        "Side view, sectional cut of last 2.5 km of magnet barrel: "
        "Left zone (T+30): evacuated barrel (vacuum 5e-3 Pa), capsule in flight (small bullet shape). "
        "Center zone (T+32 to T+32.5): helium buffer 2 km with pressure gradient 0.01 atm to 0.1 atm to 1 atm "
        "shown as color gradient (deep blue -> cyan -> white). "
        "Right zone after muzzle: replaceable kevlar membrane and Fast-Acting Valve (FAV) closing synchronously. "
        "Beyond: atmosphere at 1700 m elevation. "
        "Arrow callouts: 'Mach 7.3 -> 2.45', 'q / 7 (22 -> 3.3 MPa)', "
        "'T_stagnation 4830 -> 902 K', 'PICA nominal 4.1 MW/m^2', 'He recycled, ~$3000/launch'. "
        "Top-right comparison table: 'v1: 6.5 km/s vacuum->atm = death' vs "
        "'v3.2: 2.5 km/s gentle He buffer = survivable'."
    )),
    ("09_flight_profile.png", STYLE + (
        "Title 'FLIGHT PROFILE // T+0 to T+270 sec'. "
        "Three-axis chart over time T+0 to T+270 seconds: "
        "Left Y-axis altitude (km) 0 to 110, "
        "Right Y-axis 1 velocity (km/s) 0 to 8, "
        "Right Y-axis 2 acceleration (g) 0 to 9 as inset strip. "
        "Vertical event markers with labels: "
        "T+0 'LSM start, 8 g sustained', "
        "T+32 'End of LSM, 2.5 km/s', "
        "T+32.5 'Membrane pierce, 4.5 g spike 0.5s', "
        "T+33 'Atmosphere 1700 m, PICA active', "
        "T+60 'Scramjet ignition, Mach 7', "
        "T+200 'Scramjet cutoff, Mach 22, 6.5 km/s', "
        "T+270 'Solid stage cutoff, 7.8 km/s, orbit'. "
        "Curves: altitude blue (rises 1.7 to 100 km parabola), "
        "velocity green (rises 0 to 7.8 km/s in steps), "
        "acceleration red dashed (8g flat plateau, then 4.5g spike, then 1g cruise)."
    )),
]


def main():
    client = genai.Client(api_key=API_KEY)
    print(f"Generating {len(IMAGES)} images via Imagen 3 to {OUT_DIR}\n")

    for idx, (filename, prompt) in enumerate(IMAGES, 1):
        out_path = OUT_DIR / filename
        print(f"[{idx}/{len(IMAGES)}] {filename} ...", end=" ", flush=True)
        try:
            response = client.models.generate_images(
                model="imagen-3.0-generate-002",
                prompt=prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio="16:9",
                    safety_filter_level="block_only_high",
                ),
            )
            if not response.generated_images:
                print("FAIL: empty response")
                continue
            img_bytes = response.generated_images[0].image.image_bytes
            out_path.write_bytes(img_bytes)
            print(f"OK ({len(img_bytes)//1024} KB)")
        except Exception as e:
            print(f"FAIL: {e}")

    print(f"\nDone. Files: ls -la {OUT_DIR}")


if __name__ == "__main__":
    main()
