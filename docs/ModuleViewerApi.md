# actinia_openapi_python_client.ModuleViewerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actinia_modules_actiniamodule_get**](ModuleViewerApi.md#actinia_modules_actiniamodule_get) | **GET** /actinia_modules/{actiniamodule} | Describe an actinia module (process chain template).
[**actinia_modules_get**](ModuleViewerApi.md#actinia_modules_get) | **GET** /actinia_modules | Get a list of all actinia modules (process chain templates).
[**grass_modules_get**](ModuleViewerApi.md#grass_modules_get) | **GET** /grass_modules | Get a list of all GRASS GIS modules.
[**grass_modules_grassmodule_get**](ModuleViewerApi.md#grass_modules_grassmodule_get) | **GET** /grass_modules/{grassmodule} | Describe a GRASS GIS module.
[**modules_get**](ModuleViewerApi.md#modules_get) | **GET** /modules | Get a list of all modules.
[**modules_module_get**](ModuleViewerApi.md#modules_module_get) | **GET** /modules/{module} | Describe a module.


# **actinia_modules_actiniamodule_get**
> Module actinia_modules_actiniamodule_get(actiniamodule)

Describe an actinia module (process chain template).

Get the description of a module. Minimum required user role: user.Can be also used to reload cache for a certain modulefor the full module description in listModules.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.module import Module
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
    api_instance = actinia_openapi_python_client.ModuleViewerApi(api_client)
    actiniamodule = 'actiniamodule_example' # str | The name of a module

    try:
        # Describe an actinia module (process chain template).
        api_response = api_instance.actinia_modules_actiniamodule_get(actiniamodule)
        print("The response of ModuleViewerApi->actinia_modules_actiniamodule_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleViewerApi->actinia_modules_actiniamodule_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actiniamodule** | **str**| The name of a module | 

### Return type

[**Module**](Module.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a description of a module. |  -  |
**400** | The error message and a detailed log why describing modules did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actinia_modules_get**
> ModuleList actinia_modules_get(tag=tag, category=category, family=family, record=record)

Get a list of all actinia modules (process chain templates).

Get a list of modules. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.module_list import ModuleList
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
    api_instance = actinia_openapi_python_client.ModuleViewerApi(api_client)
    tag = 'tag_example' # str | Filter for categories (optional)
    category = 'category_example' # str | Another filter for categories (optional)
    family = 'family_example' # str | Type of GRASS GIS module (optional)
    record = 'record_example' # str | If set to 'full', all information about the returned modules are given like in the single module description. Depending on active cache, this response might run into a timeout. A filter can prevent this. (optional)

    try:
        # Get a list of all actinia modules (process chain templates).
        api_response = api_instance.actinia_modules_get(tag=tag, category=category, family=family, record=record)
        print("The response of ModuleViewerApi->actinia_modules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleViewerApi->actinia_modules_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Filter for categories | [optional] 
 **category** | **str**| Another filter for categories | [optional] 
 **family** | **str**| Type of GRASS GIS module | [optional] 
 **record** | **str**| If set to &#39;full&#39;, all information about the returned modules are given like in the single module description. Depending on active cache, this response might run into a timeout. A filter can prevent this. | [optional] 

### Return type

[**ModuleList**](ModuleList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of module names and the status. |  -  |
**400** | The error message and a detailed log why listing of modules did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grass_modules_get**
> ModuleList grass_modules_get(tag=tag, category=category, family=family, record=record)

Get a list of all GRASS GIS modules.

Get a list of modules. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.module_list import ModuleList
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
    api_instance = actinia_openapi_python_client.ModuleViewerApi(api_client)
    tag = 'tag_example' # str | Filter for categories (optional)
    category = 'category_example' # str | Another filter for categories (optional)
    family = 'family_example' # str | Type of GRASS GIS module (optional)
    record = 'record_example' # str | If set to 'full', all information about the returned modules are given like in the single module description. Depending on active cache, this response might run into a timeout. A filter can prevent this. (optional)

    try:
        # Get a list of all GRASS GIS modules.
        api_response = api_instance.grass_modules_get(tag=tag, category=category, family=family, record=record)
        print("The response of ModuleViewerApi->grass_modules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleViewerApi->grass_modules_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Filter for categories | [optional] 
 **category** | **str**| Another filter for categories | [optional] 
 **family** | **str**| Type of GRASS GIS module | [optional] 
 **record** | **str**| If set to &#39;full&#39;, all information about the returned modules are given like in the single module description. Depending on active cache, this response might run into a timeout. A filter can prevent this. | [optional] 

### Return type

[**ModuleList**](ModuleList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of module names and the status. |  -  |
**400** | The error message and a detailed log why listing of modules did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grass_modules_grassmodule_get**
> Module grass_modules_grassmodule_get(grassmodule)

Describe a GRASS GIS module.

Get the description of a module. Minimum required user role: user.Can be also used to reload cache for a certain modulefor the full module description in listModules.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.module import Module
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
    api_instance = actinia_openapi_python_client.ModuleViewerApi(api_client)
    grassmodule = 'grassmodule_example' # str | The name of a module

    try:
        # Describe a GRASS GIS module.
        api_response = api_instance.grass_modules_grassmodule_get(grassmodule)
        print("The response of ModuleViewerApi->grass_modules_grassmodule_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleViewerApi->grass_modules_grassmodule_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grassmodule** | **str**| The name of a module | 

### Return type

[**Module**](Module.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a description of a module. |  -  |
**400** | The error message and a detailed log why describing modules did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modules_get**
> ModuleList modules_get(tag=tag, category=category, family=family, record=record)

Get a list of all modules.

Get a list of modules. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.module_list import ModuleList
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
    api_instance = actinia_openapi_python_client.ModuleViewerApi(api_client)
    tag = 'tag_example' # str | Filter for categories (optional)
    category = 'category_example' # str | Another filter for categories (optional)
    family = 'family_example' # str | Type of GRASS GIS module (optional)
    record = 'record_example' # str | If set to 'full', all information about the returned modules are given like in the single module description. Depending on active cache, this response might run into a timeout. A filter can prevent this. (optional)

    try:
        # Get a list of all modules.
        api_response = api_instance.modules_get(tag=tag, category=category, family=family, record=record)
        print("The response of ModuleViewerApi->modules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleViewerApi->modules_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Filter for categories | [optional] 
 **category** | **str**| Another filter for categories | [optional] 
 **family** | **str**| Type of GRASS GIS module | [optional] 
 **record** | **str**| If set to &#39;full&#39;, all information about the returned modules are given like in the single module description. Depending on active cache, this response might run into a timeout. A filter can prevent this. | [optional] 

### Return type

[**ModuleList**](ModuleList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of module names and the status. |  -  |
**400** | The error message and a detailed log why listing of modules did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modules_module_get**
> Module modules_module_get(module)

Describe a module.

Get the description of a module. Minimum required user role: user.Can be also used to reload cache for a certain modulefor the full module description in listModules.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.module import Module
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
    api_instance = actinia_openapi_python_client.ModuleViewerApi(api_client)
    module = 'module_example' # str | The name of a module

    try:
        # Describe a module.
        api_response = api_instance.modules_module_get(module)
        print("The response of ModuleViewerApi->modules_module_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleViewerApi->modules_module_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module** | **str**| The name of a module | 

### Return type

[**Module**](Module.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a description of a module. |  -  |
**400** | The error message and a detailed log why describing modules did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

