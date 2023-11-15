# coding: utf-8

"""
    Actinia

     ================================ Actinia - The GRASS GIS REST API ================================  **Actinia** is an open source REST API for scalable, distributed, high performance processing of geographical data that uses GRASS GIS for computational tasks.  It provides a REST API to process satellite images, time series of satellite images, arbitrary raster data with geographical relations and vector data.  The REST interface allows to access, manage and manipulate the GRASS GIS database via HTTP GET,PUT,POST and DELETE requests and to process raster, vector and time series data located in a persistent GRASS GIS database. **Actinia** allows the processing of cloud based data, for example all Landsat 4-8 scenes as well as all Sentinel2A scenes in an ephemeral databases. The computational results of ephemeral processing are available via object storage as GeoTIFF files.  The full API documentation is available here: https://redocly.github.io/redoc/?url=https://actinia.mundialis.de/latest/ swagger.json   Examples: ---------  To execute the examples, first setup login information, IP address and port:      export ACTINIA_URL=https://actinia.mundialis.de/latest     export AUTH='-u demouser:gu3st!pa55w0rd'  **Data management**  - List all locations that are available in the actinia persistent database:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations\"  - List all mapsets in the location latlong_wgs84:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets\"  - List all raster layers in location latlong_wgs84 and mapset Sentinel2A      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets/Sentinel2A/raster_layers\"  - List all space-time raster datasets (STRDS) in location ECAD and mapset   PERMANENT:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/raster_layers\"  - List all raster map layers of the STRDS precipitation_1950_2013_yearly_mm:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/strds/precipitation_    1950_2013_yearly_mm/raster_layers\"  **Landsat and Sentinel2A NDVI computation**  This API call will compute the NDVI of the top of atmosphere (TOAR) corrected Landsat4 scene LC80440342016259LGN00:      curl ${AUTH} -X POST \"${ACTINIA_URL}/landsat_process/    LC80440342016259LGN00/TOAR/NDVI\"  NDVI computation of Sentinel2A scene S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138:      curl ${AUTH} -X POST \"${ACTINIA_URL}/sentinel2_process/ndvi/    S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138\"  The results of the asynchronous computations are available as GeoTIFF file in a cloud storage for download. 

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProcessLogModel(BaseModel):
    """
    This class defines the model for Unix process information.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The ID of the executable")
    executable: StrictStr = Field(description="The name of the executable")
    parameter: List[StrictStr] = Field(description="The parameter of the executable")
    stdout: StrictStr = Field(description="The stdout output of the executable")
    stderr: List[StrictStr] = Field(description="The stderr output of the executable as list of strings")
    return_code: Union[StrictFloat, StrictInt] = Field(description="The return code of the executable")
    run_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The runtime of the executable in seconds")
    mapset_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The size of the mapset in bytes")
    __properties: ClassVar[List[str]] = ["id", "executable", "parameter", "stdout", "stderr", "return_code", "run_time", "mapset_size"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProcessLogModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProcessLogModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "executable": obj.get("executable"),
            "parameter": obj.get("parameter"),
            "stdout": obj.get("stdout"),
            "stderr": obj.get("stderr"),
            "return_code": obj.get("return_code"),
            "run_time": obj.get("run_time"),
            "mapset_size": obj.get("mapset_size")
        })
        return _obj


