cmake_minimum_required(VERSION 3.29)
project(Prog_Av)

set(CMAKE_CXX_STANDARD 20)

add_executable(Prog_Av main.cpp
        Livre.h
        Livre.cpp
        Biblio.h
        Biblio.cpp
)
