
# MSCS-532 Assignment 3

## Understanding Algorithm Efficiency and Scalability

**Student:** Mani Deep Kumar Pusuluri

## Overview

This project compares Randomized Quicksort with
first-pivot Deterministic Quicksort and implements
a hash table using separate chaining.

## Algorithms

### Randomized Quicksort
- Selects a uniformly random pivot.
- Uses three-way partitioning.
- Expected time: O(n log n).
- Worst-case time: O(n²).

### Deterministic Quicksort
- Selects the first element as pivot.
- Uses three-way partitioning.
- Average performance depends on input distribution.
- Worst-case time: O(n²).

### Hash Table with Chaining
- Uses a multiply-add-mod-prime hash function.
- Stores collisions in bucket lists.
- Supports insert, search, and delete.
- Uses dynamic resizing when load factor exceeds 0.75.
- Expected search cost: O(1 + alpha).

## Requirements

Python 3.10 or newer.

No third-party packages are required.

## Run Sorting Examples

python randomized_quicksort.py
python deterministic_quicksort.py

## Run Hash Table Example

python hash_table.py

## Run Unit Tests

python test_algorithms.py

## Run Benchmarks

python benchmark.py

## Benchmark Outputs

- benchmark_results.csv
- hash_results.csv

## Files

- randomized_quicksort.py
- deterministic_quicksort.py
- hash_table.py
- test_algorithms.py
- benchmark.py
- README.md
- Assignment3_Report.pdf

## Findings

All 21 automated tests passed.

The benchmark compared Randomized Quicksort and
first-pivot Deterministic Quicksort across four input
sizes and four dataset distributions.

For 2,000 reverse-sorted elements:
- Randomized Quicksort: 4.0435 ms
- Deterministic Quicksort: 314.3567 ms

Randomized Quicksort was approximately 77.7 times
faster on this particular input.

Deterministic Quicksort performed slightly better
on random and repeated-element datasets at n=2000.

The hash table supported insertion, searching,
deletion, collision resolution, and dynamic resizing.

At 1,000 entries and 2,003 buckets:
- Load factor: 0.4993
- Collisions: 223
- Total insertion time: 1.7688 ms

These measurements illustrate how input distribution
and load factor affect algorithm performance.


## Submission

The completed repository contains the Python code,
README, empirical results, and final written report.
