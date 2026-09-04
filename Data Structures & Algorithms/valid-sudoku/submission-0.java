class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i < 9; i++){
            Set<Character> row = new HashSet<>();
            Set<Character> column = new HashSet<>();
            Set<Character> box = new HashSet<>();

            for(int j = 0; j < 9; j++){
                if(board[i][j] != '.'){
                    if(!row.add(board[i][j]))
                        return false;
                }

                if(board[j][i] != '.'){
                    if(!column.add(board[j][i]))
                        return false;
                }

                // ✅ Box check (3x3 grids)
                int rowIndex = 3 * (i / 3);
                int colIndex = 3 * (i % 3);
                int r = rowIndex + j / 3;
                int c = colIndex + j % 3;
                if (board[r][c] != '.') {
                    if (!box.add(board[r][c])) return false;
                }
            }
        }
        return true;
    }
}
