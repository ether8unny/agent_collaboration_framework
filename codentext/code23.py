```python
from llm import LLM
from collaboration_manager import CollaborationManager
from user_interface import UserInterface


llm1 = LLM("LLM1", "Model1")
llm2 = LLM("LLM2", "Model2")

collaboration_manager = CollaborationManager()
collaboration_manager.register_llm(llm1)
collaboration_manager.register_llm(llm2)

user_interface = UserInterface()

while True:
    user_input = user_interface.get_user_input()

    collaboration_manager.train_llms(user_input)

    results = collaboration_manager.infer_llms(user_input)

    user_interface.display_results(results)
```

```python
class UserInterface:
    def get_user_input(self):
        user_input = input("Enter your input: ")
        return user_input

    def display_results(self, results):
        print("Collaborative Results:")
        for result in results:
            print(result)
```