cmake_minimum_required({min_cmake_version})

project({project_name})

set(CMAKE_CXX_STANDARD, {cxx_standard})

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_{project_type}({project_name} main.cpp)

set(EXT_DEPS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/extDeps)

# Configuring glfw and glad
set(GLFW_DIR ${EXT_DEPS_DIR}/glfw-3.3.8)
set(GLAD_DIR ${EXT_DEPS_DIR}/glad)
add_subdirectory(${GLFW_DIR})
add_subdirectory(${GLAD_DIR})
find_package(OpenGL REQUIRED)
target_link_libraries({project_name} PRIVATE glfw OpenGL::GL glad)
target_include_directories({project_name} PRIVATE ${GLFW_DIR}/include ${GLAD_DIR}/include)




