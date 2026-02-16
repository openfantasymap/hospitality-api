# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401


def test_v1_json_ld_detail_in_ld_get(client: TestClient):
    """Test case for v1_json_ld_detail_in_ld_get

    GET Detail Data in JSON LD Format (Schema.org Datatypes as output)
    """
    params = [("type", 'type_example'),     ("id", 'id_example'),     ("language", 'en'),     ("idtoshow", ''),     ("urltoshow", ''),     ("imageurltoshow", ''),     ("showid", True)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/JsonLD/DetailInLD",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

