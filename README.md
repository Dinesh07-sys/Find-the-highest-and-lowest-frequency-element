# Find the Highest and Lowest Frequency Element

A Python program that examines the frequency distribution of an array and identifies the elements occurring most and least frequently.

The solution separates the task into two stages: constructing a frequency map and comparing the resulting counts to determine the extreme frequencies.

## Example

Given:

```text
[10, 5, 10, 15, 10, 5]
```

The frequency distribution is:

```text
10 → 3
5  → 2
15 → 1
```

Therefore:

```text
Highest frequency element: 10
Lowest frequency element: 15
```

## Implementation

```python
class FrequencyCounter:
    def Frequency(self, arr):
        freq_map = {}

        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        maxFreq = 0
        minFreq = len(arr)

        maxEle = 0
        minEle = 0

        for element, count in freq_map.items():
            if count > maxFreq:
                maxFreq = count
                maxEle = element

            if count < minFreq:
                minFreq = count
                minEle = element

        print("The highest frequency element is:", maxEle)
        print("The lowest frequency element is:", minEle)


if __name__ == "__main__":
    fc = FrequencyCounter()

    arr = [10, 5, 10, 15, 10, 5]

    fc.Frequency(arr)
```

## Approach

The solution can be viewed as two separate operations:

```text
Array
  ↓
Build frequency map
  ↓
Compare frequencies
  ↓
Highest / Lowest frequency elements
```

### Stage 1: Build the Frequency Map

Each element is counted using:

```python
freq_map[num] = freq_map.get(num, 0) + 1
```

For:

```text
[10, 5, 10, 15, 10, 5]
```

the resulting dictionary becomes:

```python
{
    10: 3,
    5: 2,
    15: 1
}
```

The dictionary therefore provides a compact representation of how often each distinct element appears.

## Stage 2: Find the Maximum Frequency

The initial maximum frequency is:

```python
maxFreq = 0
```

Each frequency is then compared against it:

```python
if count > maxFreq:
    maxFreq = count
    maxEle = element
```

Whenever a larger frequency is discovered, both the frequency and its corresponding element are updated.

For the example:

```text
10 → 3
```

becomes the current maximum because `3 > 0`.

## Stage 3: Find the Minimum Frequency

The initial minimum is set to:

```python
minFreq = len(arr)
```

This guarantees that the first actual frequency encountered can replace it when appropriate.

The comparison is:

```python
if count < minFreq:
    minFreq = count
    minEle = element
```

For the example:

```text
15 → 1
```

eventually becomes the minimum-frequency element.

## Walkthrough

Starting frequency map:

```text
10 → 3
5  → 2
15 → 1
```

The comparison process can be represented as:

```text
Maximum:
0 → 3
      ↑
     10

Minimum:
6 → 3 → 2 → 1
              ↑
             15
```

Final values:

```text
maxFreq = 3
maxEle  = 10

minFreq = 1
minEle  = 15
```

## Output

```text
The highest frequency element is: 10
The lowest frequency element is: 15
```

## Why Use a Frequency Map?

Without a frequency map, the program would repeatedly scan the array to determine how often each element occurs.

The dictionary approach stores each distinct value together with its count:

```text
Element → Frequency
```

Once this structure exists, finding the largest and smallest frequencies becomes a separate linear scan over the distinct elements.

## Complexity Analysis

Let:

- `N` = number of elements in the array
- `K` = number of distinct elements

| Metric | Complexity |
|---|---|
| Building frequency map | `O(N)` |
| Finding highest/lowest frequency | `O(K)` |
| Overall Time | `O(N)` |
| Auxiliary Space | `O(K)` |

Since `K ≤ N`, the total time complexity remains `O(N)`.

## Important Consideration

The current implementation stores only one element for the highest frequency and one for the lowest frequency.

If multiple elements have the same frequency, the program does not return all of them. It retains the element selected according to the order in which the frequency map is traversed.

---

The core idea is to separate **counting** from **comparison**:

```text
Count occurrences
       ↓
Create frequency map
       ↓
Compare counts
       ↓
Identify frequency extremes
```

This separation makes the logic easier to understand and extend.
