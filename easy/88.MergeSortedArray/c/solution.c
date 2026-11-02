void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    if (n == 0)
        return;
    if (m == 0) {
        for (int j = 0; j < n; j++) {
            nums1[j] = nums2[j];
        }
        return;
    }

    int k = m + n - 1, *tmp;
    m -= 1;
    n -= 1;
    while (m >= 0 && n >= 0) {
        nums1[k--] = nums1[m] > nums2[n] ? nums1[m--] : nums2[n--];
    }
    // tmp = m>=0?nums1:nums2;
    if (m>=0){
        tmp = nums1;
    }else{
        tmp = nums2;
        m = n;
    }
    while(k>=0){
        nums1[k--]=tmp[m--];
    }
}