project(PackageTest CXX)
cmake_minimum_required(VERSION 3.7)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# threads
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

add_executable(example main.cpp)
target_link_libraries(example ${CONAN_LIBS} Threads::Threads)