# Streaming Data Loader Implementation

class StreamingDataLoader:
    def __init__(self, source):
        self.source = source

    def load(self):
        for data in self.source:
            yield data

# Example usage
if __name__ == '__main__':
    data_source = range(10)
    loader = StreamingDataLoader(data_source)
    for item in loader.load():
        print(item)