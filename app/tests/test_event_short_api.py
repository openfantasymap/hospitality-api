# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.event_short import EventShort  # noqa: F401
from openapi_server.models.event_short_by_room import EventShortByRoom  # noqa: F401
from openapi_server.models.event_short_linked import EventShortLinked  # noqa: F401
from openapi_server.models.event_short_result import EventShortResult  # noqa: F401
from openapi_server.models.event_short_types import EventShortTypes  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_v1_event_short_get(client: TestClient):
    """Test case for v1_event_short_get

    GET EventShort List
    """
    params = [("pagenumber", 1),     ("pagesize", 56),     ("startdate", 'startdate_example'),     ("enddate", 'enddate_example'),     ("datetimeformat", 'datetimeformat_example'),     ("source", 'source_example'),     ("eventlocation", 'eventlocation_example'),     ("onlyactive", True),     ("websiteactive", True),     ("communityactive", True),     ("active", True),     ("eventids", 'eventids_example'),     ("webaddress", 'webaddress_example'),     ("tagfilter", 'tagfilter_example'),     ("sortorder", 'ASC'),     ("seed", 'seed_example'),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("optimizedates", False),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("lastchange", 'lastchange_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/EventShort",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_short_post(client: TestClient):
    """Test case for v1_event_short_post

    
    """
    event_short_linked = {"event_text_en":"EventTextEN","event_document":[{"language":"Language","document_url":"DocumentURL"},{"language":"Language","document_url":"DocumentURL"}],"event_text_it":"EventTextIT","contact_country":"ContactCountry","tag_ids":["TagIds","TagIds"],"published_on":["PublishedOn","PublishedOn"],"display2":"Y","video_items":{"key":[{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7},{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7}]},"display3":"Y","display4":"Y","mapping":{"key":{"key":"Mapping"}},"display5":"Y","display6":"Y","display7":"Y","display8":"Y","display9":"Y","start_date":"2000-01-23T04:56:07.000+00:00","company_name":"CompanyName","sold_out":1,"event_text":{"key":"EventText"},"display1":"Y","event_id":0,"company_url":"CompanyUrl","active_today":1,"custom_tagging":["CustomTagging","CustomTagging"],"additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"event_title":{"key":"EventTitle"},"gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"company_mail":"CompanyMail","contact_last_name":"ContactLastName","gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"typical_age_range":{"age_from":2,"age_to":4},"active":1,"end_date_utc":1.4658129805029452,"external_organizer":1,"documents":{"key":[{"language":"Language","document_url":"DocumentURL","document_name":"DocumentName"},{"language":"Language","document_url":"DocumentURL","document_name":"DocumentName"}]},"first_import":"2000-01-23T04:56:07.000+00:00","event_text_de":"EventTextDE","event_description_it":"EventDescriptionIT","start_date_utc":6.027456183070403,"id":"Id","changed_on":"2000-01-23T04:56:07.000+00:00","detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}},"event_description_en":"EventDescriptionEN","company_phone":"CompanyPhone","license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"anchor_venue":"AnchorVenue","self":"Self","company_fax":"CompanyFax","source":"Source","contact_phone":"ContactPhone","contact_cell":"ContactCell","active_community_app":1,"event_description_de":"EventDescriptionDE","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"web_address":"WebAddress","contact_fax":"ContactFax","contact_city":"ContactCity","_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"contact_first_name":"ContactFirstName","contact_code":"ContactCode","contact_postal_code":"ContactPostalCode","has_language":["HasLanguage","HasLanguage"],"company_id":"CompanyId","event_location":"NOI","technology_fields":["TechnologyFields","TechnologyFields"],"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"active_web":1,"end_date":"2000-01-23T04:56:07.000+00:00","room_booked":[{"space":"Space","start_date":"2000-01-23T04:56:07.000+00:00","subtitle":"Subtitle","comment":"Comment","end_date_utc":3.616076749251911,"space_abbrev":"SpaceAbbrev","space_desc_room_mapping":"SpaceDescRoomMapping","space_type":"SpaceType","space_desc":"SpaceDesc","start_date_utc":9.301444243932576,"end_date":"2000-01-23T04:56:07.000+00:00"},{"space":"Space","start_date":"2000-01-23T04:56:07.000+00:00","subtitle":"Subtitle","comment":"Comment","end_date_utc":3.616076749251911,"space_abbrev":"SpaceAbbrev","space_desc_room_mapping":"SpaceDescRoomMapping","space_type":"SpaceType","space_desc":"SpaceDesc","start_date_utc":9.301444243932576,"end_date":"2000-01-23T04:56:07.000+00:00"}],"video_url":"VideoUrl","company_address_line1":"CompanyAddressLine1","company_address_line2":"CompanyAddressLine2","anchor_venue_short":"AnchorVenueShort","last_change":"2000-01-23T04:56:07.000+00:00","company_postal_code":"CompanyPostalCode","contact_address_line1":"ContactAddressLine1","anchor_venue_room_mapping":"AnchorVenueRoomMapping","contact_email":"ContactEmail","contact_address_line3":"ContactAddressLine3","contact_address_line2":"ContactAddressLine2","shortname":"Shortname","company_city":"CompanyCity","event_description":"EventDescription","company_address_line3":"CompanyAddressLine3","company_country":"CompanyCountry"}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/EventShort",
    #    headers=headers,
    #    json=event_short_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_short_detail_id_get(client: TestClient):
    """Test case for v1_event_short_detail_id_get

    GET EventShort Single
    """
    params = [("language", 'language_example'),     ("optimizedates", False),     ("fields", ['fields_example']),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/EventShort/Detail/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_event_short(client: TestClient):
    """Test case for single_event_short

    GET EventShort Single
    """
    params = [("language", 'language_example'),     ("optimizedates", False),     ("fields", ['fields_example']),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/EventShort/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_short_id_put(client: TestClient):
    """Test case for v1_event_short_id_put

    
    """
    event_short_linked = {"event_text_en":"EventTextEN","event_document":[{"language":"Language","document_url":"DocumentURL"},{"language":"Language","document_url":"DocumentURL"}],"event_text_it":"EventTextIT","contact_country":"ContactCountry","tag_ids":["TagIds","TagIds"],"published_on":["PublishedOn","PublishedOn"],"display2":"Y","video_items":{"key":[{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7},{"license":"License","definition":"Definition","duration":2.3021358869347655,"bitrate":9,"url":"Url","name":"Name","video_type":"VideoType","license_holder":"LicenseHolder","video_desc":"VideoDesc","active":1,"copy_right":"CopyRight","language":"Language","streaming_source":"StreamingSource","video_source":"VideoSource","height":5,"width":5,"video_title":"VideoTitle","resolution":7}]},"display3":"Y","display4":"Y","mapping":{"key":{"key":"Mapping"}},"display5":"Y","display6":"Y","display7":"Y","display8":"Y","display9":"Y","start_date":"2000-01-23T04:56:07.000+00:00","company_name":"CompanyName","sold_out":1,"event_text":{"key":"EventText"},"display1":"Y","event_id":0,"company_url":"CompanyUrl","active_today":1,"custom_tagging":["CustomTagging","CustomTagging"],"additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"event_title":{"key":"EventTitle"},"gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"company_mail":"CompanyMail","contact_last_name":"ContactLastName","gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"typical_age_range":{"age_from":2,"age_to":4},"active":1,"end_date_utc":1.4658129805029452,"external_organizer":1,"documents":{"key":[{"language":"Language","document_url":"DocumentURL","document_name":"DocumentName"},{"language":"Language","document_url":"DocumentURL","document_name":"DocumentName"}]},"first_import":"2000-01-23T04:56:07.000+00:00","event_text_de":"EventTextDE","event_description_it":"EventDescriptionIT","start_date_utc":6.027456183070403,"id":"Id","changed_on":"2000-01-23T04:56:07.000+00:00","detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}},"event_description_en":"EventDescriptionEN","company_phone":"CompanyPhone","license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"anchor_venue":"AnchorVenue","self":"Self","company_fax":"CompanyFax","source":"Source","contact_phone":"ContactPhone","contact_cell":"ContactCell","active_community_app":1,"event_description_de":"EventDescriptionDE","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"web_address":"WebAddress","contact_fax":"ContactFax","contact_city":"ContactCity","_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"contact_first_name":"ContactFirstName","contact_code":"ContactCode","contact_postal_code":"ContactPostalCode","has_language":["HasLanguage","HasLanguage"],"company_id":"CompanyId","event_location":"NOI","technology_fields":["TechnologyFields","TechnologyFields"],"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"active_web":1,"end_date":"2000-01-23T04:56:07.000+00:00","room_booked":[{"space":"Space","start_date":"2000-01-23T04:56:07.000+00:00","subtitle":"Subtitle","comment":"Comment","end_date_utc":3.616076749251911,"space_abbrev":"SpaceAbbrev","space_desc_room_mapping":"SpaceDescRoomMapping","space_type":"SpaceType","space_desc":"SpaceDesc","start_date_utc":9.301444243932576,"end_date":"2000-01-23T04:56:07.000+00:00"},{"space":"Space","start_date":"2000-01-23T04:56:07.000+00:00","subtitle":"Subtitle","comment":"Comment","end_date_utc":3.616076749251911,"space_abbrev":"SpaceAbbrev","space_desc_room_mapping":"SpaceDescRoomMapping","space_type":"SpaceType","space_desc":"SpaceDesc","start_date_utc":9.301444243932576,"end_date":"2000-01-23T04:56:07.000+00:00"}],"video_url":"VideoUrl","company_address_line1":"CompanyAddressLine1","company_address_line2":"CompanyAddressLine2","anchor_venue_short":"AnchorVenueShort","last_change":"2000-01-23T04:56:07.000+00:00","company_postal_code":"CompanyPostalCode","contact_address_line1":"ContactAddressLine1","anchor_venue_room_mapping":"AnchorVenueRoomMapping","contact_email":"ContactEmail","contact_address_line3":"ContactAddressLine3","contact_address_line2":"ContactAddressLine2","shortname":"Shortname","company_city":"CompanyCity","event_description":"EventDescription","company_address_line3":"CompanyAddressLine3","company_country":"CompanyCountry"}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/EventShort/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=event_short_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_short_id_delete(client: TestClient):
    """Test case for v1_event_short_id_delete

    
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/EventShort/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_short_getby_room_booked_get(client: TestClient):
    """Test case for v1_event_short_getby_room_booked_get

    GET EventShort List by Room Occupation
    """
    params = [("startdate", 'startdate_example'),     ("enddate", 'enddate_example'),     ("datetimeformat", 'datetimeformat_example'),     ("source", 'source_example'),     ("eventlocation", 'eventlocation_example'),     ("onlyactive", True),     ("websiteactive", True),     ("communityactive", True),     ("active", True),     ("tagfilter", 'tagfilter_example'),     ("eventids", 'eventids_example'),     ("webaddress", 'webaddress_example'),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("lastchange", 'lastchange_example'),     ("updatefrom", 'updatefrom_example'),     ("publishedon", 'publishedon_example'),     ("eventgrouping", True),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/EventShort/GetbyRoomBooked",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_short_types_get(client: TestClient):
    """Test case for v1_event_short_types_get

    GET EventShort Types
    """
    params = [("language", 'language_example'),     ("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("seed", 'seed_example'),     ("type", 'type_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/EventShortTypes",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_event_short_types(client: TestClient):
    """Test case for single_event_short_types

    GET EventShort Type Single
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
    #    "/v1/EventShortTypes/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

