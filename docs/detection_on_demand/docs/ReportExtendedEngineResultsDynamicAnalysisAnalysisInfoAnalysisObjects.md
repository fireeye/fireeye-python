# ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjects

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha256** | **str** | sha256 of analysed object | 
**chk_sum** | [**list[ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoChkSum]**](ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoChkSum.md) | results of different static analysis engines ran for object | 
**md5_sum** | **str** | md5 of analysed object | 
**is_child** | **bool** | Whether this file is a child of another. The file could contain other files or other embedded objects. | 
**file_desc** | **str** | File extension of analysed object | 
**work_orders** | [**list[ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoWorkOrders]**](ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoWorkOrders.md) | details results of Dynamic analysis jobs ran for analysis object | 
**original_name** | **str** | File name of a analysis object | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


