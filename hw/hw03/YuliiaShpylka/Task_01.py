python_philosophy = """
1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules.
9. Although practicality beats purity.
10. Errors should never pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13. There should be one — and preferably only one — obvious way to do it.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now is better than never.
16. Although never is often better than right now.
17. If the implementation is hard to explain, it's a bad idea.
18. If the implementation is easy to explain, it may be a good idea.
19. Namespaces are one honking great idea — let's do more of those!"""

#Subtask 01
count_better = python_philosophy.count("better")
print("There was found 'better' word", count_better, "times")
count_never = python_philosophy.count("never")
print("There was found 'never' word", count_never, "times")
count_is = python_philosophy.count("is")
print("There was found 'is' word", count_is, "times")

#Subtask 02
print(python_philosophy.upper())

#Subtask 3
updated_text = python_philosophy.replace("i", "&")
print(updated_text)