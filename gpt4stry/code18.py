```python
# main.py
from llm import LLM
from coordination import CoordinationModule
from learning import LearningModule
from task import Task
from interaction import InteractionModule


coordination = CoordinationModule()

learning = LearningModule(coordination.llms)

interaction = InteractionModule(learning)

complex_task = Task('Write a research paper on collaborative AI', 95)

interaction.receive_task(task=complex_task, feedback=20)

print([llm.get_data().description for llm in coordination.llms])

print([llm.get_behavior() for llm in coordination.llms])
```
