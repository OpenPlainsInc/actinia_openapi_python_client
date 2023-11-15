# actinia_openapi_python_client.MergeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_merge_processes_get**](MergeApi.md#locations_location_name_mapsets_mapset_name_merge_processes_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/merge_processes | Returns a list of all merge processes
[**locations_location_name_mapsets_mapset_name_merge_processes_patch_get**](MergeApi.md#locations_location_name_mapsets_mapset_name_merge_processes_patch_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/merge_processes/patch | Get description of the patch merge process.
[**locations_location_name_mapsets_mapset_name_merge_processes_patch_post**](MergeApi.md#locations_location_name_mapsets_mapset_name_merge_processes_patch_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/merge_processes/patch | Merging mapsets with same raster, vector, ... maps in one mapset by


# **locations_location_name_mapsets_mapset_name_merge_processes_get**
> MergeListResponseModel locations_location_name_mapsets_mapset_name_merge_processes_get(location_name, mapset_name)

Returns a list of all merge processes

Returns The list of the merge processes.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.merge_list_response_model import MergeListResponseModel
from actinia_openapi_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = actinia_openapi_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = actinia_openapi_python_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with actinia_openapi_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = actinia_openapi_python_client.MergeApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required space-time raster dataset

    try:
        # Returns a list of all merge processes
        api_response = api_instance.locations_location_name_mapsets_mapset_name_merge_processes_get(location_name, mapset_name)
        print("The response of MergeApi->locations_location_name_mapsets_mapset_name_merge_processes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergeApi->locations_location_name_mapsets_mapset_name_merge_processes_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required space-time raster dataset | 

### Return type

[**MergeListResponseModel**](MergeListResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns list of the merge processes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_merge_processes_patch_get**
> SimpleStatusCodeResponseModel locations_location_name_mapsets_mapset_name_merge_processes_patch_get(location_name, mapset_name)

Get description of the patch merge process.

Returns only the API description of the POST endpoint.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.simple_status_code_response_model import SimpleStatusCodeResponseModel
from actinia_openapi_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = actinia_openapi_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = actinia_openapi_python_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with actinia_openapi_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = actinia_openapi_python_client.MergeApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the target mapset

    try:
        # Get description of the patch merge process.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_merge_processes_patch_get(location_name, mapset_name)
        print("The response of MergeApi->locations_location_name_mapsets_mapset_name_merge_processes_patch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergeApi->locations_location_name_mapsets_mapset_name_merge_processes_patch_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the target mapset | 

### Return type

[**SimpleStatusCodeResponseModel**](SimpleStatusCodeResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns the API description of the POST endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_merge_processes_patch_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_merge_processes_patch_post(location_name, mapset_name, keep_mapsets=keep_mapsets)

Merging mapsets with same raster, vector, ... maps in one mapset by

Merge raster, vector and STRDS data from different mapsets defined in a 'mapsetlist' by patching them in the new/target mapset. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.processing_response_model import ProcessingResponseModel
from actinia_openapi_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = actinia_openapi_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = actinia_openapi_python_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with actinia_openapi_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = actinia_openapi_python_client.MergeApi(api_client)
    location_name = 'location_name_example' # str | The location name of the mapsets
    mapset_name = 'mapset_name_example' # str | The name of the target mapset
    keep_mapsets = True # bool | A boolean if it is set to 'true' then the merged mapsets will not be deleted. The default falue is 'false', so the merged mapset will be deleted. (optional)

    try:
        # Merging mapsets with same raster, vector, ... maps in one mapset by
        api_response = api_instance.locations_location_name_mapsets_mapset_name_merge_processes_patch_post(location_name, mapset_name, keep_mapsets=keep_mapsets)
        print("The response of MergeApi->locations_location_name_mapsets_mapset_name_merge_processes_patch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergeApi->locations_location_name_mapsets_mapset_name_merge_processes_patch_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name of the mapsets | 
 **mapset_name** | **str**| The name of the target mapset | 
 **keep_mapsets** | **bool**| A boolean if it is set to &#39;true&#39; then the merged mapsets will not be deleted. The default falue is &#39;false&#39;, so the merged mapset will be deleted. | [optional] 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns the processing response. |  -  |
**400** | This response returns a detail error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

