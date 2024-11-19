cmake_minimum_required(VERSION 3.29)
project(TP1_Agenda)

set(CMAKE_CXX_STANDARD 20)

add_executable(TP1_Agenda main.cpp
        Entree.cpp
        Entree.h
        Tableau.cpp
        Tableau.h
        Agenda.cpp
        Agenda.h
)
