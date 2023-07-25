```python
class CommunicationModule:
    def __init__(self):
        self.messages = []
    
    def send_message(self, sender, recipient, content):
        if sender is not None and recipient is not None and content is not None:
            message = {
                'sender': sender,
                'recipient': recipient,
                'content': content
            }
            self.messages.append(message)
    
    def get_messages(self):
        return self.messages.copy()
    
    def filter_messages_by_sender(self, sender):
        filtered_messages = []
        
        for message in self.messages:
            if message['sender'] == sender:
                filtered_messages.append(message)
        
        return filtered_messages
    
    def filter_messages_by_recipient(self, recipient):
        filtered_messages = []
        
        for message in self.messages:
            if message['recipient'] == recipient:
                filtered_messages.append(message)
        
        return filtered_messages
```