import json

INPUT_FILE = "results/scored.jsonl"

def main():
    total = 0
    errors = 0

    risk_total = 0
    risk_errors = 0

    safe_total = 0
    safe_errors = 0

    with open(INPUT_FILE, "r") as f:
        for line in f:
            row = json.loads(line)

            total += 1

            is_error = not row["is_correct"]

            if is_error:
                errors += 1

            if row["gate_status"] == "RISK":
                risk_total += 1
                if is_error:
                    risk_errors += 1

            elif row["gate_status"] == "SAFE":
                safe_total += 1
                if is_error:
                    safe_errors += 1

    def rate(e, t):
        return 0 if t == 0 else e / t

    print("\n=== RESULTS ===\n")

    print(f"TOTAL: {total}")
    print(f"ERRORS: {errors} ({rate(errors, total):.2%})\n")

    print(f"RISK: {risk_total}")
    print(f"  errors: {risk_errors} ({rate(risk_errors, risk_total):.2%})\n")

    print(f"SAFE: {safe_total}")
    print(f"  errors: {safe_errors} ({rate(safe_errors, safe_total):.2%})\n")

    if risk_total > 0 and safe_total > 0:
        print("SEPARATION:")
        print(rate(risk_errors, risk_total) - rate(safe_errors, safe_total))

if __name__ == "__main__":
    main()