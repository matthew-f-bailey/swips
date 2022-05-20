
class NotPossibleError(Exception):
    """
        Error to raise when no connection found between 2 words
    """
    def __init__(self, *args: object) -> None:
        self.msg = "Not Possible to get from one to another"
    def __str__(self) -> str:
        return self.msg