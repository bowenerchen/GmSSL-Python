# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.27.9/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.27.9/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl

# Include any dependencies generated for this target.
include CMakeFiles/ectest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/ectest.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/ectest.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/ectest.dir/flags.make

CMakeFiles/ectest.dir/tests/ectest.c.o: CMakeFiles/ectest.dir/flags.make
CMakeFiles/ectest.dir/tests/ectest.c.o: /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/ectest.c
CMakeFiles/ectest.dir/tests/ectest.c.o: CMakeFiles/ectest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/ectest.dir/tests/ectest.c.o"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/ectest.dir/tests/ectest.c.o -MF CMakeFiles/ectest.dir/tests/ectest.c.o.d -o CMakeFiles/ectest.dir/tests/ectest.c.o -c /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/ectest.c

CMakeFiles/ectest.dir/tests/ectest.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/ectest.dir/tests/ectest.c.i"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/ectest.c > CMakeFiles/ectest.dir/tests/ectest.c.i

CMakeFiles/ectest.dir/tests/ectest.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/ectest.dir/tests/ectest.c.s"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/ectest.c -o CMakeFiles/ectest.dir/tests/ectest.c.s

# Object files for target ectest
ectest_OBJECTS = \
"CMakeFiles/ectest.dir/tests/ectest.c.o"

# External object files for target ectest
ectest_EXTERNAL_OBJECTS =

bin/ectest: CMakeFiles/ectest.dir/tests/ectest.c.o
bin/ectest: CMakeFiles/ectest.dir/build.make
bin/ectest: bin/libgmssl.a
bin/ectest: CMakeFiles/ectest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable bin/ectest"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ectest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/ectest.dir/build: bin/ectest
.PHONY : CMakeFiles/ectest.dir/build

CMakeFiles/ectest.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ectest.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ectest.dir/clean

CMakeFiles/ectest.dir/depend:
	cd /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles/ectest.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/ectest.dir/depend
