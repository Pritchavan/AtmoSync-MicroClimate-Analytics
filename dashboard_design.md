# Dashboard Design and Visualization Planning

## 1. Objective

The objective of this activity is to plan the initial dashboard design for the AtmoSync project. The dashboard will help users understand container conditions and identify possible climate-related risks through simple visualizations.

## 2. Dashboard Overview

The dashboard will present important information about containers, their environmental conditions, and their locations. It will be developed using Apache Superset and connected to Snowflake as the data source.

## 3. Planned Dashboard Components

| Dashboard Component | Visualization Type | Purpose |
|---|---|---|
| Total Containers | KPI Card | Display the total number of monitored containers |
| Average Temperature | KPI Card | Show the average container temperature |
| Average Humidity | KPI Card | Show the average humidity level |
| Temperature Trends | Line Chart | Track temperature changes over time |
| Location-wise Containers | Bar Chart | Compare containers across locations |
| Container Status | Table | Display container details and current status |
| At-Risk Containers | Table or Bar Chart | Highlight containers requiring attention |

## 4. Planned Filters

The dashboard may include the following filters:

- Date range
- Container ID
- Location
- Commodity type
- Container status

These filters will help users explore specific records and compare different conditions.

## 5. Data Requirements

The dashboard will require container telemetry data containing:

- Container ID
- Timestamp
- Temperature
- Humidity
- Location
- Commodity type
- Container status

The availability and final structure of these fields will be confirmed after the Snowflake data connection is ready.

## 6. Visualization Approach

KPI cards will provide a quick summary of important metrics. Line charts will help identify temperature changes over time, while bar charts will support location-wise comparisons. Tables will provide detailed container information and help identify containers that may require further attention.

## 7. Current Progress

The initial dashboard structure, visualization types, and required filters have been planned. The actual dashboard implementation will be carried out after the required data is available and the Snowflake connection is configured.