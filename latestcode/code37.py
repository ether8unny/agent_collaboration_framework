```python
class TaskAssignmentAndTrackingModule:
    def __init__(self):
        self.tasks = {}
    
    def assign_task(self, task_id, assigned_to):
        if task_id is not None and assigned_to is not None:
            self.tasks[task_id] = assigned_to
    
    def get_assigned_to(self, task_id):
        return self.tasks.get(task_id, None)
    
    def remove_task(self, task_id):
        if task_id is not None and task_id in self.tasks:
            del self.tasks[task_id]
    
    def get_all_tasks(self):
        return self.tasks.copy()
```