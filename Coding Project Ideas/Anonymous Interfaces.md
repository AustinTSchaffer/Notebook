# Anonymous Interfaces
> A.K.A. Auto-Duck Typing

One of the major problems with Python is its lack of strictly enforced type safety. Python has since introduced their "typing" module, which allows you to opt-in to an (at least perceived) sense of type safety. There's projects out there that strictly enforce that type safety.

What if you could have your cake and eat it too?

If say you have a function that accepts a parameter of an unknown type, the compiler should be able to still tell which methods the developer is attempting to use against that parameter. It should also be able to similarly tell what the return values of those parameter methods are.

In the example below, we can infer a couple of things about the typing of `param`

- `param` has a single method with no required arguments named `method_a`
- `method_a` returns a non-nullable value (i.e. an `Any`)
- However, `method_a` returns a value that has a single method with no required arguments named `method_b`
- `method_b` returns a potentially nullable value (i.e. an `Optional[Any]`)

```python
def some_method(param):
    x = param.method_a()
    print(x.method_b())
```

We could now rewrite the snippet with appropriate type information. Alternatively, the compiler could also determine this type information for `param` and automatically generate type information for the `param`. You could think if this type information as an anonymous interface for `param`. Thereby any values that implicitly satisfy that interface would be an appropriate argument for this method.

## Back to Java

Taking this back to Java, one problem with explicitly specifying interfaces for your parameters is specificity. What if you specify a parameter type as a `List<String>`, but your method doesn't actually care about the element order? Would a `Collection<String>` be more appropriate for that use case? What if the method only calls `.toString()` on that parameter? Could the compiler hint that the parameter's type of `List<String>` is to specific for the needs of the method? Is this speculation not useful if the method is satisfying a requirement for an existing interface?
