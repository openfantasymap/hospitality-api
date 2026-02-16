# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

class BaseDeprecatedApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDeprecatedApi.subclasses = BaseDeprecatedApi.subclasses + (cls,)
    async def v1_deprecated_get(
        self,
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")],
        odhtype: Optional[StrictStr],
        type: Annotated[Optional[StrictStr], Field(description="Mandatory search trough Entities (metadata, accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... null = search trough all entities) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\" target=\"_blank\">Wiki Dataset Type</a>")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Mandatory Select a field for the Distinct Query, example fields=Source, arrays are selected with a [*] example HasLanguage[*] / Features[*].Id  (Only one field supported). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")],
        getasarray: Annotated[Optional[StrictBool], Field(description="Get only first selected field as simple string Array")],
        excludenulloremptyvalues: Annotated[Optional[StrictBool], Field(description="Exclude empty and null values from output")],
    ) -> List[str]:
        ...
