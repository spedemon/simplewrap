
class InstallationError(Exception):
    def __init__(self, value):
        self.value = repr(value)
    def __str__(self):
        return "Installation Error: "+self.value

class UnknownType(Exception):
    def __init__(self, value):
        self.value = repr(value)
    def __str__(self):
        return "Installation Error: "+self.value

class DescriptorError(Exception):
    def __init__(self, value):
        self.value = repr(value)
    def __str__(self):
        return "Error in the descriptor of the C function parameters: "+self.value

