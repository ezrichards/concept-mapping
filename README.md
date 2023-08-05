# Concept Mapping

When I learn, I sometimes find it hard to think about and fully
understand a topic without seeing the larger picture and/or the 
real-world application of the topic.

This project has three main objectives which aim to solve that problem (and more!):

1. Provide a framework for defining abstractions and key ideas in
a curriculum.

2. Provide a visualization for students to see what they need
to study and what connections they should make between concepts.

3. Provide a framework and visualization to assist
educators in structuring and teaching curricula.

## The Framework

In any discipline, there are abstractions that need to be made in
the learning process. For instance, when learning the Python
programming language, learners are often asked to learn that `print()`
prints to the terminal before learning what functions do. 
These concepts are eventually built upon, thus building many
layers of abstraction.

**Feature**: In the context of this project, a Feature is defined
to be the most generalized form of an idea or topic. For instance,
"Conditionals" are the most basic form of many child ideas, such
as if, else if, and else statements.

**Abstraction Mapping**: An abstraction mapping is a visual representation of all
*Features* in a discipline, which highlights key ideas but can be "zoomed in" to 
focus on details.

### Feature Relations

**ofFeature** describes a relation to a key idea or completely
generalized topic. For instance, in a Python program, "if statement"
is `ofFeature` Conditionals.

**hasRelation** describes an important relation (abstraction) to
another topic.

## Roadmap
- Add graph view support
- Figure out best RDF storage + query libraries
- Student end: checkmark certain things that need to be studied, and other things that have been finished.
- Teacher creation of abstraction predicates (i.e. math theorems)
- Add real-world applications relations (grayed out, but can be toggled for highlight)
- Dijkstra's or other least-search algorithm: what do you have to understand to understand an entire Feature?
- Toggleable "Feature" display: toggle whether or not the mapping goes "towards" Features or "away" from Features
- "Abstraction maps": saveable to png and viewable on web
