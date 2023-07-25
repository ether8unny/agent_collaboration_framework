class Message:
    def __init__(self, sender, receiver, content, metadata=None):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.metadata = metadata

    def set_sender(self, sender):
        self.sender = sender

    def set_receiver(self, receiver):
        self.receiver = receiver

    def set_content(self, content):
        self.content = content

    def set_metadata(self, metadata):
        self.metadata = metadata

    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.receiver

    def get_content(self):
        return self.content

    def get_metadata(self):
        return self.metadata

class Communications:
    def __init__(self):
        self.messages = []

    def send_message(self, message):
        self.messages.append(message)

    def receive_message(self, receiver):
        received_messages = []
        for message in self.messages:
            if message.get_receiver() == receiver:
                received_messages.append(message)
        return received_messages

# Create LLMs
llm1 = "LLM 1"
llm2 = "LLM 2"

# Instantiate communications module
communications = Communications()

# Send a message from LLM 1 to LLM 2
message1 = Message(llm1, llm2, "Hello LLM 2!")
communications.send_message(message1)

# Send a message from LLM 2 to LLM 1
message2 = Message(llm2, llm1, "Hi LLM 1!")
communications.send_message(message2)

# Receive the messages for LLM 1
received_messages = communications.receive_message(llm1)
for message in received_messages:
    print(f"Received message: {message.get_content()}")

# Receive the messages for LLM 2
received_messages = communications.receive_message(llm2)
for message in received_messages:
    print(f"Received message: {message.get_content()}")