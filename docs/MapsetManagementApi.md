# actinia_openapi_python_client.MapsetManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_get**](MapsetManagementApi.md#locations_location_name_mapsets_get) | **GET** /locations/{location_name}/mapsets | Get a list of all mapsets that are located in a specific location.
[**locations_location_name_mapsets_mapset_name_delete**](MapsetManagementApi.md#locations_location_name_mapsets_mapset_name_delete) | **DELETE** /locations/{location_name}/mapsets/{mapset_name} | Delete an existing mapset
[**locations_location_name_mapsets_mapset_name_info_get**](MapsetManagementApi.md#locations_location_name_mapsets_mapset_name_info_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/info | Get the current computational region of the mapset and the projection
[**locations_location_name_mapsets_mapset_name_lock_delete**](MapsetManagementApi.md#locations_location_name_mapsets_mapset_name_lock_delete) | **DELETE** /locations/{location_name}/mapsets/{mapset_name}/lock | Delete a location/mapset lock.
[**locations_location_name_mapsets_mapset_name_lock_get**](MapsetManagementApi.md#locations_location_name_mapsets_mapset_name_lock_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/lock | Get the location/mapset lock status.
[**locations_location_name_mapsets_mapset_name_lock_post**](MapsetManagementApi.md#locations_location_name_mapsets_mapset_name_lock_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/lock | Create a location/mapset lock.
[**locations_location_name_mapsets_mapset_name_post**](MapsetManagementApi.md#locations_location_name_mapsets_mapset_name_post) | **POST** /locations/{location_name}/mapsets/{mapset_name} | Create a new mapset in an existing location.


# **locations_location_name_mapsets_get**
> StringListProcessingResultResponseModel locations_location_name_mapsets_get(location_name)

Get a list of all mapsets that are located in a specific location.

Get a list of all mapsets that are located in a specific location. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.string_list_processing_result_response_model import StringListProcessingResultResponseModel
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
    api_instance = actinia_openapi_python_client.MapsetManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The name of the location (default to 'nc_spm_08')

    try:
        # Get a list of all mapsets that are located in a specific location.
        api_response = api_instance.locations_location_name_mapsets_get(location_name)
        print("The response of MapsetManagementApi->locations_location_name_mapsets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsetManagementApi->locations_location_name_mapsets_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | [default to &#39;nc_spm_08&#39;]

### Return type

[**StringListProcessingResultResponseModel**](StringListProcessingResultResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of mapset names and the log of the process chain that was used to create the response. |  -  |
**400** | The error message and a detailed log why listing of mapsets did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_delete**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_delete(location_name, mapset_name)

Delete an existing mapset

Delete an existing mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.MapsetManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset

    try:
        # Delete an existing mapset
        api_response = api_instance.locations_location_name_mapsets_mapset_name_delete(location_name, mapset_name)
        print("The response of MapsetManagementApi->locations_location_name_mapsets_mapset_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsetManagementApi->locations_location_name_mapsets_mapset_name_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 

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
**200** | Success message for mapset deletion |  -  |
**400** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_info_get**
> MapsetInfoResponseModel locations_location_name_mapsets_mapset_name_info_get(location_name, mapset_name)

Get the current computational region of the mapset and the projection

Get the current computational region of the mapset and the projection of the location as WKT string. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.mapset_info_response_model import MapsetInfoResponseModel
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
    api_instance = actinia_openapi_python_client.MapsetManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The name of the location (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset (default to 'PERMANENT')

    try:
        # Get the current computational region of the mapset and the projection
        api_response = api_instance.locations_location_name_mapsets_mapset_name_info_get(location_name, mapset_name)
        print("The response of MapsetManagementApi->locations_location_name_mapsets_mapset_name_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsetManagementApi->locations_location_name_mapsets_mapset_name_info_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset | [default to &#39;PERMANENT&#39;]

### Return type

[**MapsetInfoResponseModel**](MapsetInfoResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current computational region of the mapset and the projection of the location |  -  |
**400** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_lock_delete**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_lock_delete(location_name, mapset_name)

Delete a location/mapset lock.

Delete a location/mapset lock. A location/mapset lock can be deleted so that operation can be performed on it until it is locked. Minimum required user role: admin.

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
    api_instance = actinia_openapi_python_client.MapsetManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The name of the location (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset (default to 'PERMANENT')

    try:
        # Delete a location/mapset lock.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_lock_delete(location_name, mapset_name)
        print("The response of MapsetManagementApi->locations_location_name_mapsets_mapset_name_lock_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsetManagementApi->locations_location_name_mapsets_mapset_name_lock_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset | [default to &#39;PERMANENT&#39;]

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
**200** | Success message if the location/mapset was unlocked successfully |  -  |
**400** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_lock_get**
> MapsetLockManagementResponseModel locations_location_name_mapsets_mapset_name_lock_get(location_name, mapset_name)

Get the location/mapset lock status.

Get the location/mapset lock status. Minimum required user role: admin.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.mapset_lock_management_response_model import MapsetLockManagementResponseModel
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
    api_instance = actinia_openapi_python_client.MapsetManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The name of the location (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset (default to 'PERMANENT')

    try:
        # Get the location/mapset lock status.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_lock_get(location_name, mapset_name)
        print("The response of MapsetManagementApi->locations_location_name_mapsets_mapset_name_lock_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsetManagementApi->locations_location_name_mapsets_mapset_name_lock_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset | [default to &#39;PERMANENT&#39;]

### Return type

[**MapsetLockManagementResponseModel**](MapsetLockManagementResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the location/mapset lock status, either \&quot;True\&quot; or \&quot;None\&quot; |  -  |
**400** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_lock_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_lock_post(location_name, mapset_name)

Create a location/mapset lock.

Create a location/mapset lock. A location/mapset lock can be created so that no operation can be performed on it until it is unlocked. Minimum required user role: admin.

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
    api_instance = actinia_openapi_python_client.MapsetManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The name of the location (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset (default to 'PERMANENT')

    try:
        # Create a location/mapset lock.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_lock_post(location_name, mapset_name)
        print("The response of MapsetManagementApi->locations_location_name_mapsets_mapset_name_lock_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsetManagementApi->locations_location_name_mapsets_mapset_name_lock_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset | [default to &#39;PERMANENT&#39;]

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
**200** | Success message if the location/mapset was locked successfully |  -  |
**400** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_post(location_name, mapset_name)

Create a new mapset in an existing location.

Create a new mapset in an existing location. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.MapsetManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset

    try:
        # Create a new mapset in an existing location.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_post(location_name, mapset_name)
        print("The response of MapsetManagementApi->locations_location_name_mapsets_mapset_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsetManagementApi->locations_location_name_mapsets_mapset_name_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 

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
**200** | Success message for mapset creation |  -  |
**400** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

