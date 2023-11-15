# actinia_openapi_python_client.TilingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_tiling_processes_get**](TilingApi.md#locations_location_name_mapsets_mapset_name_tiling_processes_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/tiling_processes | Returns a list of all tiling prcesses
[**locations_location_name_mapsets_mapset_name_tiling_processes_grid_get**](TilingApi.md#locations_location_name_mapsets_mapset_name_tiling_processes_grid_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/tiling_processes/grid | Get description of the grid tiling process.
[**locations_location_name_mapsets_mapset_name_tiling_processes_grid_post**](TilingApi.md#locations_location_name_mapsets_mapset_name_tiling_processes_grid_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/tiling_processes/grid | Create grid tiles.


# **locations_location_name_mapsets_mapset_name_tiling_processes_get**
> TilingListResponseModel locations_location_name_mapsets_mapset_name_tiling_processes_get(location_name, mapset_name)

Returns a list of all tiling prcesses

Returns The list of the tiling processes.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.tiling_list_response_model import TilingListResponseModel
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
    api_instance = actinia_openapi_python_client.TilingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the target mapset

    try:
        # Returns a list of all tiling prcesses
        api_response = api_instance.locations_location_name_mapsets_mapset_name_tiling_processes_get(location_name, mapset_name)
        print("The response of TilingApi->locations_location_name_mapsets_mapset_name_tiling_processes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TilingApi->locations_location_name_mapsets_mapset_name_tiling_processes_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the target mapset | 

### Return type

[**TilingListResponseModel**](TilingListResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns list of the tiling processes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_tiling_processes_grid_get**
> SimpleStatusCodeResponseModel locations_location_name_mapsets_mapset_name_tiling_processes_grid_get(location_name, mapset_name)

Get description of the grid tiling process.

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
    api_instance = actinia_openapi_python_client.TilingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the target mapset

    try:
        # Get description of the grid tiling process.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_tiling_processes_grid_get(location_name, mapset_name)
        print("The response of TilingApi->locations_location_name_mapsets_mapset_name_tiling_processes_grid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TilingApi->locations_location_name_mapsets_mapset_name_tiling_processes_grid_get: %s\n" % e)
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

# **locations_location_name_mapsets_mapset_name_tiling_processes_grid_post**
> GridTilingResponseModel locations_location_name_mapsets_mapset_name_tiling_processes_grid_post(location_name, mapset_name, grid_prefix)

Create grid tiles.

Creates grid tiles with a specified 'width' and 'height' in the current computational region. The created grids have the given 'grid_prefix' and will be listed in the 'process_results'. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.grid_tiling_response_model import GridTilingResponseModel
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
    api_instance = actinia_openapi_python_client.TilingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the target mapset
    grid_prefix = 'grid_prefix_example' # str | The prefix of the grid tiles.

    try:
        # Create grid tiles.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_tiling_processes_grid_post(location_name, mapset_name, grid_prefix)
        print("The response of TilingApi->locations_location_name_mapsets_mapset_name_tiling_processes_grid_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TilingApi->locations_location_name_mapsets_mapset_name_tiling_processes_grid_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the target mapset | 
 **grid_prefix** | **str**| The prefix of the grid tiles. | 

### Return type

[**GridTilingResponseModel**](GridTilingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns the processing response with the grid tile names in the &#39;processing_results&#39;. |  -  |
**400** | This response returns a detail error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

