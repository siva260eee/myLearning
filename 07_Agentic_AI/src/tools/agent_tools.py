def select_tool(tools, criteria):
    """Select a tool based on specified criteria."""
    selected_tools = [tool for tool in tools if criteria(tool)]
    return selected_tools

def execute_tool(tool, *args, **kwargs):
    """Execute a given tool with the provided arguments."""
    if callable(tool):
        return tool(*args, **kwargs)
    raise ValueError("The provided tool is not callable.")

class Tool:
    """A class representing a tool that an agent can use."""
    
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def use(self, *args, **kwargs):
        """Use the tool with the given arguments."""
        return execute_tool(self.function, *args, **kwargs)