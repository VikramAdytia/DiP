def function(**kwargs):
    return {v if v.__hash__ is not None else str(v) + " neHash": k for k, v in kwargs.items()}


print(function(arg1="Hello", arg2=2, arg3="123", arg4=[1, 2, 3, 4, 5]))
