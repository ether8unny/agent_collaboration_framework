```python
class TaskAssignmentTrackingModule:
    def __init__(self):
        self.tasks = {}
    
    def assign_task(self, task_id, assignee):
        if task_id is None or assignee is None:
            return False
        
        self.tasks[task_id] = assignee
        return True
    
    def unassign_task(self, task_id):
        if task_id is None or task_id not in self.tasks:
            return False
        
        del self.tasks[task_id]
        return True
    
    def get_assignee(self, task_id):
        return self.tasks.get(task_id, None)
    
    def get_all_tasks(self):
        return list(self.tasks.keys())
```