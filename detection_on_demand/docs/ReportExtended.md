# ReportExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | The analysis job ID of your file submission. | 
**overall_status** | **str** | Indicates whether processing of the submitted file is complete. | 
**is_malicious** | **bool** | FireEye&#39;s final determination if the file is malicious or not. | 
**started_at** | **datetime** | The time processing was started. | 
**completed_at** | **datetime** | The time processing was completed. | 
**duration** | **int** | The processing time in seconds. | 
**file_extension** | **str** | The file extension of the submitted file. | 
**file_name** | **str** | The name of the submitted file. | 
**file_size** | **int** | The size of the submitted file in KB. | 
**md5** | **str** | The MD5 hash. | 
**sha256** | **str** | The SHA256 hash. | 
**signature_name** | **list[str]** | a list of malware signatures determined by our scanning engines | 
**engine_results** | [**ReportExtendedEngineResults**](ReportExtendedEngineResults.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


