#  AtmoSync Dataset Schema Design

## Objective
To design an intermediate-to-advanced dataset structure for the AtmoSync: Micro-Climate Arbitrage Analytics project.

## Dataset Structure

The project dataset will contain four related CSV files.

### 1. containers.csv
Stores container master information.

Fields:
- container_id
- container_type
- capacity
- manufacturer
- temperature_limit_min
- temperature_limit_max

### 2. shipments.csv
Stores shipment and transportation details.

Fields:
- shipment_id
- container_id
- source_location
- destination_location
- dispatch_date
- expected_delivery_date
- actual_delivery_date
- distance_km
- transportation_cost
- shipment_status

### 3. temperature_readings.csv
Stores historical environmental readings.

Fields:
- reading_id
- container_id
- shipment_id
- reading_timestamp
- temperature_c
- humidity_percent
- location

### 4. reroute_options.csv
Stores alternative route information.

Fields:
- reroute_id
- shipment_id
- alternative_destination
- additional_distance_km
- estimated_cost
- estimated_time_hours
- expected_temperature
- recommendation_status

## Dataset Relationships

- containers.csv and shipments.csv are connected through container_id.
- shipments.csv and temperature_readings.csv are connected through shipment_id.
- shipments.csv and reroute_options.csv are connected through shipment_id.

## Planned Dataset Size

| File | Target Records |
|---|---:|
| containers.csv | 100 |
| shipments.csv | 500 |
| temperature_readings.csv | 10,000 |
| reroute_options.csv | 1,000 |

## Planned Analytics

- Historical container route analysis
- Temperature and humidity fluctuation analysis
- Spoilage risk identification
- At-risk container analysis
- Transportation cost analysis
- Alternative route comparison

## Outcome

Designed the initial relational dataset structure for AtmoSync. This schema will serve as the foundation for generating synthetic analytical data and developing dashboards in Apache Superset.