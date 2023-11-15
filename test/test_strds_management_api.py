# coding: utf-8

"""
    Actinia

     ================================ Actinia - The GRASS GIS REST API ================================  **Actinia** is an open source REST API for scalable, distributed, high performance processing of geographical data that uses GRASS GIS for computational tasks.  It provides a REST API to process satellite images, time series of satellite images, arbitrary raster data with geographical relations and vector data.  The REST interface allows to access, manage and manipulate the GRASS GIS database via HTTP GET,PUT,POST and DELETE requests and to process raster, vector and time series data located in a persistent GRASS GIS database. **Actinia** allows the processing of cloud based data, for example all Landsat 4-8 scenes as well as all Sentinel2A scenes in an ephemeral databases. The computational results of ephemeral processing are available via object storage as GeoTIFF files.  The full API documentation is available here: https://redocly.github.io/redoc/?url=https://actinia.mundialis.de/latest/ swagger.json   Examples: ---------  To execute the examples, first setup login information, IP address and port:      export ACTINIA_URL=https://actinia.mundialis.de/latest     export AUTH='-u demouser:gu3st!pa55w0rd'  **Data management**  - List all locations that are available in the actinia persistent database:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations\"  - List all mapsets in the location latlong_wgs84:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets\"  - List all raster layers in location latlong_wgs84 and mapset Sentinel2A      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets/Sentinel2A/raster_layers\"  - List all space-time raster datasets (STRDS) in location ECAD and mapset   PERMANENT:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/raster_layers\"  - List all raster map layers of the STRDS precipitation_1950_2013_yearly_mm:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/strds/precipitation_    1950_2013_yearly_mm/raster_layers\"  **Landsat and Sentinel2A NDVI computation**  This API call will compute the NDVI of the top of atmosphere (TOAR) corrected Landsat4 scene LC80440342016259LGN00:      curl ${AUTH} -X POST \"${ACTINIA_URL}/landsat_process/    LC80440342016259LGN00/TOAR/NDVI\"  NDVI computation of Sentinel2A scene S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138:      curl ${AUTH} -X POST \"${ACTINIA_URL}/sentinel2_process/ndvi/    S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138\"  The results of the asynchronous computations are available as GeoTIFF file in a cloud storage for download. 

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from actinia_openapi_python_client.api.strds_management_api import STRDSManagementApi


class TestSTRDSManagementApi(unittest.TestCase):
    """STRDSManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = STRDSManagementApi()

    def tearDown(self) -> None:
        pass

    def test_locations_location_name_mapsets_mapset_name_strds_get(self) -> None:
        """Test case for locations_location_name_mapsets_mapset_name_strds_get

        Get a list of all STRDS that are located in a specific location/mapset.
        """
        pass

    def test_locations_location_name_mapsets_mapset_name_strds_strds_name_delete(self) -> None:
        """Test case for locations_location_name_mapsets_mapset_name_strds_strds_name_delete

        Delete a STRDS that is located in a specific location/mapset.
        """
        pass

    def test_locations_location_name_mapsets_mapset_name_strds_strds_name_get(self) -> None:
        """Test case for locations_location_name_mapsets_mapset_name_strds_strds_name_get

        Get information about a STRDS that is located in a specific
        """
        pass

    def test_locations_location_name_mapsets_mapset_name_strds_strds_name_post(self) -> None:
        """Test case for locations_location_name_mapsets_mapset_name_strds_strds_name_post

        Create a new STRDS in a specific location/mapset.
        """
        pass

    def test_locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete(self) -> None:
        """Test case for locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_delete

        Unregister raster map layers from a STRDS located in a specific
        """
        pass

    def test_locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get(self) -> None:
        """Test case for locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_get

        Get a list of all raster map layers that are registered in a STRDS
        """
        pass

    def test_locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put(self) -> None:
        """Test case for locations_location_name_mapsets_mapset_name_strds_strds_name_raster_layers_put

        Register raster map layers in a STRDS located in a specific
        """
        pass

    def test_locations_location_name_mapsets_mapset_name_strds_strds_name_render_get(self) -> None:
        """Test case for locations_location_name_mapsets_mapset_name_strds_strds_name_render_get

        Render the raster map layers of a specific STRDS as a single image.
        """
        pass


if __name__ == '__main__':
    unittest.main()
