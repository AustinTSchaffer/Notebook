# Functional Techniques for C#

> This is a conceptual talk.
> 
> -- Kathleen

Functional vs OO. Functions are first class citizens in a functional language. In the F universe, the central construct is a function. In an OO language, the central construct is a class.

C# is a multiparadigm language. The central construct is a class, but functions are also first class citizens.

## Why C# with Functional

- Lots of usage
- Best of strong typing to reduce accidents
- Generics to reuse type definitions and patterns
- Extention methods to extend types
- Functions are 1st-class citizens (strongly typed delegates)
- Expression trees: a structure to describe delegate contents (great at converting LINQ to T-SQL)
- Pattern matching in C# 8
- Non-null reference types

## Benefits of functional programming in C# <= 7

### Reuse algorithms with different details

```cs
public static Result<object> BillTolls()
    => Handler.Try(() =>
        {
            var tollEvents = tollEventSources
                .SelectMany(tollSource => tollSource.GetTollEvents())
                .Select(tollEvent => BillToll(tollEvent))
                .ToList();

            return Result.Success<object>(null);
        });
```

LINQ's `Select` is C#'s analog for the common term "map". `SelectMany` is similar to the common term "flatten".

### Delegates: Functions as Data

The 2 generic Delegate types are `Action` and `Func`.

### Easier to test (purity)

```cs
class PureOrImpure
{
    public int Sample1()
    {
        // Pure
        return 42;
    }

    public int Sample2(int x, int y)
    {
        // Still pure
        int z = x + y;
        return z;
    }

    public int Sample3(int x, int y)
    {
        // Technically Impure (but logging is important, so we don't care)
        int z = x + y;
        Console.WriteLine(z);
        return z;
    }

    public int Sample3(int x, int y)
    {
        // Impure and useless
        int z = x + y;
        Console.WriteLine(z);
    }

    // Impure, result different based on same input
    public int Sample5() => DateTime.Now.Second;

    // Depends on `Foo`, can still be pure. Documentation is important.
    public int Sample6() => Foo();

    public int Sample7(int x, int y)
    {
        // Exceptions can be considered impure, because they change
        // the next line of code that runs, i.e. changing the universe
        // at design-time and runtime.
        try
        {
            return x / y;
        }
        catch
        {
            throw;
        }
    }
}
```

### The ability to test is a measure of architectural sanity

- Don't mingle pure and impure functional code
- Don't mingle unit tests and functional tests

### Easier to reason about (pattern matching in C# 7)

```cs
class Playing
{
    public void MyMethod(object o)
    {
        var oString = o as string;
        if (oString != null)
        {
            // do something stingy
        }

        // this sucks
    }

    public void MyMethod2(object o)
    {
        if (o is string oString)
        {
            // do something stingy

            // You can also do this in a switch-case statement
        }
    }
}
```

> Most code is prettier if you switch to a `switch`.
>
> -- Kathleen

### Consistent behavior (outside in refactoring)

Refactoring to Functional!

1. Grab some code
2. Make a new method
3. Use it in multiple places

**Inside-Out**: Pull it out into a method, put the method in its place.

**Outside-In**: Pull out the code that surrounds a block of code, pass the "inside-code" into the method.

> _The demo is wow, gotta get the demo code because it's a lot. Outside-In is great for standardizing your common try-catch blocks and your common using blocks. Inside-Out is the classic refactoring which helps code reuse on a rudimentary level._

### `Maybe`s and `Option`s and "Discriminated Unions"

Result class that has a status of "succeeded" and a status of "failed". All result is something that can contain a `<T>`, which can either be a failure or a result. Now you can do pattern matching on the result instead of `catch`es everywhere, EVERYWHERE.

```cs
static class Result
{
    interface IResult<T> { /* ... */ }

    class FailResult<T> : IResult<T> { /* ... */ }
    class SuccessResult<T> : IResult<T> { /* ... */ }

    public static Fail<T>(idk idk)
    {
        return new FailResult<T>(idk);
    }

    // other overloads of Fail...

    public static Success<T>(T value)
        => new SuccessResult<T>(value);
}
```

After a few abstractions...

```cs
    private static IResult<Guid> BillTill(TollEvent tollEvent)
        => tollEvent.Start()
            .IfNotFailed(GetVehicleRegistration)
            .IfNotFailed(prev => GetVehicle(prev, tollEvent))
            .IfNotFailed(prev => CalculateToll(prev, tollEvent))
            .IfNotFailed(BillingSystem.SendBill)
            .ReportFailure();

    private static IResult<object> GetVehicleRegistration(ISuccessResult<TollEvent> tollEventResult)
        => tollEventResult.Value.LicensePlate.LookFor<string, object>()
            .IfNotFound(CheckForCarRegistrations)
            .IfNotFound(CheckForTruckRegistrations)
            .IfNotFound(CheckForBoatRegistrations)
            .SomethingSomethingResult()
```

Something to note: a result class is a great return-type for functions that might have ambiguous/failable/nullable results. There's no reason to wrap `int Return42() => 42;` in a `Result.Success<int>(42)`

Closing notes: If you pass exceptions/failures as data, then you can generalize and cross boundaries, decoupling your code from a specific service or technology or platform.

## References

- Functional Programmikng in C#: How to write better C# code
- Pluralsight: Applying Functional Principles in C#
- Pluralsight: Functional Programming with C#
