def safe_print_division(a, b):
    try:
        result=a/b
    except TypeError:
        result="None"
        print("a and b are integers")
    except ZeroDivisionError:
        result="None"
        print("Denominator cannot be 0.")
    finally:
        print("Inside result: {}".format(result),"{:d} / {:d} = {}".format(a, b, result))