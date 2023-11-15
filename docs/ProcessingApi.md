# actinia_openapi_python_client.ProcessingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_location_name_mapsets_mapset_name_processing_async_post**](ProcessingApi.md#locations_location_name_mapsets_mapset_name_processing_async_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/processing_async | Execute a user defined process chain that creates a new mapset or
[**locations_location_name_mapsets_mapset_name_processing_post**](ProcessingApi.md#locations_location_name_mapsets_mapset_name_processing_post) | **POST** /locations/{location_name}/mapsets/{mapset_name}/processing | Execute a user defined process chain that creates a new mapset or
[**locations_location_name_process_chain_validation_async_post**](ProcessingApi.md#locations_location_name_process_chain_validation_async_post) | **POST** /locations/{location_name}/process_chain_validation_async | Validate a process chain asynchronously, check the provided sources
[**locations_location_name_process_chain_validation_sync_post**](ProcessingApi.md#locations_location_name_process_chain_validation_sync_post) | **POST** /locations/{location_name}/process_chain_validation_sync | Validate a process chain synchronously, check the provided sources
[**locations_location_name_processing_async_export_gcs_post**](ProcessingApi.md#locations_location_name_processing_async_export_gcs_post) | **POST** /locations/{location_name}/processing_async_export_gcs | Execute a user defined process chain in an ephemeral location/mapset
[**locations_location_name_processing_async_export_post**](ProcessingApi.md#locations_location_name_processing_async_export_post) | **POST** /locations/{location_name}/processing_async_export | Execute a user defined process chain in an ephemeral location/mapset
[**locations_location_name_processing_async_export_s3_post**](ProcessingApi.md#locations_location_name_processing_async_export_s3_post) | **POST** /locations/{location_name}/processing_async_export_s3 | Execute a user defined process chain in an ephemeral location/mapset
[**locations_location_name_processing_export_post**](ProcessingApi.md#locations_location_name_processing_export_post) | **POST** /locations/{location_name}/processing_export | Execute a user defined process chain in an ephemeral location/mapset


# **locations_location_name_mapsets_mapset_name_processing_async_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_processing_async_post(location_name, mapset_name, process_chain)

Execute a user defined process chain that creates a new mapset or

Execute a user defined process chain in an existing mapset of the persistent user database or in a new mapset that will be created by this request in the persistent user database.  The process chain is executed asynchronously. The provided status URL in the response must be polled to gain information about the processing progress and finishing status.  **Note**      Space-time dataset processing can only be performed in a new mapset     that is created by this resource call, since merging of temporal databases     of different mapsets is not supported yet.  The mapset that is used for processing will be locked until the process chain execution finished (successfully or not), even if the mapset is be created by the request. Other requests on the locked mapset will abort with a mapset lock error.  The persistent user database will not be modified if the process chain does not run successfully. The processing is performed in an ephemeral database and then merged or copied into the persistent user database.  **Note**      Make sure that the process chain definition identifies all raster, vector     or space time datasets correctly with name and mapset: name@mapset.      All required mapsets will be identified by analysing the input parameter     of all module descriptions in the provided process chain     and mounted into the ephemeral database that is used for processing.  

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
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
    api_instance = actinia_openapi_python_client.ProcessingApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'mapset_name_example' # str | The name of an existing mapset or a new mapset that should be created
    process_chain = actinia_openapi_python_client.ProcessChainModel() # ProcessChainModel | The process chain that should be executed

    try:
        # Execute a user defined process chain that creates a new mapset or
        api_response = api_instance.locations_location_name_mapsets_mapset_name_processing_async_post(location_name, mapset_name, process_chain)
        print("The response of ProcessingApi->locations_location_name_mapsets_mapset_name_processing_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->locations_location_name_mapsets_mapset_name_processing_async_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of an existing mapset or a new mapset that should be created | 
 **process_chain** | [**ProcessChainModel**](ProcessChainModel.md)| The process chain that should be executed | 

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
**200** | The result of the process chain execution |  -  |
**400** | The error message and a detailed log why process chain execution did not succeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_mapsets_mapset_name_processing_post**
> ProcessingResponseModel locations_location_name_mapsets_mapset_name_processing_post(location_name, mapset_name, process_chain)

Execute a user defined process chain that creates a new mapset or

Execute a user defined process chain in an existing mapset of the persistent user database or in a new mapset that will be created by this request in the persistent user database.  The process chain is executed asynchronously. The provided status URL in the response must be polled to gain information about the processing progress and finishing status.  **Note**      Space-time dataset processing can only be performed in a new mapset     that is created by this resource call, since merging of temporal databases     of different mapsets is not supported yet.  The mapset that is used for processing will be locked until the process chain execution finished (successfully or not), even if the mapset is be created by the request. Other requests on the locked mapset will abort with a mapset lock error.  The persistent user database will not be modified if the process chain does not run successfully. The processing is performed in an ephemeral database and then merged or copied into the persistent user database.  **Note**      Make sure that the process chain definition identifies all raster, vector     or space time datasets correctly with name and mapset: name@mapset.      All required mapsets will be identified by analysing the input parameter     of all module descriptions in the provided process chain     and mounted into the ephemeral database that is used for processing.  

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
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
    api_instance = actinia_openapi_python_client.ProcessingApi(api_client)
    location_name = 'nc_spm_08' # str | The location name (default to 'nc_spm_08')
    mapset_name = 'mapset_name_example' # str | The name of an existing mapset or a new mapset that should be created
    process_chain = actinia_openapi_python_client.ProcessChainModel() # ProcessChainModel | The process chain that should be executed

    try:
        # Execute a user defined process chain that creates a new mapset or
        api_response = api_instance.locations_location_name_mapsets_mapset_name_processing_post(location_name, mapset_name, process_chain)
        print("The response of ProcessingApi->locations_location_name_mapsets_mapset_name_processing_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->locations_location_name_mapsets_mapset_name_processing_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name | [default to &#39;nc_spm_08&#39;]
 **mapset_name** | **str**| The name of an existing mapset or a new mapset that should be created | 
 **process_chain** | [**ProcessChainModel**](ProcessChainModel.md)| The process chain that should be executed | 

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
**200** | The result of the process chain execution |  -  |
**400** | The error message and a detailed log why process chain execution did not succeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_process_chain_validation_async_post**
> ProcessingResponseModel locations_location_name_process_chain_validation_async_post(location_name, process_chain)

Validate a process chain asynchronously, check the provided sources

Validate a process chain, check the provided sources (links) and the mapsets. The list of processes that were checked by Actinia are returned in the JSON response. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
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
    api_instance = actinia_openapi_python_client.ProcessingApi(api_client)
    location_name = 'nc_spm_08' # str | The location name that contains the data that should be used in the process chain (default to 'nc_spm_08')
    process_chain = actinia_openapi_python_client.ProcessChainModel() # ProcessChainModel | The process chain that should be validated

    try:
        # Validate a process chain asynchronously, check the provided sources
        api_response = api_instance.locations_location_name_process_chain_validation_async_post(location_name, process_chain)
        print("The response of ProcessingApi->locations_location_name_process_chain_validation_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->locations_location_name_process_chain_validation_async_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name that contains the data that should be used in the process chain | [default to &#39;nc_spm_08&#39;]
 **process_chain** | [**ProcessChainModel**](ProcessChainModel.md)| The process chain that should be validated | 

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
**200** | The result of the process chain validation. A list of processes that will be executed by Actinia Core |  -  |
**400** | The error message and a detailed log why process chain validation did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_process_chain_validation_sync_post**
> ProcessingResponseModel locations_location_name_process_chain_validation_sync_post(location_name, process_chain)

Validate a process chain synchronously, check the provided sources

Validate a process chain, check the provided sources (links) and the mapsets. The list of processes that were checked by Actinia are returned in the JSON response. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
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
    api_instance = actinia_openapi_python_client.ProcessingApi(api_client)
    location_name = 'nc_spm_08' # str | The location name that contains the data that should be used in the process chain (default to 'nc_spm_08')
    process_chain = actinia_openapi_python_client.ProcessChainModel() # ProcessChainModel | The process chain that should be validated

    try:
        # Validate a process chain synchronously, check the provided sources
        api_response = api_instance.locations_location_name_process_chain_validation_sync_post(location_name, process_chain)
        print("The response of ProcessingApi->locations_location_name_process_chain_validation_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->locations_location_name_process_chain_validation_sync_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name that contains the data that should be used in the process chain | [default to &#39;nc_spm_08&#39;]
 **process_chain** | [**ProcessChainModel**](ProcessChainModel.md)| The process chain that should be validated | 

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
**200** | The result of the process chain validation. A list of processes that will be executed by Actinia Core |  -  |
**400** | The error message and a detailed log why process chain validation did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_processing_async_export_gcs_post**
> ProcessingResponseModel locations_location_name_processing_async_export_gcs_post(location_name, process_chain)

Execute a user defined process chain in an ephemeral location/mapset

Execute a user defined process chain in an ephemeral database and provide the generated resources as downloadable files via URL's. Minimum required user role: user.  The process chain is executed asynchronously. The provided status URL in the response must be polled to gain information about the processing progress and finishing status.  **Note**      Make sure that the process chain definition identifies all raster, vector     or space-time datasets correctly with name and mapset: name@mapset if you     use data from other mapsets in the specified location.      All required mapsets will be identified by analysing the input parameter     of all module descriptions in the provided process chain and     mounted read-only into the ephemeral database that is used for processing.  The persistent database will not be modified. The ephemeral database will be removed after processing. Use the URL's provided in the finished response to download the resource that were specified in the process chain for export.  This endpoint also allows the creation of STAC ITEMS through the ACTINIA STAC PLUGIN. The STAC item is stored in a dedicated CATALOG following the standard from STAC specification (https://stacspec.org/). 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
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
    api_instance = actinia_openapi_python_client.ProcessingApi(api_client)
    location_name = 'nc_spm_08' # str | The location name that contains the data that should be processed (default to 'nc_spm_08')
    process_chain = actinia_openapi_python_client.ProcessChainModel() # ProcessChainModel | The process chain that should be executed

    try:
        # Execute a user defined process chain in an ephemeral location/mapset
        api_response = api_instance.locations_location_name_processing_async_export_gcs_post(location_name, process_chain)
        print("The response of ProcessingApi->locations_location_name_processing_async_export_gcs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->locations_location_name_processing_async_export_gcs_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name that contains the data that should be processed | [default to &#39;nc_spm_08&#39;]
 **process_chain** | [**ProcessChainModel**](ProcessChainModel.md)| The process chain that should be executed | 

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
**200** | The result of the process chain execution |  -  |
**400** | The error message and a detailed log why process chain execution did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_processing_async_export_post**
> ProcessingResponseModel locations_location_name_processing_async_export_post(location_name, process_chain)

Execute a user defined process chain in an ephemeral location/mapset

Execute a user defined process chain in an ephemeral database and provide the generated resources as downloadable files via URL's. Minimum required user role: user.  The process chain is executed asynchronously. The provided status URL in the response must be polled to gain information about the processing progress and finishing status.  **Note**      Make sure that the process chain definition identifies all raster, vector     or space-time datasets correctly with name and mapset: name@mapset if you     use data from other mapsets in the specified location.      All required mapsets will be identified by analysing the input parameter     of all module descriptions in the provided process chain and     mounted read-only into the ephemeral database that is used for processing.  The persistent database will not be modified. The ephemeral database will be removed after processing. Use the URL's provided in the finished response to download the resource that were specified in the process chain for export.  This endpoint also allows the creation of STAC ITEMS through the ACTINIA STAC PLUGIN. The STAC item is stored in a dedicated CATALOG following the standard from STAC specification (https://stacspec.org/). 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
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
    api_instance = actinia_openapi_python_client.ProcessingApi(api_client)
    location_name = 'nc_spm_08' # str | The location name that contains the data that should be processed (default to 'nc_spm_08')
    process_chain = actinia_openapi_python_client.ProcessChainModel() # ProcessChainModel | The process chain that should be executed

    try:
        # Execute a user defined process chain in an ephemeral location/mapset
        api_response = api_instance.locations_location_name_processing_async_export_post(location_name, process_chain)
        print("The response of ProcessingApi->locations_location_name_processing_async_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->locations_location_name_processing_async_export_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name that contains the data that should be processed | [default to &#39;nc_spm_08&#39;]
 **process_chain** | [**ProcessChainModel**](ProcessChainModel.md)| The process chain that should be executed | 

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
**200** | The result of the process chain execution |  -  |
**400** | The error message and a detailed log why process chain execution did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_processing_async_export_s3_post**
> ProcessingResponseModel locations_location_name_processing_async_export_s3_post(location_name, process_chain)

Execute a user defined process chain in an ephemeral location/mapset

Execute a user defined process chain in an ephemeral database and provide the generated resources as downloadable files via URL's. Minimum required user role: user.  The process chain is executed asynchronously. The provided status URL in the response must be polled to gain information about the processing progress and finishing status.  **Note**      Make sure that the process chain definition identifies all raster, vector     or space-time datasets correctly with name and mapset: name@mapset if you     use data from other mapsets in the specified location.      All required mapsets will be identified by analysing the input parameter     of all module descriptions in the provided process chain and     mounted read-only into the ephemeral database that is used for processing.  The persistent database will not be modified. The ephemeral database will be removed after processing. Use the URL's provided in the finished response to download the resource that were specified in the process chain for export.  This endpoint also allows the creation of STAC ITEMS through the ACTINIA STAC PLUGIN. The STAC item is stored in a dedicated CATALOG following the standard from STAC specification (https://stacspec.org/). 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
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
    api_instance = actinia_openapi_python_client.ProcessingApi(api_client)
    location_name = 'nc_spm_08' # str | The location name that contains the data that should be processed (default to 'nc_spm_08')
    process_chain = actinia_openapi_python_client.ProcessChainModel() # ProcessChainModel | The process chain that should be executed

    try:
        # Execute a user defined process chain in an ephemeral location/mapset
        api_response = api_instance.locations_location_name_processing_async_export_s3_post(location_name, process_chain)
        print("The response of ProcessingApi->locations_location_name_processing_async_export_s3_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->locations_location_name_processing_async_export_s3_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name that contains the data that should be processed | [default to &#39;nc_spm_08&#39;]
 **process_chain** | [**ProcessChainModel**](ProcessChainModel.md)| The process chain that should be executed | 

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
**200** | The result of the process chain execution |  -  |
**400** | The error message and a detailed log why process chain execution did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_location_name_processing_export_post**
> ProcessingResponseModel locations_location_name_processing_export_post(location_name, process_chain)

Execute a user defined process chain in an ephemeral location/mapset

Execute a user defined process chain in an ephemeral database and provide the generated resources as downloadable files via URL's. Minimum required user role: user.  The process chain is executed asynchronously. The provided status URL in the response must be polled to gain information about the processing progress and finishing status.  **Note**      Make sure that the process chain definition identifies all raster, vector     or space-time datasets correctly with name and mapset: name@mapset if you     use data from other mapsets in the specified location.      All required mapsets will be identified by analysing the input parameter     of all module descriptions in the provided process chain and     mounted read-only into the ephemeral database that is used for processing.  The persistent database will not be modified. The ephemeral database will be removed after processing. Use the URL's provided in the finished response to download the resource that were specified in the process chain for export.  This endpoint also allows the creation of STAC ITEMS through the ACTINIA STAC PLUGIN. The STAC item is stored in a dedicated CATALOG following the standard from STAC specification (https://stacspec.org/). 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
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
    api_instance = actinia_openapi_python_client.ProcessingApi(api_client)
    location_name = 'nc_spm_08' # str | The location name that contains the data that should be processed (default to 'nc_spm_08')
    process_chain = actinia_openapi_python_client.ProcessChainModel() # ProcessChainModel | The process chain that should be executed

    try:
        # Execute a user defined process chain in an ephemeral location/mapset
        api_response = api_instance.locations_location_name_processing_export_post(location_name, process_chain)
        print("The response of ProcessingApi->locations_location_name_processing_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->locations_location_name_processing_export_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name that contains the data that should be processed | [default to &#39;nc_spm_08&#39;]
 **process_chain** | [**ProcessChainModel**](ProcessChainModel.md)| The process chain that should be executed | 

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
**200** | The result of the process chain execution |  -  |
**400** | The error message and a detailed log why process chain execution did not succeeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

