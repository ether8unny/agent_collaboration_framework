```python
from learning import LearningModule
from task import Task

class InteractionModule:
    def __init__(self, learning_module: LearningModule):
        self.learning_module = learning_module

    def receive_user_input(self, task_desc: str, task_difficulty: int, feedback: float):
        task = Task(task_desc, task_difficulty)
        self.learning_module.adapt_behavior(feedback)
        self.learning_module.distribute_task(task)
```

```python
# main.py
from llm import LLM
from learning import LearningModule
from coordination import CoordinationModule
from interaction import InteractionModule

coordination = CoordinationModule()
learning = LearningModule(coordination.llms)
interaction = InteractionModule(learning)

task_desc = 'Write a research paper on collaborative AI'
task_difficulty = 95
feedback = 30

interaction.receive_user_input(task_desc, task_difficulty, feedback)
```