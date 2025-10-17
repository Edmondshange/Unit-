ratiosw = {
    ("gleep", "glorp",): 3, # 3 gleeps = 1 glorp
    ("shneep", "glorp"): 60, # 60 shneeps = 1 glorp
}

ratiosr = {
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
    mult = 1
    for i, j in ratios.items():
        print(i,j)
        print(i[-2])
        print(i[-1])

        if i[-2] == from_unit:
            for p, l in ratios.items():
                if p[-1] == to_unit:
                    return int((l/j) * palue) *mult
                else:
                    mult *= l

                
        #print(i[-1])
                
        if i[-1] == from_unit:

            return int(j*palue)
            #print("here",j)


            # for p, l in ratios.items():
            #     if p[-1] == to_unit:
            #         return int(j * palue)
                


    # if (from_unit, to_unit) in ratios:
    #     return palue / ratios[(to_unit, from_unit)]  
       
    # for t, s in ratios.items():
    #     if t[0] == from_unit:
    #         for b, q in ratios.items():
    #            if b[0] == to_unit:
    #                 return int(s* palue)
    
    
    return None

print(convert(ratios, "millimeter", "kilometer", 2))




