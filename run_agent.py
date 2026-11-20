# Running the Agent
import json
from dotenv import load_dotenv
from agents.communication_agent import CommunicationAgent

load_dotenv()

def load_examples(path):
    examples = []

    with open(path, "r") as f:
        for line in f:
            examples.append(json.loads(line))

    return examples

def main():
    examples = load_examples("sample.jsonl")
    print(f"Loaded {len(examples)} examples")
    print("-" * 80)

    new_records = load_examples("test_interview.jsonl")
    print(f"Loaded {len(new_records)} new records")
    print("-" * 80)

    agent = CommunicationAgent()
    print("Agent initialized")
    print("-" * 80)

    for row in new_records:
        # new_record = row["input"]
        new_record = row
        decision = agent.decide(new_record, examples)

        print(decision.model_dump_json(indent=2))
        print("-" * 80)

if __name__ == "__main__":
    main()