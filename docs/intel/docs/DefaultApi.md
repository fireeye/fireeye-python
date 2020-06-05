# fireeye.intel.DefaultApi

All URIs are relative to *http://api.intelligence.fireeye.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a_pi_request**](DefaultApi.md#a_pi_request) | **POST** /collections/indicators/objects | Get context for indicator observables
[**get_actor_details**](DefaultApi.md#get_actor_details) | **GET** /endpoints/actor/{id} | Detailed information for the actor id specified in {id}.
[**get_actor_related**](DefaultApi.md#get_actor_related) | **GET** /endpoints/actor/{id}/{related} | Filter only related information for actor specified in {related}.
[**get_actor_summary**](DefaultApi.md#get_actor_summary) | **GET** /endpoints/actor/{id}/summary | Summary for the actor id specified in {id}.
[**get_all_actors**](DefaultApi.md#get_all_actors) | **GET** /endpoints/actor | List of all actors present in our system. This can be considered as vocab endpoint for actors.
[**get_all_attack_patterns**](DefaultApi.md#get_all_attack_patterns) | **GET** /endpoints/attack-pattern | List of all attack-patterns present in our system. This can be considered as vocab endpoint for attack-patterns.
[**get_all_cve**](DefaultApi.md#get_all_cve) | **GET** /endpoints/cve | List of all CVEs present in our system. This can be considered as vocab endpoint for cve.
[**get_all_entities**](DefaultApi.md#get_all_entities) | **GET** /entities | Extracted Entities.
[**get_all_etu_collections**](DefaultApi.md#get_all_etu_collections) | **GET** /endpoints | Endpoint details for all supported collection types.
[**get_all_industries**](DefaultApi.md#get_all_industries) | **GET** /endpoints/industry | List of all industries present in our system. This can be considered as vocab endpoint for industries.
[**get_all_iocs**](DefaultApi.md#get_all_iocs) | **GET** /endpoints/ioc | List of all iocs present in our system. This can be considered as vocab endpoint for iocs.
[**get_all_locations**](DefaultApi.md#get_all_locations) | **GET** /endpoints/location | List of all locations present in our system. This can be considered as vocab endpoint for locations.
[**get_all_malwares**](DefaultApi.md#get_all_malwares) | **GET** /endpoints/malware | List of all malwares present in our system. This can be considered as vocab endpoint for malwares.
[**get_all_news_reports**](DefaultApi.md#get_all_news_reports) | **GET** /endpoints/news | List of all news analysis reports present in our system.
[**get_all_reports**](DefaultApi.md#get_all_reports) | **GET** /endpoints/report | List of all reports present in our system. This can be considered as vocab endpoint for reports.
[**get_all_taa_reports**](DefaultApi.md#get_all_taa_reports) | **GET** /endpoints/taa | List of all reports of type Threat Activity Alert present in our system.
[**get_all_trend_vocab**](DefaultApi.md#get_all_trend_vocab) | **GET** /trend/vocab | List of all possible filter values for which we have trending data for malware and cve.
[**get_all_trend_vocab_industry_sector**](DefaultApi.md#get_all_trend_vocab_industry_sector) | **GET** /trend/vocab/industry_sector | List of industry_sectors for which we have trending data for malware and cve.
[**get_all_trend_vocab_region**](DefaultApi.md#get_all_trend_vocab_region) | **GET** /trend/vocab/region | List of regions for which we have trending data for malware and cve.
[**get_attack_pattern_details**](DefaultApi.md#get_attack_pattern_details) | **GET** /endpoints/attack-pattern/{id} | Detailed information for the attack-pattern id specified in {id}.
[**get_attack_pattern_related**](DefaultApi.md#get_attack_pattern_related) | **GET** /endpoints/attack-pattern/{id}/{related} | Filter only related information for attack-pattern specified in {related}.
[**get_attack_pattern_summary**](DefaultApi.md#get_attack_pattern_summary) | **GET** /endpoints/attack-pattern/{id}/summary | Summary for the attack-pattern id specified in {id}.
[**get_cve_details**](DefaultApi.md#get_cve_details) | **GET** /endpoints/cve/{id} | Detailed information for the CVE id specified in {id}.
[**get_industry_details**](DefaultApi.md#get_industry_details) | **GET** /endpoints/industry/{id} | Detailed information for the industry id specified in {id}.
[**get_industry_related**](DefaultApi.md#get_industry_related) | **GET** /endpoints/industry/{id}/{related} | Filter only related information for industry specified in {related}.
[**get_industry_summary**](DefaultApi.md#get_industry_summary) | **GET** /endpoints/industry/{id}/summary | Summary for the industry id specified in {id}.
[**get_ioc_details**](DefaultApi.md#get_ioc_details) | **GET** /endpoints/ioc/{id} | Detailed information for the ioc id specified in {id}.
[**get_ioc_related**](DefaultApi.md#get_ioc_related) | **GET** /endpoints/ioc/{id}/{related} | Filter only related information for ioc specified in {related}.
[**get_ioc_summary**](DefaultApi.md#get_ioc_summary) | **GET** /endpoints/ioc/{id}/summary | Summary for the ioc id specified in {id}.
[**get_latest_trends**](DefaultApi.md#get_latest_trends) | **GET** /trend | Top trends of each supported type.
[**get_latest_trends_0**](DefaultApi.md#get_latest_trends_0) | **GET** /trend/malware | Top 10 trending Malware within given date range and optionally grouped by geographical region or industry sector
[**get_location_details**](DefaultApi.md#get_location_details) | **GET** /endpoints/location/{id} | Detailed information for the location id specified in {id}.
[**get_location_related**](DefaultApi.md#get_location_related) | **GET** /endpoints/location/{id}/{related} | Filter only related information for location specified in {related}.
[**get_location_summary**](DefaultApi.md#get_location_summary) | **GET** /endpoints/location/{id}/summary | Summary for the location id specified in {id}.
[**get_malware_details**](DefaultApi.md#get_malware_details) | **GET** /endpoints/malware/{id} | Detailed information for the malware id specified in {id}.
[**get_malware_related**](DefaultApi.md#get_malware_related) | **GET** /endpoints/malware/{id}/{related} | Filter only related information for malware specified in {related}.
[**get_malware_summary**](DefaultApi.md#get_malware_summary) | **GET** /endpoints/malware/{id}/summary | Summary for the malware id specified in {id}.
[**get_news_details**](DefaultApi.md#get_news_details) | **GET** /endpoints/news/{id} | Detailed information for the news analysis report id specified in {id}.
[**get_news_related_reports**](DefaultApi.md#get_news_related_reports) | **GET** /endpoints/news/{id}/{related} | Filter only related report information for news analysis report.
[**get_report_details**](DefaultApi.md#get_report_details) | **GET** /endpoints/report/{id} | Detailed information for the report id specified in {id}.
[**get_report_related**](DefaultApi.md#get_report_related) | **GET** /endpoints/report/{id}/{related} | Filter only related information for report specified in {related}.
[**get_report_summary**](DefaultApi.md#get_report_summary) | **GET** /endpoints/report/{id}/summary | Summary for the report id specified in {id}.
[**get_taa_report_details**](DefaultApi.md#get_taa_report_details) | **GET** /endpoints/taa/{id} | Detailed information for the Threat Activity Alert report id specified in {id}.
[**get_taa_report_related**](DefaultApi.md#get_taa_report_related) | **GET** /endpoints/taa/{id}/{related} | Filter only related information for Report of type Threat Activity Alert specified in {related}.
[**get_taa_report_summary**](DefaultApi.md#get_taa_report_summary) | **GET** /endpoints/taa/{id}/summary | Summary for the Threat Activity Alert report id specified in {id}.
[**get_trend_actor_id**](DefaultApi.md#get_trend_actor_id) | **GET** /trend/actor/{id} | All trending information of an actor by id
[**get_trend_actor_related**](DefaultApi.md#get_trend_actor_related) | **GET** /trend/actor/{id}/{related} | Associated trending information of related type for an actor by id
[**get_trend_region_id**](DefaultApi.md#get_trend_region_id) | **GET** /trend/region/{id} | All trending information of an region by id
[**get_trend_region_related**](DefaultApi.md#get_trend_region_related) | **GET** /trend/region/{id}/{related} | Associated trending information of related type for an region by id
[**get_trending_actor**](DefaultApi.md#get_trending_actor) | **GET** /trend/actor | Top 10 trending actors by the timeline of recent activity
[**get_trending_cve**](DefaultApi.md#get_trending_cve) | **GET** /trend/cve | Top 5 trending CVEs within given date range and optionally grouped by industry sector
[**get_trending_region**](DefaultApi.md#get_trending_region) | **GET** /trend/region | Top 10 trending regions
[**get_yara_signature**](DefaultApi.md#get_yara_signature) | **GET** /endpoints/yara | List of all yara signatures present in our system.
[**post_all_entities**](DefaultApi.md#post_all_entities) | **POST** /entities | Bulk look up of Entities.


# **a_pi_request**
> AnyOfipContexthashContextfqdnContextsignatureContextsignatureIdContextemailContexturlContext a_pi_request(unknown_base_type=unknown_base_type)

Get context for indicator observables

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    unknown_base_type = fireeye.intel.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

    try:
        # Get context for indicator observables
        api_response = api_instance.a_pi_request(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->a_pi_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

[**AnyOfipContexthashContextfqdnContextsignatureContextsignatureIdContextemailContexturlContext**](AnyOfipContexthashContextfqdnContextsignatureContextsignatureIdContextemailContexturlContext.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Json response with specified context for IP. |  -  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actor_details**
> EndpointsActorIdResponse get_actor_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the actor id specified in {id}.

Details information about actor.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the actor id specified in {id}.
        api_response = api_instance.get_actor_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_actor_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsActorIdResponse**](EndpointsActorIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actor_related**
> AnyOfendpointsActorRelatedResponserelatedCountResponse get_actor_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)

Filter only related information for actor specified in {related}.

Actor Related Details.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumRelatedValues() # EnumRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of related objects specified by the related parameter. (optional)

    try:
        # Filter only related information for actor specified in {related}.
        api_response = api_instance.get_actor_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_actor_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of related objects specified by the related parameter. | [optional] 

### Return type

[**AnyOfendpointsActorRelatedResponserelatedCountResponse**](AnyOfendpointsActorRelatedResponserelatedCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actor_summary**
> Actor get_actor_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Summary for the actor id specified in {id}.

Actor summary.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Summary for the actor id specified in {id}.
        api_response = api_instance.get_actor_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_actor_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**Actor**](Actor.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_actors**
> EndpointsActorResponse get_all_actors(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all actors present in our system. This can be considered as vocab endpoint for actors.

Returns list of all the actors present in the system.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all actors present in our system. This can be considered as vocab endpoint for actors.
        api_response = api_instance.get_all_actors(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_actors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsActorResponse**](EndpointsActorResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_attack_patterns**
> EndpointsAttackPatternResponse get_all_attack_patterns(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all attack-patterns present in our system. This can be considered as vocab endpoint for attack-patterns.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all attack-patterns present in our system. This can be considered as vocab endpoint for attack-patterns.
        api_response = api_instance.get_all_attack_patterns(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_attack_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsAttackPatternResponse**](EndpointsAttackPatternResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cve**
> EndpointsCveResponse get_all_cve(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all CVEs present in our system. This can be considered as vocab endpoint for cve.

Returns list of all the cve present in the system.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all CVEs present in our system. This can be considered as vocab endpoint for cve.
        api_response = api_instance.get_all_cve(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_cve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsCveResponse**](EndpointsCveResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_entities**
> EntitiesSpecificProperties get_all_entities(accept=accept, authorization=authorization, x_app_name=x_app_name, match_type=match_type)

Extracted Entities.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json, application/gzip' # str | Specifies the format in which the client would like the response. (optional)
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
match_type = 'match_type_example' # str | This will list all entities matching with the queried match.type. (optional)

    try:
        # Extracted Entities.
        api_response = api_instance.get_all_entities(accept=accept, authorization=authorization, x_app_name=x_app_name, match_type=match_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] 
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **match_type** | **str**| This will list all entities matching with the queried match.type. | [optional] 

### Return type

[**EntitiesSpecificProperties**](EntitiesSpecificProperties.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_etu_collections**
> list[EndpointCollection] get_all_etu_collections(accept=accept, authorization=authorization, x_app_name=x_app_name)

Endpoint details for all supported collection types.

Returns details for the all supported collection types.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Endpoint details for all supported collection types.
        api_response = api_instance.get_all_etu_collections(accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_etu_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**list[EndpointCollection]**](EndpointCollection.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_industries**
> EndpointsIndustryResponse get_all_industries(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all industries present in our system. This can be considered as vocab endpoint for industries.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all industries present in our system. This can be considered as vocab endpoint for industries.
        api_response = api_instance.get_all_industries(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_industries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsIndustryResponse**](EndpointsIndustryResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_iocs**
> EndpointsIocsResponse get_all_iocs(accept=accept, authorization=authorization, x_app_name=x_app_name, type=type, name=name, value=value, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all iocs present in our system. This can be considered as vocab endpoint for iocs.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
type = 'type_example' # str | This will list all the iocs matching(substring match) for the type specified. Values for type are - indicator, file, domain, url, ip and email. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
value = 'value_example' # str | This will list all the objects matching(substring match) with the queried value. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all iocs present in our system. This can be considered as vocab endpoint for iocs.
        api_response = api_instance.get_all_iocs(accept=accept, authorization=authorization, x_app_name=x_app_name, type=type, name=name, value=value, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_iocs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **type** | **str**| This will list all the iocs matching(substring match) for the type specified. Values for type are - indicator, file, domain, url, ip and email. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **value** | **str**| This will list all the objects matching(substring match) with the queried value. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsIocsResponse**](EndpointsIocsResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_locations**
> EndpointsLocationResponse get_all_locations(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all locations present in our system. This can be considered as vocab endpoint for locations.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all locations present in our system. This can be considered as vocab endpoint for locations.
        api_response = api_instance.get_all_locations(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsLocationResponse**](EndpointsLocationResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_malwares**
> EndpointsMalwareResponse get_all_malwares(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all malwares present in our system. This can be considered as vocab endpoint for malwares.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all malwares present in our system. This can be considered as vocab endpoint for malwares.
        api_response = api_instance.get_all_malwares(accept=accept, authorization=authorization, x_app_name=x_app_name, name=name, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_malwares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsMalwareResponse**](EndpointsMalwareResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_news_reports**
> EndpointsNewsResponse get_all_news_reports(accept=accept, authorization=authorization, x_app_name=x_app_name, title=title, media_comment=media_comment, media_outlet=media_outlet, judgment=judgment, analyst_comment=analyst_comment, added_after=added_after, report_id=report_id, related_reports_title=related_reports_title, related_reports_report_id=related_reports_report_id, limit=limit, next=next)

List of all news analysis reports present in our system.

Returns list of all the news analysis reports present in the system.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
title = 'title_example' # str | This will list all the news analysis reports matching(substring match) with the queried title. (optional)
media_comment = 'media_comment_example' # str | This will list all the news analysis reports matching(substring match) with the queried media_comment. (optional)
media_outlet = 'media_outlet_example' # str | This will list all the news analysis reports matching(substring match) with the queried media_outlet. (optional)
judgment = 'judgment_example' # str | This will list all the news analysis reports matching(substring match) with the queried judgment. (optional)
analyst_comment = 'analyst_comment_example' # str | This will list all the news analysis reports matching(substring match) with the queried analyst_comment. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
report_id = 'report_id_example' # str | This will list all the reports matching(substring match) for the report_id specified. (optional)
related_reports_title = 'related_reports_title_example' # str | This will list all reports for news analysis where title of related reports matches(substring match) with the queried related_reports.title. (optional)
related_reports_report_id = 'related_reports_report_id_example' # str | This will list all reports for news analysis where report_id of related reports matches with the queried related_reports.report_id. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all news analysis reports present in our system.
        api_response = api_instance.get_all_news_reports(accept=accept, authorization=authorization, x_app_name=x_app_name, title=title, media_comment=media_comment, media_outlet=media_outlet, judgment=judgment, analyst_comment=analyst_comment, added_after=added_after, report_id=report_id, related_reports_title=related_reports_title, related_reports_report_id=related_reports_report_id, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_news_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **title** | **str**| This will list all the news analysis reports matching(substring match) with the queried title. | [optional] 
 **media_comment** | **str**| This will list all the news analysis reports matching(substring match) with the queried media_comment. | [optional] 
 **media_outlet** | **str**| This will list all the news analysis reports matching(substring match) with the queried media_outlet. | [optional] 
 **judgment** | **str**| This will list all the news analysis reports matching(substring match) with the queried judgment. | [optional] 
 **analyst_comment** | **str**| This will list all the news analysis reports matching(substring match) with the queried analyst_comment. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **report_id** | **str**| This will list all the reports matching(substring match) for the report_id specified. | [optional] 
 **related_reports_title** | **str**| This will list all reports for news analysis where title of related reports matches(substring match) with the queried related_reports.title. | [optional] 
 **related_reports_report_id** | **str**| This will list all reports for news analysis where report_id of related reports matches with the queried related_reports.report_id. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsNewsResponse**](EndpointsNewsResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_reports**
> EndpointsReportResponse get_all_reports(accept=accept, authorization=authorization, x_app_name=x_app_name, type=type, name=name, report_id=report_id, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all reports present in our system. This can be considered as vocab endpoint for reports.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
type = 'type_example' # str | This will list all the reports matching(substring match) for the type specified. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
report_id = 'report_id_example' # str | This will list all the reports matching(substring match) for the report_id specified. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all reports present in our system. This can be considered as vocab endpoint for reports.
        api_response = api_instance.get_all_reports(accept=accept, authorization=authorization, x_app_name=x_app_name, type=type, name=name, report_id=report_id, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **type** | **str**| This will list all the reports matching(substring match) for the type specified. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **report_id** | **str**| This will list all the reports matching(substring match) for the report_id specified. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsReportResponse**](EndpointsReportResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_taa_reports**
> EndpointsReportResponse get_all_taa_reports(accept=accept, authorization=authorization, x_app_name=x_app_name, type=type, name=name, report_id=report_id, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)

List of all reports of type Threat Activity Alert present in our system.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
type = 'type_example' # str | This will list all the reports matching(substring match) for the type specified. (optional)
name = 'name_example' # str | This will list all the objects matching(substring match) with the queried name. (optional)
report_id = 'report_id_example' # str | This will list all the reports matching(substring match) for the report_id specified. (optional)
added_after = 'added_after_example' # str | This will list all the objects added after queried date. The supported data format is '%Y-%m-%dT%H:%M:%S.%fZ' along with epoch time. (optional)
sort_by = 'sort_by_example' # str | This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. (optional)
order_by = 'order_by_example' # str | This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \"asc\" and \"desc\". The default order is ascending if order_by query paramter is not specified. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)
next = 'next_example' # str | This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. (optional)

    try:
        # List of all reports of type Threat Activity Alert present in our system.
        api_response = api_instance.get_all_taa_reports(accept=accept, authorization=authorization, x_app_name=x_app_name, type=type, name=name, report_id=report_id, added_after=added_after, sort_by=sort_by, order_by=order_by, limit=limit, next=next)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_taa_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **type** | **str**| This will list all the reports matching(substring match) for the type specified. | [optional] 
 **name** | **str**| This will list all the objects matching(substring match) with the queried name. | [optional] 
 **report_id** | **str**| This will list all the reports matching(substring match) for the report_id specified. | [optional] 
 **added_after** | **str**| This will list all the objects added after queried date. The supported data format is &#39;%Y-%m-%dT%H:%M:%S.%fZ&#39; along with epoch time. | [optional] 
 **sort_by** | **str**| This will sort objects by field specified in the sort_by. The supported fields are name, created and modified. The default sorting is by modified if sort_by query paramter is not specified. | [optional] 
 **order_by** | **str**| This will arrange all objects in order specified in the order_by field. The supported values in order_by field are \&quot;asc\&quot; and \&quot;desc\&quot;. The default order is ascending if order_by query paramter is not specified. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 
 **next** | **str**| This is the pagination parameter used to retrieve next set of objects specified in limit parameter otherwise default 500 objects or in last iteration remaining all objects. | [optional] 

### Return type

[**EndpointsReportResponse**](EndpointsReportResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_trend_vocab**
> TrendVocabResponse get_all_trend_vocab(accept=accept, authorization=authorization, x_app_name=x_app_name)

List of all possible filter values for which we have trending data for malware and cve.

Returns list of all possible filter values for which we have trending data for malware and cve.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # List of all possible filter values for which we have trending data for malware and cve.
        api_response = api_instance.get_all_trend_vocab(accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_trend_vocab: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**TrendVocabResponse**](TrendVocabResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_trend_vocab_industry_sector**
> TrendVocabIndustrySectorResponse get_all_trend_vocab_industry_sector(accept=accept, authorization=authorization, x_app_name=x_app_name)

List of industry_sectors for which we have trending data for malware and cve.

Returns list of industry_sectors for which we have trending data for malware and cve.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # List of industry_sectors for which we have trending data for malware and cve.
        api_response = api_instance.get_all_trend_vocab_industry_sector(accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_trend_vocab_industry_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**TrendVocabIndustrySectorResponse**](TrendVocabIndustrySectorResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_trend_vocab_region**
> TrendVocabRegionResponse get_all_trend_vocab_region(accept=accept, authorization=authorization, x_app_name=x_app_name)

List of regions for which we have trending data for malware and cve.

Returns list of regions for which we have trending data for malware and cve.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # List of regions for which we have trending data for malware and cve.
        api_response = api_instance.get_all_trend_vocab_region(accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_trend_vocab_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**TrendVocabRegionResponse**](TrendVocabRegionResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_pattern_details**
> EndpointsAttackPatternIdResponse get_attack_pattern_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the attack-pattern id specified in {id}.

Details information about attack-pattern.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the attack-pattern id specified in {id}.
        api_response = api_instance.get_attack_pattern_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_attack_pattern_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsAttackPatternIdResponse**](EndpointsAttackPatternIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_pattern_related**
> AnyOfendpointsAttackPatternRelatedResponserelatedCountResponse get_attack_pattern_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)

Filter only related information for attack-pattern specified in {related}.

Industry Related Details.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumRelatedValues() # EnumRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of related objects specified by the related parameter. (optional)

    try:
        # Filter only related information for attack-pattern specified in {related}.
        api_response = api_instance.get_attack_pattern_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_attack_pattern_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of related objects specified by the related parameter. | [optional] 

### Return type

[**AnyOfendpointsAttackPatternRelatedResponserelatedCountResponse**](AnyOfendpointsAttackPatternRelatedResponserelatedCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_pattern_summary**
> AttackPattern get_attack_pattern_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Summary for the attack-pattern id specified in {id}.

Attack Pattern summary.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Summary for the attack-pattern id specified in {id}.
        api_response = api_instance.get_attack_pattern_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_attack_pattern_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**AttackPattern**](AttackPattern.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cve_details**
> EndpointsCveIdResponse get_cve_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the CVE id specified in {id}.

Details information about cve.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Id for which details are requested where id can be cve identifier or vulnerability object id.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the CVE id specified in {id}.
        api_response = api_instance.get_cve_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_cve_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id for which details are requested where id can be cve identifier or vulnerability object id. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsCveIdResponse**](EndpointsCveIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_industry_details**
> EndpointsIndustryIdResponse get_industry_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the industry id specified in {id}.

Details information about industry.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the industry id specified in {id}.
        api_response = api_instance.get_industry_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_industry_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsIndustryIdResponse**](EndpointsIndustryIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_industry_related**
> AnyOfendpointsIndustryRelatedResponserelatedCountResponse get_industry_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)

Filter only related information for industry specified in {related}.

Industry Related Details.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumRelatedValues() # EnumRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of related objects specified by the related parameter. (optional)

    try:
        # Filter only related information for industry specified in {related}.
        api_response = api_instance.get_industry_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_industry_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of related objects specified by the related parameter. | [optional] 

### Return type

[**AnyOfendpointsIndustryRelatedResponserelatedCountResponse**](AnyOfendpointsIndustryRelatedResponserelatedCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_industry_summary**
> Identity get_industry_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Summary for the industry id specified in {id}.

Industry summary.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Summary for the industry id specified in {id}.
        api_response = api_instance.get_industry_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_industry_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**Identity**](Identity.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ioc_details**
> EndpointsIocIdResponse get_ioc_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the ioc id specified in {id}.

Details information about ioc.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the ioc id specified in {id}.
        api_response = api_instance.get_ioc_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_ioc_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsIocIdResponse**](EndpointsIocIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ioc_related**
> AnyOfendpointsIocRelatedResponserelatedCountResponse get_ioc_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)

Filter only related information for ioc specified in {related}.

Ioc Related Details.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumRelatedValues() # EnumRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of related objects specified by the related parameter. (optional)

    try:
        # Filter only related information for ioc specified in {related}.
        api_response = api_instance.get_ioc_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_ioc_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of related objects specified by the related parameter. | [optional] 

### Return type

[**AnyOfendpointsIocRelatedResponserelatedCountResponse**](AnyOfendpointsIocRelatedResponserelatedCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ioc_summary**
> Ioc get_ioc_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Summary for the ioc id specified in {id}.

Ioc summary.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Summary for the ioc id specified in {id}.
        api_response = api_instance.get_ioc_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_ioc_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**Ioc**](Ioc.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_trends**
> TrendResponse get_latest_trends(accept=accept, authorization=authorization, x_app_name=x_app_name)

Top trends of each supported type.

Returns the latest trending stats available for all supported trending collection types.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Top trends of each supported type.
        api_response = api_instance.get_latest_trends(accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_latest_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**TrendResponse**](TrendResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_trends_0**
> MalwareTrendResponse get_latest_trends_0(accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, region=region, industry_sector=industry_sector)

Top 10 trending Malware within given date range and optionally grouped by geographical region or industry sector

Returns top 10 trending Malware within given date range and optionally grouped by geographical region or industry sector

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
start_date = 'start_date_example' # str | Starting date of the requested time window of trending stat of a collection type. (optional)
end_date = 'end_date_example' # str | End date of the requested time window of trending stat of a collection type. (optional)
region = 'region_example' # str | Specifies filtering criteria in terms of geographical region (ISO Country code 2 or any of [North America, Americas, MENA, Gulf Cooperation Council, Africa, Europe, Middle-East]) for trending stat of a collection type. (optional)
industry_sector = 'industry_sector_example' # str | Specifies filtering criteria in terms of industry sector for trending stat of a collection type. (optional)

    try:
        # Top 10 trending Malware within given date range and optionally grouped by geographical region or industry sector
        api_response = api_instance.get_latest_trends_0(accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, region=region, industry_sector=industry_sector)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_latest_trends_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **start_date** | **str**| Starting date of the requested time window of trending stat of a collection type. | [optional] 
 **end_date** | **str**| End date of the requested time window of trending stat of a collection type. | [optional] 
 **region** | **str**| Specifies filtering criteria in terms of geographical region (ISO Country code 2 or any of [North America, Americas, MENA, Gulf Cooperation Council, Africa, Europe, Middle-East]) for trending stat of a collection type. | [optional] 
 **industry_sector** | **str**| Specifies filtering criteria in terms of industry sector for trending stat of a collection type. | [optional] 

### Return type

[**MalwareTrendResponse**](MalwareTrendResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_details**
> EndpointsLocationIdResponse get_location_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the location id specified in {id}.

Details information about location.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the location id specified in {id}.
        api_response = api_instance.get_location_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_location_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsLocationIdResponse**](EndpointsLocationIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_related**
> AnyOfendpointsLocationRelatedResponserelatedCountResponse get_location_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)

Filter only related information for location specified in {related}.

Location Related Details.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumRelatedValues() # EnumRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of related objects specified by the related parameter. (optional)

    try:
        # Filter only related information for location specified in {related}.
        api_response = api_instance.get_location_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_location_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of related objects specified by the related parameter. | [optional] 

### Return type

[**AnyOfendpointsLocationRelatedResponserelatedCountResponse**](AnyOfendpointsLocationRelatedResponserelatedCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_summary**
> Location get_location_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Summary for the location id specified in {id}.

Location summary.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Summary for the location id specified in {id}.
        api_response = api_instance.get_location_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_location_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_malware_details**
> EndpointsMalwareIdResponse get_malware_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the malware id specified in {id}.

Details information about malware.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the malware id specified in {id}.
        api_response = api_instance.get_malware_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_malware_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsMalwareIdResponse**](EndpointsMalwareIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_malware_related**
> AnyOfendpointsMalwareRelatedResponserelatedCountResponse get_malware_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)

Filter only related information for malware specified in {related}.

Malware Related Details.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumRelatedValues() # EnumRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of related objects specified by the related parameter. (optional)

    try:
        # Filter only related information for malware specified in {related}.
        api_response = api_instance.get_malware_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_malware_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of related objects specified by the related parameter. | [optional] 

### Return type

[**AnyOfendpointsMalwareRelatedResponserelatedCountResponse**](AnyOfendpointsMalwareRelatedResponserelatedCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_malware_summary**
> Malware get_malware_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Summary for the malware id specified in {id}.

Malware summary.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Summary for the malware id specified in {id}.
        api_response = api_instance.get_malware_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_malware_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**Malware**](Malware.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_details**
> EndpointsNewsIdResponse get_news_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the news analysis report id specified in {id}.

Details information about news analysis report.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the news analysis report id specified in {id}.
        api_response = api_instance.get_news_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_news_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsNewsIdResponse**](EndpointsNewsIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_related_reports**
> EndpointsNewsRelatedResponse get_news_related_reports(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name)

Filter only related report information for news analysis report.

Related reports details for specified news analysis report id.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = 'related_example' # str | Related parameter to give only related reports for news analysis report.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Filter only related report information for news analysis report.
        api_response = api_instance.get_news_related_reports(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_news_related_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | **str**| Related parameter to give only related reports for news analysis report. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsNewsRelatedResponse**](EndpointsNewsRelatedResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_details**
> EndpointsReportIdResponse get_report_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the report id specified in {id}.

Details information about report.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the report id specified in {id}.
        api_response = api_instance.get_report_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_report_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsReportIdResponse**](EndpointsReportIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_related**
> AnyOfendpointsReportRelatedResponserelatedCountResponse get_report_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)

Filter only related information for report specified in {related}.

Report Related Details.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumRelatedValues() # EnumRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of related objects specified by the related parameter. (optional)

    try:
        # Filter only related information for report specified in {related}.
        api_response = api_instance.get_report_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_report_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of related objects specified by the related parameter. | [optional] 

### Return type

[**AnyOfendpointsReportRelatedResponserelatedCountResponse**](AnyOfendpointsReportRelatedResponserelatedCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_summary**
> Report get_report_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Summary for the report id specified in {id}.

Report summary.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Summary for the report id specified in {id}.
        api_response = api_instance.get_report_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_report_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taa_report_details**
> EndpointsReportIdResponse get_taa_report_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Detailed information for the Threat Activity Alert report id specified in {id}.

Details information about report of type Threat Activity Alert.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Detailed information for the Threat Activity Alert report id specified in {id}.
        api_response = api_instance.get_taa_report_details(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_taa_report_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**EndpointsReportIdResponse**](EndpointsReportIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taa_report_related**
> AnyOfendpointsReportRelatedResponserelatedCountResponse get_taa_report_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)

Filter only related information for Report of type Threat Activity Alert specified in {related}.

Report of type Threat Activity Alert Related Details.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumRelatedValues() # EnumRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of related objects specified by the related parameter. (optional)

    try:
        # Filter only related information for Report of type Threat Activity Alert specified in {related}.
        api_response = api_instance.get_taa_report_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_taa_report_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of related objects specified by the related parameter. | [optional] 

### Return type

[**AnyOfendpointsReportRelatedResponserelatedCountResponse**](AnyOfendpointsReportRelatedResponserelatedCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taa_report_summary**
> Report get_taa_report_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

Summary for the Threat Activity Alert report id specified in {id}.

Report of type Threat Activity Alert summary.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Summary for the Threat Activity Alert report id specified in {id}.
        api_response = api_instance.get_taa_report_summary(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_taa_report_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trend_actor_id**
> TrendActorIdResponse get_trend_actor_id(id, accept=accept, authorization=authorization, x_app_name=x_app_name, metric_confidence=metric_confidence)

All trending information of an actor by id

Returns all trending information of an actor by id.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
metric_confidence = 'metric_confidence_example' # str | Applies to all the associated object’s metrics confidence. It is used to filter associated/related metrics data of an actor by specified confidence level. (optional)

    try:
        # All trending information of an actor by id
        api_response = api_instance.get_trend_actor_id(id, accept=accept, authorization=authorization, x_app_name=x_app_name, metric_confidence=metric_confidence)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_trend_actor_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **metric_confidence** | **str**| Applies to all the associated object’s metrics confidence. It is used to filter associated/related metrics data of an actor by specified confidence level. | [optional] 

### Return type

[**TrendActorIdResponse**](TrendActorIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trend_actor_related**
> AnyOftrendActorMalwareRelatedResponsetrendActorCveRelatedResponsetrendActorRegionTargetRelatedResponsetrendActorTargetingIndustriesRelatedResponse get_trend_actor_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, confidence=confidence)

Associated trending information of related type for an actor by id

Returns associated trending information of related type for an actor by id.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumTrendActorRelatedValues() # EnumTrendActorRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
start_date = 'start_date_example' # str | Represents start date of metrics of related objects. When only start date is given, it will give list of related objects where start_date falls in the range of metrics start_date and end_date period. (optional)
end_date = 'end_date_example' # str | Represents end date of metrics of related objects. When provided with start_date it would be exact match of start_date and end_date. (optional)
confidence = 'confidence_example' # str | Applies to confidence of related object’s metrics. Used to filter related objects by specific confidence level of the metrics. (optional)

    try:
        # Associated trending information of related type for an actor by id
        api_response = api_instance.get_trend_actor_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, confidence=confidence)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_trend_actor_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumTrendActorRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **start_date** | **str**| Represents start date of metrics of related objects. When only start date is given, it will give list of related objects where start_date falls in the range of metrics start_date and end_date period. | [optional] 
 **end_date** | **str**| Represents end date of metrics of related objects. When provided with start_date it would be exact match of start_date and end_date. | [optional] 
 **confidence** | **str**| Applies to confidence of related object’s metrics. Used to filter related objects by specific confidence level of the metrics. | [optional] 

### Return type

[**AnyOftrendActorMalwareRelatedResponsetrendActorCveRelatedResponsetrendActorRegionTargetRelatedResponsetrendActorTargetingIndustriesRelatedResponse**](AnyOftrendActorMalwareRelatedResponsetrendActorCveRelatedResponsetrendActorRegionTargetRelatedResponsetrendActorTargetingIndustriesRelatedResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trend_region_id**
> TrendRegionIdResponse get_trend_region_id(id, accept=accept, authorization=authorization, x_app_name=x_app_name)

All trending information of an region by id

Returns all trending information of an region by id.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # All trending information of an region by id
        api_response = api_instance.get_trend_region_id(id, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_trend_region_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**TrendRegionIdResponse**](TrendRegionIdResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trend_region_related**
> AnyOftrendRegionMalwareRelatedResponsetrendRegionMalwareInboundRelatedResponsetrendRegionMalwareOutboundRelatedResponsetrendRegionCveRelatedResponsetrendRegionCveInboundRelatedResponsetrendRegionCveOutboundRelatedResponsetrendRegionIndustryRelatedResponsetrendRegionTargetedIndustriesRelatedResponsetrendRegionTargetingIndustriesRelatedResponsetrendRegionActorRelatedResponsetrendRegionActorsTargetingRelatedResponsetrendRegionActorsLocatedRelatedResponsetrendRegionRegionRelatedResponsetrendRegionRegionSourceRelatedResponsetrendRegionRegionTargetRelatedResponse get_trend_region_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name)

Associated trending information of related type for an region by id

Returns associated trending information of related type for an region by id.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    id = 'id_example' # str | Object id for which details are requested.
related = fireeye.intel.EnumTrendRegionRelatedValues() # EnumTrendRegionRelatedValues | Related parameter to filter specific response block.
accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Associated trending information of related type for an region by id
        api_response = api_instance.get_trend_region_related(id, related, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_trend_region_related: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id for which details are requested. | 
 **related** | [**EnumTrendRegionRelatedValues**](.md)| Related parameter to filter specific response block. | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**AnyOftrendRegionMalwareRelatedResponsetrendRegionMalwareInboundRelatedResponsetrendRegionMalwareOutboundRelatedResponsetrendRegionCveRelatedResponsetrendRegionCveInboundRelatedResponsetrendRegionCveOutboundRelatedResponsetrendRegionIndustryRelatedResponsetrendRegionTargetedIndustriesRelatedResponsetrendRegionTargetingIndustriesRelatedResponsetrendRegionActorRelatedResponsetrendRegionActorsTargetingRelatedResponsetrendRegionActorsLocatedRelatedResponsetrendRegionRegionRelatedResponsetrendRegionRegionSourceRelatedResponsetrendRegionRegionTargetRelatedResponse**](AnyOftrendRegionMalwareRelatedResponsetrendRegionMalwareInboundRelatedResponsetrendRegionMalwareOutboundRelatedResponsetrendRegionCveRelatedResponsetrendRegionCveInboundRelatedResponsetrendRegionCveOutboundRelatedResponsetrendRegionIndustryRelatedResponsetrendRegionTargetedIndustriesRelatedResponsetrendRegionTargetingIndustriesRelatedResponsetrendRegionActorRelatedResponsetrendRegionActorsTargetingRelatedResponsetrendRegionActorsLocatedRelatedResponsetrendRegionRegionRelatedResponsetrendRegionRegionSourceRelatedResponsetrendRegionRegionTargetRelatedResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trending_actor**
> TrendActorResponse get_trending_actor(accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, confidence=confidence, metric_confidence=metric_confidence, name=name)

Top 10 trending actors by the timeline of recent activity

Returns top 10 trending actors by the timeline of recent activity.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
start_date = 'start_date_example' # str | Represents earliest date of actor’s activity time period. When only start date is given, it will give list of actors where start_date falls in the range of actor’s activity recorded. (optional)
end_date = 'end_date_example' # str | Represents most recent date of actor’s activity time period. When provided with start_date it would be exact match of start_date and end_date. (optional)
confidence = 'confidence_example' # str | Applies to confidence of the recent activity observed for an actor. (activity_observation.recent). (optional)
metric_confidence = 'metric_confidence_example' # str | Applies to all the associated object’s metrics confidence. It is used to filter actors by specified confidence level of the associated/related metrics data. (optional)
name = 'name_example' # str | To get actor name exactly matching by the given name. (optional)

    try:
        # Top 10 trending actors by the timeline of recent activity
        api_response = api_instance.get_trending_actor(accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, confidence=confidence, metric_confidence=metric_confidence, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_trending_actor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **start_date** | **str**| Represents earliest date of actor’s activity time period. When only start date is given, it will give list of actors where start_date falls in the range of actor’s activity recorded. | [optional] 
 **end_date** | **str**| Represents most recent date of actor’s activity time period. When provided with start_date it would be exact match of start_date and end_date. | [optional] 
 **confidence** | **str**| Applies to confidence of the recent activity observed for an actor. (activity_observation.recent). | [optional] 
 **metric_confidence** | **str**| Applies to all the associated object’s metrics confidence. It is used to filter actors by specified confidence level of the associated/related metrics data. | [optional] 
 **name** | **str**| To get actor name exactly matching by the given name. | [optional] 

### Return type

[**TrendActorResponse**](TrendActorResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trending_cve**
> CveTrendResponse get_trending_cve(accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, industry_sector=industry_sector)

Top 5 trending CVEs within given date range and optionally grouped by industry sector

Returns top 5 trending CVEs within given date range and optionally grouped by industry sector.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
start_date = 'start_date_example' # str | Starting date of the requested time window of trending stat of a collection type. (optional)
end_date = 'end_date_example' # str | End date of the requested time window of trending stat of a collection type. (optional)
industry_sector = 'industry_sector_example' # str | Specifies filtering criteria in terms of industry sector for trending stat of a collection type. (optional)

    try:
        # Top 5 trending CVEs within given date range and optionally grouped by industry sector
        api_response = api_instance.get_trending_cve(accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, industry_sector=industry_sector)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_trending_cve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **start_date** | **str**| Starting date of the requested time window of trending stat of a collection type. | [optional] 
 **end_date** | **str**| End date of the requested time window of trending stat of a collection type. | [optional] 
 **industry_sector** | **str**| Specifies filtering criteria in terms of industry sector for trending stat of a collection type. | [optional] 

### Return type

[**CveTrendResponse**](CveTrendResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trending_region**
> TrendRegionResponse get_trending_region(accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, name=name)

Top 10 trending regions

Returns top 10 trending regions

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
start_date = 'start_date_example' # str | Represents earliest date of region’s activity time period. When only start date is given, it will give list of regions where start_date falls in the range of region’s activity recorded. (optional)
end_date = 'end_date_example' # str | Represents most recent date of region’s activity time period. When provided with start_date it would be exact match of start_date and end_date. (optional)
name = 'name_example' # str | To get region name exactly matching by the given name. (optional)

    try:
        # Top 10 trending regions
        api_response = api_instance.get_trending_region(accept=accept, authorization=authorization, x_app_name=x_app_name, start_date=start_date, end_date=end_date, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_trending_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **start_date** | **str**| Represents earliest date of region’s activity time period. When only start date is given, it will give list of regions where start_date falls in the range of region’s activity recorded. | [optional] 
 **end_date** | **str**| Represents most recent date of region’s activity time period. When provided with start_date it would be exact match of start_date and end_date. | [optional] 
 **name** | **str**| To get region name exactly matching by the given name. | [optional] 

### Return type

[**TrendRegionResponse**](TrendRegionResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_yara_signature**
> AnyOfendpointsYaraResponseyaraSignatureCountResponse get_yara_signature(accept=accept, authorization=authorization, x_app_name=x_app_name, malware_id=malware_id, actor_id=actor_id, malware_name=malware_name, actor_name=actor_name, hash=hash, count=count, limit=limit)

List of all yara signatures present in our system.

Returns list of all the yara signatures present in the system.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    accept = 'application/json' # str | Specifies the format in which the client would like the response. (optional) (default to 'application/json')
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)
malware_id = 'malware_id_example' # str | Returns yara signature objects which are related with specified malware id. (optional)
actor_id = 'actor_id_example' # str | Returns yara signature objects which are related with specified actor id. (optional)
malware_name = 'malware_name_example' # str | Returns yara signature objects which are related with specified malware name. (optional)
actor_name = 'actor_name_example' # str | Returns yara signature objects which are related with specified actor name. (optional)
hash = 'hash_example' # str | Returns yara signature objects which are related with specified hash value. (optional)
count = 'count_example' # str | If count value is 'true' it will return count of yara signature objects which are related with object specified by the other query parameter. (optional)
limit = 'limit_example' # str | Limit parameter specifies the number of objects to be return in response. (optional)

    try:
        # List of all yara signatures present in our system.
        api_response = api_instance.get_yara_signature(accept=accept, authorization=authorization, x_app_name=x_app_name, malware_id=malware_id, actor_id=actor_id, malware_name=malware_name, actor_name=actor_name, hash=hash, count=count, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_yara_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] [default to &#39;application/json&#39;]
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 
 **malware_id** | **str**| Returns yara signature objects which are related with specified malware id. | [optional] 
 **actor_id** | **str**| Returns yara signature objects which are related with specified actor id. | [optional] 
 **malware_name** | **str**| Returns yara signature objects which are related with specified malware name. | [optional] 
 **actor_name** | **str**| Returns yara signature objects which are related with specified actor name. | [optional] 
 **hash** | **str**| Returns yara signature objects which are related with specified hash value. | [optional] 
 **count** | **str**| If count value is &#39;true&#39; it will return count of yara signature objects which are related with object specified by the other query parameter. | [optional] 
 **limit** | **str**| Limit parameter specifies the number of objects to be return in response. | [optional] 

### Return type

[**AnyOfendpointsYaraResponseyaraSignatureCountResponse**](AnyOfendpointsYaraResponseyaraSignatureCountResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_all_entities**
> AnyOfendpointsPostEntitiesResponseendpointsPostLocationEntitiesResponse post_all_entities(unknown_base_type, accept=accept, authorization=authorization, x_app_name=x_app_name)

Bulk look up of Entities.

### Example

* OAuth Authentication (OAuth2Security):
```python
from __future__ import print_function
import time
import fireeye.intel
from fireeye.intel.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.intelligence.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = fireeye.intel.Configuration(
    host = "http://api.intelligence.fireeye.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with fireeye.intel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.intel.DefaultApi(api_client)
    unknown_base_type = fireeye.intel.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 
accept = 'application/json, application/gzip' # str | Specifies the format in which the client would like the response. (optional)
authorization = 'authorization_example' # str | Access token to all the FireEye Intelligence API endpoints. (optional)
x_app_name = 'x_app_name_example' # str | The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be 'indicators.script.xyzcompany.v1.0' or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. (optional)

    try:
        # Bulk look up of Entities.
        api_response = api_instance.post_all_entities(unknown_base_type, accept=accept, authorization=authorization, x_app_name=x_app_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->post_all_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 
 **accept** | **str**| Specifies the format in which the client would like the response. | [optional] 
 **authorization** | **str**| Access token to all the FireEye Intelligence API endpoints. | [optional] 
 **x_app_name** | **str**| The FireEye Intel API uses the header variable X-App-Name for customers and partners to set a user-agent on all of their API calls. This mandatory field is typically a combination of the customer or partners organization name, its application name, and its version. A typical customer X-App-Name would be &#39;indicators.script.xyzcompany.v1.0&#39; or similar. The X-App-Name for customers should, at a minimum, have the calling organization name and, for partners, it is required to have the company product name and version of the integration for troubleshooting purposes. | [optional] 

### Return type

[**AnyOfendpointsPostEntitiesResponseendpointsPostLocationEntitiesResponse**](AnyOfendpointsPostEntitiesResponseendpointsPostLocationEntitiesResponse.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok - The request has succeeded. |  * Accept - Identifies the format of the response, e.g. application/json <br>  |
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**413** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

