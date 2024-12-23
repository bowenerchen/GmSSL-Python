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
include CMakeFiles/gcmtest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/gcmtest.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/gcmtest.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/gcmtest.dir/flags.make

CMakeFiles/gcmtest.dir/tests/gcmtest.c.o: CMakeFiles/gcmtest.dir/flags.make
CMakeFiles/gcmtest.dir/tests/gcmtest.c.o: /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/gcmtest.c
CMakeFiles/gcmtest.dir/tests/gcmtest.c.o: CMakeFiles/gcmtest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/gcmtest.dir/tests/gcmtest.c.o"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/gcmtest.dir/tests/gcmtest.c.o -MF CMakeFiles/gcmtest.dir/tests/gcmtest.c.o.d -o CMakeFiles/gcmtest.dir/tests/gcmtest.c.o -c /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/gcmtest.c

CMakeFiles/gcmtest.dir/tests/gcmtest.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/gcmtest.dir/tests/gcmtest.c.i"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/gcmtest.c > CMakeFiles/gcmtest.dir/tests/gcmtest.c.i

CMakeFiles/gcmtest.dir/tests/gcmtest.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/gcmtest.dir/tests/gcmtest.c.s"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/tests/gcmtest.c -o CMakeFiles/gcmtest.dir/tests/gcmtest.c.s

# Object files for target gcmtest
gcmtest_OBJECTS = \
"CMakeFiles/gcmtest.dir/tests/gcmtest.c.o"

# External object files for target gcmtest
gcmtest_EXTERNAL_OBJECTS =

bin/gcmtest: CMakeFiles/gcmtest.dir/tests/gcmtest.c.o
bin/gcmtest: CMakeFiles/gcmtest.dir/build.make
bin/gcmtest: bin/libgmssl.a
bin/gcmtest: CMakeFiles/gcmtest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable bin/gcmtest"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gcmtest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/gcmtest.dir/build: bin/gcmtest
.PHONY : CMakeFiles/gcmtest.dir/build

CMakeFiles/gcmtest.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/gcmtest.dir/cmake_clean.cmake
.PHONY : CMakeFiles/gcmtest.dir/clean

CMakeFiles/gcmtest.dir/depend:
	cd /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles/gcmtest.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/gcmtest.dir/depend

