```python
class CommunicationsModule:
    def __init__(self):
        self.messages = []
    
    def send_message(self, message):
        if message is not None:
            self.messages.append(message)
    
    def receive_messages(self):
        return self.messages.copy()
    
    def clear_messages(self):
        self.messages.clear()
```