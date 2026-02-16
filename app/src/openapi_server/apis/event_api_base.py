# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.event_linked import EventLinked
from openapi_server.models.event_linked_json_result import EventLinkedJsonResult
from openapi_server.models.event_types import EventTypes
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

class BaseEventApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEventApi.subclasses = BaseEventApi.subclasses + (cls,)
    async def v1_event_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of Event IDs, 'null' = No Filter), (default:'null')")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")],
        rancfilter: Annotated[Optional[StrictStr], Field(description="Rancfilter, Return only Events with this Ranc assigned (1 = not visible, 3 = visible, 4 = important, 5 = top-event),(default: 'null')")],
        topicfilter: Annotated[Optional[StrictStr], Field(description="Topic ID Filter (Filter by Topic ID) BITMASK refers to 'v1/EventTopics',(default: 'null')")],
        orgfilter: Annotated[Optional[StrictStr], Field(description="Organization Filter (Filter by Organizer RID)")],
        odhtagfilter: Annotated[Optional[StrictStr], Field(description="ODH Taglist Filter (refers to Array SmgTags) (String, Separator ',' more Tags possible, available Tags reference to 'v1/ODHTag?validforentity=event'), (default:'null')")],
        tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")],
        active: Annotated[Optional[StrictBool], Field(description="Active Events Filter (possible Values: 'true' only Active Events, 'false' only Disabled Events), (default:'null')")],
        odhactive: Annotated[Optional[StrictBool], Field(description="ODH Active (Published) Events Filter (Refers to field OdhActive) Events Filter (possible Values: 'true' only published Events, 'false' only not published Events), (default:'null')")],
        begindate: Annotated[Optional[StrictStr], Field(description="BeginDate of Events (Format: yyyy-MM-dd), (default: 'null')")],
        enddate: Annotated[Optional[StrictStr], Field(description="EndDate of Events (Format: yyyy-MM-dd), (default: 'null')")],
        sort: Annotated[Optional[StrictStr], Field(description="Sorting Mode of Events ('asc': Ascending simple sort by next begindate, 'desc': simple descent sorting by next begindate, 'upcoming': Sort Events by next EventDate matching passed startdate, 'upcomingspecial': Sort Events by next EventDate matching passed startdate, multiple day events are showed at bottom, default: if no sort mode passed, sort by shortname )")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")],
        source: Annotated[Optional[StrictStr], Field(description="Filter by Source (Separator ','), (Sources available 'lts','trevilab','drin'),(default: 'null')")],
        latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> EventLinkedJsonResult:
        ...


    async def v1_event_post(
        self,
        event_linked: Annotated[Optional[EventLinked], Field(description="Event Object")],
    ) -> PGCRUDResult:
        ...


    async def single_event(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Event")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> EventLinked:
        ...


    async def v1_event_id_put(
        self,
        id: Annotated[StrictStr, Field(description="Event Id")],
        event_linked: Annotated[Optional[EventLinked], Field(description="Event Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_event_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="Event Id")],
    ) -> PGCRUDResult:
        ...


    async def v1_event_topics_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        idlist: Optional[StrictStr],
        seed: Optional[StrictStr],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[EventTypes]:
        ...


    async def single_event_topics(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Event")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> EventTypes:
        ...
