```python
class CommunicationModule:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, message):
        if sender is not None and recipient is not None and message is not None:
            self.messages.append((sender, recipient, message))

    def get_messages(self):
        return self.messages.copy()

    def clear_messages(self):
        self.messages = []
```