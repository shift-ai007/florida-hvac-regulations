# Florida Energy Conservation Code - HVAC Compliance

The Florida Energy Conservation Code (FECC) is based on the International Energy Conservation Code (IECC) with Florida-specific amendments. It sets minimum efficiency and performance requirements for HVAC systems in new construction and major renovations.

## Florida Climate Zones

Florida has two IECC climate zones:

| Zone | Counties | Characteristics |
|------|----------|----------------|
| Zone 1 (Hot-Humid) | Miami-Dade, Broward, Palm Beach, Monroe, Collier, Lee, Hendry, Glades, Martin, St. Lucie, Indian River, Okeechobee, Highlands, Hardee, DeSoto, Charlotte, Sarasota, Manatee | Cooling-dominated, high humidity |
| Zone 2 (Hot-Humid) | All remaining Florida counties | Slightly lower cooling loads, occasional heating needs |

## Manual J/S/D Requirements

### Manual J - Residential Load Calculation

**Required for**: All new HVAC installations in Florida

Manual J calculates the heating and cooling loads for a building based on:

**Building Envelope Factors**:
- Wall construction and insulation R-values
- Roof/attic insulation and radiant barrier presence
- Window area, U-factor, and SHGC (Solar Heat Gain Coefficient)
- Door types and infiltration rates
- Foundation type (slab, crawlspace, basement)

**Climate Factors**:
- Outdoor design temperatures (1% cooling, 99% heating from ASHRAE data)
- Miami design temps: 91F cooling dry-bulb, 47F heating
- Orlando design temps: 93F cooling dry-bulb, 38F heating
- Jacksonville design temps: 95F cooling dry-bulb, 32F heating

**Internal Factors**:
- Occupancy (number of people)
- Appliance heat gains
- Lighting heat gains
- Duct location and leakage

**Output**: Total cooling load (sensible + latent) and heating load in BTU/h. This determines the equipment size.

### Manual S - Equipment Selection

After Manual J determines the load:
- Select equipment that matches the calculated load
- **Maximum oversizing**: 115% of the total cooling load
- Must consider latent (dehumidification) capacity for Florida's humidity
- Variable speed and two-stage equipment can handle broader load ranges

### Manual D - Duct Design

- Size each duct run based on the CFM needed for each room
- Calculate total external static pressure
- Ensure the air handler can deliver required CFM at that static pressure
- Common residential: 350-400 CFM per ton of cooling

## Duct Leakage Testing

### New Construction

Florida Energy Code requires duct leakage testing for new homes:

| Measurement | Maximum Allowed |
|-------------|----------------|
| Total duct leakage | 4 CFM25 per 100 sq ft |
| Leakage to outside | 3 CFM25 per 100 sq ft |

**Testing method**: Duct blaster test at 25 Pascals pressure

### Existing Homes (Replacement Systems)

Duct testing requirements for replacement systems vary by jurisdiction:
- Some counties require it for all replacements
- Others only when ductwork is modified
- Always check with your local building department

## Envelope Requirements That Affect HVAC

The energy code sets minimum envelope performance that directly impacts HVAC sizing:

### Zone 1 (South Florida)

| Component | Minimum Requirement |
|-----------|-------------------|
| Ceiling insulation | R-30 |
| Wall insulation (frame) | R-13 |
| Floor insulation | R-13 |
| Window U-factor | 0.40 max |
| Window SHGC | 0.25 max |
| Air leakage | 5 ACH50 max |

### Zone 2 (Central/North Florida)

| Component | Minimum Requirement |
|-----------|-------------------|
| Ceiling insulation | R-38 |
| Wall insulation (frame) | R-13 |
| Floor insulation | R-13 |
| Window U-factor | 0.40 max |
| Window SHGC | 0.25 max |
| Air leakage | 5 ACH50 max |

## Programmable Thermostat Requirement

Florida Energy Code requires:
- Programmable thermostat or smart thermostat for all new installations
- Minimum 2-program capability (occupied/unoccupied)
- Must have a temperature setback/setup feature
- Manual override capability required

## Ventilation Requirements

### ASHRAE 62.2 Compliance

New homes and major renovations must meet mechanical ventilation requirements:
- Calculated based on home size and occupancy
- Typically achieved with exhaust fans, ERV, or fresh air intake
- In Florida's humid climate, balanced ventilation (ERV/HRV) is preferred to prevent moisture intrusion

### Bathroom and Kitchen Exhaust

- Bathrooms: Minimum 50 CFM intermittent or 20 CFM continuous
- Kitchen: Minimum 100 CFM vented to outside (range hood)
- Must exhaust to the outdoors (not into attic)

## Compliance Paths

Florida offers two compliance paths for the energy code:

### Prescriptive Path
- Meet every requirement exactly as specified in the code tables
- Simplest approach for standard construction
- No flexibility to trade between components

### Performance Path (EnergyGauge/REScheck)
- Model the building using approved energy simulation software
- Total energy use must be equal to or less than a code-compliant reference building
- Allows trade-offs (e.g., better windows can offset less attic insulation)
- More common in custom homes and commercial buildings

## Resources

- [Florida Building Code - Energy Conservation](https://www.floridabuilding.org/fbc/thecode/code-online.htm)
- [ACCA Manual J/S/D](https://www.acca.org/standards)
- [ASHRAE 62.2 Ventilation Standard](https://www.ashrae.org/technical-resources/standards-and-guidelines)
- [EnergyGauge Software](https://energygauge.com/) (Florida-specific energy modeling)
