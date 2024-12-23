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
include CMakeFiles/tlstest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/tlstest.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/tlstest.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/tlstest.dir/flags.make

CMakeFiles/tlstest.dir/tests/tlstest.c.o: CMakeFiles/tlstest.dir/flags.make
CMakeFiles/tlstest.dir/tests/tlstest.c.o: /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/tlstest.c
CMakeFiles/tlstest.dir/tests/tlstest.c.o: CMakeFiles/tlstest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/tlstest.dir/tests/tlstest.c.o"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/tlstest.dir/tests/tlstest.c.o -MF CMakeFiles/tlstest.dir/tests/tlstest.c.o.d -o CMakeFiles/tlstest.dir/tests/tlstest.c.o -c /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/tlstest.c

CMakeFiles/tlstest.dir/tests/tlstest.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/tlstest.dir/tests/tlstest.c.i"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/tlstest.c > CMakeFiles/tlstest.dir/tests/tlstest.c.i

CMakeFiles/tlstest.dir/tests/tlstest.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/tlstest.dir/tests/tlstest.c.s"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/tlstest.c -o CMakeFiles/tlstest.dir/tests/tlstest.c.s

# Object files for target tlstest
tlstest_OBJECTS = \
"CMakeFiles/tlstest.dir/tests/tlstest.c.o"

# External object files for target tlstest
tlstest_EXTERNAL_OBJECTS =

bin/tlstest: CMakeFiles/tlstest.dir/tests/tlstest.c.o
bin/tlstest: CMakeFiles/tlstest.dir/build.make
bin/tlstest: bin/libgmssl.a
bin/tlstest: CMakeFiles/tlstest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable bin/tlstest"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tlstest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/tlstest.dir/build: bin/tlstest
.PHONY : CMakeFiles/tlstest.dir/build

CMakeFiles/tlstest.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/tlstest.dir/cmake_clean.cmake
.PHONY : CMakeFiles/tlstest.dir/clean

CMakeFiles/tlstest.dir/depend:
	cd /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles/tlstest.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/tlstest.dir/depend

