#include <iostream>
#include <cstring>
using namespace std;

int DP[1000001];
int Q[10000];

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int T = 0;
    int Max = 0;
    cin>>T;
    for( int i = 0; i < T; i++ )
    {
        cin>>Q[i];
        Max = Max > Q[i] ? Max:Q[i];
    }
    memset(DP, 0, sizeof(DP));
    
    int end = Max / 2;
    for( int i = 1; i <= end; i++ )
    {
        for( int j = i + i; j <= Max; j += i )
        {
            DP[j]++;
        }
    }
    
    for( int i = 2; i <= Max; i++ )
    {
        DP[i] += DP[i - 1];
    }
    
    for( int i = 0; i < T; i++ )
    {
        cout<<DP[Q[i]]<<endl;
    }
    
    return 0;
}
