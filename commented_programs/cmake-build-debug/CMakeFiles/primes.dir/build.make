# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.20

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
CMAKE_COMMAND = /opt/clion-2021.1.3/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /opt/clion-2021.1.3/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/primes.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/primes.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/primes.dir/flags.make

CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.o: CMakeFiles/primes.dir/flags.make
CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.o: ../AY2021/OpenSSL/bignum/primes.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.o -c /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/AY2021/OpenSSL/bignum/primes.c

CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/AY2021/OpenSSL/bignum/primes.c > CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.i

CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/AY2021/OpenSSL/bignum/primes.c -o CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.s

# Object files for target primes
primes_OBJECTS = \
"CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.o"

# External object files for target primes
primes_EXTERNAL_OBJECTS =

primes: CMakeFiles/primes.dir/AY2021/OpenSSL/bignum/primes.c.o
primes: CMakeFiles/primes.dir/build.make
primes: CMakeFiles/primes.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable primes"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/primes.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/primes.dir/build: primes
.PHONY : CMakeFiles/primes.dir/build

CMakeFiles/primes.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/primes.dir/cmake_clean.cmake
.PHONY : CMakeFiles/primes.dir/clean

CMakeFiles/primes.dir/depend:
	cd /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug/CMakeFiles/primes.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/primes.dir/depend

