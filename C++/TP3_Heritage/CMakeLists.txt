cmake_minimum_required(VERSION 3.29)
project(TP3_Heritage)

set(CMAKE_CXX_STANDARD 20)

add_executable(TP3_Heritage main.cpp
        Document.cpp
        Document.h
        Livre.cpp
        Livre.h
        Article.cpp
        Article.h)
