# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.geo_converter_api_base import BaseGeoConverterApi
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
from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/GeoConverter/KmlToGeoJson",
    responses={
        200: {"description": "OK"},
        404: {"model": ProblemDetails, "description": "Not Found"},
    },
    tags=["GeoConverter"],
    summary="Converts the KML file from the supplied URL to GeoJSON.",
    response_model_by_alias=True,
)
async def v1_geo_converter_kml_to_geo_json_get(
    url: Annotated[Optional[StrictStr], Field(description="The URL to the KML file.")] = Query(None, description="The URL to the KML file.", alias="url"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> None:
    if not BaseGeoConverterApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGeoConverterApi.subclasses[0]().v1_geo_converter_kml_to_geo_json_get(url)


@router.post(
    "/v1/GeoConverter/KmlToGeoJson",
    responses={
        200: {"description": "OK"},
    },
    tags=["GeoConverter"],
    summary="Converts the KML provided as the body to GeoJSON.",
    response_model_by_alias=True,
)
async def v1_geo_converter_kml_to_geo_json_post(
    body: Annotated[Optional[StrictStr], Field(description="The KML file content.")] = Query(None, description="The KML file content.", alias="body"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> None:
    if not BaseGeoConverterApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGeoConverterApi.subclasses[0]().v1_geo_converter_kml_to_geo_json_post(body)


@router.get(
    "/v1/GeoConverter/GpxToGeoJson",
    responses={
        200: {"description": "OK"},
        404: {"model": ProblemDetails, "description": "Not Found"},
    },
    tags=["GeoConverter"],
    summary="Converts the GPX file from the supplied URL to GeoJSON.",
    response_model_by_alias=True,
)
async def v1_geo_converter_gpx_to_geo_json_get(
    url: Annotated[Optional[StrictStr], Field(description="The URL to the GPX file.")] = Query(None, description="The URL to the GPX file.", alias="url"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> None:
    if not BaseGeoConverterApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGeoConverterApi.subclasses[0]().v1_geo_converter_gpx_to_geo_json_get(url)


@router.post(
    "/v1/GeoConverter/GpxToGeoJson",
    responses={
        200: {"description": "OK"},
    },
    tags=["GeoConverter"],
    summary="Converts the GPX provided as the body to GeoJSON.",
    response_model_by_alias=True,
)
async def v1_geo_converter_gpx_to_geo_json_post(
    body: Annotated[Optional[StrictStr], Field(description="The GPX file content.")] = Query(None, description="The GPX file content.", alias="body"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> None:
    if not BaseGeoConverterApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGeoConverterApi.subclasses[0]().v1_geo_converter_gpx_to_geo_json_post(body)
