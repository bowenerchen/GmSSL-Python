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
include CMakeFiles/pemtest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/pemtest.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/pemtest.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/pemtest.dir/flags.make

CMakeFiles/pemtest.dir/tests/pemtest.c.o: CMakeFiles/pemtest.dir/flags.make
CMakeFiles/pemtest.dir/tests/pemtest.c.o: /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/pemtest.c
CMakeFiles/pemtest.dir/tests/pemtest.c.o: CMakeFiles/pemtest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/pemtest.dir/tests/pemtest.c.o"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/pemtest.dir/tests/pemtest.c.o -MF CMakeFiles/pemtest.dir/tests/pemtest.c.o.d -o CMakeFiles/pemtest.dir/tests/pemtest.c.o -c /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/pemtest.c

CMakeFiles/pemtest.dir/tests/pemtest.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/pemtest.dir/tests/pemtest.c.i"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/pemtest.c > CMakeFiles/pemtest.dir/tests/pemtest.c.i

CMakeFiles/pemtest.dir/tests/pemtest.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/pemtest.dir/tests/pemtest.c.s"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/pemtest.c -o CMakeFiles/pemtest.dir/tests/pemtest.c.s

# Object files for target pemtest
pemtest_OBJECTS = \
"CMakeFiles/pemtest.dir/tests/pemtest.c.o"

# External object files for target pemtest
pemtest_EXTERNAL_OBJECTS =

bin/pemtest: CMakeFiles/pemtest.dir/tests/pemtest.c.o
bin/pemtest: CMakeFiles/pemtest.dir/build.make
bin/pemtest: bin/libgmssl.a
bin/pemtest: CMakeFiles/pemtest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable bin/pemtest"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pemtest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/pemtest.dir/build: bin/pemtest
.PHONY : CMakeFiles/pemtest.dir/build

CMakeFiles/pemtest.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/pemtest.dir/cmake_clean.cmake
.PHONY : CMakeFiles/pemtest.dir/clean

CMakeFiles/pemtest.dir/depend:
	cd /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles/pemtest.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/pemtest.dir/depend

