# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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

class BaseAccommodationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAccommodationApi.subclasses = BaseAccommodationApi.subclasses + (cls,)
    async def accommodation_list(
        self,
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page (If availabilitycheck set, pagesize has no effect all Accommodations are returned), (default:10)")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        categoryfilter: Annotated[Optional[StrictStr], Field(description="Categoryfilter BITMASK values: 1 = (not categorized), 2 = (1star), 4 = (1flower), 8 = (1sun), 14 = (1star/1flower/1sun), 16 = (2stars), 32 = (2flowers), 64 = (2suns), 112 = (2stars/2flowers/2suns), 128 = (3stars), 256 = (3flowers), 512 = (3suns), 1024 = (3sstars), 1920 = (3stars/3flowers/3suns/3sstars), 2048 = (4stars), 4096 = (4flowers), 8192 = (4suns), 16384 = (4sstars), 30720 = (4stars/4flowers/4suns/4sstars), 32768 = (5stars), 65536 = (5flowers), 131072 = (5suns), 229376 = (5stars/5flowers/5suns), 'null' = (No Filter), (default:'null')")],
        typefilter: Annotated[Optional[StrictStr], Field(description="Typefilter BITMASK values: 1 = (HotelPension), 2 = (BedBreakfast), 4 = (Farm), 8 = (Camping), 16 = (Youth), 32 = (Mountain), 64 = (Apartment), 128 = (Not defined),'null' = (No Filter), (default:'null')")],
        boardfilter: Annotated[Optional[StrictStr], Field(description="Boardfilter BITMASK values: 0 = (all boards), 1 = (without board), 2 = (breakfast), 4 = (half board), 8 = (full board), 16 = (All inclusive), 'null' = (No Filter), (default:'null')")],
        featurefilter: Annotated[Optional[StrictStr], Field(description="FeatureFilter BITMASK values: 1 = (Group-friendly), 2 = (Meeting rooms), 4 = (Swimming pool), 8 = (Sauna), 16 = (Garage), 32 = (Pick-up service), 64 = (WLAN), 128 = (Barrier-free), 256 = (Special menus for allergy sufferers), 512 = (Pets welcome), 'null' = (No Filter), (default:'null')")],
        featureidfilter: Annotated[Optional[StrictStr], Field(description="Feature Id Filter, LIST filter over ALL Features available. Separator ',' List of Feature IDs, 'null' = (No Filter), (default:'null')")],
        themefilter: Annotated[Optional[StrictStr], Field(description="Themefilter BITMASK values: 1 = (Gourmet), 2 = (At altitude), 4 = (Regional wellness offerings), 8 = (on the wheels), 16 = (With family), 32 = (Hiking), 64 = (In the vineyards), 128 = (Urban vibe), 256 = (At the ski resort), 512 = (Mediterranean), 1024 = (In the Dolomites), 2048 = (Alpine), 4096 = (Small and charming), 8192 = (Huts and mountain inns), 16384 = (Rural way of life), 32768 = (Balance), 65536 = (Christmas markets), 131072 = (Sustainability), 'null' = (No Filter), (default:'null')")],
        badgefilter: Annotated[Optional[StrictStr], Field(description="BadgeFilter BITMASK values: 1 = (Belvita Wellness Hotel), 2 = (Familyhotel), 4 = (Bikehotel), 8 = (Red Rooster Farm), 16 = (Barrier free certificated), 32 = (Vitalpina Hiking Hotel), 64 = (Private Rooms in South Tyrol), 128 = (Vinum Hotels), 'null' = (No Filter), (default:'null')")],
        idfilter: Annotated[Optional[StrictStr], Field(description="IDFilter LIST Separator ',' List of Accommodation IDs, 'null' = (No Filter), (default:'null')")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")],
        altitudefilter: Annotated[Optional[StrictStr], Field(description="Altitude Range Filter SPECIAL (Separator ',' example Value: 500,1000 Altitude from 500 up to 1000 metres), (default:'null')")],
        odhtagfilter: Annotated[Optional[StrictStr], Field(description="ODHTag Filter LIST (refers to Array SmgTags) (String, Separator ',' more ODHTags possible, 'null' = No Filter, available ODHTags reference to 'v1/ODHTag?validforentity=accommodation'), (default:'null')")],
        source: Optional[StrictStr],
        odhactive: Annotated[Optional[StrictBool], Field(description="ODHActive Filter BOOLEAN (refers to field SmgActive) (possible Values: 'null' Displays all Accommodations, 'true' only ODH Active Accommodations, 'false' only ODH Disabled Accommodations), (default:'null')")],
        active: Annotated[Optional[StrictBool], Field(description="TIC Active Filter BOOLEAN (possible Values: 'null' Displays all Accommodations, 'true' only TIC Active Accommodations, 'false' only TIC Disabled Accommodations), (default:'null')")],
        bookablefilter: Optional[StrictBool],
        arrival: Annotated[Optional[StrictStr], Field(description="Arrival DATE (yyyy-MM-dd) REQUIRED ON Availabilitycheck = true, (default:'Today's date')")],
        departure: Annotated[Optional[StrictStr], Field(description="Departure DATE (yyyy-MM-dd) REQUIRED ON Availabilitycheck = true, (default:'Tomorrow's date')")],
        roominfo: Annotated[Optional[StrictStr], Field(description="Roominfo Filter REQUIRED ON Availabilitycheck = true (Splitter for Rooms '|' Splitter for Persons Ages ',') (Room Types: 0=notprovided, 1=room, 2=apartment, 4=pitch/tent(onlyLTS), 8=dorm(onlyLTS)) possible Values Example 1-18,10|1-18 = 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:'1-18,18')")],
        bokfilter: Annotated[Optional[StrictStr], Field(description="Booking Channels Filter REQUIRED ON Availabilitycheck = true (Separator ',' possible values: hgv = (Booking Südtirol), htl = (Hotel.de), exp = (Expedia), bok = (Booking.com), lts = (LTS Availability check)), (default:'hgv')")],
        msssource: Annotated[Optional[StrictStr], Field(description="Source for MSS availability check, (default:'sinfo')")],
        availabilitychecklanguage: Annotated[Optional[StrictStr], Field(description="Language of the Availability Response (possible values: 'de','it','en')")],
        detail: Annotated[Optional[StrictStr], Field(description="Detail of the Availablity check (string, 1 = full Details, 0 = basic Details (default))")],
        tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")],
        availabilitycheck: Annotated[Optional[StrictBool], Field(description="Availability Check BOOLEAN (possible Values: 'true', 'false), (default Value: 'false') NOT AVAILABLE AS OPEN DATA, IF Availabilty Check is true certain filters are Required")],
        latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")],
        langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> AccommodationV2JsonResult:
        ...


    async def v1_accommodation_post(
        self,
        accommodation_v2: Annotated[Optional[AccommodationV2], Field(description="Accommodation Object")],
    ) -> PGCRUDResult:
        ...


    async def single_accommodation(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Accommodation")],
        idsource: Annotated[Optional[StrictStr], Field(description="ID Source Filter (possible values:'lts','hgv','a0r_id'), (default:'lts')")],
        availabilitychecklanguage: Annotated[Optional[StrictStr], Field(description="Language of the Availability Response (possible values: 'de','it','en')")],
        boardfilter: Annotated[Optional[StrictStr], Field(description="Boardfilter BITMASK values: 0 = (all boards), 1 = (without board), 2 = (breakfast), 4 = (half board), 8 = (full board), 16 = (All inclusive), 'null' = (No Filter), (default:'null')")],
        arrival: Annotated[Optional[StrictStr], Field(description="Arrival Date (yyyy-MM-dd) REQUIRED, (default:'Today')")],
        departure: Annotated[Optional[StrictStr], Field(description="Departure Date (yyyy-MM-dd) REQUIRED, (default:'Tomorrow')")],
        roominfo: Annotated[Optional[StrictStr], Field(description="Roominfo Filter REQUIRED (Splitter for Rooms '|' Splitter for Persons Ages ',') (Room Types: 0=notprovided, 1=room, 2=apartment, 4=pitch/tent(onlyLTS), 8=dorm(onlyLTS)) possible Values Example 1-18,10|1-18 = 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:'1-18,18')")],
        bokfilter: Annotated[Optional[StrictStr], Field(description="Booking Channels Filter REQUIRED (Separator ',' possible values: hgv = (Booking Südtirol), htl = (Hotel.de), exp = (Expedia), bok = (Booking.com), lts = (LTS Availability check)), (default:'hgv')")],
        msssource: Optional[StrictStr],
        availabilitycheck: Annotated[Optional[StrictBool], Field(description="Availability Check enabled/disabled (possible Values: 'true', 'false), (default Value: 'false') NOT AVAILABLE AS OPEN DATA")],
        detail: Annotated[Optional[StrictStr], Field(description="Detail of the Availablity check (string, 1 = full Details, 0 = basic Details (default))")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> AccommodationV2:
        ...


    async def v1_accommodation_id_put(
        self,
        id: Annotated[StrictStr, Field(description="Accommodation Id")],
        accommodation_v2: Annotated[Optional[AccommodationV2], Field(description="Accommodation Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_accommodation_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="Accommodation Id")],
    ) -> PGCRUDResult:
        ...


    async def v1_accommodation_types_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")],
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        idlist: Optional[StrictStr],
        seed: Optional[StrictStr],
        type: Annotated[Optional[StrictStr], Field(description="Type to filter for ('Board','Type','Theme','Category','Badge','SpecialFeature')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[AccoTypes]:
        ...


    async def single_accommodation_types(
        self,
        id: Annotated[StrictStr, Field(description="ID of the AccommodationType")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> AccoTypes:
        ...


    async def v1_accommodation_features_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")],
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        idlist: Optional[StrictStr],
        seed: Optional[StrictStr],
        ltst0idfilter: Annotated[Optional[StrictStr], Field(description="Filtering by LTS T0ID, filter behaviour is \"startswith\" so it is possible to send only one character, (default: blank)")],
        source: Annotated[Optional[StrictStr], Field(description="IF source = \"lts\" the Features list is returned in XML Format directly from LTS, (default: blank)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[AccoFeatures]:
        ...


    async def single_accommodation_features(
        self,
        id: Annotated[StrictStr, Field(description="ID of the AccommodationFeature")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language, possible values: 'de|it|en|nl|cs|pl|fr|ru' only one language supported (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> AccoFeatures:
        ...


    async def accommodation_room_list(
        self,
        accoid: Annotated[Optional[StrictStr], Field(description="Accommodation ID")],
        idsource: Annotated[Optional[StrictStr], Field(description="HGV ID or LTS ID of the Accommodation (possible values:'lts','hgv','a0r_id'), (default:'lts')")],
        source: Annotated[Optional[StrictStr], Field(description="Source Filter (possible values:'lts','hgv'), (default:null)")],
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        idlist: Optional[StrictStr],
        getall: Annotated[Optional[StrictBool], Field(description="Get Rooms from all sources (If an accommodation is bookable on Booking Southtyrol, rooms from this source are returned, setting getall to true returns also LTS Rooms), (default:false)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        seed: Optional[StrictStr],
        publishedon: Optional[StrictStr],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[AccommodationRoomLinked]:
        ...


    async def single_accommodation_room(
        self,
        id: Annotated[StrictStr, Field(description="AccommodationRoom ID")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> AccommodationRoomLinked:
        ...


    async def v1_accommodation_available_post(
        self,
        availabilitychecklanguage: Annotated[Optional[StrictStr], Field(description="Language of the Availability Response")],
        boardfilter: Annotated[Optional[StrictStr], Field(description="Boardfilter (BITMASK values: 0 = (all boards), 1 = (without board), 2 = (breakfast), 4 = (half board), 8 = (full board), 16 = (All inclusive), 'null' = No Filter)")],
        arrival: Annotated[Optional[StrictStr], Field(description="Arrival Date (yyyy-MM-dd) REQUIRED")],
        departure: Annotated[Optional[StrictStr], Field(description="Departure Date (yyyy-MM-dd) REQUIRED")],
        roominfo: Annotated[Optional[StrictStr], Field(description="Roominfo Filter REQUIRED (Splitter for Rooms '|' Splitter for Persons Ages ',') (Room Types: 0=notprovided, 1=room, 2=apartment, 4=pitch/tent(onlyLTS), 8=dorm(onlyLTS)) possible Values Example 1-18,10|1-18 = 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:'1-18,18')")],
        bokfilter: Annotated[Optional[StrictStr], Field(description="Booking Channels Filter (Separator ',' possible values: hgv = (Booking Südtirol), htl = (Hotel.de), exp = (Expedia), bok = (Booking.com), lts = (LTS Availability check), (default:hgv)) REQUIRED")],
        msssource: Annotated[Optional[StrictStr], Field(description="Source of the Requester (possible value: 'sinfo' = Suedtirol.info, 'sbalance' = Südtirol Balance) REQUIRED")],
        detail: Annotated[Optional[StrictStr], Field(description="Include Offer Details (String, 1 = full Details)")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")],
        publishedon: Optional[StrictStr],
        availabilityonly: Annotated[Optional[StrictBool], Field(description="Get only availability information without Accommodation information")],
        usemsscache: Annotated[Optional[StrictBool], Field(description="Use the MSS Cache to Request Data. No Ids have to be passed, the whole MSS Result of whole South Tyrol is used, available options (null/false/true) default (null), false = pass always the Ids to MSS omit its caching mechanism, true = do not pass ids to MSS get availability result and filter the resultset of MSS, null = let opendatahub decide when to use caching and when not.")],
        uselcscache: Annotated[Optional[StrictBool], Field(description="Currently not used (planned to be active in 2025)")],
        removeduplicatesfrom: Annotated[Optional[StrictStr], Field(description="Remove all duplicate offers from the requested booking channel possible values: ('lts','hgv'), default(NULL)")],
        ltsapiversion: Optional[StrictStr],
        body: Annotated[Optional[StrictStr], Field(description="Posted Accommodation IDs (Separated by , must be specified in the POST Body as raw)")],
    ) -> AccommodationV2JsonResultWithBookingInfo:
        ...


    async def v1_availability_check_post(
        self,
        availabilitychecklanguage: Annotated[Optional[StrictStr], Field(description="Language of the Availability Response")],
        boardfilter: Annotated[Optional[StrictStr], Field(description="Boardfilter (BITMASK values: 0 = (all boards), 1 = (without board), 2 = (breakfast), 4 = (half board), 8 = (full board), 16 = (All inclusive), 'null' = No Filter)")],
        arrival: Annotated[Optional[StrictStr], Field(description="Arrival Date (yyyy-MM-dd) REQUIRED")],
        departure: Annotated[Optional[StrictStr], Field(description="Departure Date (yyyy-MM-dd) REQUIRED")],
        roominfo: Annotated[Optional[StrictStr], Field(description="Roominfo Filter REQUIRED (Splitter for Rooms '|' Splitter for Persons Ages ',') (Room Types: 0=notprovided, 1=room, 2=apartment, 4=pitch/tent(onlyLTS), 8=dorm(onlyLTS)) possible Values Example 1-18,10|1-18 = 2 Rooms, Room 1 for 2 person Age 18 and Age 10, Room 2 for 1 Person Age 18), (default:'1-18,18')")],
        bokfilter: Annotated[Optional[StrictStr], Field(description="Booking Channels Filter (Separator ',' possible values: hgv = (Booking Südtirol), htl = (Hotel.de), exp = (Expedia), bok = (Booking.com), lts = (LTS Availability check), (default:hgv)) REQUIRED")],
        msssource: Annotated[Optional[StrictStr], Field(description="Source of the Requester (possible value: 'sinfo' = Suedtirol.info, 'sbalance' = Südtirol Balance) REQUIRED")],
        detail: Annotated[Optional[StrictStr], Field(description="Include Offer Details (String, 1 = full Details)")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")],
        publishedon: Optional[StrictStr],
        usemsscache: Annotated[Optional[StrictBool], Field(description="Use the MSS Cache to Request Data. No Ids have to be passed, the whole MSS Result of whole South Tyrol is used, default(false)")],
        uselcscache: Annotated[Optional[StrictBool], Field(description="Currently not used (planned to be active in 2025)")],
        removeduplicatesfrom: Annotated[Optional[StrictStr], Field(description="Remove all duplicate offers from the requested booking channel possible values: ('lts','hgv'), default(NULL)")],
        ltsapiversion: Optional[StrictStr],
        body: Annotated[Optional[StrictStr], Field(description="Posted Accommodation IDs (Separated by , must be specified in the POST Body as raw)")],
    ) -> MssResultJsonResultWithBookingInfo:
        ...
