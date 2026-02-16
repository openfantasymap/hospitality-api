# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.event_short import EventShort
from openapi_server.models.event_short_by_room import EventShortByRoom
from openapi_server.models.event_short_linked import EventShortLinked
from openapi_server.models.event_short_result import EventShortResult
from openapi_server.models.event_short_types import EventShortTypes
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

class BaseEventShortApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEventShortApi.subclasses = BaseEventShortApi.subclasses + (cls,)
    async def v1_event_short_get(
        self,
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber (Integer)")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Pagesize (Integer), (default: 'null')")],
        startdate: Annotated[Optional[StrictStr], Field(description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp")],
        enddate: Annotated[Optional[StrictStr], Field(description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp")],
        datetimeformat: Annotated[Optional[StrictStr], Field(description="not provided, use default format, for unix timestamp pass \"uxtimestamp\"")],
        source: Annotated[Optional[StrictStr], Field(description="Source of the data, (possible values 'Content' or 'EBMS')")],
        eventlocation: Annotated[Optional[StrictStr], Field(description="<p>Members:</p><ul><li><i>NOI</i> - NOI Techpark</li> <li><i>EC</i> - Eurac</li> <li><i>VV</i> - Virtual Village</li> <li><i>OUT</i> - Other Location</li> </ul>")],
        onlyactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for today.noi.bz.it should be returned")],
        websiteactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for noi.bz.it should be returned")],
        communityactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for Noi community should be returned")],
        active: Annotated[Optional[StrictBool], Field(description="Active Events Filter (possible Values: 'true' only Active Events, 'false' only Disabled Events), (default:'true')")],
        eventids: Annotated[Optional[StrictStr], Field(description="comma separated list of event ids")],
        webaddress: Annotated[Optional[StrictStr], Field(description="Searches the webaddress")],
        tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")],
        sortorder: Annotated[Optional[StrictStr], Field(description="ASC or DESC by StartDate")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")],
        optimizedates: Annotated[Optional[StrictBool], Field(description="Optimizes dates, cuts out all Rooms with Comment \"x\", revisits and corrects start + enddate")],
        latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        lastchange: Optional[StrictStr],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> EventShortResult:
        ...


    async def v1_event_short_post(
        self,
        event_short_linked: Optional[EventShortLinked],
    ) -> PGCRUDResult:
        ...


    async def v1_event_short_detail_id_get(
        self,
        id: Annotated[StrictStr, Field(description="Id of the Event")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        optimizedates: Annotated[Optional[StrictBool], Field(description="Optimizes dates, cuts out all Rooms with Comment \"x\", revisits and corrects start + enddate")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> EventShort:
        ...


    async def single_event_short(
        self,
        id: Annotated[StrictStr, Field(description="Id of the Event")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        optimizedates: Annotated[Optional[StrictBool], Field(description="Optimizes dates, cuts out all Rooms with Comment \"x\", revisits and corrects start + enddate")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> EventShort:
        ...


    async def v1_event_short_id_put(
        self,
        id: StrictStr,
        event_short_linked: Optional[EventShortLinked],
    ) -> PGCRUDResult:
        ...


    async def v1_event_short_id_delete(
        self,
        id: StrictStr,
    ) -> PGCRUDResult:
        ...


    async def v1_event_short_getby_room_booked_get(
        self,
        startdate: Annotated[Optional[StrictStr], Field(description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp")],
        enddate: Annotated[Optional[StrictStr], Field(description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp")],
        datetimeformat: Annotated[Optional[StrictStr], Field(description="not provided, use default format, for unix timestamp pass \"uxtimestamp\"")],
        source: Annotated[Optional[StrictStr], Field(description="Source of the data, (possible values 'Content' or 'EBMS')")],
        eventlocation: Annotated[Optional[StrictStr], Field(description="<p>Members:</p><ul><li><i>NOI</i> - NOI Techpark</li> <li><i>EC</i> - Eurac</li> <li><i>VV</i> - Virtual Village</li> <li><i>OUT</i> - Other Location</li> </ul>")],
        onlyactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for today.noi.bz.it should be returned")],
        websiteactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for noi.bz.it should be returned")],
        communityactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for Noi community should be returned")],
        active: Annotated[Optional[StrictBool], Field(description="Active Events Filter (possible Values: 'true' only Active Events, 'false' only Disabled Events), (default:'true')")],
        tagfilter: Optional[StrictStr],
        eventids: Annotated[Optional[StrictStr], Field(description="comma separated list of event ids")],
        webaddress: Annotated[Optional[StrictStr], Field(description="Filter by WebAddress Field")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")],
        lastchange: Optional[StrictStr],
        updatefrom: Optional[StrictStr],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        eventgrouping: Annotated[Optional[StrictBool], Field(description="Groups Events with the Same Date/Id/Name and adds all Rooms to the SpaceDesc List")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[EventShortByRoom]:
        ...


    async def v1_event_short_types_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        idlist: Optional[StrictStr],
        seed: Optional[StrictStr],
        type: Annotated[Optional[StrictStr], Field(description="Type to filter for ('TechnologyFields','CustomTagging')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[EventShortTypes]:
        ...


    async def single_event_short_types(
        self,
        id: Annotated[StrictStr, Field(description="ID of the EventShort Type")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> EventShortTypes:
        ...
