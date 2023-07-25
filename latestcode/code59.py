```python
class InformationSharingModule:
    def __init__(self):
        self.shared_information = {}
    
    def share_information(self, key, value):
        if key is not None and value is not None:
            self.shared_information[key] = value
    
    def get_information(self, key):
        return self.shared_information.get(key, None)
    
    def remove_information(self, key):
        if key in self.shared_information:
            del self.shared_information[key]
    
    def clear_information(self):
        self.shared_information = {}
```