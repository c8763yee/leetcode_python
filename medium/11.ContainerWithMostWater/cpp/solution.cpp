class Solution {
public:
    int maxArea(vector<int>& height) {
        int length = height.size();
        int left = 0, right = length - 1;
        int area, maxArea = 0;
        int leftSize, rightSize;
        while (left < right){
            leftSize = height[left];
            rightSize = height[right];
            area = min(leftSize, rightSize) * (right-left);
            if (area>maxArea)maxArea = area;
            if (leftSize >= rightSize){
                right--;
            }
            if (leftSize <= rightSize){
                left++;
            }
        }return maxArea;
    }
};