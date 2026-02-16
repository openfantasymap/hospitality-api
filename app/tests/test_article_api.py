# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.article_types import ArticleTypes  # noqa: F401
from openapi_server.models.articles_linked import ArticlesLinked  # noqa: F401
from openapi_server.models.articles_linked_json_result import ArticlesLinkedJsonResult  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_v1_article_get(client: TestClient):
    """Test case for v1_article_get

    GET Article List
    """
    params = [("language", 'language_example'),     ("pagenumber", 1),     ("pagesize", 56),     ("articletype", 'articletype_example'),     ("articlesubtype", 'articlesubtype_example'),     ("idlist", 'idlist_example'),     ("langfilter", 'langfilter_example'),     ("sortbyarticledate", True),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("odhactive", True),     ("active", True),     ("updatefrom", 'updatefrom_example'),     ("startdate", 'startdate_example'),     ("enddate", 'enddate_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("source", 'source_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Article",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_article_post(client: TestClient):
    """Test case for v1_article_post

    POST Insert new Article
    """
    articles_linked = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"tag_ids":["TagIds","TagIds"],"highlight":1,"article_date":"2000-01-23T04:56:07.000+00:00","published_on":["PublishedOn","PublishedOn"],"article_type_list":["ArticleTypeList","ArticleTypeList"],"video_items":{"key":[{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7},{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7}]},"odh_active":1,"mapping":{"key":{"key":"Mapping"}},"self":"Self","source":"Source","smg_active":1,"image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"contact_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"article_link_info":{"key":{"language":"Language","elements":{"key":"Elements"}}},"additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"gps_track":[{"type":"Type","format":"Format","gpx_track_url":"GpxTrackUrl","gpx_track_desc":{"key":"GpxTrackDesc"},"id":"Id"},{"type":"Type","format":"Format","gpx_track_url":"GpxTrackUrl","gpx_track_desc":{"key":"GpxTrackDesc"},"id":"Id"}],"smg_tags":["SmgTags","SmgTags"],"has_language":["HasLanguage","HasLanguage"],"sub_type":"SubType","gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"additional_article_infos":{"key":{"language":"Language","elements":{"key":"Elements"}}},"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"article_types":[{"type":"Type","id":"Id","self":"Self"},{"type":"Type","id":"Id","self":"Self"}],"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"type":"Type","expiration_date":"2000-01-23T04:56:07.000+00:00","first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","odh_tags":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"id":"Id","shortname":"Shortname","article_date_to":"2000-01-23T04:56:07.000+00:00","operation_schedule":[{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]},{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]}],"distance_info":{"distance_to_municipality":5.025004791520295,"distance_to_district":9.965781217890562},"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/Article",
    #    headers=headers,
    #    json=articles_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_article(client: TestClient):
    """Test case for single_article

    GET Article Single
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
    #    "/v1/Article/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_article_id_put(client: TestClient):
    """Test case for v1_article_id_put

    PUT Modify existing Article
    """
    articles_linked = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"tag_ids":["TagIds","TagIds"],"highlight":1,"article_date":"2000-01-23T04:56:07.000+00:00","published_on":["PublishedOn","PublishedOn"],"article_type_list":["ArticleTypeList","ArticleTypeList"],"video_items":{"key":[{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7},{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7}]},"odh_active":1,"mapping":{"key":{"key":"Mapping"}},"self":"Self","source":"Source","smg_active":1,"image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"contact_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"article_link_info":{"key":{"language":"Language","elements":{"key":"Elements"}}},"additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"gps_track":[{"type":"Type","format":"Format","gpx_track_url":"GpxTrackUrl","gpx_track_desc":{"key":"GpxTrackDesc"},"id":"Id"},{"type":"Type","format":"Format","gpx_track_url":"GpxTrackUrl","gpx_track_desc":{"key":"GpxTrackDesc"},"id":"Id"}],"smg_tags":["SmgTags","SmgTags"],"has_language":["HasLanguage","HasLanguage"],"sub_type":"SubType","gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"additional_article_infos":{"key":{"language":"Language","elements":{"key":"Elements"}}},"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"article_types":[{"type":"Type","id":"Id","self":"Self"},{"type":"Type","id":"Id","self":"Self"}],"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"type":"Type","expiration_date":"2000-01-23T04:56:07.000+00:00","first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","odh_tags":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"id":"Id","shortname":"Shortname","article_date_to":"2000-01-23T04:56:07.000+00:00","operation_schedule":[{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]},{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]}],"distance_info":{"distance_to_municipality":5.025004791520295,"distance_to_district":9.965781217890562},"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/Article/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=articles_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_article_id_delete(client: TestClient):
    """Test case for v1_article_id_delete

    DELETE Article by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/Article/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_article_types_get(client: TestClient):
    """Test case for v1_article_types_get

    GET Article Types List
    """
    params = [("language", 'language_example'),     ("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("seed", 'seed_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/ArticleTypes",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_article_types(client: TestClient):
    """Test case for single_article_types

    GET Article Types Single
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
    #    "/v1/ArticleTypes/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

