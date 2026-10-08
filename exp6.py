"""
Experiment 6: Predicting Student Course Success Based on Attendance and Participation using Bayesian Network

Algorithm:
1. Take attendance and participation as evidence.
2. Define probabilities for course success.
3. Calculate the probability of success for each combination of evidence.
4. Use Bayes' theorem to find the most likely outcome.
5. Predict Success or Failure based on the higher probability.
"""


def predict(attendance, participation):
    # P(Success | Attendance, Participation)
    p = {
        ("High", "High"): 0.95,
        ("High", "Low"): 0.75,
        ("Low", "High"): 0.60,
        ("Low", "Low"): 0.20
    }
    return "Success" if p[(attendance, participation)] >= 0.5 else "Failure"


attendance = input("Attendance (High/Low): ").title()
participation = input("Participation (High/Low): ").title()

print("Prediction:", predict(attendance, participation))

# INPUT:
# Attendance (High/Low): High
# Participation (High/Low): High

# OUTPUT:
# Prediction: Success
