import csv
import statistics

def read_scores(file_path):
    scores = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                score = float(row['Score'])
                scores.append(score)
            except ValueError:
                continue  # Skip invalid data
    return scores

def grade_distribution(scores):
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in scores:
        if score >= 90:
            distribution["A"] += 1
        elif score >= 80:
            distribution["B"] += 1
        elif score >= 70:
            distribution["C"] += 1
        elif score >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1
    return distribution

def analyze_scores(scores):
    return {
        "count": len(scores),
        "average": round(statistics.mean(scores), 2),
        "median": statistics.median(scores),
        "min": min(scores),
        "max": max(scores),
        "grades": grade_distribution(scores)
    }

if __name__ == "__main__":
    file = "scores.csv"
    scores = read_scores(file)
    result = analyze_scores(scores)

    print("📊 Quiz Statistics:")
    print(f"Total Scores: {result['count']}")
    print(f"Average: {result['average']}")
    print(f"Median: {result['median']}")
    print(f"Min Score: {result['min']}")
    print(f"Max Score: {result['max']}")
    print("Grade Distribution:")
    for grade, count in result["grades"].items():
        print(f"  {grade}: {count}")
