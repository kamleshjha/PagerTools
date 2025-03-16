from flask import request

def convert_unit_route():
    value = float(request.form["value"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    
    # Conversion logic (example: meters to feet)
    if from_unit == "meters" and to_unit == "feet":
        result = value * 3.28084  # Corrected conversion factor
    elif from_unit == "feet" and to_unit == "meters":
        result = value / 3.28084  # Corrected conversion factor
    else:
        result = "Unsupported conversion"
    
    return str(result)