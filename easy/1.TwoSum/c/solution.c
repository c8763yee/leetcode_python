#include <stdlib.h>

struct hash_entry {
    int key;            // 儲存差值 (target - nums[i]) 或數值本身
    int val;            // 儲存陣列索引 i
    UT_hash_handle hh;
};

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    struct hash_entry *maps = NULL, *ele = NULL, *tmp = NULL;
    int* result = NULL;
    *returnSize = 0;

    for (int i = 0; i < numsSize; i++) {
        // 尋找當前數值 nums[i] 是否為某個先前數字所需要的「差值」
        HASH_FIND_INT(maps, &nums[i], ele);
        
        if (ele != NULL) {
            result = (int*)malloc(2 * sizeof(int));
            result[0] = ele->val; // 先前數字的索引
            result[1] = i;        // 當前數字的索引
            *returnSize = 2;
            break;
        } else {
            ele = (struct hash_entry*)malloc(sizeof(struct hash_entry));
            ele->key = target - nums[i]; // 將需要的差值作為 key
            ele->val = i;                // 紀錄當前索引
            HASH_ADD_INT(maps, key, ele); // 第二個參數填寫結構體欄位名稱 key
        }
    }

    // 釋放雜湊表佔用的記憶體，避免 Memory Leak
    HASH_ITER(hh, maps, ele, tmp) {
        HASH_DEL(maps, ele);
        free(ele);
    }

    return result;
}