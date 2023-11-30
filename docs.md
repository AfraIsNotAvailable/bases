# Explanations

## Addition in a given base

**! THERE WILL BE A CHECK TO SEE IF THE BASE IS EITHER BETWEEN *2* AND *10* OR IF IT'S **EXPLICITLY** *16***

### Base <=10

```
Input: a = 123, b = 234, base = 6
Expected Output: 401
Explanation:
    1 1 
    1 2 3
+   2 3 4
------------
    4 0 1

Input: a = 546, b = 248 base = 9
Output: 805
Explanation:
Sum of two integers in base 9 - 
    1 1
    5 4 6
+   2 4 8
-------------
    8 0 5 
``` 

**Succintly**: 
Let two digits of the number be `d1` and `d2`
**Place value** = `(d1 + d2) % base`
**Carry** = `(d1 + d2) / base`
Then add the rest
<br/>
<br/>

### Base 16
```
// TODO:
```

