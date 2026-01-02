class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.memory = {}
    
    def store_memory(self, key, value):
        self.memory[key] = value
    
    def retrieve_memory(self, key):
        return self.memory.get(key, None)
    
    def act(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def learn(self, experience):
        raise NotImplementedError("Subclasses should implement this method.")