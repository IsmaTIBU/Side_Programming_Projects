cmake_minimum_required(VERSION 3.29)
project(TP2_Agenda)

set(CMAKE_CXX_STANDARD 20)

add_executable(TP2_Agenda main.cpp
        Tableau.cpp
        Tableau.h
        Entree.cpp
        Entree.h
        Agenda.cpp
        Agenda.h)
