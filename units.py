def convert(ratios, from_unit, to_unit, value):
    accessed_units = set()

    def recursive_conversion(from_unit, to_unit, value):
        if from_unit == to_unit:
            return value

        accessed_units.add(from_unit)

        if (from_unit, to_unit) in ratios:
            return value / ratios[(from_unit, to_unit)]

        if (to_unit, from_unit) in ratios:
            return value * ratios[(to_unit, from_unit)]

        for (start, end), ratio in ratios.items():
            if from_unit == start and end not in accessed_units:
                intermediate_value = value / ratio
                outcome = recursive_conversion(end, to_unit, intermediate_value)
                if outcome is not None:
                    return outcome
            elif from_unit == end and start not in accessed_units:
                intermediate_value = value * ratio
                outcome = recursive_conversion(start, to_unit, intermediate_value)
                if outcome is not None:
                    return outcome

        
        return None

    return recursive_conversion(from_unit, to_unit, value)
