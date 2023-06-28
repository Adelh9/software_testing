def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if len(matrix) == 0: # Inserted after 1st Bug
        return []
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    while left < right and top < bottom:

        right = len(matrix[top]) - left # Insertion after 2nd Bug
        # get every i in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        if not (left < right and top < bottom):
            break
        
        #right = len(matrix[top]) - left # Insertion after 2nd Bug
        # get every i in the right col
        for i in range(top, bottom):
            right = len(matrix[i]) - left # Insertion after 4th Bug
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        if not (left < right and top < bottom): #Insertion after 3rd Bug
            break
        
        # get every i in the left col
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res