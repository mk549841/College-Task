#include<stdio.h>
int max(int a, int b)
{
    return a > b ? a : b;
}
int max_subarray(int *array, size_t n)
{
    int max_ending_here = 0;
    int max_so_far = 0;
    unsigned int i;
 
    for (i = 0; i < n; i++) {
        max_ending_here = max(0, max_ending_here + array[i]);
        max_so_far = max(max_so_far, max_ending_here);
    }
    return max_so_far;
}
int main()
{
    int array[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    const size_t n = sizeof(array) / sizeof(int);
    printf("Max subarray sum is %d\n", max_subarray(array, n));
    return 0;
}
