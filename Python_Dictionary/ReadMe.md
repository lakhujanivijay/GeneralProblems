### Problem Definition

For `key-value` pairs, associate the `values` to a 'key' in a single instance

Consider following type of data set.
```
a 1
a 2
a 3
a 4
b 5
b 6 
b 7
c 8
c 9
```

And we want an ouput like this
```
a 1, 2, 3, 4
b 5, 6, 7
c 8, 9
```

i.e. each unique value in column `1` is associated with values in common `2` if the value in column `1` is same
