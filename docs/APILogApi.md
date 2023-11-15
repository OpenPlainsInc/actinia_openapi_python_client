# actinia_openapi_python_client.APILogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_log_user_id_get**](APILogApi.md#api_log_user_id_get) | **GET** /api_log/{user_id} | Get a list of all API calls that have been called by the provided user.


# **api_log_user_id_get**
> ApiLogListModel api_log_user_id_get(user_id)

Get a list of all API calls that have been called by the provided user.

Get a list of all API calls that have been called by the provided user. Admin and superadmin roles can list API calls from any user. A user role can only list API calls from itself. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.api_log_list_model import ApiLogListModel
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
    api_instance = actinia_openapi_python_client.APILogApi(api_client)
    user_id = 'user_id_example' # str | The unique user name/id

    try:
        # Get a list of all API calls that have been called by the provided user.
        api_response = api_instance.api_log_user_id_get(user_id)
        print("The response of APILogApi->api_log_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APILogApi->api_log_user_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique user name/id | 

### Return type

[**ApiLogListModel**](ApiLogListModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned a list of all API calls that have been called by the provided user. |  -  |
**400** | The error message why API log gathering did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

