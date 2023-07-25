```python
class InformationSharingModule:
    def __init__(self):
        self.shared_information = []
    
    def share_information(self, information):
        if information is not None:
            self.shared_information.append(information)
    
    def get_shared_information(self):
        return self.shared_information.copy()
    
    def clear_shared_information(self):
        self.shared_information = []
```