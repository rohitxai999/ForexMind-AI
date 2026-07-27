class BaseAgent:

    def __init__(self, name):
        self.name = name


    def analyze(self, data):
        raise NotImplementedError(
            "Agent must implement analyze method"
        )