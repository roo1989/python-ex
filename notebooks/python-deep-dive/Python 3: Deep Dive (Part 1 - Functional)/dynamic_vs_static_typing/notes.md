#### Some languages (Java, C++, Swift) are *statically* typed.

Let's look at at a Java example:
```
String myVar = "Hello";
```
There are a few thiings happening there:
 - Firstly we have the data type of String.
 - Secondly we have the variable name myVar
 - Thirdly we have a value of string literal "Hello"

 What happens under the hood is similar to Python with some minor differences.
 The string "Hello" will be stored as an object in memory with a memory address associated with it. But we also have a referebce in memory that associates that variable_name (memory address to the specific data type String.

#### Python, in contrast. is *dynamically* typed.

``` my_var = 'Hello' ```

The variable name is purely a reference to a string object with value hello.
No type is "attatched" to me_var.

``` my_var = 10 ```

This is perfectly legal, now we simply create another object in memory and change the my_var reference to point to that memory address instead of the "hello" one.

We can use the built-in `type()` function to determine the type of the object currently referenced by a variable.

Remember: variables in Python do not have an inherent static type.

Instead, when we call `type(my_var)`

- Python looks up the object my_var is referencing (pointing to),
and returns the *type of the object* at that memory location.