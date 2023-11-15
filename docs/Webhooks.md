# Webhooks

Specify HTTP(S) GET/POST endpoints that should be called when the process chain was executed successful or unsuccessfully (finished) or when a status/progress update is available (update). The actinia JSON response will be send as JSON content to the POST endpoints after processing finished or the status was updated. The GET endpoints, that must be available by the same URL as the POST endpoints (update/finished), will be used to check if the webhooks endpoints are available. The finished endpoint is mandatory, the update endpoint is optional.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **str** | Specify a HTTP(S) GET/POST endpoint that should be called when a status update is available while the process chain is executed. The actinia JSON status response will be send as JSON content to the POST endpoint for each status update until the process finished. The GET endpoint, that must be available by the same URL as the POST endpoint, will be used to check if the webhook endpoint is available. | [optional] 
**finished** | **str** | Specify a HTTP(S) GET/POST endpoint that should be called when the process chain was executed successful or unsuccessfully. The actinia JSON response will be send as JSON content to the POST endpoint after processing finished. The GET endpoint, that must be available by the same URL as the POST endpoint, will be used to check if the webhook endpoint is available. | 

## Example

```python
from actinia_openapi_python_client.models.webhooks import Webhooks

# TODO update the JSON string below
json = "{}"
# create an instance of Webhooks from a JSON string
webhooks_instance = Webhooks.from_json(json)
# print the JSON string representation of the object
print Webhooks.to_json()

# convert the object into a dict
webhooks_dict = webhooks_instance.to_dict()
# create an instance of Webhooks from a dict
webhooks_form_dict = webhooks.from_dict(webhooks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


