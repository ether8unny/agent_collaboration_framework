```python
class CollaborationModule:
    def __init__(self):
        self.tasks = []
    
    def create_task(self, id, description, assignee=None, status="Pending"):
        task = {
            'id': id,
            'description': description,
            'assignee': assignee,
            'status': status
        }
        self.tasks.append(task)
    
    def assign_task(self, task_id, assignee):
        task = self.get_task_by_id(task_id)
        if task:
            task['assignee'] = assignee
    
    def start_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task and task['status'] == "Pending":
            task['status'] = "In Progress"
    
    def complete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task and task['status'] == "In Progress":
            task['status'] = "Completed"
    
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def get_assigned_tasks(self, assignee):
        return [task for task in self.tasks if task['assignee'] == assignee]
```

```python
class InformationSharingModule:
    def __init__(self):
        self.data = []
    
    def share_information(self, id, content):
        info = {
            'id': id,
            'content': content
        }
        self.data.append(info)
    
    def get_all_information(self):
        return self.data
    
    def get_information_by_id(self, id):
        for info in self.data:
            if info['id'] == id:
                return info
        return None
```