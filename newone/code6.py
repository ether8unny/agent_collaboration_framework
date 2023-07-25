```python
class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.assigned_llm = None
        self.status = "New"

    def assign_llm(self, llm):
        self.assigned_llm = llm
        
    def set_status(self, status):
        self.status = status

    def get_task_id(self):
        return self.task_id

    def get_description(self):
        return self.description

    def get_assigned_llm(self):
        return self.assigned_llm

    def get_status(self):
        return self.status


class TaskTracker:
    def __init__(self):
        self.tasks = []

    def assign_task(self, task, llm):
        task.assign_llm(llm)
        task.set_status("Assigned")
        self.tasks.append(task)

    def get_task_status(self, task_id):
        for task in self.tasks:
            if task.get_task_id() == task_id:
                return task.get_status()
        return "Task not found"

# Create LLMs
llm1 = "LLM 1"
llm2 = "LLM 2"

# Instantiate task tracker
task_tracker = TaskTracker()

# Create a new task
task1 = Task(1, "Implement feature A")

# Assign the task to LLM 1
task_tracker.assign_task(task1, llm1)

# Get the status of the task
print(task_tracker.get_task_status(1))  # Output: Assigned

# Assign the task to LLM 2
task_tracker.assign_task(task1, llm2)

# Get the status of the task
print(task_tracker.get_task_status(1))  # Output: Assigned

# Create another task
task2 = Task(2, "Fix bug B")

# Get the status of the task
print(task_tracker.get_task_status(2))  # Output: Task not found
```