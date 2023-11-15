# actinia_openapi_python_client.ProcessChainMonitoringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_user_id_resource_id_mapsetsizes_diffs_get**](ProcessChainMonitoringApi.md#resources_user_id_resource_id_mapsetsizes_diffs_get) | **GET** /resources/{user_id}/{resource_id}/mapsetsizes/diffs | Get the step-by-step mapset size differences of a resource.
[**resources_user_id_resource_id_mapsetsizes_diffs_render_get**](ProcessChainMonitoringApi.md#resources_user_id_resource_id_mapsetsizes_diffs_render_get) | **GET** /resources/{user_id}/{resource_id}/mapsetsizes/diffs/render | Render the step-by-step mapset size differences of a resource.
[**resources_user_id_resource_id_mapsetsizes_get**](ProcessChainMonitoringApi.md#resources_user_id_resource_id_mapsetsizes_get) | **GET** /resources/{user_id}/{resource_id}/mapsetsizes | Get the sizes of mapset of a resource.
[**resources_user_id_resource_id_mapsetsizes_max_get**](ProcessChainMonitoringApi.md#resources_user_id_resource_id_mapsetsizes_max_get) | **GET** /resources/{user_id}/{resource_id}/mapsetsizes/max | Get the maximum size of mapset of a resource.
[**resources_user_id_resource_id_mapsetsizes_render_get**](ProcessChainMonitoringApi.md#resources_user_id_resource_id_mapsetsizes_render_get) | **GET** /resources/{user_id}/{resource_id}/mapsetsizes/render | Render the mapset sizes of a resource.


# **resources_user_id_resource_id_mapsetsizes_diffs_get**
> MapsetSizeResponseModel resources_user_id_resource_id_mapsetsizes_diffs_get(user_id, resource_id)

Get the step-by-step mapset size differences of a resource.

Get the step-by-step mapset size differences of a resource. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.mapset_size_response_model import MapsetSizeResponseModel
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
    api_instance = actinia_openapi_python_client.ProcessChainMonitoringApi(api_client)
    user_id = 'user_id_example' # str | The unique user name/id
    resource_id = 'resource_id_example' # str | The id of the resource

    try:
        # Get the step-by-step mapset size differences of a resource.
        api_response = api_instance.resources_user_id_resource_id_mapsetsizes_diffs_get(user_id, resource_id)
        print("The response of ProcessChainMonitoringApi->resources_user_id_resource_id_mapsetsizes_diffs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessChainMonitoringApi->resources_user_id_resource_id_mapsetsizes_diffs_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique user name/id | 
 **resource_id** | **str**| The id of the resource | 

### Return type

[**MapsetSizeResponseModel**](MapsetSizeResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current state of the resource |  -  |
**400** | The error message if the resource does not exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_user_id_resource_id_mapsetsizes_diffs_render_get**
> resources_user_id_resource_id_mapsetsizes_diffs_render_get(user_id, resource_id)

Render the step-by-step mapset size differences of a resource.

Render the step-by-step mapset size differences of a resource. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
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
    api_instance = actinia_openapi_python_client.ProcessChainMonitoringApi(api_client)
    user_id = 'user_id_example' # str | The unique user name/id
    resource_id = 'resource_id_example' # str | The id of the resource

    try:
        # Render the step-by-step mapset size differences of a resource.
        api_instance.resources_user_id_resource_id_mapsetsizes_diffs_render_get(user_id, resource_id)
    except Exception as e:
        print("Exception when calling ProcessChainMonitoringApi->resources_user_id_resource_id_mapsetsizes_diffs_render_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique user name/id | 
 **resource_id** | **str**| The id of the resource | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PNG image |  -  |
**400** | The error message and a detailed log why rendering did not succeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_user_id_resource_id_mapsetsizes_get**
> MapsetSizeResponseModel resources_user_id_resource_id_mapsetsizes_get(user_id, resource_id)

Get the sizes of mapset of a resource.

Get the mapset sizes of a resource. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.mapset_size_response_model import MapsetSizeResponseModel
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
    api_instance = actinia_openapi_python_client.ProcessChainMonitoringApi(api_client)
    user_id = 'user_id_example' # str | The unique user name/id
    resource_id = 'resource_id_example' # str | The id of the resource

    try:
        # Get the sizes of mapset of a resource.
        api_response = api_instance.resources_user_id_resource_id_mapsetsizes_get(user_id, resource_id)
        print("The response of ProcessChainMonitoringApi->resources_user_id_resource_id_mapsetsizes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessChainMonitoringApi->resources_user_id_resource_id_mapsetsizes_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique user name/id | 
 **resource_id** | **str**| The id of the resource | 

### Return type

[**MapsetSizeResponseModel**](MapsetSizeResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current state of the resource |  -  |
**400** | The error message if the resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_user_id_resource_id_mapsetsizes_max_get**
> MaxMapsetSizeResponseModel resources_user_id_resource_id_mapsetsizes_max_get(user_id, resource_id)

Get the maximum size of mapset of a resource.

Get the maximum mapset size of a resource. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.max_mapset_size_response_model import MaxMapsetSizeResponseModel
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
    api_instance = actinia_openapi_python_client.ProcessChainMonitoringApi(api_client)
    user_id = 'user_id_example' # str | The unique user name/id
    resource_id = 'resource_id_example' # str | The id of the resource

    try:
        # Get the maximum size of mapset of a resource.
        api_response = api_instance.resources_user_id_resource_id_mapsetsizes_max_get(user_id, resource_id)
        print("The response of ProcessChainMonitoringApi->resources_user_id_resource_id_mapsetsizes_max_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessChainMonitoringApi->resources_user_id_resource_id_mapsetsizes_max_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique user name/id | 
 **resource_id** | **str**| The id of the resource | 

### Return type

[**MaxMapsetSizeResponseModel**](MaxMapsetSizeResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current state of the resource |  -  |
**400** | The error message if the resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_user_id_resource_id_mapsetsizes_render_get**
> resources_user_id_resource_id_mapsetsizes_render_get(user_id, resource_id)

Render the mapset sizes of a resource.

Render the mapset sizes of a resource. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
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
    api_instance = actinia_openapi_python_client.ProcessChainMonitoringApi(api_client)
    user_id = 'user_id_example' # str | The unique user name/id
    resource_id = 'resource_id_example' # str | The id of the resource

    try:
        # Render the mapset sizes of a resource.
        api_instance.resources_user_id_resource_id_mapsetsizes_render_get(user_id, resource_id)
    except Exception as e:
        print("Exception when calling ProcessChainMonitoringApi->resources_user_id_resource_id_mapsetsizes_render_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique user name/id | 
 **resource_id** | **str**| The id of the resource | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PNG image |  -  |
**400** | The error message and a detailed log why rendering did not succeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

