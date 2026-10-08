"""
Experiment 5: Inference Rule to Identify Disease Diagnosis Based on Test Results

Algorithm:
1. Take the patient's test results/symptoms as input.
2. Define IF-THEN inference rules for possible diseases.
3. Compare the test results with each rule.
4. If all conditions of a rule are satisfied, infer the corresponding disease.
5. Display the diagnosed disease.
6. If no rule matches, display No diagnosis found.
"""


def diagnose(t):
    rules = [
        (["fever", "cough", "body_pain"], "Flu"),
        (["fever", "cough", "breathing_problem"], "Pneumonia"),
        (["fever", "rash"], "Measles"),
        (["headache", "vomiting"], "Migraine")
    ]

    for symptoms, disease in rules:
        if all(x in t for x in symptoms):
            return disease
    return "No diagnosis found"


tests = input("Enter test results: ").lower().split(",")
print("Diagnosis:", diagnose([x.strip() for x in tests]))

# INPUT:
# fever,cough,body_pain

# OUTPUT:
# Diagnosis: Flu
