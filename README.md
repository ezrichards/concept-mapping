# Abstraction Based Learning

The question we're trying to answer: how do you know what you don't know?
More specifically, How do you know what to study and where to improve?

Abstraction-based learning is a concept I propose which answers these
questions. In *any* discipline, there are abstractions that need to be
made in the learning process.

When I learn, I sometimes find it hard to think about and fully
understand a topic without seeing the larger picture and/or the 
real-world application of the topic.

This project provides a framework for defining abstractions
of disciplines as abstractions and key ideas, as well
as a visualizer (see *Abstraction Mapping*) for both students 
and teachers to explore and visualize topics.

## Terminology

**Feature**: In the context of this project, a Feature is defined
to be the most generalized form of an idea or topic. For instance,
"Conditionals" are the most basic form of many child ideas, such
as if, else if, and else statements.

## Abstraction Mapping

An abstraction mapping is a visual representation of all
levels of abstraction in a discipline, which highlights key ideas
but can be "zoomed in" to focus on details.

### Mapping Predicates

Throughout each mapping, there are predicates. These
predicates vary from disciplines, but all abstraction mappings
should have `ofFeature` and `hasRelation` predicates.

**ofFeature** describes a relation to a key idea or completely
generalized topic. For instance, in a Python program, "if statement"
is `ofFeature` Conditionals.

**hasRelation** describes an important relation (abstraction) to
another topic.

## Roadmap
- Add tree view support
- Add graph view support
- Figure out best RDF storage + query libraries
- Student end: checkmark certain things that need to be studied, and other things that have been finished.
- Teacher creation of abstraction predicates (i.e. math theorems)
- Add real-world applications relations (grayed out, but can be toggled for highlight)
- Dijkstra's or other least-search algorithm: what do you have to understand to understand an entire Feature?
- Toggleable "Feature" display: toggle whether or not the mapping goes "towards" Features or "away" from Features
