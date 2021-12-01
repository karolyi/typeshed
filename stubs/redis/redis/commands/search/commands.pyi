from typing import Any
from typing_extensions import Literal

NUMERIC: Literal["NUMERIC"]

CREATE_CMD: Literal["FT.CREATE"]
ALTER_CMD: Literal["FT.ALTER"]
SEARCH_CMD: Literal["FT.SEARCH"]
ADD_CMD: Literal["FT.ADD"]
ADDHASH_CMD: Literal["FT.ADDHASH"]
DROP_CMD: Literal["FT.DROP"]
EXPLAIN_CMD: Literal["FT.EXPLAIN"]
EXPLAINCLI_CMD: Literal["FT.EXPLAINCLI"]
DEL_CMD: Literal["FT.DEL"]
AGGREGATE_CMD: Literal["FT.AGGREGATE"]
CURSOR_CMD: Literal["FT.CURSOR"]
SPELLCHECK_CMD: Literal["FT.SPELLCHECK"]
DICT_ADD_CMD: Literal["FT.DICTADD"]
DICT_DEL_CMD: Literal["FT.DICTDEL"]
DICT_DUMP_CMD: Literal["FT.DICTDUMP"]
GET_CMD: Literal["FT.GET"]
MGET_CMD: Literal["FT.MGET"]
CONFIG_CMD: Literal["FT.CONFIG"]
TAGVALS_CMD: Literal["FT.TAGVALS"]
ALIAS_ADD_CMD: Literal["FT.ALIASADD"]
ALIAS_UPDATE_CMD: Literal["FT.ALIASUPDATE"]
ALIAS_DEL_CMD: Literal["FT.ALIASDEL"]
INFO_CMD: Literal["FT.INFO"]
SUGADD_COMMAND: Literal["FT.SUGADD"]
SUGDEL_COMMAND: Literal["FT.SUGDEL"]
SUGLEN_COMMAND: Literal["FT.SUGLEN"]
SUGGET_COMMAND: Literal["FT.SUGGET"]
SYNUPDATE_CMD: Literal["FT.SYNUPDATE"]
SYNDUMP_CMD: Literal["FT.SYNDUMP"]

NOOFFSETS: Literal["NOOFFSETS"]
NOFIELDS: Literal["NOFIELDS"]
STOPWORDS: Literal["STOPWORDS"]
WITHSCORES: Literal["WITHSCORES"]
FUZZY: Literal["FUZZY"]
WITHPAYLOADS: Literal["WITHPAYLOADS"]

class SearchCommands:
    def batch_indexer(self, chunk_size: int = ...): ...
    def create_index(
        self,
        fields,
        no_term_offsets: bool = ...,
        no_field_flags: bool = ...,
        stopwords: Any | None = ...,
        definition: Any | None = ...,
    ): ...
    def alter_schema_add(self, fields): ...
    def drop_index(self, delete_documents: bool = ...): ...
    def dropindex(self, delete_documents: bool = ...): ...
    def add_document(
        self,
        doc_id,
        nosave: bool = ...,
        score: float = ...,
        payload: Any | None = ...,
        replace: bool = ...,
        partial: bool = ...,
        language: Any | None = ...,
        no_create: bool = ...,
        **fields,
    ): ...
    def add_document_hash(self, doc_id, score: float = ..., language: Any | None = ..., replace: bool = ...): ...
    def delete_document(self, doc_id, conn: Any | None = ..., delete_actual_document: bool = ...): ...
    def load_document(self, id): ...
    def get(self, *ids): ...
    def info(self): ...
    def search(self, query): ...
    def explain(self, query): ...
    def explain_cli(self, query): ...
    def aggregate(self, query): ...
    def spellcheck(self, query, distance: Any | None = ..., include: Any | None = ..., exclude: Any | None = ...): ...
    def dict_add(self, name, *terms): ...
    def dict_del(self, name, *terms): ...
    def dict_dump(self, name): ...
    def config_set(self, option, value): ...
    def config_get(self, option): ...
    def tagvals(self, tagfield): ...
    def aliasadd(self, alias): ...
    def aliasupdate(self, alias): ...
    def aliasdel(self, alias): ...
    def sugadd(self, key, *suggestions, **kwargs): ...
    def suglen(self, key): ...
    def sugdel(self, key, string): ...
    def sugget(self, key, prefix, fuzzy: bool = ..., num: int = ..., with_scores: bool = ..., with_payloads: bool = ...): ...
    def synupdate(self, groupid, skipinitial: bool = ..., *terms): ...
    def syndump(self): ...
