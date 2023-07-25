```python
# main.py
from llm import LLM
from learning import LearningModule
from coordination import CoordinationModule
from interaction import InteractionModule
from task import Task

coordination = CoordinationModule()
learning = LearningModule(coordination.llms)
interaction = InteractionModule(learning)
new_task = Task('Write a research paper on collaborative AI', 95)
interaction.receive_task(new_task, 30)
```
