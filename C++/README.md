# Practical Assignments in Object-Oriented Programming (C++)

This repository contains practical assignments from coursework focused on developing proficiency in object-oriented programming (OOP) concepts using C++. Each practical session explores key programming principles through structured tasks and implementations.

## Contents

### TP1 - Agenda Management
The goal was to design a program for managing an agenda. This involved:
- Creating classes for entries (`Entree`) with a name and phone number.
- Implementing a dynamic array (`Tableau`) to store and manipulate entries, supporting addition, deletion, and display operations.
- Developing an agenda class (`Agenda`) that utilized the array and supported functionalities like concatenating agendas, adding, deleting, and displaying entries.

### TP2 - Agenda Operators
Building on TP1, this session introduced operator overloading to enhance the `Agenda` class. The operators implemented included:
- `<<` for displaying the agenda.
- `+=` to add entries or concatenate agendas.
- `[]` to find the first occurrence of a name.
- `-=` to delete all entries matching a name.
- `==` to compare two agendas.
- Other advanced functionalities, such as testing for names within an agenda or filtering entries by a starting letter.

### TP3 - Inheritance
This session introduced inheritance by extending base classes to create hierarchies. The tasks focused on:
- Abstracting common properties and behaviors into parent classes.
- Using derived classes to implement specific functionalities.
- Polymorphism to handle objects dynamically through base class references.

### TP4 - Polymorphism
Building on TP3, this practical focused on:
- Using polymorphic classes to dynamically manage diverse object types.
- Implementing abstract classes and virtual functions to provide a flexible and scalable architecture.
- Enhancing reusability and maintainability of the code through OOP principles.

## Purpose
These assignments collectively provide a strong foundation in C++ OOP concepts, with applications that simulate real-world scenarios, including data management, operator overloading, inheritance, and polymorphism. The repository serves as a reference and learning tool for students and professionals interested in mastering C++ programming techniques.
