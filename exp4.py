"""
Experiment 4: Traffic Assistance and Route Recommendations Bot

Algorithm:
1. Get the user's current location and destination.
2. Check available routes between them.
3. Analyze traffic conditions for each route.
4. Calculate a score based on distance + traffic delay.
5. Select the route with the lowest score.
6. Display the recommended route and traffic advice.
"""


def traffic_bot(routes):
    best = min(routes, key=lambda r: r["distance"] + r["delay"])
    print("Recommended Route:", best["name"])
    print("Distance:", best["distance"], "km")
    print("Traffic:", best["traffic"])
    print("Advice:", "Use this route" if best["delay"] < 10 else "Expect traffic")


routes = [
    {"name": "Route A", "distance": 10, "delay": 15, "traffic": "High"},
    {"name": "Route B", "distance": 12, "delay": 5, "traffic": "Low"},
    {"name": "Route C", "distance": 8, "delay": 20, "traffic": "Heavy"}
]

traffic_bot(routes)

# INPUT:
# Routes with distance, traffic delay and traffic condition.

# OUTPUT:
# Recommended Route: Route B
# Distance: 12 km
# Traffic: Low
# Advice: Use this route
