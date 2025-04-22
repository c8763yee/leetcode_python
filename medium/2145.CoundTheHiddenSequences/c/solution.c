#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int numberOfArrays(int *differences, int differencesSize, int lower, int upper){
  // int cur = y = x = 0;
  int cur = 0, y = 0, x = 0;
  for (int i = 0; i < differencesSize; i++){
    cur += differences[i];
    y = (cur >= y ? cur : y);
    x = (cur <= x ? cur : x);
    if ((y-x) > (upper-lower))
      return 0;
  }
  return (upper - lower + 1) - (y-x);
}
