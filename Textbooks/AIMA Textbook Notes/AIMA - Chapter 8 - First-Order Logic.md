---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 8 - First-Order Logic

## Chapter Summary

- Knowledge representation languages should be declarative, compositional, expressive, context independent, and unambiguous.  
- Logics differ in their ontological commitments and epistemological commitments. While propositional logic commits only to the existence of facts, first-order logic commits to the existence of objects and relations and thereby gains expressive power, appropriate for domains such as the wumpus world and electronic circuits.
- Both propositional logic and first-order logic share a difficulty in representing vague propositions. This difficulty limits their applicability in domains that require personal judgments, like politics or cuisine.  
- The syntax of first-order logic builds on that of propositional logic. It adds terms to represent objects, and has universal and existential quantifiers to construct assertions about all or some of the possible values of the quantified variables.
- A possible world, or model, for first-order logic includes a set of objects and an interpretation that maps constant symbols to objects, predicate symbols to relations among objects, and function symbols to functions on objects.  
- An atomic sentence is true only when the relation named by the predicate holds between the objects named by the terms. Extended interpretations, which map quantifier variables to objects in the model, define the truth of quantified sentences. Developing a knowledge base in first-order logic requires a careful process of analyzing the domain, choosing a vocabulary, and encoding the axioms required to support the desired inferences.