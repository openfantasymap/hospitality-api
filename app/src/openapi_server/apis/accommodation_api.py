# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.accommodation_api_base import BaseAccommodationApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.acco_features import AccoFeatures
from openapi_server.models.acco_types import AccoTypes
from openapi_server.models.accommodation_room_linked import AccommodationRoomLinked
from openapi_server.models.accommodation_v2 import AccommodationV2
from openapi_server.models.accommodation_v2_json_result import AccommodationV2JsonResult
from openapi_server.models.accommodation_v2_json_result_with_booking_info import AccommodationV2JsonResultWithBookingInfo
from openapi_server.models.mss_result_json_result_with_booking_info import MssResultJsonResultWithBookingInfo
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/Accommodation",
    responses={
        200: {"model": AccommodationV2JsonResult, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        401: {"model": ProblemDetails, "description": "Unauthorized"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="GET Accommodation List",
    response_model_by_alias=True,
)
async def accommodation_list(
    pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")] = Query(1, description="Pagenumber", alias="pagenumber"),
    pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page (If availabilitycheck set, pagesize has no effect all Accommodations are returned), (default:10)")] = Query(None, description="Elements per Page (If availabilitycheck set, pagesize has no effect all Accommodations are returned), (default:10)", alias="pagesize"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, &#39;null&#39; disables Random Sorting, (default:null)", alias="seed"),
    categoryfilter: Annotated[Optional[StrictStr], Field(description="Categoryfilter BITMASK values: 1 = (not categorized), 2 = (1star), 4 = (1flower), 8 = (1sun), 14 = (1star/1flower/1sun), 16 = (2stars), 32 = (2flowers), 64 = (2suns), 112 = (2stars/2flowers/2suns), 128 = (3stars), 256 = (3flowers), 512 = (3suns), 1024 = (3sstars), 1920 = (3stars/3flowers/3suns/3sstars), 2048 = (4stars), 4096 = (4flowers), 8192 = (4suns), 16384 = (4sstars), 30720 = (4stars/4flowers/4suns/4sstars), 32768 = (5stars), 65536 = (5flowers), 131072 = (5suns), 229376 = (5stars/5flowers/5suns), 'null' = (No Filter), (default:'null')")] = Query(None, description="Categoryfilter BITMASK values: 1 &#x3D; (not categorized), 2 &#x3D; (1star), 4 &#x3D; (1flower), 8 &#x3D; (1sun), 14 &#x3D; (1star/1flower/1sun), 16 &#x3D; (2stars), 32 &#x3D; (2flowers), 64 &#x3D; (2suns), 112 &#x3D; (2stars/2flowers/2suns), 128 &#x3D; (3stars), 256 &#x3D; (3flowers), 512 &#x3D; (3suns), 1024 &#x3D; (3sstars), 1920 &#x3D; (3stars/3flowers/3suns/3sstars), 2048 &#x3D; (4stars), 4096 &#x3D; (4flowers), 8192 &#x3D; (4suns), 16384 &#x3D; (4sstars), 30720 &#x3D; (4stars/4flowers/4suns/4sstars), 32768 &#x3D; (5stars), 65536 &#x3D; (5flowers), 131072 &#x3D; (5suns), 229376 &#x3D; (5stars/5flowers/5suns), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="categoryfilter"),
    typefilter: Annotated[Optional[StrictStr], Field(description="Typefilter BITMASK values: 1 = (HotelPension), 2 = (BedBreakfast), 4 = (Farm), 8 = (Camping), 16 = (Youth), 32 = (Mountain), 64 = (Apartment), 128 = (Not defined),'null' = (No Filter), (default:'null')")] = Query(None, description="Typefilter BITMASK values: 1 &#x3D; (HotelPension), 2 &#x3D; (BedBreakfast), 4 &#x3D; (Farm), 8 &#x3D; (Camping), 16 &#x3D; (Youth), 32 &#x3D; (Mountain), 64 &#x3D; (Apartment), 128 &#x3D; (Not defined),&#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="typefilter"),
    boardfilter: Annotated[Optional[StrictStr], Field(description="Boardfilter BITMASK values: 0 = (all boards), 1 = (without board), 2 = (breakfast), 4 = (half board), 8 = (full board), 16 = (All inclusive), 'null' = (No Filter), (default:'null')")] = Query(None, description="Boardfilter BITMASK values: 0 &#x3D; (all boards), 1 &#x3D; (without board), 2 &#x3D; (breakfast), 4 &#x3D; (half board), 8 &#x3D; (full board), 16 &#x3D; (All inclusive), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="boardfilter"),
    featurefilter: Annotated[Optional[StrictStr], Field(description="FeatureFilter BITMASK values: 1 = (Group-friendly), 2 = (Meeting rooms), 4 = (Swimming pool), 8 = (Sauna), 16 = (Garage), 32 = (Pick-up service), 64 = (WLAN), 128 = (Barrier-free), 256 = (Special menus for allergy sufferers), 512 = (Pets welcome), 'null' = (No Filter), (default:'null')")] = Query(None, description="FeatureFilter BITMASK values: 1 &#x3D; (Group-friendly), 2 &#x3D; (Meeting rooms), 4 &#x3D; (Swimming pool), 8 &#x3D; (Sauna), 16 &#x3D; (Garage), 32 &#x3D; (Pick-up service), 64 &#x3D; (WLAN), 128 &#x3D; (Barrier-free), 256 &#x3D; (Special menus for allergy sufferers), 512 &#x3D; (Pets welcome), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="featurefilter"),
    featureidfilter: Annotated[Optional[StrictStr], Field(description="Feature Id Filter, LIST filter over ALL Features available. Separator ',' List of Feature IDs, 'null' = (No Filter), (default:'null')")] = Query(None, description="Feature Id Filter, LIST filter over ALL Features available. Separator &#39;,&#39; List of Feature IDs, &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="featureidfilter"),
    themefilter: Annotated[Optional[StrictStr], Field(description="Themefilter BITMASK values: 1 = (Gourmet), 2 = (At altitude), 4 = (Regional wellness offerings), 8 = (on the wheels), 16 = (With family), 32 = (Hiking), 64 = (In the vineyards), 128 = (Urban vibe), 256 = (At the ski resort), 512 = (Mediterranean), 1024 = (In the Dolomites), 2048 = (Alpine), 4096 = (Small and charming), 8192 = (Huts and mountain inns), 16384 = (Rural way of life), 32768 = (Balance), 65536 = (Christmas markets), 131072 = (Sustainability), 'null' = (No Filter), (default:'null')")] = Query(None, description="Themefilter BITMASK values: 1 &#x3D; (Gourmet), 2 &#x3D; (At altitude), 4 &#x3D; (Regional wellness offerings), 8 &#x3D; (on the wheels), 16 &#x3D; (With family), 32 &#x3D; (Hiking), 64 &#x3D; (In the vineyards), 128 &#x3D; (Urban vibe), 256 &#x3D; (At the ski resort), 512 &#x3D; (Mediterranean), 1024 &#x3D; (In the Dolomites), 2048 &#x3D; (Alpine), 4096 &#x3D; (Small and charming), 8192 &#x3D; (Huts and mountain inns), 16384 &#x3D; (Rural way of life), 32768 &#x3D; (Balance), 65536 &#x3D; (Christmas markets), 131072 &#x3D; (Sustainability), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="themefilter"),
    badgefilter: Annotated[Optional[StrictStr], Field(description="BadgeFilter BITMASK values: 1 = (Belvita Wellness Hotel), 2 = (Familyhotel), 4 = (Bikehotel), 8 = (Red Rooster Farm), 16 = (Barrier free certificated), 32 = (Vitalpina Hiking Hotel), 64 = (Private Rooms in South Tyrol), 128 = (Vinum Hotels), 'null' = (No Filter), (default:'null')")] = Query(None, description="BadgeFilter BITMASK values: 1 &#x3D; (Belvita Wellness Hotel), 2 &#x3D; (Familyhotel), 4 &#x3D; (Bikehotel), 8 &#x3D; (Red Rooster Farm), 16 &#x3D; (Barrier free certificated), 32 &#x3D; (Vitalpina Hiking Hotel), 64 &#x3D; (Private Rooms in South Tyrol), 128 &#x3D; (Vinum Hotels), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="badgefilter"),
    idfilter: Annotated[Optional[StrictStr], Field(description="IDFilter LIST Separator ',' List of Accommodation IDs, 'null' = (No Filter), (default:'null')")] = Query(None, description="IDFilter LIST Separator &#39;,&#39; List of Accommodation IDs, &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="idfilter"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")] = Query(None, description="Locfilter SPECIAL Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki locfilter&lt;/a&gt;", alias="locfilter"),
    altitudefilter: Annotated[Optional[StrictStr], Field(description="Altitude Range Filter SPECIAL (Separator ',' example Value: 500,1000 Altitude from 500 up to 1000 metres), (default:'null')")] = Query(None, description="Altitude Range Filter SPECIAL (Separator &#39;,&#39; example Value: 500,1000 Altitude from 500 up to 1000 metres), (default:&#39;null&#39;)", alias="altitudefilter"),
    odhtagfilter: Annotated[Optional[StrictStr], Field(description="ODHTag Filter LIST (refers to Array SmgTags) (String, Separator ',' more ODHTags possible, 'null' = No Filter, available ODHTags reference to 'v1/ODHTag?validforentity=accommodation'), (default:'null')")] = Query(None, description="ODHTag Filter LIST (refers to Array SmgTags) (String, Separator &#39;,&#39; more ODHTags possible, &#39;null&#39; &#x3D; No Filter, available ODHTags reference to &#39;v1/ODHTag?validforentity&#x3D;accommodation&#39;), (default:&#39;null&#39;)", alias="odhtagfilter"),
    source: Optional[StrictStr] = Query(None, description="", alias="source"),
    odhactive: Annotated[Optional[StrictBool], Field(description="ODHActive Filter BOOLEAN (refers to field SmgActive) (possible Values: 'null' Displays all Accommodations, 'true' only ODH Active Accommodations, 'false' only ODH Disabled Accommodations), (default:'null')")] = Query(None, description="ODHActive Filter BOOLEAN (refers to field SmgActive) (possible Values: &#39;null&#39; Displays all Accommodations, &#39;true&#39; only ODH Active Accommodations, &#39;false&#39; only ODH Disabled Accommodations), (default:&#39;null&#39;)", alias="odhactive"),
    active: Annotated[Optional[StrictBool], Field(description="TIC Active Filter BOOLEAN (possible Values: 'null' Displays all Accommodations, 'true' only TIC Active Accommodations, 'false' only TIC Disabled Accommodations), (default:'null')")] = Query(None, description="TIC Active Filter BOOLEAN (possible Values: &#39;null&#39; Displays all Accommodations, &#39;true&#39; only TIC Active Accommodations, &#39;false&#39; only TIC Disabled Accommodations), (default:&#39;null&#39;)", alias="active"),
    bookablefilter: Optional[StrictBool] = Query(None, description="", alias="bookablefilter"),
    arrival: Annotated[Optional[StrictStr], Field(description="Arrival DATE (yyyy-MM-dd) REQUIRED ON Availabilitycheck = true, (default:'Today's date')")] = Query(None, description="Arrival DATE (yyyy-MM-dd) REQUIRED ON Availabilitycheck &#x3D; true, (default:&#39;Today&#39;s date&#39;)", alias="arrival"),
    departure: Annotated[Optional[StrictStr], Field(description="Departure DATE (yyyy-MM-dd) REQUIRED ON Availabilitycheck = true, (default:'Tomorrow's date')")] = Query(None, description="Departure DATE (yyyy-MM-dd) REQUIRED ON Availabilitycheck &#x3D; true, (default:&#39;Tomorrow&#39;s date&#39;)", alias="departure"),
    roominfo: Annotated[Optional[StrictStr], Field(description="Roominfo Filter REQUIRED ON Availabilitycheck = true (Splitter for Rooms '|' Splitter for Persons Ages ',') (Room Types: 0=notprovided, 1=room, 2=apartment, 4=pitch/tent(onlyLTS), 8=dorm(onlyLTS)) possible Values Example 1-18,10|1-18 = 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:'1-18,18')")] = Query('1-18,18', description="Roominfo Filter REQUIRED ON Availabilitycheck &#x3D; true (Splitter for Rooms &#39;|&#39; Splitter for Persons Ages &#39;,&#39;) (Room Types: 0&#x3D;notprovided, 1&#x3D;room, 2&#x3D;apartment, 4&#x3D;pitch/tent(onlyLTS), 8&#x3D;dorm(onlyLTS)) possible Values Example 1-18,10|1-18 &#x3D; 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:&#39;1-18,18&#39;)", alias="roominfo"),
    bokfilter: Annotated[Optional[StrictStr], Field(description="Booking Channels Filter REQUIRED ON Availabilitycheck = true (Separator ',' possible values: hgv = (Booking Südtirol), htl = (Hotel.de), exp = (Expedia), bok = (Booking.com), lts = (LTS Availability check)), (default:'hgv')")] = Query('hgv', description="Booking Channels Filter REQUIRED ON Availabilitycheck &#x3D; true (Separator &#39;,&#39; possible values: hgv &#x3D; (Booking Südtirol), htl &#x3D; (Hotel.de), exp &#x3D; (Expedia), bok &#x3D; (Booking.com), lts &#x3D; (LTS Availability check)), (default:&#39;hgv&#39;)", alias="bokfilter"),
    msssource: Annotated[Optional[StrictStr], Field(description="Source for MSS availability check, (default:'sinfo')")] = Query('sinfo', description="Source for MSS availability check, (default:&#39;sinfo&#39;)", alias="msssource"),
    availabilitychecklanguage: Annotated[Optional[StrictStr], Field(description="Language of the Availability Response (possible values: 'de','it','en')")] = Query('en', description="Language of the Availability Response (possible values: &#39;de&#39;,&#39;it&#39;,&#39;en&#39;)", alias="availabilitychecklanguage"),
    detail: Annotated[Optional[StrictStr], Field(description="Detail of the Availablity check (string, 1 = full Details, 0 = basic Details (default))")] = Query('0', description="Detail of the Availablity check (string, 1 &#x3D; full Details, 0 &#x3D; basic Details (default))", alias="detail"),
    tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")] = Query(None, description="Filter on Tags. (Endpoint on v1/Tag) Syntax &#x3D;and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: &#39;null&#39;)", alias="tagfilter"),
    availabilitycheck: Annotated[Optional[StrictBool], Field(description="Availability Check BOOLEAN (possible Values: 'true', 'false), (default Value: 'false') NOT AVAILABLE AS OPEN DATA, IF Availabilty Check is true certain filters are Required")] = Query(None, description="Availability Check BOOLEAN (possible Values: &#39;true&#39;, &#39;false), (default Value: &#39;false&#39;) NOT AVAILABLE AS OPEN DATA, IF Availabilty Check is true certain filters are Required", alias="availabilitycheck"),
    latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Latitude Format: &#39;46.624975&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="latitude"),
    longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Longitude Format: &#39;11.369909&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="longitude"),
    radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="radius"),
    polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: &#39;Bounding Box Contains&#39;, &#39;bbi&#39;: &#39;Bounding Box Intersects&#39;, followed by a List of Comma Separated Longitude Latitude Tuples, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="polygon"),
    publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")] = Query(None, description="Published On Filter (Separator &#39;,&#39; List of publisher IDs), (default:&#39;null&#39;)", alias="publishedon"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language, possible values: &#39;de|it|en|nl|cs|pl|fr|ru&#39; only one language supported (default:&#39;null&#39; all languages are displayed)", alias="language"),
    langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")] = Query(None, description="Language filter (returns only data available in the selected Language, Separator &#39;,&#39; possible values: &#39;de,it,en,nl,sc,pl,fr,ru&#39;, &#39;null&#39;: Filter disabled)", alias="langfilter"),
    updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")] = Query(None, description="Returns data changed after this date Format (yyyy-MM-dd), (default: &#39;null&#39;)", alias="updatefrom"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Get result only as Array of Ids, (default:false)  Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="getasidarray"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> AccommodationV2JsonResult:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().accommodation_list(pagenumber, pagesize, seed, categoryfilter, typefilter, boardfilter, featurefilter, featureidfilter, themefilter, badgefilter, idfilter, locfilter, altitudefilter, odhtagfilter, source, odhactive, active, bookablefilter, arrival, departure, roominfo, bokfilter, msssource, availabilitychecklanguage, detail, tagfilter, availabilitycheck, latitude, longitude, radius, polygon, publishedon, language, langfilter, updatefrom, fields, searchfilter, rawfilter, rawsort, removenullvalues, getasidarray)


@router.post(
    "/v1/Accommodation",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="POST Insert new Accommodation",
    response_model_by_alias=True,
)
async def v1_accommodation_post(
    accommodation_v2: Annotated[Optional[AccommodationV2], Field(description="Accommodation Object")] = Body(None, description="Accommodation Object"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> PGCRUDResult:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().v1_accommodation_post(accommodation_v2)


@router.get(
    "/v1/Accommodation/{id}",
    responses={
        200: {"model": AccommodationV2, "description": "Object created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        401: {"model": ProblemDetails, "description": "Unauthorized"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="GET Accommodation Single",
    response_model_by_alias=True,
)
async def single_accommodation(
    id: Annotated[StrictStr, Field(description="ID of the Accommodation")] = Path(..., description="ID of the Accommodation"),
    idsource: Annotated[Optional[StrictStr], Field(description="ID Source Filter (possible values:'lts','hgv','a0r_id'), (default:'lts')")] = Query('lts', description="ID Source Filter (possible values:&#39;lts&#39;,&#39;hgv&#39;,&#39;a0r_id&#39;), (default:&#39;lts&#39;)", alias="idsource"),
    availabilitychecklanguage: Annotated[Optional[StrictStr], Field(description="Language of the Availability Response (possible values: 'de','it','en')")] = Query('en', description="Language of the Availability Response (possible values: &#39;de&#39;,&#39;it&#39;,&#39;en&#39;)", alias="availabilitychecklanguage"),
    boardfilter: Annotated[Optional[StrictStr], Field(description="Boardfilter BITMASK values: 0 = (all boards), 1 = (without board), 2 = (breakfast), 4 = (half board), 8 = (full board), 16 = (All inclusive), 'null' = (No Filter), (default:'null')")] = Query(None, description="Boardfilter BITMASK values: 0 &#x3D; (all boards), 1 &#x3D; (without board), 2 &#x3D; (breakfast), 4 &#x3D; (half board), 8 &#x3D; (full board), 16 &#x3D; (All inclusive), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="boardfilter"),
    arrival: Annotated[Optional[StrictStr], Field(description="Arrival Date (yyyy-MM-dd) REQUIRED, (default:'Today')")] = Query(None, description="Arrival Date (yyyy-MM-dd) REQUIRED, (default:&#39;Today&#39;)", alias="arrival"),
    departure: Annotated[Optional[StrictStr], Field(description="Departure Date (yyyy-MM-dd) REQUIRED, (default:'Tomorrow')")] = Query(None, description="Departure Date (yyyy-MM-dd) REQUIRED, (default:&#39;Tomorrow&#39;)", alias="departure"),
    roominfo: Annotated[Optional[StrictStr], Field(description="Roominfo Filter REQUIRED (Splitter for Rooms '|' Splitter for Persons Ages ',') (Room Types: 0=notprovided, 1=room, 2=apartment, 4=pitch/tent(onlyLTS), 8=dorm(onlyLTS)) possible Values Example 1-18,10|1-18 = 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:'1-18,18')")] = Query('1-18,18', description="Roominfo Filter REQUIRED (Splitter for Rooms &#39;|&#39; Splitter for Persons Ages &#39;,&#39;) (Room Types: 0&#x3D;notprovided, 1&#x3D;room, 2&#x3D;apartment, 4&#x3D;pitch/tent(onlyLTS), 8&#x3D;dorm(onlyLTS)) possible Values Example 1-18,10|1-18 &#x3D; 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:&#39;1-18,18&#39;)", alias="roominfo"),
    bokfilter: Annotated[Optional[StrictStr], Field(description="Booking Channels Filter REQUIRED (Separator ',' possible values: hgv = (Booking Südtirol), htl = (Hotel.de), exp = (Expedia), bok = (Booking.com), lts = (LTS Availability check)), (default:'hgv')")] = Query('hgv', description="Booking Channels Filter REQUIRED (Separator &#39;,&#39; possible values: hgv &#x3D; (Booking Südtirol), htl &#x3D; (Hotel.de), exp &#x3D; (Expedia), bok &#x3D; (Booking.com), lts &#x3D; (LTS Availability check)), (default:&#39;hgv&#39;)", alias="bokfilter"),
    msssource: Optional[StrictStr] = Query('sinfo', description="", alias="msssource"),
    availabilitycheck: Annotated[Optional[StrictBool], Field(description="Availability Check enabled/disabled (possible Values: 'true', 'false), (default Value: 'false') NOT AVAILABLE AS OPEN DATA")] = Query(None, description="Availability Check enabled/disabled (possible Values: &#39;true&#39;, &#39;false), (default Value: &#39;false&#39;) NOT AVAILABLE AS OPEN DATA", alias="availabilitycheck"),
    detail: Annotated[Optional[StrictStr], Field(description="Detail of the Availablity check (string, 1 = full Details, 0 = basic Details (default))")] = Query('0', description="Detail of the Availablity check (string, 1 &#x3D; full Details, 0 &#x3D; basic Details (default))", alias="detail"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> AccommodationV2:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().single_accommodation(id, idsource, availabilitychecklanguage, boardfilter, arrival, departure, roominfo, bokfilter, msssource, availabilitycheck, detail, fields, language, removenullvalues)


@router.put(
    "/v1/Accommodation/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="PUT Modify existing Accommodation",
    response_model_by_alias=True,
)
async def v1_accommodation_id_put(
    id: Annotated[StrictStr, Field(description="Accommodation Id")] = Path(..., description="Accommodation Id"),
    accommodation_v2: Annotated[Optional[AccommodationV2], Field(description="Accommodation Object")] = Body(None, description="Accommodation Object"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> PGCRUDResult:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().v1_accommodation_id_put(id, accommodation_v2)


@router.delete(
    "/v1/Accommodation/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="DELETE Accommodation by Id",
    response_model_by_alias=True,
)
async def v1_accommodation_id_delete(
    id: Annotated[StrictStr, Field(description="Accommodation Id")] = Path(..., description="Accommodation Id"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> PGCRUDResult:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().v1_accommodation_id_delete(id)


@router.get(
    "/v1/AccommodationTypes",
    responses={
        200: {"model": List[AccoTypes], "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="GET Accommodation Types List",
    response_model_by_alias=True,
)
async def v1_accommodation_types_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language, possible values: &#39;de|it|en|nl|cs|pl|fr|ru&#39; only one language supported (default:&#39;null&#39; all languages are displayed)", alias="language"),
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    idlist: Optional[StrictStr] = Query(None, description="", alias="idlist"),
    seed: Optional[StrictStr] = Query(None, description="", alias="seed"),
    type: Annotated[Optional[StrictStr], Field(description="Type to filter for ('Board','Type','Theme','Category','Badge','SpecialFeature')")] = Query(None, description="Type to filter for (&#39;Board&#39;,&#39;Type&#39;,&#39;Theme&#39;,&#39;Category&#39;,&#39;Badge&#39;,&#39;SpecialFeature&#39;)", alias="type"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[AccoTypes]:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().v1_accommodation_types_get(language, pagenumber, pagesize, idlist, seed, type, fields, searchfilter, rawfilter, rawsort, removenullvalues)


@router.get(
    "/v1/AccommodationTypes/{id}",
    responses={
        200: {"model": AccoTypes, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="GET Accommodation Types Single",
    response_model_by_alias=True,
)
async def single_accommodation_types(
    id: Annotated[StrictStr, Field(description="ID of the AccommodationType")] = Path(..., description="ID of the AccommodationType"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language, possible values: &#39;de|it|en|nl|cs|pl|fr|ru&#39; only one language supported (default:&#39;null&#39; all languages are displayed)", alias="language"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> AccoTypes:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().single_accommodation_types(id, language, fields, removenullvalues)


@router.get(
    "/v1/AccommodationFeatures",
    responses={
        200: {"model": List[AccoFeatures], "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="GET Accommodation Feature List (LTS Features)",
    response_model_by_alias=True,
)
async def v1_accommodation_features_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language, possible values: &#39;de|it|en|nl|cs|pl|fr|ru&#39; only one language supported (default:&#39;null&#39; all languages are displayed)", alias="language"),
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    idlist: Optional[StrictStr] = Query(None, description="", alias="idlist"),
    seed: Optional[StrictStr] = Query(None, description="", alias="seed"),
    ltst0idfilter: Annotated[Optional[StrictStr], Field(description="Filtering by LTS T0ID, filter behaviour is \"startswith\" so it is possible to send only one character, (default: blank)")] = Query(None, description="Filtering by LTS T0ID, filter behaviour is \&quot;startswith\&quot; so it is possible to send only one character, (default: blank)", alias="ltst0idfilter"),
    source: Annotated[Optional[StrictStr], Field(description="IF source = \"lts\" the Features list is returned in XML Format directly from LTS, (default: blank)")] = Query(None, description="IF source &#x3D; \&quot;lts\&quot; the Features list is returned in XML Format directly from LTS, (default: blank)", alias="source"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[AccoFeatures]:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().v1_accommodation_features_get(language, pagenumber, pagesize, idlist, seed, ltst0idfilter, source, fields, searchfilter, rawfilter, rawsort, removenullvalues)


@router.get(
    "/v1/AccommodationFeatures/{id}",
    responses={
        200: {"model": AccoFeatures, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="GET Accommodation Feature Single (LTS Features)",
    response_model_by_alias=True,
)
async def single_accommodation_features(
    id: Annotated[StrictStr, Field(description="ID of the AccommodationFeature")] = Path(..., description="ID of the AccommodationFeature"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language, possible values: &#39;de|it|en|nl|cs|pl|fr|ru&#39; only one language supported (default:&#39;null&#39; all languages are displayed)", alias="language"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> AccoFeatures:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().single_accommodation_features(id, language, fields, removenullvalues)


@router.get(
    "/v1/AccommodationRoom",
    responses={
        200: {"model": List[AccommodationRoomLinked], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="GET Accommodation Room Info by Accommodation",
    response_model_by_alias=True,
)
async def accommodation_room_list(
    accoid: Annotated[Optional[StrictStr], Field(description="Accommodation ID")] = Query(None, description="Accommodation ID", alias="accoid"),
    idsource: Annotated[Optional[StrictStr], Field(description="HGV ID or LTS ID of the Accommodation (possible values:'lts','hgv','a0r_id'), (default:'lts')")] = Query('lts', description="HGV ID or LTS ID of the Accommodation (possible values:&#39;lts&#39;,&#39;hgv&#39;,&#39;a0r_id&#39;), (default:&#39;lts&#39;)", alias="idsource"),
    source: Annotated[Optional[StrictStr], Field(description="Source Filter (possible values:'lts','hgv'), (default:null)")] = Query(None, description="Source Filter (possible values:&#39;lts&#39;,&#39;hgv&#39;), (default:null)", alias="source"),
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    idlist: Optional[StrictStr] = Query(None, description="", alias="idlist"),
    getall: Annotated[Optional[StrictBool], Field(description="Get Rooms from all sources (If an accommodation is bookable on Booking Southtyrol, rooms from this source are returned, setting getall to true returns also LTS Rooms), (default:false)")] = Query(False, description="Get Rooms from all sources (If an accommodation is bookable on Booking Southtyrol, rooms from this source are returned, setting getall to true returns also LTS Rooms), (default:false)", alias="getall"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")] = Query(None, description="Language filter (returns only data available in the selected Language, Separator &#39;,&#39; possible values: &#39;de,it,en,nl,sc,pl,fr,ru&#39;, &#39;null&#39;: Filter disabled)", alias="langfilter"),
    updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")] = Query(None, description="Returns data changed after this date Format (yyyy-MM-dd), (default: &#39;null&#39;)", alias="updatefrom"),
    seed: Optional[StrictStr] = Query(None, description="", alias="seed"),
    publishedon: Optional[StrictStr] = Query(None, description="", alias="publishedon"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[AccommodationRoomLinked]:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().accommodation_room_list(accoid, idsource, source, pagenumber, pagesize, idlist, getall, fields, language, langfilter, updatefrom, seed, publishedon, searchfilter, rawfilter, rawsort, removenullvalues)


@router.get(
    "/v1/AccommodationRoom/{id}",
    responses={
        200: {"model": AccommodationRoomLinked, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="GET Accommodation Room Info Single",
    response_model_by_alias=True,
)
async def single_accommodation_room(
    id: Annotated[StrictStr, Field(description="AccommodationRoom ID")] = Path(..., description="AccommodationRoom ID"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> AccommodationRoomLinked:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().single_accommodation_room(id, language, fields, removenullvalues)


@router.post(
    "/v1/AccommodationAvailable",
    responses={
        200: {"model": AccommodationV2JsonResultWithBookingInfo, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        401: {"model": ProblemDetails, "description": "Unauthorized"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="POST Pass Accommodation Ids and get Accommodations with Availability Information / Availability Information Only &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Accommodation-Workflow#availability-search\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki Availability Search&lt;/a&gt;",
    response_model_by_alias=True,
)
async def v1_accommodation_available_post(
    availabilitychecklanguage: Annotated[Optional[StrictStr], Field(description="Language of the Availability Response")] = Query('en', description="Language of the Availability Response", alias="availabilitychecklanguage"),
    boardfilter: Annotated[Optional[StrictStr], Field(description="Boardfilter (BITMASK values: 0 = (all boards), 1 = (without board), 2 = (breakfast), 4 = (half board), 8 = (full board), 16 = (All inclusive), 'null' = No Filter)")] = Query(None, description="Boardfilter (BITMASK values: 0 &#x3D; (all boards), 1 &#x3D; (without board), 2 &#x3D; (breakfast), 4 &#x3D; (half board), 8 &#x3D; (full board), 16 &#x3D; (All inclusive), &#39;null&#39; &#x3D; No Filter)", alias="boardfilter"),
    arrival: Annotated[Optional[StrictStr], Field(description="Arrival Date (yyyy-MM-dd) REQUIRED")] = Query(None, description="Arrival Date (yyyy-MM-dd) REQUIRED", alias="arrival"),
    departure: Annotated[Optional[StrictStr], Field(description="Departure Date (yyyy-MM-dd) REQUIRED")] = Query(None, description="Departure Date (yyyy-MM-dd) REQUIRED", alias="departure"),
    roominfo: Annotated[Optional[StrictStr], Field(description="Roominfo Filter REQUIRED (Splitter for Rooms '|' Splitter for Persons Ages ',') (Room Types: 0=notprovided, 1=room, 2=apartment, 4=pitch/tent(onlyLTS), 8=dorm(onlyLTS)) possible Values Example 1-18,10|1-18 = 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:'1-18,18')")] = Query('1-18,18', description="Roominfo Filter REQUIRED (Splitter for Rooms &#39;|&#39; Splitter for Persons Ages &#39;,&#39;) (Room Types: 0&#x3D;notprovided, 1&#x3D;room, 2&#x3D;apartment, 4&#x3D;pitch/tent(onlyLTS), 8&#x3D;dorm(onlyLTS)) possible Values Example 1-18,10|1-18 &#x3D; 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:&#39;1-18,18&#39;)", alias="roominfo"),
    bokfilter: Annotated[Optional[StrictStr], Field(description="Booking Channels Filter (Separator ',' possible values: hgv = (Booking Südtirol), htl = (Hotel.de), exp = (Expedia), bok = (Booking.com), lts = (LTS Availability check), (default:hgv)) REQUIRED")] = Query('hgv', description="Booking Channels Filter (Separator &#39;,&#39; possible values: hgv &#x3D; (Booking Südtirol), htl &#x3D; (Hotel.de), exp &#x3D; (Expedia), bok &#x3D; (Booking.com), lts &#x3D; (LTS Availability check), (default:hgv)) REQUIRED", alias="bokfilter"),
    msssource: Annotated[Optional[StrictStr], Field(description="Source of the Requester (possible value: 'sinfo' = Suedtirol.info, 'sbalance' = Südtirol Balance) REQUIRED")] = Query('sinfo', description="Source of the Requester (possible value: &#39;sinfo&#39; &#x3D; Suedtirol.info, &#39;sbalance&#39; &#x3D; Südtirol Balance) REQUIRED", alias="msssource"),
    detail: Annotated[Optional[StrictStr], Field(description="Include Offer Details (String, 1 = full Details)")] = Query('0', description="Include Offer Details (String, 1 &#x3D; full Details)", alias="detail"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")] = Query(None, description="Locfilter SPECIAL Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki locfilter&lt;/a&gt;", alias="locfilter"),
    publishedon: Optional[StrictStr] = Query(None, description="", alias="publishedon"),
    availabilityonly: Annotated[Optional[StrictBool], Field(description="Get only availability information without Accommodation information")] = Query(False, description="Get only availability information without Accommodation information", alias="availabilityonly"),
    usemsscache: Annotated[Optional[StrictBool], Field(description="Use the MSS Cache to Request Data. No Ids have to be passed, the whole MSS Result of whole South Tyrol is used, available options (null/false/true) default (null), false = pass always the Ids to MSS omit its caching mechanism, true = do not pass ids to MSS get availability result and filter the resultset of MSS, null = let opendatahub decide when to use caching and when not.")] = Query(False, description="Use the MSS Cache to Request Data. No Ids have to be passed, the whole MSS Result of whole South Tyrol is used, available options (null/false/true) default (null), false &#x3D; pass always the Ids to MSS omit its caching mechanism, true &#x3D; do not pass ids to MSS get availability result and filter the resultset of MSS, null &#x3D; let opendatahub decide when to use caching and when not.", alias="usemsscache"),
    uselcscache: Annotated[Optional[StrictBool], Field(description="Currently not used (planned to be active in 2025)")] = Query(True, description="Currently not used (planned to be active in 2025)", alias="uselcscache"),
    removeduplicatesfrom: Annotated[Optional[StrictStr], Field(description="Remove all duplicate offers from the requested booking channel possible values: ('lts','hgv'), default(NULL)")] = Query(None, description="Remove all duplicate offers from the requested booking channel possible values: (&#39;lts&#39;,&#39;hgv&#39;), default(NULL)", alias="removeduplicatesfrom"),
    ltsapiversion: Optional[StrictStr] = Query('v1', description="", alias="ltsapiversion"),
    body: Annotated[Optional[StrictStr], Field(description="Posted Accommodation IDs (Separated by , must be specified in the POST Body as raw)")] = Body(None, description="Posted Accommodation IDs (Separated by , must be specified in the POST Body as raw)"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> AccommodationV2JsonResultWithBookingInfo:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().v1_accommodation_available_post(availabilitychecklanguage, boardfilter, arrival, departure, roominfo, bokfilter, msssource, detail, locfilter, publishedon, availabilityonly, usemsscache, uselcscache, removeduplicatesfrom, ltsapiversion, body)


@router.post(
    "/v1/AvailabilityCheck",
    responses={
        200: {"model": MssResultJsonResultWithBookingInfo, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        401: {"model": ProblemDetails, "description": "Unauthorized"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Accommodation"],
    summary="POST Pass Accommodation Ids and get Accommodations with Availability Information / Availability Information Only",
    response_model_by_alias=True,
)
async def v1_availability_check_post(
    availabilitychecklanguage: Annotated[Optional[StrictStr], Field(description="Language of the Availability Response")] = Query('en', description="Language of the Availability Response", alias="availabilitychecklanguage"),
    boardfilter: Annotated[Optional[StrictStr], Field(description="Boardfilter (BITMASK values: 0 = (all boards), 1 = (without board), 2 = (breakfast), 4 = (half board), 8 = (full board), 16 = (All inclusive), 'null' = No Filter)")] = Query(None, description="Boardfilter (BITMASK values: 0 &#x3D; (all boards), 1 &#x3D; (without board), 2 &#x3D; (breakfast), 4 &#x3D; (half board), 8 &#x3D; (full board), 16 &#x3D; (All inclusive), &#39;null&#39; &#x3D; No Filter)", alias="boardfilter"),
    arrival: Annotated[Optional[StrictStr], Field(description="Arrival Date (yyyy-MM-dd) REQUIRED")] = Query(None, description="Arrival Date (yyyy-MM-dd) REQUIRED", alias="arrival"),
    departure: Annotated[Optional[StrictStr], Field(description="Departure Date (yyyy-MM-dd) REQUIRED")] = Query(None, description="Departure Date (yyyy-MM-dd) REQUIRED", alias="departure"),
    roominfo: Annotated[Optional[StrictStr], Field(description="Roominfo Filter REQUIRED (Splitter for Rooms '|' Splitter for Persons Ages ',') (Room Types: 0=notprovided, 1=room, 2=apartment, 4=pitch/tent(onlyLTS), 8=dorm(onlyLTS)) possible Values Example 1-18,10|1-18 = 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:'1-18,18')")] = Query('1-18,18', description="Roominfo Filter REQUIRED (Splitter for Rooms &#39;|&#39; Splitter for Persons Ages &#39;,&#39;) (Room Types: 0&#x3D;notprovided, 1&#x3D;room, 2&#x3D;apartment, 4&#x3D;pitch/tent(onlyLTS), 8&#x3D;dorm(onlyLTS)) possible Values Example 1-18,10|1-18 &#x3D; 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:&#39;1-18,18&#39;)", alias="roominfo"),
    bokfilter: Annotated[Optional[StrictStr], Field(description="Booking Channels Filter (Separator ',' possible values: hgv = (Booking Südtirol), htl = (Hotel.de), exp = (Expedia), bok = (Booking.com), lts = (LTS Availability check), (default:hgv)) REQUIRED")] = Query('hgv', description="Booking Channels Filter (Separator &#39;,&#39; possible values: hgv &#x3D; (Booking Südtirol), htl &#x3D; (Hotel.de), exp &#x3D; (Expedia), bok &#x3D; (Booking.com), lts &#x3D; (LTS Availability check), (default:hgv)) REQUIRED", alias="bokfilter"),
    msssource: Annotated[Optional[StrictStr], Field(description="Source of the Requester (possible value: 'sinfo' = Suedtirol.info, 'sbalance' = Südtirol Balance) REQUIRED")] = Query('sinfo', description="Source of the Requester (possible value: &#39;sinfo&#39; &#x3D; Suedtirol.info, &#39;sbalance&#39; &#x3D; Südtirol Balance) REQUIRED", alias="msssource"),
    detail: Annotated[Optional[StrictStr], Field(description="Include Offer Details (String, 1 = full Details)")] = Query('0', description="Include Offer Details (String, 1 &#x3D; full Details)", alias="detail"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")] = Query(None, description="Locfilter SPECIAL Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki locfilter&lt;/a&gt;", alias="locfilter"),
    publishedon: Optional[StrictStr] = Query('idm-marketplace', description="", alias="publishedon"),
    usemsscache: Annotated[Optional[StrictBool], Field(description="Use the MSS Cache to Request Data. No Ids have to be passed, the whole MSS Result of whole South Tyrol is used, default(false)")] = Query(False, description="Use the MSS Cache to Request Data. No Ids have to be passed, the whole MSS Result of whole South Tyrol is used, default(false)", alias="usemsscache"),
    uselcscache: Annotated[Optional[StrictBool], Field(description="Currently not used (planned to be active in 2025)")] = Query(False, description="Currently not used (planned to be active in 2025)", alias="uselcscache"),
    removeduplicatesfrom: Annotated[Optional[StrictStr], Field(description="Remove all duplicate offers from the requested booking channel possible values: ('lts','hgv'), default(NULL)")] = Query(None, description="Remove all duplicate offers from the requested booking channel possible values: (&#39;lts&#39;,&#39;hgv&#39;), default(NULL)", alias="removeduplicatesfrom"),
    ltsapiversion: Optional[StrictStr] = Query('v1', description="", alias="ltsapiversion"),
    body: Annotated[Optional[StrictStr], Field(description="Posted Accommodation IDs (Separated by , must be specified in the POST Body as raw)")] = Body(None, description="Posted Accommodation IDs (Separated by , must be specified in the POST Body as raw)"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> MssResultJsonResultWithBookingInfo:
    if not BaseAccommodationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccommodationApi.subclasses[0]().v1_availability_check_post(availabilitychecklanguage, boardfilter, arrival, departure, roominfo, bokfilter, msssource, detail, locfilter, publishedon, usemsscache, uselcscache, removeduplicatesfrom, ltsapiversion, body)
