# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.tourism_meta_data import TourismMetaData  # noqa: F401
from openapi_server.models.tourism_meta_data_json_result import TourismMetaDataJsonResult  # noqa: F401


def test_tourism_api(client: TestClient):
    """Test case for tourism_api

    GET Tourism MetaData List
    """
    params = [("language", 'language_example'),     ("pagenumber", 1),     ("pagesize", 56),     ("seed", 'seed_example'),     ("updatefrom", 'updatefrom_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tourism_api_meta_data(client: TestClient):
    """Test case for tourism_api_meta_data

    GET Tourism MetaData List
    """
    params = [("language", 'language_example'),     ("pagenumber", 1),     ("pagesize", 56),     ("seed", 'seed_example'),     ("updatefrom", 'updatefrom_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/MetaData",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_meta_data_post(client: TestClient):
    """Test case for v1_meta_data_post

    POST Insert new MetaData
    """
    tourism_meta_data = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"published_on":["PublishedOn","PublishedOn"],"category":["Category","Category"],"tag_ids":["TagIds","TagIds"],"self":"Self","data_provider":["DataProvider","DataProvider"],"api_url":"ApiUrl","deprecated":1,"output":{"key":"Output"},"image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"api_type":"ApiType","meta_description":{"key":"MetaDescription"},"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"base_url":"BaseUrl","path_param":["PathParam","PathParam"],"dataspace":"Dataspace","tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"api_access":{"key":"ApiAccess"},"meta_title":{"key":"MetaTitle"},"api_filter":["ApiFilter","ApiFilter"],"sources":["Sources","Sources"],"type":"Type","first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","dataset_licenses":["DatasetLicenses","DatasetLicenses"],"id":"Id","shortname":"Shortname","record_count":{"key":5},"api_description":{"key":"ApiDescription"},"odh_type":"OdhType","swagger_url":"SwaggerUrl"}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/MetaData",
    #    headers=headers,
    #    json=tourism_meta_data,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_meta_data(client: TestClient):
    """Test case for single_meta_data

    GET TourismMetaData Single
    """
    params = [("language", 'language_example'),     ("fields", ['fields_example']),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/MetaData/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_meta_data_id_put(client: TestClient):
    """Test case for v1_meta_data_id_put

    PUT Modify existing MetaData
    """
    tourism_meta_data = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"published_on":["PublishedOn","PublishedOn"],"category":["Category","Category"],"tag_ids":["TagIds","TagIds"],"self":"Self","data_provider":["DataProvider","DataProvider"],"api_url":"ApiUrl","deprecated":1,"output":{"key":"Output"},"image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"api_type":"ApiType","meta_description":{"key":"MetaDescription"},"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"base_url":"BaseUrl","path_param":["PathParam","PathParam"],"dataspace":"Dataspace","tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"api_access":{"key":"ApiAccess"},"meta_title":{"key":"MetaTitle"},"api_filter":["ApiFilter","ApiFilter"],"sources":["Sources","Sources"],"type":"Type","first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","dataset_licenses":["DatasetLicenses","DatasetLicenses"],"id":"Id","shortname":"Shortname","record_count":{"key":5},"api_description":{"key":"ApiDescription"},"odh_type":"OdhType","swagger_url":"SwaggerUrl"}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/MetaData/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=tourism_meta_data,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_meta_data_id_delete(client: TestClient):
    """Test case for v1_meta_data_id_delete

    DELETE MetaData by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/MetaData/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

