cmake_minimum_required(VERSION 3.29)
project(TP4_Virtualite_Polymorphisme)

set(CMAKE_CXX_STANDARD 20)

add_executable(TP4_Virtualite_Polymorphisme main.cpp
        Biblio.cpp
        Biblio.h
        Document.cpp
        Document.h
        Livre.cpp
        Livre.h
        Article.cpp
        Article.h)
