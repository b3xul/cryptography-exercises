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
include CMakeFiles/rsa_sign_verify.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/rsa_sign_verify.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/rsa_sign_verify.dir/flags.make

CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.o: CMakeFiles/rsa_sign_verify.dir/flags.make
CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.o: ../AY2021/OpenSSL/asymmetric/rsa_sign_verify.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.o -c /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c

CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c > CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.i

CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c -o CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.s

# Object files for target rsa_sign_verify
rsa_sign_verify_OBJECTS = \
"CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.o"

# External object files for target rsa_sign_verify
rsa_sign_verify_EXTERNAL_OBJECTS =

rsa_sign_verify: CMakeFiles/rsa_sign_verify.dir/AY2021/OpenSSL/asymmetric/rsa_sign_verify.c.o
rsa_sign_verify: CMakeFiles/rsa_sign_verify.dir/build.make
rsa_sign_verify: CMakeFiles/rsa_sign_verify.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable rsa_sign_verify"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rsa_sign_verify.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/rsa_sign_verify.dir/build: rsa_sign_verify
.PHONY : CMakeFiles/rsa_sign_verify.dir/build

CMakeFiles/rsa_sign_verify.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/rsa_sign_verify.dir/cmake_clean.cmake
.PHONY : CMakeFiles/rsa_sign_verify.dir/clean

CMakeFiles/rsa_sign_verify.dir/depend:
	cd /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug /mnt/26158F5879578F52/Università/Magistrale/Cryptography/Attacks/cryptography-exercises/my_programs/cmake-build-debug/CMakeFiles/rsa_sign_verify.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/rsa_sign_verify.dir/depend

