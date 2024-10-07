def convert(ratios, from_unit, to_unit, value):
    if from_unit == to_unit:
        return value

    if (from_unit, to_unit) in ratios:
        return value / ratios[(from_unit, to_unit)]

    return None