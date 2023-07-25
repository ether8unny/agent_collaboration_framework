```python
class LearningModule:
    def __init__(self):
        self.training_data = []
    
    def add_training_data(self, data):
        if data is not None:
            self.training_data.append(data)
    
    def get_training_data(self):
        return self.training_data
    
    def clear_training_data(self):
        self.training_data = []
```