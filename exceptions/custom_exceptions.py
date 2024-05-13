class NoInputDataException(Exception):
    """Custom exception class."""
    def __init__(self, message="Input files have no data"):
        self.message = message
        super().__init__(self.message)