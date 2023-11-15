# actinia_openapi_python_client.LocationManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_get**](LocationManagementApi.md#locations_get) | **GET** /locations | Get a list of all available locations
[**locations_location_name_delete**](LocationManagementApi.md#locations_location_name_delete) | **DELETE** /locations/{location_name} | Delete an existing location and everything inside from the user
[**locations_location_name_info_get**](LocationManagementApi.md#locations_location_name_info_get) | **GET** /locations/{location_name}/info | Get the location projection and current computational region of the
[**locations_location_name_post**](LocationManagementApi.md#locations_location_name_post) | **POST** /locations/{location_name} | Create a new location based on EPSG code in the user database.


# **locations_get**
> LocationListResponseModel locations_get()

Get a list of all available locations

Get a list of all available locations that are located in the GRASS database and the user has access to. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.location_list_response_model import LocationListResponseModel
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
    api_instance = actinia_openapi_python_client.LocationManagementApi(api_client)

    try:
        # Get a list of all available locations
        api_response = api_instance.locations_get()
        print("The response of LocationManagementApi->locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->locations_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**LocationListResponseModel**](LocationListResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of location names |  -  |
**400** | The error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_delete**
> SimpleResponseModel locations_location_name_delete(location_name)

Delete an existing location and everything inside from the user

Delete an existing location and everything inside from the user database. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.simple_response_model import SimpleResponseModel
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
    api_instance = actinia_openapi_python_client.LocationManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location to be deleted

    try:
        # Delete an existing location and everything inside from the user
        api_response = api_instance.locations_location_name_delete(location_name)
        print("The response of LocationManagementApi->locations_location_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->locations_location_name_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location to be deleted | 

### Return type

[**SimpleResponseModel**](SimpleResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success message for location deletion |  -  |
**400** | The error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_info_get**
> MapsetInfoResponseModel locations_location_name_info_get(location_name)

Get the location projection and current computational region of the

Get the location projection and current computational region of the PERMANENT mapset. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.LocationManagementApi(api_client)
    location_name = 'nc_spm_08' # str | The name of the location (default to 'nc_spm_08')

    try:
        # Get the location projection and current computational region of the
        api_response = api_instance.locations_location_name_info_get(location_name)
        print("The response of LocationManagementApi->locations_location_name_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->locations_location_name_info_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location | [default to &#39;nc_spm_08&#39;]

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
**200** | The location projection and current computational region of the PERMANENT mapset |  -  |
**400** | The error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_post**
> ProcessingResponseModel locations_location_name_post(location_name, epsg_code)

Create a new location based on EPSG code in the user database.

Create a new location based on EPSG code in the user database. Minimum required user role: user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.processing_response_model import ProcessingResponseModel
from actinia_openapi_python_client.models.projection_info_model import ProjectionInfoModel
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
    api_instance = actinia_openapi_python_client.LocationManagementApi(api_client)
    location_name = 'location_name_example' # str | The name of the location to be created
    epsg_code = actinia_openapi_python_client.ProjectionInfoModel() # ProjectionInfoModel | The EPSG code

    try:
        # Create a new location based on EPSG code in the user database.
        api_response = api_instance.locations_location_name_post(location_name, epsg_code)
        print("The response of LocationManagementApi->locations_location_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->locations_location_name_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The name of the location to be created | 
 **epsg_code** | [**ProjectionInfoModel**](ProjectionInfoModel.md)| The EPSG code | 

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
**200** | Create a new location based on EPSG code |  -  |
**400** | The error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

