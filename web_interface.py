class WebInterface:
    def __init__(self):
        # Initialize necessary attributes
        self.user_input = None
        self.response = None

    def get_user_input(self):
        # Get user input from the web interface
        self.user_input = input("Enter your input: ")

    def send_response(self):
        # Send the response back to the web interface
        print(self.response)
