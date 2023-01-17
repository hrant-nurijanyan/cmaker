cmake_minimum_required({min_cmake_version})

project({project_name})

set(CMAKE_CXX_STANDARD, {cxx_standard})

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_{project_type}({project_name} main.cpp)
