# actinia_openapi_python_client.SatelliteImageAlgorithmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**landsat_process_landsat_id_atcor_method_processing_method_post**](SatelliteImageAlgorithmsApi.md#landsat_process_landsat_id_atcor_method_processing_method_post) | **POST** /landsat_process/{landsat_id}/{atcor_method}/{processing_method} | Vegetation index computation from an atmospherically corrected Landsat scene.
[**landsat_query_get**](SatelliteImageAlgorithmsApi.md#landsat_query_get) | **GET** /landsat_query | Query the Google Landsat archives using time interval, lat/lon coordinates, scene id, spacecraft id and cloud cover.
[**locations_location_name_mapsets_mapset_name_landsat_import_post**](SatelliteImageAlgorithmsApi.md#locations_location_name_mapsets_mapset_name_landsat_import_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/landsat_import | Download and import Landsat scenes into a new mapset and create a space time dataset for each imported band.
[**locations_location_name_mapsets_mapset_name_sentinel2_import_post**](SatelliteImageAlgorithmsApi.md#locations_location_name_mapsets_mapset_name_sentinel2_import_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/sentinel2_import | Download and import Sentinel2A scenes into a new mapset and create a space-time raster dataset for each imported band.
[**sentinel2_process_gcs_ndvi_product_id_post**](SatelliteImageAlgorithmsApi.md#sentinel2_process_gcs_ndvi_product_id_post) | **POST** /sentinel2_process_gcs/ndvi/{product_id} | NDVI computation of an arbitrary Sentinel-2 scene. The results are stored in the Google Cloud Storage.
[**sentinel2_process_ndvi_product_id_post**](SatelliteImageAlgorithmsApi.md#sentinel2_process_ndvi_product_id_post) | **POST** /sentinel2_process/ndvi/{product_id} | NDVI computation of an arbitrary Sentinel-2 scene.
[**sentinel2_query_get**](SatelliteImageAlgorithmsApi.md#sentinel2_query_get) | **GET** /sentinel2_query | Query the Google Sentinel2 archives using time interval, lat/lon coordinates, scene id and cloud cover.
[**sentinel2a_aws_query_post**](SatelliteImageAlgorithmsApi.md#sentinel2a_aws_query_post) | **POST** /sentinel2a_aws_query | Generate the download urls for a list of sentinel2A scenes and band numbers.


# **landsat_process_landsat_id_atcor_method_processing_method_post**
> LandsatNDVIResponseModel landsat_process_landsat_id_atcor_method_processing_method_post(landsat_id, atcor_method, processing_method)

Vegetation index computation from an atmospherically corrected Landsat scene.

Vegetation index computation from an atmospherically corrected Landsat scene. The Landsat scene is located in the google cloud storage. The processing is as follows: A user specific Landsat scene (LT4, LT5, LE7 and LC8) will be download and imported into an ephemeral database. Then atmospheric correction will be performed, with either TOAR or DOS4, depending on the users choice. The user specific vegetation index will be computed based on the TOAR or DOS4 data. The result of the computation is available as gzipped Geotiff file. In addition, the univariate statistic will be computed as well as a preview image including a legend. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.landsat_ndvi_response_model import LandsatNDVIResponseModel
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
    api_instance = actinia_openapi_python_client.SatelliteImageAlgorithmsApi(api_client)
    landsat_id = 'LT41970251990147XXX03' # str | The id of a Landsat scene only with sensors: LT04, LT05, LE07, LC08 (default to 'LT41970251990147XXX03')
    atcor_method = 'DOS4' # str | The method for atmospheric correction (default to 'DOS4')
    processing_method = 'NDVI' # str | The method that should be used to compute the vegetation index (default to 'NDVI')

    try:
        # Vegetation index computation from an atmospherically corrected Landsat scene.
        api_response = api_instance.landsat_process_landsat_id_atcor_method_processing_method_post(landsat_id, atcor_method, processing_method)
        print("The response of SatelliteImageAlgorithmsApi->landsat_process_landsat_id_atcor_method_processing_method_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SatelliteImageAlgorithmsApi->landsat_process_landsat_id_atcor_method_processing_method_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **landsat_id** | **str**| The id of a Landsat scene only with sensors: LT04, LT05, LE07, LC08 | [default to &#39;LT41970251990147XXX03&#39;]
 **atcor_method** | **str**| The method for atmospheric correction | [default to &#39;DOS4&#39;]
 **processing_method** | **str**| The method that should be used to compute the vegetation index | [default to &#39;NDVI&#39;]

### Return type

[**LandsatNDVIResponseModel**](LandsatNDVIResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response includes all created resources as URL as well as the processing log and other metadata. |  -  |
**400** | The error message and a detailed log why NDVI processing of a Landsat scene did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **landsat_query_get**
> SatelliteSceneList landsat_query_get(scene_id=scene_id, spacecraft_id=spacecraft_id, start_time=start_time, end_time=end_time, lon=lon, lat=lat, cloud_covert=cloud_covert)

Query the Google Landsat archives using time interval, lat/lon coordinates, scene id, spacecraft id and cloud cover.

Query the Google Landsat archives using time interval, lat/lon coordinates, scene id, spacecraft id and cloud cover. All scenes that are located within the time interval and that intersect the given latitude/longitude coordinates are returned as a list of scene names with associated time stamps. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.satellite_scene_list import SatelliteSceneList
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
    api_instance = actinia_openapi_python_client.SatelliteImageAlgorithmsApi(api_client)
    scene_id = 'scene_id_example' # str | The scene id of the landsat scenes that should be searched (optional)
    spacecraft_id = 'spacecraft_id_example' # str | The spacecraft id of the landsat scenes that should be searched (optional)
    start_time = 'start_time_example' # str | The start time of the search interval (optional)
    end_time = 'end_time_example' # str | The end time of the search interval (optional)
    lon = 3.4 # float | The longitude coordinate with which the scenes should intersect (optional)
    lat = 3.4 # float | The latitude coordinate with which the scenes should intersect (optional)
    cloud_covert = 3.4 # float | Cloud cover between 0 - 100 (optional)

    try:
        # Query the Google Landsat archives using time interval, lat/lon coordinates, scene id, spacecraft id and cloud cover.
        api_response = api_instance.landsat_query_get(scene_id=scene_id, spacecraft_id=spacecraft_id, start_time=start_time, end_time=end_time, lon=lon, lat=lat, cloud_covert=cloud_covert)
        print("The response of SatelliteImageAlgorithmsApi->landsat_query_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SatelliteImageAlgorithmsApi->landsat_query_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **str**| The scene id of the landsat scenes that should be searched | [optional] 
 **spacecraft_id** | **str**| The spacecraft id of the landsat scenes that should be searched | [optional] 
 **start_time** | **str**| The start time of the search interval | [optional] 
 **end_time** | **str**| The end time of the search interval | [optional] 
 **lon** | **float**| The longitude coordinate with which the scenes should intersect | [optional] 
 **lat** | **float**| The latitude coordinate with which the scenes should intersect | [optional] 
 **cloud_covert** | **float**| Cloud cover between 0 - 100 | [optional] 

### Return type

[**SatelliteSceneList**](SatelliteSceneList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of satellite scenes that fit the search |  -  |
**400** | The error message if the search did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_landsat_import_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_landsat_import_post(location_name, mapset_name, tiles)

Download and import Landsat scenes into a new mapset and create a space time dataset for each imported band.

Download and import Landsat scenes into a new mapset and create a space-time raster dataset for each imported band. The resulting data will be located in a persistent user database. The location name is part of the path and must exist. The mapset will be created while importing and should not already exist in the location. The names of theLandsat scenes that should be downloaded must be specified in the HTTP body as application/json content. In addition, the basename of the STRDS that should manage the Landsat scenes must be provided in the application/json content. For each band a separate strds will be cerated and the STRDS base name will be extended with the band number.This call is performed asynchronously. The provided resource URL must be pulled to receive the status of the import. The data is available in the provided location/mapset, after the download and import finished. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.landsat_scene_list_model import LandsatSceneListModel
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
    api_instance = actinia_openapi_python_client.SatelliteImageAlgorithmsApi(api_client)
    location_name = 'location_name_example' # str | The location name to import the Landsat scenes in
    mapset_name = 'mapset_name_example' # str | The name of the mapset to import the Landsat scenes in
    tiles = actinia_openapi_python_client.LandsatSceneListModel() # LandsatSceneListModel | The list of Landsat scenes, the band names and the target STRDS names

    try:
        # Download and import Landsat scenes into a new mapset and create a space time dataset for each imported band.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_landsat_import_post(location_name, mapset_name, tiles)
        print("The response of SatelliteImageAlgorithmsApi->locations_location_name_mapsets_mapset_name_landsat_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SatelliteImageAlgorithmsApi->locations_location_name_mapsets_mapset_name_landsat_import_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name to import the Landsat scenes in | 
 **mapset_name** | **str**| The name of the mapset to import the Landsat scenes in | 
 **tiles** | [**LandsatSceneListModel**](LandsatSceneListModel.md)| The list of Landsat scenes, the band names and the target STRDS names | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the Landsat time series import |  -  |
**400** | The error message and a detailed log why Landsat time series import did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_sentinel2_import_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_sentinel2_import_post(location_name, mapset_name, tiles)

Download and import Sentinel2A scenes into a new mapset and create a space-time raster dataset for each imported band.

Download and import Sentinel2A scenes into a new mapset and create a space-time raster dataset for each imported band. The resulting data will be located in a persistent user database. The location name is part of the path and must exist. The mapset will be created while importing and should not already exist in the location. The names of theSentinel-2 scenes and the band names that should be downloaded must be specified in the HTTP body as application/json content. In addition, the names of the STRDS that should manage the sentinel scenes must be provided in the application/json content. For each band a separate STRDS name must be provided.This call is performed asynchronously. The provided resource URL must be pulled to receive the status of the import. The data is available in the provided location/mapset, after the download and import finished. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.processing_response_model import ProcessingResponseModel
from actinia_openapi_python_client.models.sentinel2_a_scene_list_model import Sentinel2ASceneListModel
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
    api_instance = actinia_openapi_python_client.SatelliteImageAlgorithmsApi(api_client)
    location_name = 'location_name_example' # str | The location name to import the Sentinel2A scenes in
    mapset_name = 'mapset_name_example' # str | The name of the mapset to import the Sentinel2A scenes in
    tiles = actinia_openapi_python_client.Sentinel2ASceneListModel() # Sentinel2ASceneListModel | The list of Sentinel-2 scenes, the band names and the target STRDS names

    try:
        # Download and import Sentinel2A scenes into a new mapset and create a space-time raster dataset for each imported band.
        api_response = api_instance.locations_location_name_mapsets_mapset_name_sentinel2_import_post(location_name, mapset_name, tiles)
        print("The response of SatelliteImageAlgorithmsApi->locations_location_name_mapsets_mapset_name_sentinel2_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SatelliteImageAlgorithmsApi->locations_location_name_mapsets_mapset_name_sentinel2_import_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name to import the Sentinel2A scenes in | 
 **mapset_name** | **str**| The name of the mapset to import the Sentinel2A scenes in | 
 **tiles** | [**Sentinel2ASceneListModel**](Sentinel2ASceneListModel.md)| The list of Sentinel-2 scenes, the band names and the target STRDS names | 

### Return type

[**ProcessingResponseModel**](ProcessingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the Sentinel-2 time series import |  -  |
**400** | The error message and a detailed log why Sentinel 2A time series import did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sentinel2_process_gcs_ndvi_product_id_post**
> SentinelNDVIResponseModel sentinel2_process_gcs_ndvi_product_id_post(product_id)

NDVI computation of an arbitrary Sentinel-2 scene. The results are stored in the Google Cloud Storage.

NDVI computation of an arbitrary Sentinel-2 scene.The processing is as follows: A user specific Sentinel-2 scene (Bands 04 and 08)will be download and imported into an ephemeral database.. The NDVI will be computed via r.mapcalc. The result of the computation is available as gzipped geotiff file. In addition, the univariate statistic will be computed as well as a preview image including a legend and scale. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.sentinel_ndvi_response_model import SentinelNDVIResponseModel
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
    api_instance = actinia_openapi_python_client.SatelliteImageAlgorithmsApi(api_client)
    product_id = 'S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138' # str | The product id of a sentinel scene (default to 'S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138')

    try:
        # NDVI computation of an arbitrary Sentinel-2 scene. The results are stored in the Google Cloud Storage.
        api_response = api_instance.sentinel2_process_gcs_ndvi_product_id_post(product_id)
        print("The response of SatelliteImageAlgorithmsApi->sentinel2_process_gcs_ndvi_product_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SatelliteImageAlgorithmsApi->sentinel2_process_gcs_ndvi_product_id_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The product id of a sentinel scene | [default to &#39;S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138&#39;]

### Return type

[**SentinelNDVIResponseModel**](SentinelNDVIResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response includes all created resources as URL as well as the processing log and other metadata. |  -  |
**400** | The error message and a detailed log why NDVI processing of a sentinel2 scene did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sentinel2_process_ndvi_product_id_post**
> SentinelNDVIResponseModel sentinel2_process_ndvi_product_id_post(product_id)

NDVI computation of an arbitrary Sentinel-2 scene.

NDVI computation of an arbitrary Sentinel-2 scene.The processing is as follows: A user specific Sentinel-2 scene (Bands 04 and 08)will be download and imported into an ephemeral database.. The NDVI will be computed via r.mapcalc. The result of the computation is available as gzipped geotiff file. In addition, the univariate statistic will be computed as well as a preview image including a legend and scale. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.sentinel_ndvi_response_model import SentinelNDVIResponseModel
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
    api_instance = actinia_openapi_python_client.SatelliteImageAlgorithmsApi(api_client)
    product_id = 'S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138' # str | The product id of a sentinel scene (default to 'S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138')

    try:
        # NDVI computation of an arbitrary Sentinel-2 scene.
        api_response = api_instance.sentinel2_process_ndvi_product_id_post(product_id)
        print("The response of SatelliteImageAlgorithmsApi->sentinel2_process_ndvi_product_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SatelliteImageAlgorithmsApi->sentinel2_process_ndvi_product_id_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The product id of a sentinel scene | [default to &#39;S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138&#39;]

### Return type

[**SentinelNDVIResponseModel**](SentinelNDVIResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response includes all created resources as URL as well as the processing log and other metadata. |  -  |
**400** | The error message and a detailed log why NDVI processing of a sentinel2 scene did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sentinel2_query_get**
> SatelliteSceneList sentinel2_query_get(scene_id=scene_id, start_time=start_time, end_time=end_time, lon=lon, lat=lat, cloud_covert=cloud_covert)

Query the Google Sentinel2 archives using time interval, lat/lon coordinates, scene id and cloud cover.

Query the Google Sentinel2 archives using time interval, lat/lon coordinates, scene id and cloud cover. All scenes that are located within the time interval and that intersect the given latitude/longitude coordinates are returned as a list of scene names with associated time stamps. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.satellite_scene_list import SatelliteSceneList
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
    api_instance = actinia_openapi_python_client.SatelliteImageAlgorithmsApi(api_client)
    scene_id = 'scene_id_example' # str | The scene id also named product id of the Sentinel2A scenes that should be searched (optional)
    start_time = 'start_time_example' # str | The start time of the search interval (optional)
    end_time = 'end_time_example' # str | The end time of the search interval (optional)
    lon = 3.4 # float | The longitude coordinate with which the scenes should intersect (optional)
    lat = 3.4 # float | The latitude coordinate with which the scenes should intersect (optional)
    cloud_covert = 3.4 # float | Cloud cover between 0 - 100 (optional)

    try:
        # Query the Google Sentinel2 archives using time interval, lat/lon coordinates, scene id and cloud cover.
        api_response = api_instance.sentinel2_query_get(scene_id=scene_id, start_time=start_time, end_time=end_time, lon=lon, lat=lat, cloud_covert=cloud_covert)
        print("The response of SatelliteImageAlgorithmsApi->sentinel2_query_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SatelliteImageAlgorithmsApi->sentinel2_query_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **str**| The scene id also named product id of the Sentinel2A scenes that should be searched | [optional] 
 **start_time** | **str**| The start time of the search interval | [optional] 
 **end_time** | **str**| The end time of the search interval | [optional] 
 **lon** | **float**| The longitude coordinate with which the scenes should intersect | [optional] 
 **lat** | **float**| The latitude coordinate with which the scenes should intersect | [optional] 
 **cloud_covert** | **float**| Cloud cover between 0 - 100 | [optional] 

### Return type

[**SatelliteSceneList**](SatelliteSceneList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of satellite scenes that fit the search |  -  |
**400** | The error message if the search did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sentinel2a_aws_query_post**
> Sentinel2ASceneList sentinel2a_aws_query_post(scenes)

Generate the download urls for a list of sentinel2A scenes and band numbers.

Generate the download urls for a list of sentinel2A scenes and band numbers. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.sentinel2_a_scene_list import Sentinel2ASceneList
from actinia_openapi_python_client.models.sentinel2_a_scene_list_model import Sentinel2ASceneListModel
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
    api_instance = actinia_openapi_python_client.SatelliteImageAlgorithmsApi(api_client)
    scenes = actinia_openapi_python_client.Sentinel2ASceneListModel() # Sentinel2ASceneListModel | The list of Sentinel-2 scenes and the band names

    try:
        # Generate the download urls for a list of sentinel2A scenes and band numbers.
        api_response = api_instance.sentinel2a_aws_query_post(scenes)
        print("The response of SatelliteImageAlgorithmsApi->sentinel2a_aws_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SatelliteImageAlgorithmsApi->sentinel2a_aws_query_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenes** | [**Sentinel2ASceneListModel**](Sentinel2ASceneListModel.md)| The list of Sentinel-2 scenes and the band names | 

### Return type

[**Sentinel2ASceneList**](Sentinel2ASceneList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the Sentinel-2 time series import |  -  |
**400** | The error message and a detailed log why Sentinel 2A scene download url creation did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

