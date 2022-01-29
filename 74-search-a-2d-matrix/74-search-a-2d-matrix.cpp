class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        if (n == 0) return false;
        int m = matrix[0].size();
        int row = -1;
        for (int i = 1; i < n; i++) {
            if (matrix[i-1][0] <= target && matrix[i][0] > target) {
                row = i - 1;
                break;
            }
        }
        if (row == -1) {
            row = n - 1;
        }
        int low = 0, high = m - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (matrix[row][mid] == target) {
                return true;
            } else if (matrix[row][mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }
};