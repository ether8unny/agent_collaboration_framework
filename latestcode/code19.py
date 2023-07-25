```python
class LearningModule:
    def __init__(self):
        self.knowledge_base = {}

    def add_knowledge(self, knowledge_id, knowledge):
        if knowledge_id not in self.knowledge_base:
            self.knowledge_base[knowledge_id] = knowledge
            return True
        return False

    def get_knowledge(self, knowledge_id):
        return self.knowledge_base.get(knowledge_id)

    def update_knowledge(self, knowledge_id, knowledge):
        if knowledge_id in self.knowledge_base:
            self.knowledge_base[knowledge_id] = knowledge
            return True
        return False

    def delete_knowledge(self, knowledge_id):
        if knowledge_id in self.knowledge_base:
            del self.knowledge_base[knowledge_id]
            return True
        return False

    def get_all_knowledge(self):
        return list(self.knowledge_base.items())
```