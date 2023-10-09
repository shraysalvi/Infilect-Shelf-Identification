from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def is_2d_matrix(value):
    if not value:
        return False

    if not isinstance(value, list):
        return False
    
    for item in value:
        if not isinstance(item, list):
            return False
    
    # To ensure all rows contain same number of columns or value
    lengths = {len(item) for item in value}
    if len(lengths) > 1:
        return False
    
    return True


def identify_product(layout, i, j, visited):
    """This function is used to find all posible shapes"""
    rows, cols = len(layout), len(layout[0])
    product = layout[i][j]
    stack = [(i, j)]
    min_row, max_row = i, i
    min_col, max_col = j, j
    count = 0

    # DFS Traversal
    while stack:
        x, y = stack.pop()
        if 0 <= x < rows and 0 <= y < cols and not visited[x][y] and layout[x][y] == product:
            visited[x][y] = True
            count += 1
            min_row, max_row = min(min_row, x), max(max_row, x)
            min_col, max_col = min(min_col, y), max(max_col, y)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # Neighbour Cells
                stack.append((x+dx, y+dy))

    height, width = max_row - min_row + 1, max_col - min_col + 1

    if count == 1:
        shape = "single cell"
    elif count == height * width:
        if height == width:
            shape = "square"
        elif height > width:
            shape = "vertical rectangle"
        else:
            shape = "horizontal rectangle"
    else:
        shape = "polygon"

    return shape, min_row, min_col, max_row, max_col


def shelf_identifier(layout):
    m, n = len(layout), len(layout[0])
    visited = [[False]*n for _ in range(m)]
    result = {}

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                shape, min_row, min_col, max_row, max_col = identify_product(layout, i, j, visited)

                # Location Finding
                location = []
                if min_row == 0:
                    location.append("top")
                if max_row == m - 1:
                    location.append("bottom")
                if min_col == 0:
                    location.append("left")
                if max_col == n - 1:
                    location.append("right")
                if (0 < min_row and max_row < m - 1) or (0 < min_col and max_col < n - 1):
                    location.append("middle")
                result[layout[i][j]] = {
                    'shape': shape,
                    'location': location
                }
    return result


class ShelfIdentificationView(APIView):
    def post(self, request):
        input_matrix = request.data.get('matrix')
        if not is_2d_matrix(input_matrix):
            return Response({'error': 'Incorrect input Matrix', "input parameter": {"matrix": [[], []]}, "input description": "Input must be 2d-array or matrix with equal element in each rows."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            result = shelf_identifier(input_matrix)
        except TypeError:
            return Response({'error': 'invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)
