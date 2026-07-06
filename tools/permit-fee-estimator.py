#!/usr/bin/env python3
"""
Florida HVAC Permit Fee Estimator

Estimates permit fees for common HVAC jobs in South Florida's three
most populous counties: Miami-Dade, Broward, and Palm Beach.

Usage:
    python3 tools/permit-fee-estimator.py

No dependencies beyond Python 3.6+ standard library.
"""

import sys
from typing import Dict, List, Optional


def print_header(text: str) -> None:
    """Print a section header with decorative border."""
    width = min(60, max(len(text) + 4, 40))
    print(f"\n{'=' * width}")
    print(f"  {text}")
    print(f"{'=' * width}\n")


def ask_yes_no(prompt: str) -> bool:
    """Ask a yes/no question and return the result."""
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("  Please enter 'y' or 'n'.")


def ask_choice(prompt: str, options: Dict[str, str]) -> str:
    """Ask the user to pick from a dictionary of options. Returns the key."""
    print(f"\n{prompt}")
    for key, label in options.items():
        print(f"  [{key}] {label}")
    while True:
        choice = input("Enter choice: ").strip().lower()
        if choice in options:
            return choice
        print(f"  Invalid choice. Pick from: {', '.join(options.keys())}")


def ask_int(prompt: str, default: Optional[int] = None) -> int:
    """Ask for a whole number with optional default."""
    while True:
        prompt_text = f"{prompt} [{default}] " if default is not None else f"{prompt} "
        response = input(prompt_text).strip()
        if not response and default is not None:
            return default
        try:
            value = int(response)
            if value < 0:
                print("  Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("  Please enter a whole number.")


def ask_float(prompt: str, default: Optional[float] = None) -> float:
    """Ask for a dollar amount with optional default."""
    while True:
        prompt_text = f"{prompt} [{default}] " if default is not None else f"{prompt} "
        response = input(prompt_text).strip()
        if not response and default is not None:
            return default
        try:
            value = float(response.replace(",", "").replace("$", ""))
            if value < 0:
                print("  Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("  Please enter a valid number.")


# ── Fee schedule data ──
# These baselines are as of mid-2026. Fees change annually — always verify
# with the actual building department before pulling permits.

FEE_SCHEDULES = {
    "miami-dade": {
        "name": "Miami-Dade County",
        "url": "https://www.miamidade.gov/building/",
        "base_permits": {
            "ac_replace": {"desc": "AC replacement (same tonnage)", "base_fee": 165, "variable": "tonnage"},
            "ac_new": {"desc": "New AC installation", "base_fee": 200, "variable": "tonnage"},
            "duct_mod": {"desc": "Duct modification (>25 sq ft)", "base_fee": 95, "variable": None},
            "gas_furnace": {"desc": "Gas furnace replacement", "base_fee": 120, "variable": "btu"},
            "heat_pump": {"desc": "Heat pump installation", "base_fee": 200, "variable": "tonnage"},
        },
        "tonnage_fee": 30,      # per ton
        "btu_fee": 0.01,        # per BTU over baseline
        "plan_review": 85,      # flat plan review fee
        "surcharges": [
            ("School Board Tax", 12.50, True),
            ("Administrative Fee", 15.00, True),
            ("ERecording Fee", 8.50, True),
        ],
        "expedited": False,       # Miami-Dade doesn't offer express HVAC permits
        "notes": (
            "Miami-Dade requires a Notice of Acceptance (NOA) for all AC equipment. "
            "Verify the unit model is on the approved list before applying. "
            "Additional fees apply for work in the High Velocity Hurricane Zone (HVHZ)."
        ),
    },
    "broward": {
        "name": "Broward County",
        "url": "https://www.broward.org/Permitting/",
        "base_permits": {
            "ac_replace": {"desc": "AC replacement (same tonnage)", "base_fee": 125, "variable": "tonnage"},
            "ac_new": {"desc": "New AC installation", "base_fee": 155, "variable": "tonnage"},
            "duct_mod": {"desc": "Duct modification (>25 sq ft)", "base_fee": 75, "variable": None},
            "gas_furnace": {"desc": "Gas furnace replacement", "base_fee": 100, "variable": "btu"},
            "heat_pump": {"desc": "Heat pump installation", "base_fee": 155, "variable": "tonnage"},
        },
        "tonnage_fee": 22,
        "btu_fee": 0.008,
        "plan_review": 65,
        "surcharges": [
            ("County Surcharge", 10.00, True),
            ("Administrative Fee", 12.00, True),
            ("Fire Review (if gas)", 45.00, False),
        ],
        "expedited": True,
        "expedited_fee": 95,
        "notes": (
            "Broward allows expedited permitting for same-tonnage replacements — "
            "typically same-day if no plan review is needed. Municipalities within "
            "Broward (Fort Lauderdale, Hollywood, Pembroke Pines) may have separate "
            "fee schedules; this reflects unincorporated Broward County."
        ),
    },
    "palm-beach": {
        "name": "Palm Beach County",
        "url": "https://discover.pbcgov.org/pzb/building/",
        "base_permits": {
            "ac_replace": {"desc": "AC replacement (same tonnage)", "base_fee": 140, "variable": "tonnage"},
            "ac_new": {"desc": "New AC installation", "base_fee": 175, "variable": "tonnage"},
            "duct_mod": {"desc": "Duct modification (>25 sq ft)", "base_fee": 85, "variable": None},
            "gas_furnace": {"desc": "Gas furnace replacement", "base_fee": 110, "variable": "btu"},
            "heat_pump": {"desc": "Heat pump installation", "base_fee": 175, "variable": "tonnage"},
        },
        "tonnage_fee": 25,
        "btu_fee": 0.009,
        "plan_review": 75,
        "surcharges": [
            ("Building surcharge", 8.00, True),
            ("Administrative Fee", 14.00, True),
        ],
        "expedited": True,
        "expedited_fee": 85,
        "notes": (
            "Palm Beach County requires a separate electrical permit for the "
            "disconnect. West Palm Beach, Boca Raton, and Delray Beach have "
            "their own building departments with independent fee schedules."
        ),
    },
}


def estimate_fee(county: str, job_type: str, tonnage: int = 0,
                 btu: int = 0, expedited: bool = False,
                 has_gas: bool = False) -> Dict:
    """Calculate estimated permit fees for a given job configuration."""
    schedule = FEE_SCHEDULES[county]
    job = schedule["base_permits"][job_type]

    fee = job["base_fee"]

    # Variable fees based on system size
    var = job["variable"]
    if var == "tonnage" and tonnage > 0:
        fee += tonnage * schedule["tonnage_fee"]
    elif var == "btu" and btu > 0:
        fee += btu * schedule["btu_fee"]

    # Plan review
    fee += schedule["plan_review"]

    # Mandatory surcharges
    surcharge_total = 0
    surcharge_details = []
    for name, amount, is_mandatory in schedule["surcharges"]:
        if is_mandatory:
            surcharge_total += amount
            surcharge_details.append(f"{name}: ${amount:.2f}")
        elif has_gas and "gas" in name.lower() or "fire" in name.lower():
            surcharge_total += amount
            surcharge_details.append(f"{name}: ${amount:.2f}")

    fee += surcharge_total

    # Expedited fee
    if expedited and schedule.get("expedited", False):
        fee += schedule["expedited_fee"]

    total = fee

    return {
        "county": schedule["name"],
        "job": job["desc"],
        "base_permit": job["base_fee"],
        "variable_fee": fee - job["base_fee"] - schedule["plan_review"] - surcharge_total,
        "plan_review": schedule["plan_review"],
        "surcharges": surcharge_details,
        "expedited_fee": schedule.get("expedited_fee", 0) if expedited else 0,
        "total": total,
        "notes": schedule["notes"],
    }


def format_estimate(result: Dict, county_key: str) -> None:
    """Pretty-print a permit fee estimate."""
    schedule = FEE_SCHEDULES[county_key]
    print(f"\n  {'─' * 45}")
    print(f"  Permit Fee Estimate")
    print(f"  {result['county']}")
    print(f"  {result['job']}")
    print(f"  {'─' * 45}")
    print(f"  Base permit fee:            ${result['base_permit']:.2f}")
    print(f"  Variable (tonnage/BTU):     ${result['variable_fee']:.2f}")
    print(f"  Plan review:                ${result['plan_review']:.2f}")
    for surcharge in result['surcharges']:
        print(f"  {surcharge}")
    if result['expedited_fee']:
        print(f"  Expedited fee:              ${result['expedited_fee']:.2f}")
    print(f"  {'─' * 45}")
    print(f"  ESTIMATED TOTAL:            ${result['total']:.2f}")
    print(f"  {'─' * 45}")
    print(f"\n  Important notes:")
    print(f"  {result['notes']}")
    print()
    print(f"  Verify on {FEE_SCHEDULES[county_key]['url']}")

    if result['expedited_fee']:
        print(f"\n  💡 Expedited permitting available — +${result['expedited_fee']:.2f}")
        print(f"     Good for: same-tonnage replacements requiring no plan review")

    print()
    print(f"  Built by [AC Repair Today](https://ac-repair.today) — "
          f"Licensed FL CAC1824118")
    print(f"  Need professional [AC replacement](https://ac-repair.today/"
          f"services/ac-replacement/) or")
    print(f"  [new installation](https://ac-repair.today/services/"
          f"ac-installation/)? We handle all")
    print(f"  county permitting as part of every job.")


def main() -> None:
    """Run the interactive permit fee estimator."""
    print_header("Florida HVAC Permit Fee Estimator")
    print("Estimate permit fees for HVAC work in South Florida counties.")
    print("All fees are estimates — always confirm with the building department.\n")

    # ── Select county ──
    county_options = {
        k: v["name"] for k, v in FEE_SCHEDULES.items()
    }
    county = ask_choice("Select your county:", county_options)

    # ── Select job type ──
    job_options = {
        k: v["desc"] for k, v in FEE_SCHEDULES[county]["base_permits"].items()
    }
    job_type = ask_choice("What type of HVAC work?", job_options)

    tonnage = 0
    btu = 0
    job_info = FEE_SCHEDULES[county]["base_permits"][job_type]

    if job_info["variable"] == "tonnage":
        tonnage = ask_int("System tonnage? (e.g., 3 for 3-ton, or 0 if unsure)",
                           default=3)
        if tonnage == 0:
            tonnage = ask_int("Typical sizes: 2 (small home), 3 (median), "
                              "4 (large), 5 (very large). Try:", default=3)

    elif job_info["variable"] == "btu":
        btu = ask_int("Furnace BTU rating? (e.g. 80000 for 80K BTU)",
                       default=80000)

    # ── Gas? ──
    has_gas = False
    if job_type in ("ac_replace", "ac_new", "heat_pump"):
        has_gas = ask_yes_no("Does the system include gas furnace or gas piping?")

    # ── Expedited? ──
    expedited = False
    if FEE_SCHEDULES[county].get("expedited", False):
        if job_type == "ac_replace" or ask_yes_no("Want expedited processing?"):
            expedited = ask_yes_no("Pay extra for expedited permit?")
            if not expedited:
                print("  Standard processing: 5-15 business days.")

    # ── Calculate ──
    result = estimate_fee(county, job_type, tonnage, btu, expedited, has_gas)

    # ── Display ──
    print_header("Permit Fee Estimate")
    format_estimate(result, county)

    # ── Additional info ──
    print_header("Tips to Save on Permit Fees")

    if job_type == "ac_replace":
        print("  1. Same-tonnage replacements may qualify for reduced fees in")
        print("     all three South Florida counties.")
        print("  2. If your county charges per ton, a correctly-sized system")
        print("     (not oversized) saves permitting costs in addition to")
        print("     equipment costs.")
        print("  3. Bundle electrical disconnect permit with HVAC permit —")
        print("     many counties waive electrical permit fees when bundled.")

    print()
    print("  4. Verify fees online before applying — most counties have")
    print("     updated fee schedules on their building department sites.")
    print("  5. Schedule work through a licensed contractor who includes")
    print("     permit fees in the quote. [AC Repair Today](https://")
    print("     ac-repair.today) handles all county permitting for every")
    print("     job, so you don't need to navigate the process yourself.")
    print()
    print(f"  For professional [AC installation or replacement]"
          f"(https://ac-repair.today/services/ac-replacement/)")
    print(f"  in {FEE_SCHEDULES[county]['name']}, call (800) 917-2580.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Calculator cancelled. Run again anytime.")
        sys.exit(0)
