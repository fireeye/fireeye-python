# ReportExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** |  | [optional] 
**overall_status** | **str** | Indicates whether processing of the submitted file is complete. | [optional] 
**is_malicious** | **bool** | FireEye&#39;s final determination if the file is malicious or not. | [optional] 
**started_at** | **str** | The time processing was started. | [optional] 
**completed_at** | **str** | The time processing was completed. | [optional] 
**duration** | **float** | The processing time in seconds. | [optional] 
**file_extension** | **str** | The file extension of the submitted file. | [optional] 
**file_name** | **str** | The name of the submitted file. | [optional] 
**file_size** | **int** | The size of the submitted file in KB. | [optional] 
**md5** | **str** | MD5 hash. | [optional] 
**sha256** | **str** | SHA256 hash. | [optional] 
**signature_name** | **list[str]** |  | [optional] 
**engine_results** | [**ReportExtendedEngineResults**](ReportExtendedEngineResults.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


