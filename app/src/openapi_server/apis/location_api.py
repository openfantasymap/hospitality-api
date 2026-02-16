# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.location_api_base import BaseLocationApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.loc_helperclass import LocHelperclass
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/Location",
    responses={
        200: {"model": List[LocHelperclass], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Location"],
    summary="GET Location List (Use in locfilter)",
    response_model_by_alias=True,
)
async def v1_location_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default 'en'), if 'null' is passed all languages are returned as Dictionary")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default &#39;en&#39;), if &#39;null&#39; is passed all languages are returned as Dictionary", alias="language"),
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    type: Annotated[Optional[StrictStr], Field(description="Type ('mta','reg','tvs','mun','fra') Separator ',' : 'null' returns all Location Objects (default)")] = Query(null, description="Type (&#39;mta&#39;,&#39;reg&#39;,&#39;tvs&#39;,&#39;mun&#39;,&#39;fra&#39;) Separator &#39;,&#39; : &#39;null&#39; returns all Location Objects (default)", alias="type"),
    showall: Annotated[Optional[StrictBool], Field(description="Show all Data (true = all, false = show only data marked as visible)")] = Query(True, description="Show all Data (true &#x3D; all, false &#x3D; show only data marked as visible)", alias="showall"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (Separator ',') possible values: mta + MetaREGIONID = (Filter by MetaRegion), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), (default:'null')")] = Query(None, description="Locfilter (Separator &#39;,&#39;) possible values: mta + MetaREGIONID &#x3D; (Filter by MetaRegion), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), (default:&#39;null&#39;)", alias="locfilter"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[LocHelperclass]:
    if not BaseLocationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLocationApi.subclasses[0]().v1_location_get(language, pagenumber, type, showall, locfilter)


@router.get(
    "/v1/Location/Skiarea",
    responses={
        200: {"model": List[LocHelperclass], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Location"],
    summary="GET Skiarea List (Use in locfilter as \&quot;ska\&quot;)",
    response_model_by_alias=True,
)
async def v1_location_skiarea_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default 'en'), if 'null' is passed all languages are returned as Dictionary")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default &#39;en&#39;), if &#39;null&#39; is passed all languages are returned as Dictionary", alias="language"),
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (Separator ',') possible values: mta + MetaREGIONID = (Filter by MetaRegion), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), (default:'null')")] = Query(None, description="Locfilter (Separator &#39;,&#39;) possible values: mta + MetaREGIONID &#x3D; (Filter by MetaRegion), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), (default:&#39;null&#39;)", alias="locfilter"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[LocHelperclass]:
    if not BaseLocationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLocationApi.subclasses[0]().v1_location_skiarea_get(language, pagenumber, locfilter)
