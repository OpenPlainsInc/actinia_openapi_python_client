# actinia_openapi_python_client.ProcessChainTemplateManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actinia_templates_get**](ProcessChainTemplateManagementApi.md#actinia_templates_get) | **GET** /actinia_templates | Get a list of all actinia templates (process chain templates).
[**actinia_templates_post**](ProcessChainTemplateManagementApi.md#actinia_templates_post) | **POST** /actinia_templates | Create an actinia template (process chain template).
[**actinia_templates_template_id_delete**](ProcessChainTemplateManagementApi.md#actinia_templates_template_id_delete) | **DELETE** /actinia_templates/{template_id} | Delete an actinia template (process chain template).
[**actinia_templates_template_id_get**](ProcessChainTemplateManagementApi.md#actinia_templates_template_id_get) | **GET** /actinia_templates/{template_id} | Read an actinia template (process chain template).
[**actinia_templates_template_id_put**](ProcessChainTemplateManagementApi.md#actinia_templates_template_id_put) | **PUT** /actinia_templates/{template_id} | Update an actinia template (process chain template).


# **actinia_templates_get**
> actinia_templates_get()

Get a list of all actinia templates (process chain templates).

Get a list of process chain templates. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.ProcessChainTemplateManagementApi(api_client)

    try:
        # Get a list of all actinia templates (process chain templates).
        api_instance.actinia_templates_get()
    except Exception as e:
        print("Exception when calling ProcessChainTemplateManagementApi->actinia_templates_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of module names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actinia_templates_post**
> actinia_templates_post(template)

Create an actinia template (process chain template).

Create a process chain template. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_template import ProcessChainTemplate
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
    api_instance = actinia_openapi_python_client.ProcessChainTemplateManagementApi(api_client)
    template = actinia_openapi_python_client.ProcessChainTemplate() # ProcessChainTemplate | The process chain template

    try:
        # Create an actinia template (process chain template).
        api_instance.actinia_templates_post(template)
    except Exception as e:
        print("Exception when calling ProcessChainTemplateManagementApi->actinia_templates_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**ProcessChainTemplate**](ProcessChainTemplate.md)| The process chain template | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/gml+xml, application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | This response returns True if creation was successfull. |  -  |
**404** | The error message and a detailed log why creation did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actinia_templates_template_id_delete**
> actinia_templates_template_id_delete(template_id)

Delete an actinia template (process chain template).

Delete a process chain template. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.ProcessChainTemplateManagementApi(api_client)
    template_id = 'template_id_example' # str | The name of a process chain template

    try:
        # Delete an actinia template (process chain template).
        api_instance.actinia_templates_template_id_delete(template_id)
    except Exception as e:
        print("Exception when calling ProcessChainTemplateManagementApi->actinia_templates_template_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The name of a process chain template | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns True if deletion was successfull. |  -  |
**404** | The error message and a detailed log why deletion did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actinia_templates_template_id_get**
> ProcessChainTemplate actinia_templates_template_id_get(template_id)

Read an actinia template (process chain template).

Read a process chain template. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_template import ProcessChainTemplate
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
    api_instance = actinia_openapi_python_client.ProcessChainTemplateManagementApi(api_client)
    template_id = 'template_id_example' # str | The name of a process chain template

    try:
        # Read an actinia template (process chain template).
        api_response = api_instance.actinia_templates_template_id_get(template_id)
        print("The response of ProcessChainTemplateManagementApi->actinia_templates_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessChainTemplateManagementApi->actinia_templates_template_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The name of a process chain template | 

### Return type

[**ProcessChainTemplate**](ProcessChainTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a process chain template. |  -  |
**404** | The error message and a detailed log why describing did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actinia_templates_template_id_put**
> actinia_templates_template_id_put(template_id)

Update an actinia template (process chain template).

Update a process chain template. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.ProcessChainTemplateManagementApi(api_client)
    template_id = 'template_id_example' # str | The name of a process chain template

    try:
        # Update an actinia template (process chain template).
        api_instance.actinia_templates_template_id_put(template_id)
    except Exception as e:
        print("Exception when calling ProcessChainTemplateManagementApi->actinia_templates_template_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The name of a process chain template | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | This response returns True if update was successfull. |  -  |
**404** | The error message and a detailed log why update did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

