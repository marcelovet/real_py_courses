# File Input and Output
# So far, you’ve written programs that get their input from one of two
# places: from the program itself or from the user. Program output has
# been limited to displaying some text in IDLE’s interactive window.
# These input and output methods are not useful in several common
# scenarios:
# • The input values are unknown while writing the program
# • The program requires more data than a user can be expected to
# type in by themselves
# • Output must be shared with other people after the program runs
# This is where files come in.
# In this chapter, you will learn how to:
# • Work with file paths and file metadata
# • How to read and write text files
# • How to read and write Comma-Separated Value (CSV) files
# • How to create, delete, copy, and move files and folders

# Files and the File System
# You have likely been working with computer files for a long time. Even
# so, there are some things that programmers need to know about files
# that the general user does not.
# In this section, you’ll learn the concepts necessary to get started working
# with files in Python.
# Note
# If you are familiar with concepts like the file system and file
# paths, may wish to read the Working With File Paths in Python
# and File Metadata sections before skipping to the next section.
# Let’s start by exploring what a file is and how computers interact with
# them.

# The Anatomy of a File
# There are a multitude of types of files out there: text files, image files,
# audio files, and PDF files, just to name a few. Ultimately, though, a
# file is just a sequence of bytes called the contents of the file.
# Each byte in a file can be thought of as an integer with a value between
# 0 and 255, including both endpoints. The bytes are the values that are
# stored on a physical storage device when a file is saved.
# When you access a file on a computer, the contents of the file are read
# from the disk in the correct sequence of bytes. The important thing to
# know here is that there is nothing intrinsic to the file itself that dictates
# how to interpret the contents.
# As a programmer, it’s your job to properly interpret the contents when
# you open a file. This might sound difficult, but Python does a lot of the
# hard work for you.
# For example, when you open a text file, Python can convert the numerical
# bytes of the file into text characters for you. You do not need to
# know the specifics of how this conversion happens. There are tools in
# the standard library for working with all sorts of file types, including
# images and audio files.
# In order to access a file from a storage device, a whole host of things
# need to happen. You need to know on which device the file is stored,
# how to interact with that device, and where exactly on the device the
# file is located.
# This monumental task is managed by a file system. Python interacts
# with the file system on your computer in order to read, write, and manipulate
# files.

# The File System
# The file system on a computer does two things:
# 1. It provides an abstract representation of the files stored on your
# computer and devices connected to it.
# 2. It interfaces with devices to control storage and retrieval file data.
# Python interacts with the file system on your computer, so you can
# only do in Python whatever your file system allows.
# Important
# Different operating systems use different file systems. This is
# very important to keep in mind when writing code that will be
# run on different operating systems.
# The file system itself manages communication between the computer
# and the physical storage device, so the only part of the file system you
# need to understand as a programmer is how it represents files.

# The File System Hierarchy
# File systems organize files in a hierarchy of directories, which are
# also known as folders. At the top of the hierarchy is a directory called
# the root directory. All other files and directories in the file system
# are contained in the root directory.
# Each file in directory has a file name that must be unique from any
# other file in the same directory. Directories can also contain other
# directories, called subdirectories or subfolders.
# The following directory tree visualizes the hierarchy of files and
# directories in an example file system:
# root/
# |
# |
# | --- app/
# |     |
# |     --- program.py
# |     |
# |     --- data.txt
# | --- photos/
#       |
#       | --- cats/
#       |     | --- lion.jpg
#       |     | --- siamese.jpg
#       | --- dogs/
#             | --- dachshound.jpg
#             | --- jack_russel.jpg
# In this file system, the root folder is called root/.
# It has two subdirectories:
# app/ and photos/. The app/ subdirectory contains a program.py file
# and a data.txt file. The photos/ directory also has two subdirectories,
# cats/ and dogs/, that both contains two image files.

# File Paths
# To locate a file in a file system, you can list the directories in order,
# starting with the root directory, followed by the name of the file.
# string with the file location represented in this manner is called a file
# path.
# For example, the file path for the jack_russel.gif file in the above file
# system is root/photos/dogs/jack_russel.gif.
# How you write file paths depends on your operating system. Here are
# three examples of file paths on Windows, macOS, and Linux:
# 1. Windows: C:\Users\David\Documents\hello.txt
# 2. macOS: /Users/David/Documents/hello.txt
# 3. Ubuntu Linux: /home/David/Documents/hello.txt
# All three of these file paths locate a text file named hello.txt that is
# stored in the Documents subfolder of the user directory for a user named
# David. As you can see, there are some pretty big differences between
# file paths from one operating system to another.
# On macOS and Ubuntu Linux, the operating system uses a virtual
# file system that organizes all files and directories for all devices on
# the system under a single root directory, usually represented by a forward
# slash symbol (/). Files and folders from external storage devices
# are usually located in a subdirectory called media/.
# In Windows, there is no universal root directory. Each device has a
# separate file system with a unique root directory that is named with
# a drive letter followed by a colon (:) and a back slash symbol (\).
# Typically, the hard drive where the operating system is installed is
# assigned the letter C, so the root directory of the file system for that
# drive is C:.
# The other major difference between Windows, macOS, and Ubuntu
# files paths is that directories in a Windows file path are separated by
# back slashes (\), whereas directories in macOS and Ubuntu file paths
# are separated by forward slashes (/).
# When you write programs that need to run on multiple operating systems,
# it is critical that you handle the differences in file paths apprpriately.
# In versions of Python greater than 3.4, the standard library
# contains a module called pathlib helps take the pain out of handling
# file paths across operating systems.
# Read on to learn how to use pathlib to work with file paths in Python.

import csv
import pathlib
# Working With File Paths in Python
# To work with file paths in Python, use the standard libraries pathlib
# module. You’ll need to import the module before you can do anything
# with it.
# >>> import pathlib
# The pathlib module contains a class called Path that is used to represent a
# file path.
import shutil

# Creating Path Objects
# There are several ways to create a new Path object:
# 1. From a string
# 2. With Path.home() and Path.cwd() class methods
# 3. With the / operator
# The most straightforward way to create a Path object is from a string.
# Creating Path Objects from Strings
# For instance, the following creates a Path object representing the
# macOS file path "/Users/David/Documents/hello.txt":
path = pathlib.Path("/Users/David/Documents/hello.txt")
# There’s problem, though, with Windows paths. On Windows, directories are
# separated by back slashes \. Python interprets back slashes as
# the start of an escape sequence that represent a special character in
# the string, such as the newline character (\n).
# Attempting to create a Path object with the Windows file path
# "C:\Users\David\Desktop\hello.txt" raises an exception:
# >>> path = pathlib.Path("C:\Users\David\Desktop\hello.txt")
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
# in position 2-3: truncated \UXXXXXXXX escape
# There are two ways to get around this problem:
# You can use a forward slash (/) instead of a back slash (\) in your
# Windows file paths
path = pathlib.Path("C:/Users/David/Desktop/hello.txt")
# Python can interpret this just fine and will translate the path appropriately
# and automatically when interfacing with the Windows operating
# system.
# You can also turn the string into a raw string by prefixing it with an r:
path = pathlib.Path(r"C:\Users\David\Desktop\hello.txt")
# This tells Python to ignore any escape sequences and just read the
# string as-is.

# Path.home() and Path.cwd()
# Besides creating a Path object from a string, the Path class has class
# methods that return Path objects of special directories. Two of the
# most useful class methods are Path.home() and Path.cwd().
# Every operating system has a special directory for storing data for the
# currently logged in user. This directory is called the user’s home directory.
# The location of this directory depends on the operating system:
# • Windows: C:\Users\<username>
# • macOS: /Users/<username>
# • Ubuntu Linux: /home/<username>
# The Path.home() class method creates a Path object representing the
# home directory regardless of which operating system the code runs
# on:
home = pathlib.Path.home()
print(home, type(home))
# The Path object created is a subclass of Path called WindowsPath. On
# other operating systems, the Path object returned is a subclass called
# PosixPath.
# For example, on macOS, inspecting home will display something like
# the following:
# >>> home
# PosixPath("/Users/David")
# For the rest of this section, WindowsPath objects will be shown in the
# example output. However, all of the examples will work with PosixPath
# objects.
# WindowsPath and PosixPath objects share the same methods and
# attributes. From a programming standpoint, there is no difference
# between the two types of Path objects.
# The Path.cwd() class method returns a Path object representing the
# current working directory, or CWD. The current working directory is a dynamic
# reference to a directory that depends on where a
# process on the computer is currently working.
# When you run IDLE, the current working directory is usually set to
# the Documents directory in the current user’s home directory:
print(pathlib.Path.cwd())
# This is not always the case, though. Moreover, the current working
# directory may change during the lifetime of a program.
# Path.cwd() is useful, but be careful when you use it. When you do,
# make sure you know that the current working directory refers the directory
# that you expect it to.

# Using the / Operator
# If you have an existing Path object, you can use the / operator to extend
# the path with subdirectories or file names.
# For example, the following creates a Path object representing a file
# named hello.txt in the Documents subdirectory of the current user’s
# home directory:
print(home / "Desktop" / "hello.txt")
# The / operator must always have a Path object on the left hand side.
# The right hand side can have either string representing a single file or
# directory, or a string representing a path, or another Path object.

# Absolute vs. Relative Paths
# A path that begins with the root directory in a file system is called an
# absolute рle path. Not all file paths are absolute. A file path that is
# not absolute is called a relative file path.
# Here’s an example of a Path object that references a relative path:
# >>> # Relative Windows path
path = pathlib.Path(r"Photos\image.jpg")
# >>> # Relative macOS or Linux path
# >>> path = pathlib.Path("Photos/image.jpg")
# Notice that the path string does not start with C:\ on Windows, or /
# on macOS and Linux.
# You can check whether or not a file path is absolute using the .is_-
# absolute() method:
print(path.is_absolute())
# Relative paths only make sense when considered within the context
# of some other directory. They are perhaps most commonly used to
# describe the path to a file relative to the current working directory, or
# the user’s home directory.
# You can extend a relative path to an absolute path using the forward
# slash (/) operator:
# >>> home = pathlib.Path.home()
# WindowsPath('C:/Users/David')
print(home / pathlib.Path(r"Photos\image.png"))
# On the left of the forward slash (/), put an absolute path to the directory
# that contains the relative path. Then put the relative path on the
# right side of the forward slash.
# Once you create a Path object, you can inspect the various components
# of the file path that it refers to.

# Accessing File Path Components
# All file paths contain a list of directories. The .parents attribute of a
# Path object returns an iterable containing the list of directories in the
# file path:
path = pathlib.Path.home() / "hello.txt"
print(path)
print(list(path.parents))
print(list(path.parents)[::-1])

# Notice that the list of the directories are returned in reverse order
# from how they appear in the file path. That is, the last directory in
# the path is the first directory in the list of parent directories.
# You can iterate over the parent directories in a for loop:
for directory in path.parents:
    print(directory)
# The .parent attribute returns the name of the first parent directory in
# the file path as a string:
print(path.parent)
# If the file path is absolute, you can access the root directory of the file
# path with the .anchor attribute:
print(path.anchor)
# Note that .anchor returns a string, and not another Path object.
# For relative paths, .anchor return an empty string:
path = pathlib.Path('hello.txt')
print(path.anchor)
# The .name attribute returns the name of the file or directory that the
# path points to:
print(home.name)
path = home / 'hello.txt'
print(path.name)
# The name of a file is broken down into two parts. The part to the left
# of the dot (.) is called the stem, and the part to the right of the dot (.)
# is called the suffix or file extension.
# The .stem and .suffix attributes return strings containing each of these
# parts of the file name:
print(path.stem)
print(path.suffix)
# You might be wondering at this point how to actually do something
# with the hello.txt file. You’ll learn how to read and write files in the
# next section. But before you open a file for reading, it might be a good
# idea to know whether or not that file exists.

# Checking Whether Or Not a File Path Exists
# You can create a Path object for a file path even if that path doesn’t
# actually exist. Of course, file paths that don’t represent actual files
# or directories aren’t very useful, unless you plan on creating them at
# some point.
# Path objects have an .exists() method that returns True or False depending
# on whether or not the file path exists on the machine executing the program.
# For instance, if you don’t have a hello.txt file in your home directory,
# then the .exists() method on the Path object representing that file path
# returns False:
print(path)
print(path.exists())
# Using a text editor, or some other means, create a blank text file called
# hello.txt in your home directory. Then re-run the code from above,
# making sure path.exists returns True.
# You can check whether or not a file path refers to a file or a directory.
# To check if the path is a file, use the .is_file() method:
path = pathlib.Path.cwd() / 'real_python' / 'hello.txt'
print(path)
print(path.exists())
print(path.is_file())
# Note that if the file path refers to a file, but doesn’t exist, then .is_-
# file() returns False.
# Use the .is_dir() method to check if the file path refers to a directory
print(path.is_dir())
# Working with file paths is an essential part of any programming
# project that reads or writes data from a hard drive or other storage
# device. Understanding the differences between file paths on different
# operating systems and how to work with pathblib.Path objects so that
# your programs can work on any operating system is an important
# and useful skill.

# Common File System Operations
# Now that you have a good grasp on the file system and working with
# file paths using the pathlib module, let’s take a look at some common
# file operations and how you do them in Python.
# In this section, you’ll learn how to:
# • Create directories and files
# • Iterate over the contents of a directory
# • Search for files within a directory
# • Move and delete files and folders

# Creating Directories and Files
# To create a new directory, use the Path.mkdir() method.
proj_dir = pathlib.Path.cwd() / 'real_python'
new_dir = proj_dir / 'new_directory'
print(new_dir)
print(new_dir.exists())
new_dir.mkdir(exist_ok=True)
# After importing the Path class, you create a new path to a directory
# called new_directory/ in your home folder and assign this path to the
# new_dir variable. Then you use the .mkdir() method to create the new
# directory.
# You can now check that the new directory exists and is, in fact, a directory:
print(new_dir.exists())
print(new_dir.is_dir())
# If you try to create a directory that already exists, you get an error:
# >>> new_dir.mkdir()
# Traceback (most recent call last):
# File "<pyshell#32>", line 1, in <module>
# new_dir.mkdir()
# File "C:\Users\David\AppData\Local\Programs\Python\
# Python38-32\lib\pathlib.py", line 1266, in mkdir
# self._accessor.mkdir(self, mode)
# FileExistsError: [WinError 183] Cannot create a file when
# that file already exists: 'C:\\Users\\David\\new_directory'
# When you call the .mkdir() method, Python attempts to create the
# new_directory/ folder again. Since it already exists, this operation fails
# and a FileExistsError exception is raised.
# If you want to create a new directory if it doesn’t exists, but avoid
# raising the FileExistsError if it does, then you can set the options exist_ok
# parameter of the .mkdir() method to True:
# >>> new_dir.mkdir(exist_ok=True)
# When you execute .mkdir() with the exist_ok parameter set to True, the
# directory is created if it does not exist, or nothing happens if it does.
# Setting exist_ok to True when calling .mkdir()
# is equivalent to the following code:
# >>> if not new_dir.exists():
# ... new_dir.mkdir()
# Although the above code works just fine, setting the exist_ok parameter
# to True is shorter and doesn’t sacrifice readability.
# Now let’s see what happens if you try to create a subdirectory within
# a directory that does not exist:
nested_dir = new_dir / "folder_a" / "folder_b"
# >>> nested_dir.mkdir()
# Traceback (most recent call last):
# File "<pyshell#38>", line 1, in <module>
# nested_dir.mkdir()
# File "C:\Users\David\AppData\Local\Programs\Python\
# Python38-32\lib\pathlib.py", line 1266, in mkdir
# self._accessor.mkdir(self, mode)
# FileNotFoundError: [WinError 3] The system cannot findthe path
# specified: 'C:\\Users\\David\\new_directory\\folder_a\\folder_b'
# The problem is that the directory folder_a/ does not exist. Typically,
# to create a directory, all of the parent directories of the target directory
# folder_b/ in the path must already exist.
# To create any parent directories needed in order to create the target
# directory, set the optional parents parameter of .mkdir() to True:
# nested_dir.mkdir(parents=True)
# Now .mkdir() creates the parent directory folder_a/ so that the target
# directory folder_b/ can be created.
# By putting all of this together you get the following common pattern
# for creating directories:
# path.mkdir(parents=True, exist_ok=True)
nested_dir.mkdir(parents=True, exist_ok=True)
# By setting both the parents and exist_ok parameters to True, the entire
# path is created, if needed, and no exception is raised if the path already
# exists.
# This pattern is useful, but it may not always be what you want. For
# example, if the path is input by a user, you may wish to instead catch
# an exception so that you can ask the user to verify that the path they
# entered is correct. They might have just mistyped a directory name!
# Now let’s look at how to create files. Create a new Path object called
# file_path for the path new_directory/file1.txt:
file_path = new_dir / 'file1.txt'
# There is no file in new_directory/ called file1.txt, so the path doesn’t
# exist yet:
print(file_path.exists())
# You can create the file using the Path.touch() method:
file_path.touch()
# This creates a new file called file1.txt in the new_directory/ folder. It
# doesn’t contain any data yet, but the file exists:
print(file_path.exists())
print(file_path.is_file())
# Unlike .mkdir(), the .touch() method does not raise an exception if the
# path being created already exists:
file_path.touch()
# When you create a file using .touch(), the file does not contain any data.
# You will learn how to write data to a file in Section 11.4: Reading and
# Writing Files.
# You can’t create a file in a directory that doesn’t exist:
file_path = new_dir / "folder_c" / "file2.txt"
# >>> file_path.touch()
# Traceback (most recent call last):
# File "<pyshell#47>", line 1, in <module>
# file_path.touch()
# File "C:\Users\David\AppData\Local\Programs\Python\
# Python38-32\lib\pathlib.py", line 1256, in touch
# fd = self._raw_open(flags, mode)
# File "C:\Users\David\AppData\Local\Programs\Python\
# Python38-32\lib\pathlib.py", line 1063, in _raw_open
# return self._accessor.open(self, flags, mode)
# FileNotFoundError: [Errno 2] No such file or directory:
# 'C:\\Users\\David\\new_directory\\folder_c\\file2.txt'
# The FileNotFoundError exception is raised because the new_directory/
# folder has no folder_c/ subfolder.
# Unlike .mkdir(), the .touch() method has no parents parameter that
# you can set to automatically create an parent directories. This means
# that you need to first create any directories needed before calling
# .touch() to create the file.
# For instance, you can use .parent to get the path to the parent folder
# for file2.txt and then call .mkdir() to create the directory:
file_path.parent.mkdir(parents=True, exist_ok=True)
# Since .parent returns Path object, you can chain the .mkdir() method
# to write the entire operation on a single line of code.
# With the folder_c/ directory created, you can successfully create the
# file:
file_path.touch()
print(file_path.exists())
# Now that you know how to create files and directories, let’s look at
# how to get the contents of a directory

# Iterating Over Directory Contents
# Using pathlib, you can iterate over the contents of a directory. You
# might need to do this in order to process all of the files in a directory.
# The word process is vague. It could be reading the file and extracting
# some data, or compressing files in the directory, or some other operation.
# For now, let’s focus on how you go about retrieving all of the contents
# of a directory. You’ll learn how to read data from files in the next
# section.
# Everything in a directory is either a file or a subdirectory. The
# Path.iterdir() method returns an iterator over Path objects representing
# each item in the directory.
# To use .iterdir(), you first need a Path representing a directory. Let’s
# use the new_directory/ folder you created previously in your home directory
# and assigned to the new_dir variable:
print('Parent: ', new_dir)
for path in new_dir.iterdir():
    print(path)
# Right now, this new_directory/ folder contains three items:
# 1. A file called file1.txt
# 2. A directory called folder_c/
# 3. A directory called folder_a/
# Since .iterdir() returns an iterable, you can convert it to a list:
print(list(new_dir.iterdir()))
# You won’t often need to convert this to a list, but we’ll do it in subsequent
# examples to keep the code short. Generally, you’ll use .iterdir()
# in a for loop like you did in the first example.
# Notice that .iterdir() only returns items that are directly contained
# in the new_directoy/ folder. That is, you can’t see the path to the file
# that exists in the folder_c/ directory.
# There is a way to iterate over the contents a directory and all of its
# subdirectories, but you can’t do it easily with .iterdir(). We’ll get to
# this task in a moment, but first let’s talk about how to search for files
# within a directory.

# Searching For Files In a Directory
# Sometimes you only need to iterate over files of a certain type, or files
# with certain naming schemes. You can use the Path.glob() method
# on a path representing a directory to get an iterable over directory
# contents that meet some criteria.
# It might seem strange that a method that searches for files is called
# .glob(). The reason the method is given this name is historical. In
# early version of the Unix operating system, a program called glob was
# used expand to file path patterns to full file paths.
# The .glob() method does something similar. You pass to the method a
# string containing a partial containing a wildcard character and .glob()
# returns a list of file paths that match the pattern.
# A wildcard character is a special character that acts as a placeholder
# in a pattern. The wildcard are replaced with other characters to create
# a concrete file path. For example, in the pattern "*.txt", the asterisk *
# is a wildcard character that can be replaced with any number of other
# characters.
# The pattern "*.txt" matches any file path that ends with.txt. That is,
# if replacing the * in the pattern with everything in some file path up to
# the last four characters results in the original file path, then that file
# path is a match for the pattern "*.txt".
# Let’s look at an example using the new_directory/ folder previously assigned
# to the new_dir variable:
for path in new_dir.glob('*.txt'):
    print(path)
# Like .iterdir(), the .glob() method returns an iterable of paths, but
# this time only paths that match the pattern "*.txt" are returned.
# .glob() returns only paths that are directly contained in the folder on
# which it is called.
# You can convert the return value of .glob() to a list:
print(list(new_dir.glob('*.txt')))
# You will most often use .glob() in a for loop.
# The following table describes some common wildcard characters:
# Wildcard
# Character     Description     Example     Matches         Does Not
#                                                           Match
# *             Any number      "*b*"       b, ab, bc, abc  a, c, ac
#               of characters
# ?             A single        "?bc"       abc, bbc, cbc   bc, aabc,
#               character                                   abcd
# [abc]         Matches one     [CB]at      Cat, Bat        at, cat, bat
#               character in
#               the brackets
# We’ll look at some examples of each of the wildcard characters, but
# first, let’s create a few more files in the new_directory/ folder so that we
# have more options to play with:
paths = [
    new_dir / 'program1.py',
    new_dir / 'program2.py',
    new_dir / 'folder_a' / 'program3.py',
    new_dir / 'folder_a' / 'folder_b' / 'image1.jpg',
    new_dir / 'folder_a' / 'folder_b' / 'image2.jpg'
]
for path in paths:
    path.touch()
# Now that we have a more interesting structure to work with, let’s see
# how .glob() works with each of the wildcard characters.

# The * Wildcard
# The * wildcard matches any number of characters in a file path pattern.
# For example, the patter "*.py" matches all file paths that end in .py:
print(*list(new_dir.glob('*.py')), sep='\n')
# You can use the * wildcard multiple times in a single pattern:
print(list(new_dir.glob('*1*')))
# The pattern "*1*" matches any file path containing the number 1 with
# any number of characters before and after it. The only files in new_-
# directory/ that contain the number 1 are file1.txt and program1.py.
# If you leave off the first * from the patter "*1*" to get the pattern "1*",
# then nothing gets matched:
print(list(new_dir.glob('1*')))
# The pattern "1*" matches files paths that start with the number 1 and
# are followed by any number of characters after it. There are no files
# in the new_directory/ folder that match this, so .glob() doesn’t return
# anything.

# The ? Wildcard
# The ? wildcard character matches a single character in a pattern. For
# example, the pattern "program?.py" will match any file path that starts
# with the word program followed by a single character and then .py:
print(list(new_dir.glob('program?.py')))
# You can use multiple instances if ? in a single pattern:
print(list(new_dir.glob('?older_?')))
# The pattern "?older_?" matches paths that start with any letter followed
# by older_ and some other character. In the new_directory/ folder,
# those paths are the folder_a/ and folder_b/ directories.
# You can also combine the * and ? wildcards:
print(list(new_dir.glob('*1.??')))
# The pattern "*1.??" matches any file path that contains a 1 followed
# by a dot (.) and two more characters. The only path in new_directory/
# matching this pattern is program1.py. Notice that file1.txt doesn’t
# match the pattern because the dot is followed by three characters.

# The [] Wildcard
# The [] wildcard works kind of like the ? wildcard because it matches
# only a single character. The difference is that instead of matching any
# single character like ? does, [] only matches characters that are included
# between the square brackets.
# For example, the pattern "program[13].py" matches any path containing the
# word program, followed by either a 1 or 3 and the extension .py.
# In the new_directory/ folder, program1.py is the only path matching this
# pattern:
print(list(new_dir.glob('program[13].py')))
# As with the other wildcards, you can use multiple instances of the []
# wildcard, as well as combine it with any of the others.

# Recursive Matching With The ** Wildcard
# The major limitation you’ve seen with both .iterdir() and .glob() is
# that they only return paths that are directly contained in the folder on
# which they are called.
# For example, new_dir.glob("*.txt") only returns the file1.txt path in
# new_directory/. It does not return the file2.txt path in the folder_c/
# subdirectory, even though that path matches the "*.txt" pattern.
# There is a special wildcard character ** that makes the pattern recursive.
# The common was to use it is to prefix your pattern with "**/".
# This tells .glob() to match your pattern in the current directory and
# any of its subdirectories.
# For example, the pattern "**/*.txt" matches both file1.txt and
# folder_c/file2.txt":
print(list(new_dir.glob('**/*.txt')))
# Similarly, the pattern "**/*.py" matches any .py files in new_directory/
# and any of its subdirectories:
print(list(new_dir.glob('**/*.py')))
# There is also a shorthand method to doing recursive matching called
# .rglob(). To use it, pass the pattern without the **/ prefix:
print(*list(new_dir.rglob('*.py')), sep='\n')
# The r in .rglob() stands for “recursive.” Some people prefer to use
# this method instead of prefixing their patterns with **/ because it is
# slightly shorter. Both versions are perfectly valid. In this book, we’ll
# use .rglob() instead of the **/ prefix.

# Moving and Deleting Files and Folders
# Sometimes you need to move a file or directory to a new location or
# delete a file or directory all together. You can do this using pathlib,
# but keep in mind that doing so can result in the loss of data, so these
# operations must be made with extreme care.
# To move a file or directory, use the .replace() method. For example,
# the following moves the file1.txt file in the new_directory/ folder to
# the folder_a/ subfolder:
source = new_dir / 'file1.txt'
destination = new_dir / 'folder_a' / 'file1.txt'
# The .replace() method is called on the source path. The destination
# path is passed to .replace() as a single argument. Notice that
# .replace() returns the path to the new location of the file.
# Important
# If the destination path already exists, .replace() overwrites the
# destination with the source file without raising any kind of exception.
# This can cause undesired loss of data if you aren’t careful.
# You may want to first check if the destination file exists, and
# move the file only in the case that it does not:
# if not destination.exists():
# source.replace(destination)
if source.exists() and not destination.exists():
    source.replace(destination)
# You can also use .replace() to move or rename an entire directory.
# For instance, the following renames the folder_c subdirectory of new_-
# directory/ to folder_d/:
source = new_dir / 'folder_c'
destination = new_dir / 'folder_d'
if source.exists() and not destination.exists():
    source.replace(destination)
# Again, if the destination folder already exists, it is completely replaces
# with the source folder, which could result in the loss of quite a bit of
# data.
# To delete a file, use the .unlink() method:
file_path = new_dir / 'program1.py'
file_path.unlink()
# This deletes the program1.py file in the new_directory/ folder, which you
# can check with .exists():
file_path.exists()
# You can also see it removed with .iterdir():
print(list(new_dir.iterdir()))
# If the path that you call .unlink() does not exists, a FileNotFoundError
# exception is raised:
# >>> file_path.unlink()
# Traceback (most recent call last):
# File "<pyshell#94>", line 1, in <module>
# file_path.unlink()
# File "C:\Users\David\AppData\Local\Programs\Python\
# Python38-32\lib\pathlib.py", line 1303, in unlink
# self._accessor.unlink(self)
# FileNotFoundError: [WinError 2] The system cannot find the file
# specified: 'C:\\Users\\David\\new_directory\\program1.py'
# If you want to ignore the exception, set the optional missing_ok
# parameter to True:
file_path.unlink(missing_ok=True)
# In this case, nothing actually happens because the file located at file_-
# path does not exist.
# Important
# When you delete a file it is gone forever. Make sure you really
# want to delete it before you proceed!
# unlink() only works for paths representing files.
# To remove a directory, use the .rmdir() method. Keep in mind that the folder
# must be empty, otherwise an OSError exception is raised:
# >>> folder_d = new_dir / "folder_d"
# >>> folder_d.rmdir()
# Traceback (most recent call last):
# File "<pyshell#97>", line 1, in <module>
# folder_d.rmdir()
# File "C:\Users\David\AppData\Local\Programs\Python\
# Python38-32\lib\pathlib.py", line 1314, in rmdir
# self._accessor.rmdir(self)
# OSError: [WinError 145] The directory is not empty:
# 'C:\\Users\\David\\new_directory\\folder_d'
# In the case of folder_d/, it only contains a single file called file2.txt.
# To delete folder_d/, first delete all of the files it contains:
folder_d = new_dir / 'folder_d'
for path in folder_d.iterdir():
    path.unlink()
folder_d.rmdir()
print(folder_d.exists())
# If you need to delete an entire directory, even if it is non-empty, then
# pathlib won’t help you much. However, you can use the rmtree() function
# from the built-in shutil module:

folder_a = new_dir / 'folder_a'
shutil.rmtree(folder_a)
print(folder_a.exists())
# Recall that folder_a/ contains a subfolder folder_b/ which itself contains
# two files called image1.jpg and image2.png.
# When you pass the folder_a path object to rmtree(), the folder_a/ and
# all of it’s contents are deleted:
print(list(new_dir.rglob('image*.*')))
# In this section you covered quite a bit of ground. You learned how to
# do several common file system operations, such as:
# • Creating files and directories
# • Iterating over the contents of a directory
# • Searching for files and folders using wildcards
# • Moving and deleting files and folders
# All of these are common tasks. It is extremely important, however,
# to remember that your programs are guests on another persons computer.
# If you aren’t careful, you can inadvertently cause damage to a
# user’s computer resulting the loss of important documents and other
# data.
# When working with the file system you should always use caution.
# When in doubt, check that file paths exist or do not exists before performing
# some operation, and always check with the user that what
# you are about to do is OK!

# Review Exercises
# 1. Create a new directory in your home folder called my_folder/.
my_folder = pathlib.Path.cwd() / 'real_python' / 'my_folder'
my_folder.mkdir(exist_ok=True)
# 2. Inside my_folder/ create three files:
# • file1.txt
# • file2.txt
# • image1.png
file_list = [
    my_folder / 'file1.txt',
    my_folder / 'file2.txt',
    my_folder / 'image1.png'
]
for file in file_list:
    file.touch()
    print(f'{file} exists? {file.exists()}')
# 3. Move the file image1.png to a new directory called images/ inside of
# the my_folder/ directory.
image_1 = my_folder / 'image1.png'
dest = my_folder / 'images' / 'image1.png'
dest.parent.mkdir(parents=True, exist_ok=True)
image_1.replace(dest)
# 4. Delete the file file1.txt
file_1 = my_folder / 'file1.txt'
file_1.unlink(missing_ok=True)
# 5. Delete the my_folder/ directory.
shutil.rmtree(my_folder)


# Reading and Writing Files
# text file
# The Path.open() Method
# To use the Path.open() method, you first need a Path object.

path = pathlib.Path.cwd() / "real_python" / "new_directory" / "hello.txt"
path.touch()
file = path.open(mode="r", encoding="utf-8")

# 1. The mode parameter determines in which mode the file should be
# opened. The "r" argument opens the file in read mode.
# 2. The encoding parameter determines the character encoding used to
# decode the file. The argument "utf-8" represents the UTF-8 character encoding

print(file)

# "r" Creates a text file object for reading and raises an error if
# the file can’t be opened.
# "w" Creates a text file object for writing and overwrites all
# existing data in the file.
# "a" Creates a text file object for appending data to the end of
# a file.
# "rb" Creates a binary file object for reading and raises an
# error if the file can’t be opened.
# "wb" Creates a binary file object for writing and overwrites all
# existing data in the file.
# "ab" Creates a binary file object for appending data to the end
# of the file
# When you create a file object with .open(), Python maintains a link to
# the file resource until you either explicitly tell Python to close the file,
# or the program ends.
# You should always explicitly tell Python to close a file.
file.close()

# The open() Built-in
# The built-in open() function works almost exactly like the Path.open()
# method, except that it’s first parameter is a string containing the path
# the file you want to open.
file_path = "C:/Users/marce/Documents/python/real_python/" \
    "new_directory/hello.txt"
file = open(file_path, mode="r", encoding="utf-8")
print(file)
file.close()

# The with Statement
# If your program crashes between the time that a file is opened and
# when it is closed, the system resources maintained by the connection
# may continue to live on until the operating system realizes that it’s no
# longer needed.
# To ensure that file system resources are cleaned up even if a program
# crashes, you can open a file in a with statement. The pattern for using
# the with statement looks like this:
# with path.open(mode="r", encoding=-"utf-8") as file:
# Do something with file

# Reading Data From a File
cwd_path = pathlib.Path.cwd() / "real_python"
text_path = cwd_path / "new_directory" / "hello.txt"

with text_path.open(mode="r", encoding="utf-8") as file:
    text = file.read()

print(text)
print(f'{text!r}')

# Instead of reading the entire file at once, you can process each line of
# the file one at a time:
with text_path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")
    print()

# If you try to read from a file that does not exists, both .open() and
# open() raise a FileNotFoundError

# Writing Data To a File
# To write data to a plain text file, you pass a string to a file object’s
# .write() method. The file object must be opened in write mode by
# passing the value "w" to the mode parameter.

with text_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hi there!")

# When you set mode="w" in .open(), the contents of the original file
# are overwritten. This results in the loss of all of the original data
# in the file!

with text_path.open(mode="r", encoding="utf-8") as file:
    print(file.read())

# You can append data to the end of a file by opening the file in append
# mode:

with text_path.open(mode="a", encoding="utf-8") as file:
    file.write("\nHello")

with text_path.open(mode="r", encoding="utf-8") as file:
    print(file.read())

# You can write multiple lines to a file at the same time using the
# .writelines() method. First, create a list of strings:
lines_of_text = [
    "Hello from Line 1\n",
    "Hello from Line 2\n",
    "Hello from Line 3\n"
]

with text_path.open(mode="w", encoding="utf-8") as file:
    file.writelines(lines_of_text)

with text_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hello world\nHi again")

# If you open a non-existent path in write mode, Python attempts to
# automatically create the file. If all of the parent folders in the path
# exist, then the file can be created without problem:
# If you want to write to a path with parent folders that may not exist,
# call the .mkdir() method with the parents parameter set to True before
# opening the file in write mode
new_text_path = cwd_path / "new_directory" / "new_file.txt"
new_text_path.parent.mkdir(parents=True, exist_ok=True)
with new_text_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hello!")
print(new_text_path.is_file() and new_text_path.exists())
new_text_path.unlink()

# Read and Write CSV Data
# The csv Module
# The csv module can be used to read and write CSV files.
# import csv
# Writing CSV Files With csv.writer

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73]
]

# Instead of using a with statement, a file object is created and assigned
# to the file variable so that we can inspect each step of the writing
# process as we go.

csv_path = cwd_path / "new_directory" / "temperatures.csv"
file = csv_path.open(mode="w", encoding="utf-8")
writer = csv.writer(file)
for temp_list in daily_temperatures:
    writer.writerow(temp_list)
file.close()

# here’s what the code looks like using the with statement:
with csv_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    for temp_list in daily_temperatures:
        writer.writerow(temp_list)

# .writerow() writes a single row to the CSV file, but you can write multiple
# rows at one using the .writerows() method. This shortens the code
# even more when your data is already in a list of lists:
with csv_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(daily_temperatures)

# Reading CSV Files With csv.reader
# Create an empty list
daily_temperatures = []
with csv_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        # Convert row to list of integers
        int_row = [int(value) for value in row]
        # Append the list of integers to daily_temperatures list
        daily_temperatures.append(int_row)
print(daily_temperatures)

# Reading and Writing CSV Files With Headers
# It’s possible to read CSV files such as the one above using csv.reader(),
# but you have to keep track of the header row, and each row is returned
# as a list without the field names attached to it. It makes more sense to
# return each row as a dictionary whose keys are the field names and values
# are the field values in the row. This is precisely what csv.DictReater
# objects do!
# name,department,salary
# Lee,Operations,75000.00
# Jane,Engineering,85000.00
# Diego,Sales,80000.00
employees_dt = [
    ['name', 'department', 'salary'],
    ['Lee', 'Operations', 75000.00],
    ['Jane', 'Engineering', 85000.00],
    ['Diego', 'Sales', 80000.00]
]

csv_path = cwd_path / "new_directory" / "employees.csv"
with csv_path.open(mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(employees_dt)

# open the employees.csv file and create a new csv.DictReater object:
file = csv_path.open(mode='r', encoding='utf-8')
reader = csv.DictReader(file)
print(reader.fieldnames)
for row in reader:
    print(row)
file.close()
print()


def process_row(row, key='salary'):
    """Cast a str to float value inside a dict"""
    row[key] = float(row[key])
    return row


with csv_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print(*[process_row(row) for row in reader], sep='\n')

# You can write CSV files with headers using the csv.DictWriter class,
# which writes dictionaries with shared keys to rows in a CSV file.
people = [
    {'name': 'Veronica', 'age': 29},
    {'name': 'Audrey', 'age': 32},
    {'name': 'Sam', 'age': 24},
]
csv_path = cwd_path / "new_directory" / "people.csv"
with csv_path.open(mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file, fieldnames=people[0].keys(), lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(people)

# Review Exercises
# 1. Write a script that writes the following list of lists to a file called
# numbers.csv in your home directory:
numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
csv_path = cwd_path / "new_directory" / "numbers.csv"
with csv_path.open(mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(numbers)

# 2. Write a script that reads the numbers in the numbers.csv file from
# Exercise 1 into a list of lists of integers called numbers. Print the list
# of lists. Your output should like the following:
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]


def list_str_to_int(row):
    int_list = [int(val) for val in row]
    return int_list


with csv_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    print([list_str_to_int(row) for row in reader])

# 3. Write a script that writes the following list of dictionaries to a file
# called favorite_colors.csv in your home directory:
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]
csv_path = cwd_path / "new_directory" / "favorite_colors.csv"
with csv_path.open(mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file, fieldnames=favorite_colors[0].keys(), lineterminator='\n'
    )
    writer.writeheader()
    writer.writerows(favorite_colors)
# The output CSV file should have the following format:
# name,favorite color
# Joe,blue
# Anne,green
# Bailey,red
# 4. Write a script that reads the data from the favorite_colors.csv file
# from Exercise 3 into a list of dictionaries called favorite_colors.
# Print the list of dictionaries. The output should look something
# like this:
# [{"name": "Joe", "favorite_color": "blue"},
# {"name": "Anne", "favorite_color": "green"},
# {"name": "Bailey", "favorite_color": "red"}]
with csv_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print(list(reader))

# Challenge: Create a High Scores
# List
# In the Chapter 12 Practice Files folder, there is a CSV file called
# scores.csv containing data about game players and their scores. The
# first few lines of the file look like this:
# name, score
# LLCoolDave,23
# LLCoolDave,27
# red,12
# LLCoolDave,26
# tom123,26
# Write a script that reads the data from this CSV file and creates a new
# file called high_scores.csv where each row contains the player name
# and their highest score.
# The output CSV file should look like this:
# name,high_score
# LLCoolDave,27
# red,12
# tom123,26
# O_O,7
# Misha46,25
# Empiro,23
# MaxxT,25

# first read the csv file into a list of dicts
csv_path = cwd_path / "new_directory" / "scores.csv"
with csv_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    scores = [process_row(row, 'score') for row in reader]

# print(scores)
print()

# now sort by name and score
scores_by_name = sorted(scores, key=lambda k: (k['name'], -k['score']))
# print(*scores_by_name, sep='\n')

# then get only the high score
names = set()
high_scores = list()
for score in scores_by_name:
    if score['name'] in names:
        continue
    high_scores.append(score)
    names.add(score['name'])

print(high_scores)
csv_path = cwd_path / "new_directory" / "high_scores.csv"
with csv_path.open(mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file, fieldnames=high_scores[0].keys(), lineterminator='\n'
    )
    writer.writeheader()
    writer.writerows(high_scores)
