def update_dictionary(a_dictionary, key, value):
    try:
        key=""
    except TypeError:
        print("key argument is always a string")
    finally:
        a_dictionary[key]=value
    return(a_dictionary, key, value)