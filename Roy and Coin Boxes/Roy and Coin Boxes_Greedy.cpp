#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
using namespace std;

int DP[1000005];
int A[1000005];
int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int N = 0;
    int M = 0;
    int Q = 0;
    int a = 0;
    int b = 0;
    
    scanf("%d", &N);
    scanf("%d", &M);
    
    for( int i = 0; i < M; i++ )
    {
        scanf("%d %d", &a, &b);
        A[a] += 1;
        A[b + 1] += -1;
    }
    
    for( int i = 1; i <= N; i++ )
    {
        A[i] += A[i - 1];
        DP[A[i]]++;
    }
    
    for( int i = N - 1; i >= 1; i-- )
    {
        DP[i] += DP[i + 1];
    }
    
    scanf("%d", &Q);
    for( int i = 0; i < Q; i++ )
    {
        int temp = 0;
        scanf("%d", &temp);
        printf("%d\n", DP[temp]);
    }
    
    return 0;
}
