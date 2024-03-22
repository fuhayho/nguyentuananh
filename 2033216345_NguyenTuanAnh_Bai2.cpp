#include <stdio.h>
#include <math.h>


int checkscp(int num) 
{
    int sqrtNum = sqrt(num);
    return (sqrtNum * sqrtNum == num);
}

int demscp(int n) 
{
    int count = 0;
    for (int i = 1; i < n; i++) 
    {
        if (checkscp(i)) 
        {
            count++;
        }
    }
    return count;
}

int main() {
    int n;
    printf("Nhap so nguyen duong n: ");
    scanf("%d", &n);

    printf("Các so chinh phuong nho hon %d la:\n", n);
    for (int i = 1; i < n; i++) 
    {
        if (checkscp(i)) 
        {
            printf("%d ", i);
        }
    }
    return 0;
}

