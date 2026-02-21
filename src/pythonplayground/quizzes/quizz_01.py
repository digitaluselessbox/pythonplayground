
for i in range(5):
    if i == 2:
        continue
        eLif i == 4:
        break
        print(i, end=" ")

# What does this code snippet print?
# A) 0 1 3 4
# B) 0 1 2 3
# C) 1 3 4
# D) 0 1 3

# My suggestion without running the code:
# - Error at "eLif".
# - Even if eLif does not cause an error,
#   nothing will be printed since it never reaches the print statement.
#
# Many answers in the comments say: 0, 1, 3 (I think this is wrong)


# My answer after running the code and searching for the error cause:
#
# SyntaxError: invalid syntax at "i".
# Contrary to what I initially thought, `eLif` isn't seen as an error,
# but simply not recognized as `elif` and is initially treated as a
# normal identifier (variable name). After that, an identifier like "i"
# simply cannot be used. The parser then exits and returns a syntax
# error at `i`.
#
# The complete quizz could probably be a trick question, since it contains a
# syntax error.
# But....
# - the question provides several reasonable answers
# - the indentation of the code snippet is completely jumbled
# - even if we ignore the "eLif" line, nothing will be printed and no answer fits.
#
# I think that the quizmaster himself made a mess of things and may
# have intended to write the code like this:
#
# for i in range(5):
#   if i == 2:
#     continue
#   elif i == 4:
#     break
#	print(i, end=" ")
#
# In this case, with D) 0, 1, 3 we would hit an existing answer and the quizz
# would be more meaningful.
#
# Nobody will ever know.....
