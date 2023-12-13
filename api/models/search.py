class SearchRequestParam:
  def __init__(self, diff: str) -> None:
    self.diff = diff

class SearchResponse:
  def __init__(self, messages: list[str]) -> None:
    self.messages = messages