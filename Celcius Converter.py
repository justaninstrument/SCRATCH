def convert (s= input("Enter your temperature in Farenheit?")):
    f = float(s)
    c = (f -32) * 5/9
    return c 

print (convert())