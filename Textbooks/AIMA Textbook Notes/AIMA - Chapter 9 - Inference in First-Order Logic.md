---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 9 - Inference in First-Order Logic

## Chapter Summary
- A first approach uses inference rules (universal instantiation and existential instantiation) to propositionalize the inference problem. Typically, this approach is slow, unless the domain is small.  
- The use of unification to identify appropriate substitutions for variables eliminates the instantiation step in first-order proofs, making the process more efficient in many cases. A lifted version of Modus Ponens uses unification to provide a natural and powerful inference rule, generalized Modus Ponens. The forward-chaining and backward- chaining algorithms apply this rule to sets of definite clauses.  
- Generalized Modus Ponens is complete for definite clauses, although the entailment problem is semidecidable. For Datalog knowledge bases consisting of function-free definite clauses, entailment is decidable.  
- Forward chaining is used in deductive databases, where it can be combined with relational database operations. It is also used in production systems, which perform efficient updates with very large rule sets. Forward chaining is complete for Datalog and runs in polynomial time.  
- Backward chaining is used in logic programming systems, which employ sophisticated compiler technology to provide very fast inference. Backward chaining suffers from redundant inferences and infinite loops; these can be alleviated by memoization. Prolog, unlike first-order logic, uses a closed world with the unique names assumption and negation as failure. These make Prolog a more practical programming language, but bring it further from pure logic.  
- The generalized resolution inference rule provides a complete proof system for first- order logic, using knowledge bases in conjunctive normal form.  
- Several strategies exist for reducing the search space of a resolution system without compromising completeness. One of the most important issues is dealing with equality; we showed how demodulation and paramodulation can be used.  
- Efficient resolution-based theorem provers have been used to prove interesting mathematical theorems and to verify and synthesize software and hardware.