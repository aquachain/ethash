cmake_minimum_required(VERSION 2.8.7)
project(aquahash)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/modules/")
set(AQUAHASH_LIBS aquahash)

if (WIN32 AND WANT_CRYPTOPP)
	add_subdirectory(cryptopp)
endif()

add_subdirectory(src/libaquahash)

add_subdirectory(src/benchmark EXCLUDE_FROM_ALL)
add_subdirectory(test/c)
