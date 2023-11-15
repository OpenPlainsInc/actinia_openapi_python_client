# actinia_openapi_python_client.STACApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stac_catalogs_catalog_json_get**](STACApi.md#stac_catalogs_catalog_json_get) | **GET** /stac/catalogs/catalog.json | Get a list of all instances.
[**stac_collections_get**](STACApi.md#stac_collections_get) | **GET** /stac/collections | Get a list of all Collection.
[**stac_collections_post**](STACApi.md#stac_collections_post) | **POST** /stac/collections | Add a new stac to the user collection
[**stac_collections_stac_collection_id_delete**](STACApi.md#stac_collections_stac_collection_id_delete) | **DELETE** /stac/collections/{stac_collection_id} | This function deletes the STAC collection with the given id.
[**stac_collections_stac_collection_id_get**](STACApi.md#stac_collections_stac_collection_id_get) | **GET** /stac/collections/{stac_collection_id} | Get a list of specified Collection.
[**stac_get**](STACApi.md#stac_get) | **GET** /stac | Get a list of instances and its notation.
[**stac_instances_get**](STACApi.md#stac_instances_get) | **GET** /stac/instances | Get a list of all instances.
[**stac_instances_post**](STACApi.md#stac_instances_post) | **POST** /stac/instances | Add a new stac to the user collection
[**stac_instances_stac_instance_id_delete**](STACApi.md#stac_instances_stac_instance_id_delete) | **DELETE** /stac/instances/{stac_instance_id} | This function delete the STAC Collection stored before on ID basis.
[**stac_instances_stac_instance_id_get**](STACApi.md#stac_instances_stac_instance_id_get) | **GET** /stac/instances/{stac_instance_id} | Get a list of collection that are inside a instance and its notation.


# **stac_catalogs_catalog_json_get**
> stac_catalogs_catalog_json_get()

Get a list of all instances.

Get a list of STAC result-catalog. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STACApi(api_client)

    try:
        # Get a list of all instances.
        api_instance.stac_catalogs_catalog_json_get()
    except Exception as e:
        print("Exception when calling STACApi->stac_catalogs_catalog_json_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of STAC catalogs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_collections_get**
> stac_collections_get()

Get a list of all Collection.

Get a list of STAC collectionsMinimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STACApi(api_client)

    try:
        # Get a list of all Collection.
        api_instance.stac_collections_get()
    except Exception as e:
        print("Exception when calling STACApi->stac_collections_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of STAC collections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_collections_post**
> stac_collections_post(body)

Add a new stac to the user collection

Add a new STAC collection to the user instance

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.stac_collections_post_request import StacCollectionsPostRequest
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
    api_instance = actinia_openapi_python_client.STACApi(api_client)
    body = actinia_openapi_python_client.StacCollectionsPostRequest() # StacCollectionsPostRequest | the instance id where the collection will be stored

    try:
        # Add a new stac to the user collection
        api_instance.stac_collections_post(body)
    except Exception as e:
        print("Exception when calling STACApi->stac_collections_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StacCollectionsPostRequest**](StacCollectionsPostRequest.md)| the instance id where the collection will be stored | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/gml+xml, application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a message with the STAC collection successfully added |  -  |
**400** | This response returns a detail error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_collections_stac_collection_id_delete**
> stac_collections_stac_collection_id_delete(stac_collection_id)

This function deletes the STAC collection with the given id.

Delete a new STAC collection to the user instance

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
    api_instance = actinia_openapi_python_client.STACApi(api_client)
    stac_collection_id = 'stac_collection_id_example' # str | the STAC collection id of the collection to be deleted

    try:
        # This function deletes the STAC collection with the given id.
        api_instance.stac_collections_stac_collection_id_delete(stac_collection_id)
    except Exception as e:
        print("Exception when calling STACApi->stac_collections_stac_collection_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stac_collection_id** | **str**| the STAC collection id of the collection to be deleted | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a message with the STAC collection successfully deleted |  -  |
**400** | This response returns a detail error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_collections_stac_collection_id_get**
> stac_collections_stac_collection_id_get(stac_collection_id)

Get a list of specified Collection.

Get the STAC collection with the id given Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STACApi(api_client)
    stac_collection_id = 'stac_collection_id_example' # str | the STAC collection id of the collection to be obtained

    try:
        # Get a list of specified Collection.
        api_instance.stac_collections_stac_collection_id_get(stac_collection_id)
    except Exception as e:
        print("Exception when calling STACApi->stac_collections_stac_collection_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stac_collection_id** | **str**| the STAC collection id of the collection to be obtained | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a STAC collection |  -  |
**400** | This response returns a detail error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_get**
> stac_get()

Get a list of instances and its notation.

Get a list of STAC instances. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STACApi(api_client)

    try:
        # Get a list of instances and its notation.
        api_instance.stac_get()
    except Exception as e:
        print("Exception when calling STACApi->stac_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of STAC instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_instances_get**
> stac_instances_get()

Get a list of all instances.

Get a list of STAC instances. Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STACApi(api_client)

    try:
        # Get a list of all instances.
        api_instance.stac_instances_get()
    except Exception as e:
        print("Exception when calling STACApi->stac_instances_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of STAC instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_instances_post**
> stac_instances_post(body)

Add a new stac to the user collection

Add a new STAC instances to the user

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.stac_instances_post_request import StacInstancesPostRequest
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
    api_instance = actinia_openapi_python_client.STACApi(api_client)
    body = actinia_openapi_python_client.StacInstancesPostRequest() # StacInstancesPostRequest | the instance id where the collection will be stored

    try:
        # Add a new stac to the user collection
        api_instance.stac_instances_post(body)
    except Exception as e:
        print("Exception when calling STACApi->stac_instances_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StacInstancesPostRequest**](StacInstancesPostRequest.md)| the instance id where the collection will be stored | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/gml+xml, application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a message with the instance successfully added |  -  |
**400** | This response returns a detail error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_instances_stac_instance_id_delete**
> stac_instances_stac_instance_id_delete(stac_instance_id)

This function delete the STAC Collection stored before on ID basis.

Delete an instance

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
    api_instance = actinia_openapi_python_client.STACApi(api_client)
    stac_instance_id = 'stac_instance_id_example' # str | the instance id to be deleted (All collections will be removed)

    try:
        # This function delete the STAC Collection stored before on ID basis.
        api_instance.stac_instances_stac_instance_id_delete(stac_instance_id)
    except Exception as e:
        print("Exception when calling STACApi->stac_instances_stac_instance_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stac_instance_id** | **str**| the instance id to be deleted (All collections will be removed) | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a message with the instance and the STAC collections deleted |  -  |
**400** | This response returns a detail error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stac_instances_stac_instance_id_get**
> stac_instances_stac_instance_id_get(stac_instance_id)

Get a list of collection that are inside a instance and its notation.

Get the instance with the id given Minimum required user role: user.

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
    api_instance = actinia_openapi_python_client.STACApi(api_client)
    stac_instance_id = 'stac_instance_id_example' # str | the instance id of the collection to be obtained

    try:
        # Get a list of collection that are inside a instance and its notation.
        api_instance.stac_instances_stac_instance_id_get(stac_instance_id)
    except Exception as e:
        print("Exception when calling STACApi->stac_instances_stac_instance_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stac_instance_id** | **str**| the instance id of the collection to be obtained | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a instance with its collections |  -  |
**400** | This response returns a detail error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

