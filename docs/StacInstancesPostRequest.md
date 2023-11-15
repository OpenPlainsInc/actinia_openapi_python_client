# StacInstancesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stac_instance_id** | **str** | name of the instance id to create | [optional] 

## Example

```python
from actinia_openapi_python_client.models.stac_instances_post_request import StacInstancesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StacInstancesPostRequest from a JSON string
stac_instances_post_request_instance = StacInstancesPostRequest.from_json(json)
# print the JSON string representation of the object
print StacInstancesPostRequest.to_json()

# convert the object into a dict
stac_instances_post_request_dict = stac_instances_post_request_instance.to_dict()
# create an instance of StacInstancesPostRequest from a dict
stac_instances_post_request_form_dict = stac_instances_post_request.from_dict(stac_instances_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


