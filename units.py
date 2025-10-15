def convert(ratios, from_unit, to_unit, value):

    # STEP 1: Handle the easy case first
    if from_unit == to_unit:
        return value

    # STEP 2: Build my connections map to be able to navigate units
    connections = {}
    for (unit_a, unit_b), ratio in ratios.items():
        if unit_a not in connections:
            connections[unit_a] = []
        if unit_b not in connections:
            connections[unit_b] = []
        connections[unit_a].append((unit_b, 1 / ratio))
        connections[unit_b].append((unit_a, ratio))

    # STEP 3: Search between units
    to_visit = [(from_unit, value)]
    visited = set()

    while to_visit:
        current_unit, current_value = to_visit.pop(0)

        if current_unit == to_unit:
            return current_value

        visited.add(current_unit)

        for next_unit, multiplier in connections.get(current_unit, []):
            if next_unit not in visited:
                new_value = current_value * multiplier
                to_visit.append((next_unit, new_value))

    # No path was found here
    return None
