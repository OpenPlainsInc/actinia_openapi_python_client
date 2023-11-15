# GridTilingResponseModel

Grid tiling response schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the response | [optional] 
**user_id** | **str** | The id of the user that issued a request | [optional] 
**resource_id** | **str** | The unique resource id | [optional] 
**queue** | **str** | The name of the queue in which the job is queued | [optional] 
**process_log** | [**List[ProcessLogModel]**](ProcessLogModel.md) | A list of ProcessLogModels | [optional] 
**process_chain_list** | [**List[GrassModule]**](GrassModule.md) | The list of GRASS modules that were used in the processing | [optional] 
**process_results** | **List[str]** | The names of all created tiles. | [optional] 
**progress** | [**ProgressInfoModel**](ProgressInfoModel.md) |  | [optional] 
**message** | **str** | Message for the user, maybe status, finished or error message | [optional] 
**exception** | [**ExceptionTracebackModel**](ExceptionTracebackModel.md) |  | [optional] 
**accept_timestamp** | **float** | The acceptance timestamp in seconds of the response | [optional] 
**accept_datetime** | **str** | The acceptance timestamp of the response in human readable format | [optional] 
**timestamp** | **float** | The current timestamp in seconds of the response | [optional] 
**time_delta** | **float** | The time delta of the processing in seconds | [optional] 
**datetime** | **str** | The current timestamp of the response in human readable format | [optional] 
**http_code** | **float** | The HTTP code of the response | [optional] 
**urls** | [**UrlModel**](UrlModel.md) |  | [optional] 
**api_info** | [**ApiInfoModel**](ApiInfoModel.md) |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.grid_tiling_response_model import GridTilingResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GridTilingResponseModel from a JSON string
grid_tiling_response_model_instance = GridTilingResponseModel.from_json(json)
# print the JSON string representation of the object
print GridTilingResponseModel.to_json()

# convert the object into a dict
grid_tiling_response_model_dict = grid_tiling_response_model_instance.to_dict()
# create an instance of GridTilingResponseModel from a dict
grid_tiling_response_model_form_dict = grid_tiling_response_model.from_dict(grid_tiling_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


