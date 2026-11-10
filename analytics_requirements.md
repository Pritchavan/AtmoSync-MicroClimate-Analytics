## Analytics Requirements and KPI Planning

## 1. Objective

The objective of this activity is to identify the analytical requirements of the AtmoSync project and define the key performance indicators (KPIs) required for monitoring container conditions and understanding micro-climate variations.

## 2. Data Understanding

The project will use container telemetry data containing information such as:

- Container ID
- Timestamp
- Location
- Temperature
- Humidity
- Latitude and Longitude
- Commodity Type
- Container Status

This data will help analyze environmental conditions and identify containers that may require attention.

## 3. Key Performance Indicators (KPIs)

The following KPIs are proposed for the analytical dashboard:

| KPI | Purpose |
|---|---|
| Total Containers | Count of monitored containers |
| Average Temperature | Monitor average container temperature |
| Average Humidity | Understand humidity conditions |
| At-Risk Containers | Identify containers with potentially unsafe conditions |
| Location-wise Container Count | Compare container distribution by location |
| Temperature Variation | Identify changes in temperature over time |

## 4. Planned Data Analysis

The analysis will focus on:

- Temperature trends over time.
- Humidity comparison across containers.
- Location-wise environmental variations.
- Identification of containers with unusual readings.
- Comparison of environmental conditions by commodity type.

## 5. Visualization Plan

Apache Superset will be used to develop analytical dashboards.

Planned visualizations include:

- KPI cards for important metrics.
- Line charts for temperature trends.
- Bar charts for location-wise comparisons.
- Tables to display container details.
- Charts to highlight at-risk containers.

## 6. Data Quality Considerations

Before analysis, the dataset will be checked for:

- Missing values.
- Duplicate records.
- Invalid temperature and humidity values.
- Incorrect timestamps.
- Inconsistent location and commodity names.

## 7. Current Status

Initial analytical requirements, proposed KPIs, and dashboard visualization ideas have been documented. Actual KPI calculations and dashboard implementation will be performed after the required data becomes available.