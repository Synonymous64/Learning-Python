import time
print("Coffee is here")
username = "Prajwal"
print(username)

# (base) PS D:\LearnPython> python -u "d:\LearnPython\01_Basics\LoopsQUestions.py"
# (base) PS D:\LearnPython> python -u "d:\LearnPython\01_Basics\LoopsQUestions.py"
# 120
# (base) PS D:\LearnPython> python -u "d:\LearnPython\01_Basics\LoopsQUestions.py"
# 24
# (base) PS D:\LearnPython> python -u "d:\LearnPython\01_Basics\LoopsQUestions.py"
# 120
# (base) PS D:\LearnPython> python -u "d:\LearnPython\01_Basics\LoopsQUestions.py"
# Attempt 1  - wait time 1
# Attempt 2  - wait time 2
# Attempt 3  - wait time 4
# Attempt 4  - wait time 8
# Attempt 5  - wait time 16
# Attempt 6  - wait time 32
# (base) PS D:\LearnPython> python -u "d:\LearnPython\01_Basics\LoopsQUestions.py"
# Attempt 1  - wait time 1
# Attempt 2  - wait time 2
# Attempt 3  - wait time 4
# Attempt 4  - wait time 8
# Attempt 5  - wait time 16
# (base) PS D:\LearnPython> git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         01_Basics/LoopsQUestions.py

# nothing added to commit but untracked files present (use "git add" to track)
# (base) PS D:\LearnPython> git add .
# (base) PS D:\LearnPython> git commit -m "Loop Practice Questions Completed"
# [master c5b3853] Loop Practice Questions Completed
#  1 file changed, 63 insertions(+)
#  create mode 100644 01_Basics/LoopsQUestions.py
# (base) PS D:\LearnPython> git push origin master
# Enumerating objects: 6, done.
# Counting objects: 100% (6/6), done.
# Delta compression using up to 16 threads
# Compressing objects: 100% (3/3), done.
# Writing objects: 100% (4/4), 847 bytes | 847.00 KiB/s, done.
# Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
# remote: Resolving deltas: 100% (1/1), completed with 1 local object.
# To github.com:Synonymous64/Learning-Python.git
#    c9e6a87..c5b3853  master -> master
# (base) PS D:\LearnPython>
#  *  History restored 

# (base) PS D:\LearnPython> ls


#     Directory: D:\LearnPython


# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# d-----        13-12-2025     19:32                01_Basics
# d-----        13-12-2025     19:33                02_iterations_loops


# (base) PS D:\LearnPython> cd .\02_iterations_loops\
# (base) PS D:\LearnPython\02_iterations_loops> ls


#     Directory: D:\LearnPython\02_iterations_loops


# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# -a----        13-12-2025     19:33             77 random_code.py


# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> f = open("randome_code.py)
#   File "<stdin>", line 1
#     f = open("randome_code.py)
#              ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> f = open('randome_code.py')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#         ^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'randome_code.py'
# >>> f = open("random_code")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#         ^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'random_code'
# >>>
# KeyboardInterrupt
# >>>
# KeyboardInterrupt
# >>>
# KeyboardInterrupt
# >>> exit()
# (base) PS D:\LearnPython\02_iterations_loops> ls


#     Directory: D:\LearnPython\02_iterations_loops


# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# -a----        13-12-2025     19:33             77 code.py


# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> f = open("code.py")
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# 'print("Coffee is here")\n'
# >>> f.readline()
# 'username = "Prajwal"\n'
# >>> f.readline()
# 'print(username)\n'
# >>> f.readline()
# ''
# >>> f.readline()
# ''
# >>> f.readline()
# ''
# >>> exit()
# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> f = open("code.py")
# >>> f.__next__()
# 'import time\n'
# >>> f.__next__()
# 'print("Coffee is here")\n'
# >>> f.__next__()
# 'username = "Prajwal"\n'
# >>> f.__next__()
# 'print(username)\n'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^
# StopIteration
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^
# StopIteration
# >>> f = open("random_code")
# KeyboardInterrupt
# >>> for line in open("code.py").readlines()
#   File "<stdin>", line 1
#     for line in open("code.py").readlines()
#                                            ^
# SyntaxError: expected ':'
# >>> for line in open("code.py"):           
# ... print(line)
#   File "<stdin>", line 2
#     print(line)
#     ^^^^^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> print(line)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#           ^^^^
# NameError: name 'line' is not defined. Did you mean: 'slice'?
# >>> exit*(
# ... ^X^X
#   File "<stdin>", line 2
#     ↑↑
#     ^
# SyntaxError: invalid non-printable character U+0018
# >>> exit()
# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> for line in open ("code.py"):
# ...     print(lint)
# ...     print(line)
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     import sys
#            ^^^
# NameError: name 'lint' is not defined. Did you mean: 'line'?
# >>> for line in open ("code.py"):
# ...     print(line)
# ...
# import time

# print("Coffee is here")

# username = "Prajwal"

# print(username)

# >>> while True:
# ...     line = f.readline()
# ...     if not line: break
# ...     print(line, end="") 
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     import sys
#             ^
# NameError: name 'f' is not defined
# >>> exit()
# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> f = open("code.py")
# >>> while True:
# ...     line = f.readline()
# ...     if not line: break
# ...     print(line, end="")
# ...
# import time
# print("Coffee is here")
# username = "Prajwal"
# print(username)
# >>> ^X
#   File "<stdin>", line 1
#     ↑
#     ^
# SyntaxError: invalid non-printable character U+0018
# >>> ^X^X^X
#   File "<stdin>", line 1
#     ↑↑↑
#     ^
# SyntaxError: invalid non-printable character U+0018
# >>> exit()
# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> myList = [1,2,3,4]
# >>> it = iter(myList) 
# >>> it
# <list_iterator object at 0x000001BC180CD300>
# >>> it.next() 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^
# AttributeError: 'list_iterator' object has no attribute 'next'
# >>> it.__next__()
# 1
# >>> it.__next__()
# 2
# >>> it.__next__()
# 3
# >>> it.__next__()
# 4
# >>> it.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^^
# StopIteration
# >>> exit()
# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> f = open("code.py")
# >>> f.__next__()
# 'import time\n'
# >>> iter(f) is f
# True
# >>> iter(f) is f.__iter__()
# True
# >>> myNewList = [1,2,3]
# >>> iter(myNewList) is myNewList  
# False
# >>>
# KeyboardInterrupt
# >>>
# KeyboardInterrupt
# >>> exit()
# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> D = {'a': 1, 'b': 2}
# >>> for key in D.keys():
# ...     print(key)
# ...
# a
# b
# >>> it = iter(D)
# >>> it
# <dict_keyiterator object at 0x0000019DBCE57CE0>
# >>> it.__next__()
# 'a'
# >>> it.__next__()
# 'b'
# >>> next(it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^
# StopIteration
# >>> exit()
# (base) PS D:\LearnPython\02_iterations_loops> python
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> range(5)
# range(0, 5)
# >>> R = range(5)
# >>> R
# range(0, 5)
# >>> it = iter(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#          ^^^^^^^
# TypeError: 'int' object is not iterable
# >>> it = iter(R)
# >>> next(it)
# 0
# >>> next(it)
# 1
# >>> next(it)
# 2
# >>> next(it)
# 3
# >>> next(it)
# 4
# >>> next(it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^
# StopIteration