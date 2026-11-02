#pragma GCC optimize("03")
#pragma GCC target ("avx")

#define NOT_MET 0
#define MAX_DIGIT_SUM 82

int getDigitSum(int val) {
    int num = 0;
    while (val) {
        num += val % 10;
        val /= 10;
    }
    return num;
}

int maximumSum(int* nums, int numsSize) {
    int *maxValSum = (int *)calloc(MAX_DIGIT_SUM, sizeof(int));

    int val, digitSum, pairSum;
    int maxTotal = NOT_MET;

    for (int i = 0; i < numsSize; i++) {
        val = *(nums + i);
        digitSum = getDigitSum(val);

        if (maxValSum[digitSum] > 0) {
            pairSum = maxValSum[digitSum] + val;
            if (pairSum > maxTotal)
                maxTotal = pairSum;
        }
        if (val > maxValSum[digitSum])
            maxValSum[digitSum] = val;
    }
    free(maxValSum);
    return maxTotal != NOT_MET ? maxTotal : -1;
}