# actinia_openapi_python_client.ResourceIterationManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_user_id_resource_id_iteration_get**](ResourceIterationManagementApi.md#resources_user_id_resource_id_iteration_get) | **GET** /resources/{user_id}/{resource_id}/{iteration} | Get the status of a resource of a given iteration.


# **resources_user_id_resource_id_iteration_get**
> ProcessingResponseModel resources_user_id_resource_id_iteration_get(user_id, resource_id, iteration)

Get the status of a resource of a given iteration.

Get the status of a resource with the iterations. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.ResourceIterationManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique user name/id
    resource_id = 'resource_id_example' # str | The id of the resource
    iteration = 56 # int | The id of the resource

    try:
        # Get the status of a resource of a given iteration.
        api_response = api_instance.resources_user_id_resource_id_iteration_get(user_id, resource_id, iteration)
        print("The response of ResourceIterationManagementApi->resources_user_id_resource_id_iteration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceIterationManagementApi->resources_user_id_resource_id_iteration_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique user name/id | 
 **resource_id** | **str**| The id of the resource | 
 **iteration** | **int**| The id of the resource | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

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

