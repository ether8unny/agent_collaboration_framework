```python
class DataWarehousingModule:
    def __init__(self):
        self.data_warehouse = {}
    
    def store_data(self, key, data):
        if key is not None and data is not None:
            self.data_warehouse[key] = data
    
    def get_data(self, key):
        return self.data_warehouse.get(key, None)
    
    def remove_data(self, key):
        if key in self.data_warehouse:
            del self.data_warehouse[key]
    
    def clear_data_warehouse(self):
        self.data_warehouse = {}
```