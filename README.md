## Run Locally

Start the server and run web UI application

```bash
    python main.py run
```

Run Unit Test

```bash
    python main.py unit_test
```

Run UI Test

```bash
    python main.py webui_test
```

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

## UI Tests
**Bug Type** Wrong answer
**Input:** ""

**Test Failed:** Empty Output

## Bug Report Conclusion
Most of the bugs encountered due to neet code solution being optimized for a square matrix hence it hit beyond the range on irregular or non square matrices.
