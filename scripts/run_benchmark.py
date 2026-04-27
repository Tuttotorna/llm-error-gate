import json

INPUT_FILE = "results/data.jsonl"
OUTPUT_FILE = "results/scored.jsonl"

def fake_gate(output_text):
    # placeholder semplice (da sostituire)
    if "because" in output_text and "=" in output_text:
        return "RISK", 0.7
    return "SAFE", 0.3

def main():
    results = []

    with open(INPUT_FILE, "r") as f:
        for line in f:
            row = json.loads(line)

            status, score = fake_gate(row["llm_output"])

            row["gate_status"] = status
            row["risk_score"] = score

            results.append(row)

    with open(OUTPUT_FILE, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    print(f"Processed {len(results)} cases")

if __name__ == "__main__":
    main()