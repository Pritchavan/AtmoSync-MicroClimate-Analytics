# Superset User Access Planning

## 1. Objective

The objective of this activity is to understand and plan user access permissions for the AtmoSync analytics dashboard using Apache Superset.

## 2. User Roles

The dashboard may be accessed by different users based on their responsibilities.

| User Role | Access Requirements |
|---|---|
| Admin | Manage users, roles, dashboards, and data connections |
| Analyst | Create charts, explore datasets, and develop dashboards |
| Viewer | View dashboards and analyze the available visualizations |

## 3. Access Control Requirements

- Admin users should have permission to manage dashboard settings and user access.
- Analysts should be able to create and modify charts and dashboards.
- Viewers should have read-only access to published dashboards.
- Access to datasets should be provided according to user responsibilities.
- Unauthorized users should not be allowed to modify dashboard information.

## 4. Dashboard Access Requirements

The AtmoSync dashboard should provide access to important analytical information, including:

- Total monitored containers.
- Average temperature and humidity.
- Location-wise container information.
- Temperature trends.
- At-risk container details.

The information displayed will depend on the permissions assigned to each user.

## 5. Security Considerations

- Follow the principle of least privilege.
- Assign permissions based on user roles.
- Avoid sharing administrator credentials.
- Restrict access to sensitive information.
- Review user permissions whenever responsibilities change.

## 6. Implementation Plan

Apache Superset will be configured with suitable user roles and permissions. The dashboard will be connected to the Snowflake data warehouse once the required access and connection details are available.

## 7. Current Progress

The initial user roles, dashboard access requirements, and security considerations have been documented. Actual role configuration and permission testing will be performed during the Superset setup.