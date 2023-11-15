# actinia_openapi_python_client.GeoNetworkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_geodata_tags_tags_get**](GeoNetworkApi.md#metadata_geodata_tags_tags_get) | **GET** /metadata/geodata/tags/{tags} | Get geodata object from requests to Geonetwork opensource by one or many tags.
[**metadata_geodata_uuids_uuid_get**](GeoNetworkApi.md#metadata_geodata_uuids_uuid_get) | **GET** /metadata/geodata/uuids/{uuid} | Get geodata object from requests to Geonetwork opensource by uuid.
[**metadata_raw_categories_category_get**](GeoNetworkApi.md#metadata_raw_categories_category_get) | **GET** /metadata/raw/categories/{category} | Requests a category from Geonetwork opensource.
[**metadata_raw_tags_tags_get**](GeoNetworkApi.md#metadata_raw_tags_tags_get) | **GET** /metadata/raw/tags/{tags} | Requests one or many tags from Geonetwork opensource.
[**metadata_raw_uuids_uuid_get**](GeoNetworkApi.md#metadata_raw_uuids_uuid_get) | **GET** /metadata/raw/uuids/{uuid} | Requests an uuid from Geonetwork opensource.
[**metadata_test_connection_get**](GeoNetworkApi.md#metadata_test_connection_get) | **GET** /metadata/test/connection | Tests for active connection to Geonetwork opensource.
[**metadata_test_connection_post**](GeoNetworkApi.md#metadata_test_connection_post) | **POST** /metadata/test/connection | Tests for active connection to Geonetwork opensource.


# **metadata_geodata_tags_tags_get**
> GeodataResponseModel metadata_geodata_tags_tags_get(tags)

Get geodata object from requests to Geonetwork opensource by one or many tags.

The request will ask Geonetwork which metadata records are available for a certain tag or more tags separated by comma and returns a parsed record build from model. At the moment only the first record is returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.geodata_response_model import GeodataResponseModel
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
    api_instance = actinia_openapi_python_client.GeoNetworkApi(api_client)
    tags = 'tags_example' # str | One or more Geonetwork tags, comma separated

    try:
        # Get geodata object from requests to Geonetwork opensource by one or many tags.
        api_response = api_instance.metadata_geodata_tags_tags_get(tags)
        print("The response of GeoNetworkApi->metadata_geodata_tags_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoNetworkApi->metadata_geodata_tags_tags_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| One or more Geonetwork tags, comma separated | 

### Return type

[**GeodataResponseModel**](GeodataResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modelled Search Results from Geonetwork |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_geodata_uuids_uuid_get**
> GeodataResponseModel metadata_geodata_uuids_uuid_get(uuid)

Get geodata object from requests to Geonetwork opensource by uuid.

The request will ask Geonetwork which metadata records are available for a certain uuid and returns a parsed record build from model. At the moment only the first record is returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.geodata_response_model import GeodataResponseModel
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
    api_instance = actinia_openapi_python_client.GeoNetworkApi(api_client)
    uuid = 'uuid_example' # str | A Geonetwork uuid from a record

    try:
        # Get geodata object from requests to Geonetwork opensource by uuid.
        api_response = api_instance.metadata_geodata_uuids_uuid_get(uuid)
        print("The response of GeoNetworkApi->metadata_geodata_uuids_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoNetworkApi->metadata_geodata_uuids_uuid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A Geonetwork uuid from a record | 

### Return type

[**GeodataResponseModel**](GeodataResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modelled Search Results from Geonetwork |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_raw_categories_category_get**
> object metadata_raw_categories_category_get(category)

Requests a category from Geonetwork opensource.

The request will ask Geonetwork which metadata records are available for a certain category and returns the JSON response with these records. Requirement: a virtual CSW is defined in Geonetwork

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
    api_instance = actinia_openapi_python_client.GeoNetworkApi(api_client)
    category = 'category_example' # str | A Geonetwork category

    try:
        # Requests a category from Geonetwork opensource.
        api_response = api_instance.metadata_raw_categories_category_get(category)
        print("The response of GeoNetworkApi->metadata_raw_categories_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoNetworkApi->metadata_raw_categories_category_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| A Geonetwork category | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Search Results from Geonetwork |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_raw_tags_tags_get**
> object metadata_raw_tags_tags_get(tags)

Requests one or many tags from Geonetwork opensource.

The request will ask Geonetwork which metadata records are available for a certain tag or more tags separated by comma and returns the JSON response with these records.

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
    api_instance = actinia_openapi_python_client.GeoNetworkApi(api_client)
    tags = 'tags_example' # str | One or more Geonetwork tags, comma separated

    try:
        # Requests one or many tags from Geonetwork opensource.
        api_response = api_instance.metadata_raw_tags_tags_get(tags)
        print("The response of GeoNetworkApi->metadata_raw_tags_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoNetworkApi->metadata_raw_tags_tags_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| One or more Geonetwork tags, comma separated | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Search Results from Geonetwork |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_raw_uuids_uuid_get**
> object metadata_raw_uuids_uuid_get(uuid)

Requests an uuid from Geonetwork opensource.

The request will ask Geonetwork which metadata records are available for a certain uuid and returns the JSON response with this record.

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
    api_instance = actinia_openapi_python_client.GeoNetworkApi(api_client)
    uuid = 'uuid_example' # str | A Geonetwork uuid from a record

    try:
        # Requests an uuid from Geonetwork opensource.
        api_response = api_instance.metadata_raw_uuids_uuid_get(uuid)
        print("The response of GeoNetworkApi->metadata_raw_uuids_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoNetworkApi->metadata_raw_uuids_uuid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A Geonetwork uuid from a record | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Search Results from Geonetwork |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_test_connection_get**
> SimpleStatusCodeResponseModel metadata_test_connection_get()

Tests for active connection to Geonetwork opensource.

The request will ask the backend if it can successfully connect to Geonetwork.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.simple_status_code_response_model import SimpleStatusCodeResponseModel
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
    api_instance = actinia_openapi_python_client.GeoNetworkApi(api_client)

    try:
        # Tests for active connection to Geonetwork opensource.
        api_response = api_instance.metadata_test_connection_get()
        print("The response of GeoNetworkApi->metadata_test_connection_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoNetworkApi->metadata_test_connection_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SimpleStatusCodeResponseModel**](SimpleStatusCodeResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or failure of connection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_test_connection_post**
> SimpleStatusCodeResponseModel metadata_test_connection_post()

Tests for active connection to Geonetwork opensource.

The request will ask the backend if it can successfully connect to Geonetwork.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.simple_status_code_response_model import SimpleStatusCodeResponseModel
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
    api_instance = actinia_openapi_python_client.GeoNetworkApi(api_client)

    try:
        # Tests for active connection to Geonetwork opensource.
        api_response = api_instance.metadata_test_connection_post()
        print("The response of GeoNetworkApi->metadata_test_connection_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoNetworkApi->metadata_test_connection_post: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SimpleStatusCodeResponseModel**](SimpleStatusCodeResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or failure of connection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

