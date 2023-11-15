# coding: utf-8

"""
    Actinia

     ================================ Actinia - The GRASS GIS REST API ================================  **Actinia** is an open source REST API for scalable, distributed, high performance processing of geographical data that uses GRASS GIS for computational tasks.  It provides a REST API to process satellite images, time series of satellite images, arbitrary raster data with geographical relations and vector data.  The REST interface allows to access, manage and manipulate the GRASS GIS database via HTTP GET,PUT,POST and DELETE requests and to process raster, vector and time series data located in a persistent GRASS GIS database. **Actinia** allows the processing of cloud based data, for example all Landsat 4-8 scenes as well as all Sentinel2A scenes in an ephemeral databases. The computational results of ephemeral processing are available via object storage as GeoTIFF files.  The full API documentation is available here: https://redocly.github.io/redoc/?url=https://actinia.mundialis.de/latest/ swagger.json   Examples: ---------  To execute the examples, first setup login information, IP address and port:      export ACTINIA_URL=https://actinia.mundialis.de/latest     export AUTH='-u demouser:gu3st!pa55w0rd'  **Data management**  - List all locations that are available in the actinia persistent database:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations\"  - List all mapsets in the location latlong_wgs84:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets\"  - List all raster layers in location latlong_wgs84 and mapset Sentinel2A      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets/Sentinel2A/raster_layers\"  - List all space-time raster datasets (STRDS) in location ECAD and mapset   PERMANENT:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/raster_layers\"  - List all raster map layers of the STRDS precipitation_1950_2013_yearly_mm:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/strds/precipitation_    1950_2013_yearly_mm/raster_layers\"  **Landsat and Sentinel2A NDVI computation**  This API call will compute the NDVI of the top of atmosphere (TOAR) corrected Landsat4 scene LC80440342016259LGN00:      curl ${AUTH} -X POST \"${ACTINIA_URL}/landsat_process/    LC80440342016259LGN00/TOAR/NDVI\"  NDVI computation of Sentinel2A scene S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138:      curl ${AUTH} -X POST \"${ACTINIA_URL}/sentinel2_process/ndvi/    S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138\"  The results of the asynchronous computations are available as GeoTIFF file in a cloud storage for download. 

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from actinia_openapi_python_client.models.vector_sampling_response_model import VectorSamplingResponseModel

class TestVectorSamplingResponseModel(unittest.TestCase):
    """VectorSamplingResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VectorSamplingResponseModel:
        """Test VectorSamplingResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VectorSamplingResponseModel`
        """
        model = VectorSamplingResponseModel()
        if include_optional:
            return VectorSamplingResponseModel(
                status = '',
                user_id = '',
                resource_id = '',
                queue = '',
                process_log = [
                    {executable=g.list, parameter=[type=raster, mapset=PERMANENT], return_code=0, run_time=0.05017662048339844, stderr=[], stdout=aspect
basin_50K
}
                    ],
                process_chain_list = [
                    {module=r.slope.aspect, id=r_slope_aspect_1, inputs=[{import_descr={source=https://storage.googleapis.com/graas-geodata/elev_ned_30m.tif, type=raster}, param=raster, value=elev_ned_30m_new}], outputs=[{export={format=GTiff, type=raster}, param=slope, value=elev_ned_30m_new_slope}], flags=a}
                    ],
                process_results = [
                    [
                        ''
                        ]
                    ],
                progress = {num_of_steps=6, step=6},
                message = '',
                exception = {message=Error, type=exceptions.Exception, traceback=File "main.py", line 2, in <module>
    raise Exception("Error")
},
                accept_timestamp = 1.337,
                accept_datetime = '',
                timestamp = 1.337,
                time_delta = 1.337,
                datetime = '',
                http_code = 1.337,
                urls = {resources=[http://localhost/api/v3/resource/user/resource_id-4846cbcc-3918-4654-bf4d-7e1ba2b59ce6/my_slope.tiff], status=http://localhost/api/v3/resources/user/resource_id-4846cbcc-3918-4654-bf4d-7e1ba2b59ce6},
                api_info = {endpoint=asyncephemeralresource, method=POST, path=/api/v3/locations/nc_spm_08/processing_async, request_url=http://localhost/api/v3/locations/nc_spm_08/processing_async}
            )
        else:
            return VectorSamplingResponseModel(
                status = '',
                user_id = '',
                resource_id = '',
                message = '',
                accept_timestamp = 1.337,
                accept_datetime = '',
                timestamp = 1.337,
                datetime = '',
        )
        """

    def testVectorSamplingResponseModel(self):
        """Test VectorSamplingResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
