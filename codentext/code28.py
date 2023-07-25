class LLM:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model

    def train(self, user_input: str) -> None:
        print(f"LLM {self.name} trained on: {user_input}")

    def infer(self, user_input: str) -> str:
        result = f"Inference result for LLM {self.name} with input: {user_input}"
        return result

from typing import List

class CollaborationManager:
    def __init__(self):
        self.llms: List[LLM] = []

    def register_llm(self, llm: LLM) -> None:
        self.llms.append(llm)

    def train_llms(self, user_input: str) -> None:
        for llm in self.llms:
            llm.train(user_input)

    def infer_llms(self, user_input: str) -> List[str]:
        results = []
        for llm in self.llms:
            inference_result = llm.infer(user_input)
            results.append(inference_result)
        return results

class UserInterface:
    def get_user_input(self) -> str:
        user_input = input("Enter your input: ")
        return user_input

    def display_results(self, results: List[str]) -> None:
        print("Collaborative Results:")
        for result in results:
            print(result)

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