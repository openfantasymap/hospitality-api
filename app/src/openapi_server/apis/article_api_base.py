# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.article_types import ArticleTypes
from openapi_server.models.articles_linked import ArticlesLinked
from openapi_server.models.articles_linked_json_result import ArticlesLinkedJsonResult
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

class BaseArticleApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseArticleApi.subclasses = BaseArticleApi.subclasses + (cls,)
    async def v1_article_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")],
        articletype: Annotated[Optional[StrictStr], Field(description="Type of the Article ('null' = Filter disabled, possible values: BITMASK values: 1 = basearticle, 2 = book article, 4 = contentarticle, 8 = eventarticle, 16 = pressarticle, 32 = recipe, 64 = touroperator , 128 = b2b, 256  = idmarticle, 512 = specialannouncement, 1024 = newsfeednoi), (also possible for compatibily reasons: basisartikel, buchtippartikel, contentartikel, veranstaltungsartikel, presseartikel, rezeptartikel, reiseveranstalter, b2bartikel ) (default:'255' == ALL), REFERENCE TO: GET /api/ArticleTypes")],
        articlesubtype: Annotated[Optional[StrictStr], Field(description="Sub Type of the Article (depends on the Maintype of the Article 'null' = Filter disabled)")],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of Article IDs), (default:'null')")],
        langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")],
        sortbyarticledate: Annotated[Optional[StrictBool], Field(description="Sort By Articledate ('true' sorts Articles by Articledate)")],
        odhtagfilter: Annotated[Optional[StrictStr], Field(description="ODH Taglist Filter (refers to Array SmgTags) (String, Separator ',' more Tags possible, available Tags reference to 'v1/ODHTag?validforentity=article'), (default:'null')")],
        tagfilter: Optional[StrictStr],
        odhactive: Annotated[Optional[StrictBool], Field(description="ODH Active (Published) Articles Filter (Refers to field OdhActive) (possible Values: 'true' only published Article, 'false' only not published Articles), (default:'null')")],
        active: Annotated[Optional[StrictBool], Field(description="Active Articles Filter (possible Values: 'true' only Active Articles, 'false' only Disabled Articles), (default:'null')")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        startdate: Annotated[Optional[StrictStr], Field(description="Filter by ArticleDate Format (yyyy-MM-dd HH:mm)")],
        enddate: Annotated[Optional[StrictStr], Field(description="Filter by ArticleDate Format (yyyy-MM-dd HH:mm)")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        source: Annotated[Optional[StrictStr], Field(description="Filter by Source (Separator ','), (Sources available 'idm','noi'...),(default: 'null')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> ArticlesLinkedJsonResult:
        ...


    async def v1_article_post(
        self,
        articles_linked: Annotated[Optional[ArticlesLinked], Field(description="Article Object")],
    ) -> PGCRUDResult:
        ...


    async def single_article(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Article")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> ArticlesLinked:
        ...


    async def v1_article_id_put(
        self,
        id: Annotated[StrictStr, Field(description="Article Id")],
        articles_linked: Annotated[Optional[ArticlesLinked], Field(description="Article Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_article_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="Article Id")],
    ) -> PGCRUDResult:
        ...


    async def v1_article_types_get(
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
    ) -> List[ArticleTypes]:
        ...


    async def single_article_types(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Article Type")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> ArticleTypes:
        ...
