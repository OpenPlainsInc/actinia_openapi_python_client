# actinia_openapi_python_client.AuthenticationManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_get**](AuthenticationManagementApi.md#api_key_get) | **GET** /api_key | Create an API key for permanent authentication.
[**token_get**](AuthenticationManagementApi.md#token_get) | **GET** /token | Create an authentication token.


# **api_key_get**
> TokenResponseModel api_key_get()

Create an API key for permanent authentication.

Create an API key for permanent authentication. API keys have no expiration time. Minimum required user role: admin.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.token_response_model import TokenResponseModel
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
    api_instance = actinia_openapi_python_client.AuthenticationManagementApi(api_client)

    try:
        # Create an API key for permanent authentication.
        api_response = api_instance.api_key_get()
        print("The response of AuthenticationManagementApi->api_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationManagementApi->api_key_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenResponseModel**](TokenResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API key generation response |  -  |
**400** | The error message in case of failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_get**
> TokenResponseModel token_get(expiration_time=expiration_time)

Create an authentication token.

Create an authentication token. Tokens have an expiration time. The default expiration time is one day (86400s). maximum length is 365 days. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.token_response_model import TokenResponseModel
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
    api_instance = actinia_openapi_python_client.AuthenticationManagementApi(api_client)
    expiration_time = 86400 # int | The expiration time in seconds for the generated token. (optional) (default to 86400)

    try:
        # Create an authentication token.
        api_response = api_instance.token_get(expiration_time=expiration_time)
        print("The response of AuthenticationManagementApi->token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationManagementApi->token_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expiration_time** | **int**| The expiration time in seconds for the generated token. | [optional] [default to 86400]

### Return type

[**TokenResponseModel**](TokenResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token generation response |  -  |
**400** | The error message in case of failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

