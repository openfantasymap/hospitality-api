# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.tag_linked import TagLinked  # noqa: F401


def test_v1_tag_get(client: TestClient):
    """Test case for v1_tag_get

    GET Tag List
    """
    params = [("pagenumber", 1),     ("pagesize", 56),     ("language", 'language_example'),     ("idlist", 'idlist_example'),     ("validforentity", 'validforentity_example'),     ("types", 'types_example'),     ("displayascategory", True),     ("publishedon", 'publishedon_example'),     ("source", 'source_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Tag",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_tag_post(client: TestClient):
    """Test case for v1_tag_post

    POST Insert new Tag
    """
    tag_linked = {"publish_data_with_tag_on":{"key":1},"types":["Types","Types"],"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"description":{"key":"Description"},"published_on":["PublishedOn","PublishedOn"],"tag_name":{"key":"TagName"},"valid_for_entity":["ValidForEntity","ValidForEntity"],"display_as_category":1,"mapping":{"key":{"key":"Mapping"}},"self":"Self","main_entity":"MainEntity","source":"Source","active":1,"idm_category_mapping":{"key":"IDMCategoryMapping"},"first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","lts_tagging_info":{"ltsrid":"LTSRID","parent_ltsrid":"ParentLTSRID"},"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"id":"Id","shortname":"Shortname","odh_tag_ids":["ODHTagIds","ODHTagIds"],"mapped_tag_ids":["MappedTagIds","MappedTagIds"]}
    params = [("generateid", True)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/Tag",
    #    headers=headers,
    #    json=tag_linked,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_tag(client: TestClient):
    """Test case for single_tag

    GET Tag Single
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
    #    "/v1/Tag/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_tag_id_put(client: TestClient):
    """Test case for v1_tag_id_put

    PUT Modify existing Tag
    """
    tag_linked = {"publish_data_with_tag_on":{"key":1},"types":["Types","Types"],"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"description":{"key":"Description"},"published_on":["PublishedOn","PublishedOn"],"tag_name":{"key":"TagName"},"valid_for_entity":["ValidForEntity","ValidForEntity"],"display_as_category":1,"mapping":{"key":{"key":"Mapping"}},"self":"Self","main_entity":"MainEntity","source":"Source","active":1,"idm_category_mapping":{"key":"IDMCategoryMapping"},"first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","lts_tagging_info":{"ltsrid":"LTSRID","parent_ltsrid":"ParentLTSRID"},"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"id":"Id","shortname":"Shortname","odh_tag_ids":["ODHTagIds","ODHTagIds"],"mapped_tag_ids":["MappedTagIds","MappedTagIds"]}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/Tag/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=tag_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_tag_id_delete(client: TestClient):
    """Test case for v1_tag_id_delete

    DELETE Tag by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/Tag/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

