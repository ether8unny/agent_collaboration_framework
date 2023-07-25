```python
# task.py

class Task:
    def __init__(self, description, required_skills):
        self.description = description
        self.required_skills = required_skills
      
    def get_description(self):
        return self.description

    def get_required_skills(self):
        return self.required_skills
```

```python
# interaction.py

class InteractionModule:
    def __init__(self):
        pass  # initialize user interface here

    def handle_user_interaction(self):
        input_data = self.get_user_input()
        task = self.format_to_task(input_data)
        return task

    def get_user_input(self):
        return input("Please describe the task and required skills:")

    def format_to_task(self, input_data):
        description, skills = input_data.split(';')
        skills = skills.split(',')
        return Task(description, skills)
```

```python
# coordination.py
from llm import LLM
from task import Task

class CoordinationModule:
    def __init__(self):
        self.llms = [LLM() for _ in range(5)]
    
    def distribute_task(self, task):
        for llm in self.llms:
            llm.assign_task(task)
    
    def synchronize_llms(self):
        if not self.compare_llm_data():
            print("LLMs are not in sync. Updating...")
            self.update_llms_data()
    
    def compare_llm_data(self):
        return False
    
    def update_llms_data(self):
        for llm in self.llms:
            llm.update_behavior("new state")
```