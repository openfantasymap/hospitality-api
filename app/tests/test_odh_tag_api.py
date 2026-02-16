# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.odh_tag_linked import ODHTagLinked  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_v1_odh_tag_get(client: TestClient):
    """Test case for v1_odh_tag_get

    GET ODHTag List
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("language", 'language_example'),     ("validforentity", 'validforentity_example'),     ("mainentity", 'mainentity_example'),     ("displayascategory", True),     ("source", 'source_example'),     ("publishedon", 'publishedon_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("localizationlanguage", 'localizationlanguage_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/ODHTag",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_odh_tag(client: TestClient):
    """Test case for single_odh_tag

    GET ODHTag Single
    """
    params = [("language", 'language_example'),     ("fields", ['fields_example']),     ("localizationlanguage", 'localizationlanguage_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/ODHTag/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

