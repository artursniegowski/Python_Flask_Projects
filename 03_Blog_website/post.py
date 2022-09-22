class Post:
    """
    class for representing a single post
    """
    def __init__(self, id:int, title:str, subtitle:str, body:str) -> None:
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body