# actinia_openapi_python_client.CacheManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_cache_delete**](CacheManagementApi.md#download_cache_delete) | **DELETE** /download_cache | Clean the download cache and remove all cached data
[**download_cache_get**](CacheManagementApi.md#download_cache_get) | **GET** /download_cache | Get the current size of the download cache


# **download_cache_delete**
> StorageResponseModel download_cache_delete()

Clean the download cache and remove all cached data

Clean the download cache and remove all cached data. Minimum required user role: admin.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.storage_response_model import StorageResponseModel
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
    api_instance = actinia_openapi_python_client.CacheManagementApi(api_client)

    try:
        # Clean the download cache and remove all cached data
        api_response = api_instance.download_cache_delete()
        print("The response of CacheManagementApi->download_cache_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheManagementApi->download_cache_delete: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageResponseModel**](StorageResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Processing status of cache deletion |  -  |
**400** | The error message why cache cleaning did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_cache_get**
> StorageResponseModel download_cache_get()

Get the current size of the download cache

Get the current size of the download cache. Minimum required user role: admin.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.storage_response_model import StorageResponseModel
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
    api_instance = actinia_openapi_python_client.CacheManagementApi(api_client)

    try:
        # Get the current size of the download cache
        api_response = api_instance.download_cache_get()
        print("The response of CacheManagementApi->download_cache_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheManagementApi->download_cache_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageResponseModel**](StorageResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current state of the download cache |  -  |
**400** | The error message why cache information gathering did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

