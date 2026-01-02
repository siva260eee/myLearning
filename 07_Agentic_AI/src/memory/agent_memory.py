class AgentMemory:
    def __init__(self):
        self.memory_store = {}

    def store_memory(self, key, value):
        self.memory_store[key] = value

    def retrieve_memory(self, key):
        return self.memory_store.get(key, None)

    def update_memory(self, key, value):
        if key in self.memory_store:
            self.memory_store[key] = value
        else:
            raise KeyError(f"Memory key '{key}' not found.")

    def clear_memory(self):
        self.memory_store.clear()