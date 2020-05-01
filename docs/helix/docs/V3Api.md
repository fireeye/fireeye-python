# fireeye.helix.V3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_alerts_cases_create**](V3Api.md#v3_alerts_cases_create) | **POST** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alerts}/cases/ | 
[**v3_alerts_cases_delete**](V3Api.md#v3_alerts_cases_delete) | **DELETE** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alerts}/cases/ | 
[**v3_alerts_cases_delete_0**](V3Api.md#v3_alerts_cases_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alerts}/cases//{id} | 
[**v3_alerts_cases_list**](V3Api.md#v3_alerts_cases_list) | **GET** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alerts}/cases/ | 
[**v3_alerts_cases_partial_update**](V3Api.md#v3_alerts_cases_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alerts}/cases//{id} | 
[**v3_alerts_cases_partial_update0**](V3Api.md#v3_alerts_cases_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alerts}/cases//{id} | 
[**v3_alerts_cases_read**](V3Api.md#v3_alerts_cases_read) | **GET** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alerts}/cases//{id} | 
[**v3_alerts_cases_search**](V3Api.md#v3_alerts_cases_search) | **GET** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alerts}/cases//search | 
[**v3_alerts_create**](V3Api.md#v3_alerts_create) | **POST** /helix/id/hexzsq689/api/v3/alerts/ | 
[**v3_alerts_get_enum_fields**](V3Api.md#v3_alerts_get_enum_fields) | **GET** /helix/id/hexzsq689/api/v3/alerts//fields | Lists all fields that describe alerts.
[**v3_alerts_get_events**](V3Api.md#v3_alerts_get_events) | **GET** /helix/id/hexzsq689/api/v3/alerts//{id}/events | Lists alert events for a specific alert.
[**v3_alerts_get_hx_host_endpoints**](V3Api.md#v3_alerts_get_hx_host_endpoints) | **GET** /helix/id/hexzsq689/api/v3/alerts//{id}/endpoints | Retrieves a specific alert from an HX endpoint.
[**v3_alerts_get_intel_context**](V3Api.md#v3_alerts_get_intel_context) | **GET** /helix/id/hexzsq689/api/v3/alerts//{id}/context | Gets the instances and indicators for a specific alert.
[**v3_alerts_get_investigative_tips**](V3Api.md#v3_alerts_get_investigative_tips) | **GET** /helix/id/hexzsq689/api/v3/alerts//{id}/tips | Lists the investigative tips for a specific alert.
[**v3_alerts_get_md_investigation_results**](V3Api.md#v3_alerts_get_md_investigation_results) | **GET** /helix/id/hexzsq689/api/v3/alerts//{id}/investigations | Retrieves Managed Defense investigation results for an alert.
[**v3_alerts_get_org_metrics**](V3Api.md#v3_alerts_get_org_metrics) | **GET** /helix/id/hexzsq689/api/v3/alerts//org_metrics | Lists alert metrics by organization.
[**v3_alerts_get_revisions**](V3Api.md#v3_alerts_get_revisions) | **GET** /helix/id/hexzsq689/api/v3/alerts//{id}/revisions | Returns the revision history.
[**v3_alerts_get_unique_values**](V3Api.md#v3_alerts_get_unique_values) | **GET** /helix/id/hexzsq689/api/v3/alerts//values | Lists the number of occurrences of each field value.
[**v3_alerts_list**](V3Api.md#v3_alerts_list) | **GET** /helix/id/hexzsq689/api/v3/alerts/ | 
[**v3_alerts_notes_create**](V3Api.md#v3_alerts_notes_create) | **POST** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_object_id}/notes/ | Adds a note to the specified alert or case.
[**v3_alerts_notes_delete**](V3Api.md#v3_alerts_notes_delete) | **DELETE** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_object_id}/notes//{id} | Deletes the specified note.
[**v3_alerts_notes_list**](V3Api.md#v3_alerts_notes_list) | **GET** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_object_id}/notes/ | 
[**v3_alerts_notes_partial_update**](V3Api.md#v3_alerts_notes_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_object_id}/notes//{id} | 
[**v3_alerts_notes_partial_update0**](V3Api.md#v3_alerts_notes_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_object_id}/notes//{id} | 
[**v3_alerts_notes_read**](V3Api.md#v3_alerts_notes_read) | **GET** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_object_id}/notes//{id} | 
[**v3_alerts_plays_list**](V3Api.md#v3_alerts_plays_list) | **GET** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alert}/plays/ | 
[**v3_alerts_plays_read**](V3Api.md#v3_alerts_plays_read) | **GET** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alert}/plays//{id} | 
[**v3_alerts_plays_search**](V3Api.md#v3_alerts_plays_search) | **GET** /helix/id/hexzsq689/api/v3/alerts//{parent_lookup_alert}/plays//search | 
[**v3_alerts_read**](V3Api.md#v3_alerts_read) | **GET** /helix/id/hexzsq689/api/v3/alerts//{id} | 
[**v3_alerts_search**](V3Api.md#v3_alerts_search) | **GET** /helix/id/hexzsq689/api/v3/alerts//search | 
[**v3_alerts_types_create**](V3Api.md#v3_alerts_types_create) | **POST** /helix/id/hexzsq689/api/v3/alerts/types/ | 
[**v3_alerts_types_delete**](V3Api.md#v3_alerts_types_delete) | **DELETE** /helix/id/hexzsq689/api/v3/alerts/types//{id} | 
[**v3_alerts_types_list**](V3Api.md#v3_alerts_types_list) | **GET** /helix/id/hexzsq689/api/v3/alerts/types/ | 
[**v3_alerts_types_partial_update**](V3Api.md#v3_alerts_types_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/alerts/types//{id} | 
[**v3_alerts_types_partial_update0**](V3Api.md#v3_alerts_types_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/alerts/types//{id} | 
[**v3_alerts_types_read**](V3Api.md#v3_alerts_types_read) | **GET** /helix/id/hexzsq689/api/v3/alerts/types//{id} | 
[**v3_alerts_types_search**](V3Api.md#v3_alerts_types_search) | **GET** /helix/id/hexzsq689/api/v3/alerts/types//search | 
[**v3_appliances_get_appliance_health**](V3Api.md#v3_appliances_get_appliance_health) | **GET** /helix/id/hexzsq689/api/v3/appliances//health | Provides a summary of the health of your FireEye network appliances.
[**v3_appliances_list**](V3Api.md#v3_appliances_list) | **GET** /helix/id/hexzsq689/api/v3/appliances/ | 
[**v3_appliances_read**](V3Api.md#v3_appliances_read) | **GET** /helix/id/hexzsq689/api/v3/appliances//{id} | Searches for appliance by ID (the deviceid from GET /appliances).
[**v3_automation_jobs_artifacts_create**](V3Api.md#v3_automation_jobs_artifacts_create) | **POST** /helix/id/hexzsq689/api/v3/automation/jobs//{parent_lookup_play_execution}/artifacts/ | Overrides the default &#39;create&#39; method in order to associate the
[**v3_automation_jobs_artifacts_delete**](V3Api.md#v3_automation_jobs_artifacts_delete) | **DELETE** /helix/id/hexzsq689/api/v3/automation/jobs//{parent_lookup_play_execution}/artifacts//{id} | 
[**v3_automation_jobs_artifacts_list**](V3Api.md#v3_automation_jobs_artifacts_list) | **GET** /helix/id/hexzsq689/api/v3/automation/jobs//{parent_lookup_play_execution}/artifacts/ | 
[**v3_automation_jobs_artifacts_partial_update**](V3Api.md#v3_automation_jobs_artifacts_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/automation/jobs//{parent_lookup_play_execution}/artifacts//{id} | 
[**v3_automation_jobs_artifacts_partial_update0**](V3Api.md#v3_automation_jobs_artifacts_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/automation/jobs//{parent_lookup_play_execution}/artifacts//{id} | 
[**v3_automation_jobs_artifacts_read**](V3Api.md#v3_automation_jobs_artifacts_read) | **GET** /helix/id/hexzsq689/api/v3/automation/jobs//{parent_lookup_play_execution}/artifacts//{id} | 
[**v3_automation_jobs_artifacts_search**](V3Api.md#v3_automation_jobs_artifacts_search) | **GET** /helix/id/hexzsq689/api/v3/automation/jobs//{parent_lookup_play_execution}/artifacts//search | 
[**v3_automation_jobs_create**](V3Api.md#v3_automation_jobs_create) | **POST** /helix/id/hexzsq689/api/v3/automation/jobs/ | 
[**v3_automation_jobs_delete**](V3Api.md#v3_automation_jobs_delete) | **DELETE** /helix/id/hexzsq689/api/v3/automation/jobs//{id} | 
[**v3_automation_jobs_list**](V3Api.md#v3_automation_jobs_list) | **GET** /helix/id/hexzsq689/api/v3/automation/jobs/ | 
[**v3_automation_jobs_partial_update**](V3Api.md#v3_automation_jobs_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/automation/jobs//{id} | 
[**v3_automation_jobs_partial_update0**](V3Api.md#v3_automation_jobs_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/automation/jobs//{id} | 
[**v3_automation_jobs_read**](V3Api.md#v3_automation_jobs_read) | **GET** /helix/id/hexzsq689/api/v3/automation/jobs//{id} | 
[**v3_automation_jobs_search**](V3Api.md#v3_automation_jobs_search) | **GET** /helix/id/hexzsq689/api/v3/automation/jobs//search | 
[**v3_cases_alerts_create**](V3Api.md#v3_cases_alerts_create) | **POST** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts/ | Alerts associated with a case.
[**v3_cases_alerts_delete**](V3Api.md#v3_cases_alerts_delete) | **DELETE** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts/ | Removes all alerts from a case.
[**v3_cases_alerts_delete_0**](V3Api.md#v3_cases_alerts_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts//{id} | Removes the specified alert from a case.
[**v3_cases_alerts_list**](V3Api.md#v3_cases_alerts_list) | **GET** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts/ | Alerts associated with a case.
[**v3_cases_alerts_partial_update**](V3Api.md#v3_cases_alerts_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts//{id} | Alerts associated with a case.
[**v3_cases_alerts_partial_update0**](V3Api.md#v3_cases_alerts_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts//{id} | Alerts associated with a case.
[**v3_cases_alerts_read**](V3Api.md#v3_cases_alerts_read) | **GET** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts//{id} | Alerts associated with a case.
[**v3_cases_alerts_search**](V3Api.md#v3_cases_alerts_search) | **GET** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts//search | Alerts associated with a case.
[**v3_cases_alerts_update**](V3Api.md#v3_cases_alerts_update) | **PUT** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_incidents}/alerts/ | Alerts associated with a case.
[**v3_cases_create**](V3Api.md#v3_cases_create) | **POST** /helix/id/hexzsq689/api/v3/cases/ | 
[**v3_cases_delete**](V3Api.md#v3_cases_delete) | **DELETE** /helix/id/hexzsq689/api/v3/cases//{id} | 
[**v3_cases_export_all**](V3Api.md#v3_cases_export_all) | **GET** /helix/id/hexzsq689/api/v3/cases//export | Creates an export file in JSON format.
[**v3_cases_export_single**](V3Api.md#v3_cases_export_single) | **GET** /helix/id/hexzsq689/api/v3/cases//{id}/export | Exports the specified case to a JSON file.
[**v3_cases_get_all_existing_case_statuses_with_counts**](V3Api.md#v3_cases_get_all_existing_case_statuses_with_counts) | **GET** /helix/id/hexzsq689/api/v3/cases//statuses | Returns an object containing various status values with their respective counts.
[**v3_cases_get_all_tags**](V3Api.md#v3_cases_get_all_tags) | **GET** /helix/id/hexzsq689/api/v3/cases//tags | Retrieves the number of tags associated with cases and the tags themselves.
[**v3_cases_get_revisions**](V3Api.md#v3_cases_get_revisions) | **GET** /helix/id/hexzsq689/api/v3/cases//{id}/revisions | Returns the revision history.
[**v3_cases_list**](V3Api.md#v3_cases_list) | **GET** /helix/id/hexzsq689/api/v3/cases/ | 
[**v3_cases_notes_create**](V3Api.md#v3_cases_notes_create) | **POST** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_object_id}/notes/ | Adds a note to the specified alert or case.
[**v3_cases_notes_delete**](V3Api.md#v3_cases_notes_delete) | **DELETE** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_object_id}/notes//{id} | Deletes the specified note.
[**v3_cases_notes_list**](V3Api.md#v3_cases_notes_list) | **GET** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_object_id}/notes/ | 
[**v3_cases_notes_partial_update**](V3Api.md#v3_cases_notes_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_object_id}/notes//{id} | 
[**v3_cases_notes_partial_update0**](V3Api.md#v3_cases_notes_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_object_id}/notes//{id} | 
[**v3_cases_notes_read**](V3Api.md#v3_cases_notes_read) | **GET** /helix/id/hexzsq689/api/v3/cases//{parent_lookup_object_id}/notes//{id} | 
[**v3_cases_partial_update**](V3Api.md#v3_cases_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/cases//{id} | 
[**v3_cases_partial_update0**](V3Api.md#v3_cases_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/cases//{id} | 
[**v3_cases_read**](V3Api.md#v3_cases_read) | **GET** /helix/id/hexzsq689/api/v3/cases//{id} | 
[**v3_cases_search**](V3Api.md#v3_cases_search) | **GET** /helix/id/hexzsq689/api/v3/cases//search | 
[**v3_dashboards_clone**](V3Api.md#v3_dashboards_clone) | **POST** /helix/id/hexzsq689/api/v3/dashboards//{id}/clone | Clones the specified dashboard, including all widgets.
[**v3_dashboards_create**](V3Api.md#v3_dashboards_create) | **POST** /helix/id/hexzsq689/api/v3/dashboards/ | Creates a dashboard.
[**v3_dashboards_delete**](V3Api.md#v3_dashboards_delete) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_favorite_create**](V3Api.md#v3_dashboards_favorite_create) | **POST** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/favorite/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_favorite_delete**](V3Api.md#v3_dashboards_favorite_delete) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/favorite/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_favorite_delete_0**](V3Api.md#v3_dashboards_favorite_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/favorite//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_favorite_list**](V3Api.md#v3_dashboards_favorite_list) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/favorite/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_favorite_partial_update**](V3Api.md#v3_dashboards_favorite_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/favorite//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_favorite_partial_update0**](V3Api.md#v3_dashboards_favorite_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/favorite//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_favorite_read**](V3Api.md#v3_dashboards_favorite_read) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/favorite//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_favorite_update**](V3Api.md#v3_dashboards_favorite_update) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/favorite/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_get_all_tags**](V3Api.md#v3_dashboards_get_all_tags) | **GET** /helix/id/hexzsq689/api/v3/dashboards//tags | Lists all tags associated with dashboards.
[**v3_dashboards_list**](V3Api.md#v3_dashboards_list) | **GET** /helix/id/hexzsq689/api/v3/dashboards/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_partial_update**](V3Api.md#v3_dashboards_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_partial_update0**](V3Api.md#v3_dashboards_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/dashboards//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_read**](V3Api.md#v3_dashboards_read) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{id} | Retrieves the specified dashboard.
[**v3_dashboards_reports_create**](V3Api.md#v3_dashboards_reports_create) | **POST** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports/ | 
[**v3_dashboards_reports_delete**](V3Api.md#v3_dashboards_reports_delete) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports/ | 
[**v3_dashboards_reports_delete_0**](V3Api.md#v3_dashboards_reports_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports//{id} | 
[**v3_dashboards_reports_export_pdf**](V3Api.md#v3_dashboards_reports_export_pdf) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports//{id}/export | 
[**v3_dashboards_reports_list**](V3Api.md#v3_dashboards_reports_list) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports/ | 
[**v3_dashboards_reports_partial_update**](V3Api.md#v3_dashboards_reports_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports//{id} | 
[**v3_dashboards_reports_partial_update0**](V3Api.md#v3_dashboards_reports_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports//{id} | 
[**v3_dashboards_reports_read**](V3Api.md#v3_dashboards_reports_read) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports//{id} | Override to include widget result serializer
[**v3_dashboards_reports_search**](V3Api.md#v3_dashboards_reports_search) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/reports//search | 
[**v3_dashboards_schedule_create**](V3Api.md#v3_dashboards_schedule_create) | **POST** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/schedule/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_schedule_delete**](V3Api.md#v3_dashboards_schedule_delete) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/schedule/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_schedule_delete_0**](V3Api.md#v3_dashboards_schedule_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/schedule//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_schedule_list**](V3Api.md#v3_dashboards_schedule_list) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/schedule/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_schedule_partial_update**](V3Api.md#v3_dashboards_schedule_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/schedule//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_schedule_partial_update0**](V3Api.md#v3_dashboards_schedule_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/schedule//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_schedule_read**](V3Api.md#v3_dashboards_schedule_read) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/schedule//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_schedule_update**](V3Api.md#v3_dashboards_schedule_update) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/schedule/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_schedules_list**](V3Api.md#v3_dashboards_schedules_list) | **GET** /helix/id/hexzsq689/api/v3/dashboards/schedules/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_search**](V3Api.md#v3_dashboards_search) | **GET** /helix/id/hexzsq689/api/v3/dashboards//search | View for tying together the serializer, authentication, permission and
[**v3_dashboards_subscribe**](V3Api.md#v3_dashboards_subscribe) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{id}/subscribe | Subscribes/Unsubscribes the current user from receiving
[**v3_dashboards_widgets_create**](V3Api.md#v3_dashboards_widgets_create) | **POST** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets/ | Creates a widget for the specified dashboard.
[**v3_dashboards_widgets_delete**](V3Api.md#v3_dashboards_widgets_delete) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets/ | Deletes all widgets from the specified dashboard.
[**v3_dashboards_widgets_delete_0**](V3Api.md#v3_dashboards_widgets_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets//{id} | Deletes a widget from the specified dashboard.
[**v3_dashboards_widgets_list**](V3Api.md#v3_dashboards_widgets_list) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets/ | View for tying together the serializer, authentication, permission and
[**v3_dashboards_widgets_partial_update**](V3Api.md#v3_dashboards_widgets_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_widgets_partial_update0**](V3Api.md#v3_dashboards_widgets_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_widgets_perform_search**](V3Api.md#v3_dashboards_widgets_perform_search) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets//{id}/results/ | Returns the results of a dashboard widget.
[**v3_dashboards_widgets_read**](V3Api.md#v3_dashboards_widgets_read) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets//{id} | View for tying together the serializer, authentication, permission and
[**v3_dashboards_widgets_search**](V3Api.md#v3_dashboards_widgets_search) | **GET** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets//search | View for tying together the serializer, authentication, permission and
[**v3_dashboards_widgets_update**](V3Api.md#v3_dashboards_widgets_update) | **PUT** /helix/id/hexzsq689/api/v3/dashboards//{parent_lookup_dashboard}/widgets/ | Updates all widgets for the specified dashboard.
[**v3_domains_resolve_list**](V3Api.md#v3_domains_resolve_list) | **GET** /helix/id/hexzsq689/api/v3/domains/resolve | 
[**v3_fields_analytics_list**](V3Api.md#v3_fields_analytics_list) | **GET** /helix/id/hexzsq689/api/v3/fields/analytics | 
[**v3_indicators_stream_list**](V3Api.md#v3_indicators_stream_list) | **GET** /helix/id/hexzsq689/api/v3/indicators/stream/ | 
[**v3_indicators_stream_read**](V3Api.md#v3_indicators_stream_read) | **GET** /helix/id/hexzsq689/api/v3/indicators/stream//{id} | 
[**v3_intel_context_characteristics_list**](V3Api.md#v3_intel_context_characteristics_list) | **GET** /helix/id/hexzsq689/api/v3/intel/context/characteristics | 
[**v3_lists_create**](V3Api.md#v3_lists_create) | **POST** /helix/id/hexzsq689/api/v3/lists/ | Returns a list of Lists.  You can search for specific lists by name,
[**v3_lists_delete**](V3Api.md#v3_lists_delete) | **DELETE** /helix/id/hexzsq689/api/v3/lists//{id} | Returns a list of Lists.  You can search for specific lists by name,
[**v3_lists_export_all**](V3Api.md#v3_lists_export_all) | **GET** /helix/id/hexzsq689/api/v3/lists//export | Creates an export file in JSON format.
[**v3_lists_export_single**](V3Api.md#v3_lists_export_single) | **GET** /helix/id/hexzsq689/api/v3/lists//{id}/export | Exports the specified case to a JSON file.
[**v3_lists_items_create**](V3Api.md#v3_lists_items_create) | **POST** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items/ | Overrides the default &#39;create&#39; method in order to associate the
[**v3_lists_items_delete**](V3Api.md#v3_lists_items_delete) | **DELETE** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items/ | Deletes list items from the specified list. You cannot delete items from internal or protected lists.
[**v3_lists_items_delete_0**](V3Api.md#v3_lists_items_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items//{id} | Exports list items as a JSON file.
[**v3_lists_items_export**](V3Api.md#v3_lists_items_export) | **GET** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items//export | Exports the specified list as a JSON file.
[**v3_lists_items_export_single**](V3Api.md#v3_lists_items_export_single) | **GET** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items//{id}/export | Exports the specified case to a JSON file.
[**v3_lists_items_list**](V3Api.md#v3_lists_items_list) | **GET** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items/ | Exports list items as a JSON file.
[**v3_lists_items_partial_update**](V3Api.md#v3_lists_items_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items//{id} | Exports list items as a JSON file.
[**v3_lists_items_partial_update0**](V3Api.md#v3_lists_items_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items//{id} | Exports list items as a JSON file.
[**v3_lists_items_read**](V3Api.md#v3_lists_items_read) | **GET** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items//{id} | Exports list items as a JSON file.
[**v3_lists_items_search**](V3Api.md#v3_lists_items_search) | **GET** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items//search | Exports list items as a JSON file.
[**v3_lists_items_types_list**](V3Api.md#v3_lists_items_types_list) | **GET** /helix/id/hexzsq689/api/v3/lists/items/types | Returns all list item types and their labels.
[**v3_lists_items_upload**](V3Api.md#v3_lists_items_upload) | **POST** /helix/id/hexzsq689/api/v3/lists//{parent_lookup_list}/items//import | Imports list items into the specified list.
[**v3_lists_list**](V3Api.md#v3_lists_list) | **GET** /helix/id/hexzsq689/api/v3/lists/ | Returns a list of Lists.  You can search for specific lists by name,
[**v3_lists_partial_update**](V3Api.md#v3_lists_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/lists//{id} | Returns a list of Lists.  You can search for specific lists by name,
[**v3_lists_partial_update0**](V3Api.md#v3_lists_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/lists//{id} | Returns a list of Lists.  You can search for specific lists by name,
[**v3_lists_read**](V3Api.md#v3_lists_read) | **GET** /helix/id/hexzsq689/api/v3/lists//{id} | Returns a list of Lists.  You can search for specific lists by name,
[**v3_lists_search**](V3Api.md#v3_lists_search) | **GET** /helix/id/hexzsq689/api/v3/lists//search | Returns a list of Lists.  You can search for specific lists by name,
[**v3_patterndb_create**](V3Api.md#v3_patterndb_create) | **POST** /helix/id/hexzsq689/api/v3/patterndb/ | 
[**v3_patterndb_delete**](V3Api.md#v3_patterndb_delete) | **DELETE** /helix/id/hexzsq689/api/v3/patterndb//{id} | 
[**v3_patterndb_export**](V3Api.md#v3_patterndb_export) | **GET** /helix/id/hexzsq689/api/v3/patterndb//{id}/export | 
[**v3_patterndb_list**](V3Api.md#v3_patterndb_list) | **GET** /helix/id/hexzsq689/api/v3/patterndb/ | 
[**v3_playbooks_create**](V3Api.md#v3_playbooks_create) | **POST** /helix/id/hexzsq689/api/v3/playbooks/ | View for tying together the serializer, authentication, permission and
[**v3_playbooks_delete**](V3Api.md#v3_playbooks_delete) | **DELETE** /helix/id/hexzsq689/api/v3/playbooks//{id} | View for tying together the serializer, authentication, permission and
[**v3_playbooks_list**](V3Api.md#v3_playbooks_list) | **GET** /helix/id/hexzsq689/api/v3/playbooks/ | View for tying together the serializer, authentication, permission and
[**v3_playbooks_partial_update**](V3Api.md#v3_playbooks_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/playbooks//{id} | View for tying together the serializer, authentication, permission and
[**v3_playbooks_partial_update0**](V3Api.md#v3_playbooks_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/playbooks//{id} | View for tying together the serializer, authentication, permission and
[**v3_playbooks_plays_create**](V3Api.md#v3_playbooks_plays_create) | **POST** /helix/id/hexzsq689/api/v3/playbooks/{id}/plays/ | Override the default create method to add playbook_id
[**v3_playbooks_plays_list**](V3Api.md#v3_playbooks_plays_list) | **GET** /helix/id/hexzsq689/api/v3/playbooks/{id}/plays/ | Override the default list method to add playbook_id
[**v3_playbooks_read**](V3Api.md#v3_playbooks_read) | **GET** /helix/id/hexzsq689/api/v3/playbooks//{id} | View for tying together the serializer, authentication, permission and
[**v3_plays_create**](V3Api.md#v3_plays_create) | **POST** /helix/id/hexzsq689/api/v3/plays/ | Override the default create method to add playbook_id
[**v3_plays_delete**](V3Api.md#v3_plays_delete) | **DELETE** /helix/id/hexzsq689/api/v3/plays//{id} | View for tying together the serializer, authentication, permission and
[**v3_plays_list**](V3Api.md#v3_plays_list) | **GET** /helix/id/hexzsq689/api/v3/plays/ | Override the default list method to add playbook_id
[**v3_plays_partial_update**](V3Api.md#v3_plays_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/plays//{id} | View for tying together the serializer, authentication, permission and
[**v3_plays_partial_update0**](V3Api.md#v3_plays_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/plays//{id} | View for tying together the serializer, authentication, permission and
[**v3_plays_read**](V3Api.md#v3_plays_read) | **GET** /helix/id/hexzsq689/api/v3/plays//{id} | View for tying together the serializer, authentication, permission and
[**v3_preferences_cms_url**](V3Api.md#v3_preferences_cms_url) | **PUT** /helix/id/hexzsq689/api/v3/preferences//cms_url | Specifies the Network (CMS) URL used by Helix.
[**v3_preferences_etp_url**](V3Api.md#v3_preferences_etp_url) | **PUT** /helix/id/hexzsq689/api/v3/preferences//etp_url | Specifies the Email (ETP) URL used by Helix.
[**v3_preferences_hx_url**](V3Api.md#v3_preferences_hx_url) | **PUT** /helix/id/hexzsq689/api/v3/preferences//hx_url | Specifies the Endpoint (HX) URLs used by Helix.
[**v3_reports_create**](V3Api.md#v3_reports_create) | **POST** /helix/id/hexzsq689/api/v3/reports/ | 
[**v3_reports_delete**](V3Api.md#v3_reports_delete) | **DELETE** /helix/id/hexzsq689/api/v3/reports/ | 
[**v3_reports_delete_0**](V3Api.md#v3_reports_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/reports//{id} | 
[**v3_reports_export_pdf**](V3Api.md#v3_reports_export_pdf) | **GET** /helix/id/hexzsq689/api/v3/reports//{id}/export | 
[**v3_reports_list**](V3Api.md#v3_reports_list) | **GET** /helix/id/hexzsq689/api/v3/reports/ | 
[**v3_reports_partial_update**](V3Api.md#v3_reports_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/reports//{id} | 
[**v3_reports_partial_update0**](V3Api.md#v3_reports_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/reports//{id} | 
[**v3_reports_read**](V3Api.md#v3_reports_read) | **GET** /helix/id/hexzsq689/api/v3/reports//{id} | Override to include widget result serializer
[**v3_reports_search**](V3Api.md#v3_reports_search) | **GET** /helix/id/hexzsq689/api/v3/reports//search | 
[**v3_reports_widgets_create**](V3Api.md#v3_reports_widgets_create) | **POST** /helix/id/hexzsq689/api/v3/reports//{parent_lookup_report}/widgets/ | 
[**v3_reports_widgets_delete**](V3Api.md#v3_reports_widgets_delete) | **DELETE** /helix/id/hexzsq689/api/v3/reports//{parent_lookup_report}/widgets//{widget__id} | 
[**v3_reports_widgets_list**](V3Api.md#v3_reports_widgets_list) | **GET** /helix/id/hexzsq689/api/v3/reports//{parent_lookup_report}/widgets/ | 
[**v3_reports_widgets_partial_update**](V3Api.md#v3_reports_widgets_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/reports//{parent_lookup_report}/widgets//{widget__id} | 
[**v3_reports_widgets_partial_update0**](V3Api.md#v3_reports_widgets_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/reports//{parent_lookup_report}/widgets//{widget__id} | 
[**v3_reports_widgets_read**](V3Api.md#v3_reports_widgets_read) | **GET** /helix/id/hexzsq689/api/v3/reports//{parent_lookup_report}/widgets//{widget__id} | 
[**v3_reports_widgets_view_results**](V3Api.md#v3_reports_widgets_view_results) | **GET** /helix/id/hexzsq689/api/v3/reports//{parent_lookup_report}/widgets//{widget__id}/results | 
[**v3_rules_assertions_list**](V3Api.md#v3_rules_assertions_list) | **GET** /helix/id/hexzsq689/api/v3/rules/assertions/ | Lists rule assertions, including:
[**v3_rules_assertions_read**](V3Api.md#v3_rules_assertions_read) | **GET** /helix/id/hexzsq689/api/v3/rules/assertions//{id} | Lists rule assertions, including:
[**v3_rules_create**](V3Api.md#v3_rules_create) | **POST** /helix/id/hexzsq689/api/v3/rules/ | 
[**v3_rules_dependencies_list**](V3Api.md#v3_rules_dependencies_list) | **GET** /helix/id/hexzsq689/api/v3/rules/dependencies/ | Lists rule dependencies, including:
[**v3_rules_dependencies_read**](V3Api.md#v3_rules_dependencies_read) | **GET** /helix/id/hexzsq689/api/v3/rules/dependencies//{id} | Lists rule dependencies, including:
[**v3_rules_get_enabled_rule_percentages_history**](V3Api.md#v3_rules_get_enabled_rule_percentages_history) | **GET** /helix/id/hexzsq689/api/v3/rules//stats | Calculates a collection of hourly values from the current hour the method is called and the zeroed-out time from today.
[**v3_rules_get_revisions**](V3Api.md#v3_rules_get_revisions) | **GET** /helix/id/hexzsq689/api/v3/rules//{id}/revisions | Returns the revision history of the specified rule.
[**v3_rules_get_rules_recommendations**](V3Api.md#v3_rules_get_rules_recommendations) | **GET** /helix/id/hexzsq689/api/v3/rules//recommendations | Provides class/field recommendations based on the number of impacted rules.
[**v3_rules_list**](V3Api.md#v3_rules_list) | **GET** /helix/id/hexzsq689/api/v3/rules/ | 
[**v3_rules_read**](V3Api.md#v3_rules_read) | **GET** /helix/id/hexzsq689/api/v3/rules//{id} | 
[**v3_search_saved_create**](V3Api.md#v3_search_saved_create) | **POST** /helix/id/hexzsq689/api/v3/search/saved/ | Creates a new search. Defining &#x60;is_favorite&#x60; is optional.
[**v3_search_saved_delete**](V3Api.md#v3_search_saved_delete) | **DELETE** /helix/id/hexzsq689/api/v3/search/saved//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_favorite_create**](V3Api.md#v3_search_saved_favorite_create) | **POST** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/favorite/ | Overrides the default &#39;create&#39; method in order to associate the
[**v3_search_saved_favorite_delete**](V3Api.md#v3_search_saved_favorite_delete) | **DELETE** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/favorite/ | View for tying together the serializer, authentication, permission and
[**v3_search_saved_favorite_delete_0**](V3Api.md#v3_search_saved_favorite_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/favorite//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_favorite_list**](V3Api.md#v3_search_saved_favorite_list) | **GET** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/favorite/ | View for tying together the serializer, authentication, permission and
[**v3_search_saved_favorite_partial_update**](V3Api.md#v3_search_saved_favorite_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/favorite//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_favorite_partial_update0**](V3Api.md#v3_search_saved_favorite_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/favorite//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_favorite_read**](V3Api.md#v3_search_saved_favorite_read) | **GET** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/favorite//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_list**](V3Api.md#v3_search_saved_list) | **GET** /helix/id/hexzsq689/api/v3/search/saved/ | View for tying together the serializer, authentication, permission and
[**v3_search_saved_partial_update**](V3Api.md#v3_search_saved_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/search/saved//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_partial_update0**](V3Api.md#v3_search_saved_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/search/saved//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_read**](V3Api.md#v3_search_saved_read) | **GET** /helix/id/hexzsq689/api/v3/search/saved//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_schedule_create**](V3Api.md#v3_search_saved_schedule_create) | **POST** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule/ | Overrides the default &#39;create&#39; method in order to associate the
[**v3_search_saved_schedule_delete**](V3Api.md#v3_search_saved_schedule_delete) | **DELETE** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule/ | View for tying together the serializer, authentication, permission and
[**v3_search_saved_schedule_delete_0**](V3Api.md#v3_search_saved_schedule_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_schedule_jobs_download**](V3Api.md#v3_search_saved_schedule_jobs_download) | **GET** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule/jobs//{id}/download | Downloads the results of a scheduled search job as a zip file.
[**v3_search_saved_schedule_jobs_list**](V3Api.md#v3_search_saved_schedule_jobs_list) | **GET** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule/jobs/ | Endpoint for accessing scheduled search jobs.
[**v3_search_saved_schedule_jobs_read**](V3Api.md#v3_search_saved_schedule_jobs_read) | **GET** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule/jobs//{id} | Endpoint for accessing scheduled search jobs.
[**v3_search_saved_schedule_list**](V3Api.md#v3_search_saved_schedule_list) | **GET** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule/ | View for tying together the serializer, authentication, permission and
[**v3_search_saved_schedule_partial_update**](V3Api.md#v3_search_saved_schedule_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_schedule_partial_update0**](V3Api.md#v3_search_saved_schedule_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_schedule_read**](V3Api.md#v3_search_saved_schedule_read) | **GET** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule//{id} | View for tying together the serializer, authentication, permission and
[**v3_search_saved_schedule_update**](V3Api.md#v3_search_saved_schedule_update) | **PUT** /helix/id/hexzsq689/api/v3/search/saved//{parent_lookup_saved_search}/schedule/ | View for tying together the serializer, authentication, permission and
[**v3_search_saved_search**](V3Api.md#v3_search_saved_search) | **GET** /helix/id/hexzsq689/api/v3/search/saved//search | View for tying together the serializer, authentication, permission and
[**v3_search_stats_get_indexing_latency**](V3Api.md#v3_search_stats_get_indexing_latency) | **GET** /helix/id/hexzsq689/api/v3/search/stats/indexing/ | 
[**v3_search_tables_create**](V3Api.md#v3_search_tables_create) | **POST** /helix/id/hexzsq689/api/v3/search/tables/ | Endpoint for accessing search tables.
[**v3_search_tables_delete**](V3Api.md#v3_search_tables_delete) | **DELETE** /helix/id/hexzsq689/api/v3/search/tables//{id} | Deletes the specified search table. You can only delete tables that you created.
[**v3_search_tables_list**](V3Api.md#v3_search_tables_list) | **GET** /helix/id/hexzsq689/api/v3/search/tables/ | Endpoint for accessing search tables.
[**v3_search_tables_partial_update**](V3Api.md#v3_search_tables_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/search/tables//{id} | Endpoint for accessing search tables.
[**v3_search_tables_partial_update0**](V3Api.md#v3_search_tables_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/search/tables//{id} | Endpoint for accessing search tables.
[**v3_search_tables_read**](V3Api.md#v3_search_tables_read) | **GET** /helix/id/hexzsq689/api/v3/search/tables//{id} | Endpoint for accessing search tables.
[**v3_senders_create**](V3Api.md#v3_senders_create) | **POST** /helix/id/hexzsq689/api/v3/senders// | 
[**v3_senders_delete**](V3Api.md#v3_senders_delete) | **DELETE** /helix/id/hexzsq689/api/v3/senders// | 
[**v3_senders_enable_delete**](V3Api.md#v3_senders_enable_delete) | **DELETE** /helix/id/hexzsq689/api/v3/senders/enable/ | 
[**v3_senders_enable_update**](V3Api.md#v3_senders_enable_update) | **PUT** /helix/id/hexzsq689/api/v3/senders/enable/ | 
[**v3_senders_read**](V3Api.md#v3_senders_read) | **GET** /helix/id/hexzsq689/api/v3/senders// | 
[**v3_sensors_create**](V3Api.md#v3_sensors_create) | **POST** /helix/id/hexzsq689/api/v3/sensors/ | 
[**v3_sensors_delete**](V3Api.md#v3_sensors_delete) | **DELETE** /helix/id/hexzsq689/api/v3/sensors//{id} | 
[**v3_sensors_get_sensor_status**](V3Api.md#v3_sensors_get_sensor_status) | **GET** /helix/id/hexzsq689/api/v3/sensors//status | Returns the status of your FireEye sensors.
[**v3_sensors_list**](V3Api.md#v3_sensors_list) | **GET** /helix/id/hexzsq689/api/v3/sensors/ | Lists your FireEye sensors, including metrics for input events and average CPU and memory usage.
[**v3_sensors_partial_update**](V3Api.md#v3_sensors_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/sensors//{id} | 
[**v3_sensors_partial_update0**](V3Api.md#v3_sensors_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/sensors//{id} | 
[**v3_sensors_read**](V3Api.md#v3_sensors_read) | **GET** /helix/id/hexzsq689/api/v3/sensors//{id} | 
[**v3_tags_list**](V3Api.md#v3_tags_list) | **GET** /helix/id/hexzsq689/api/v3/tags/ | 
[**v3_tasks_status_read**](V3Api.md#v3_tasks_status_read) | **GET** /helix/id/hexzsq689/api/v3/tasks/status/{id}/ | 
[**v3_user_challenge_query**](V3Api.md#v3_user_challenge_query) | **GET** /helix/id/hexzsq689/api/v3/user//challenge-query | Returns a token to use for Talk to an Expert.
[**v3_user_customer_support_chat**](V3Api.md#v3_user_customer_support_chat) | **GET** /helix/id/hexzsq689/api/v3/user//chat | Connects to SFDC to chat with FireEye Support.
[**v3_user_eod_chat**](V3Api.md#v3_user_eod_chat) | **GET** /helix/id/hexzsq689/api/v3/user//expert | Returns Expert on Demand contact information for authorized users.
[**v3_widgets_templates_create**](V3Api.md#v3_widgets_templates_create) | **POST** /helix/id/hexzsq689/api/v3/widgets/templates/ | View for tying together the serializer, authentication, permission and
[**v3_widgets_templates_delete**](V3Api.md#v3_widgets_templates_delete) | **DELETE** /helix/id/hexzsq689/api/v3/widgets/templates/ | Deletes all widgets from the specified dashboard.
[**v3_widgets_templates_delete_0**](V3Api.md#v3_widgets_templates_delete_0) | **DELETE** /helix/id/hexzsq689/api/v3/widgets/templates//{id} | Deletes a widget from the specified dashboard.
[**v3_widgets_templates_list**](V3Api.md#v3_widgets_templates_list) | **GET** /helix/id/hexzsq689/api/v3/widgets/templates/ | View for tying together the serializer, authentication, permission and
[**v3_widgets_templates_partial_update**](V3Api.md#v3_widgets_templates_partial_update) | **PUT** /helix/id/hexzsq689/api/v3/widgets/templates//{id} | View for tying together the serializer, authentication, permission and
[**v3_widgets_templates_partial_update0**](V3Api.md#v3_widgets_templates_partial_update0) | **PATCH** /helix/id/hexzsq689/api/v3/widgets/templates//{id} | View for tying together the serializer, authentication, permission and
[**v3_widgets_templates_perform_search**](V3Api.md#v3_widgets_templates_perform_search) | **GET** /helix/id/hexzsq689/api/v3/widgets/templates//{id}/results/ | Returns the results of a dashboard widget.
[**v3_widgets_templates_read**](V3Api.md#v3_widgets_templates_read) | **GET** /helix/id/hexzsq689/api/v3/widgets/templates//{id} | View for tying together the serializer, authentication, permission and
[**v3_widgets_templates_search**](V3Api.md#v3_widgets_templates_search) | **GET** /helix/id/hexzsq689/api/v3/widgets/templates//search | View for tying together the serializer, authentication, permission and
[**v3_widgets_templates_update**](V3Api.md#v3_widgets_templates_update) | **PUT** /helix/id/hexzsq689/api/v3/widgets/templates/ | Updates all widgets for the specified dashboard.


# **v3_alerts_cases_create**
> v3_alerts_cases_create(parent_lookup_alerts, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alerts = 'parent_lookup_alerts_example' # str | 
data = fireeye.helix.InlineObject106() # InlineObject106 |  (optional)

try:
    api_instance.v3_alerts_cases_create(parent_lookup_alerts, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_cases_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alerts** | **str**|  | 
 **data** | [**InlineObject106**](InlineObject106.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_cases_delete**
> v3_alerts_cases_delete(parent_lookup_alerts)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alerts = 'parent_lookup_alerts_example' # str | 

try:
    api_instance.v3_alerts_cases_delete(parent_lookup_alerts)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_cases_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alerts** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_cases_delete_0**
> v3_alerts_cases_delete_0(parent_lookup_alerts, id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alerts = 'parent_lookup_alerts_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_cases_delete_0(parent_lookup_alerts, id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_cases_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alerts** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_cases_list**
> v3_alerts_cases_list(parent_lookup_alerts, limit=limit, offset=offset, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alerts = 'parent_lookup_alerts_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_cases_list(parent_lookup_alerts, limit=limit, offset=offset, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_cases_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alerts** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_cases_partial_update**
> v3_alerts_cases_partial_update(parent_lookup_alerts, id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alerts = 'parent_lookup_alerts_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject107() # InlineObject107 |  (optional)

try:
    api_instance.v3_alerts_cases_partial_update(parent_lookup_alerts, id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_cases_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alerts** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject107**](InlineObject107.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_cases_partial_update0**
> v3_alerts_cases_partial_update0(parent_lookup_alerts, id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alerts = 'parent_lookup_alerts_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject108() # InlineObject108 |  (optional)

try:
    api_instance.v3_alerts_cases_partial_update0(parent_lookup_alerts, id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_cases_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alerts** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject108**](InlineObject108.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_cases_read**
> v3_alerts_cases_read(parent_lookup_alerts, id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alerts = 'parent_lookup_alerts_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_cases_read(parent_lookup_alerts, id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_cases_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alerts** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_cases_search**
> v3_alerts_cases_search(parent_lookup_alerts)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alerts = 'parent_lookup_alerts_example' # str | 

try:
    api_instance.v3_alerts_cases_search(parent_lookup_alerts)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_cases_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alerts** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_create**
> v3_alerts_create(data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject105() # InlineObject105 |  (optional)

try:
    api_instance.v3_alerts_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject105**](InlineObject105.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_enum_fields**
> v3_alerts_get_enum_fields()

Lists all fields that describe alerts.

Lists all fields that describe alerts.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Lists all fields that describe alerts.
    api_instance.v3_alerts_get_enum_fields()
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_enum_fields: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_events**
> v3_alerts_get_events(id)

Lists alert events for a specific alert.

Lists alert events for a specific alert.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Lists alert events for a specific alert.
    api_instance.v3_alerts_get_events(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_hx_host_endpoints**
> v3_alerts_get_hx_host_endpoints(id)

Retrieves a specific alert from an HX endpoint.

Retrieves a specific alert from an HX endpoint.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Retrieves a specific alert from an HX endpoint.
    api_instance.v3_alerts_get_hx_host_endpoints(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_hx_host_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_intel_context**
> v3_alerts_get_intel_context(id)

Gets the instances and indicators for a specific alert.

Gets the instances and indicators for a specific alert.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Gets the instances and indicators for a specific alert.
    api_instance.v3_alerts_get_intel_context(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_intel_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_investigative_tips**
> v3_alerts_get_investigative_tips(id)

Lists the investigative tips for a specific alert.

Lists the investigative tips for a specific alert.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Lists the investigative tips for a specific alert.
    api_instance.v3_alerts_get_investigative_tips(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_investigative_tips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_md_investigation_results**
> v3_alerts_get_md_investigation_results(id)

Retrieves Managed Defense investigation results for an alert.

Retrieves Managed Defense investigation results for an alert.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Retrieves Managed Defense investigation results for an alert.
    api_instance.v3_alerts_get_md_investigation_results(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_md_investigation_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_org_metrics**
> v3_alerts_get_org_metrics()

Lists alert metrics by organization.

Lists alert metrics by organization.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Lists alert metrics by organization.
    api_instance.v3_alerts_get_org_metrics()
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_org_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_revisions**
> v3_alerts_get_revisions(id)

Returns the revision history.

Returns the revision history.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Returns the revision history.
    api_instance.v3_alerts_get_revisions(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_revisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_get_unique_values**
> v3_alerts_get_unique_values()

Lists the number of occurrences of each field value.

Lists the number of occurrences of each field value.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Lists the number of occurrences of each field value.
    api_instance.v3_alerts_get_unique_values()
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_get_unique_values: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_list**
> v3_alerts_list(limit=limit, offset=offset, alert_threat=alert_threat, alert_type=alert_type, alert_type_destination=alert_type_destination, alert_type_source=alert_type_source, alert_type_srcdst=alert_type_srcdst, alert_type_summary=alert_type_summary, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, distinguishers=distinguishers, mongo_id=mongo_id, is_suppressed=is_suppressed, is_threat=is_threat, is_tuned=is_tuned, message=message, origin_id=origin_id, organization=organization, queues=queues, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, type=type, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updated_by=updated_by, metaclasses=metaclasses, products=products, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
alert_threat = 'alert_threat_example' # str |  (optional)
alert_type = 'alert_type_example' # str |  (optional)
alert_type_destination = 'alert_type_destination_example' # str |  (optional)
alert_type_source = 'alert_type_source_example' # str |  (optional)
alert_type_srcdst = 'alert_type_srcdst_example' # str |  (optional)
alert_type_summary = 'alert_type_summary_example' # str |  (optional)
assigned_to = 'assigned_to_example' # str |  (optional)
classification = 3.4 # float |  (optional)
closed_state = 'closed_state_example' # str |  (optional)
confidence = 'confidence_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
distinguishers = 'distinguishers_example' # str |  (optional)
mongo_id = 'mongo_id_example' # str |  (optional)
is_suppressed = 'is_suppressed_example' # str |  (optional)
is_threat = 'is_threat_example' # str |  (optional)
is_tuned = 'is_tuned_example' # str |  (optional)
message = 'message_example' # str |  (optional)
origin_id = 'origin_id_example' # str |  (optional)
organization = 'organization_example' # str |  (optional)
queues = 'queues_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
state = 'state_example' # str |  (optional)
threat_type = 3.4 # float |  (optional)
trigger_id = 'trigger_id_example' # str |  (optional)
trigger_revision = 3.4 # float |  (optional)
type = 'type_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
metaclasses = 'metaclasses_example' # str |  (optional)
products = 'products_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_list(limit=limit, offset=offset, alert_threat=alert_threat, alert_type=alert_type, alert_type_destination=alert_type_destination, alert_type_source=alert_type_source, alert_type_srcdst=alert_type_srcdst, alert_type_summary=alert_type_summary, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, distinguishers=distinguishers, mongo_id=mongo_id, is_suppressed=is_suppressed, is_threat=is_threat, is_tuned=is_tuned, message=message, origin_id=origin_id, organization=organization, queues=queues, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, type=type, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updated_by=updated_by, metaclasses=metaclasses, products=products, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **alert_threat** | **str**|  | [optional] 
 **alert_type** | **str**|  | [optional] 
 **alert_type_destination** | **str**|  | [optional] 
 **alert_type_source** | **str**|  | [optional] 
 **alert_type_srcdst** | **str**|  | [optional] 
 **alert_type_summary** | **str**|  | [optional] 
 **assigned_to** | **str**|  | [optional] 
 **classification** | **float**|  | [optional] 
 **closed_state** | **str**|  | [optional] 
 **confidence** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **distinguishers** | **str**|  | [optional] 
 **mongo_id** | **str**|  | [optional] 
 **is_suppressed** | **str**|  | [optional] 
 **is_threat** | **str**|  | [optional] 
 **is_tuned** | **str**|  | [optional] 
 **message** | **str**|  | [optional] 
 **origin_id** | **str**|  | [optional] 
 **organization** | **str**|  | [optional] 
 **queues** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **threat_type** | **float**|  | [optional] 
 **trigger_id** | **str**|  | [optional] 
 **trigger_revision** | **float**|  | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **metaclasses** | **str**|  | [optional] 
 **products** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_notes_create**
> v3_alerts_notes_create(parent_lookup_object_id, data=data)

Adds a note to the specified alert or case.

Adds a note to the specified alert or case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
data = fireeye.helix.InlineObject109() # InlineObject109 |  (optional)

try:
    # Adds a note to the specified alert or case.
    api_instance.v3_alerts_notes_create(parent_lookup_object_id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_notes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **data** | [**InlineObject109**](InlineObject109.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_notes_delete**
> v3_alerts_notes_delete(parent_lookup_object_id, id, order_by=order_by)

Deletes the specified note.

Deletes the specified note. You can only delete notes that you created.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Deletes the specified note.
    api_instance.v3_alerts_notes_delete(parent_lookup_object_id, id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_notes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_notes_list**
> v3_alerts_notes_list(parent_lookup_object_id, limit=limit, offset=offset, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_notes_list(parent_lookup_object_id, limit=limit, offset=offset, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_notes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_notes_partial_update**
> v3_alerts_notes_partial_update(parent_lookup_object_id, id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject110() # InlineObject110 |  (optional)

try:
    api_instance.v3_alerts_notes_partial_update(parent_lookup_object_id, id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_notes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject110**](InlineObject110.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_notes_partial_update0**
> v3_alerts_notes_partial_update0(parent_lookup_object_id, id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject111() # InlineObject111 |  (optional)

try:
    api_instance.v3_alerts_notes_partial_update0(parent_lookup_object_id, id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_notes_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject111**](InlineObject111.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_notes_read**
> v3_alerts_notes_read(parent_lookup_object_id, id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_notes_read(parent_lookup_object_id, id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_notes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_plays_list**
> v3_alerts_plays_list(parent_lookup_alert, limit=limit, offset=offset, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alert = 'parent_lookup_alert_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_plays_list(parent_lookup_alert, limit=limit, offset=offset, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_plays_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alert** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_plays_read**
> v3_alerts_plays_read(parent_lookup_alert, id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alert = 'parent_lookup_alert_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_plays_read(parent_lookup_alert, id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_plays_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alert** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_plays_search**
> v3_alerts_plays_search(parent_lookup_alert)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_alert = 'parent_lookup_alert_example' # str | 

try:
    api_instance.v3_alerts_plays_search(parent_lookup_alert)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_plays_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_alert** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_read**
> v3_alerts_read(id, alert_threat=alert_threat, alert_type=alert_type, alert_type_destination=alert_type_destination, alert_type_source=alert_type_source, alert_type_srcdst=alert_type_srcdst, alert_type_summary=alert_type_summary, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, distinguishers=distinguishers, mongo_id=mongo_id, is_suppressed=is_suppressed, is_threat=is_threat, is_tuned=is_tuned, message=message, origin_id=origin_id, organization=organization, queues=queues, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, type=type, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updated_by=updated_by, metaclasses=metaclasses, products=products, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
alert_threat = 'alert_threat_example' # str |  (optional)
alert_type = 'alert_type_example' # str |  (optional)
alert_type_destination = 'alert_type_destination_example' # str |  (optional)
alert_type_source = 'alert_type_source_example' # str |  (optional)
alert_type_srcdst = 'alert_type_srcdst_example' # str |  (optional)
alert_type_summary = 'alert_type_summary_example' # str |  (optional)
assigned_to = 'assigned_to_example' # str |  (optional)
classification = 3.4 # float |  (optional)
closed_state = 'closed_state_example' # str |  (optional)
confidence = 'confidence_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
distinguishers = 'distinguishers_example' # str |  (optional)
mongo_id = 'mongo_id_example' # str |  (optional)
is_suppressed = 'is_suppressed_example' # str |  (optional)
is_threat = 'is_threat_example' # str |  (optional)
is_tuned = 'is_tuned_example' # str |  (optional)
message = 'message_example' # str |  (optional)
origin_id = 'origin_id_example' # str |  (optional)
organization = 'organization_example' # str |  (optional)
queues = 'queues_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
state = 'state_example' # str |  (optional)
threat_type = 3.4 # float |  (optional)
trigger_id = 'trigger_id_example' # str |  (optional)
trigger_revision = 3.4 # float |  (optional)
type = 'type_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
metaclasses = 'metaclasses_example' # str |  (optional)
products = 'products_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_read(id, alert_threat=alert_threat, alert_type=alert_type, alert_type_destination=alert_type_destination, alert_type_source=alert_type_source, alert_type_srcdst=alert_type_srcdst, alert_type_summary=alert_type_summary, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, distinguishers=distinguishers, mongo_id=mongo_id, is_suppressed=is_suppressed, is_threat=is_threat, is_tuned=is_tuned, message=message, origin_id=origin_id, organization=organization, queues=queues, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, type=type, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updated_by=updated_by, metaclasses=metaclasses, products=products, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **alert_threat** | **str**|  | [optional] 
 **alert_type** | **str**|  | [optional] 
 **alert_type_destination** | **str**|  | [optional] 
 **alert_type_source** | **str**|  | [optional] 
 **alert_type_srcdst** | **str**|  | [optional] 
 **alert_type_summary** | **str**|  | [optional] 
 **assigned_to** | **str**|  | [optional] 
 **classification** | **float**|  | [optional] 
 **closed_state** | **str**|  | [optional] 
 **confidence** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **distinguishers** | **str**|  | [optional] 
 **mongo_id** | **str**|  | [optional] 
 **is_suppressed** | **str**|  | [optional] 
 **is_threat** | **str**|  | [optional] 
 **is_tuned** | **str**|  | [optional] 
 **message** | **str**|  | [optional] 
 **origin_id** | **str**|  | [optional] 
 **organization** | **str**|  | [optional] 
 **queues** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **threat_type** | **float**|  | [optional] 
 **trigger_id** | **str**|  | [optional] 
 **trigger_revision** | **float**|  | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **metaclasses** | **str**|  | [optional] 
 **products** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_search**
> v3_alerts_search()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_alerts_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_types_create**
> v3_alerts_types_create(data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject112() # InlineObject112 |  (optional)

try:
    api_instance.v3_alerts_types_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject112**](InlineObject112.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_types_delete**
> v3_alerts_types_delete(id, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_types_delete(id, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_types_list**
> v3_alerts_types_list(limit=limit, offset=offset, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_types_list(limit=limit, offset=offset, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_types_partial_update**
> v3_alerts_types_partial_update(id, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject113() # InlineObject113 |  (optional)

try:
    api_instance.v3_alerts_types_partial_update(id, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject113**](InlineObject113.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_types_partial_update0**
> v3_alerts_types_partial_update0(id, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject114() # InlineObject114 |  (optional)

try:
    api_instance.v3_alerts_types_partial_update0(id, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_types_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject114**](InlineObject114.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_types_read**
> v3_alerts_types_read(id, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_alerts_types_read(id, category=category, is_internal=is_internal, type_id=type_id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_alerts_types_search**
> v3_alerts_types_search()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_alerts_types_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_alerts_types_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_appliances_get_appliance_health**
> v3_appliances_get_appliance_health()

Provides a summary of the health of your FireEye network appliances.

Provides a summary of the health of your FireEye network appliances.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Provides a summary of the health of your FireEye network appliances.
    api_instance.v3_appliances_get_appliance_health()
except ApiException as e:
    print("Exception when calling V3Api->v3_appliances_get_appliance_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_appliances_list**
> v3_appliances_list()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_appliances_list()
except ApiException as e:
    print("Exception when calling V3Api->v3_appliances_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_appliances_read**
> v3_appliances_read(id)

Searches for appliance by ID (the deviceid from GET /appliances).

Searches for appliance by ID (the deviceid from GET /appliances). :param request: Request object :param args: Arguments :param kwargs: Keyword Arguments :return: Dictionary of results from MqlClient response

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Searches for appliance by ID (the deviceid from GET /appliances).
    api_instance.v3_appliances_read(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_appliances_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_artifacts_create**
> v3_automation_jobs_artifacts_create(parent_lookup_play_execution, data=data)

Overrides the default 'create' method in order to associate the

Overrides the default 'create' method in order to associate the parent_lookup that may be in the URL parameters due to nested routes

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_play_execution = 'parent_lookup_play_execution_example' # str | 
data = fireeye.helix.InlineObject118() # InlineObject118 |  (optional)

try:
    # Overrides the default 'create' method in order to associate the
    api_instance.v3_automation_jobs_artifacts_create(parent_lookup_play_execution, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_artifacts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_play_execution** | **str**|  | 
 **data** | [**InlineObject118**](InlineObject118.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_artifacts_delete**
> v3_automation_jobs_artifacts_delete(parent_lookup_play_execution, id, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_play_execution = 'parent_lookup_play_execution_example' # str | 
id = 'id_example' # str | 
content_type = 'content_type_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_automation_jobs_artifacts_delete(parent_lookup_play_execution, id, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_artifacts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_play_execution** | **str**|  | 
 **id** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_artifacts_list**
> v3_automation_jobs_artifacts_list(parent_lookup_play_execution, limit=limit, offset=offset, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_play_execution = 'parent_lookup_play_execution_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
content_type = 'content_type_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_automation_jobs_artifacts_list(parent_lookup_play_execution, limit=limit, offset=offset, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_artifacts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_play_execution** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **content_type** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_artifacts_partial_update**
> v3_automation_jobs_artifacts_partial_update(parent_lookup_play_execution, id, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_play_execution = 'parent_lookup_play_execution_example' # str | 
id = 'id_example' # str | 
content_type = 'content_type_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject119() # InlineObject119 |  (optional)

try:
    api_instance.v3_automation_jobs_artifacts_partial_update(parent_lookup_play_execution, id, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_artifacts_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_play_execution** | **str**|  | 
 **id** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject119**](InlineObject119.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_artifacts_partial_update0**
> v3_automation_jobs_artifacts_partial_update0(parent_lookup_play_execution, id, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_play_execution = 'parent_lookup_play_execution_example' # str | 
id = 'id_example' # str | 
content_type = 'content_type_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject120() # InlineObject120 |  (optional)

try:
    api_instance.v3_automation_jobs_artifacts_partial_update0(parent_lookup_play_execution, id, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_artifacts_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_play_execution** | **str**|  | 
 **id** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject120**](InlineObject120.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_artifacts_read**
> v3_automation_jobs_artifacts_read(parent_lookup_play_execution, id, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_play_execution = 'parent_lookup_play_execution_example' # str | 
id = 'id_example' # str | 
content_type = 'content_type_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_automation_jobs_artifacts_read(parent_lookup_play_execution, id, content_type=content_type, created_by=created_by, filename=filename, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_artifacts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_play_execution** | **str**|  | 
 **id** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_artifacts_search**
> v3_automation_jobs_artifacts_search(parent_lookup_play_execution)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_play_execution = 'parent_lookup_play_execution_example' # str | 

try:
    api_instance.v3_automation_jobs_artifacts_search(parent_lookup_play_execution)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_artifacts_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_play_execution** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_create**
> v3_automation_jobs_create(data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject115() # InlineObject115 |  (optional)

try:
    api_instance.v3_automation_jobs_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject115**](InlineObject115.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_delete**
> v3_automation_jobs_delete(id, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
alert__mongo_id = 'alert__mongo_id_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
status = 'status_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_automation_jobs_delete(id, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **alert__mongo_id** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_list**
> v3_automation_jobs_list(limit=limit, offset=offset, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
alert__mongo_id = 'alert__mongo_id_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
status = 'status_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_automation_jobs_list(limit=limit, offset=offset, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **alert__mongo_id** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_partial_update**
> v3_automation_jobs_partial_update(id, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
alert__mongo_id = 'alert__mongo_id_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
status = 'status_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject116() # InlineObject116 |  (optional)

try:
    api_instance.v3_automation_jobs_partial_update(id, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **alert__mongo_id** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject116**](InlineObject116.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_partial_update0**
> v3_automation_jobs_partial_update0(id, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
alert__mongo_id = 'alert__mongo_id_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
status = 'status_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject117() # InlineObject117 |  (optional)

try:
    api_instance.v3_automation_jobs_partial_update0(id, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **alert__mongo_id** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject117**](InlineObject117.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_read**
> v3_automation_jobs_read(id, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
alert__mongo_id = 'alert__mongo_id_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
status = 'status_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_automation_jobs_read(id, alert__mongo_id=alert__mongo_id, created_by=created_by, status=status, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **alert__mongo_id** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_automation_jobs_search**
> v3_automation_jobs_search()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_automation_jobs_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_automation_jobs_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_create**
> v3_cases_alerts_create(parent_lookup_incidents, data=data)

Alerts associated with a case.

Alerts associated with a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 
data = fireeye.helix.InlineObject125() # InlineObject125 |  (optional)

try:
    # Alerts associated with a case.
    api_instance.v3_cases_alerts_create(parent_lookup_incidents, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_incidents** | **str**|  | 
 **data** | [**InlineObject125**](InlineObject125.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_delete**
> v3_cases_alerts_delete(parent_lookup_incidents)

Removes all alerts from a case.

Removes all alerts from a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 

try:
    # Removes all alerts from a case.
    api_instance.v3_cases_alerts_delete(parent_lookup_incidents)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_incidents** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_delete_0**
> v3_cases_alerts_delete_0(id, parent_lookup_incidents, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by)

Removes the specified alert from a case.

Removes the specified alert from a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 
assigned_to = 'assigned_to_example' # str |  (optional)
classification = 3.4 # float |  (optional)
closed_state = 'closed_state_example' # str |  (optional)
confidence = 'confidence_example' # str |  (optional)
is_suppressed = 'is_suppressed_example' # str |  (optional)
is_tuned = 'is_tuned_example' # str |  (optional)
origin_id = 'origin_id_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
state = 'state_example' # str |  (optional)
threat_type = 3.4 # float |  (optional)
trigger_id = 'trigger_id_example' # str |  (optional)
trigger_revision = 3.4 # float |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Removes the specified alert from a case.
    api_instance.v3_cases_alerts_delete_0(id, parent_lookup_incidents, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_incidents** | **str**|  | 
 **assigned_to** | **str**|  | [optional] 
 **classification** | **float**|  | [optional] 
 **closed_state** | **str**|  | [optional] 
 **confidence** | **str**|  | [optional] 
 **is_suppressed** | **str**|  | [optional] 
 **is_tuned** | **str**|  | [optional] 
 **origin_id** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **threat_type** | **float**|  | [optional] 
 **trigger_id** | **str**|  | [optional] 
 **trigger_revision** | **float**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_list**
> v3_cases_alerts_list(parent_lookup_incidents, limit=limit, offset=offset, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by)

Alerts associated with a case.

Alerts associated with a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
assigned_to = 'assigned_to_example' # str |  (optional)
classification = 3.4 # float |  (optional)
closed_state = 'closed_state_example' # str |  (optional)
confidence = 'confidence_example' # str |  (optional)
is_suppressed = 'is_suppressed_example' # str |  (optional)
is_tuned = 'is_tuned_example' # str |  (optional)
origin_id = 'origin_id_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
state = 'state_example' # str |  (optional)
threat_type = 3.4 # float |  (optional)
trigger_id = 'trigger_id_example' # str |  (optional)
trigger_revision = 3.4 # float |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Alerts associated with a case.
    api_instance.v3_cases_alerts_list(parent_lookup_incidents, limit=limit, offset=offset, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_incidents** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **assigned_to** | **str**|  | [optional] 
 **classification** | **float**|  | [optional] 
 **closed_state** | **str**|  | [optional] 
 **confidence** | **str**|  | [optional] 
 **is_suppressed** | **str**|  | [optional] 
 **is_tuned** | **str**|  | [optional] 
 **origin_id** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **threat_type** | **float**|  | [optional] 
 **trigger_id** | **str**|  | [optional] 
 **trigger_revision** | **float**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_partial_update**
> v3_cases_alerts_partial_update(id, parent_lookup_incidents, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by, data=data)

Alerts associated with a case.

Alerts associated with a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 
assigned_to = 'assigned_to_example' # str |  (optional)
classification = 3.4 # float |  (optional)
closed_state = 'closed_state_example' # str |  (optional)
confidence = 'confidence_example' # str |  (optional)
is_suppressed = 'is_suppressed_example' # str |  (optional)
is_tuned = 'is_tuned_example' # str |  (optional)
origin_id = 'origin_id_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
state = 'state_example' # str |  (optional)
threat_type = 3.4 # float |  (optional)
trigger_id = 'trigger_id_example' # str |  (optional)
trigger_revision = 3.4 # float |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject126() # InlineObject126 |  (optional)

try:
    # Alerts associated with a case.
    api_instance.v3_cases_alerts_partial_update(id, parent_lookup_incidents, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_incidents** | **str**|  | 
 **assigned_to** | **str**|  | [optional] 
 **classification** | **float**|  | [optional] 
 **closed_state** | **str**|  | [optional] 
 **confidence** | **str**|  | [optional] 
 **is_suppressed** | **str**|  | [optional] 
 **is_tuned** | **str**|  | [optional] 
 **origin_id** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **threat_type** | **float**|  | [optional] 
 **trigger_id** | **str**|  | [optional] 
 **trigger_revision** | **float**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject126**](InlineObject126.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_partial_update0**
> v3_cases_alerts_partial_update0(id, parent_lookup_incidents, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by, data=data)

Alerts associated with a case.

Alerts associated with a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 
assigned_to = 'assigned_to_example' # str |  (optional)
classification = 3.4 # float |  (optional)
closed_state = 'closed_state_example' # str |  (optional)
confidence = 'confidence_example' # str |  (optional)
is_suppressed = 'is_suppressed_example' # str |  (optional)
is_tuned = 'is_tuned_example' # str |  (optional)
origin_id = 'origin_id_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
state = 'state_example' # str |  (optional)
threat_type = 3.4 # float |  (optional)
trigger_id = 'trigger_id_example' # str |  (optional)
trigger_revision = 3.4 # float |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject127() # InlineObject127 |  (optional)

try:
    # Alerts associated with a case.
    api_instance.v3_cases_alerts_partial_update0(id, parent_lookup_incidents, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_incidents** | **str**|  | 
 **assigned_to** | **str**|  | [optional] 
 **classification** | **float**|  | [optional] 
 **closed_state** | **str**|  | [optional] 
 **confidence** | **str**|  | [optional] 
 **is_suppressed** | **str**|  | [optional] 
 **is_tuned** | **str**|  | [optional] 
 **origin_id** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **threat_type** | **float**|  | [optional] 
 **trigger_id** | **str**|  | [optional] 
 **trigger_revision** | **float**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject127**](InlineObject127.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_read**
> v3_cases_alerts_read(id, parent_lookup_incidents, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by)

Alerts associated with a case.

Alerts associated with a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 
assigned_to = 'assigned_to_example' # str |  (optional)
classification = 3.4 # float |  (optional)
closed_state = 'closed_state_example' # str |  (optional)
confidence = 'confidence_example' # str |  (optional)
is_suppressed = 'is_suppressed_example' # str |  (optional)
is_tuned = 'is_tuned_example' # str |  (optional)
origin_id = 'origin_id_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
state = 'state_example' # str |  (optional)
threat_type = 3.4 # float |  (optional)
trigger_id = 'trigger_id_example' # str |  (optional)
trigger_revision = 3.4 # float |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Alerts associated with a case.
    api_instance.v3_cases_alerts_read(id, parent_lookup_incidents, assigned_to=assigned_to, classification=classification, closed_state=closed_state, confidence=confidence, is_suppressed=is_suppressed, is_tuned=is_tuned, origin_id=origin_id, risk=risk, severity=severity, state=state, threat_type=threat_type, trigger_id=trigger_id, trigger_revision=trigger_revision, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_incidents** | **str**|  | 
 **assigned_to** | **str**|  | [optional] 
 **classification** | **float**|  | [optional] 
 **closed_state** | **str**|  | [optional] 
 **confidence** | **str**|  | [optional] 
 **is_suppressed** | **str**|  | [optional] 
 **is_tuned** | **str**|  | [optional] 
 **origin_id** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **threat_type** | **float**|  | [optional] 
 **trigger_id** | **str**|  | [optional] 
 **trigger_revision** | **float**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_search**
> v3_cases_alerts_search(parent_lookup_incidents)

Alerts associated with a case.

Alerts associated with a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 

try:
    # Alerts associated with a case.
    api_instance.v3_cases_alerts_search(parent_lookup_incidents)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_incidents** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_alerts_update**
> v3_cases_alerts_update(parent_lookup_incidents, data=data)

Alerts associated with a case.

Alerts associated with a case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_incidents = 'parent_lookup_incidents_example' # str | 
data = fireeye.helix.InlineObject124() # InlineObject124 |  (optional)

try:
    # Alerts associated with a case.
    api_instance.v3_cases_alerts_update(parent_lookup_incidents, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_alerts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_incidents** | **str**|  | 
 **data** | [**InlineObject124**](InlineObject124.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_create**
> v3_cases_create(data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject121() # InlineObject121 |  (optional)

try:
    api_instance.v3_cases_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject121**](InlineObject121.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_delete**
> v3_cases_delete(id, assigned_to=assigned_to, created_by=created_by, id2=id2, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
assigned_to = 'assigned_to_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
id2 = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
priority = 'priority_example' # str |  (optional)
severity = 3.4 # float |  (optional)
state = 'state_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_cases_delete(id, assigned_to=assigned_to, created_by=created_by, id2=id2, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **assigned_to** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **id2** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **priority** | **str**|  | [optional] 
 **severity** | **float**|  | [optional] 
 **state** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_export_all**
> v3_cases_export_all()

Creates an export file in JSON format.

Creates an export file in JSON format.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Creates an export file in JSON format.
    api_instance.v3_cases_export_all()
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_export_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_export_single**
> v3_cases_export_single(id)

Exports the specified case to a JSON file.

Exports the specified case to a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Exports the specified case to a JSON file.
    api_instance.v3_cases_export_single(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_export_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_get_all_existing_case_statuses_with_counts**
> v3_cases_get_all_existing_case_statuses_with_counts()

Returns an object containing various status values with their respective counts.

Returns an object containing various status values with their respective counts.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Returns an object containing various status values with their respective counts.
    api_instance.v3_cases_get_all_existing_case_statuses_with_counts()
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_get_all_existing_case_statuses_with_counts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_get_all_tags**
> v3_cases_get_all_tags()

Retrieves the number of tags associated with cases and the tags themselves.

Retrieves the number of tags associated with cases and the tags themselves.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Retrieves the number of tags associated with cases and the tags themselves.
    api_instance.v3_cases_get_all_tags()
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_get_all_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_get_revisions**
> v3_cases_get_revisions(id)

Returns the revision history.

Returns the revision history.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Returns the revision history.
    api_instance.v3_cases_get_revisions(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_get_revisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_list**
> v3_cases_list(limit=limit, offset=offset, assigned_to=assigned_to, created_by=created_by, id=id, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
assigned_to = 'assigned_to_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
priority = 'priority_example' # str |  (optional)
severity = 3.4 # float |  (optional)
state = 'state_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_cases_list(limit=limit, offset=offset, assigned_to=assigned_to, created_by=created_by, id=id, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **assigned_to** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **priority** | **str**|  | [optional] 
 **severity** | **float**|  | [optional] 
 **state** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_notes_create**
> v3_cases_notes_create(parent_lookup_object_id, data=data)

Adds a note to the specified alert or case.

Adds a note to the specified alert or case.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
data = fireeye.helix.InlineObject128() # InlineObject128 |  (optional)

try:
    # Adds a note to the specified alert or case.
    api_instance.v3_cases_notes_create(parent_lookup_object_id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_notes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **data** | [**InlineObject128**](InlineObject128.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_notes_delete**
> v3_cases_notes_delete(parent_lookup_object_id, id, order_by=order_by)

Deletes the specified note.

Deletes the specified note. You can only delete notes that you created.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Deletes the specified note.
    api_instance.v3_cases_notes_delete(parent_lookup_object_id, id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_notes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_notes_list**
> v3_cases_notes_list(parent_lookup_object_id, limit=limit, offset=offset, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_cases_notes_list(parent_lookup_object_id, limit=limit, offset=offset, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_notes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_notes_partial_update**
> v3_cases_notes_partial_update(parent_lookup_object_id, id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject129() # InlineObject129 |  (optional)

try:
    api_instance.v3_cases_notes_partial_update(parent_lookup_object_id, id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_notes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject129**](InlineObject129.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_notes_partial_update0**
> v3_cases_notes_partial_update0(parent_lookup_object_id, id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject130() # InlineObject130 |  (optional)

try:
    api_instance.v3_cases_notes_partial_update0(parent_lookup_object_id, id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_notes_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject130**](InlineObject130.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_notes_read**
> v3_cases_notes_read(parent_lookup_object_id, id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_object_id = 'parent_lookup_object_id_example' # str | 
id = 'id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_cases_notes_read(parent_lookup_object_id, id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_notes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_object_id** | **str**|  | 
 **id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_partial_update**
> v3_cases_partial_update(id, assigned_to=assigned_to, created_by=created_by, id2=id2, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
assigned_to = 'assigned_to_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
id2 = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
priority = 'priority_example' # str |  (optional)
severity = 3.4 # float |  (optional)
state = 'state_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject122() # InlineObject122 |  (optional)

try:
    api_instance.v3_cases_partial_update(id, assigned_to=assigned_to, created_by=created_by, id2=id2, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **assigned_to** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **id2** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **priority** | **str**|  | [optional] 
 **severity** | **float**|  | [optional] 
 **state** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject122**](InlineObject122.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_partial_update0**
> v3_cases_partial_update0(id, assigned_to=assigned_to, created_by=created_by, id2=id2, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
assigned_to = 'assigned_to_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
id2 = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
priority = 'priority_example' # str |  (optional)
severity = 3.4 # float |  (optional)
state = 'state_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject123() # InlineObject123 |  (optional)

try:
    api_instance.v3_cases_partial_update0(id, assigned_to=assigned_to, created_by=created_by, id2=id2, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **assigned_to** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **id2** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **priority** | **str**|  | [optional] 
 **severity** | **float**|  | [optional] 
 **state** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject123**](InlineObject123.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_read**
> v3_cases_read(id, assigned_to=assigned_to, created_by=created_by, id2=id2, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
assigned_to = 'assigned_to_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
id2 = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
priority = 'priority_example' # str |  (optional)
severity = 3.4 # float |  (optional)
state = 'state_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_cases_read(id, assigned_to=assigned_to, created_by=created_by, id2=id2, name=name, priority=priority, severity=severity, state=state, status=status, tags=tags, updated_by=updated_by, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **assigned_to** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **id2** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **priority** | **str**|  | [optional] 
 **severity** | **float**|  | [optional] 
 **state** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cases_search**
> v3_cases_search()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_cases_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_cases_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_clone**
> v3_dashboards_clone(id, data=data)

Clones the specified dashboard, including all widgets.

Clones the specified dashboard, including all widgets.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject134() # InlineObject134 |  (optional)

try:
    # Clones the specified dashboard, including all widgets.
    api_instance.v3_dashboards_clone(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject134**](InlineObject134.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_create**
> v3_dashboards_create(data=data)

Creates a dashboard.

Creates a dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject131() # InlineObject131 |  (optional)

try:
    # Creates a dashboard.
    api_instance.v3_dashboards_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject131**](InlineObject131.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_delete**
> v3_dashboards_delete(id, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing dashboards

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
is_deleted = 'is_deleted_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
title = 'title_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_delete(id, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **is_deleted** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_favorite_create**
> v3_dashboards_favorite_create(parent_lookup_dashboard, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject137() # InlineObject137 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_favorite_create(parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_favorite_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject137**](InlineObject137.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_favorite_delete**
> v3_dashboards_favorite_delete(parent_lookup_dashboard)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_favorite_delete(parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_favorite_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_favorite_delete_0**
> v3_dashboards_favorite_delete_0(id, parent_lookup_dashboard)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_favorite_delete_0(id, parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_favorite_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_favorite_list**
> v3_dashboards_favorite_list(parent_lookup_dashboard, limit=limit, offset=offset)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_favorite_list(parent_lookup_dashboard, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_favorite_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_favorite_partial_update**
> v3_dashboards_favorite_partial_update(id, parent_lookup_dashboard, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject138() # InlineObject138 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_favorite_partial_update(id, parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_favorite_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject138**](InlineObject138.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_favorite_partial_update0**
> v3_dashboards_favorite_partial_update0(id, parent_lookup_dashboard, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject139() # InlineObject139 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_favorite_partial_update0(id, parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_favorite_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject139**](InlineObject139.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_favorite_read**
> v3_dashboards_favorite_read(id, parent_lookup_dashboard)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_favorite_read(id, parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_favorite_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_favorite_update**
> v3_dashboards_favorite_update(parent_lookup_dashboard, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject136() # InlineObject136 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_favorite_update(parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_favorite_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject136**](InlineObject136.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_get_all_tags**
> v3_dashboards_get_all_tags()

Lists all tags associated with dashboards.

Lists all tags associated with dashboards.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Lists all tags associated with dashboards.
    api_instance.v3_dashboards_get_all_tags()
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_get_all_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_list**
> v3_dashboards_list(limit=limit, offset=offset, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing dashboards

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
is_deleted = 'is_deleted_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
title = 'title_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_list(limit=limit, offset=offset, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **is_deleted** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_partial_update**
> v3_dashboards_partial_update(id, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing dashboards

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
is_deleted = 'is_deleted_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
title = 'title_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject132() # InlineObject132 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_partial_update(id, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **is_deleted** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject132**](InlineObject132.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_partial_update0**
> v3_dashboards_partial_update0(id, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing dashboards

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
is_deleted = 'is_deleted_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
title = 'title_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject133() # InlineObject133 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_partial_update0(id, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **is_deleted** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject133**](InlineObject133.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_read**
> v3_dashboards_read(id, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by)

Retrieves the specified dashboard.

Retrieves the specified dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
is_deleted = 'is_deleted_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
title = 'title_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Retrieves the specified dashboard.
    api_instance.v3_dashboards_read(id, is_deleted=is_deleted, is_internal=is_internal, is_public=is_public, tags=tags, title=title, created_at=created_at, created_by=created_by, updated_at=updated_at, description=description, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **is_deleted** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_create**
> v3_dashboards_reports_create(parent_lookup_dashboard, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject140() # InlineObject140 |  (optional)

try:
    api_instance.v3_dashboards_reports_create(parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject140**](InlineObject140.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_delete**
> v3_dashboards_reports_delete(parent_lookup_dashboard)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    api_instance.v3_dashboards_reports_delete(parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_delete_0**
> v3_dashboards_reports_delete_0(id, parent_lookup_dashboard, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_dashboards_reports_delete_0(id, parent_lookup_dashboard, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_export_pdf**
> v3_dashboards_reports_export_pdf(id, parent_lookup_dashboard)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    api_instance.v3_dashboards_reports_export_pdf(id, parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_export_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_list**
> v3_dashboards_reports_list(parent_lookup_dashboard, limit=limit, offset=offset, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_dashboards_reports_list(parent_lookup_dashboard, limit=limit, offset=offset, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_partial_update**
> v3_dashboards_reports_partial_update(id, parent_lookup_dashboard, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject141() # InlineObject141 |  (optional)

try:
    api_instance.v3_dashboards_reports_partial_update(id, parent_lookup_dashboard, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject141**](InlineObject141.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_partial_update0**
> v3_dashboards_reports_partial_update0(id, parent_lookup_dashboard, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject142() # InlineObject142 |  (optional)

try:
    api_instance.v3_dashboards_reports_partial_update0(id, parent_lookup_dashboard, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject142**](InlineObject142.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_read**
> v3_dashboards_reports_read(id, parent_lookup_dashboard, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)

Override to include widget result serializer

Override to include widget result serializer

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Override to include widget result serializer
    api_instance.v3_dashboards_reports_read(id, parent_lookup_dashboard, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_reports_search**
> v3_dashboards_reports_search(parent_lookup_dashboard)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    api_instance.v3_dashboards_reports_search(parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_reports_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedule_create**
> v3_dashboards_schedule_create(parent_lookup_dashboard, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject144() # InlineObject144 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedule_create(parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedule_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject144**](InlineObject144.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedule_delete**
> v3_dashboards_schedule_delete(parent_lookup_dashboard)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedule_delete(parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedule_delete_0**
> v3_dashboards_schedule_delete_0(id, parent_lookup_dashboard, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
email_recipients = 'email_recipients_example' # str |  (optional)
email_password = 'email_password_example' # str |  (optional)
email_pdf = 'email_pdf_example' # str |  (optional)
is_enabled = 'is_enabled_example' # str |  (optional)
latest_run = 'latest_run_example' # str |  (optional)
repeat = 'repeat_example' # str |  (optional)
repeat_on = 'repeat_on_example' # str | Multiple values may be separated by commas. (optional)
run_at = 'run_at_example' # str |  (optional)
dashboard_title = 'dashboard_title_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedule_delete_0(id, parent_lookup_dashboard, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedule_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **email_recipients** | **str**|  | [optional] 
 **email_password** | **str**|  | [optional] 
 **email_pdf** | **str**|  | [optional] 
 **is_enabled** | **str**|  | [optional] 
 **latest_run** | **str**|  | [optional] 
 **repeat** | **str**|  | [optional] 
 **repeat_on** | **str**| Multiple values may be separated by commas. | [optional] 
 **run_at** | **str**|  | [optional] 
 **dashboard_title** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedule_list**
> v3_dashboards_schedule_list(parent_lookup_dashboard, limit=limit, offset=offset, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
email_recipients = 'email_recipients_example' # str |  (optional)
email_password = 'email_password_example' # str |  (optional)
email_pdf = 'email_pdf_example' # str |  (optional)
is_enabled = 'is_enabled_example' # str |  (optional)
latest_run = 'latest_run_example' # str |  (optional)
repeat = 'repeat_example' # str |  (optional)
repeat_on = 'repeat_on_example' # str | Multiple values may be separated by commas. (optional)
run_at = 'run_at_example' # str |  (optional)
dashboard_title = 'dashboard_title_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedule_list(parent_lookup_dashboard, limit=limit, offset=offset, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **email_recipients** | **str**|  | [optional] 
 **email_password** | **str**|  | [optional] 
 **email_pdf** | **str**|  | [optional] 
 **is_enabled** | **str**|  | [optional] 
 **latest_run** | **str**|  | [optional] 
 **repeat** | **str**|  | [optional] 
 **repeat_on** | **str**| Multiple values may be separated by commas. | [optional] 
 **run_at** | **str**|  | [optional] 
 **dashboard_title** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedule_partial_update**
> v3_dashboards_schedule_partial_update(id, parent_lookup_dashboard, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
email_recipients = 'email_recipients_example' # str |  (optional)
email_password = 'email_password_example' # str |  (optional)
email_pdf = 'email_pdf_example' # str |  (optional)
is_enabled = 'is_enabled_example' # str |  (optional)
latest_run = 'latest_run_example' # str |  (optional)
repeat = 'repeat_example' # str |  (optional)
repeat_on = 'repeat_on_example' # str | Multiple values may be separated by commas. (optional)
run_at = 'run_at_example' # str |  (optional)
dashboard_title = 'dashboard_title_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject145() # InlineObject145 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedule_partial_update(id, parent_lookup_dashboard, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedule_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **email_recipients** | **str**|  | [optional] 
 **email_password** | **str**|  | [optional] 
 **email_pdf** | **str**|  | [optional] 
 **is_enabled** | **str**|  | [optional] 
 **latest_run** | **str**|  | [optional] 
 **repeat** | **str**|  | [optional] 
 **repeat_on** | **str**| Multiple values may be separated by commas. | [optional] 
 **run_at** | **str**|  | [optional] 
 **dashboard_title** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject145**](InlineObject145.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedule_partial_update0**
> v3_dashboards_schedule_partial_update0(id, parent_lookup_dashboard, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
email_recipients = 'email_recipients_example' # str |  (optional)
email_password = 'email_password_example' # str |  (optional)
email_pdf = 'email_pdf_example' # str |  (optional)
is_enabled = 'is_enabled_example' # str |  (optional)
latest_run = 'latest_run_example' # str |  (optional)
repeat = 'repeat_example' # str |  (optional)
repeat_on = 'repeat_on_example' # str | Multiple values may be separated by commas. (optional)
run_at = 'run_at_example' # str |  (optional)
dashboard_title = 'dashboard_title_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject146() # InlineObject146 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedule_partial_update0(id, parent_lookup_dashboard, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedule_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **email_recipients** | **str**|  | [optional] 
 **email_password** | **str**|  | [optional] 
 **email_pdf** | **str**|  | [optional] 
 **is_enabled** | **str**|  | [optional] 
 **latest_run** | **str**|  | [optional] 
 **repeat** | **str**|  | [optional] 
 **repeat_on** | **str**| Multiple values may be separated by commas. | [optional] 
 **run_at** | **str**|  | [optional] 
 **dashboard_title** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject146**](InlineObject146.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedule_read**
> v3_dashboards_schedule_read(id, parent_lookup_dashboard, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
email_recipients = 'email_recipients_example' # str |  (optional)
email_password = 'email_password_example' # str |  (optional)
email_pdf = 'email_pdf_example' # str |  (optional)
is_enabled = 'is_enabled_example' # str |  (optional)
latest_run = 'latest_run_example' # str |  (optional)
repeat = 'repeat_example' # str |  (optional)
repeat_on = 'repeat_on_example' # str | Multiple values may be separated by commas. (optional)
run_at = 'run_at_example' # str |  (optional)
dashboard_title = 'dashboard_title_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedule_read(id, parent_lookup_dashboard, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedule_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **email_recipients** | **str**|  | [optional] 
 **email_password** | **str**|  | [optional] 
 **email_pdf** | **str**|  | [optional] 
 **is_enabled** | **str**|  | [optional] 
 **latest_run** | **str**|  | [optional] 
 **repeat** | **str**|  | [optional] 
 **repeat_on** | **str**| Multiple values may be separated by commas. | [optional] 
 **run_at** | **str**|  | [optional] 
 **dashboard_title** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedule_update**
> v3_dashboards_schedule_update(parent_lookup_dashboard, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject143() # InlineObject143 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedule_update(parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedule_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject143**](InlineObject143.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_schedules_list**
> v3_dashboards_schedules_list(limit=limit, offset=offset, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Lists

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
email_recipients = 'email_recipients_example' # str |  (optional)
email_password = 'email_password_example' # str |  (optional)
email_pdf = 'email_pdf_example' # str |  (optional)
is_enabled = 'is_enabled_example' # str |  (optional)
latest_run = 'latest_run_example' # str |  (optional)
repeat = 'repeat_example' # str |  (optional)
repeat_on = 'repeat_on_example' # str | Multiple values may be separated by commas. (optional)
run_at = 'run_at_example' # str |  (optional)
dashboard_title = 'dashboard_title_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_schedules_list(limit=limit, offset=offset, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, dashboard=dashboard, email_recipients=email_recipients, email_password=email_password, email_pdf=email_pdf, is_enabled=is_enabled, latest_run=latest_run, repeat=repeat, repeat_on=repeat_on, run_at=run_at, dashboard_title=dashboard_title, is_internal=is_internal, is_public=is_public, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_schedules_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **email_recipients** | **str**|  | [optional] 
 **email_password** | **str**|  | [optional] 
 **email_pdf** | **str**|  | [optional] 
 **is_enabled** | **str**|  | [optional] 
 **latest_run** | **str**|  | [optional] 
 **repeat** | **str**|  | [optional] 
 **repeat_on** | **str**| Multiple values may be separated by commas. | [optional] 
 **run_at** | **str**|  | [optional] 
 **dashboard_title** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_search**
> v3_dashboards_search()

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing dashboards

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_subscribe**
> v3_dashboards_subscribe(id, data=data)

Subscribes/Unsubscribes the current user from receiving

Subscribes/Unsubscribes the current user from receiving email notifications on a dashboard report

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject135() # InlineObject135 |  (optional)

try:
    # Subscribes/Unsubscribes the current user from receiving
    api_instance.v3_dashboards_subscribe(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_subscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject135**](InlineObject135.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_create**
> v3_dashboards_widgets_create(parent_lookup_dashboard, data=data)

Creates a widget for the specified dashboard.

Creates a widget for the specified dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject148() # InlineObject148 |  (optional)

try:
    # Creates a widget for the specified dashboard.
    api_instance.v3_dashboards_widgets_create(parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject148**](InlineObject148.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_delete**
> v3_dashboards_widgets_delete(parent_lookup_dashboard)

Deletes all widgets from the specified dashboard.

Deletes all widgets from the specified dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    # Deletes all widgets from the specified dashboard.
    api_instance.v3_dashboards_widgets_delete(parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_delete_0**
> v3_dashboards_widgets_delete_0(id, parent_lookup_dashboard, order_by=order_by)

Deletes a widget from the specified dashboard.

Deletes a widget from the specified dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Deletes a widget from the specified dashboard.
    api_instance.v3_dashboards_widgets_delete_0(id, parent_lookup_dashboard, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_list**
> v3_dashboards_widgets_list(parent_lookup_dashboard, limit=limit, offset=offset, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Widgets

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_widgets_list(parent_lookup_dashboard, limit=limit, offset=offset, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_partial_update**
> v3_dashboards_widgets_partial_update(id, parent_lookup_dashboard, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Widgets

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject149() # InlineObject149 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_widgets_partial_update(id, parent_lookup_dashboard, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject149**](InlineObject149.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_partial_update0**
> v3_dashboards_widgets_partial_update0(id, parent_lookup_dashboard, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Widgets

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject150() # InlineObject150 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_widgets_partial_update0(id, parent_lookup_dashboard, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject150**](InlineObject150.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_perform_search**
> v3_dashboards_widgets_perform_search(id, parent_lookup_dashboard)

Returns the results of a dashboard widget.

Returns the results of a dashboard widget.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    # Returns the results of a dashboard widget.
    api_instance.v3_dashboards_widgets_perform_search(id, parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_perform_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_read**
> v3_dashboards_widgets_read(id, parent_lookup_dashboard, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Widgets

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_widgets_read(id, parent_lookup_dashboard, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_dashboard** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_search**
> v3_dashboards_widgets_search(parent_lookup_dashboard)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Widgets

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_dashboards_widgets_search(parent_lookup_dashboard)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_dashboards_widgets_update**
> v3_dashboards_widgets_update(parent_lookup_dashboard, data=data)

Updates all widgets for the specified dashboard.

Updates all widgets for the specified dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_dashboard = 'parent_lookup_dashboard_example' # str | 
data = fireeye.helix.InlineObject147() # InlineObject147 |  (optional)

try:
    # Updates all widgets for the specified dashboard.
    api_instance.v3_dashboards_widgets_update(parent_lookup_dashboard, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_dashboards_widgets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_dashboard** | **str**|  | 
 **data** | [**InlineObject147**](InlineObject147.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_domains_resolve_list**
> v3_domains_resolve_list()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_domains_resolve_list()
except ApiException as e:
    print("Exception when calling V3Api->v3_domains_resolve_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_fields_analytics_list**
> v3_fields_analytics_list()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_fields_analytics_list()
except ApiException as e:
    print("Exception when calling V3Api->v3_fields_analytics_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_indicators_stream_list**
> v3_indicators_stream_list(limit=limit, offset=offset, query=query, sort=sort, fields=fields, includes=includes)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
query = 'query_example' # str | Mongo JSON query syntax used to filter for specific results. See https://docs.mongodb.com/manual/reference/operator/query-comparison/ for more information on Mongo JSON query operators. Here is an example of the syntax for this filter:  ?query={\"state\":{\"$in\":[\"Open\",\"Reopened\"]},\"suppressed\":false} (optional)
sort = 'sort_example' # str | Comma-separated list of field names to sort the results by. For example: \"createDate\" or \"-updateDate,riskOrder\" (optional)
fields = 'fields_example' # str | Comma-separated list of field names to only select or exclude from the resulting data. (optional)
includes = 'includes_example' # str | Comma-separated list of field names to expand an ID into a full object representation of the related data. (optional)

try:
    api_instance.v3_indicators_stream_list(limit=limit, offset=offset, query=query, sort=sort, fields=fields, includes=includes)
except ApiException as e:
    print("Exception when calling V3Api->v3_indicators_stream_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **query** | **str**| Mongo JSON query syntax used to filter for specific results. See https://docs.mongodb.com/manual/reference/operator/query-comparison/ for more information on Mongo JSON query operators. Here is an example of the syntax for this filter:  ?query&#x3D;{\&quot;state\&quot;:{\&quot;$in\&quot;:[\&quot;Open\&quot;,\&quot;Reopened\&quot;]},\&quot;suppressed\&quot;:false} | [optional] 
 **sort** | **str**| Comma-separated list of field names to sort the results by. For example: \&quot;createDate\&quot; or \&quot;-updateDate,riskOrder\&quot; | [optional] 
 **fields** | **str**| Comma-separated list of field names to only select or exclude from the resulting data. | [optional] 
 **includes** | **str**| Comma-separated list of field names to expand an ID into a full object representation of the related data. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_indicators_stream_read**
> v3_indicators_stream_read(id, query=query, sort=sort, fields=fields, includes=includes)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
query = 'query_example' # str | Mongo JSON query syntax used to filter for specific results. See https://docs.mongodb.com/manual/reference/operator/query-comparison/ for more information on Mongo JSON query operators. Here is an example of the syntax for this filter:  ?query={\"state\":{\"$in\":[\"Open\",\"Reopened\"]},\"suppressed\":false} (optional)
sort = 'sort_example' # str | Comma-separated list of field names to sort the results by. For example: \"createDate\" or \"-updateDate,riskOrder\" (optional)
fields = 'fields_example' # str | Comma-separated list of field names to only select or exclude from the resulting data. (optional)
includes = 'includes_example' # str | Comma-separated list of field names to expand an ID into a full object representation of the related data. (optional)

try:
    api_instance.v3_indicators_stream_read(id, query=query, sort=sort, fields=fields, includes=includes)
except ApiException as e:
    print("Exception when calling V3Api->v3_indicators_stream_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **query** | **str**| Mongo JSON query syntax used to filter for specific results. See https://docs.mongodb.com/manual/reference/operator/query-comparison/ for more information on Mongo JSON query operators. Here is an example of the syntax for this filter:  ?query&#x3D;{\&quot;state\&quot;:{\&quot;$in\&quot;:[\&quot;Open\&quot;,\&quot;Reopened\&quot;]},\&quot;suppressed\&quot;:false} | [optional] 
 **sort** | **str**| Comma-separated list of field names to sort the results by. For example: \&quot;createDate\&quot; or \&quot;-updateDate,riskOrder\&quot; | [optional] 
 **fields** | **str**| Comma-separated list of field names to only select or exclude from the resulting data. | [optional] 
 **includes** | **str**| Comma-separated list of field names to expand an ID into a full object representation of the related data. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_intel_context_characteristics_list**
> v3_intel_context_characteristics_list()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_intel_context_characteristics_list()
except ApiException as e:
    print("Exception when calling V3Api->v3_intel_context_characteristics_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_create**
> v3_lists_create(data=data)

Returns a list of Lists.  You can search for specific lists by name,

Returns a list of Lists.  You can search for specific lists by name, short_name, type, or description.  Results can be ordered by name, short_name, type, is_internal, is_protected, is_active, created_at, updated_at, description, or item_count. The response does not inlcude list items. To get a list of list items, use GET /v3/lists/export.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject151() # InlineObject151 |  (optional)

try:
    # Returns a list of Lists.  You can search for specific lists by name,
    api_instance.v3_lists_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject151**](InlineObject151.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_delete**
> v3_lists_delete(id, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by)

Returns a list of Lists.  You can search for specific lists by name,

Returns a list of Lists.  You can search for specific lists by name, short_name, type, or description.  Results can be ordered by name, short_name, type, is_internal, is_protected, is_active, created_at, updated_at, description, or item_count. The response does not inlcude list items. To get a list of list items, use GET /v3/lists/export.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
created_at = 'created_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
is_active = 'is_active_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
name = 'name_example' # str |  (optional)
short_name = 'short_name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Returns a list of Lists.  You can search for specific lists by name,
    api_instance.v3_lists_delete(id, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **created_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **short_name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_export_all**
> v3_lists_export_all()

Creates an export file in JSON format.

Creates an export file in JSON format.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Creates an export file in JSON format.
    api_instance.v3_lists_export_all()
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_export_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_export_single**
> v3_lists_export_single(id)

Exports the specified case to a JSON file.

Exports the specified case to a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Exports the specified case to a JSON file.
    api_instance.v3_lists_export_single(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_export_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_create**
> v3_lists_items_create(parent_lookup_list, data=data)

Overrides the default 'create' method in order to associate the

Overrides the default 'create' method in order to associate the list_id that may be in the URL parameters due to nested routes

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_list = 'parent_lookup_list_example' # str | 
data = fireeye.helix.InlineObject154() # InlineObject154 |  (optional)

try:
    # Overrides the default 'create' method in order to associate the
    api_instance.v3_lists_items_create(parent_lookup_list, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_list** | **str**|  | 
 **data** | [**InlineObject154**](InlineObject154.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_delete**
> v3_lists_items_delete(parent_lookup_list)

Deletes list items from the specified list. You cannot delete items from internal or protected lists.

Deletes list items from the specified list. You cannot delete items from internal or protected lists.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_list = 'parent_lookup_list_example' # str | 

try:
    # Deletes list items from the specified list. You cannot delete items from internal or protected lists.
    api_instance.v3_lists_items_delete(parent_lookup_list)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_list** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_delete_0**
> v3_lists_items_delete_0(id, parent_lookup_list, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by)

Exports list items as a JSON file.

Exports list items as a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_list = 'parent_lookup_list_example' # str | 
list_type = 'list_type_example' # str |  (optional)
list = 'list_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
type = 'type_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
value = 'value_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Exports list items as a JSON file.
    api_instance.v3_lists_items_delete_0(id, parent_lookup_list, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_list** | **str**|  | 
 **list_type** | **str**|  | [optional] 
 **list** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **value** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_export**
> v3_lists_items_export(parent_lookup_list)

Exports the specified list as a JSON file.

Exports the specified list as a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_list = 'parent_lookup_list_example' # str | 

try:
    # Exports the specified list as a JSON file.
    api_instance.v3_lists_items_export(parent_lookup_list)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_list** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_export_single**
> v3_lists_items_export_single(id, parent_lookup_list)

Exports the specified case to a JSON file.

Exports the specified case to a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_list = 'parent_lookup_list_example' # str | 

try:
    # Exports the specified case to a JSON file.
    api_instance.v3_lists_items_export_single(id, parent_lookup_list)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_export_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_list** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_list**
> v3_lists_items_list(parent_lookup_list, limit=limit, offset=offset, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by)

Exports list items as a JSON file.

Exports list items as a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_list = 'parent_lookup_list_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
list_type = 'list_type_example' # str |  (optional)
list = 'list_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
type = 'type_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
value = 'value_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Exports list items as a JSON file.
    api_instance.v3_lists_items_list(parent_lookup_list, limit=limit, offset=offset, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_list** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **list_type** | **str**|  | [optional] 
 **list** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **value** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_partial_update**
> v3_lists_items_partial_update(id, parent_lookup_list, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by, data=data)

Exports list items as a JSON file.

Exports list items as a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_list = 'parent_lookup_list_example' # str | 
list_type = 'list_type_example' # str |  (optional)
list = 'list_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
type = 'type_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
value = 'value_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject156() # InlineObject156 |  (optional)

try:
    # Exports list items as a JSON file.
    api_instance.v3_lists_items_partial_update(id, parent_lookup_list, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_list** | **str**|  | 
 **list_type** | **str**|  | [optional] 
 **list** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **value** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject156**](InlineObject156.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_partial_update0**
> v3_lists_items_partial_update0(id, parent_lookup_list, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by, data=data)

Exports list items as a JSON file.

Exports list items as a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_list = 'parent_lookup_list_example' # str | 
list_type = 'list_type_example' # str |  (optional)
list = 'list_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
type = 'type_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
value = 'value_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject157() # InlineObject157 |  (optional)

try:
    # Exports list items as a JSON file.
    api_instance.v3_lists_items_partial_update0(id, parent_lookup_list, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_list** | **str**|  | 
 **list_type** | **str**|  | [optional] 
 **list** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **value** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject157**](InlineObject157.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_read**
> v3_lists_items_read(id, parent_lookup_list, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by)

Exports list items as a JSON file.

Exports list items as a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_list = 'parent_lookup_list_example' # str | 
list_type = 'list_type_example' # str |  (optional)
list = 'list_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
risk = 'risk_example' # str |  (optional)
type = 'type_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
value = 'value_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Exports list items as a JSON file.
    api_instance.v3_lists_items_read(id, parent_lookup_list, list_type=list_type, list=list, notes=notes, risk=risk, type=type, usage=usage, value=value, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_list** | **str**|  | 
 **list_type** | **str**|  | [optional] 
 **list** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **risk** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **value** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_search**
> v3_lists_items_search(parent_lookup_list)

Exports list items as a JSON file.

Exports list items as a JSON file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_list = 'parent_lookup_list_example' # str | 

try:
    # Exports list items as a JSON file.
    api_instance.v3_lists_items_search(parent_lookup_list)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_list** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_types_list**
> v3_lists_items_types_list()

Returns all list item types and their labels.

Returns all list item types and their labels.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Returns all list item types and their labels.
    api_instance.v3_lists_items_types_list()
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_types_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_items_upload**
> v3_lists_items_upload(parent_lookup_list, data=data)

Imports list items into the specified list.

Imports list items into the specified list.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_list = 'parent_lookup_list_example' # str | 
data = fireeye.helix.InlineObject155() # InlineObject155 |  (optional)

try:
    # Imports list items into the specified list.
    api_instance.v3_lists_items_upload(parent_lookup_list, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_items_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_list** | **str**|  | 
 **data** | [**InlineObject155**](InlineObject155.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_list**
> v3_lists_list(limit=limit, offset=offset, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by)

Returns a list of Lists.  You can search for specific lists by name,

Returns a list of Lists.  You can search for specific lists by name, short_name, type, or description.  Results can be ordered by name, short_name, type, is_internal, is_protected, is_active, created_at, updated_at, description, or item_count. The response does not inlcude list items. To get a list of list items, use GET /v3/lists/export.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
created_at = 'created_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
is_active = 'is_active_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
name = 'name_example' # str |  (optional)
short_name = 'short_name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Returns a list of Lists.  You can search for specific lists by name,
    api_instance.v3_lists_list(limit=limit, offset=offset, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **created_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **short_name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_partial_update**
> v3_lists_partial_update(id, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by, data=data)

Returns a list of Lists.  You can search for specific lists by name,

Returns a list of Lists.  You can search for specific lists by name, short_name, type, or description.  Results can be ordered by name, short_name, type, is_internal, is_protected, is_active, created_at, updated_at, description, or item_count. The response does not inlcude list items. To get a list of list items, use GET /v3/lists/export.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
created_at = 'created_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
is_active = 'is_active_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
name = 'name_example' # str |  (optional)
short_name = 'short_name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject152() # InlineObject152 |  (optional)

try:
    # Returns a list of Lists.  You can search for specific lists by name,
    api_instance.v3_lists_partial_update(id, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **created_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **short_name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject152**](InlineObject152.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_partial_update0**
> v3_lists_partial_update0(id, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by, data=data)

Returns a list of Lists.  You can search for specific lists by name,

Returns a list of Lists.  You can search for specific lists by name, short_name, type, or description.  Results can be ordered by name, short_name, type, is_internal, is_protected, is_active, created_at, updated_at, description, or item_count. The response does not inlcude list items. To get a list of list items, use GET /v3/lists/export.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
created_at = 'created_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
is_active = 'is_active_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
name = 'name_example' # str |  (optional)
short_name = 'short_name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject153() # InlineObject153 |  (optional)

try:
    # Returns a list of Lists.  You can search for specific lists by name,
    api_instance.v3_lists_partial_update0(id, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **created_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **short_name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject153**](InlineObject153.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_read**
> v3_lists_read(id, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by)

Returns a list of Lists.  You can search for specific lists by name,

Returns a list of Lists.  You can search for specific lists by name, short_name, type, or description.  Results can be ordered by name, short_name, type, is_internal, is_protected, is_active, created_at, updated_at, description, or item_count. The response does not inlcude list items. To get a list of list items, use GET /v3/lists/export.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
created_at = 'created_at_example' # str |  (optional)
description = 'description_example' # str |  (optional)
is_active = 'is_active_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
name = 'name_example' # str |  (optional)
short_name = 'short_name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
usage = 'usage_example' # str | Multiple values may be separated by commas. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Returns a list of Lists.  You can search for specific lists by name,
    api_instance.v3_lists_read(id, created_at=created_at, description=description, is_active=is_active, is_internal=is_internal, is_protected=is_protected, name=name, short_name=short_name, type=type, updated_at=updated_at, usage=usage, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **created_at** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **short_name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **usage** | **str**| Multiple values may be separated by commas. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lists_search**
> v3_lists_search()

Returns a list of Lists.  You can search for specific lists by name,

Returns a list of Lists.  You can search for specific lists by name, short_name, type, or description.  Results can be ordered by name, short_name, type, is_internal, is_protected, is_active, created_at, updated_at, description, or item_count. The response does not inlcude list items. To get a list of list items, use GET /v3/lists/export.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Returns a list of Lists.  You can search for specific lists by name,
    api_instance.v3_lists_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_lists_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_patterndb_create**
> v3_patterndb_create()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_patterndb_create()
except ApiException as e:
    print("Exception when calling V3Api->v3_patterndb_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_patterndb_delete**
> v3_patterndb_delete(id)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    api_instance.v3_patterndb_delete(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_patterndb_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_patterndb_export**
> v3_patterndb_export(id)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    api_instance.v3_patterndb_export(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_patterndb_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_patterndb_list**
> v3_patterndb_list()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_patterndb_list()
except ApiException as e:
    print("Exception when calling V3Api->v3_patterndb_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_playbooks_create**
> v3_playbooks_create(data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Playbooks

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject158() # InlineObject158 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_playbooks_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_playbooks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject158**](InlineObject158.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_playbooks_delete**
> v3_playbooks_delete(id)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Playbooks

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_playbooks_delete(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_playbooks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_playbooks_list**
> v3_playbooks_list(limit=limit, offset=offset)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Playbooks

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_playbooks_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_playbooks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_playbooks_partial_update**
> v3_playbooks_partial_update(id, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Playbooks

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject159() # InlineObject159 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_playbooks_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_playbooks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject159**](InlineObject159.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_playbooks_partial_update0**
> v3_playbooks_partial_update0(id, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Playbooks

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject160() # InlineObject160 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_playbooks_partial_update0(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_playbooks_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject160**](InlineObject160.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_playbooks_plays_create**
> v3_playbooks_plays_create(id, data=data)

Override the default create method to add playbook_id

Override the default create method to add playbook_id

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject161() # InlineObject161 |  (optional)

try:
    # Override the default create method to add playbook_id
    api_instance.v3_playbooks_plays_create(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_playbooks_plays_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject161**](InlineObject161.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_playbooks_plays_list**
> v3_playbooks_plays_list(id, limit=limit, offset=offset)

Override the default list method to add playbook_id

Override the default list method to add playbook_id

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # Override the default list method to add playbook_id
    api_instance.v3_playbooks_plays_list(id, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_playbooks_plays_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_playbooks_read**
> v3_playbooks_read(id)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Playbooks

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_playbooks_read(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_playbooks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_plays_create**
> v3_plays_create(data=data)

Override the default create method to add playbook_id

Override the default create method to add playbook_id

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject162() # InlineObject162 |  (optional)

try:
    # Override the default create method to add playbook_id
    api_instance.v3_plays_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_plays_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject162**](InlineObject162.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_plays_delete**
> v3_plays_delete(id)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Plays

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_plays_delete(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_plays_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_plays_list**
> v3_plays_list(limit=limit, offset=offset)

Override the default list method to add playbook_id

Override the default list method to add playbook_id

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # Override the default list method to add playbook_id
    api_instance.v3_plays_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_plays_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_plays_partial_update**
> v3_plays_partial_update(id, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Plays

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject163() # InlineObject163 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_plays_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_plays_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject163**](InlineObject163.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_plays_partial_update0**
> v3_plays_partial_update0(id, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Plays

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject164() # InlineObject164 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_plays_partial_update0(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_plays_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject164**](InlineObject164.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_plays_read**
> v3_plays_read(id)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Plays

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_plays_read(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_plays_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_preferences_cms_url**
> v3_preferences_cms_url()

Specifies the Network (CMS) URL used by Helix.

Specifies the Network (CMS) URL used by Helix.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Specifies the Network (CMS) URL used by Helix.
    api_instance.v3_preferences_cms_url()
except ApiException as e:
    print("Exception when calling V3Api->v3_preferences_cms_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_preferences_etp_url**
> v3_preferences_etp_url()

Specifies the Email (ETP) URL used by Helix.

Specifies the Email (ETP) URL used by Helix.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Specifies the Email (ETP) URL used by Helix.
    api_instance.v3_preferences_etp_url()
except ApiException as e:
    print("Exception when calling V3Api->v3_preferences_etp_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_preferences_hx_url**
> v3_preferences_hx_url()

Specifies the Endpoint (HX) URLs used by Helix.

Specifies the Endpoint (HX) URLs used by Helix.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Specifies the Endpoint (HX) URLs used by Helix.
    api_instance.v3_preferences_hx_url()
except ApiException as e:
    print("Exception when calling V3Api->v3_preferences_hx_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_create**
> v3_reports_create(data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject165() # InlineObject165 |  (optional)

try:
    api_instance.v3_reports_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject165**](InlineObject165.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_delete**
> v3_reports_delete()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_reports_delete()
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_delete_0**
> v3_reports_delete_0(id, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_reports_delete_0(id, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_export_pdf**
> v3_reports_export_pdf(id)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    api_instance.v3_reports_export_pdf(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_export_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_list**
> v3_reports_list(limit=limit, offset=offset, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_reports_list(limit=limit, offset=offset, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_partial_update**
> v3_reports_partial_update(id, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject166() # InlineObject166 |  (optional)

try:
    api_instance.v3_reports_partial_update(id, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject166**](InlineObject166.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_partial_update0**
> v3_reports_partial_update0(id, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject167() # InlineObject167 |  (optional)

try:
    api_instance.v3_reports_partial_update0(id, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject167**](InlineObject167.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_read**
> v3_reports_read(id, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)

Override to include widget result serializer

Override to include widget result serializer

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
updated_by = 'updated_by_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
query_end = 'query_end_example' # str |  (optional)
query_end__lt = 'query_end__lt_example' # str |  (optional)
query_end__lte = 'query_end__lte_example' # str |  (optional)
query_end__gt = 'query_end__gt_example' # str |  (optional)
query_end__gte = 'query_end__gte_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lt = 'updated_at__lt_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gt = 'updated_at__gt_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
duration = 3.4 # float |  (optional)
duration__lt = 3.4 # float |  (optional)
duration__lte = 3.4 # float |  (optional)
duration__gt = 3.4 # float |  (optional)
duration__gte = 3.4 # float |  (optional)
started_at = 'started_at_example' # str |  (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lt = 'created_at__lt_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gt = 'created_at__gt_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
state__iexact = 'state__iexact_example' # str |  (optional)
dashboard = 'dashboard_example' # str |  (optional)
query_start = 'query_start_example' # str |  (optional)
query_start__lt = 'query_start__lt_example' # str |  (optional)
query_start__lte = 'query_start__lte_example' # str |  (optional)
query_start__gt = 'query_start__gt_example' # str |  (optional)
query_start__gte = 'query_start__gte_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Override to include widget result serializer
    api_instance.v3_reports_read(id, updated_by=updated_by, finished_at=finished_at, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, query_end=query_end, query_end__lt=query_end__lt, query_end__lte=query_end__lte, query_end__gt=query_end__gt, query_end__gte=query_end__gte, updated_at=updated_at, updated_at__lt=updated_at__lt, updated_at__lte=updated_at__lte, updated_at__gt=updated_at__gt, updated_at__gte=updated_at__gte, duration=duration, duration__lt=duration__lt, duration__lte=duration__lte, duration__gt=duration__gt, duration__gte=duration__gte, started_at=started_at, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, created_at=created_at, created_at__lt=created_at__lt, created_at__lte=created_at__lte, created_at__gt=created_at__gt, created_at__gte=created_at__gte, created_by=created_by, state__iexact=state__iexact, dashboard=dashboard, query_start=query_start, query_start__lt=query_start__lt, query_start__lte=query_start__lte, query_start__gt=query_start__gt, query_start__gte=query_start__gte, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **updated_by** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **query_end** | **str**|  | [optional] 
 **query_end__lt** | **str**|  | [optional] 
 **query_end__lte** | **str**|  | [optional] 
 **query_end__gt** | **str**|  | [optional] 
 **query_end__gte** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lt** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gt** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **duration** | **float**|  | [optional] 
 **duration__lt** | **float**|  | [optional] 
 **duration__lte** | **float**|  | [optional] 
 **duration__gt** | **float**|  | [optional] 
 **duration__gte** | **float**|  | [optional] 
 **started_at** | **str**|  | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lt** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gt** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **state__iexact** | **str**|  | [optional] 
 **dashboard** | **str**|  | [optional] 
 **query_start** | **str**|  | [optional] 
 **query_start__lt** | **str**|  | [optional] 
 **query_start__lte** | **str**|  | [optional] 
 **query_start__gt** | **str**|  | [optional] 
 **query_start__gte** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_search**
> v3_reports_search()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_reports_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_widgets_create**
> v3_reports_widgets_create(parent_lookup_report, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_report = 'parent_lookup_report_example' # str | 
data = fireeye.helix.InlineObject168() # InlineObject168 |  (optional)

try:
    api_instance.v3_reports_widgets_create(parent_lookup_report, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_widgets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_report** | **str**|  | 
 **data** | [**InlineObject168**](InlineObject168.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_widgets_delete**
> v3_reports_widgets_delete(parent_lookup_report, widget__id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_report = 'parent_lookup_report_example' # str | 
widget__id = 'widget__id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_reports_widgets_delete(parent_lookup_report, widget__id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_widgets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_report** | **str**|  | 
 **widget__id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_widgets_list**
> v3_reports_widgets_list(parent_lookup_report, limit=limit, offset=offset, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_report = 'parent_lookup_report_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_reports_widgets_list(parent_lookup_report, limit=limit, offset=offset, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_widgets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_report** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_widgets_partial_update**
> v3_reports_widgets_partial_update(parent_lookup_report, widget__id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_report = 'parent_lookup_report_example' # str | 
widget__id = 'widget__id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject169() # InlineObject169 |  (optional)

try:
    api_instance.v3_reports_widgets_partial_update(parent_lookup_report, widget__id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_widgets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_report** | **str**|  | 
 **widget__id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject169**](InlineObject169.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_widgets_partial_update0**
> v3_reports_widgets_partial_update0(parent_lookup_report, widget__id, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_report = 'parent_lookup_report_example' # str | 
widget__id = 'widget__id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject170() # InlineObject170 |  (optional)

try:
    api_instance.v3_reports_widgets_partial_update0(parent_lookup_report, widget__id, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_widgets_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_report** | **str**|  | 
 **widget__id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject170**](InlineObject170.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_widgets_read**
> v3_reports_widgets_read(parent_lookup_report, widget__id, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_report = 'parent_lookup_report_example' # str | 
widget__id = 'widget__id_example' # str | 
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_reports_widgets_read(parent_lookup_report, widget__id, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_widgets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_report** | **str**|  | 
 **widget__id** | **str**|  | 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_reports_widgets_view_results**
> v3_reports_widgets_view_results(parent_lookup_report, widget__id)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_report = 'parent_lookup_report_example' # str | 
widget__id = 'widget__id_example' # str | 

try:
    api_instance.v3_reports_widgets_view_results(parent_lookup_report, widget__id)
except ApiException as e:
    print("Exception when calling V3Api->v3_reports_widgets_view_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_report** | **str**|  | 
 **widget__id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_assertions_list**
> v3_rules_assertions_list(limit=limit, offset=offset)

Lists rule assertions, including:

Lists rule assertions, including: name -- name to use when you reference assertions with dependencies in subsequent rules seconds_valid -- duration that the assertion remains active and can be referenced by dependencies fields -- value to be stored by the assertion, such as srcipv4  An assertion is a variable created by a rule when its MQL query and threshold values match.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # Lists rule assertions, including:
    api_instance.v3_rules_assertions_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_assertions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_assertions_read**
> v3_rules_assertions_read(id)

Lists rule assertions, including:

Lists rule assertions, including: name -- name to use when you reference assertions with dependencies in subsequent rules seconds_valid -- duration that the assertion remains active and can be referenced by dependencies fields -- value to be stored by the assertion, such as srcipv4  An assertion is a variable created by a rule when its MQL query and threshold values match.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Lists rule assertions, including:
    api_instance.v3_rules_assertions_read(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_assertions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_create**
> v3_rules_create()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_rules_create()
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_dependencies_list**
> v3_rules_dependencies_list(limit=limit, offset=offset)

Lists rule dependencies, including:

Lists rule dependencies, including: assertion_name -- name of the assertion that must be active in order for this rule to generate       another assertion, another dependency, alert, or log rule_type -- rule type source_fields -- value that must resolve in order for this rule to generate another assertion,       another dependency, alert, or log, such as domain or hostname       A dependency is a variable that causes a rule hit to not generate an alert (or a log) unless  an equivalent assertion exists and is active. An assertion and a dependency are equivalent  if they have the same name and entry in their respective assertion fields.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # Lists rule dependencies, including:
    api_instance.v3_rules_dependencies_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_dependencies_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_dependencies_read**
> v3_rules_dependencies_read(id)

Lists rule dependencies, including:

Lists rule dependencies, including: assertion_name -- name of the assertion that must be active in order for this rule to generate       another assertion, another dependency, alert, or log rule_type -- rule type source_fields -- value that must resolve in order for this rule to generate another assertion,       another dependency, alert, or log, such as domain or hostname       A dependency is a variable that causes a rule hit to not generate an alert (or a log) unless  an equivalent assertion exists and is active. An assertion and a dependency are equivalent  if they have the same name and entry in their respective assertion fields.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Lists rule dependencies, including:
    api_instance.v3_rules_dependencies_read(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_dependencies_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_get_enabled_rule_percentages_history**
> v3_rules_get_enabled_rule_percentages_history()

Calculates a collection of hourly values from the current hour the method is called and the zeroed-out time from today.

Calculates a collection of hourly values from the current hour the method is called and the zeroed-out time from today. Each object represents each day within the range that is specified by the days parameter in the GET call. Each object includes the number of covered_classes, internal_event_classes (total_classes), enabled_covered_rules, enabled_uncovered_rules, and disabled_rules.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Calculates a collection of hourly values from the current hour the method is called and the zeroed-out time from today.
    api_instance.v3_rules_get_enabled_rule_percentages_history()
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_get_enabled_rule_percentages_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_get_revisions**
> v3_rules_get_revisions(id)

Returns the revision history of the specified rule.

Returns the revision history of the specified rule.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Returns the revision history of the specified rule.
    api_instance.v3_rules_get_revisions(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_get_revisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_get_rules_recommendations**
> v3_rules_get_rules_recommendations()

Provides class/field recommendations based on the number of impacted rules.

Provides class/field recommendations based on the number of impacted rules.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Provides class/field recommendations based on the number of impacted rules.
    api_instance.v3_rules_get_rules_recommendations()
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_get_rules_recommendations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_list**
> v3_rules_list()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_rules_list()
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_rules_read**
> v3_rules_read(id)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    api_instance.v3_rules_read(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_rules_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_create**
> v3_search_saved_create(data=data)

Creates a new search. Defining `is_favorite` is optional.

Creates a new search. Defining `is_favorite` is optional.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject171() # InlineObject171 |  (optional)

try:
    # Creates a new search. Defining `is_favorite` is optional.
    api_instance.v3_search_saved_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject171**](InlineObject171.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_delete**
> v3_search_saved_delete(id, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing saved searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
query_ast = 'query_ast_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
query = 'query_example' # str |  (optional)
category = 'category_example' # str |  (optional)
table = 'table_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
is_hidden = 'is_hidden_example' # str |  (optional)
is_favorite = 'is_favorite_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_delete(id, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **query_ast** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **table** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **is_hidden** | **str**|  | [optional] 
 **is_favorite** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_favorite_create**
> v3_search_saved_favorite_create(parent_lookup_saved_search, data=data)

Overrides the default 'create' method in order to associate the

Overrides the default 'create' method in order to associate the list_id that may be in the URL parameters due to nested routes

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
data = fireeye.helix.InlineObject174() # InlineObject174 |  (optional)

try:
    # Overrides the default 'create' method in order to associate the
    api_instance.v3_search_saved_favorite_create(parent_lookup_saved_search, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_favorite_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_saved_search** | **str**|  | 
 **data** | [**InlineObject174**](InlineObject174.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_favorite_delete**
> v3_search_saved_favorite_delete(parent_lookup_saved_search)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing search favorites.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_favorite_delete(parent_lookup_saved_search)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_favorite_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_saved_search** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_favorite_delete_0**
> v3_search_saved_favorite_delete_0(id, parent_lookup_saved_search)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing search favorites.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_favorite_delete_0(id, parent_lookup_saved_search)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_favorite_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_favorite_list**
> v3_search_saved_favorite_list(parent_lookup_saved_search, limit=limit, offset=offset)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing search favorites.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_favorite_list(parent_lookup_saved_search, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_favorite_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_saved_search** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_favorite_partial_update**
> v3_search_saved_favorite_partial_update(id, parent_lookup_saved_search, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing search favorites.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
data = fireeye.helix.InlineObject175() # InlineObject175 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_favorite_partial_update(id, parent_lookup_saved_search, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_favorite_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 
 **data** | [**InlineObject175**](InlineObject175.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_favorite_partial_update0**
> v3_search_saved_favorite_partial_update0(id, parent_lookup_saved_search, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing search favorites.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
data = fireeye.helix.InlineObject176() # InlineObject176 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_favorite_partial_update0(id, parent_lookup_saved_search, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_favorite_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 
 **data** | [**InlineObject176**](InlineObject176.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_favorite_read**
> v3_search_saved_favorite_read(id, parent_lookup_saved_search)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing search favorites.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_favorite_read(id, parent_lookup_saved_search)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_favorite_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_list**
> v3_search_saved_list(limit=limit, offset=offset, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing saved searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
query_ast = 'query_ast_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
query = 'query_example' # str |  (optional)
category = 'category_example' # str |  (optional)
table = 'table_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
is_hidden = 'is_hidden_example' # str |  (optional)
is_favorite = 'is_favorite_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_list(limit=limit, offset=offset, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **query_ast** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **table** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **is_hidden** | **str**|  | [optional] 
 **is_favorite** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_partial_update**
> v3_search_saved_partial_update(id, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing saved searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
query_ast = 'query_ast_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
query = 'query_example' # str |  (optional)
category = 'category_example' # str |  (optional)
table = 'table_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
is_hidden = 'is_hidden_example' # str |  (optional)
is_favorite = 'is_favorite_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject172() # InlineObject172 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_partial_update(id, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **query_ast** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **table** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **is_hidden** | **str**|  | [optional] 
 **is_favorite** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject172**](InlineObject172.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_partial_update0**
> v3_search_saved_partial_update0(id, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing saved searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
query_ast = 'query_ast_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
query = 'query_example' # str |  (optional)
category = 'category_example' # str |  (optional)
table = 'table_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
is_hidden = 'is_hidden_example' # str |  (optional)
is_favorite = 'is_favorite_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject173() # InlineObject173 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_partial_update0(id, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **query_ast** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **table** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **is_hidden** | **str**|  | [optional] 
 **is_favorite** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject173**](InlineObject173.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_read**
> v3_search_saved_read(id, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing saved searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
site = 'site_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
created_by = 'created_by_example' # str |  (optional)
updated_by = 'updated_by_example' # str |  (optional)
query_ast = 'query_ast_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
query = 'query_example' # str |  (optional)
category = 'category_example' # str |  (optional)
table = 'table_example' # str |  (optional)
is_protected = 'is_protected_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
is_hidden = 'is_hidden_example' # str |  (optional)
is_favorite = 'is_favorite_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_read(id, site=site, created_at=created_at, updated_at=updated_at, created_by=created_by, updated_by=updated_by, query_ast=query_ast, name=name, description=description, query=query, category=category, table=table, is_protected=is_protected, is_public=is_public, is_hidden=is_hidden, is_favorite=is_favorite, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **site** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **updated_by** | **str**|  | [optional] 
 **query_ast** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **table** | **str**|  | [optional] 
 **is_protected** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **is_hidden** | **str**|  | [optional] 
 **is_favorite** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_create**
> v3_search_saved_schedule_create(parent_lookup_saved_search, data=data)

Overrides the default 'create' method in order to associate the

Overrides the default 'create' method in order to associate the list_id that may be in the URL parameters due to nested routes

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
data = fireeye.helix.InlineObject178() # InlineObject178 |  (optional)

try:
    # Overrides the default 'create' method in order to associate the
    api_instance.v3_search_saved_schedule_create(parent_lookup_saved_search, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_saved_search** | **str**|  | 
 **data** | [**InlineObject178**](InlineObject178.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_delete**
> v3_search_saved_schedule_delete(parent_lookup_saved_search)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing scheduled searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_schedule_delete(parent_lookup_saved_search)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_saved_search** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_delete_0**
> v3_search_saved_schedule_delete_0(id, parent_lookup_saved_search)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing scheduled searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_schedule_delete_0(id, parent_lookup_saved_search)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_jobs_download**
> v3_search_saved_schedule_jobs_download(id, parent_lookup_saved_search)

Downloads the results of a scheduled search job as a zip file.

Downloads the results of a scheduled search job as a zip file.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 

try:
    # Downloads the results of a scheduled search job as a zip file.
    api_instance.v3_search_saved_schedule_jobs_download(id, parent_lookup_saved_search)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_jobs_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_jobs_list**
> v3_search_saved_schedule_jobs_list(parent_lookup_saved_search, limit=limit, offset=offset, state=state)

Endpoint for accessing scheduled search jobs.

Endpoint for accessing scheduled search jobs.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
state = 'state_example' # str |  (optional)

try:
    # Endpoint for accessing scheduled search jobs.
    api_instance.v3_search_saved_schedule_jobs_list(parent_lookup_saved_search, limit=limit, offset=offset, state=state)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_jobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_saved_search** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **state** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_jobs_read**
> v3_search_saved_schedule_jobs_read(id, parent_lookup_saved_search, state=state)

Endpoint for accessing scheduled search jobs.

Endpoint for accessing scheduled search jobs.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
state = 'state_example' # str |  (optional)

try:
    # Endpoint for accessing scheduled search jobs.
    api_instance.v3_search_saved_schedule_jobs_read(id, parent_lookup_saved_search, state=state)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_jobs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 
 **state** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_list**
> v3_search_saved_schedule_list(parent_lookup_saved_search, limit=limit, offset=offset)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing scheduled searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_schedule_list(parent_lookup_saved_search, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_saved_search** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_partial_update**
> v3_search_saved_schedule_partial_update(id, parent_lookup_saved_search, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing scheduled searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
data = fireeye.helix.InlineObject179() # InlineObject179 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_schedule_partial_update(id, parent_lookup_saved_search, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 
 **data** | [**InlineObject179**](InlineObject179.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_partial_update0**
> v3_search_saved_schedule_partial_update0(id, parent_lookup_saved_search, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing scheduled searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
data = fireeye.helix.InlineObject180() # InlineObject180 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_schedule_partial_update0(id, parent_lookup_saved_search, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 
 **data** | [**InlineObject180**](InlineObject180.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_read**
> v3_search_saved_schedule_read(id, parent_lookup_saved_search)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing scheduled searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_schedule_read(id, parent_lookup_saved_search)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parent_lookup_saved_search** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_schedule_update**
> v3_search_saved_schedule_update(parent_lookup_saved_search, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing scheduled searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
parent_lookup_saved_search = 'parent_lookup_saved_search_example' # str | 
data = fireeye.helix.InlineObject177() # InlineObject177 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_schedule_update(parent_lookup_saved_search, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_schedule_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_saved_search** | **str**|  | 
 **data** | [**InlineObject177**](InlineObject177.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_saved_search**
> v3_search_saved_search()

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing saved searches.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_search_saved_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_search_saved_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_stats_get_indexing_latency**
> v3_search_stats_get_indexing_latency()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_search_stats_get_indexing_latency()
except ApiException as e:
    print("Exception when calling V3Api->v3_search_stats_get_indexing_latency: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_tables_create**
> v3_search_tables_create(data=data)

Endpoint for accessing search tables.

Endpoint for accessing search tables.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject181() # InlineObject181 |  (optional)

try:
    # Endpoint for accessing search tables.
    api_instance.v3_search_tables_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_tables_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject181**](InlineObject181.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_tables_delete**
> v3_search_tables_delete(id)

Deletes the specified search table. You can only delete tables that you created.

Deletes the specified search table. You can only delete tables that you created.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Deletes the specified search table. You can only delete tables that you created.
    api_instance.v3_search_tables_delete(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_tables_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_tables_list**
> v3_search_tables_list(limit=limit, offset=offset)

Endpoint for accessing search tables.

Endpoint for accessing search tables.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # Endpoint for accessing search tables.
    api_instance.v3_search_tables_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_tables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_tables_partial_update**
> v3_search_tables_partial_update(id, data=data)

Endpoint for accessing search tables.

Endpoint for accessing search tables.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject182() # InlineObject182 |  (optional)

try:
    # Endpoint for accessing search tables.
    api_instance.v3_search_tables_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_tables_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject182**](InlineObject182.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_tables_partial_update0**
> v3_search_tables_partial_update0(id, data=data)

Endpoint for accessing search tables.

Endpoint for accessing search tables.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
data = fireeye.helix.InlineObject183() # InlineObject183 |  (optional)

try:
    # Endpoint for accessing search tables.
    api_instance.v3_search_tables_partial_update0(id, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_tables_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**InlineObject183**](InlineObject183.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_search_tables_read**
> v3_search_tables_read(id)

Endpoint for accessing search tables.

Endpoint for accessing search tables.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Endpoint for accessing search tables.
    api_instance.v3_search_tables_read(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_search_tables_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_senders_create**
> v3_senders_create()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_senders_create()
except ApiException as e:
    print("Exception when calling V3Api->v3_senders_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_senders_delete**
> v3_senders_delete()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_senders_delete()
except ApiException as e:
    print("Exception when calling V3Api->v3_senders_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_senders_enable_delete**
> v3_senders_enable_delete()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_senders_enable_delete()
except ApiException as e:
    print("Exception when calling V3Api->v3_senders_enable_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_senders_enable_update**
> v3_senders_enable_update()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_senders_enable_update()
except ApiException as e:
    print("Exception when calling V3Api->v3_senders_enable_update: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_senders_read**
> v3_senders_read()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_senders_read()
except ApiException as e:
    print("Exception when calling V3Api->v3_senders_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_sensors_create**
> v3_sensors_create(data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject184() # InlineObject184 |  (optional)

try:
    api_instance.v3_sensors_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_sensors_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject184**](InlineObject184.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_sensors_delete**
> v3_sensors_delete(id, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
interval = 'interval_example' # str |  (optional)
meta_cbid = 'meta_cbid_example' # str |  (optional)
status = 'status_example' # str |  (optional)
status_order = 3.4 # float |  (optional)
hostname = 'hostname_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_sensors_delete(id, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_sensors_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **interval** | **str**|  | [optional] 
 **meta_cbid** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **status_order** | **float**|  | [optional] 
 **hostname** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_sensors_get_sensor_status**
> v3_sensors_get_sensor_status()

Returns the status of your FireEye sensors.

Returns the status of your FireEye sensors.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Returns the status of your FireEye sensors.
    api_instance.v3_sensors_get_sensor_status()
except ApiException as e:
    print("Exception when calling V3Api->v3_sensors_get_sensor_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_sensors_list**
> v3_sensors_list(limit=limit, offset=offset, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by)

Lists your FireEye sensors, including metrics for input events and average CPU and memory usage.

Lists your FireEye sensors, including metrics for input events and average CPU and memory usage.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
interval = 'interval_example' # str |  (optional)
meta_cbid = 'meta_cbid_example' # str |  (optional)
status = 'status_example' # str |  (optional)
status_order = 3.4 # float |  (optional)
hostname = 'hostname_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Lists your FireEye sensors, including metrics for input events and average CPU and memory usage.
    api_instance.v3_sensors_list(limit=limit, offset=offset, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_sensors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **interval** | **str**|  | [optional] 
 **meta_cbid** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **status_order** | **float**|  | [optional] 
 **hostname** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_sensors_partial_update**
> v3_sensors_partial_update(id, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
interval = 'interval_example' # str |  (optional)
meta_cbid = 'meta_cbid_example' # str |  (optional)
status = 'status_example' # str |  (optional)
status_order = 3.4 # float |  (optional)
hostname = 'hostname_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject185() # InlineObject185 |  (optional)

try:
    api_instance.v3_sensors_partial_update(id, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_sensors_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **interval** | **str**|  | [optional] 
 **meta_cbid** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **status_order** | **float**|  | [optional] 
 **hostname** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject185**](InlineObject185.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_sensors_partial_update0**
> v3_sensors_partial_update0(id, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by, data=data)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
interval = 'interval_example' # str |  (optional)
meta_cbid = 'meta_cbid_example' # str |  (optional)
status = 'status_example' # str |  (optional)
status_order = 3.4 # float |  (optional)
hostname = 'hostname_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject186() # InlineObject186 |  (optional)

try:
    api_instance.v3_sensors_partial_update0(id, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_sensors_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **interval** | **str**|  | [optional] 
 **meta_cbid** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **status_order** | **float**|  | [optional] 
 **hostname** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject186**](InlineObject186.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_sensors_read**
> v3_sensors_read(id, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
interval = 'interval_example' # str |  (optional)
meta_cbid = 'meta_cbid_example' # str |  (optional)
status = 'status_example' # str |  (optional)
status_order = 3.4 # float |  (optional)
hostname = 'hostname_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.v3_sensors_read(id, interval=interval, meta_cbid=meta_cbid, status=status, status_order=status_order, hostname=hostname, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_sensors_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **interval** | **str**|  | [optional] 
 **meta_cbid** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **status_order** | **float**|  | [optional] 
 **hostname** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_tags_list**
> v3_tags_list()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    api_instance.v3_tags_list()
except ApiException as e:
    print("Exception when calling V3Api->v3_tags_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_tasks_status_read**
> v3_tasks_status_read(id)



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    api_instance.v3_tasks_status_read(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_tasks_status_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_user_challenge_query**
> v3_user_challenge_query()

Returns a token to use for Talk to an Expert.

Returns a token to use for Talk to an Expert.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Returns a token to use for Talk to an Expert.
    api_instance.v3_user_challenge_query()
except ApiException as e:
    print("Exception when calling V3Api->v3_user_challenge_query: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_user_customer_support_chat**
> v3_user_customer_support_chat()

Connects to SFDC to chat with FireEye Support.

Connects to SFDC to chat with FireEye Support.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Connects to SFDC to chat with FireEye Support.
    api_instance.v3_user_customer_support_chat()
except ApiException as e:
    print("Exception when calling V3Api->v3_user_customer_support_chat: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_user_eod_chat**
> v3_user_eod_chat()

Returns Expert on Demand contact information for authorized users.

Returns Expert on Demand contact information for authorized users.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Returns Expert on Demand contact information for authorized users.
    api_instance.v3_user_eod_chat()
except ApiException as e:
    print("Exception when calling V3Api->v3_user_eod_chat: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_create**
> v3_widgets_templates_create(data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing WidgetTemplates

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject188() # InlineObject188 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_widgets_templates_create(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject188**](InlineObject188.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_delete**
> v3_widgets_templates_delete()

Deletes all widgets from the specified dashboard.

Deletes all widgets from the specified dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # Deletes all widgets from the specified dashboard.
    api_instance.v3_widgets_templates_delete()
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_delete_0**
> v3_widgets_templates_delete_0(id, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by)

Deletes a widget from the specified dashboard.

Deletes a widget from the specified dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
type = 'type_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # Deletes a widget from the specified dashboard.
    api_instance.v3_widgets_templates_delete_0(id, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_list**
> v3_widgets_templates_list(limit=limit, offset=offset, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing WidgetTemplates

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
type = 'type_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_widgets_templates_list(limit=limit, offset=offset, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_partial_update**
> v3_widgets_templates_partial_update(id, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing WidgetTemplates

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
type = 'type_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject189() # InlineObject189 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_widgets_templates_partial_update(id, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject189**](InlineObject189.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_partial_update0**
> v3_widgets_templates_partial_update0(id, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by, data=data)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing WidgetTemplates

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
type = 'type_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
data = fireeye.helix.InlineObject190() # InlineObject190 |  (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_widgets_templates_partial_update0(id, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by, data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_partial_update0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **data** | [**InlineObject190**](InlineObject190.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_perform_search**
> v3_widgets_templates_perform_search(id)

Returns the results of a dashboard widget.

Returns the results of a dashboard widget.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 

try:
    # Returns the results of a dashboard widget.
    api_instance.v3_widgets_templates_perform_search(id)
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_perform_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_read**
> v3_widgets_templates_read(id, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing WidgetTemplates

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
id = 'id_example' # str | 
category = 'category_example' # str |  (optional)
is_internal = 'is_internal_example' # str |  (optional)
is_public = 'is_public_example' # str |  (optional)
type = 'type_example' # str |  (optional)
order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_widgets_templates_read(id, category=category, is_internal=is_internal, is_public=is_public, type=type, order_by=order_by)
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category** | **str**|  | [optional] 
 **is_internal** | **str**|  | [optional] 
 **is_public** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_search**
> v3_widgets_templates_search()

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing WidgetTemplates

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.v3_widgets_templates_search()
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_widgets_templates_update**
> v3_widgets_templates_update(data=data)

Updates all widgets for the specified dashboard.

Updates all widgets for the specified dashboard.

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V3Api()
data = fireeye.helix.InlineObject187() # InlineObject187 |  (optional)

try:
    # Updates all widgets for the specified dashboard.
    api_instance.v3_widgets_templates_update(data=data)
except ApiException as e:
    print("Exception when calling V3Api->v3_widgets_templates_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InlineObject187**](InlineObject187.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

