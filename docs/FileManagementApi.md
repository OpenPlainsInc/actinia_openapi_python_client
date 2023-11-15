# actinia_openapi_python_client.FileManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_post**](FileManagementApi.md#files_post) | **POST** /files | Upload file.


# **files_post**
> SimpleStatusCodeResponseModel files_post()

Upload file.

File can be uploaded, best used with https://bmvimetadaten.mundialis.de.

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
    api_instance = actinia_openapi_python_client.FileManagementApi(api_client)

    try:
        # Upload file.
        api_response = api_instance.files_post()
        print("The response of FileManagementApi->files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileManagementApi->files_post: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**200** | Success or failure of connection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

