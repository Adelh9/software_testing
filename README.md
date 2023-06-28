# Bug Report
## Unit Tests
### Bug 1:
**Bug Type:** NULL pointer hit and crash
**Input:** []
**Test Failed:** Empty Matrix
**Change:**
		+Insertion on line 2 ->
		if len(matrix) == 0:
        	return 0
    
### Bug 2:
**Bug Type:** NULL pointer hit and crash
**Input:** [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

**Test Failed:** Matrix with irregular dimension

### Bug 3:
**Bug Type:** NULL pointer hit and crash
**Input:** [[1, 2, 3, 4, 5]]

Test Failed: Matrix with single row

### Bug 4:
**Bug Type:** Wrong answer
**Input:** [[1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]]
        
**Test Failed:** Matrix with irregular dimension

## UI Test
No Bugs encountered
