cmake_minimum_required({min_cmake_version})

project({project_name})

set(CMAKE_CXX_STANDARD, {cxx_standard})

set(cmake_export_compile_commands on)

add_{project_type}({project_name} main.cpp)
