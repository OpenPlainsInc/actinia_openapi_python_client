# actinia_openapi_python_client.UserManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](UserManagementApi.md#users_get) | **GET** /users | List all users in the database
[**users_user_id_delete**](UserManagementApi.md#users_user_id_delete) | **DELETE** /users/{user_id} | Delete a specific user
[**users_user_id_get**](UserManagementApi.md#users_user_id_get) | **GET** /users/{user_id} | Return the credentials of a single user
[**users_user_id_post**](UserManagementApi.md#users_user_id_post) | **POST** /users/{user_id} | Create a user in the database


# **users_get**
> UserListResponseModel users_get()

List all users in the database

Get a list of all users. Minimum required user role: admin.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.user_list_response_model import UserListResponseModel
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
    api_instance = actinia_openapi_python_client.UserManagementApi(api_client)

    try:
        # List all users in the database
        api_response = api_instance.users_get()
        print("The response of UserManagementApi->users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->users_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UserListResponseModel**](UserListResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns a list of user names. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> SimpleResponseModel users_user_id_delete(user_id)

Delete a specific user

Deletes a user. Minimum required user role: admin.

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
    api_instance = actinia_openapi_python_client.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique name of the user

    try:
        # Delete a specific user
        api_response = api_instance.users_user_id_delete(user_id)
        print("The response of UserManagementApi->users_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->users_user_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique name of the user | 

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
**200** | This response returns the status of user deletion. |  -  |
**400** | The error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> UserInfoResponseModel users_user_id_get(user_id)

Return the credentials of a single user

Get information about the group, role and permissions of a certain user. Minimum required user role: admin.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import actinia_openapi_python_client
from actinia_openapi_python_client.models.user_info_response_model import UserInfoResponseModel
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
    api_instance = actinia_openapi_python_client.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique name of the user

    try:
        # Return the credentials of a single user
        api_response = api_instance.users_user_id_get(user_id)
        print("The response of UserManagementApi->users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->users_user_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique name of the user | 

### Return type

[**UserInfoResponseModel**](UserInfoResponseModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response returns information about a certain user. |  -  |
**400** | The error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_post**
> SimpleResponseModel users_user_id_post(user_id, password, group)

Create a user in the database

Creates a new user in the database. Minimum required user role: admin.

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
    api_instance = actinia_openapi_python_client.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique name of the user
    password = 'password_example' # str | The password of the new user
    group = 'group_example' # str | The group of the new user

    try:
        # Create a user in the database
        api_response = api_instance.users_user_id_post(user_id, password, group)
        print("The response of UserManagementApi->users_user_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->users_user_id_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique name of the user | 
 **password** | **str**| The password of the new user | 
 **group** | **str**| The group of the new user | 

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
**200** | This response returns the status of user creation. |  -  |
**400** | The error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

