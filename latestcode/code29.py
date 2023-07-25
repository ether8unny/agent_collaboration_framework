```python
class InformationSharingModule:
    def __init__(self):
        self.information = {}
    
    def share_information(self, key, value):
        if key is not None and value is not None:
            self.information[key] = value
    
    def get_information(self, key):
        return self.information.get(key, None)
    
    def remove_information(self, key):
        if key is not None and key in self.information:
            del self.information[key]
    
    def get_all_information(self):
        return self.information.copy()
```