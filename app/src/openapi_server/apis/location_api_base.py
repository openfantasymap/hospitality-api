# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.loc_helperclass import LocHelperclass
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

class BaseLocationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseLocationApi.subclasses = BaseLocationApi.subclasses + (cls,)
    async def v1_location_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default 'en'), if 'null' is passed all languages are returned as Dictionary")],
        pagenumber: Optional[StrictInt],
        type: Annotated[Optional[StrictStr], Field(description="Type ('mta','reg','tvs','mun','fra') Separator ',' : 'null' returns all Location Objects (default)")],
        showall: Annotated[Optional[StrictBool], Field(description="Show all Data (true = all, false = show only data marked as visible)")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (Separator ',') possible values: mta + MetaREGIONID = (Filter by MetaRegion), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), (default:'null')")],
    ) -> List[LocHelperclass]:
        ...


    async def v1_location_skiarea_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default 'en'), if 'null' is passed all languages are returned as Dictionary")],
        pagenumber: Optional[StrictInt],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (Separator ',') possible values: mta + MetaREGIONID = (Filter by MetaRegion), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), (default:'null')")],
    ) -> List[LocHelperclass]:
        ...
