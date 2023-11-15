# actinia_openapi_python_client.VectorSamplingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_async_post**](VectorSamplingApi.md#locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_async_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/vector_layers/{vector_name}/sampling_async | Perform vector map sampling on a vector map layer based on input
[**locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_sync_post**](VectorSamplingApi.md#locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_sync_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/vector_layers/{vector_name}/sampling_sync | Perform vector map sampling on a vector map layer based on input


# **locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_async_post**
> VectorSamplingResponseModel locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_async_post(location_name, mapset_name, vector_name, points)

Perform vector map sampling on a vector map layer based on input

Spatial sampling of a vector dataset with vector points. The vector points must be in the same coordinate reference system as the location that contains the vector dataset. The result of the sampling is located in the resource response JSON document after the processing was finished, as a list of values for each vector point. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.point_list_model import PointListModel
from actinia_openapi_python_client.models.vector_sampling_response_model import VectorSamplingResponseModel
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
    api_instance = actinia_openapi_python_client.VectorSamplingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required vector map layer
    vector_name = 'vector_name_example' # str | The name of the vector map layer to perform the vector map sampling from
    points = actinia_openapi_python_client.PointListModel() # PointListModel | The sampling point array [[id, x, y],[id, x, y]]. The coordinates of the sampling points must be in the same coordinate reference system as the location that contains the vector dataset.

    try:
        # Perform vector map sampling on a vector map layer based on input
        api_response = api_instance.locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_async_post(location_name, mapset_name, vector_name, points)
        print("The response of VectorSamplingApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorSamplingApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_async_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required vector map layer | 
 **vector_name** | **str**| The name of the vector map layer to perform the vector map sampling from | 
 **points** | [**PointListModel**](PointListModel.md)| The sampling point array [[id, x, y],[id, x, y]]. The coordinates of the sampling points must be in the same coordinate reference system as the location that contains the vector dataset. | 

### Return type

[**VectorSamplingResponseModel**](VectorSamplingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the vector map sampling |  -  |
**400** | The error message and a detailed log why vector sampling did not succeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_sync_post**
> VectorSamplingResponseModel locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_sync_post(location_name, mapset_name, vector_name, points)

Perform vector map sampling on a vector map layer based on input

Spatial sampling of a vector dataset with vector points. The vector points must be in the same coordinate reference system as the location that contains the vector dataset. The result of the sampling is located in the resource response JSON document after the processing was finished, as a list of values for each vector point. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.point_list_model import PointListModel
from actinia_openapi_python_client.models.vector_sampling_response_model import VectorSamplingResponseModel
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
    api_instance = actinia_openapi_python_client.VectorSamplingApi(api_client)
    location_name = 'location_name_example' # str | The location name
    mapset_name = 'mapset_name_example' # str | The name of the mapset that contains the required vector map layer
    vector_name = 'vector_name_example' # str | The name of the vector map layer to perform the vector map sampling from
    points = actinia_openapi_python_client.PointListModel() # PointListModel | The sampling point array [[id, x, y],[id, x, y]]. The coordinates of the sampling points must be in the same coordinate reference system as the location that contains the vector dataset.

    try:
        # Perform vector map sampling on a vector map layer based on input
        api_response = api_instance.locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_sync_post(location_name, mapset_name, vector_name, points)
        print("The response of VectorSamplingApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorSamplingApi->locations_location_name_mapsets_mapset_name_vector_layers_vector_name_sampling_sync_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | 
 **mapset_name** | **str**| The name of the mapset that contains the required vector map layer | 
 **vector_name** | **str**| The name of the vector map layer to perform the vector map sampling from | 
 **points** | [**PointListModel**](PointListModel.md)| The sampling point array [[id, x, y],[id, x, y]]. The coordinates of the sampling points must be in the same coordinate reference system as the location that contains the vector dataset. | 

### Return type

[**VectorSamplingResponseModel**](VectorSamplingResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the vector map sampling |  -  |
**400** | The error message and a detailed log why vector sampling did not succeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

