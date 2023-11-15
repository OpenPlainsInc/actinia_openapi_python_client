# actinia_openapi_python_client.MapsetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsets_get**](MapsetsApi.md#mapsets_get) | **GET** /mapsets | 


# **mapsets_get**
> LockedMapsetListResponseModel mapsets_get(mapsets=mapsets, status=status, user=user)



List available or locked mapsets.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.locked_mapset_list_response_model import LockedMapsetListResponseModel
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
    api_instance = actinia_openapi_python_client.MapsetsApi(api_client)
    mapsets = 'mapsets_example' # str | List all mapsets in the global database available to the authenticated user. (optional)
    status = 'status_example' # str | If set to 'locked', list all locked mapsets across all locations. Minimum required user role: admin. (optional)
    user = 'user_example' # str | List all mapsets in the global database available to the specified user. Minimum required user role: admin (optional)

    try:
        api_response = api_instance.mapsets_get(mapsets=mapsets, status=status, user=user)
        print("The response of MapsetsApi->mapsets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsetsApi->mapsets_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapsets** | **str**| List all mapsets in the global database available to the authenticated user. | [optional] 
 **status** | **str**| If set to &#39;locked&#39;, list all locked mapsets across all locations. Minimum required user role: admin. | [optional] 
 **user** | **str**| List all mapsets in the global database available to the specified user. Minimum required user role: admin | [optional] 

### Return type

[**LockedMapsetListResponseModel**](LockedMapsetListResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of available (or locked) mapsets  |  -  |
**500** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

