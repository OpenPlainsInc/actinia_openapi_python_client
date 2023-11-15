# SentinelNDVIResponseModel

The response of the Sentinel2A vegetation index computation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the response | 
**user_id** | **str** | The id of the user that issued a request | 
**resource_id** | **str** | The unique resource id | 
**queue** | **str** | The name of the queue in which the job is queued | [optional] 
**process_log** | [**List[ProcessLogModel]**](ProcessLogModel.md) | A list of ProcessLogModels | [optional] 
**process_chain_list** | [**List[GrassModule]**](GrassModule.md) | The list of GRASS modules that were used in the processing | [optional] 
**process_results** | [**List[UnivarResultModel]**](UnivarResultModel.md) |  | [optional] 
**progress** | [**ProgressInfoModel**](ProgressInfoModel.md) |  | [optional] 
**message** | **str** | Message for the user, maybe status, finished or error message | 
**exception** | [**ExceptionTracebackModel**](ExceptionTracebackModel.md) |  | [optional] 
**accept_timestamp** | **float** | The acceptance timestamp in seconds of the response | 
**accept_datetime** | **str** | The acceptance timestamp of the response in human readable format | 
**timestamp** | **float** | The current timestamp in seconds of the response | 
**time_delta** | **float** | The time delta of the processing in seconds | [optional] 
**datetime** | **str** | The current timestamp of the response in human readable format | 
**http_code** | **float** | The HTTP code of the response | [optional] 
**urls** | [**UrlModel**](UrlModel.md) |  | [optional] 
**api_info** | [**ApiInfoModel**](ApiInfoModel.md) |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.sentinel_ndvi_response_model import SentinelNDVIResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelNDVIResponseModel from a JSON string
sentinel_ndvi_response_model_instance = SentinelNDVIResponseModel.from_json(json)
# print the JSON string representation of the object
print SentinelNDVIResponseModel.to_json()

# convert the object into a dict
sentinel_ndvi_response_model_dict = sentinel_ndvi_response_model_instance.to_dict()
# create an instance of SentinelNDVIResponseModel from a dict
sentinel_ndvi_response_model_form_dict = sentinel_ndvi_response_model.from_dict(sentinel_ndvi_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


