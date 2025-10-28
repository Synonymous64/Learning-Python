# Object types // DataTypes

- Numbers: 1, 2, 3, 4, 3+4j (Complext number), 0b11, Decimal(), Fraction()

- String: 'Spam', "Bob's", b'a\z01c', u'sp\zc4m',(unicode characters also)

- List: [1, 2, 3, [12, 2]], ['spam', 'eggs', 100], list(range(5))  # [0, 1, 2, 3, 4]

- Tuple: (1, 2, 3), ('spam', 'eggs', 100), tuple(range(5))  # (0, 1, 2, 3, 4)

- Dictionary: {'name': 'Bob', 'age': 40}, dict(name='Bob', age=40), dict([('name', 'Bob'), ('age', 40)]) (no indexing like lists, we have to give the keys and values by ourselves)

- Set: {1, 2, 3}, set([1, 2, 3, 2, 1])  # {1, 2, 3} (no duplicates, unordered)

- File: open('data.txt', 'r'), open('data.txt', 'w')  # file object for reading or writing files

- Boolean: True, False  # Subclass of integers

- NoneType: None  # Represents the absence of a value

- Functions, Modules, Classes, Instances: user-defined types created using def, import, class keywords respectively

- Advanced: Decorators, Generators, Context Managers, Coroutines, MetaProgramming

