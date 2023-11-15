# actinia_openapi_python_client.RasterSamplingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_async_post**](RasterSamplingApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_async_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name}/sampling_async | Perform raster map sampling on a raster map layer based on input
[**locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_sync_post**](RasterSamplingApi.md#locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_sync_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/raster_layers/{raster_name}/sampling_sync | Perform raster map sampling on a raster map layer based on input


# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_async_post**
> RasterSamplingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_async_post(location_name, mapset_name, raster_name, points)

Perform raster map sampling on a raster map layer based on input

Spatial sampling of a raster dataset with vector points. The vector points must be in the same coordinate reference system as the location that contains the raster dataset. The result of the sampling is located in the resource responseJSON document after the processing was finished, as a list of values for each vector point. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.point_list_model import PointListModel
from actinia_openapi_python_client.models.raster_sampling_response_model import RasterSamplingResponseModel
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
    api_instance = actinia_openapi_python_client.RasterSamplingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required raster map layer
    raster_name = 'raster_name_example' # str | The name of the raster map layer to perform the raster map sampling from
    points = actinia_openapi_python_client.PointListModel() # PointListModel | The sampling point array [[id, x, y],[id, x, y]]. The coordinates of the sampling points must be in the same coordinate reference system as the location that contains the vector dataset.

    try:
        # Perform raster map sampling on a raster map layer based on input
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_async_post(location_name, mapset_name, raster_name, points)
        print("The response of RasterSamplingApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterSamplingApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_async_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | 
 **raster_name** | **str**| The name of the raster map layer to perform the raster map sampling from | 
 **points** | [**PointListModel**](PointListModel.md)| The sampling point array [[id, x, y],[id, x, y]]. The coordinates of the sampling points must be in the same coordinate reference system as the location that contains the vector dataset. | 

### Return type

[**RasterSamplingResponseModel**](RasterSamplingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the raster map sampling |  -  |
**400** | The error message and a detailed log why raster sampling did not succeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_sync_post**
> RasterSamplingResponseModel locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_sync_post(location_name, mapset_name, raster_name, points)

Perform raster map sampling on a raster map layer based on input

Spatial sampling of a raster dataset with vector points. The vector points must be in the same coordinate reference system as the location that contains the raster dataset. The result of the sampling is located in the resource responseJSON document after the processing was finished, as a list of values for each vector point. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.point_list_model import PointListModel
from actinia_openapi_python_client.models.raster_sampling_response_model import RasterSamplingResponseModel
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
    api_instance = actinia_openapi_python_client.RasterSamplingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required raster map layer
    raster_name = 'raster_name_example' # str | The name of the raster map layer to perform the raster map sampling from
    points = actinia_openapi_python_client.PointListModel() # PointListModel | The sampling point array [[id, x, y],[id, x, y]]. The coordinates of the sampling points must be in the same coordinate reference system as the location that contains the vector dataset.

    try:
        # Perform raster map sampling on a raster map layer based on input
        api_response = api_instance.locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_sync_post(location_name, mapset_name, raster_name, points)
        print("The response of RasterSamplingApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RasterSamplingApi->locations_location_name_mapsets_mapset_name_raster_layers_raster_name_sampling_sync_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | 
 **raster_name** | **str**| The name of the raster map layer to perform the raster map sampling from | 
 **points** | [**PointListModel**](PointListModel.md)| The sampling point array [[id, x, y],[id, x, y]]. The coordinates of the sampling points must be in the same coordinate reference system as the location that contains the vector dataset. | 

### Return type

[**RasterSamplingResponseModel**](RasterSamplingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the raster map sampling |  -  |
**400** | The error message and a detailed log why raster sampling did not succeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

