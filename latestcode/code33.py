```python
class LearningModule:
    def __init__(self):
        self.learning_data = {}
    
    def store_learning_data(self, key, data):
        if key is not None and data is not None:
            self.learning_data[key] = data
    
    def get_learning_data(self, key):
        return self.learning_data.get(key, None)
    
    def remove_learning_data(self, key):
        if key is not None and key in self.learning_data:
            del self.learning_data[key]
    
    def get_all_learning_data(self):
        return self.learning_data.copy()
```