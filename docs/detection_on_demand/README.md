## Getting Started

```python
from __future__ import print_function

import time
import fireeye.detection
from fireeye.detection.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://feapi.marketplace.apps.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.detection.Configuration(
    host = "https://feapi.marketplace.apps.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FireEyeAPIKey
configuration = fireeye.detection.Configuration(
    host = "https://feapi.marketplace.apps.fireeye.com",
    api_key = {
        'feye-auth-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['feye-auth-key'] = 'Bearer'


# Enter a context with an instance of the API client
with fireeye.detection.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.detection.FilesApi(api_client)
    file = '/path/to/file' # file | This is the binary file that you want to submit for malware analysis.

    try:
        # Submit a single file for analysis
        api_response = api_instance.post_file(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->post_file: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://feapi.marketplace.apps.fireeye.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FilesApi* | [**post_file**](docs/FilesApi.md#post_file) | **POST** /files | Submit a single file for analysis
*HashesApi* | [**get_hash_by_id**](docs/HashesApi.md#get_hash_by_id) | **GET** /hashes/{hash_id} | Get hash analysis results
*PresignedUrlApi* | [**get_presigned_url**](docs/PresignedUrlApi.md#get_presigned_url) | **GET** /presigned-url/{report_id} | Get a presigned URL
*ReportsApi* | [**get_report**](docs/ReportsApi.md#get_report) | **GET** /reports/{report_id} | Get single report


## Documentation For Models

 - [Forbidden](docs/Forbidden.md)
 - [InlineObject](docs/InlineObject.md)
 - [InternalServerError](docs/InternalServerError.md)
 - [RateLimitExceeded](docs/RateLimitExceeded.md)
 - [ReportExtended](docs/ReportExtended.md)
 - [ReportExtendedEngineResults](docs/ReportExtendedEngineResults.md)
 - [ReportExtendedEngineResultsAvLookup](docs/ReportExtendedEngineResultsAvLookup.md)
 - [ReportExtendedEngineResultsAvsLookup](docs/ReportExtendedEngineResultsAvsLookup.md)
 - [ReportExtendedEngineResultsDtiLookup](docs/ReportExtendedEngineResultsDtiLookup.md)
 - [ReportExtendedEngineResultsDynamicAnalysis](docs/ReportExtendedEngineResultsDynamicAnalysis.md)
 - [ReportExtendedEngineResultsDynamicAnalysisAnalysisInfo](docs/ReportExtendedEngineResultsDynamicAnalysisAnalysisInfo.md)
 - [ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjects](docs/ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjects.md)
 - [ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoChkSum](docs/ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoChkSum.md)
 - [ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoNetworkAnomaly](docs/ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoNetworkAnomaly.md)
 - [ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges](docs/ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.md)
 - [ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesCorrelationResults](docs/ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesCorrelationResults.md)
 - [ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesVmResults](docs/ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesVmResults.md)
 - [ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoWorkOrders](docs/ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoWorkOrders.md)
 - [ReportExtendedEngineResultsFireml](docs/ReportExtendedEngineResultsFireml.md)
 - [ReportNotExtended](docs/ReportNotExtended.md)
 - [Unauthorized](docs/Unauthorized.md)


## Documentation For Authorization


## FireEyeAPIKey

- **Type**: API key
- **API key parameter name**: feye-auth-key
- **Location**: HTTP header


## Author

developers@fireeye.com


