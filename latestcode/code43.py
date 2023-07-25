```python
class TaskAssignmentTrackingModule:
    def __init__(self):
        self.tasks = {}
    
    def assign_task(self, task, assignee):
        if task is not None and assignee is not None:
            self.tasks[task] = assignee
    
    def get_assignee(self, task):
        if task in self.tasks:
            return self.tasks[task]
        else:
            return None
    
    def unassign_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
    
    def get_tasks(self):
        return self.tasks.keys()
```
