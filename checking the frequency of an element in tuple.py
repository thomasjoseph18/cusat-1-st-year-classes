from ast import literal_eval

values = literal_eval(input("Enter the tuple: "))
element = int(input("Enter the element to count: "))

print(element, "occurs", values.count(element), "time(s) in the tuple.")
