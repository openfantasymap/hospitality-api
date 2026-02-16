# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.file_upload_api_base import BaseFileUploadApi
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
from pydantic import StrictStr
from typing import Any, List, Optional
from openapi_server.models.string_string_values_key_value_pair import StringStringValuesKeyValuePair
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/v1/FileUpload",
    responses={
        200: {"description": "OK"},
    },
    tags=["FileUpload"],
    summary=" (Auth)",
    response_model_by_alias=True,
)
async def v1_file_upload_post(
    form: Optional[List[StringStringValuesKeyValuePair]] = Form(None, description=""),
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
    if not BaseFileUploadApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFileUploadApi.subclasses[0]().v1_file_upload_post(form)


@router.post(
    "/v1/FileUpload/Image",
    responses={
        200: {"description": "OK"},
    },
    tags=["FileUpload"],
    summary=" (Auth)",
    response_model_by_alias=True,
)
async def v1_file_upload_image_post(
    form: Optional[List[StringStringValuesKeyValuePair]] = Form(None, description=""),
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
    if not BaseFileUploadApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFileUploadApi.subclasses[0]().v1_file_upload_image_post(form)


@router.delete(
    "/v1/FileDelete/{filepath}",
    responses={
        200: {"description": "OK"},
    },
    tags=["FileUpload"],
    summary=" (Auth)",
    response_model_by_alias=True,
)
async def v1_file_delete_filepath_delete(
    filepath: StrictStr = Path(..., description=""),
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
    if not BaseFileUploadApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFileUploadApi.subclasses[0]().v1_file_delete_filepath_delete(filepath)
