```python
class CommunicationsModule:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, message):
        if sender is None or recipient is None or message is None:
            return False

        self.messages.append({
            'sender': sender,
            'recipient': recipient,
            'message': message
        })

        return True

    def get_messages(self):
        return self.messages
```