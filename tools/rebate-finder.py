#!/usr/bin/env python3
"""
Florida HVAC Rebate & Incentive Finder

Estimate available rebates, tax credits, and financing incentives for
HVAC upgrades in Florida. Covers federal tax credits, FPL rebates,
Duke Energy Florida programs, TECO, and local utility incentives.

Usage:
    python3 tools/rebate-finder.py          # Interactive mode
    python3 tools/rebate-finder.py --quick   # Quick estimate

No dependencies beyond Python 3.6+ standard library.
"""

import argparse
import sys

FEDERAL_CREDITS = {
    "heat_pump": {"name": "Central Heat Pump", "max": 2000, "pct": 0.30, "cap": 2000},
    "central_ac": {"name": "Central AC (cooling only)", "max": 600, "pct": 0.30, "cap": 600},
    "smart_thermostat": {"name": "Smart Thermostat", "max": 150, "flat": 150},
    "duct_sealing": {"name": "Duct Sealing", "max": 1100, "pct": 0.30, "cap": 1100},
}

UTILITY_REBATES = {
    "fpl": {
        "name": "FPL (Florida Power & Light)",
        "programs": [
            ("HVAC Rebate", "$150-$400", "Replace AC/heat pump with >=16 SEER2"),
            ("Smart Thermostat", "$25-$50", "Wi-Fi thermostat, load mgmt enrollment"),
            ("Duct Sealing", "$100-$300", "Duct sealing with leakage test"),
        ],
    },
    "duke": {
        "name": "Duke Energy Florida",
        "programs": [
            ("HVAC Rebate", "$200-$500", ">=16 SEER2 AC or heat pump"),
            ("Duct Sealing", "$150-$250", "Existing home duct sealing"),
        ],
    },
    "teco": {
        "name": "TECO (Tampa Electric)",
        "programs": [
            ("HVAC Rebate", "$150-$350", ">=16 SEER2 replacement"),
        ],
    },
}


def print_header(text):
    width = min(60, max(len(text) + 4, 40))
    print(f"\n{'=' * width}")
    print(f"  {text}")
    print(f"{'=' * width}\n")


def estimate_federal(heat_pump, ac_only, smart_tstat, duct_seal, system_cost):
    results = []
    total = 0
    if heat_pump:
        est = min(system_cost * 0.30, 2000)
        total += est
        results.append(f"  Heat Pump: ${round(est):,} (up to $2,000)")
    if ac_only:
        est = min(system_cost * 0.30, 600)
        total += est
        results.append(f"  Central AC: ${round(est):,} (up to $600)")
    if smart_tstat:
        total += 150
        results.append(f"  Smart Thermostat: $150")
    if duct_seal:
        est = min(1500 * 0.30, 1100)
        total += est
        results.append(f"  Duct Sealing: ${round(est):,} (up to $1,100)")
    return results, round(total)


def interactive_mode():
    print_header("Florida HVAC Rebate & Incentive Finder")

    heat_pump = input("Installing a heat pump? (y/n): ").strip().lower() == "y"
    ac_only = input("Installing central AC only? (y/n): ").strip().lower() == "y"
    smart_tstat = input("Adding a smart thermostat? (y/n): ").strip().lower() == "y"
    duct_seal = input("Sealing ductwork? (y/n): ").strip().lower() == "y"

    try:
        cost = int(input("Estimated system cost ($): ").strip() or "7000")
    except ValueError:
        cost = 7000

    federal_results, federal_total = estimate_federal(heat_pump, ac_only, smart_tstat, duct_seal, cost)

    print_header("Federal Tax Credits (non-refundable)")
    for r in federal_results:
        print(r)
    print(f"\n  Total federal credits: ${federal_total:,}")

    print_header("Utility Rebates")
    print("  Check with your utility provider for current programs:")
    for key, util in UTILITY_REBATES.items():
        print(f"\n  {util['name']}:")
        for prog in util["programs"]:
            print(f"    {prog[0]} ({prog[1]}) -- {prog[2]}")

    print()
    print(f"  For professional AC installation: https://ac-repair.today/services/ac-installation/")


def quick_estimate():
    federal_results, federal_total = estimate_federal(True, False, True, False, 7500)
    print_header("Quick Estimate")
    print("  Assumptions: Heat pump + smart thermostat, $7,500 installed")
    for r in federal_results:
        print(r)
    print(f"\n  Estimated federal credits: ${federal_total:,}")
    print("  Plus utility rebates: $150-$400 (FPL territory)")
    print()
    print("  For professional installation: https://ac-repair.today/services/ac-installation/")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        quick_estimate()
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
