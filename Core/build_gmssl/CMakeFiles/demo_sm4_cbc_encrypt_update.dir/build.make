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
include CMakeFiles/demo_sm4_cbc_encrypt_update.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/demo_sm4_cbc_encrypt_update.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/demo_sm4_cbc_encrypt_update.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/demo_sm4_cbc_encrypt_update.dir/flags.make

CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o: CMakeFiles/demo_sm4_cbc_encrypt_update.dir/flags.make
CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o: /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/demos/src/demo_sm4_cbc_encrypt_update.c
CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o: CMakeFiles/demo_sm4_cbc_encrypt_update.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o -MF CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o.d -o CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o -c /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/demos/src/demo_sm4_cbc_encrypt_update.c

CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.i"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/demos/src/demo_sm4_cbc_encrypt_update.c > CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.i

CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.s"
	/opt/homebrew/opt/llvm/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1/demos/src/demo_sm4_cbc_encrypt_update.c -o CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.s

# Object files for target demo_sm4_cbc_encrypt_update
demo_sm4_cbc_encrypt_update_OBJECTS = \
"CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o"

# External object files for target demo_sm4_cbc_encrypt_update
demo_sm4_cbc_encrypt_update_EXTERNAL_OBJECTS =

bin/demo_sm4_cbc_encrypt_update: CMakeFiles/demo_sm4_cbc_encrypt_update.dir/demos/src/demo_sm4_cbc_encrypt_update.c.o
bin/demo_sm4_cbc_encrypt_update: CMakeFiles/demo_sm4_cbc_encrypt_update.dir/build.make
bin/demo_sm4_cbc_encrypt_update: bin/libgmssl.a
bin/demo_sm4_cbc_encrypt_update: CMakeFiles/demo_sm4_cbc_encrypt_update.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable bin/demo_sm4_cbc_encrypt_update"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/demo_sm4_cbc_encrypt_update.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/demo_sm4_cbc_encrypt_update.dir/build: bin/demo_sm4_cbc_encrypt_update
.PHONY : CMakeFiles/demo_sm4_cbc_encrypt_update.dir/build

CMakeFiles/demo_sm4_cbc_encrypt_update.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/demo_sm4_cbc_encrypt_update.dir/cmake_clean.cmake
.PHONY : CMakeFiles/demo_sm4_cbc_encrypt_update.dir/clean

CMakeFiles/demo_sm4_cbc_encrypt_update.dir/depend:
	cd /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/GmSSL-3.1.1 /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl /Users/cyx/easy_gmssl/GmSSL-Python/Core/build_gmssl/CMakeFiles/demo_sm4_cbc_encrypt_update.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/demo_sm4_cbc_encrypt_update.dir/depend

