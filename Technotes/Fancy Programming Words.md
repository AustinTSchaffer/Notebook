---
tags: Programming
---

# Fancy Programming Words

- idempotent
    - "idem" is Latin for "the same".
    - Means that an operation will have the same result even when applied multiple times.
    - `1 * 1` = `1 * 1 * 1` = `1 * 1 * 1 * 1`, idempotent
    - `2 * 2 = 4` but `2 * 2 * 2 = 8`, not idempotent
    - Pushing a crosswalk button multiple times doesn't speed up the signal change. Idempotent.
    - Adding to a list is **not** idempotent. Adding to a set **is** idempotent.
    - HTTP methods `GET`, `PUSH`, and `DELETE` should always be idempotent.
- ephemeral
    - from the Greek, "ephemeros", meaning lasting only a day
    - in programming, antonym of persistent, and maybe immutable
    - RAM is ephemeral, mutable objects in memory are ephemeral
    - Ephemeral architecture is better for DevOps, because you can just redeploy if something bad happens
    - Server-less architecture is ephemeral
- immutable
    - cannot be changed
- anonymous
    - doesn't have a name
    - effectively an ephemeral version of X, where X is a class/method/function
- predicate
    - a function that returns a single boolean value
    - often predicate functions start with the word `is`
- memoization
    - cache the return value of a function, given some input
    - JS/TS has `useMemo`, which sets up EZ-one-click memoization
    - Python has the `functools.lru_cache` decorator, which does the same thing
    - commonly used for recursive functions
- abstraction
    - make something solve more problems by hiding implementation details from the end user
    - this is essentially the fancy word that's synonymous with Don't Repeat Yourself (DRY)
- serialization
    - process of converting program data to a common format that can be read by other programs
