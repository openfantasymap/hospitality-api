# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.batch_crud_result import BatchCRUDResult  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.urban_green import UrbanGreen  # noqa: F401
from openapi_server.models.urban_green_json_result import UrbanGreenJsonResult  # noqa: F401


def test_v1_urban_green_get(client: TestClient):
    """Test case for v1_urban_green_get

    GET UrbanGreen List
    """
    params = [("pagenumber", 1),     ("pagesize", 56),     ("language", 'language_example'),     ("langfilter", 'langfilter_example'),     ("idlist", 'idlist_example'),     ("source", 'source_example'),     ("greencode", 'greencode_example'),     ("greencodeversion", 'greencodeversion_example'),     ("greencodetype", 'greencodetype_example'),     ("greencodesubtype", 'greencodesubtype_example'),     ("activefilter", True),     ("tagfilter", 'tagfilter_example'),     ("seed", 'seed_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/UrbanGreen",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_urban_green_put(client: TestClient):
    """Test case for v1_urban_green_put

    PUT Upsert array of UrbanGreens with well known ids
    """
    urban_green = [{"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"has_language":["HasLanguage","HasLanguage"],"tag_ids":["TagIds","TagIds"],"green_code_type":"GreenCodeType","mapping":{"key":{"key":"Mapping"}},"green_code_version":"GreenCodeVersion","green_code":"GreenCode","source":"Source","geo":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"removed_from_site":"2000-01-23T04:56:07.000+00:00","put_on_site":"2000-01-23T04:56:07.000+00:00","green_code_subtype":"GreenCodeSubtype","first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id","_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"shortname":"Shortname","additional_properties":{"echarging_data_properties":{"payment_info":"PaymentInfo","car_parking_space_next_to_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"vertical_road_sign":1,"barrierfree":"Barrierefrei","access_type_info":"AccessTypeInfo","car_parking_space_behind_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"survey_annotations":{"key":"SurveyAnnotations"},"stepless_sidewalk_connection":1,"charging_cable_length":7,"horizontal_floor_road_sign":1,"charging_station_accessible":1,"covered":1,"survey_type":"SurveyType","capacity":5,"state":"UNAVAILABLE","survey_date":"2000-01-23T04:56:07.000+00:00","shielding_post_in_front_of_station":1,"charging_pistol_operation_height":2,"charging_pistol_types":["ChargingPistolTypes","ChargingPistolTypes"],"display_or_card_reader_operation_height":5,"access_type":"PUBLIC"},"poi_age_data_properties":{"age_from":8,"age_to":9},"road_incident_properties":"{}","suedtirol_wein_company_data_properties":{"has_deliveryservice":1,"socials_linked_in":"SocialsLinkedIn","is_wine_summit":1,"is_wine_stories":1,"is_sparkling_wineassociation":1,"openingtimes_wineshop":{"key":"OpeningtimesWineshop"},"h1_sparkling_wineproducer":{"key":"H1SparklingWineproducer"},"online_shopurl":{"key":"OnlineShopurl"},"quote_author":{"key":"QuoteAuthor"},"is_anteprima":1,"wines":["Wines","Wines"],"socials_youtube":"SocialsYoutube","openingtimes_gastronomie":{"key":"OpeningtimesGastronomie"},"socials_tiktok":"SocialsTiktok","has_visits":1,"is_skyalps_partner":1,"delivery_service_url":{"key":"DeliveryServiceUrl"},"socials_facebook":"SocialsFacebook","socials_twitter":"SocialsTwitter","image_sparkling_wineproducer":"ImageSparklingWineproducer","socials_instagram":"SocialsInstagram","is_winery":1,"h1":{"key":"H1"},"h2":{"key":"H2"},"h2_sparkling_wineproducer":{"key":"H2SparklingWineproducer"},"has_overnights":1,"has_accommodation":1,"is_vinum_hotel":1,"has_biowine":1,"socials_pinterest":"SocialsPinterest","quote":{"key":"Quote"},"has_direct_sales":1,"description_sparkling_wineproducer":{"key":"DescriptionSparklingWineproducer"},"openingtimes_guides":{"key":"OpeningtimesGuides"},"has_onlineshop":1,"company_holiday":{"key":"CompanyHoliday"}},"poi_lts_data_properties":{"has_free_entrance":1,"is_open":1},"gastronomy_lts_data_properties":{"capacity_ceremony":[{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"},{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"}],"dish_rates":[{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669},{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669}],"max_seating_capacity":5,"category_codes":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}],"facilities":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}]},"activity_lts_data_properties":{"bike_transport":1,"is_prepared":1,"lift_available":1,"lift_type":"LiftType","has_rentals":1,"exposition":["Exposition","Exposition"],"altitude_highest_point":1.2315135367772556,"ratings":{"experience":"Experience","landscape":"Landscape","difficulty":"Difficulty","technique":"Technique","stamina":"Stamina"},"feet_climb":1,"is_with_ligth":1,"number":"Number","distance_length":1.1730742509559433,"altitude_sum_up":1.4894159098541704,"altitude_sum_down":6.84685269835264,"altitude_lowest_point":1.0246457001441578,"lift_capacity_type":"LiftCapacityType","way_number":4,"altitude_difference":7.386281948385884,"mountain_bike_permitted":1,"distance_duration":7.457744773683766,"is_open":1,"run_to_valley":1}},"detail":{"key":{"base_text":"BaseText","language":"Language","title":"Title"}}}]

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/UrbanGreen",
    #    headers=headers,
    #    json=urban_green,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_urban_green_post(client: TestClient):
    """Test case for v1_urban_green_post

    POST Insert new UrbanGreen
    """
    urban_green = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"has_language":["HasLanguage","HasLanguage"],"tag_ids":["TagIds","TagIds"],"green_code_type":"GreenCodeType","mapping":{"key":{"key":"Mapping"}},"green_code_version":"GreenCodeVersion","green_code":"GreenCode","source":"Source","geo":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"removed_from_site":"2000-01-23T04:56:07.000+00:00","put_on_site":"2000-01-23T04:56:07.000+00:00","green_code_subtype":"GreenCodeSubtype","first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id","_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"shortname":"Shortname","additional_properties":{"echarging_data_properties":{"payment_info":"PaymentInfo","car_parking_space_next_to_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"vertical_road_sign":1,"barrierfree":"Barrierefrei","access_type_info":"AccessTypeInfo","car_parking_space_behind_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"survey_annotations":{"key":"SurveyAnnotations"},"stepless_sidewalk_connection":1,"charging_cable_length":7,"horizontal_floor_road_sign":1,"charging_station_accessible":1,"covered":1,"survey_type":"SurveyType","capacity":5,"state":"UNAVAILABLE","survey_date":"2000-01-23T04:56:07.000+00:00","shielding_post_in_front_of_station":1,"charging_pistol_operation_height":2,"charging_pistol_types":["ChargingPistolTypes","ChargingPistolTypes"],"display_or_card_reader_operation_height":5,"access_type":"PUBLIC"},"poi_age_data_properties":{"age_from":8,"age_to":9},"road_incident_properties":"{}","suedtirol_wein_company_data_properties":{"has_deliveryservice":1,"socials_linked_in":"SocialsLinkedIn","is_wine_summit":1,"is_wine_stories":1,"is_sparkling_wineassociation":1,"openingtimes_wineshop":{"key":"OpeningtimesWineshop"},"h1_sparkling_wineproducer":{"key":"H1SparklingWineproducer"},"online_shopurl":{"key":"OnlineShopurl"},"quote_author":{"key":"QuoteAuthor"},"is_anteprima":1,"wines":["Wines","Wines"],"socials_youtube":"SocialsYoutube","openingtimes_gastronomie":{"key":"OpeningtimesGastronomie"},"socials_tiktok":"SocialsTiktok","has_visits":1,"is_skyalps_partner":1,"delivery_service_url":{"key":"DeliveryServiceUrl"},"socials_facebook":"SocialsFacebook","socials_twitter":"SocialsTwitter","image_sparkling_wineproducer":"ImageSparklingWineproducer","socials_instagram":"SocialsInstagram","is_winery":1,"h1":{"key":"H1"},"h2":{"key":"H2"},"h2_sparkling_wineproducer":{"key":"H2SparklingWineproducer"},"has_overnights":1,"has_accommodation":1,"is_vinum_hotel":1,"has_biowine":1,"socials_pinterest":"SocialsPinterest","quote":{"key":"Quote"},"has_direct_sales":1,"description_sparkling_wineproducer":{"key":"DescriptionSparklingWineproducer"},"openingtimes_guides":{"key":"OpeningtimesGuides"},"has_onlineshop":1,"company_holiday":{"key":"CompanyHoliday"}},"poi_lts_data_properties":{"has_free_entrance":1,"is_open":1},"gastronomy_lts_data_properties":{"capacity_ceremony":[{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"},{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"}],"dish_rates":[{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669},{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669}],"max_seating_capacity":5,"category_codes":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}],"facilities":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}]},"activity_lts_data_properties":{"bike_transport":1,"is_prepared":1,"lift_available":1,"lift_type":"LiftType","has_rentals":1,"exposition":["Exposition","Exposition"],"altitude_highest_point":1.2315135367772556,"ratings":{"experience":"Experience","landscape":"Landscape","difficulty":"Difficulty","technique":"Technique","stamina":"Stamina"},"feet_climb":1,"is_with_ligth":1,"number":"Number","distance_length":1.1730742509559433,"altitude_sum_up":1.4894159098541704,"altitude_sum_down":6.84685269835264,"altitude_lowest_point":1.0246457001441578,"lift_capacity_type":"LiftCapacityType","way_number":4,"altitude_difference":7.386281948385884,"mountain_bike_permitted":1,"distance_duration":7.457744773683766,"is_open":1,"run_to_valley":1}},"detail":{"key":{"base_text":"BaseText","language":"Language","title":"Title"}}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/UrbanGreen",
    #    headers=headers,
    #    json=urban_green,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_urban_green(client: TestClient):
    """Test case for single_urban_green

    GET UrbanGreen Single
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
    #    "/v1/UrbanGreen/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_urban_green_id_put(client: TestClient):
    """Test case for v1_urban_green_id_put

    PUT Modify existing UrbanGreen
    """
    urban_green = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"has_language":["HasLanguage","HasLanguage"],"tag_ids":["TagIds","TagIds"],"green_code_type":"GreenCodeType","mapping":{"key":{"key":"Mapping"}},"green_code_version":"GreenCodeVersion","green_code":"GreenCode","source":"Source","geo":{"key":{"gpstype":"position","geometry":"Geometry","altitude_unitof_measure":"AltitudeUnitofMeasure","latitude":1.2315135367772556,"longitude":1.0246457001441578,"default":1,"altitude":1.4894159098541704}},"active":1,"removed_from_site":"2000-01-23T04:56:07.000+00:00","put_on_site":"2000-01-23T04:56:07.000+00:00","green_code_subtype":"GreenCodeSubtype","first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","id":"Id","_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"shortname":"Shortname","additional_properties":{"echarging_data_properties":{"payment_info":"PaymentInfo","car_parking_space_next_to_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"vertical_road_sign":1,"barrierfree":"Barrierefrei","access_type_info":"AccessTypeInfo","car_parking_space_behind_each_other":{"gradient":9.301444243932576,"length":4,"barrier_free_access_spaceto_charging_point":1,"pavement":"Barrierefrei","lateral_inclination":3.616076749251911,"flat":1,"maneuvring_space_signage_present":1,"width":2},"survey_annotations":{"key":"SurveyAnnotations"},"stepless_sidewalk_connection":1,"charging_cable_length":7,"horizontal_floor_road_sign":1,"charging_station_accessible":1,"covered":1,"survey_type":"SurveyType","capacity":5,"state":"UNAVAILABLE","survey_date":"2000-01-23T04:56:07.000+00:00","shielding_post_in_front_of_station":1,"charging_pistol_operation_height":2,"charging_pistol_types":["ChargingPistolTypes","ChargingPistolTypes"],"display_or_card_reader_operation_height":5,"access_type":"PUBLIC"},"poi_age_data_properties":{"age_from":8,"age_to":9},"road_incident_properties":"{}","suedtirol_wein_company_data_properties":{"has_deliveryservice":1,"socials_linked_in":"SocialsLinkedIn","is_wine_summit":1,"is_wine_stories":1,"is_sparkling_wineassociation":1,"openingtimes_wineshop":{"key":"OpeningtimesWineshop"},"h1_sparkling_wineproducer":{"key":"H1SparklingWineproducer"},"online_shopurl":{"key":"OnlineShopurl"},"quote_author":{"key":"QuoteAuthor"},"is_anteprima":1,"wines":["Wines","Wines"],"socials_youtube":"SocialsYoutube","openingtimes_gastronomie":{"key":"OpeningtimesGastronomie"},"socials_tiktok":"SocialsTiktok","has_visits":1,"is_skyalps_partner":1,"delivery_service_url":{"key":"DeliveryServiceUrl"},"socials_facebook":"SocialsFacebook","socials_twitter":"SocialsTwitter","image_sparkling_wineproducer":"ImageSparklingWineproducer","socials_instagram":"SocialsInstagram","is_winery":1,"h1":{"key":"H1"},"h2":{"key":"H2"},"h2_sparkling_wineproducer":{"key":"H2SparklingWineproducer"},"has_overnights":1,"has_accommodation":1,"is_vinum_hotel":1,"has_biowine":1,"socials_pinterest":"SocialsPinterest","quote":{"key":"Quote"},"has_direct_sales":1,"description_sparkling_wineproducer":{"key":"DescriptionSparklingWineproducer"},"openingtimes_guides":{"key":"OpeningtimesGuides"},"has_onlineshop":1,"company_holiday":{"key":"CompanyHoliday"}},"poi_lts_data_properties":{"has_free_entrance":1,"is_open":1},"gastronomy_lts_data_properties":{"capacity_ceremony":[{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"},{"max_seating_capacity":6,"id":"Id","shortname":"Shortname"}],"dish_rates":[{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669},{"currency_code":"CurrencyCode","min_amount":9.965781217890562,"id":"Id","shortname":"Shortname","max_amount":9.369310271410669}],"max_seating_capacity":5,"category_codes":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}],"facilities":[{"id":"Id","shortname":"Shortname"},{"id":"Id","shortname":"Shortname"}]},"activity_lts_data_properties":{"bike_transport":1,"is_prepared":1,"lift_available":1,"lift_type":"LiftType","has_rentals":1,"exposition":["Exposition","Exposition"],"altitude_highest_point":1.2315135367772556,"ratings":{"experience":"Experience","landscape":"Landscape","difficulty":"Difficulty","technique":"Technique","stamina":"Stamina"},"feet_climb":1,"is_with_ligth":1,"number":"Number","distance_length":1.1730742509559433,"altitude_sum_up":1.4894159098541704,"altitude_sum_down":6.84685269835264,"altitude_lowest_point":1.0246457001441578,"lift_capacity_type":"LiftCapacityType","way_number":4,"altitude_difference":7.386281948385884,"mountain_bike_permitted":1,"distance_duration":7.457744773683766,"is_open":1,"run_to_valley":1}},"detail":{"key":{"base_text":"BaseText","language":"Language","title":"Title"}}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/UrbanGreen/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=urban_green,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_urban_green_id_delete(client: TestClient):
    """Test case for v1_urban_green_id_delete

    DELETE UrbanGreen by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/UrbanGreen/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

