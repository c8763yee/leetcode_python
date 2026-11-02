int min(int x, int y){
    return x<y?x:y;
}

int maxArea(int* height, int heightSize){
    int left = 0, right = heightSize - 1;
    int mostWater = 0;
    while (right > left){
        int hl = height[left], hr = height[right];
        int currentWater = (min(hl, hr) * (right - left));
        if (currentWater > mostWater) mostWater = currentWater;
        if (hl<=hr)  left++;
        if (hl >= hr) right --;
    }return mostWater;
}