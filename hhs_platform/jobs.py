# FILE: hhs_platform/jobs.py - MODERN AUGUST 2025 APPROACH
"""
Modern job definitions following August 2025 best practices
- Clear asset type separation
- No mixing of dbt and monitoring assets
- Modern naming conventions
"""
from dagster import (
    AssetSelection,
    define_asset_job
)
from hhs_platform.assets import (
    # dbt assets
    hhs_staging_assets,
    hhs_integration_assets, 
    hhs_presentation_assets,
    # Pure monitoring assets (separate)
    pipeline_health_monitor,
    data_quality_summary
)
 
# ================================================================
# DBT DATA PIPELINE JOBS - Only dbt assets (August 2025)
# ================================================================
 
staging_job = define_asset_job(
    name="hhs_staging_pipeline",
    selection=AssetSelection.assets(hhs_staging_assets),
    description="Process staging layer models for child assistance programs",
    tags={"layer": "staging", "type": "dbt", "version": "2025"}
)
 
integration_job = define_asset_job(
    name="hhs_integration_pipeline", 
    selection=AssetSelection.assets(hhs_integration_assets),
    description="Execute integration layer business logic",
    tags={"layer": "integration", "type": "dbt", "version": "2025"}
)
 
presentation_job = define_asset_job(
    name="hhs_presentation_pipeline",
    selection=AssetSelection.assets(hhs_presentation_assets),
    description="Generate final presentation layer tables",
    tags={"layer": "presentation", "type": "dbt", "version": "2025"}
)
 
# FIXED: Correct naming - this matches what your schedules expect
full_pipeline_job = define_asset_job(
    name="hhs_full_pipeline",
    selection=AssetSelection.assets(
        hhs_staging_assets,
        hhs_integration_assets,
        hhs_presentation_assets
    ),
    description="Complete HHS dbt data pipeline from staging to presentation",
    tags={"pipeline": "complete", "type": "dbt", "version": "2025"}
)
 
# ================================================================
# MODERN OBSERVABILITY JOBS - Only monitoring assets (August 2025)
# ================================================================
 
monitoring_job = define_asset_job(
    name="hhs_monitoring_pipeline",
    selection=AssetSelection.assets(
        pipeline_health_monitor,
        data_quality_summary
    ),
    description="Modern observability and monitoring checks",
    tags={"type": "monitoring", "framework": "modern_2025"}
)
