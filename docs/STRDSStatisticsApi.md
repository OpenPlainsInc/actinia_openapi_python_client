# actinia_openapi_python_client.STRDSStatisticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_async_post**](STRDSStatisticsApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_async_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/timestamp/{timestamp}/area_stats_async | Compute area statistics based on a vector map for a single raster
[**locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_sync_post**](STRDSStatisticsApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_sync_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/timestamp/{timestamp}/area_stats_sync | Compute area statistics based on a vector map for a single raster
[**locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_async_post**](STRDSStatisticsApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_async_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/timestamp/{timestamp}/area_stats_univar_async | Compute areal univariate statistics on a raster map layer contained in
[**locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_sync_post**](STRDSStatisticsApi.md#locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_sync_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/strds/{strds_name}/timestamp/{timestamp}/area_stats_univar_sync | Compute areal univariate statistics on a raster map layer contained in


# **locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_async_post**
> RasterAreaStatsResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_async_post(location_name, mapset_name, strds_name, timestamp, shape)

Compute area statistics based on a vector map for a single raster

Compute areal categorical statistics on a raster map layer contained in a space-time raster dataset based on an input polygon. The input polygon must be provided as GeoJSON content in the request body. A correct coordinate reference system must be present in the GeoJSON definition. For each category the size of the occupied area, the number of pixel of the area and the percentage of the area size in relation to all other categories inclusive NULL data are computed. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.raster_area_stats_response_model import RasterAreaStatsResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSStatisticsApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required space-time raster dataset
    strds_name = 'strds_name_example' # str | The name of the space-time raster dataset to select the raster map layer from
    timestamp = 'timestamp_example' # str | The time stamp that should be used for raster map layer selection. Required format is: YYYY-MM-DDTHH:MM:SS for example 2001-03-16T12:30:15.
    shape = 'shape_example' # str | GeoJSON definition of the polygon to compute the statistics for. The .

    try:
        # Compute area statistics based on a vector map for a single raster
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_async_post(location_name, mapset_name, strds_name, timestamp, shape)
        print("The response of STRDSStatisticsApi->locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSStatisticsApi->locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_async_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required space-time raster dataset | 
 **strds_name** | **str**| The name of the space-time raster dataset to select the raster map layer from | 
 **timestamp** | **str**| The time stamp that should be used for raster map layer selection. Required format is: YYYY-MM-DDTHH:MM:SS for example 2001-03-16T12:30:15. | 
 **shape** | **str**| GeoJSON definition of the polygon to compute the statistics for. The . | 

### Return type

[**RasterAreaStatsResponseModel**](RasterAreaStatsResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the areal raster statistical computation |  -  |
**400** | The error message and a detailed log why raster statistic did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_sync_post**
> RasterAreaStatsResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_sync_post(location_name, mapset_name, strds_name, timestamp, shape)

Compute area statistics based on a vector map for a single raster

Compute areal categorical statistics on a raster map layer contained in a space-time raster dataset based on an input polygon. The input polygon must be provided as GeoJSON content in the request body. A correct coordinate reference system must be present in the GeoJSON definition. For each category the size of the occupied area, the number of pixel of the area and the percentage of the area size in relation to all other categories inclusive NULL data are computed. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.raster_area_stats_response_model import RasterAreaStatsResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSStatisticsApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required space-time raster dataset
    strds_name = 'strds_name_example' # str | The name of the space-time raster dataset to select the raster map layer from
    timestamp = 'timestamp_example' # str | The time stamp that should be used for raster map layer selection. Required format is: YYYY-MM-DDTHH:MM:SS for example 2001-03-16T12:30:15.
    shape = 'shape_example' # str | GeoJSON definition of the polygon to compute the statistics for. The .

    try:
        # Compute area statistics based on a vector map for a single raster
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_sync_post(location_name, mapset_name, strds_name, timestamp, shape)
        print("The response of STRDSStatisticsApi->locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSStatisticsApi->locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_sync_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required space-time raster dataset | 
 **strds_name** | **str**| The name of the space-time raster dataset to select the raster map layer from | 
 **timestamp** | **str**| The time stamp that should be used for raster map layer selection. Required format is: YYYY-MM-DDTHH:MM:SS for example 2001-03-16T12:30:15. | 
 **shape** | **str**| GeoJSON definition of the polygon to compute the statistics for. The . | 

### Return type

[**RasterAreaStatsResponseModel**](RasterAreaStatsResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the areal raster statistical computation |  -  |
**400** | The error message and a detailed log why raster statistic did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_async_post**
> RasterAreaUnivarStatsResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_async_post(location_name, mapset_name, strds_name, timestamp, shape)

Compute areal univariate statistics on a raster map layer contained in

Compute areal univariate statistics on a raster map layer contained in a space-time raster dataset based on an input polygon. The input polygon must be provided as GeoJSON content in the request body. A correct coordinate reference system must be present in the GeoJSON definition. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.raster_area_univar_stats_response_model import RasterAreaUnivarStatsResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSStatisticsApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required space-time raster dataset
    strds_name = 'strds_name_example' # str | The name of the space-time raster dataset to select the raster map layer from
    timestamp = 'timestamp_example' # str | The time stamp that should be used for raster map layer selection. Required format is: YYYY-MM-DDTHH:MM:SS for example 2001-03-16T12:30:15.
    shape = 'shape_example' # str | GeoJSON definition of the polygon to compute the statistics for.

    try:
        # Compute areal univariate statistics on a raster map layer contained in
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_async_post(location_name, mapset_name, strds_name, timestamp, shape)
        print("The response of STRDSStatisticsApi->locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSStatisticsApi->locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_async_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required space-time raster dataset | 
 **strds_name** | **str**| The name of the space-time raster dataset to select the raster map layer from | 
 **timestamp** | **str**| The time stamp that should be used for raster map layer selection. Required format is: YYYY-MM-DDTHH:MM:SS for example 2001-03-16T12:30:15. | 
 **shape** | **str**| GeoJSON definition of the polygon to compute the statistics for. | 

### Return type

[**RasterAreaUnivarStatsResponseModel**](RasterAreaUnivarStatsResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the areal univar raster statistical computation |  -  |
**400** | The error message and a detailed log why univar raster statistic did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_sync_post**
> RasterAreaUnivarStatsResponseModel locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_sync_post(location_name, mapset_name, strds_name, timestamp, shape)

Compute areal univariate statistics on a raster map layer contained in

Compute areal univariate statistics on a raster map layer contained in a space-time raster dataset based on an input polygon. The input polygon must be provided as GeoJSON content in the request body. A correct coordinate reference system must be present in the GeoJSON definition. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.raster_area_univar_stats_response_model import RasterAreaUnivarStatsResponseModel
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
    api_instance = actinia_openapi_python_client.STRDSStatisticsApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required space-time raster dataset
    strds_name = 'strds_name_example' # str | The name of the space-time raster dataset to select the raster map layer from
    timestamp = 'timestamp_example' # str | The time stamp that should be used for raster map layer selection. Required format is: YYYY-MM-DDTHH:MM:SS for example 2001-03-16T12:30:15.
    shape = 'shape_example' # str | GeoJSON definition of the polygon to compute the statistics for.

    try:
        # Compute areal univariate statistics on a raster map layer contained in
        api_response = api_instance.locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_sync_post(location_name, mapset_name, strds_name, timestamp, shape)
        print("The response of STRDSStatisticsApi->locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling STRDSStatisticsApi->locations_location_name_mapsets_mapset_name_strds_strds_name_timestamp_timestamp_area_stats_univar_sync_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required space-time raster dataset | 
 **strds_name** | **str**| The name of the space-time raster dataset to select the raster map layer from | 
 **timestamp** | **str**| The time stamp that should be used for raster map layer selection. Required format is: YYYY-MM-DDTHH:MM:SS for example 2001-03-16T12:30:15. | 
 **shape** | **str**| GeoJSON definition of the polygon to compute the statistics for. | 

### Return type

[**RasterAreaUnivarStatsResponseModel**](RasterAreaUnivarStatsResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the areal univar raster statistical computation |  -  |
**400** | The error message and a detailed log why univar raster statistic did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

