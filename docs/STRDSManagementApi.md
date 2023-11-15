# actinia_openapi_python_client.STRDSManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_strds_get**](STRDSManagementApi.md#locations_location_name_mapsets_mapset_name_strds_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/strds | Get a list of all STRDS that are located in a specific location/mapset.
[**locations_location_name_mapsets_mapset_name_strds_strds_name_delete**](STRDSManagementApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_delete) | **DELETE** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name} | Delete a STRDS that is located in a specific location/mapset.
[**locations_location_name_mapsets_mapset_name_strds_strds_name_get**](STRDSManagementApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name} | Get information about a STRDS that is located in a specific
[**locations_location_name_mapsets_mapset_name_strds_strds_name_post**](STRDSManagementApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name} | Create a new STRDS in a specific location/mapset.
[**locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete**](STRDSManagementApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete) | **DELETE** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/raster_layers | Unregister raster map layers from a STRDS located in a specific
[**locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get**](STRDSManagementApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/raster_layers | Get a list of all raster map layers that are registered in a STRDS
[**locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put**](STRDSManagementApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put) | **PUT** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/raster_layers | Register raster map layers in a STRDS located in a specific
[**locations_location_name_mapsets_mapset_name_strds_strds_name_render_get**](STRDSManagementApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_render_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/render | Render the raster map layers of a specific STRDS as a single image.


# **locations_location_name_mapsets_mapset_name_strds_get**
> StringListProcessingResultResponseModel locations_location_name_mapsets_mapset_name_strds_get(location_name, mapset_name, where=where)

Get a list of all STRDS that are located in a specific location/mapset.

Get a list of all STRDS that are located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STRDSManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset
    where = 'where_example' # str | A where statement to select user specific STRDS (optional)

    try:
        # Get a list of all STRDS that are located in a specific location/mapset.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_get(location_name, mapset_name, where=where)
        print("The response of STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 
 **where** | **str**| A where statement to select user specific STRDS | [optional] 

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
**200** | This response returns a list of STRDS names and timestamps and the log of the process chain that was used to create the response. |  -  |
**400** | The error message and a detailed log why listing of STRDS did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_delete**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_delete(location_name, mapset_name, strds_name, recursive=recursive)

Delete a STRDS that is located in a specific location/mapset.

Delete a STRDS that is located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STRDSManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset
    strds_name = 'strds_name_example' # str | The name of the STRDS
    recursive = True # bool | Delete the STRDS and all registered raster map layer recursively (optional)

    try:
        # Delete a STRDS that is located in a specific location/mapset.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_delete(location_name, mapset_name, strds_name, recursive=recursive)
        print("The response of STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 
 **strds_name** | **str**| The name of the STRDS | 
 **recursive** | **bool**| Delete the STRDS and all registered raster map layer recursively | [optional] 

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
**200** | Deletion of the STRDS was successfully finished. |  -  |
**400** | The error message and a detailed log why deletion of the STRDS did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_get**
> STRDSInfoResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_get(location_name, mapset_name, strds_name)

Get information about a STRDS that is located in a specific

Get information about a STRDS that is located in a specific location/mapset. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.strds_info_response_model import STRDSInfoResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset
    strds_name = 'strds_name_example' # str | The name of the STRDS

    try:
        # Get information about a STRDS that is located in a specific
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_get(location_name, mapset_name, strds_name)
        print("The response of STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 
 **strds_name** | **str**| The name of the STRDS | 

### Return type

[**STRDSInfoResponseModel**](STRDSInfoResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns information about a specific STRDS and the log of the process chain that was used to create the response. |  -  |
**400** | The error message and a detailed log why information gathering of the STRDS did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_post(location_name, mapset_name, strds_name, metadata)

Create a new STRDS in a specific location/mapset.

Create a new STRDS in a specific location/mapset. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.processing_response_model import ProcessingResponseModel
from actinia_openapi_python_client.models.strds_creation_model import STRDSCreationModel
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
    api_instance = actinia_openapi_python_client.STRDSManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset
    strds_name = 'strds_name_example' # str | The name of the STRDS
    metadata = actinia_openapi_python_client.STRDSCreationModel() # STRDSCreationModel | Temporal type, title and description of the STRDS

    try:
        # Create a new STRDS in a specific location/mapset.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_post(location_name, mapset_name, strds_name, metadata)
        print("The response of STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 
 **strds_name** | **str**| The name of the STRDS | 
 **metadata** | [**STRDSCreationModel**](STRDSCreationModel.md)| Temporal type, title and description of the STRDS | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/gml+xml, application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creation of the STRDS was successfully finished. |  -  |
**400** | The error message and a detailed log why creation of the STRDS did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete(location_name, mapset_name, strds_name, raster_list)

Unregister raster map layers from a STRDS located in a specific

Unregister raster map layers from a STRDS located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STRDSManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset
    strds_name = 'strds_name_example' # str | The name of the STRDS
    raster_list = ['raster_list_example'] # List[str] | The list of raster map layers to be unregistered from the STRDS

    try:
        # Unregister raster map layers from a STRDS located in a specific
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete(location_name, mapset_name, strds_name, raster_list)
        print("The response of STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 
 **strds_name** | **str**| The name of the STRDS | 
 **raster_list** | [**List[str]**](str.md)| The list of raster map layers to be unregistered from the STRDS | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/gml+xml, application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unregistration of raster map layers was successfully finished. |  -  |
**400** | The error message and a detailed log why raster map layer unregistration did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get**
> STRDSRasterListResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get(location_name, mapset_name, strds_name, where=where)

Get a list of all raster map layers that are registered in a STRDS

Get a list of all raster map layers that are registered in a STRDS that is located in a specific location/mapset. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.strds_raster_list_response_model import STRDSRasterListResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset
    strds_name = 'strds_name_example' # str | The name of the STRDS
    where = 'where_example' # str | A where statement to select user specific raster map layers from the STRDS (optional)

    try:
        # Get a list of all raster map layers that are registered in a STRDS
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get(location_name, mapset_name, strds_name, where=where)
        print("The response of STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 
 **strds_name** | **str**| The name of the STRDS | 
 **where** | **str**| A where statement to select user specific raster map layers from the STRDS | [optional] 

### Return type

[**STRDSRasterListResponseModel**](STRDSRasterListResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of all raster map layers that are registered a specific STRDS and the log of the process chain that was used to create the response. |  -  |
**400** | The error message and a detailed log why creating a list of raster map layers from STRDS did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put(location_name, mapset_name, strds_name, raster_list)

Register raster map layers in a STRDS located in a specific

Register raster map layers in a STRDS located in a specific location/mapset. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.processing_response_model import ProcessingResponseModel
from actinia_openapi_python_client.models.raster_list_entry_model import RasterListEntryModel
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
    api_instance = actinia_openapi_python_client.STRDSManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location
    mapset_name = 'mapset_name_example' # str | The name of the mapset
    strds_name = 'strds_name_example' # str | The name of the STRDS
    raster_list = [actinia_openapi_python_client.RasterListEntryModel()] # List[RasterListEntryModel] | The list of raster map layers to be registered in the STRDS

    try:
        # Register raster map layers in a STRDS located in a specific
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put(location_name, mapset_name, strds_name, raster_list)
        print("The response of STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | 
 **mapset_name** | **str**| The name of the mapset | 
 **strds_name** | **str**| The name of the STRDS | 
 **raster_list** | [**List[RasterListEntryModel]**](RasterListEntryModel.md)| The list of raster map layers to be registered in the STRDS | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/gml+xml, application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registration of raster map layers was successfully finished. |  -  |
**400** | The error message and a detailed log why raster map layer registration did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_render_get**
> locations_location_name_mapsets_mapset_name_strds_strds_name_render_get(location_name, mapset_name, strds_name, n=n, s=s, e=e, w=w, width=width, height=height, start_time=start_time, end_time=end_time)

Render the raster map layers of a specific STRDS as a single image.

Render the raster map layers of a specific STRDS as a single image. All raster layers are rendered in order of their time stamps, from past to future. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STRDSManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    strds_name = 'elevation' # str | The name of the STRDS to render (default to 'elevation')
    n = 3.4 # float | Northern border (optional)
    s = 3.4 # float | Southern border (optional)
    e = 3.4 # float | Eastern border (optional)
    w = 3.4 # float | Western border (optional)
    width = 800.0 # float | Image width in pixel, default is 800 (optional) (default to 800.0)
    height = 600.0 # float | Image height in pixel, default is 600 (optional) (default to 600.0)
    start_time = 'start_time_example' # str | Raster map layers that have equal or greater the start time will be rendered (optional)
    end_time = 'end_time_example' # str | Raster map layers that have equal or lower the end time will be rendered (optional)

    try:
        # Render the raster map layers of a specific STRDS as a single image.
        api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_render_get(location_name, mapset_name, strds_name, n=n, s=s, e=e, w=w, width=width, height=height, start_time=start_time, end_time=end_time)
    except Exception as e:
        print("Exception when calling STRDSManagementApi->locations_location_name_mapsets_mapset_name_strds_strds_name_render_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **strds_name** | **str**| The name of the STRDS to render | [default to &#39;elevation&#39;]
 **n** | **float**| Northern border | [optional] 
 **s** | **float**| Southern border | [optional] 
 **e** | **float**| Eastern border | [optional] 
 **w** | **float**| Western border | [optional] 
 **width** | **float**| Image width in pixel, default is 800 | [optional] [default to 800.0]
 **height** | **float**| Image height in pixel, default is 600 | [optional] [default to 600.0]
 **start_time** | **str**| Raster map layers that have equal or greater the start time will be rendered | [optional] 
 **end_time** | **str**| Raster map layers that have equal or lower the end time will be rendered | [optional] 

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
**400** | The error message and a detailed log why rendering did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

