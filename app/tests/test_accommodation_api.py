# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.acco_features import AccoFeatures  # noqa: F401
from openapi_server.models.acco_types import AccoTypes  # noqa: F401
from openapi_server.models.accommodation_room_linked import AccommodationRoomLinked  # noqa: F401
from openapi_server.models.accommodation_v2 import AccommodationV2  # noqa: F401
from openapi_server.models.accommodation_v2_json_result import AccommodationV2JsonResult  # noqa: F401
from openapi_server.models.accommodation_v2_json_result_with_booking_info import AccommodationV2JsonResultWithBookingInfo  # noqa: F401
from openapi_server.models.mss_result_json_result_with_booking_info import MssResultJsonResultWithBookingInfo  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_accommodation_list(client: TestClient):
    """Test case for accommodation_list

    GET Accommodation List
    """
    params = [("pagenumber", 1),     ("pagesize", 56),     ("seed", 'seed_example'),     ("categoryfilter", 'categoryfilter_example'),     ("typefilter", 'typefilter_example'),     ("boardfilter", 'boardfilter_example'),     ("featurefilter", 'featurefilter_example'),     ("featureidfilter", 'featureidfilter_example'),     ("themefilter", 'themefilter_example'),     ("badgefilter", 'badgefilter_example'),     ("idfilter", 'idfilter_example'),     ("locfilter", 'locfilter_example'),     ("altitudefilter", 'altitudefilter_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("source", 'source_example'),     ("odhactive", True),     ("active", True),     ("bookablefilter", True),     ("arrival", 'arrival_example'),     ("departure", 'departure_example'),     ("roominfo", '1-18,18'),     ("bokfilter", 'hgv'),     ("msssource", 'sinfo'),     ("availabilitychecklanguage", 'en'),     ("detail", '0'),     ("tagfilter", 'tagfilter_example'),     ("availabilitycheck", True),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("publishedon", 'publishedon_example'),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Accommodation",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_accommodation_post(client: TestClient):
    """Test case for v1_accommodation_post

    POST Insert new Accommodation
    """
    accommodation_v2 = {"has_apartment":1,"tag_ids":["TagIds","TagIds"],"published_on":["PublishedOn","PublishedOn"],"latitude":6.84685269835264,"mapping":{"key":{"key":"Mapping"}},"gastronomy_id":"GastronomyId","altitude_unitof_measure":"AltitudeUnitofMeasure","hgv_id":"HgvId","main_language":"MainLanguage","additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"smg_tags":["SmgTags","SmgTags"],"trust_you_active":1,"trust_you_state":4,"is_bookable":1,"trust_you_score":3.616076749251911,"gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"representation":4,"longitude":7.457744773683766,"acco_category":{"id":"Id","self":"Self"},"is_camping":1,"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"independent_data":{"independent_description":{"key":{"backlink_url":"BacklinkUrl","description":"Description","language":"Language","commitment_to_accessibility_url":"CommitmentToAccessibilityUrl"}},"independent_rating":9,"enabled":1},"active":1,"tourism_verein_id":"TourismVereinId","has_room":1,"first_import":"2000-01-23T04:56:07.000+00:00","mss_response_short":[{"cheapest_offer_hb":6.778324963048013,"offer_show":3,"cheapest_offer_ws":1.284659006116532,"cheapest_offer_fb":6.878052220127876,"offer_typ":6,"onlinepayment_prepayment":"OnlinepaymentPrepayment","cheapest_offer_string":"CheapestOfferString","onlinepayment_methods":"OnlinepaymentMethods","channel_id":"ChannelID","offer_gid":"OfferGid","cheapest_offer_bb":2.8841621266687802,"offer_id":"OfferId","room_details":[{"roomdesc":"Roomdesc","room_channel_link":"RoomChannelLink","price_ws":3.0937452626664474,"price_fb":7.058770351582356,"roomtype":0,"price_hb":0.8851374739011653,"price_bb":7.143538047012306,"roomfree":4,"room_id":"RoomId","roomtitle":"Roomtitle","payment_term":{"description":"Description","bank":{"iban":"Iban","swift":"Swift","name":"Name"},"ccards":5,"priority":3,"id":"Id","prepayment":7,"methods":3},"price_ai":6.519180951018382,"total_price_string":"TotalPriceString","roommin":7,"offer_id":"OfferId","roomstd":3,"roommax":8,"room_pictures":[{"pictureurl":"Pictureurl"},{"pictureurl":"Pictureurl"}],"room_seq":6,"total_price":3.353193347011243,"cancel_policy":{"penalties":[{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6},{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6}],"description":"Description","refundable":4,"id":"Id","refundable_until":"2000-01-23T04:56:07.000+00:00"}},{"roomdesc":"Roomdesc","room_channel_link":"RoomChannelLink","price_ws":3.0937452626664474,"price_fb":7.058770351582356,"roomtype":0,"price_hb":0.8851374739011653,"price_bb":7.143538047012306,"roomfree":4,"room_id":"RoomId","roomtitle":"Roomtitle","payment_term":{"description":"Description","bank":{"iban":"Iban","swift":"Swift","name":"Name"},"ccards":5,"priority":3,"id":"Id","prepayment":7,"methods":3},"price_ai":6.519180951018382,"total_price_string":"TotalPriceString","roommin":7,"offer_id":"OfferId","roomstd":3,"roommax":8,"room_pictures":[{"pictureurl":"Pictureurl"},{"pictureurl":"Pictureurl"}],"room_seq":6,"total_price":3.353193347011243,"cancel_policy":{"penalties":[{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6},{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6}],"description":"Description","refundable":4,"id":"Id","refundable_until":"2000-01-23T04:56:07.000+00:00"}}],"hotel_id":9,"cheapest_offer_detail":[{"price":7.260521264802104,"cheapest_room_combination_detail":[{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"},{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"}],"service":"Service"},{"price":7.260521264802104,"cheapest_room_combination_detail":[{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"},{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"}],"service":"Service"}],"a0_rid":"A0RID","channellink":"Channellink","cheapest_offer":6.965117697638846,"cheapest_offer_ai":5.944895607614016,"onlinepayment_c_cards":"OnlinepaymentCCards","bookable":1},{"cheapest_offer_hb":6.778324963048013,"offer_show":3,"cheapest_offer_ws":1.284659006116532,"cheapest_offer_fb":6.878052220127876,"offer_typ":6,"onlinepayment_prepayment":"OnlinepaymentPrepayment","cheapest_offer_string":"CheapestOfferString","onlinepayment_methods":"OnlinepaymentMethods","channel_id":"ChannelID","offer_gid":"OfferGid","cheapest_offer_bb":2.8841621266687802,"offer_id":"OfferId","room_details":[{"roomdesc":"Roomdesc","room_channel_link":"RoomChannelLink","price_ws":3.0937452626664474,"price_fb":7.058770351582356,"roomtype":0,"price_hb":0.8851374739011653,"price_bb":7.143538047012306,"roomfree":4,"room_id":"RoomId","roomtitle":"Roomtitle","payment_term":{"description":"Description","bank":{"iban":"Iban","swift":"Swift","name":"Name"},"ccards":5,"priority":3,"id":"Id","prepayment":7,"methods":3},"price_ai":6.519180951018382,"total_price_string":"TotalPriceString","roommin":7,"offer_id":"OfferId","roomstd":3,"roommax":8,"room_pictures":[{"pictureurl":"Pictureurl"},{"pictureurl":"Pictureurl"}],"room_seq":6,"total_price":3.353193347011243,"cancel_policy":{"penalties":[{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6},{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6}],"description":"Description","refundable":4,"id":"Id","refundable_until":"2000-01-23T04:56:07.000+00:00"}},{"roomdesc":"Roomdesc","room_channel_link":"RoomChannelLink","price_ws":3.0937452626664474,"price_fb":7.058770351582356,"roomtype":0,"price_hb":0.8851374739011653,"price_bb":7.143538047012306,"roomfree":4,"room_id":"RoomId","roomtitle":"Roomtitle","payment_term":{"description":"Description","bank":{"iban":"Iban","swift":"Swift","name":"Name"},"ccards":5,"priority":3,"id":"Id","prepayment":7,"methods":3},"price_ai":6.519180951018382,"total_price_string":"TotalPriceString","roommin":7,"offer_id":"OfferId","roomstd":3,"roommax":8,"room_pictures":[{"pictureurl":"Pictureurl"},{"pictureurl":"Pictureurl"}],"room_seq":6,"total_price":3.353193347011243,"cancel_policy":{"penalties":[{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6},{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6}],"description":"Description","refundable":4,"id":"Id","refundable_until":"2000-01-23T04:56:07.000+00:00"}}],"hotel_id":9,"cheapest_offer_detail":[{"price":7.260521264802104,"cheapest_room_combination_detail":[{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"},{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"}],"service":"Service"},{"price":7.260521264802104,"cheapest_room_combination_detail":[{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"},{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"}],"service":"Service"}],"a0_rid":"A0RID","channellink":"Channellink","cheapest_offer":6.965117697638846,"cheapest_offer_ai":5.944895607614016,"onlinepayment_c_cards":"OnlinepaymentCCards","bookable":1}],"id":"Id","acco_special_features":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"marketing_group_ids":["MarketingGroupIds","MarketingGroupIds"],"theme_ids":["ThemeIds","ThemeIds"],"distance_info":{"distance_to_municipality":5.025004791520295,"distance_to_district":9.965781217890562},"gpstype":"Gpstype","license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"odh_active":1,"review":{"key":{"score":5.962133916683182,"active":1,"results":5,"state":"State","state_integer":2,"review_id":"ReviewId","provider":"Provider"}},"self":"Self","is_gastronomy":1,"acco_detail":{"key":{"zip":"Zip","email":"Email","lastname":"Lastname","vat":"Vat","website":"Website","city":"City","name_addition":"NameAddition","mobile":"Mobile","name":"Name","firstname":"Firstname","longdesc":"Longdesc","language":"Language","shortdesc":"Shortdesc","phone":"Phone","street":"Street","fax":"Fax","country_code":"CountryCode"}},"rate_plan":[{"rate_plan_id":"RatePlanId","long_description":{"key":"LongDescription"},"last_update":"2000-01-23T04:56:07.000+00:00","charge_type":"ChargeType","visibility":"Visibility","code":"Code","name":{"key":"Name"},"short_description":{"key":"ShortDescription"}},{"rate_plan_id":"RatePlanId","long_description":{"key":"LongDescription"},"last_update":"2000-01-23T04:56:07.000+00:00","charge_type":"ChargeType","visibility":"Visibility","code":"Code","name":{"key":"Name"},"short_description":{"key":"ShortDescription"}}],"board_ids":["BoardIds","BoardIds"],"source":"Source","acco_hgv_info":{"price_from":0,"available_from":"AvailableFrom","bookable":1},"is_accommodation":1,"acco_badges":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"smg_active":1,"acco_overview":{"max_persons":0,"camping_toilettes":8,"apartment_room_size":1,"double_rooms":4,"camping_washingstands":9,"baggage_service_from":"BaggageServiceFrom","camping_units":8,"single_rooms":5,"apartment_beds":3,"reception_open_from":"ReceptionOpenFrom","baggage_service_to":"BaggageServiceTo","camping_douches":4,"garage_parkings":1,"room_service_to":"RoomServiceTo","triple_rooms":6,"quadruple_rooms":8,"room_service_from":"RoomServiceFrom","reception_open_to":"ReceptionOpenTo","check_in_to":"CheckInTo","camping_washrooms":6,"check_out_to":"CheckOutTo","apartments":4,"check_in_from":"CheckInFrom","total_rooms":7,"check_out_from":"CheckOutFrom","outdoor_parkings":2},"trust_you_id":"TrustYouID","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"features":[{"room_amenity_codes":[7,7],"ota_codes":"OtaCodes","hgv_id":"HgvId","self":"Self","id":"Id","name":"Name"},{"room_amenity_codes":[7,7],"ota_codes":"OtaCodes","hgv_id":"HgvId","self":"Self","id":"Id","name":"Name"}],"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"acco_themes":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"acco_lts_info":{"price_from":9,"price_from_per_unit":0},"tv_member":1,"acco_type":{"id":"Id","self":"Self"},"has_language":["HasLanguage","HasLanguage"],"district_id":"DistrictId","acco_room_info":[{"self":"Self","id":"Id","source":"Source"},{"self":"Self","id":"Id","source":"Source"}],"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"location_info":{"municipality_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"tv_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"region_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"district_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"area_info":{"self":"Self","id":"Id","name":{"key":"Name"}}},"special_features_ids":["SpecialFeaturesIds","SpecialFeaturesIds"],"acco_boards":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"acco_properties":{"is_camping":1,"has_apartment":1,"is_accommodation":1,"is_bookable":1,"has_room":1,"has_pitches":1,"has_dorm":1,"is_gastronomy":1,"tv_member":1},"acco_category_id":"AccoCategoryId","last_change":"2000-01-23T04:56:07.000+00:00","odh_tags":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"acco_type_id":"AccoTypeId","trust_you_results":2,"shortname":"Shortname","badge_ids":["BadgeIds","BadgeIds"],"operation_schedule":[{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]},{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]}],"acco_booking_channel":[{"portalname":"Portalname","booking_id":"BookingId","id":"Id","pos1_id":"Pos1ID"},{"portalname":"Portalname","booking_id":"BookingId","id":"Id","pos1_id":"Pos1ID"}],"altitude":1.1730742509559433}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/Accommodation",
    #    headers=headers,
    #    json=accommodation_v2,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_accommodation(client: TestClient):
    """Test case for single_accommodation

    GET Accommodation Single
    """
    params = [("idsource", 'lts'),     ("availabilitychecklanguage", 'en'),     ("boardfilter", 'boardfilter_example'),     ("arrival", 'arrival_example'),     ("departure", 'departure_example'),     ("roominfo", '1-18,18'),     ("bokfilter", 'hgv'),     ("msssource", 'sinfo'),     ("availabilitycheck", True),     ("detail", '0'),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Accommodation/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_accommodation_id_put(client: TestClient):
    """Test case for v1_accommodation_id_put

    PUT Modify existing Accommodation
    """
    accommodation_v2 = {"has_apartment":1,"tag_ids":["TagIds","TagIds"],"published_on":["PublishedOn","PublishedOn"],"latitude":6.84685269835264,"mapping":{"key":{"key":"Mapping"}},"gastronomy_id":"GastronomyId","altitude_unitof_measure":"AltitudeUnitofMeasure","hgv_id":"HgvId","main_language":"MainLanguage","additional_properties":{"key":""},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"smg_tags":["SmgTags","SmgTags"],"trust_you_active":1,"trust_you_state":4,"is_bookable":1,"trust_you_score":3.616076749251911,"gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"representation":4,"longitude":7.457744773683766,"acco_category":{"id":"Id","self":"Self"},"is_camping":1,"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"independent_data":{"independent_description":{"key":{"backlink_url":"BacklinkUrl","description":"Description","language":"Language","commitment_to_accessibility_url":"CommitmentToAccessibilityUrl"}},"independent_rating":9,"enabled":1},"active":1,"tourism_verein_id":"TourismVereinId","has_room":1,"first_import":"2000-01-23T04:56:07.000+00:00","mss_response_short":[{"cheapest_offer_hb":6.778324963048013,"offer_show":3,"cheapest_offer_ws":1.284659006116532,"cheapest_offer_fb":6.878052220127876,"offer_typ":6,"onlinepayment_prepayment":"OnlinepaymentPrepayment","cheapest_offer_string":"CheapestOfferString","onlinepayment_methods":"OnlinepaymentMethods","channel_id":"ChannelID","offer_gid":"OfferGid","cheapest_offer_bb":2.8841621266687802,"offer_id":"OfferId","room_details":[{"roomdesc":"Roomdesc","room_channel_link":"RoomChannelLink","price_ws":3.0937452626664474,"price_fb":7.058770351582356,"roomtype":0,"price_hb":0.8851374739011653,"price_bb":7.143538047012306,"roomfree":4,"room_id":"RoomId","roomtitle":"Roomtitle","payment_term":{"description":"Description","bank":{"iban":"Iban","swift":"Swift","name":"Name"},"ccards":5,"priority":3,"id":"Id","prepayment":7,"methods":3},"price_ai":6.519180951018382,"total_price_string":"TotalPriceString","roommin":7,"offer_id":"OfferId","roomstd":3,"roommax":8,"room_pictures":[{"pictureurl":"Pictureurl"},{"pictureurl":"Pictureurl"}],"room_seq":6,"total_price":3.353193347011243,"cancel_policy":{"penalties":[{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6},{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6}],"description":"Description","refundable":4,"id":"Id","refundable_until":"2000-01-23T04:56:07.000+00:00"}},{"roomdesc":"Roomdesc","room_channel_link":"RoomChannelLink","price_ws":3.0937452626664474,"price_fb":7.058770351582356,"roomtype":0,"price_hb":0.8851374739011653,"price_bb":7.143538047012306,"roomfree":4,"room_id":"RoomId","roomtitle":"Roomtitle","payment_term":{"description":"Description","bank":{"iban":"Iban","swift":"Swift","name":"Name"},"ccards":5,"priority":3,"id":"Id","prepayment":7,"methods":3},"price_ai":6.519180951018382,"total_price_string":"TotalPriceString","roommin":7,"offer_id":"OfferId","roomstd":3,"roommax":8,"room_pictures":[{"pictureurl":"Pictureurl"},{"pictureurl":"Pictureurl"}],"room_seq":6,"total_price":3.353193347011243,"cancel_policy":{"penalties":[{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6},{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6}],"description":"Description","refundable":4,"id":"Id","refundable_until":"2000-01-23T04:56:07.000+00:00"}}],"hotel_id":9,"cheapest_offer_detail":[{"price":7.260521264802104,"cheapest_room_combination_detail":[{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"},{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"}],"service":"Service"},{"price":7.260521264802104,"cheapest_room_combination_detail":[{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"},{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"}],"service":"Service"}],"a0_rid":"A0RID","channellink":"Channellink","cheapest_offer":6.965117697638846,"cheapest_offer_ai":5.944895607614016,"onlinepayment_c_cards":"OnlinepaymentCCards","bookable":1},{"cheapest_offer_hb":6.778324963048013,"offer_show":3,"cheapest_offer_ws":1.284659006116532,"cheapest_offer_fb":6.878052220127876,"offer_typ":6,"onlinepayment_prepayment":"OnlinepaymentPrepayment","cheapest_offer_string":"CheapestOfferString","onlinepayment_methods":"OnlinepaymentMethods","channel_id":"ChannelID","offer_gid":"OfferGid","cheapest_offer_bb":2.8841621266687802,"offer_id":"OfferId","room_details":[{"roomdesc":"Roomdesc","room_channel_link":"RoomChannelLink","price_ws":3.0937452626664474,"price_fb":7.058770351582356,"roomtype":0,"price_hb":0.8851374739011653,"price_bb":7.143538047012306,"roomfree":4,"room_id":"RoomId","roomtitle":"Roomtitle","payment_term":{"description":"Description","bank":{"iban":"Iban","swift":"Swift","name":"Name"},"ccards":5,"priority":3,"id":"Id","prepayment":7,"methods":3},"price_ai":6.519180951018382,"total_price_string":"TotalPriceString","roommin":7,"offer_id":"OfferId","roomstd":3,"roommax":8,"room_pictures":[{"pictureurl":"Pictureurl"},{"pictureurl":"Pictureurl"}],"room_seq":6,"total_price":3.353193347011243,"cancel_policy":{"penalties":[{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6},{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6}],"description":"Description","refundable":4,"id":"Id","refundable_until":"2000-01-23T04:56:07.000+00:00"}},{"roomdesc":"Roomdesc","room_channel_link":"RoomChannelLink","price_ws":3.0937452626664474,"price_fb":7.058770351582356,"roomtype":0,"price_hb":0.8851374739011653,"price_bb":7.143538047012306,"roomfree":4,"room_id":"RoomId","roomtitle":"Roomtitle","payment_term":{"description":"Description","bank":{"iban":"Iban","swift":"Swift","name":"Name"},"ccards":5,"priority":3,"id":"Id","prepayment":7,"methods":3},"price_ai":6.519180951018382,"total_price_string":"TotalPriceString","roommin":7,"offer_id":"OfferId","roomstd":3,"roommax":8,"room_pictures":[{"pictureurl":"Pictureurl"},{"pictureurl":"Pictureurl"}],"room_seq":6,"total_price":3.353193347011243,"cancel_policy":{"penalties":[{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6},{"percent":0,"datefrom":"2000-01-23T04:56:07.000+00:00","daysarrival":6}],"description":"Description","refundable":4,"id":"Id","refundable_until":"2000-01-23T04:56:07.000+00:00"}}],"hotel_id":9,"cheapest_offer_detail":[{"price":7.260521264802104,"cheapest_room_combination_detail":[{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"},{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"}],"service":"Service"},{"price":7.260521264802104,"cheapest_room_combination_detail":[{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"},{"room_seq":4,"price":1.041444916118296,"room_free":4,"room_id":"RoomId"}],"service":"Service"}],"a0_rid":"A0RID","channellink":"Channellink","cheapest_offer":6.965117697638846,"cheapest_offer_ai":5.944895607614016,"onlinepayment_c_cards":"OnlinepaymentCCards","bookable":1}],"id":"Id","acco_special_features":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"marketing_group_ids":["MarketingGroupIds","MarketingGroupIds"],"theme_ids":["ThemeIds","ThemeIds"],"distance_info":{"distance_to_municipality":5.025004791520295,"distance_to_district":9.965781217890562},"gpstype":"Gpstype","license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"odh_active":1,"review":{"key":{"score":5.962133916683182,"active":1,"results":5,"state":"State","state_integer":2,"review_id":"ReviewId","provider":"Provider"}},"self":"Self","is_gastronomy":1,"acco_detail":{"key":{"zip":"Zip","email":"Email","lastname":"Lastname","vat":"Vat","website":"Website","city":"City","name_addition":"NameAddition","mobile":"Mobile","name":"Name","firstname":"Firstname","longdesc":"Longdesc","language":"Language","shortdesc":"Shortdesc","phone":"Phone","street":"Street","fax":"Fax","country_code":"CountryCode"}},"rate_plan":[{"rate_plan_id":"RatePlanId","long_description":{"key":"LongDescription"},"last_update":"2000-01-23T04:56:07.000+00:00","charge_type":"ChargeType","visibility":"Visibility","code":"Code","name":{"key":"Name"},"short_description":{"key":"ShortDescription"}},{"rate_plan_id":"RatePlanId","long_description":{"key":"LongDescription"},"last_update":"2000-01-23T04:56:07.000+00:00","charge_type":"ChargeType","visibility":"Visibility","code":"Code","name":{"key":"Name"},"short_description":{"key":"ShortDescription"}}],"board_ids":["BoardIds","BoardIds"],"source":"Source","acco_hgv_info":{"price_from":0,"available_from":"AvailableFrom","bookable":1},"is_accommodation":1,"acco_badges":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"smg_active":1,"acco_overview":{"max_persons":0,"camping_toilettes":8,"apartment_room_size":1,"double_rooms":4,"camping_washingstands":9,"baggage_service_from":"BaggageServiceFrom","camping_units":8,"single_rooms":5,"apartment_beds":3,"reception_open_from":"ReceptionOpenFrom","baggage_service_to":"BaggageServiceTo","camping_douches":4,"garage_parkings":1,"room_service_to":"RoomServiceTo","triple_rooms":6,"quadruple_rooms":8,"room_service_from":"RoomServiceFrom","reception_open_to":"ReceptionOpenTo","check_in_to":"CheckInTo","camping_washrooms":6,"check_out_to":"CheckOutTo","apartments":4,"check_in_from":"CheckInFrom","total_rooms":7,"check_out_from":"CheckOutFrom","outdoor_parkings":2},"trust_you_id":"TrustYouID","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"features":[{"room_amenity_codes":[7,7],"ota_codes":"OtaCodes","hgv_id":"HgvId","self":"Self","id":"Id","name":"Name"},{"room_amenity_codes":[7,7],"ota_codes":"OtaCodes","hgv_id":"HgvId","self":"Self","id":"Id","name":"Name"}],"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"acco_themes":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"acco_lts_info":{"price_from":9,"price_from_per_unit":0},"tv_member":1,"acco_type":{"id":"Id","self":"Self"},"has_language":["HasLanguage","HasLanguage"],"district_id":"DistrictId","acco_room_info":[{"self":"Self","id":"Id","source":"Source"},{"self":"Self","id":"Id","source":"Source"}],"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"location_info":{"municipality_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"tv_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"region_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"district_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"area_info":{"self":"Self","id":"Id","name":{"key":"Name"}}},"special_features_ids":["SpecialFeaturesIds","SpecialFeaturesIds"],"acco_boards":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"acco_properties":{"is_camping":1,"has_apartment":1,"is_accommodation":1,"is_bookable":1,"has_room":1,"has_pitches":1,"has_dorm":1,"is_gastronomy":1,"tv_member":1},"acco_category_id":"AccoCategoryId","last_change":"2000-01-23T04:56:07.000+00:00","odh_tags":[{"id":"Id","self":"Self"},{"id":"Id","self":"Self"}],"acco_type_id":"AccoTypeId","trust_you_results":2,"shortname":"Shortname","badge_ids":["BadgeIds","BadgeIds"],"operation_schedule":[{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]},{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]}],"acco_booking_channel":[{"portalname":"Portalname","booking_id":"BookingId","id":"Id","pos1_id":"Pos1ID"},{"portalname":"Portalname","booking_id":"BookingId","id":"Id","pos1_id":"Pos1ID"}],"altitude":1.1730742509559433}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/Accommodation/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=accommodation_v2,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_accommodation_id_delete(client: TestClient):
    """Test case for v1_accommodation_id_delete

    DELETE Accommodation by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/Accommodation/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_accommodation_types_get(client: TestClient):
    """Test case for v1_accommodation_types_get

    GET Accommodation Types List
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
    #    "/v1/AccommodationTypes",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_accommodation_types(client: TestClient):
    """Test case for single_accommodation_types

    GET Accommodation Types Single
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
    #    "/v1/AccommodationTypes/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_accommodation_features_get(client: TestClient):
    """Test case for v1_accommodation_features_get

    GET Accommodation Feature List (LTS Features)
    """
    params = [("language", 'language_example'),     ("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("seed", 'seed_example'),     ("ltst0idfilter", 'ltst0idfilter_example'),     ("source", 'source_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/AccommodationFeatures",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_accommodation_features(client: TestClient):
    """Test case for single_accommodation_features

    GET Accommodation Feature Single (LTS Features)
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
    #    "/v1/AccommodationFeatures/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_accommodation_room_list(client: TestClient):
    """Test case for accommodation_room_list

    GET Accommodation Room Info by Accommodation
    """
    params = [("accoid", 'accoid_example'),     ("idsource", 'lts'),     ("source", 'source_example'),     ("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("getall", False),     ("fields", ['fields_example']),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("updatefrom", 'updatefrom_example'),     ("seed", 'seed_example'),     ("publishedon", 'publishedon_example'),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/AccommodationRoom",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_accommodation_room(client: TestClient):
    """Test case for single_accommodation_room

    GET Accommodation Room Info Single
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
    #    "/v1/AccommodationRoom/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_accommodation_available_post(client: TestClient):
    """Test case for v1_accommodation_available_post

    POST Pass Accommodation Ids and get Accommodations with Availability Information / Availability Information Only <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Accommodation-Workflow#availability-search\" target=\"_blank\">Wiki Availability Search</a>
    """
    body = 'body_example'
    params = [("availabilitychecklanguage", 'en'),     ("boardfilter", 'boardfilter_example'),     ("arrival", 'arrival_example'),     ("departure", 'departure_example'),     ("roominfo", '1-18,18'),     ("bokfilter", 'hgv'),     ("msssource", 'sinfo'),     ("detail", '0'),     ("locfilter", 'locfilter_example'),     ("publishedon", 'publishedon_example'),     ("availabilityonly", False),     ("usemsscache", False),     ("uselcscache", True),     ("removeduplicatesfrom", 'removeduplicatesfrom_example'),     ("ltsapiversion", 'v1')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/AccommodationAvailable",
    #    headers=headers,
    #    json=body,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_availability_check_post(client: TestClient):
    """Test case for v1_availability_check_post

    POST Pass Accommodation Ids and get Accommodations with Availability Information / Availability Information Only
    """
    body = 'body_example'
    params = [("availabilitychecklanguage", 'en'),     ("boardfilter", 'boardfilter_example'),     ("arrival", 'arrival_example'),     ("departure", 'departure_example'),     ("roominfo", '1-18,18'),     ("bokfilter", 'hgv'),     ("msssource", 'sinfo'),     ("detail", '0'),     ("locfilter", 'locfilter_example'),     ("publishedon", 'idm-marketplace'),     ("usemsscache", False),     ("uselcscache", False),     ("removeduplicatesfrom", 'removeduplicatesfrom_example'),     ("ltsapiversion", 'v1')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/AvailabilityCheck",
    #    headers=headers,
    #    json=body,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

