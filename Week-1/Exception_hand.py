a =10
b = 0

try:
    print("Resource Opened")
    c = a/b
except ZeroDivisionError as e:
    print("U can not divide the number by zero", e)

except ValueError as v_e:
    print("Invalid ouput, v_e")

except Exception as e:
    print("General Excepetion")

finally:
    print("Bye")