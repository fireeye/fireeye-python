# ReportExtendedEngineResultsDynamicAnalysis

Detailed Dynamic Analysis results for both extracted objects and as well for submission
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the analysis job. | 
**is_malicious** | **bool** | Result of analysis.  Either malicious or not malicious. | 
**signature** | **str** | signature names based on all the submission results, from Dynamic Analysis | [optional] 
**analysis_info** | [**ReportExtendedEngineResultsDynamicAnalysisAnalysisInfo**](ReportExtendedEngineResultsDynamicAnalysisAnalysisInfo.md) |  | 
**files_analysed** | **int** | Number of objects analysed including primary and extracted objects | 
**overall_weight** | **int** | Maximum weight amongst weights assigned to different triggered rules while dynamic analysis | 
**total_duration** | **int** | Total time spend during Dynamic Analysis in seconds | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


