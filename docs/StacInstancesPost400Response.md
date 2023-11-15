# StacInstancesPost400Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | detailed message | [optional] 

## Example

```python
from actinia_openapi_python_client.models.stac_instances_post400_response import StacInstancesPost400Response

# TODO update the JSON string below
json = "{}"
# create an instance of StacInstancesPost400Response from a JSON string
stac_instances_post400_response_instance = StacInstancesPost400Response.from_json(json)
# print the JSON string representation of the object
print StacInstancesPost400Response.to_json()

# convert the object into a dict
stac_instances_post400_response_dict = stac_instances_post400_response_instance.to_dict()
# create an instance of StacInstancesPost400Response from a dict
stac_instances_post400_response_form_dict = stac_instances_post400_response.from_dict(stac_instances_post400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


