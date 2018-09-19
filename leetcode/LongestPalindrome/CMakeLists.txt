cmake_minimum_required(VERSION 3.6)
project(LongestPalindrome)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp)
set(CMAKE_BUILD_TYPE debug)
add_executable(LongestPalindrome ${SOURCE_FILES})