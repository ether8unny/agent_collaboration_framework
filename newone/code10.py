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

```python
from communications import Communications

def main():
    # Instantiate the Communications module
    communications = Communications()

    # Sending a message
    sender = "LLM 1"
    recipient = "LLM 2"
    message = "Hello LLM 2!"
    communications.send_message(sender, recipient, message)

    # Receiving messages
    received_messages = communications.receive_message(recipient)
    for message in received_messages:
        print(f"Received message: {message}")

if __name__ == "__main__":
    main()
```