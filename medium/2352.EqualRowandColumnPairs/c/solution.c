typedef struct {
    uint64_t key;
    int count;
    UT_hash_handle hh;
} HashEntry;

static uint64_t custom_hash(uint64_t h, int x)
{
    return (h + (uint64_t)x) * UINT64_C(0x61C88647);
}

int equalPairs(int **grid, int gridSize, int *gridColSize)
{
    int n = gridSize;
    int ans = 0;
    HashEntry *map = NULL, *entry, *tmp;

    // Count identical row hashes.
    for (int i = 0; i < n; i++) {
        uint64_t key = 0;

        for (int j = 0; j < n; j++)
            key = custom_hash(key, grid[i][j]);

        HASH_FIND(hh, map, &key, sizeof(key), entry);

        if (entry) {
            entry->count++;
        } else {
            entry = malloc(sizeof(*entry));
            if (!entry) {
                ans = -1;
                goto cleanup;
            }

            entry->key = key;
            entry->count = 1;
            HASH_ADD(hh, map, key, sizeof(entry->key), entry);
        }
    }

    // Match column hashes against row hashes.
    for (int j = 0; j < n; j++) {
        uint64_t key = 0;

        for (int i = 0; i < n; i++)
            key = custom_hash(key, grid[i][j]);

        HASH_FIND(hh, map, &key, sizeof(key), entry);

        if (entry)
            ans += entry->count;
    }

cleanup:
    HASH_ITER(hh, map, entry, tmp) {
        HASH_DEL(map, entry);
        free(entry);
    }

    return ans;
}
