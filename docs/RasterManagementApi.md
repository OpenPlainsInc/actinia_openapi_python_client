# actinia_openapi_python_client.RasterManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_raster_layers_delete**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_delete) | **DELETE** /locations/{location_name}/mapsets/{mapset_name}/raster_layers | Delete a single raster map layer or a list of raster map layer names
[**locations_location_name_mapsets_mapset_name_raster_layers_get**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/raster_layers | Get a list of raster map layer names that are located in a specific
[**locations_location_name_mapsets_mapset_name_raster_layers_put**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_put) | **PUT** /locations/{location_name}/mapsets/{mapset_name}/raster_layers | Rename a single raster map layer or a list of raster map layers that
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_get**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name}/colors | Get the color definition of an existing raster map layer.
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_post**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name}/colors | Set the color definition for an existing raster map layer.
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_delete**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_delete) | **DELETE** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name} | Delete an existing raster map layer.
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_orig_post**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_orig_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name}/geotiff_async_orig | Export an existing raster map layer as GeoTiff using the raster
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_post**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name}/geotiff_async | Export an existing raster map layer as GeoTiff.
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_get**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name} | Get information about an existing raster map layer.
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_legend_get**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_legend_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name}/legend | Render the legend of a raster map layer as a PNG image.
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_post**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name} | Create a new raster layer by uploading a GeoTIFF
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_render_get**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_render_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name}/render | Render a raster map layer as a PNG image.
[**locations_location_name_mapsets_mapset_name_render_rgb_get**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_render_rgb_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/render_rgb | Render three raster map layer as composed RGB PNG image.
[**locations_location_name_mapsets_mapset_name_render_shade_get**](RasterManagementApi.md#locations_location_name_mapsets_mapset_name_render_shade_get) | **GET** /locations/{location_name}/mapsets/{mapset_name}/render_shade | Render two raster layers as a composed shade PNG image


# **locations_location_name_mapsets_mapset_name_raster_layers_delete**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_delete(location_name, mapset_name, pattern=pattern)

Delete a single raster map layer or a list of raster map layer names

Delete a single raster map layer or a list of raster map layer names that are located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location that should be accessed
    mapset_name = 'mapset_name_example' # str | The name of the mapset from which the raster map layers should be deleted
    pattern = 'pattern_example' # str | A parameter passed for g.remove to remove a list of raster map layers, to remove all eg.: http://<url>?pattern=\"*\" (optional)

    try:
        # Delete a single raster map layer or a list of raster map layer names
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_delete(location_name, mapset_name, pattern=pattern)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location that should be accessed | 
 **mapset_name** | **str**| The name of the mapset from which the raster map layers should be deleted | 
 **pattern** | **str**| A parameter passed for g.remove to remove a list of raster map layers, to remove all eg.: http://&lt;url&gt;?pattern&#x3D;\&quot;*\&quot; | [optional] 

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
**400** | The error message and a detailed log why deletion of raster map layers did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_get**
> StringListProcessingResultResponseModel locations_location_name_mapsets_mapset_name_raster_layers_get(location_name, mapset_name, pattern=pattern)

Get a list of raster map layer names that are located in a specific

Get a list of raster map layer names that are located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The name of the location that should be accessed (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset from which the raster map layers should be listed (default to 'PERMANENT')
    pattern = 'pattern_example' # str | A parameter passed to g.list for raster map layer selection, eg.: http://<url>?pattern=\"*\" (optional)

    try:
        # Get a list of raster map layer names that are located in a specific
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_get(location_name, mapset_name, pattern=pattern)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location that should be accessed | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset from which the raster map layers should be listed | [default to &#39;PERMANENT&#39;]
 **pattern** | **str**| A parameter passed to g.list for raster map layer selection, eg.: http://&lt;url&gt;?pattern&#x3D;\&quot;*\&quot; | [optional] 

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
**200** | This response returns a list of raster map layers and the log of the process chain that was used to create the response. |  -  |
**400** | The error message and a detailed log why listing of raster map layers did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_put**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_put(location_name, mapset_name, rename_list)

Rename a single raster map layer or a list of raster map layers that

Rename a single raster map layer or a list of raster map layers that are located in a specific location/mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location that should be accessed
    mapset_name = 'mapset_name_example' # str | The name of the mapset from which the raster map layers should be renamed
    rename_list = 'rename_list_example' # str | A list of raster name tuples [(a, a_new),(b, b_new),(c, c_new), ...]

    try:
        # Rename a single raster map layer or a list of raster map layers that
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_put(location_name, mapset_name, rename_list)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location that should be accessed | 
 **mapset_name** | **str**| The name of the mapset from which the raster map layers should be renamed | 
 **rename_list** | **str**| A list of raster name tuples [(a, a_new),(b, b_new),(c, c_new), ...] | 

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
**400** | The error message and a detailed log why listing of raster map layers did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_get**
> StringListProcessingResultResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_get(location_name, mapset_name, raster_name)

Get the color definition of an existing raster map layer.

Get the color definition of an existing raster map layer. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required raster map layer
    raster_name = 'raster_name_example' # str | The name of the raster map layer to get the color table from

    try:
        # Get the color definition of an existing raster map layer.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_get(location_name, mapset_name, raster_name)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | 
 **raster_name** | **str**| The name of the raster map layer to get the color table from | 

### Return type

[**StringListProcessingResultResponseModel**](StringListProcessingResultResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of color rules |  -  |
**400** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_post(location_name, mapset_name, raster_name, color)

Set the color definition for an existing raster map layer.

Set the color definition for an existing raster map layer. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.processing_response_model import ProcessingResponseModel
from actinia_openapi_python_client.models.raster_color_model import RasterColorModel
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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required raster map layer
    raster_name = 'raster_name_example' # str | The name of the raster map layer to set the color table
    color = actinia_openapi_python_client.RasterColorModel() # RasterColorModel | The color definition.

    try:
        # Set the color definition for an existing raster map layer.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_post(location_name, mapset_name, raster_name, color)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_colors_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | 
 **raster_name** | **str**| The name of the raster map layer to set the color table | 
 **color** | [**RasterColorModel**](RasterColorModel.md)| The color definition. | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfuly set the color table for a raster map layer |  -  |
**400** | The error message and a detailed error log |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_delete**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_delete(location_name, mapset_name, raster_name)

Delete an existing raster map layer.

Delete an existing raster map layer. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required raster map layer
    raster_name = 'raster_name_example' # str | The name of the raster map layer to be deleted

    try:
        # Delete an existing raster map layer.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_delete(location_name, mapset_name, raster_name)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | 
 **raster_name** | **str**| The name of the raster map layer to be deleted | 

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
**200** | Successfuly delete a raster map layer |  -  |
**400** | The error message and a detailed log why raster map layer deletion did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_orig_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_orig_post(location_name, mapset_name, raster_name)

Export an existing raster map layer as GeoTiff using the raster

Export an existing raster map layer as GTiff or COG (if COG driver available). The link to the exported raster map layer is located in the JSON response. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    raster_name = 'elevation' # str | The name of the raster map layer to export (default to 'elevation')

    try:
        # Export an existing raster map layer as GeoTiff using the raster
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_orig_post(location_name, mapset_name, raster_name)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_orig_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_orig_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **raster_name** | **str**| The name of the raster map layer to export | [default to &#39;elevation&#39;]

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
**200** | The response including the URL to the raster map layer GeoTiff file |  -  |
**400** | The error message and a detailed log why gathering raster map layer information did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_post(location_name, mapset_name, raster_name)

Export an existing raster map layer as GeoTiff.

Export an existing raster map layer as GTiff or COG (if COG driver available). The link to the exported raster map layer is located in the JSON response.The current region settings of the mapset are used to export the raster layer. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    raster_name = 'elevation' # str | The name of the raster map layer to export (default to 'elevation')

    try:
        # Export an existing raster map layer as GeoTiff.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_post(location_name, mapset_name, raster_name)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_geotiff_async_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **raster_name** | **str**| The name of the raster map layer to export | [default to &#39;elevation&#39;]

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
**200** | The response including the URL to the raster map layer GeoTiff file |  -  |
**400** | The error message and a detailed log why gathering raster map layer information did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_get**
> RasterInfoResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_get(location_name, mapset_name, raster_name)

Get information about an existing raster map layer.

Get information about an existing raster map layer. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.raster_info_response_model import RasterInfoResponseModel
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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    raster_name = 'elevation' # str | The name of the raster map layer to get information about (default to 'elevation')

    try:
        # Get information about an existing raster map layer.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_get(location_name, mapset_name, raster_name)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **raster_name** | **str**| The name of the raster map layer to get information about | [default to &#39;elevation&#39;]

### Return type

[**RasterInfoResponseModel**](RasterInfoResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The raster map layer information |  -  |
**400** | The error message and a detailed log why gathering raster map layer information did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_legend_get**
> locations_location_name_mapsets_mapset_name_raster_layers_raster_name_legend_get(location_name, mapset_name, raster_name)

Render the legend of a raster map layer as a PNG image.

Render the legend of a raster map layer as a PNG image. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    raster_name = 'elevation' # str | The name of the raster map layer of which the legend should be rendered (default to 'elevation')

    try:
        # Render the legend of a raster map layer as a PNG image.
        api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_legend_get(location_name, mapset_name, raster_name)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_legend_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **raster_name** | **str**| The name of the raster map layer of which the legend should be rendered | [default to &#39;elevation&#39;]

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
**400** | The error message and a detailed log why legend rendering did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_post(location_name, mapset_name, raster_name)

Create a new raster layer by uploading a GeoTIFF

Create a new raster map layer by uploading a GeoTIFF. This method will fail if the map already exists. An example request is 'curl -L -u \"XXX:XXX\" -X POST -H \"Content-Type: multipart/form-data\" -F \"file=@/home/....tif\" http://localhost:8088/api/v3/locations/nc_spm_08/mapsets/test_mapset/raster_layers/testraster'. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset in which the raster map layer should be created
    raster_name = 'raster_name_example' # str | The name of the new raster map layer to be created

    try:
        # Create a new raster layer by uploading a GeoTIFF
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_post(location_name, mapset_name, raster_name)
        print("The response of RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset in which the raster map layer should be created | 
 **raster_name** | **str**| The name of the new raster map layer to be created | 

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
**200** | Raster map layer import information |  -  |
**400** | The error message and a detailed log why raster map layer import failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_render_get**
> locations_location_name_mapsets_mapset_name_raster_layers_raster_name_render_get(location_name, mapset_name, raster_name, n=n, s=s, e=e, w=w, width=width, height=height)

Render a raster map layer as a PNG image.

Render a raster map layer as a PNG image. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    raster_name = 'elevation' # str | The name of the raster map layer to render (default to 'elevation')
    n = 3.4 # float | Northern border (optional)
    s = 3.4 # float | Southern border (optional)
    e = 3.4 # float | Eastern border (optional)
    w = 3.4 # float | Western border (optional)
    width = 800.0 # float | Image width in pixel, default is 800 (optional) (default to 800.0)
    height = 600.0 # float | Image height in pixel, default is 600 (optional) (default to 600.0)

    try:
        # Render a raster map layer as a PNG image.
        api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_render_get(location_name, mapset_name, raster_name, n=n, s=s, e=e, w=w, width=width, height=height)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_render_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **raster_name** | **str**| The name of the raster map layer to render | [default to &#39;elevation&#39;]
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

# **locations_location_name_mapsets_mapset_name_render_rgb_get**
> locations_location_name_mapsets_mapset_name_render_rgb_get(location_name, mapset_name, red, green, blue, n=n, s=s, e=e, w=w, width=width, height=height)

Render three raster map layer as composed RGB PNG image.

Render three raster map layer as composed RGB PNG image. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'landsat' # str | The name of the mapset that contains the required raster map layer (default to 'landsat')
    red = 'lsat5_1987_30' # str | The name of the raster map layer to render as color red (default to 'lsat5_1987_30')
    green = 'lsat5_1987_20' # str | The name of the raster map layer to render as color green (default to 'lsat5_1987_20')
    blue = 'lsat5_1987_10' # str | The name of the raster map layer to render as color blue (default to 'lsat5_1987_10')
    n = 3.4 # float | Northern border (optional)
    s = 3.4 # float | Southern border (optional)
    e = 3.4 # float | Eastern border (optional)
    w = 3.4 # float | Western border (optional)
    width = 800.0 # float | Image width in pixel, default is 800 (optional) (default to 800.0)
    height = 600.0 # float | Image height in pixel, default is 600 (optional) (default to 600.0)

    try:
        # Render three raster map layer as composed RGB PNG image.
        api_instance.locations_location_name_mapsets_mapset_name_render_rgb_get(location_name, mapset_name, red, green, blue, n=n, s=s, e=e, w=w, width=width, height=height)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_render_rgb_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;landsat&#39;]
 **red** | **str**| The name of the raster map layer to render as color red | [default to &#39;lsat5_1987_30&#39;]
 **green** | **str**| The name of the raster map layer to render as color green | [default to &#39;lsat5_1987_20&#39;]
 **blue** | **str**| The name of the raster map layer to render as color blue | [default to &#39;lsat5_1987_10&#39;]
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
**200** | The RGB composition PNG image |  -  |
**400** | The error message and a detailed log why rendering did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_render_shade_get**
> locations_location_name_mapsets_mapset_name_render_shade_get(location_name, mapset_name, shade, color, n=n, s=s, e=e, w=w, width=width, height=height)

Render two raster layers as a composed shade PNG image

Render two raster layers as a composed shade PNG image. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.RasterManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    shade = 'aspect' # str | The name of the raster map layer to be used for shading (default to 'aspect')
    color = 'elevation' # str | The name of the raster map layer to be used for coloring (default to 'elevation')
    n = 3.4 # float | Northern border (optional)
    s = 3.4 # float | Southern border (optional)
    e = 3.4 # float | Eastern border (optional)
    w = 3.4 # float | Western border (optional)
    width = 800.0 # float | Image width in pixel, default is 800 (optional) (default to 800.0)
    height = 600.0 # float | Image height in pixel, default is 600 (optional) (default to 600.0)

    try:
        # Render two raster layers as a composed shade PNG image
        api_instance.locations_location_name_mapsets_mapset_name_render_shade_get(location_name, mapset_name, shade, color, n=n, s=s, e=e, w=w, width=width, height=height)
    except Exception as e:
        print("Exception when calling RasterManagementApi->locations_location_name_mapsets_mapset_name_render_shade_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **shade** | **str**| The name of the raster map layer to be used for shading | [default to &#39;aspect&#39;]
 **color** | **str**| The name of the raster map layer to be used for coloring | [default to &#39;elevation&#39;]
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
**200** | The shade/color composition PNG image |  -  |
**400** | The error message and a detailed log why rendering did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

