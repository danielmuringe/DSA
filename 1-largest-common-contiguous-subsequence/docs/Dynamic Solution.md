# Largest Common Substring

The algorithm compares 2 strings to find the largest common substring between the strings
It goes through the 2 strings using a cartesian product and looks through the values diagonally
This is because all common substrings must follow a diagonal path in the cartesian product space of the 2 strings
The algorithm goes through the diagonals from the largest diagonal to the smallest diagonal

The cartesian space with comparisons looks as follows for the strings `"xmrxmrsx"` and `"xmrsx"`:


.     | x    | m    | r    | x    | m    | r    | s    | x 
----  | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
__y__ | -    | -    | -    | -    | -    | -    | -    | -
__m__ | -    | #    | -    | -    | #    | -    | -    | -
__r__ | -    | -    | #    | -    | -    | #    | -    | -
__s__ | -    | -    | -    | -    | -    | -    | #    | -
__y__ | -    | -    | -    | -    | -    | -    | -    | -

- `#` -> match, `-` -> not match 

The solution is good for relatively small strings but does not scale well because it is dependant on n and m. It has a time complexity of O( n<sup>2</sup> ) or O( n*m )

