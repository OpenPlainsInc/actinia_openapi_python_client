# actinia_openapi_python_client.VectorManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_vector_layers_delete**](VectorManagementApi.md#locations_location_name_mapsets_mapset_name_vector_layers_delete) | **DELETE** /locations/{location_name}/mapsets/{mapset_name}/vector_layers | Delete a single vector map layer or a list of vector map layer names
[**locations_location_name_mapsets_mapset_name_vector_layers_get**](VectorManagementApi.md#locations_location_name_mapsets_mapset_name_vector_layers_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/vector_layers | Get a list of vector map layer names that are located in a specific
[**locations_location_name_mapsets_mapset_name_vector_layers_put**](VectorManagementApi.md#locations_location_name_mapsets_mapset_name_vector_layers_put) | **PUT** /locations/{location_name}/mapsets/{mapset_name}/vector_layers | Rename a single vector map layer or a list of vector map layers that
[**locations_location_name_mapsets_mapset_name_vector_layers_vector_name_delete**](VectorManagementApi.md#locations_location_name_mapsets_mapset_name_vector_layers_vector_name_delete) | **DELETE** /locations/{location_name}/mapsets/{mapset_name}/vector_layers/{vector_name} | Delete an existing vector map layer.
[**locations_location_name_mapsets_mapset_name_vector_layers_vector_name_get**](VectorManagementApi.md#locations_location_name_mapsets_mapset_name_vector_layers_vector_name_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/vector_layers/{vector_name} | Get information about an existing vector map layer.
[**locations_location_name_mapsets_mapset_name_vector_layers_vector_name_post**](VectorManagementApi.md#locations_location_name_mapsets_mapset_name_vector_layers_vector_name_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/vector_layers/{vector_name} | Create a new vector layer by uploading a GPKG, zipped Shapefile,
[**locations_location_name_mapsets_mapset_name_vector_layers_vector_name_render_get**](VectorManagementApi.md#locations_location_name_mapsets_mapset_name_vector_layers_vector_name_render_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/vector_layers/{vector_name}/render | Render a single vector map layer


# **locations_location_name_mapsets_mapset_name_vector_layers_delete**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_vector_layers_delete(location_name, mapset_name, pattern=pattern)

Delete a single vector map layer or a list of vector map layer names

Delete a single vector map layer or a list of vector map layer names that are located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.VectorManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location that should be accessed
    mapset_name = 'mapset_name_example' # str | The name of the mapset from which the vector map layers should be deleted
    pattern = 'pattern_example' # str | A parameter passed for g.remove to remove a list of vector map layers, to remove all eg.: http://<url>?pattern=\"*\" (optional)

    try:
        # Delete a single vector map layer or a list of vector map layer names
        api_response = api_instance.locations_location_name_mapsets_mapset_name_vector_layers_delete(location_name, mapset_name, pattern=pattern)
        print("The response of VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location that should be accessed | 
 **mapset_name** | **str**| The name of the mapset from which the vector map layers should be deleted | 
 **pattern** | **str**| A parameter passed for g.remove to remove a list of vector map layers, to remove all eg.: http://&lt;url&gt;?pattern&#x3D;\&quot;*\&quot; | [optional] 

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
**200** | This response returns the log of the process chain that was used to create the response. |  -  |
**400** | The error message and a detailed log why deletion of vector map layers did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_vector_layers_get**
> StringListProcessingResultResponseModel locations_location_name_mapsets_mapset_name_vector_layers_get(location_name, mapset_name, pattern=pattern)

Get a list of vector map layer names that are located in a specific

Get a list of vector map layer names that are located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.VectorManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The name of the location that should be accessed (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset from which the vector map layers should be listed (default to 'PERMANENT')
    pattern = 'pattern_example' # str | A parameter passed to g.list for vector map layer selection, eg.: http://<url>?pattern=\"*\" (optional)

    try:
        # Get a list of vector map layer names that are located in a specific
        api_response = api_instance.locations_location_name_mapsets_mapset_name_vector_layers_get(location_name, mapset_name, pattern=pattern)
        print("The response of VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location that should be accessed | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset from which the vector map layers should be listed | [default to &#39;PERMANENT&#39;]
 **pattern** | **str**| A parameter passed to g.list for vector map layer selection, eg.: http://&lt;url&gt;?pattern&#x3D;\&quot;*\&quot; | [optional] 

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
**200** | This response returns a list of vector map layers and the log of the process chain that was used to create the response. |  -  |
**400** | The error message and a detailed log why listing of vector map layers did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_vector_layers_put**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_vector_layers_put(location_name, mapset_name, rename_list)

Rename a single vector map layer or a list of vector map layers that

Rename a single vector map layer or a list of vector map layers that are located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.VectorManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location that should be accessed
    mapset_name = 'mapset_name_example' # str | The name of the mapset from which the vector map layers should be renamed
    rename_list = 'rename_list_example' # str | A list of vector name tuples [(a, a_new),(b, b_new),(c, c_new), ...]

    try:
        # Rename a single vector map layer or a list of vector map layers that
        api_response = api_instance.locations_location_name_mapsets_mapset_name_vector_layers_put(location_name, mapset_name, rename_list)
        print("The response of VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location that should be accessed | 
 **mapset_name** | **str**| The name of the mapset from which the vector map layers should be renamed | 
 **rename_list** | **str**| A list of vector name tuples [(a, a_new),(b, b_new),(c, c_new), ...] | 

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
**200** | This response returns the log of the process chain that was used to create the response. |  -  |
**400** | The error message and a detailed log why listing of vector map layers did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_vector_layers_vector_name_delete**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_vector_layers_vector_name_delete(location_name, mapset_name, vector_name)

Delete an existing vector map layer.

Delete an existing vector map layer. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.VectorManagementApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required vector map layer
    vector_name = 'vector_name_example' # str | The name of the vector map layer to be deleted

    try:
        # Delete an existing vector map layer.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_vector_layers_vector_name_delete(location_name, mapset_name, vector_name)
        print("The response of VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required vector map layer | 
 **vector_name** | **str**| The name of the vector map layer to be deleted | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully delete a vector map layer |  -  |
**400** | The error message and a detailed log why vector map layer deletion did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_vector_layers_vector_name_get**
> VectorInfoResponseModel locations_location_name_mapsets_mapset_name_vector_layers_vector_name_get(location_name, mapset_name, vector_name)

Get information about an existing vector map layer.

Get information about an existing vector map layer. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.vector_info_response_model import VectorInfoResponseModel
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
    api_instance = actinia_openapi_python_client.VectorManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required vector map layer (default to 'PERMANENT')
    vector_name = 'boundary_county' # str | The name of the vector map layer to get information about (default to 'boundary_county')

    try:
        # Get information about an existing vector map layer.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_vector_layers_vector_name_get(location_name, mapset_name, vector_name)
        print("The response of VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required vector map layer | [default to &#39;PERMANENT&#39;]
 **vector_name** | **str**| The name of the vector map layer to get information about | [default to &#39;boundary_county&#39;]

### Return type

[**VectorInfoResponseModel**](VectorInfoResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The vector map layer information |  -  |
**400** | The error message and a detailed log why gathering vector map layer information did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_vector_layers_vector_name_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_vector_layers_vector_name_post(location_name, mapset_name, vector_name, creation_params)

Create a new vector layer by uploading a GPKG, zipped Shapefile,

Create a new vector map layer by uploading a GPKG, zipped Shapefile or GeoJSON. This method will fail if the map already exists. An example request is 'curl -L -u \"XXX:XXX\" -X POST -H \"Content-Type: multipart/form-data\" -F \"file=@/home/....gpkg\" http://localhost:8088/api/v3/locations/nc_spm_08/mapsets/test_mapset/vector_layers/testvector'. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.processing_response_model import ProcessingResponseModel
from actinia_openapi_python_client.models.vector_region_creation_model import VectorRegionCreationModel
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
    api_instance = actinia_openapi_python_client.VectorManagementApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required vector map layer
    vector_name = 'vector_name_example' # str | The name of the new vector map layer to be created.
    creation_params = actinia_openapi_python_client.VectorRegionCreationModel() # VectorRegionCreationModel | Parameters to create random vector point map layer in a specific region.

    try:
        # Create a new vector layer by uploading a GPKG, zipped Shapefile,
        api_response = api_instance.locations_location_name_mapsets_mapset_name_vector_layers_vector_name_post(location_name, mapset_name, vector_name, creation_params)
        print("The response of VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required vector map layer | 
 **vector_name** | **str**| The name of the new vector map layer to be created. | 
 **creation_params** | [**VectorRegionCreationModel**](VectorRegionCreationModel.md)| Parameters to create random vector point map layer in a specific region. | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Content-Type: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The vector map layer import information |  -  |
**400** | The error message and a detailed log why vector map layer import failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_vector_layers_vector_name_render_get**
> locations_location_name_mapsets_mapset_name_vector_layers_vector_name_render_get(location_name, mapset_name, vector_name, n=n, s=s, e=e, w=w, width=width, height=height)

Render a single vector map layer

Render a single vector map layer. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.VectorManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    vector_name = 'boundary_county' # str | The name of the vector map layer to render (default to 'boundary_county')
    n = 3.4 # float | Northern border (optional)
    s = 3.4 # float | Southern border (optional)
    e = 3.4 # float | Eastern border (optional)
    w = 3.4 # float | Western border (optional)
    width = 800.0 # float | Image width in pixel, default is 800 (optional) (default to 800.0)
    height = 600.0 # float | Image height in pixel, default is 600 (optional) (default to 600.0)

    try:
        # Render a single vector map layer
        api_instance.locations_location_name_mapsets_mapset_name_vector_layers_vector_name_render_get(location_name, mapset_name, vector_name, n=n, s=s, e=e, w=w, width=width, height=height)
    except Exception as e:
        print("Exception when calling VectorManagementApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_render_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **vector_name** | **str**| The name of the vector map layer to render | [default to &#39;boundary_county&#39;]
 **n** | **float**| Northern border | [optional] 
 **s** | **float**| Southern border | [optional] 
 **e** | **float**| Eastern border | [optional] 
 **w** | **float**| Western border | [optional] 
 **width** | **float**| Image width in pixel, default is 800 | [optional] [default to 800.0]
 **height** | **float**| Image height in pixel, default is 600 | [optional] [default to 600.0]

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

