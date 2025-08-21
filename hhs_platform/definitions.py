# FILE: hhs_platform/definitions.py - MODERN AUGUST 2025
"""
Modern Dagster definitions following August 2025 best practices
- Clean separation of asset types
- No mixed dbt and monitoring assets in same jobs
- Modern observability patterns
"""
from dagster import Definitions
 
# Import modern separated assets
from hhs_platform.assets import (
    # dbt assets - generated from manifest
    hhs_staging_assets,
    hhs_integration_assets,
    hhs_presentation_assets,
    
    # Modern monitoring assets - pure Dagster (August 2025)
    pipeline_health_monitor,
    data_quality_summary
)
 
# Import fixed job definitions
from hhs_platform.jobs import (
    # Data pipeline jobs (dbt assets only)
    staging_job,
    integration_job,
    presentation_job,
    full_pipeline_job,  # FIXED: This matches your schedules.py
    
    # Observability jobs (monitoring assets only)
    monitoring_job
)
 
from hhs_platform.schedules import daily_hhs_pipeline, monitoring_schedule
from hhs_platform.sensors import data_arrival_sensor
from hhs_platform.resources import dbt_resource, snowflake_resource
 
# Modern Dagster definitions (August 2025)
defs = Definitions(
    assets=[
        # dbt assets - data transformation pipeline
        hhs_staging_assets,
        hhs_integration_assets, 
        hhs_presentation_assets,
        
        # Modern observability assets - monitoring & health
        pipeline_health_monitor,
        data_quality_summary
    ],
    jobs=[
        # Data transformation jobs
        staging_job,
        integration_job,
        presentation_job,
        full_pipeline_job,
        
        # Observability jobs
        monitoring_job
    ],
    schedules=[
        daily_hhs_pipeline,
        monitoring_schedule
    ],
    sensors=[
        data_arrival_sensor
    ],
    resources={
        "dbt": dbt_resource,
        "snowflake": snowflake_resource
    }
)
