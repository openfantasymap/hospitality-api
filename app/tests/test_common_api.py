# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.area_linked import AreaLinked  # noqa: F401
from openapi_server.models.area_linked_json_result import AreaLinkedJsonResult  # noqa: F401
from openapi_server.models.district_linked import DistrictLinked  # noqa: F401
from openapi_server.models.district_linked_json_result import DistrictLinkedJsonResult  # noqa: F401
from openapi_server.models.experience_area_linked import ExperienceAreaLinked  # noqa: F401
from openapi_server.models.experience_area_linked_json_result import ExperienceAreaLinkedJsonResult  # noqa: F401
from openapi_server.models.meta_region_linked import MetaRegionLinked  # noqa: F401
from openapi_server.models.meta_region_linked_json_result import MetaRegionLinkedJsonResult  # noqa: F401
from openapi_server.models.municipality_linked import MunicipalityLinked  # noqa: F401
from openapi_server.models.municipality_linked_json_result import MunicipalityLinkedJsonResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.region_linked import RegionLinked  # noqa: F401
from openapi_server.models.region_linked_json_result import RegionLinkedJsonResult  # noqa: F401
from openapi_server.models.ski_area_linked import SkiAreaLinked  # noqa: F401
from openapi_server.models.ski_area_linked_json_result import SkiAreaLinkedJsonResult  # noqa: F401
from openapi_server.models.ski_region_linked import SkiRegionLinked  # noqa: F401
from openapi_server.models.ski_region_linked_json_result import SkiRegionLinkedJsonResult  # noqa: F401
from openapi_server.models.tourismverein_linked import TourismvereinLinked  # noqa: F401
from openapi_server.models.tourismverein_linked_json_result import TourismvereinLinkedJsonResult  # noqa: F401
from openapi_server.models.wine_linked import WineLinked  # noqa: F401
from openapi_server.models.wine_linked_json_result import WineLinkedJsonResult  # noqa: F401


def test_v1_meta_region_get(client: TestClient):
    """Test case for v1_meta_region_get

    GET MetaRegion List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/MetaRegion",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_meta_region(client: TestClient):
    """Test case for single_meta_region

    GET MetaRegion Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/MetaRegion/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_experience_area_get(client: TestClient):
    """Test case for v1_experience_area_get

    GET Experiencearea List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("visibleinsearch", True),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/ExperienceArea",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_experience_area(client: TestClient):
    """Test case for single_experience_area

    GET ExperienceArea Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/ExperienceArea/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_region_get(client: TestClient):
    """Test case for v1_region_get

    GET Region List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Region",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_region(client: TestClient):
    """Test case for single_region

    GET Region Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Region/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_tourism_association_get(client: TestClient):
    """Test case for v1_tourism_association_get

    GET TourismAssociation List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/TourismAssociation",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_tourism_association(client: TestClient):
    """Test case for single_tourism_association

    GET TourismAssociation Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/TourismAssociation/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_municipality_get(client: TestClient):
    """Test case for v1_municipality_get

    GET Municipality List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("visibleinsearch", True),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Municipality",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_municipality(client: TestClient):
    """Test case for single_municipality

    GET Municipality Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Municipality/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_district_get(client: TestClient):
    """Test case for v1_district_get

    GET District List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("visibleinsearch", True),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/District",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_district(client: TestClient):
    """Test case for single_district

    GET District Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/District/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_area_get(client: TestClient):
    """Test case for v1_area_get

    GET Area List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Area",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_area(client: TestClient):
    """Test case for single_area

    GET Area Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Area/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_ski_region_get(client: TestClient):
    """Test case for v1_ski_region_get

    GET SkiRegion List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/SkiRegion",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_ski_region(client: TestClient):
    """Test case for single_ski_region

    GET SkiRegion Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/SkiRegion/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_ski_area_get(client: TestClient):
    """Test case for v1_ski_area_get

    GET SkiArea List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("active", True),     ("odhactive", True),     ("tagfilter", 'tagfilter_example'),     ("source", 'source_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/SkiArea",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_ski_area(client: TestClient):
    """Test case for single_ski_area

    GET SkiArea Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/SkiArea/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_wine_award_get(client: TestClient):
    """Test case for v1_wine_award_get

    GET Wine Awards List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("active", True),     ("odhactive", True),     ("source", 'source_example'),     ("wineid", 'wineid_example'),     ("companyid", 'companyid_example'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/WineAward",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_wine_award(client: TestClient):
    """Test case for single_wine_award

    GET Wine Award Single
    """
    params = [("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/WineAward/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

