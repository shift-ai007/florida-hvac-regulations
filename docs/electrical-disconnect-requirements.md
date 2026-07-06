# Electrical Disconnect & Branch Circuit Requirements for Florida HVAC

Every HVAC system requires a properly sized electrical disconnect and branch circuit. In South Florida, where salt air accelerates corrosion and hurricane codes demand specific wind-load ratings, homeowners and contractors must navigate requirements that go well beyond basic NEC compliance.

This guide covers the disconnect and circuit requirements for residential HVAC systems in Florida, common inspection failures, and what to look for when evaluating a contractor's electrical work.

---

## When Is an HVAC Disconnect Required?

The Florida Building Code (adopting NEC Article 440) requires a **disconnecting means** within sight of and within reach of every HVAC outdoor unit. "Within sight" means visible from the unit and no more than 50 feet away.

### What counts as an acceptable disconnect:

| Type | Acceptable? | Notes |
|------|------------|-------|
| Fused pull-out disconnect (30A/60A) | ✅ Standard | Most common in older installations |
| Non-fused pull-out disconnect | ✅ Standard | Typical for new installations with breaker protection at panel |
| Circuit breaker lockable at panel | ❌ | Must be within sight — panel is rarely within sight of outdoor unit |
| AC-rated toggle switch (disconnect switch) | ✅ | Common for mini-splits and smaller units |
| Service disconnect as part of unit | ️⚠️ | Only if the unit has an integral disconnect handle rated for the application |

### Exceptions:
- **Ductless mini-splits**: The indoor unit can serve as the disconnect if it is within sight of the outdoor unit, or a separate disconnect must be installed at the outdoor unit
- **Commercial equipment**: May require lockable disconnect per NFPA 70 Article 430

---

## Sizing Requirements

### Branch Circuit

NEC Article 440 requires the branch circuit to be sized per the **Nameplate Rated Load** or **Minimum Circuit Ampacity (MCA)** — not the breaker size.

| Component | Requirement |
|-----------|-------------|
| Wire gauge | Per MCA on the nameplate (typically 10 AWG for 3-ton, 8 AWG for 4-ton, 6 AWG for 5-ton) |
| Breaker | Per **Maximum Overcurrent Protection (MOP)** on the nameplate — not the MCA |
| Disconnect rating | Minimum of 30A for most residential. Must not be less than MCA. |
| Circuit type | Dedicated branch circuit. Cannot share with other appliances. |

**Common mistake**: Installing 12 AWG wire because the breaker is 20A, when the nameplate requires 10 AWG and 30A breaker. Always pull wire per MCA.

### Disconnect Rating

| System Size | Minimum Disconnect | Recommended Disconnect |
|-------------|-------------------|----------------------|
| Up to 2-ton (18k BTU) | 30A non-fused | 30A non-fused |
| 2.5-ton to 4-ton (30k-48k BTU) | 30A non-fused | 60A non-fused (future-proofing) |
| 5-ton (60k BTU) | 60A non-fused | 60A non-fused |
| Heat pump (any size) | 30A minimum | 60A non-fused (auxiliary heat load) |

---

## South Florida Specific Requirements

### Corrosion Resistance (Coastal Zones)

Miami-Dade and Broward counties enforce stricter requirements for outdoor electrical equipment within the High Velocity Hurricane Zone (HVHZ) and coastal construction areas:

- **Disconnect enclosure**: Must be NEMA 3R (rainproof) minimum. NEMA 4X (stainless/corrosion-resistant) recommended for homes within 1 mile of the coast.
- **Copper vs aluminum bus**: Copper bus is strongly preferred in coastal areas. Aluminum bus in disconnects can fail within 3-5 years in salt-air environments.
- **GFCI requirements**: NEC 2023 requires GFCI protection for outdoor outlets supplying HVAC equipment in dwelling units. This applies to the service receptacle but NOT to the HVAC dedicated circuit itself (per 440.6(B) exception).
- **Miami-Dade Notice of Acceptance (NOA)**: Disconnect switches and enclosures installed in Miami-Dade must carry a valid NOA for wind-load compliance. Verify NOA status at the Miami-Dade Product Control Division website before purchasing.

### Hurricane Hardening

| Requirement | Standard | Details |
|-------------|----------|---------|
| Disconnect mounting height | 4-6 ft above grade | Prevents flood damage AND provides accessibility per NEC |
| Breakaway wiring | Recommended | Flexible conduit between house wall and disconnect allows the disconnect to move with the unit during storm surge without tearing house wiring |
| Impact-rated enclosure | Required in Miami-Dade | Disconnect within 30 ft of opening must meet missile impact test per HVHZ |
| Emergency shutoff label | Required | Florida Building Code requires exterior shutoff labeled "EMERGENCY SHUTOFF — AC" in visible location |

---

## Heat Pump Disconnect Requirements

Heat pumps require special attention because they draw higher starting currents and have auxiliary/emergency heat that adds load:

- **Dual disconnects**: Some jurisdictions require separate disconnects for the outdoor unit and the indoor auxiliary heat (electric strip heat above 5kW)
- **Fused vs non-fused**: Heat pumps with large inrush currents benefit from fused disconnects sized to the MOP, protecting the contacts from pitting
- **Minimum rating**: Heat pump disconnect should be rated for 60A minimum if electric auxiliary heat is present at the air handler — even if the outdoor unit alone needs only 30A

---

## Common Inspection Failures in South Florida

### 1. Missing or Improper Disconnect Location

The disconnect must be within sight of the outdoor unit. This is the #1 HVAC electrical inspection failure in Miami-Dade.

**How it fails:** Disconnect is installed at ground level on the wall 15 feet from the outdoor unit, but a corner of the house blocks line of sight.

**Fix:** Relocate the disconnect or install a second disconnect adjacent to the unit.

### 2. Undersized Wire

Installers pull 14 AWG or 12 AWG for a 3-ton unit because the breaker is 20A.

**How it fails:** Inspector checks the nameplate MCA (typically 17-21A for a 3-ton) and compares it to the wire table — 14 AWG is good for only 15A and 12 AWG for 20A, but the actual amp draw at peak load may exceed the 80% continuous rating.

**Fix:** Pull wire per the nameplate MCA + 25% continuous load margin.

### 3. No Strain Relief on Conduit Entering Disconnect

In coastal South Florida more than anywhere else, strain relief matters because high winds can stress conduit connections.

**How it fails:** Flexible metal conduit (FMC) enters the disconnect through a knock-out without a proper connector. Inspection fails under NEC 300.12.

**Fix:** Use listed liquid-tight connectors for all FMC or schedule 80 PVC entering the disconnect.

### 4. Disconnect Too Close to Gas Piping

**How it fails:** Disconnect installed within 3 feet of gas meter or gas piping without proper clearance. This is a safety violation — an electrical arc from the disconnect could ignite a gas leak.

**Fix:** Maintain minimum 36-inch clearance between disconnect enclosure and gas meter/piping. If space is tight, install a non-metallic disconnect.

---

## Permitting Requirements

In Miami-Dade, Broward, and Palm Beach counties:

- **Separate electrical permit**: HVAC electrical work generally requires a separate electrical permit even when bundled with the mechanical permit
- **Licensed electrician**: HVAC electrical disconnects and branch circuits must be installed by a licensed electrical contractor — not an HVAC contractor in most cases
- **Exceptions**: Some counties allow the HVAC contractor to run the disconnect wiring if they hold both CAC and EC (Electrical Contractor) licenses
- **Inspection**: The electrical disconnect is inspected alongside the mechanical equipment. Failure on either holds the entire permit open

A licensed HVAC contractor who coordinates electrical permitting as part of the job saves homeowners the headache of separate permits. Our team at [AC Repair Today](https://ac-repair.today) manages all electrical and mechanical permitting for every installation and replacement job in Miami-Dade, Broward, and Palm Beach counties.

---

## Upgrading an Existing Disconnect

If your disconnect is rusted, undersized, or non-compliant, replacement involves:

1. Obtain electrical permit
2. Have utility company or electrician verify service disconnect at panel
3. Remove old disconnect (verify power is off at panel)
4. Install new NEMA 3R or 4X enclosure with proper connectors
5. Pull new wire if upgrading ampacity
6. Install GFCI receptacle if required (within 25 ft of unit)
7. Label as "AC Disconnect"
8. Schedule inspection

**Cost range:** $150-400 for disconnect replacement with existing wiring; $400-1,200 for new branch circuit and disconnect.

---

## Quick Reference: Disconnect Checklist

Before signing off on any AC installation or replacement, verify:

- [ ] Disconnect within sight of outdoor unit (visible, within 50 ft)
- [ ] Disconnect rating ≥ MCA on unit nameplate
- [ ] Wire gauge sized per MCA (not breaker size)
- [ ] Breaker sized per MOP (not MCA)
- [ ] NEMA 3R or 4X enclosure (coastal: prefer 4X stainless)
- [ ] Proper strain relief on all conduit entries
- [ ] Minimum 36 inches from gas meter/piping
- [ ] GFCI receptacle within 25 ft (if required by local code)
- [ ] Emergency shutoff label in visible location
- [ ] Miami-Dade NOA (if applicable)
- [ ] Disconnect mounted 4-6 ft above grade
- [ ] Separation from flammable materials

---

*This guide is for informational purposes. Electrical code requirements vary by jurisdiction and are subject to change. Always consult a [licensed Florida HVAC contractor](https://ac-repair.today) and your local building department before performing electrical work. FL License CAC1824118.*

*Last updated: July 2026.*
