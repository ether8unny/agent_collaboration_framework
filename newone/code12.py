```python
class Communications:
    def __init__(self):
        self.message_queue = []

    def send_message(self, sender, recipient, message):
        self.message_queue.append({"sender": sender, "recipient": recipient, "message": message})

    def receive_message(self, recipient):
        received_messages = []
        for message in self.message_queue:
            if message["recipient"] == recipient:
                received_messages.append(message["message"])
        self.message_queue = [message for message in self.message_queue if message["recipient"] != recipient]
        return received_messages
```