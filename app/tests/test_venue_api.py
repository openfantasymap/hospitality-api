# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.dd_venue_codes import DDVenueCodes  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.venue_v2 import VenueV2  # noqa: F401
from openapi_server.models.venue_v2_json_result import VenueV2JsonResult  # noqa: F401


def test_v1_venue_get(client: TestClient):
    """Test case for v1_venue_get

    GET Venue List
    """
    params = [("language", 'language_example'),     ("pagenumber", 1),     ("pagesize", 56),     ("categoryfilter", 'categoryfilter_example'),     ("idlist", 'idlist_example'),     ("locfilter", 'locfilter_example'),     ("featurefilter", 'featurefilter_example'),     ("setuptypefilter", 'setuptypefilter_example'),     ("odhtagfilter", 'odhtagfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("source", 'source_example'),     ("active", True),     ("publishedon", 'publishedon_example'),     ("updatefrom", 'updatefrom_example'),     ("langfilter", 'langfilter_example'),     ("seed", 'seed_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Venue",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_venue_post(client: TestClient):
    """Test case for v1_venue_post

    POST Insert new Venue
    """
    venue_v2 = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"published_on":["PublishedOn","PublishedOn"],"tag_ids":["TagIds","TagIds"],"mapping":{"key":{"key":"Mapping"}},"self":"Self","source":"Source","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"contact_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"additional_properties":{"echarging_data_properties":{"payment_info":"PaymentInfo","car_parking_space_next_to_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"vertical_road_sign":1,"barrierfree":"Barrierefrei","access_type_info":"AccessTypeInfo","car_parking_space_behind_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"survey_annotations":{"key":"SurveyAnnotations"},"stepless_sidewalk_connection":1,"charging_cable_length":7,"horizontal_floor_road_sign":1,"charging_station_accessible":1,"covered":1,"survey_type":"SurveyType","capacity":5,"state":"UNAVAILABLE","survey_date":"2000-01-23T04:56:07.000+00:00","shielding_post_in_front_of_station":1,"charging_pistol_operation_height":2,"charging_pistol_types":["ChargingPistolTypes","ChargingPistolTypes"],"display_or_card_reader_operation_height":5,"access_type":"PUBLIC"},"poi_age_data_properties":{"age_from":8,"age_to":9},"road_incident_properties":"{}","suedtirol_wein_company_data_properties":{"has_deliveryservice":1,"socials_linked_in":"SocialsLinkedIn","is_wine_summit":1,"is_wine_stories":1,"is_sparkling_wineassociation":1,"openingtimes_wineshop":{"key":"OpeningtimesWineshop"},"h1_sparkling_wineproducer":{"key":"H1SparklingWineproducer"},"online_shopurl":{"key":"OnlineShopurl"},"quote_author":{"key":"QuoteAuthor"},"is_anteprima":1,"wines":["Wines","Wines"],"socials_youtube":"SocialsYoutube","openingtimes_gastronomie":{"key":"OpeningtimesGastronomie"},"socials_tiktok":"SocialsTiktok","has_visits":1,"is_skyalps_partner":1,"delivery_service_url":{"key":"DeliveryServiceUrl"},"socials_facebook":"SocialsFacebook","socials_twitter":"SocialsTwitter","image_sparkling_wineproducer":"ImageSparklingWineproducer","socials_instagram":"SocialsInstagram","is_winery":1,"h1":{"key":"H1"},"h2":{"key":"H2"},"h2_sparkling_wineproducer":{"key":"H2SparklingWineproducer"},"has_overnights":1,"has_accommodation":1,"is_vinum_hotel":1,"has_biowine":1,"socials_pinterest":"SocialsPinterest","quote":{"key":"Quote"},"has_direct_sales":1,"description_sparkling_wineproducer":{"key":"DescriptionSparklingWineproducer"},"openingtimes_guides":{"key":"OpeningtimesGuides"},"has_onlineshop":1,"company_holiday":{"key":"CompanyHoliday"}},"poi_lts_data_properties":{"has_free_entrance":1,"is_open":1},"gastronomy_lts_data_properties":{"capacity_ceremony":[{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"},{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"}],"dish_rates":[{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669},{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669}],"max_seating_capacity":5,"category_codes":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}],"facilities":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}]},"activity_lts_data_properties":{"bike_transport":1,"is_prepared":1,"lift_available":1,"lift_type":"LiftType","has_rentals":1,"exposition":["Exposition","Exposition"],"altitude_highest_point":1.2315135367772556,"ratings":{"experience":"Experience","landscape":"Landscape","difficulty":"Difficulty","technique":"Technique","stamina":"Stamina"},"feet_climb":1,"is_with_ligth":1,"number":"Number","distance_length":1.1730742509559433,"altitude_sum_up":1.4894159098541704,"altitude_sum_down":6.84685269835264,"altitude_lowest_point":1.0246457001441578,"lift_capacity_type":"LiftCapacityType","way_number":4,"altitude_difference":7.386281948385884,"mountain_bike_permitted":1,"distance_duration":7.457744773683766,"is_open":1,"run_to_valley":1}},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"has_language":["HasLanguage","HasLanguage"],"district_id":"DistrictId","gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"location_info":{"municipality_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"tv_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"region_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"district_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"area_info":{"self":"Self","id":"Id","name":{"key":"Name"}}},"room_details":[{"tag_ids":["TagIds","TagIds"],"placement":"Placement","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"venue_room_properties":{"door_width_in_centimeters":9,"square_meters":5,"room_height_in_centimeters":2,"room_depth_in_meters":7,"room_width_in_meters":5,"door_height_in_centimeters":3},"id":"Id","shortname":"Shortname","tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}},{"tag_ids":["TagIds","TagIds"],"placement":"Placement","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"venue_room_properties":{"door_width_in_centimeters":9,"square_meters":5,"room_height_in_centimeters":2,"room_depth_in_meters":7,"room_width_in_meters":5,"door_height_in_centimeters":3},"id":"Id","shortname":"Shortname","tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}}],"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id","shortname":"Shortname","distance_info":{"distance_to_municipality":5.025004791520295,"distance_to_district":9.965781217890562},"operation_schedule":[{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]},{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]}],"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/Venue",
    #    headers=headers,
    #    json=venue_v2,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_venue(client: TestClient):
    """Test case for single_venue

    GET Venue Single
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
    #    "/v1/Venue/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_venue_id_put(client: TestClient):
    """Test case for v1_venue_id_put

    PUT Modify existing Venue
    """
    venue_v2 = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"published_on":["PublishedOn","PublishedOn"],"tag_ids":["TagIds","TagIds"],"mapping":{"key":{"key":"Mapping"}},"self":"Self","source":"Source","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"contact_infos":{"key":{"name_prefix":"NamePrefix","email":"Email","address":"Address","region_code":"RegionCode","country_name":"CountryName","zip_code":"ZipCode","logo_url":"LogoUrl","vat":"Vat","faxnumber":"Faxnumber","tax":"Tax","city":"City","url":"Url","company_name":"CompanyName","area":"Area","language":"Language","givenname":"Givenname","region":"Region","country_code":"CountryCode","surname":"Surname","phonenumber":"Phonenumber"}},"_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"additional_properties":{"echarging_data_properties":{"payment_info":"PaymentInfo","car_parking_space_next_to_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"vertical_road_sign":1,"barrierfree":"Barrierefrei","access_type_info":"AccessTypeInfo","car_parking_space_behind_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"survey_annotations":{"key":"SurveyAnnotations"},"stepless_sidewalk_connection":1,"charging_cable_length":7,"horizontal_floor_road_sign":1,"charging_station_accessible":1,"covered":1,"survey_type":"SurveyType","capacity":5,"state":"UNAVAILABLE","survey_date":"2000-01-23T04:56:07.000+00:00","shielding_post_in_front_of_station":1,"charging_pistol_operation_height":2,"charging_pistol_types":["ChargingPistolTypes","ChargingPistolTypes"],"display_or_card_reader_operation_height":5,"access_type":"PUBLIC"},"poi_age_data_properties":{"age_from":8,"age_to":9},"road_incident_properties":"{}","suedtirol_wein_company_data_properties":{"has_deliveryservice":1,"socials_linked_in":"SocialsLinkedIn","is_wine_summit":1,"is_wine_stories":1,"is_sparkling_wineassociation":1,"openingtimes_wineshop":{"key":"OpeningtimesWineshop"},"h1_sparkling_wineproducer":{"key":"H1SparklingWineproducer"},"online_shopurl":{"key":"OnlineShopurl"},"quote_author":{"key":"QuoteAuthor"},"is_anteprima":1,"wines":["Wines","Wines"],"socials_youtube":"SocialsYoutube","openingtimes_gastronomie":{"key":"OpeningtimesGastronomie"},"socials_tiktok":"SocialsTiktok","has_visits":1,"is_skyalps_partner":1,"delivery_service_url":{"key":"DeliveryServiceUrl"},"socials_facebook":"SocialsFacebook","socials_twitter":"SocialsTwitter","image_sparkling_wineproducer":"ImageSparklingWineproducer","socials_instagram":"SocialsInstagram","is_winery":1,"h1":{"key":"H1"},"h2":{"key":"H2"},"h2_sparkling_wineproducer":{"key":"H2SparklingWineproducer"},"has_overnights":1,"has_accommodation":1,"is_vinum_hotel":1,"has_biowine":1,"socials_pinterest":"SocialsPinterest","quote":{"key":"Quote"},"has_direct_sales":1,"description_sparkling_wineproducer":{"key":"DescriptionSparklingWineproducer"},"openingtimes_guides":{"key":"OpeningtimesGuides"},"has_onlineshop":1,"company_holiday":{"key":"CompanyHoliday"}},"poi_lts_data_properties":{"has_free_entrance":1,"is_open":1},"gastronomy_lts_data_properties":{"capacity_ceremony":[{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"},{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"}],"dish_rates":[{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669},{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669}],"max_seating_capacity":5,"category_codes":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}],"facilities":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}]},"activity_lts_data_properties":{"bike_transport":1,"is_prepared":1,"lift_available":1,"lift_type":"LiftType","has_rentals":1,"exposition":["Exposition","Exposition"],"altitude_highest_point":1.2315135367772556,"ratings":{"experience":"Experience","landscape":"Landscape","difficulty":"Difficulty","technique":"Technique","stamina":"Stamina"},"feet_climb":1,"is_with_ligth":1,"number":"Number","distance_length":1.1730742509559433,"altitude_sum_up":1.4894159098541704,"altitude_sum_down":6.84685269835264,"altitude_lowest_point":1.0246457001441578,"lift_capacity_type":"LiftCapacityType","way_number":4,"altitude_difference":7.386281948385884,"mountain_bike_permitted":1,"distance_duration":7.457744773683766,"is_open":1,"run_to_valley":1}},"tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"has_language":["HasLanguage","HasLanguage"],"district_id":"DistrictId","gps_info":[{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704},{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}],"related_content":[{"type":"accommodation","id":"Id","self":"Self"},{"type":"accommodation","id":"Id","self":"Self"}],"location_info":{"municipality_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"tv_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"region_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"district_info":{"self":"Self","id":"Id","name":{"key":"Name"}},"area_info":{"self":"Self","id":"Id","name":{"key":"Name"}}},"room_details":[{"tag_ids":["TagIds","TagIds"],"placement":"Placement","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"venue_room_properties":{"door_width_in_centimeters":9,"square_meters":5,"room_height_in_centimeters":2,"room_depth_in_meters":7,"room_width_in_meters":5,"door_height_in_centimeters":3},"id":"Id","shortname":"Shortname","tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}},{"tag_ids":["TagIds","TagIds"],"placement":"Placement","image_gallery":[{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}},{"license":"License","image_url":"ImageUrl","image_title":{"key":"ImageTitle"},"image_tags":["ImageTags","ImageTags"],"list_position":8,"license_holder":"LicenseHolder","image_name":"ImageName","copy_right":"CopyRight","valid_to":"2000-01-23T04:56:07.000+00:00","valid_from":"2000-01-23T04:56:07.000+00:00","height":6,"image_source":"ImageSource","width":9,"image_alt_text":{"key":"ImageAltText"},"is_in_gallery":1,"image_desc":{"key":"ImageDesc"}}],"venue_room_properties":{"door_width_in_centimeters":9,"square_meters":5,"room_height_in_centimeters":2,"room_depth_in_meters":7,"room_width_in_meters":5,"door_height_in_centimeters":3},"id":"Id","shortname":"Shortname","tags":[{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"},{"type":"Type","tag_entry":{"key":"TagEntry"},"id":"Id","self":"Self","source":"Source","name":"Name"}],"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}}],"gps_points":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id","shortname":"Shortname","distance_info":{"distance_to_municipality":5.025004791520295,"distance_to_district":9.965781217890562},"operation_schedule":[{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]},{"type":"Type","start":"2000-01-23T04:56:07.000+00:00","stop":"2000-01-23T04:56:07.000+00:00","operationschedule_name":{"key":"OperationscheduleName"},"operation_schedule_time":[{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1},{"monday":1,"thursday":1,"start":"Start","friday":1,"timecode":9,"sunday":1,"state":7,"wednesday":1,"thuresday":1,"end":"End","tuesday":1,"saturday":1}]}],"detail":{"key":{"base_text":"BaseText","keywords":["Keywords","Keywords"],"meta_title":"MetaTitle","title":"Title","safety_info":"SafetyInfo","additional_text":"AdditionalText","public_transportation_info":"PublicTransportationInfo","meta_desc":"MetaDesc","get_there_text":"GetThereText","parking_info":"ParkingInfo","header":"Header","language":"Language","author_tip":"AuthorTip","sub_header":"SubHeader","equipment_info":"EquipmentInfo","intro_text":"IntroText"}}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/Venue/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=venue_v2,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_venue_id_delete(client: TestClient):
    """Test case for v1_venue_id_delete

    DELETE Venue by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/Venue/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_venue_types_get(client: TestClient):
    """Test case for v1_venue_types_get

    GET Venue Types List
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
    #    "/v1/VenueTypes",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_venue_types(client: TestClient):
    """Test case for single_venue_types

    GET Venue Types Single
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
    #    "/v1/VenueTypes/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

