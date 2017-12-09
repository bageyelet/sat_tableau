# sat_tableau
A very naive implementation of Smullyan's Tableau for satisfiability in Propositional Logic

Example of usage:
```
> not ((a or b) -> (b or a))
> UNSAT
```

**NOTE**: the parser is naive, use parenthesis! It's right-associative: `not a -> b` is interpreted as `not (a -> b)`
