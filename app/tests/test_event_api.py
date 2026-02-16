# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.event_linked import EventLinked  # noqa: F401
from openapi_server.models.event_linked_json_result import EventLinkedJsonResult  # noqa: F401
from openapi_server.models.event_types import EventTypes  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_v1_event_get(client: TestClient):
    """Test case for v1_event_get

    GET Event List
    """
    params = [("language", 'language_example'),     ("pagenumber", 1),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("locfilter", 'locfilter_example'),     ("rancfilter", 'rancfilter_example'),     ("topicfilter", 'topicfilter_example'),     ("orgfilter", 'orgfilter_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("active", True),     ("odhactive", True),     ("begindate", 'begindate_example'),     ("enddate", 'enddate_example'),     ("sort", 'sort_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("langfilter", 'langfilter_example'),     ("source", 'source_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Event",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_post(client: TestClient):
    """Test case for v1_event_post

    POST Insert new Event
    """
    event_linked = {"event_date":[{"single_days":1,"max_persons":1,"ticket":1,"event_calculated_days":[{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2},{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2}],"event_calculated_day":{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2},"price_from":7.386281948385884,"is_bookable":1,"is_cancelled":1,"day_rid":"DayRID","event_date_additional_info":{"key":{"description":"Description","guide":"Guide","language":"Language","cancellation_description":"CancellationDescription","registration_within":"RegistrationWithin"}},"event_date_id":"EventDateId","from":"2000-01-23T04:56:07.000+00:00","event_date_ticket_info":{"active":1,"online_contingent":6,"online_sale_until":1},"cancelled":"Cancelled","entrance":"Entrance","active":1,"event_variant_ids":["EventVariantIds","EventVariantIds"],"begin":"Begin","end":"End","to":"2000-01-23T04:56:07.000+00:00","min_persons":1},{"single_days":1,"max_persons":1,"ticket":1,"event_calculated_days":[{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2},{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2}],"event_calculated_day":{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2},"price_from":7.386281948385884,"is_bookable":1,"is_cancelled":1,"day_rid":"DayRID","event_date_additional_info":{"key":{"description":"Description","guide":"Guide","language":"Language","cancellation_description":"CancellationDescription","registration_within":"RegistrationWithin"}},"event_date_id":"EventDateId","from":"2000-01-23T04:56:07.000+00:00","event_date_ticket_info":{"active":1,"online_contingent":6,"online_sale_until":1},"cancelled":"Cancelled","entrance":"Entrance","active":1,"event_variant_ids":["EventVariantIds","EventVariantIds"],"begin":"Begin","end":"End","to":"2000-01-23T04:56:07.000+00:00","min_persons":1}],"tag_ids":["TagIds","TagIds"],"published_on":["PublishedOn","PublishedOn"],"date_begin":"2000-01-23T04:56:07.000+00:00","sign_on":"SignOn","latitude":5.637376656633329,"mapping":{"key":{"key":"Mapping"}},"date_end":"2000-01-23T04:56:07.000+00:00","altitude_unitof_measure":"AltitudeUnitofMeasure","additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"smg_tags":["SmgTags","SmgTags"],"topic_rids":["TopicRIDs","TopicRIDs"],"event_publisher":[{"ranc":9,"publisher_rid":"PublisherRID","publication_status":"PublicationStatus","publish":3},{"ranc":9,"publisher_rid":"PublisherRID","publication_status":"PublicationStatus","publish":3}],"gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"district_ids":["DistrictIds","DistrictIds"],"event_urls":[{"type":"Type","active":1,"url":{"key":"Url"}},{"type":"Type","active":1,"url":{"key":"Url"}}],"longitude":2.3021358869347655,"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"event_booking":{"bookable_from":"2000-01-23T04:56:07.000+00:00","booking_url":{"key":{"url":"Url"}},"bookable_to":"2000-01-23T04:56:07.000+00:00","booking_active":1},"first_import":"2000-01-23T04:56:07.000+00:00","id":"Id","distance_info":{"distance_to_municipality":5.025004791520295,"distance_to_district":9.965781217890562},"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}},"gpstype":"Gpstype","license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"organizer_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"event_price":{"key":{"long_desc":"LongDesc","type":"Type","description":"Description","short_desc":"ShortDesc","language":"Language","price":4.965218492984954,"pstd":"Pstd","price_rid":"PriceRID","var_rid":"VarRID"}},"odh_active":1,"event_property":{"event_organizer_id":"EventOrganizerId","is_bookable":1,"registration_required":1,"ticket_required":1,"included_in_suedtirol_guest_pass":1,"event_classification_id":"EventClassificationId"},"self":"Self","source":"Source","smg_active":1,"image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"event_additional_infos":{"key":{"what_to_bring":"WhatToBring","cancellation_modality":"CancellationModality","language":"Language","reg":"Reg","registration":"Registration","service_description":"ServiceDescription","mplace":"Mplace","meeting_point":"MeetingPoint","location":"Location"}},"districts":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"contact_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"event_dates_begin":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"ticket":"Ticket","has_language":["HasLanguage","HasLanguage"],"topics":[{"topic_rid":"TopicRID","self":"Self","topic_info":"TopicInfo"},{"topic_rid":"TopicRID","self":"Self","topic_info":"TopicInfo"}],"district_id":"DistrictId","event_date_counter":5,"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"org_rid":"OrgRID","location_info":{"municipality_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"tv_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"region_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"district_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"area_info":{"self":"Self","id":"Id","name":{"key":"Name"}}},"event_dates_end":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"event_variants":[{"order":7,"is_standard":1,"price":1.1730742509559433,"variant_category_id":"VariantCategoryId","tax_rate_id":"TaxRateId","variant_id":"VariantId","combined_sales_ids":["CombinedSalesIds","CombinedSalesIds"],"name":{"key":"Name"},"is_ignored_in_availability":1},{"order":7,"is_standard":1,"price":1.1730742509559433,"variant_category_id":"VariantCategoryId","tax_rate_id":"TaxRateId","variant_id":"VariantId","combined_sales_ids":["CombinedSalesIds","CombinedSalesIds"],"name":{"key":"Name"},"is_ignored_in_availability":1}],"classification_rid":"ClassificationRID","last_change":"2000-01-23T04:56:07.000+00:00","odh_tags":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"shortname":"Shortname","altitude":7.061401241503109}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/Event",
    #    headers=headers,
    #    json=event_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_event(client: TestClient):
    """Test case for single_event

    GET Event Single
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
    #    "/v1/Event/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_id_put(client: TestClient):
    """Test case for v1_event_id_put

    PUT Modify existing Event
    """
    event_linked = {"event_date":[{"single_days":1,"max_persons":1,"ticket":1,"event_calculated_days":[{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2},{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2}],"event_calculated_day":{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2},"price_from":7.386281948385884,"is_bookable":1,"is_cancelled":1,"day_rid":"DayRID","event_date_additional_info":{"key":{"description":"Description","guide":"Guide","language":"Language","cancellation_description":"CancellationDescription","registration_within":"RegistrationWithin"}},"event_date_id":"EventDateId","from":"2000-01-23T04:56:07.000+00:00","event_date_ticket_info":{"active":1,"online_contingent":6,"online_sale_until":1},"cancelled":"Cancelled","entrance":"Entrance","active":1,"event_variant_ids":["EventVariantIds","EventVariantIds"],"begin":"Begin","end":"End","to":"2000-01-23T04:56:07.000+00:00","min_persons":1},{"single_days":1,"max_persons":1,"ticket":1,"event_calculated_days":[{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2},{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2}],"event_calculated_day":{"availability_low":1,"calculated_day_id":"CalculatedDayId","sold_out":1,"begin":"Begin","day":"2000-01-23T04:56:07.000+00:00","event_date_calculated_day_variant":[{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4},{"availability_low":1,"variant_id":"VariantId","availability_calculated_value":4}],"c_day_rid":"CDayRID","availability_calculated_value":2},"price_from":7.386281948385884,"is_bookable":1,"is_cancelled":1,"day_rid":"DayRID","event_date_additional_info":{"key":{"description":"Description","guide":"Guide","language":"Language","cancellation_description":"CancellationDescription","registration_within":"RegistrationWithin"}},"event_date_id":"EventDateId","from":"2000-01-23T04:56:07.000+00:00","event_date_ticket_info":{"active":1,"online_contingent":6,"online_sale_until":1},"cancelled":"Cancelled","entrance":"Entrance","active":1,"event_variant_ids":["EventVariantIds","EventVariantIds"],"begin":"Begin","end":"End","to":"2000-01-23T04:56:07.000+00:00","min_persons":1}],"tag_ids":["TagIds","TagIds"],"published_on":["PublishedOn","PublishedOn"],"date_begin":"2000-01-23T04:56:07.000+00:00","sign_on":"SignOn","latitude":5.637376656633329,"mapping":{"key":{"key":"Mapping"}},"date_end":"2000-01-23T04:56:07.000+00:00","altitude_unitof_measure":"AltitudeUnitofMeasure","additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"smg_tags":["SmgTags","SmgTags"],"topic_rids":["TopicRIDs","TopicRIDs"],"event_publisher":[{"ranc":9,"publisher_rid":"PublisherRID","publication_status":"PublicationStatus","publish":3},{"ranc":9,"publisher_rid":"PublisherRID","publication_status":"PublicationStatus","publish":3}],"gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"district_ids":["DistrictIds","DistrictIds"],"event_urls":[{"type":"Type","active":1,"url":{"key":"Url"}},{"type":"Type","active":1,"url":{"key":"Url"}}],"longitude":2.3021358869347655,"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"event_booking":{"bookable_from":"2000-01-23T04:56:07.000+00:00","booking_url":{"key":{"url":"Url"}},"bookable_to":"2000-01-23T04:56:07.000+00:00","booking_active":1},"first_import":"2000-01-23T04:56:07.000+00:00","id":"Id","distance_info":{"distance_to_municipality":5.025004791520295,"distance_to_district":9.965781217890562},"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}},"gpstype":"Gpstype","license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"organizer_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"event_price":{"key":{"long_desc":"LongDesc","type":"Type","description":"Description","short_desc":"ShortDesc","language":"Language","price":4.965218492984954,"pstd":"Pstd","price_rid":"PriceRID","var_rid":"VarRID"}},"odh_active":1,"event_property":{"event_organizer_id":"EventOrganizerId","is_bookable":1,"registration_required":1,"ticket_required":1,"included_in_suedtirol_guest_pass":1,"event_classification_id":"EventClassificationId"},"self":"Self","source":"Source","smg_active":1,"image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"event_additional_infos":{"key":{"what_to_bring":"WhatToBring","cancellation_modality":"CancellationModality","language":"Language","reg":"Reg","registration":"Registration","service_description":"ServiceDescription","mplace":"Mplace","meeting_point":"MeetingPoint","location":"Location"}},"districts":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"contact_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"event_dates_begin":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"ticket":"Ticket","has_language":["HasLanguage","HasLanguage"],"topics":[{"topic_rid":"TopicRID","self":"Self","topic_info":"TopicInfo"},{"topic_rid":"TopicRID","self":"Self","topic_info":"TopicInfo"}],"district_id":"DistrictId","event_date_counter":5,"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"org_rid":"OrgRID","location_info":{"municipality_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"tv_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"region_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"district_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"area_info":{"self":"Self","id":"Id","name":{"key":"Name"}}},"event_dates_end":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"event_variants":[{"order":7,"is_standard":1,"price":1.1730742509559433,"variant_category_id":"VariantCategoryId","tax_rate_id":"TaxRateId","variant_id":"VariantId","combined_sales_ids":["CombinedSalesIds","CombinedSalesIds"],"name":{"key":"Name"},"is_ignored_in_availability":1},{"order":7,"is_standard":1,"price":1.1730742509559433,"variant_category_id":"VariantCategoryId","tax_rate_id":"TaxRateId","variant_id":"VariantId","combined_sales_ids":["CombinedSalesIds","CombinedSalesIds"],"name":{"key":"Name"},"is_ignored_in_availability":1}],"classification_rid":"ClassificationRID","last_change":"2000-01-23T04:56:07.000+00:00","odh_tags":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"shortname":"Shortname","altitude":7.061401241503109}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/Event/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=event_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_id_delete(client: TestClient):
    """Test case for v1_event_id_delete

    DELETE Event by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/Event/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_event_topics_get(client: TestClient):
    """Test case for v1_event_topics_get

    GET Event Topic List
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
    #    "/v1/EventTopics",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_event_topics(client: TestClient):
    """Test case for single_event_topics

    GET Event Topic Single
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
    #    "/v1/EventTopics/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

