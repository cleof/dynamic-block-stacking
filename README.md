# dynamic-block-stacking
Problem set 9 for CS140 Algorithms.

## Submission information:
Files included:
* block-stacking.py: File with algorithm code. This file takes some input file formatted, formatted as is described in the PS9 assignment (https://goo.gl/2LmvHj), and outputs a file with the optimized block stack formation. The first line outputted will be the max block stack height and the following lines will be the list of block dimensions in the solution, in order of decreasing base size.
* ps9TestFiles: Folder with test files provided on Piazza. These output files now include the results of my tests.
* README.md

## To run block-stacking.py:
```python block-stacking.py input.txt output.txt```

## Block stacking algorithm
My block stacking algorithm follow these steps:
1. For each of the inputted dimensions, it generates the 3 different base size possibilities and adds them to a list. Because we later have to compare the depths and widths of the different dimension options, we must make sure they are ordered in a consistent way. In my blockOrientations() function, I ensure that for any appended base size, the depth (first tuple value) will always be less than or equal to the width (second tuple value).
2. I sort the list of dimensions in order of decreasing base area. I do this by calculating each of their base size, zipping the two lists, sorting by the base size value of the tuple and then removing the base size component.
3. In order to generate the dynamic programming table, I first initialize three arrays to track the three pieces of info that I care about for all dimensions: the height of the max stack that includes that dimension, the number of blocks used to achieve that height, and the list of blocks in the stack. These are all initialized as if the answer for each dimension was just a stack of itself. Next, we generate two for loops. For each block, we look at all blocks with larger area and determine whether or not we can stack the current block on top of it. If we can, then we know that we can increase the stack of the previous blocks optimal solution by the height of the current block. Thus, as we iterate through the outer for loop, we progressively generate the optimal solution for each block dimension.
4. Finally, we search through the dynamic programming table for the maximum possible stack height.

## Design decision
I chose to track the relevant information (max stack height, number of blocks in the max stack and the list of blocks in the max stack) in three separate lists that would all be updated as the solution was generated. I knew that the max_index for one was guaranteed to also the max_index for the others. This is sort of like generating 3 separate dynamic programming tables for the different solutions, which arguably takes up more space than is strictly necessary. Another option might have been to construct a single list of lists that each had three entries with the three relevant pieces of information. However, I personally found updating the three lists to be more readable and straightforward, and seeing as a solution with space usage 3N isn't asymptotically worse than space N, I figured it was an acceptable tradeoff.

## Code testing process
I tested my code progressively, as I was writing it. I first wrote the blockOrientations() function using various entries and print statements. I wanted to make sure that I wouldn't run into issues when comparing the depths and widths, respectively. Next, I wrote the blockStacking() method in stages, testing each stage before progressing (each stage was one of the steps of the algorithm, as described above). These were tested using lots of print statements, in order to visualize the lists and the DP table. I initially tested with a relatively small input, provided by the assignment. Lastly, I wrote the input and output functions. I tested my final algorithm using the test files included on Piazza, the results of which are included in this repo.

