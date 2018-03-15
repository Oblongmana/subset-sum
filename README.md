# Subset Sum

_Derived from http://stackoverflow.com/questions/4632322_

## Usage Example
``` python
>>> subset_sum([157.42,714.00,1009.50,1274.70,1978.50,2246.71,6391.22,6660.72,8785.00,9568.00,17404.16,18800.13,19233.74,33201.00,51000.00,51000.00,51000.00],198347.23)
Interim Result - Exact Match found:
    Iterations: 2597
    Matching Set: [51000.0, 51000.0, 51000.0, 17404.16, 8785.0, 6660.72, 6391.22, 2246.71, 1978.5, 1009.5, 714.0, 157.42]
    Amount: 198347.23
Execution Finished after 114111 iterations. Exact match(es) found, see above for details
```

## Additions
- Extended to allow float inputs.
- Added an optimization: sort numbers in descending order first
  -> As the algorithm cycles to the next number at a given index when
       the sum thus far exceeds the target, starting with the largest numbers
       means that we'll be able to cycle forward earlier

## Matt Damon

![Matt Damon](https://pixel.nymag.com/imgs/daily/vulture/2017/10/09/09-matt-damon.w190.h190.2x.jpg)
