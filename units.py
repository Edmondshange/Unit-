ratios = {
    ("millimeter", "centimeter"): 10, # 10 millimeters = 1 centimeter
    ("centimeter", "meter"): 100, # 100 centimeters = 1 meter
    ("meter", "decameter"): 10, # 10 meters = 1 decameter
    ("decameter", "hectometer"): 10, # 10 decameters = 1 hectometer
    ("hectometer", "kilometer"): 10, # 10 hectometers = 1 kilometer
}

def convert(ratios, from_unit, to_unit, palue):
    if from_unit == to_unit:
        return palue

    if (from_unit, to_unit) in ratios:
        return palue / ratios[(from_unit, to_unit)]
    
    if (to_unit, from_unit) in ratios:
        return palue * ratios[(to_unit, from_unit)]
    
    
    for i, j in ratios.items():
        if i[-2] == from_unit:
            for p, l in ratios.items():
                if p[-2] == to_unit:
                   return int((l/j) * palue)
                
# ratios = {
#     ("millimeter", "centimeter"): 10, # 10 millimeters = 1 centimeter
#     ("centimeter", "meter"): 100, # 100 centimeters = 1 meter
#     ("meter", "decameter"): 10, # 10 meters = 1 decameter
#     ("decameter", "hectometer"): 10, # 10 decameters = 1 hectometer
#     ("hectometer", "kilometer"): 10, # 10 hectometers = 1 kilometer
# }

    store_value = 1
    target_unit = to_unit
    for t, s in ratios.items():
        if t[0] == target_unit:
            store_value = store_value * s
            target_unit = t[-1]
        if target_unit == from_unit:
            return palue * store_value
        
    
    return None


print(convert(ratios, "kilometer", "millimeter", 2))






