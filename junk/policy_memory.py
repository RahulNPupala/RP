import json
from collections import defaultdict


class PolicyMemory:

    def __init__(self):
        self.examples = []

    def load(self, path):
        with open(path) as f:
            for line in f:
                self.examples.append(json.loads(line))

    def retrieve(self, record, k=5):
        stage = record["context"]["lifecycle_stage"]
        matches = []
        for e in self.examples:
            if (e["input"]["context"]["lifecycle_stage"] == stage):
                matches.append(e)

        return matches[:k]