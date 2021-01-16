---
tags: [Gripes, Programming]
---

# Assorted Notes on Programming Languages

Most of these are gripes on code style, honestly.

## Ordered Function Parameters of the Same Type

One thing that drives me crazy about function parameters is when you have a bunch of ordered arguments that are all the same type. As an example imagine a function that takes 4 strings. Each string param in that function presumably has a different job, so swapping any 2 of the parameters would likely result in a different output.

```py
def login(user: str, passwd: str, one_time_code: str, user_agent: str):
    # TODO: Add login functionality
    pass

login("password", "username", "firefox", "123456")
```

- If the parameters had different types, the program's compiler would let you know that params are swapped. That doesn't happen when they're the same type.
- If you make the function accept a configuration object instead of the raw params themselves, then it would help developer intention, but really it just MOVES the problem somewhere else.

The part that's frustrating is most programming languages don't have any inherent controls for ensuring that a developer's intentions are considered in cases such as these. In cases such as this where you have multiple ordered function parameters with the same type, they should probably be keyword arguments that can't be supplied as ordered parameters. It would be nice if the compiler warned about this at least, to reduce future ambiguity and miscommunication issues between the developer and the program's source code.

Python has a neat feature where you can force arguments to be kwargs without specifying default values.

```py
# https://www.python.org/dev/peps/pep-3102/

def login(*, user: str, passwd: str, one_time_code: str, user_agent: str):
    # TODO: Add login functionality
    pass

# TypeError: login() takes 0 positional arguments but 4 were given
login("password", "username", "firefox", "123456")

# Developer's intention preserved
login(
    passwd="password",
    user="username",
    user_agent="firefox",
    one_time_code="123456",
)
```

It's a lot wordier, you have to remember to use it, and there's not an easy way to express when you should use it. Any usage of the `*`, "keywords only after this point" character comes down to one's opinion on code style.

## Playing Nice with Source/Version Control Systems

- Source control depends on newline characters to separate chunks of code
- Sometimes chunks of code are a single variable assignment in a list of parameters
- Results in cases where changes that are functionally identical but cannot be merged by the VCS

In the example below, if a dev changes one property of the `login` function call and another dev changes a different propery, the VCS should be able to merge the 2 changes. However, if the function call was short enough to fit on one line and the 2 devs did the exact same thing, the VCS would likely not be able to merge the changes.

```python
# Changes to individual properties can be easily merged.
login(
    passwd="password",
    user="username",
    user_agent="firefox",
    one_time_code="123456",
)

# Changes to individual properties are cannot be easily merged.
login("password", "username", "firefox", "123456")
```

Should there be a VCS that can merge program files based on expressions instead of lines? How do you track changes to a program's expressions?
