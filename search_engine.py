class SearchEngine:
    def __init__(self):
        self.name = "search_engine"
        self.parameters = {
            "model": "BERT",
            "input_source": "text",
            "output_format": "text",
            # ...
        }
        self.tools = {
            "search_engine": {
                "name": "Elasticsearch",
                "version": "7.14.0",
                "host": "localhost",
                "port": 9200,
                # ...
            },
            # ...
        }
