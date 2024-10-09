def convert(ratios, from_unit, to_unit, value):
    from collections import defaultdict, deque #creating a graph from the ratios

    graph = defaultdict(list)
    
    for (unit1, unit2), ratio in ratios.items():
        graph[unit1].append((unit2, 1 / ratio))  # converting from unit1 to unit2
        graph[unit2].append((unit1, ratio))      # converting from unit2 to unit1
    
    
    queue = deque([(from_unit, 1)])  
    visited = {from_unit: 1} 

    while queue:
        initial_unit, initial_multiplier = queue.popleft()

        
        if initial_unit == to_unit:
            return value * initial_multiplier

        for neighbor, conversion_ratio in graph[initial_unit]:
            if neighbor not in visited:
                visited[neighbor] = initial_multiplier * conversion_ratio
                queue.append((neighbor, visited[neighbor]))        
        
    # no unit found
    return None