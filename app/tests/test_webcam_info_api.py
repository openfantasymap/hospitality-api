# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.webcam_info import WebcamInfo  # noqa: F401
from openapi_server.models.webcam_info_json_result import WebcamInfoJsonResult  # noqa: F401
from openapi_server.models.webcam_info_linked import WebcamInfoLinked  # noqa: F401


def test_v1_webcam_info_get(client: TestClient):
    """Test case for v1_webcam_info_get

    GET Webcam List
    """
    params = [("language", 'language_example'),     ("pagenumber", 1),     ("pagesize", 56),     ("source", 'source_example'),     ("idlist", 'idlist_example'),     ("active", True),     ("odhactive", True),     ("tagfilter", 'tagfilter_example'),     ("seed", 'seed_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("updatefrom", 'updatefrom_example'),     ("publishedon", 'publishedon_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/WebcamInfo",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_webcam_info_post(client: TestClient):
    """Test case for v1_webcam_info_post

    POST Insert new WebcamInfo
    """
    webcam_info_linked = {"webcamurl":"Webcamurl","license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"tag_ids":["TagIds","TagIds"],"published_on":["PublishedOn","PublishedOn"],"video_items":{"key":[{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7},{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7}]},"odh_active":1,"mapping":{"key":{"key":"Mapping"}},"self":"Self","webcamname":{"key":"Webcamname"},"source":"Source","previewurl":"Previewurl","smg_active":1,"image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"webcam_assigned_on":[{"type":"Type","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id"},{"type":"Type","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id"}],"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"contact_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"smg_tags":["SmgTags","SmgTags"],"webcam_id":"WebcamId","has_language":["HasLanguage","HasLanguage"],"gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"web_cam_properties":{"webcam_url":"WebcamUrl","preview_url":"PreviewUrl","has_vr":1,"view_angle_degree":"ViewAngleDegree","html_embed":"HtmlEmbed","tour_cam":1,"viewer_type":"ViewerType","stream_url":"StreamUrl","zero_direction":"ZeroDirection"},"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"streamurl":"Streamurl","areas":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"list_position":0,"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"area_ids":["AreaIds","AreaIds"],"last_change":"2000-01-23T04:56:07.000+00:00","first_import":"2000-01-23T04:56:07.000+00:00","odh_tags":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"id":"Id","shortname":"Shortname","detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/WebcamInfo",
    #    headers=headers,
    #    json=webcam_info_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_webcam_info(client: TestClient):
    """Test case for single_webcam_info

    GET Webcam Single
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
    #    "/v1/WebcamInfo/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_webcam_info_id_put(client: TestClient):
    """Test case for v1_webcam_info_id_put

    PUT Modify existing WebcamInfo
    """
    webcam_info_linked = {"webcamurl":"Webcamurl","license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"tag_ids":["TagIds","TagIds"],"published_on":["PublishedOn","PublishedOn"],"video_items":{"key":[{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7},{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7}]},"odh_active":1,"mapping":{"key":{"key":"Mapping"}},"self":"Self","webcamname":{"key":"Webcamname"},"source":"Source","previewurl":"Previewurl","smg_active":1,"image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"webcam_assigned_on":[{"type":"Type","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id"},{"type":"Type","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id"}],"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"contact_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"smg_tags":["SmgTags","SmgTags"],"webcam_id":"WebcamId","has_language":["HasLanguage","HasLanguage"],"gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"web_cam_properties":{"webcam_url":"WebcamUrl","preview_url":"PreviewUrl","has_vr":1,"view_angle_degree":"ViewAngleDegree","html_embed":"HtmlEmbed","tour_cam":1,"viewer_type":"ViewerType","stream_url":"StreamUrl","zero_direction":"ZeroDirection"},"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"streamurl":"Streamurl","areas":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"list_position":0,"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"area_ids":["AreaIds","AreaIds"],"last_change":"2000-01-23T04:56:07.000+00:00","first_import":"2000-01-23T04:56:07.000+00:00","odh_tags":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"id":"Id","shortname":"Shortname","detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/WebcamInfo/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=webcam_info_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_webcam_info_id_delete(client: TestClient):
    """Test case for v1_webcam_info_id_delete

    DELETE WebcamInfo by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/WebcamInfo/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

