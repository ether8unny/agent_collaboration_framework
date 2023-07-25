```python
# Code:
class TaskAssignmentAndTrackingModule:
    def __init__(self):
        self.tasks = {}
    
    def assign_task(self, task_id, assigned_to):
        if task_id is None or assigned_to is None:
            raise ValueError("Invalid input: task_id and assigned_to cannot be None.")
        if not isinstance(task_id, int) or not isinstance(assigned_to, str):
            raise TypeError("Invalid input type: task_id should be an integer and assigned_to should be a string.")
        if task_id in self.tasks:
            raise ValueError(f"A task with task_id='{task_id}' already exists.")
        self.tasks[task_id] = assigned_to
    
    def remove_task(self, task_id):
        if task_id is None:
            raise ValueError("Invalid input: task_id cannot be None.")
        if not isinstance(task_id, int):
            raise TypeError("Invalid input type: task_id should be an integer.")
        if task_id not in self.tasks:
            raise ValueError(f"No task with task_id='{task_id}' exists.")
        del self.tasks[task_id]
    
    def get_assigned_agent(self, task_id):
        if task_id is None:
            raise ValueError("Invalid input: task_id cannot be None.")
        if not isinstance(task_id, int):
            raise TypeError("Invalid input type: task_id should be an integer.")
        if task_id not in self.tasks:
            raise ValueError(f"No task with task_id='{task_id}' exists.")
        return self.tasks[task_id]
    
    def get_all_tasks(self):
        return self.tasks
```
