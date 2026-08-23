## Day of the Programmer

**HackerRank Problem:** Day of the Programmer

### Problem
Find the 256th day of a given year while considering the differences between the Julian and Gregorian calendars.

### Approach
- For **1918**, Russia switched from the Julian to the Gregorian calendar, so the 256th day was `26.09.1918`.
- For years **1917 and earlier**, use the Julian leap-year rule.
- For years **1919 and later**, use the Gregorian leap-year rule.
- Return `12.09.year` for leap years and `13.09.year` for non-leap years.

### Time Complexity
- **O(1)**

### Space Complexity
- **O(1)**

### Language
- Python 3