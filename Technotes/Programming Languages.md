# Assorted Notes on Programming Languages

## Ordered Function Parameters of the Same Type

One thing that drives me crazy about function parameters is when you have a bunch of ordered arguments that are all the same type. As an example imagine a function that takes 4 strings. Each string param in that function presumably has a different job, so swapping any 2 of the parameters would likely result in a different output.

```py
def login(user: str, passwd: str, one_time_code: str, user_agent: str):
    # TODO: Add login functionality
    pass

login("somepassword", "someusername", "firefox", "123456")
```

- If the parameters had different types, the program's compiler would let you know that params are swapped. That doesn't happen when they're the same type.
- If you make the function accept a configuration object instead of the raw params themselves, then it would help developer intention, but really it just MOVES the problem somewhere else.

The part that's frustrating is most programming languages don't have any inherent controls for ensuring that a developer's intentions are considered in cases such as these. In cases such as this where you have multiple ordered function parameters with the same type, they should probably be keyword arguments that can't be supplied as ordered parameters. It would be nice if the compiler warned about this at least, to reduce future ambiguity and miscommunication issues between the developer and the program.
