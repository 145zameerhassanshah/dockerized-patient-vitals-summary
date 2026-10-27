import csv

CSV_FILE = "patient_vitals.csv"

def load_vitals(filename):
    records = []
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append({
                "patient_id": row["patient_id"],
                "systolic": float(row["systolic"]),
                "diastolic": float(row["diastolic"]),
                "heart_rate": float(row["heart_rate"]),
            })
    return records

def calculate_average(records, field):
    values = [record[field] for record in records]
    return sum(values) / len(values)

def main():
    records = load_vitals(CSV_FILE)
    if not records:
        print("No patient records found.")
        return

    print("=" * 45)
    print("PATIENT VITALS SUMMARY")
    print("=" * 45)
    print(f"Total patient records : {len(records)}")
    print(f"Average systolic BP   : {calculate_average(records, 'systolic'):.2f} mmHg")
    print(f"Average diastolic BP  : {calculate_average(records, 'diastolic'):.2f} mmHg")
    print(f"Average heart rate    : {calculate_average(records, 'heart_rate'):.2f} bpm")
    print("=" * 45)
    print("Data type: Synthetic educational data")

if __name__ == "__main__":
    main()
