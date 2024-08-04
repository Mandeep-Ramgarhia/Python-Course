To insert characters that cannot be directly used in a string, we use an escape sequence character.
An escape sequence character is a backslash \ followed by the character you want to insert.
An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:
print("This doesnt "execute")
print("This will \" execute")

More on Print statement:
The syntax of a print statement looks something like this:
print(object(s), sep=separator, end=end, file=file, flush=flush)
