```python
# interaction.py
from learning import LearningModule
from task import Task

class InteractionModule:
    def __init__(self, learning_module: LearningModule):
        self.learning_module = learning_module

    def receive_task(self, task: Task, feedback: float):
        self.learning_module.adapt_behavior(feedback)
        self.learning_module.llms = [self.learning_module._update_behavior(llm, feedback) for llm in self.learning_module.llms]


# learning.py 

class LearningModule:
    def __init__(self, llms) -> None:
        self.llms = llms

    def adapt_behavior(self, feedback):
        self.llms = [self._update_behavior(llm, feedback) for llm in self.llms]

    def _update_behavior(self, llm, feedback):
        current_behavior = llm.get_behavior()
        updated_behavior = self.analyze_feedback(current_behavior, feedback)
        llm.update_behavior(updated_behavior)
        return llm

    def analyze_feedback(self, current_behavior, feedback):
        return current_behavior * (1 + feedback/100)


# coordination.py
from llm import LLM  

class CoordinationModule:
    def __init__(self):
        self.llms = [LLM(5) for _ in range(5)]

    def distribute_task(self, task):
        self.llms = [self._update_llm_data(llm, task) for llm in self.llms]

    def _update_llm_data(self, llm, new_data):
        llm.update_data(new_data)
        return llm


# test.py
from llm import LLM
from coordination import CoordinationModule
from learning import LearningModule
from task import Task
from interaction import InteractionModule

coordination = CoordinationModule()

learning = LearningModule(llms = coordination.llms)

interaction = InteractionModule(learning_module = learning)

complex_task = Task('Write a research paper on collaborative AI', 95)

interaction.receive_task(task=complex_task, feedback=30)

# We check if all llms have updated data
print([llm.get_data().description for llm in coordination.llms])

# We check if all llms have updated behavior
print([llm.get_behavior() for llm in coordination.llms])
```