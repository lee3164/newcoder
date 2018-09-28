cmake_minimum_required(VERSION 3.5)
project(ThreeSum)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp)
set(CMAKE_BUILD_TYPE DEBUG)
add_executable(ThreeSum ${SOURCE_FILES})