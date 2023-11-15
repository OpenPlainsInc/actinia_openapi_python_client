# actinia_openapi_python_client.STRDSSamplingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_geojson_post**](STRDSSamplingApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_geojson_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/sampling_async_geojson | Sample a strds by point coordinates, asynchronous call
[**locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_post**](STRDSSamplingApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/sampling_async | Sample a strds by point coordinates, asynchronous call
[**locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_geojson_post**](STRDSSamplingApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_geojson_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/sampling_sync_geojson | Sample a strds by point coordinates, synchronous call
[**locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_post**](STRDSSamplingApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/sampling_sync | Sample a strds by point coordinates, synchronous call


# **locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_geojson_post**
> STRDSSampleGeoJSONResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_geojson_post(location_name, mapset_name, strds_name, points)

Sample a strds by point coordinates, asynchronous call

Spatial sampling of a space-time raster dataset (STRDS) with vector points. The vector points must be provided as GeoJSON vector point format that includes correct coordinate system specification. The result of the sampling is located in the resource responseJSON document after the processing was finished, as a list of timestamped values for each vector point. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.strds_sample_geo_json_response_model import STRDSSampleGeoJSONResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSSamplingApi(api_client)
    location_name = 'ECAD' # str | The location name (default to 'ECAD')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    strds_name = 'temperature_mean_1950_2013_yearly_celsius' # str | The name of the space-time raster dataset that should be sampled (default to 'temperature_mean_1950_2013_yearly_celsius')
    points = 'points_example' # str | GeoJSON vector input that contains the vector points for sampling

    try:
        # Sample a strds by point coordinates, asynchronous call
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_geojson_post(location_name, mapset_name, strds_name, points)
        print("The response of STRDSSamplingApi->locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_geojson_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSSamplingApi->locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_geojson_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;ECAD&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **strds_name** | **str**| The name of the space-time raster dataset that should be sampled | [default to &#39;temperature_mean_1950_2013_yearly_celsius&#39;]
 **points** | **str**| GeoJSON vector input that contains the vector points for sampling | 

### Return type

[**STRDSSampleGeoJSONResponseModel**](STRDSSampleGeoJSONResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the strds sampling |  -  |
**400** | The error message and a detailed log why strds sampling did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_post**
> STRDSSampleResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_post(location_name, mapset_name, strds_name, points)

Sample a strds by point coordinates, asynchronous call

Spatial sampling of a space-time raster dataset with vector points. The vector points must be in the same coordinate reference system as the location that contains the space-time raster dataset. The result of the sampling is located in the resource responseJSON docuement after the processing was finished, as a list of timestamped values for each vector point. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.point_list_model import PointListModel
from actinia_openapi_python_client.models.strds_sample_response_model import STRDSSampleResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSSamplingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required raster map layer
    strds_name = 'strds_name_example' # str | The name of the space-time raster dataset that should be sampled
    points = actinia_openapi_python_client.PointListModel() # PointListModel | The sampling point array [[id, x, y],[id, x, y]] and an optional where statement. The coordinates of the sampling points must be the same as of the location that contains the space-time raster dataset.

    try:
        # Sample a strds by point coordinates, asynchronous call
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_post(location_name, mapset_name, strds_name, points)
        print("The response of STRDSSamplingApi->locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSSamplingApi->locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_async_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | 
 **strds_name** | **str**| The name of the space-time raster dataset that should be sampled | 
 **points** | [**PointListModel**](PointListModel.md)| The sampling point array [[id, x, y],[id, x, y]] and an optional where statement. The coordinates of the sampling points must be the same as of the location that contains the space-time raster dataset. | 

### Return type

[**STRDSSampleResponseModel**](STRDSSampleResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the strds sampling |  -  |
**400** | The error message and a detailed log why strds sampling did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_geojson_post**
> STRDSSampleGeoJSONResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_geojson_post(location_name, mapset_name, strds_name, points)

Sample a strds by point coordinates, synchronous call

Spatial sampling of a space-time raster dataset (STRDS) with vector points. The vector points must be provided as GeoJSON vector point format that includes correct coordinate system specification. The result of the sampling is located in the resource responseJSON document after the processing was finished, as a list of timestamped values for each vector point. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.strds_sample_geo_json_response_model import STRDSSampleGeoJSONResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSSamplingApi(api_client)
    location_name = 'ECAD' # str | The location name (default to 'ECAD')
    mapset_name = 'PERMANENT' # str | The name of the mapset that contains the required raster map layer (default to 'PERMANENT')
    strds_name = 'temperature_mean_1950_2013_yearly_celsius' # str | The name of the space-time raster dataset that should be sampled (default to 'temperature_mean_1950_2013_yearly_celsius')
    points = 'points_example' # str | GeoJSON vector input that contains the vector points for sampling

    try:
        # Sample a strds by point coordinates, synchronous call
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_geojson_post(location_name, mapset_name, strds_name, points)
        print("The response of STRDSSamplingApi->locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_geojson_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSSamplingApi->locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_geojson_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;ECAD&#39;]
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | [default to &#39;PERMANENT&#39;]
 **strds_name** | **str**| The name of the space-time raster dataset that should be sampled | [default to &#39;temperature_mean_1950_2013_yearly_celsius&#39;]
 **points** | **str**| GeoJSON vector input that contains the vector points for sampling | 

### Return type

[**STRDSSampleGeoJSONResponseModel**](STRDSSampleGeoJSONResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the strds sampling |  -  |
**400** | The error message and a detailed log why strds sampling did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_post**
> STRDSSampleResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_post(location_name, mapset_name, strds_name, points)

Sample a strds by point coordinates, synchronous call

Spatial sampling of a space-time raster dataset with vector points. The vector points must be in the same coordinate reference system as the location that contains the space-time raster dataset. The result of the sampling is located in the resource responseJSON docuement after the processing was finished, as a list of timestamped values for each vector point. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.point_list_model import PointListModel
from actinia_openapi_python_client.models.strds_sample_response_model import STRDSSampleResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSSamplingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required raster map layer
    strds_name = 'strds_name_example' # str | The name of the space-time raster dataset that should be sampled
    points = actinia_openapi_python_client.PointListModel() # PointListModel | The sampling point array [[id, x, y],[id, x, y]] and an optional where statement. The coordinates of the sampling points must be the same as of the location that contains the space-time raster dataset.

    try:
        # Sample a strds by point coordinates, synchronous call
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_post(location_name, mapset_name, strds_name, points)
        print("The response of STRDSSamplingApi->locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSSamplingApi->locations_location_name_mapsets_mapset_name_strds_strds_name_sampling_sync_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required raster map layer | 
 **strds_name** | **str**| The name of the space-time raster dataset that should be sampled | 
 **points** | [**PointListModel**](PointListModel.md)| The sampling point array [[id, x, y],[id, x, y]] and an optional where statement. The coordinates of the sampling points must be the same as of the location that contains the space-time raster dataset. | 

### Return type

[**STRDSSampleResponseModel**](STRDSSampleResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the strds sampling |  -  |
**400** | The error message and a detailed log why strds sampling did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

