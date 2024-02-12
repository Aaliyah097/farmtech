class Error:
    def __init__(self, status: int, data: str):
        self.status = status
        self.data = data
