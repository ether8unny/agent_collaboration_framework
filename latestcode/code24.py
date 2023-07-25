```
# Code block 1: Input validation
def send_message(self, sender, recipient, message):
    if sender is None:
        raise ValueError("Sender cannot be None.")
    if recipient is None:
        raise ValueError("Recipient cannot be None.")
    if sender == recipient:
        raise ValueError("Sender and recipient cannot be the same.")
    if message is None or message == "":
        raise ValueError("Message cannot be empty.")
    if len(message) > 100:
        raise ValueError("Message is too long.")

# Code block 2: Message class
class Message:
    def __init__(self, sender, recipient, message):
        self.sender = sender
        self.recipient = recipient
        self.message = message

# Code block 3: Message persistence
class MessagePersistence:
    def __init__(self):
        self.messages = []

    def save_message(self, message):
        self.messages.append(message)

    def retrieve_messages(self):
        return self.messages

# Code block 4: Real-time messaging
import pika

# RabbitMQ configuration
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='messages')

def callback(ch, method, properties, body):
    print("Received message:", body)

channel.basic_consume(queue='messages', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
```

Please note that the code blocks are extracted and formatted for readability, but may not necessarily be complete or functional without the necessary imports, class definitions, etc.