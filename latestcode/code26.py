```
class TaskAssignmentTrackingModule:
    def __init__(self):
        self.tasks = {}

    def assign_task(self, task_id, assignee):
        if task_id is None or assignee is None:
            return
        
        # Validate inputs
        # Add additional checks if needed
        
        if task_id in self.tasks:
            raise Exception("Task already assigned")
        
        self.tasks[task_id] = assignee

    def unassign_task(self, task_id):
        if task_id is None:
            return
        
        # Validate inputs
        # Add additional checks if needed

        if task_id not in self.tasks:
            raise Exception("Task does not exist")
        
        del self.tasks[task_id]

    def retrieve_task(self, task_id):
        if task_id is None:
            return None
        
        # Validate inputs
        # Add additional checks if needed

        return self.tasks.get(task_id, None)
```