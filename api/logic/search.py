from models.search import SearchRequestParam, SearchResponse

from database.search import serch_from_diff

def serch_logic(param: SearchRequestParam) -> SearchResponse:
  return SearchResponse(serch_from_diff(param.diff))