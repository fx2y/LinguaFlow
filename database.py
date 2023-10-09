class Database:
    def __init__(self):
        self.connection = None
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database_name = None

    def connect(self):
        if self.connection is not None:
            raise ValueError("Already connected")

        # Connect to the database using the configured parameters
        # ...

        self.connection = ...  # store the connection object

    def disconnect(self):
        if self.connection is None:
            raise ValueError("Not connected")

        # Disconnect from the database
        # ...

        self.connection = None

    def execute_query(self, query):
        if self.connection is None:
            raise ValueError("Not connected")

        # Execute the given query on the database and return the result
        # ...

        # return result
