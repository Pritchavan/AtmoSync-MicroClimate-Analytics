#  Apache Superset BI Environment Setup

## Objective
To install and deploy Apache Superset as the Business Intelligence tool for the AtmoSync project.

## Work Completed

1. Installed and verified Docker Desktop.
2. Cloned the official Apache Superset repository.
3. Configured the Superset Docker environment.
4. Started Superset using Docker Compose.
5. Resolved the initial PostgreSQL driver issue by switching to the `latest-dev` image.
6. Verified that the Superset application is running successfully.
7. Accessed the Superset Home page through the local browser.

## Environment Details

- BI Tool: Apache Superset
- Container Platform: Docker Desktop
- Database: PostgreSQL
- Cache: Redis
- Local URL: http://localhost:8088

## Current Status

Apache Superset has been successfully deployed and the application health check is passing.

The default sample dashboards are visible. AtmoSync-specific dashboards have not yet been created.

## Pending Work

- Obtain Snowflake account access from the internship team.
- Connect Snowflake to Apache Superset.
- Configure user access roles.

## Outcome

Successfully completed the Apache Superset installation and initial deployment as part of Day 6 of the AtmoSync project.