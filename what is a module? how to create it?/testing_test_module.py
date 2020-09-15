import testmodule as tm
tm.helloworld()
x=tm.name_of_author[0]
print(x)
# built-in function to list all the function names (or variable names) in a module. The dir() function
function_names=dir(tm)
print('listing the function,names of variables in a module using the dir() built-in-function',function_names)
