class TaskAssignmentTrackingModule:
    def __init__(self):
        self.task_assignments = {}
    
    def assign_task(self, task_id, assignee):
        if task_id is not None and assignee is not None:
            self.task_assignments[task_id] = assignee
    
    def get_assignee(self, task_id):
        return self.task_assignments.get(task_id, None)
    
    def remove_assignment(self, task_id):
        if task_id in self.task_assignments:
            del self.task_assignments[task_id]
    
    def clear_assignments(self):
        self.task_assignments = {}