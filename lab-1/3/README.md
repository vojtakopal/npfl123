# Minimum change distance

`python3 test_suite.py`

`dist(hyp, gold)` returns a pair of list of operations and calculated minimum distance.
operation: (name of operation [,characters]), e.g. 
  - ('n'): nothing, 
  - ('d', 'A'): delete A
  - ('i', 'B'): insert B
  - ('s', 'C', 'D'): subsitute C for D 
