class Series(list):
    def __init__(self, dtype: type) -> None:
        self.dtype = dtype
        return super().__init__()

    def append(self, datapoint) -> None:
        if not isinstance(datapoint, self.dtype):
            raise TypeError(f'datapoint must be type {self.dtype!r}, not {type(datapoint)!r}')
        super().append(datapoint)