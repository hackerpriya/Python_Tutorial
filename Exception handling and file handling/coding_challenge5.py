"""
Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.

"""
def divide(a, b):
    try:
        div=a/b
        return div
    except ZeroDivisionError:
        print("Denominator should not be zero")

result=divide(20,10)
print("Result of division",result)