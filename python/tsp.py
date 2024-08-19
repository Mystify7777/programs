import itertools

def distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def total_distance(route, cities):
    # Calculate the total distance of a route that visits all cities
    dist = 0
    for i in range(len(route) - 1):
        dist += distance(cities[route[i]], cities[route[i + 1]])
    dist += distance(cities[route[-1]], cities[route[0]])  # Return to the starting city
    return dist

def tsp_brute_force(cities):
    # Generate all permutations of cities
    all_routes = itertools.permutations(range(len(cities)))
    
    # Initialize variables to track the best route and its distance
    best_route = None
    min_distance = float('inf')
    
    # Iterate through all permutations and find the route with the minimum distance
    for route in all_routes:
        route_distance = total_distance(route, cities)
        if route_distance < min_distance:
            min_distance = route_distance
            best_route = route
    
    return best_route, min_distance

# Example usage:
cities = [(0, 0), (1, 2), (3, 1), (5, 4)]
best_route, min_distance = tsp_brute_force(cities)
print("Best route:", best_route)
print("Minimum distance:", min_distance)
