## Python test 1 : Data types :
### **Datatyes in python :**
#### **Numeric**
- `int` (represents number)
- `float` (represents float number)
- `complex` (represenst complex number use .real() and .img() to extract real and imaginary part)

#### **Sequence**
- `str` (represents sequence of characters)
- `list` (mutable collection)
- `tuple` (immutable collection)
- `range` (represents sequence of numbers)

#### **Set types**
- `set` 
- `frozenset` (use fronzenset() function)

#### **Mapping types**
- `dict` (store data as key value pairs)

#### **Binary types**
- `byte` (immutable sequence of bytes | declared as `b'hello'` )
- `Bytearray` (collection of bytes)

#### **other types**
- `None` (no value)
- `True and False`

#### **Extras**
- `memoryview()`  returns where the data is stored  
- `id()`  returns a unique identifier that can be used to identify objects in memory.
- `isInstance(object , classinfo)` returns true if classinfo belongs to the specified object

answers :
- In Python, why is 0.1 + 0.2 != 0.3? Explain with IEEE-754 (because python stores the value nearest to the floating point rather than acual floating point specified , means if 0.1 is specified , it's not be stored 0.1 accurately)
- What happens if you evaluate float('inf') - float('inf')?   (result is nan)  (question passed)
- Why is True == 1 but True is 1 is False? (because by attaching the membership operator , we check if the both values belongs to sam object)
- What’s the output of:
```python
a = 256
b = 256
print(a is b) ## Answer True
c = 257
d = 257
print(c is d) ## Answer True
```
- Explain why -5 // 2 gives -3 and not -2. (because floor division returns roundedoff value) (question passed)
`/` divide operator (divide and return the actual value wheather it's float or int)
`//` floor division operator (returns rounded off value after divide)
`divmod()` (first divide and then returns the absolute value)  (question passed)
- Why does 0.1 + 0.1 + 0.1 - 0.3 give a non-zero result? (already answeres above)
- Show a case where Decimal and Fraction behave differently.( not approached)



### Remaining test :
📝 Section 2: Strings

Why are Python strings immutable, but bytearray is mutable?

What’s the output:

s = "hello"
print(id(s), id(s[:]))


Why is "abc"*3 allowed but 3*"abc" also valid?

Explain ''.join(['a', 'b', 'c']) vs '+'.join(['a', 'b', 'c']).

What does "🐍".encode('utf-8') return, and why length differs?

How does string interning affect "hello" is "hello"?

Why is "".join(['a', 'b']) faster than concatenation with + in a loop?

What does "abc"[::-1] mean?

Show a case where .find() and .index() differ.

How does Python handle "ab" in "abc" internally?

📋 Section 3: Lists & Tuples

Why does list1 = [[]]*3 create linked sublists?

What’s the difference between list.append() and list.extend()?

Why does tuple immutability not prevent t = ([],) from being mutated?

What happens when slicing a list: lst[1:1000] on a 5-element list?

Is tuple hashing affected if it contains a mutable object?

Why is lst.sort() different from sorted(lst)?

Explain the time complexity of lst.insert(0, x).

Why is tuple([1,2,3]) hashable but tuple([[1]]) not?

Show the difference between shallow copy and deep copy of lists.

Explain why *args collects into a tuple, not a list.

🧩 Section 4: Sets & Frozensets

Why does set([1,2,2,3]) have only 3 elements?

Can a set contain another set? Why or why not?

What is the hash value of frozenset([1,2,3]) compared to frozenset([3,2,1])?

Why does {True, 1, 2} collapse into {True, 2}?

Explain the difference between .union() and |.

Why is set lookup average-case O(1)?

What happens when you add float('nan') to a set multiple times?

Why can’t mutable objects be in a set?

Show a case where two distinct objects hash the same.

How does Python resolve hash collisions in sets?

📚 Section 5: Dictionaries

What is the output:

d = {}
d[float('nan')] = "snake"
print(d[float('nan')])


Why does dict maintain insertion order since Python 3.7?

What’s the difference between d.get('x') and d['x']?

How are dict keys stored internally?

Can a list be a dict key? Why not?

Show a dict comprehension that inverts keys and values.

What happens when two equal keys are inserted into a dict?

Why is lookup time in dicts not strictly O(1)?

What happens with d = {True: "yes", 1: "no"}?

Can a dict have a None key?

⚙️ Section 6: Advanced Internals

Explain the difference between is and ==.

Why does a = []; b = []; print(a is b) return False but a == b return True?

What is the difference between mutable and immutable datatypes?

Why is id(x) sometimes reused after deletion?

What happens with sys.getsizeof(1000) vs sys.getsizeof(1000000000)?

Explain the concept of Python’s small integer cache.

Why is id(257) == id(257) sometimes False?

What is the difference between hash() and id()?

Show how aliasing affects mutable objects.

Explain how garbage collection affects reference cycles.

🔄 Section 7: Type Conversions & Coercions

Why does int(True) return 1 but int(False) return 0?

What happens when you do int(5.9)?

What does float("nan") == float("nan") return? Why?

Why is bool([]) False but bool([0]) True?

What’s the difference between str([1,2,3]) and "".join(map(str, [1,2,3]))?

What happens if you do bytes("hello", "utf-8")?

Show a case where int() fails on a valid float string.

Explain coercion rules in mixed operations (e.g., int + float).

What happens with "5" * 3 vs int("5") * 3?

Show a failed case of eval("05").

🌀 Section 8: Special Objects

What is the purpose of Ellipsis (...) in Python?

What’s the difference between None and NotImplemented?

Why does print(None == 0) return False?

Show how Ellipsis can be used in NumPy slicing.

Why is NotImplemented returned in rich comparisons?

What does type(None) return?

Can None be a dictionary key?

Show a case where __eq__ returns NotImplemented.

Why is Ellipsis hashable?

What does repr(NotImplemented) show?

🧠 Section 9: Tricky Gotchas

What happens with:

x = 10
def f():
    print(x)
    x = 5
f()


Why is [] * 0 an empty list but "" * 0 also empty?

Why is set([[], []]) invalid?

Why is hash("abc") different across runs?

What’s the result of:

a = "py"
b = "thon"
print(a+b is "python")


Why is float('nan') in [float('nan')] True but float('nan') == float('nan') False?

Why does dict.fromkeys([1,2,3], []) share the same list?

Explain a = [[]]; b = a*3; b[0].append(1); print(b).

What’s wrong with using a mutable default arg in a function?

Why is round(2.675, 2) equal to 2.67 not 2.68?

🎯 Section 10: Mixed Edge Cases

Can you sort [1, "1", 2] in Python 3?

What happens when you compare [] < ()?

Why is print(hash((1,2,[3]))) invalid?

What does frozenset({1:2}) mean?

Why is 0 == 0.0 but 0 is 0.0 is False?

Why is True + True + True == 3?

Explain why bool("False") is True.

Show how __eq__ and __hash__ must be consistent for dict keys.

Why does isinstance(True, int) return True?

Show how subclassing tuple can break immutability assumptions.