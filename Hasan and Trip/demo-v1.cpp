#include <iostream>
#include <limits>
#include <cmath>
using namespace std;

double DP[3005];
int X[3005];
int Y[3005];
int F[3005];
int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int N = 0;
    cin>>N;
    for( int i = 0; i < N; i++ )
    {
        cin>>X[i]>>Y[i]>>F[i];
        DP[i] = -100000000.0;
        //cout<<DP[i]<<endl;
    }
    DP[0] = F[0];
    
    for( int i = 1; i < N; i++ )
    {
        for( int j = 0; j < i; j++ )
        {
            double dis = sqrt( pow((X[i] - X[j] + 0.0), 2.0) + pow( (Y[i] - Y[j] + 0.0), 2.0 ));
            DP[i] = max( DP[i], DP[j] + F[i] - dis );
            //cout<<DP[i]<<endl;
        }
    }
    
    cout<<fixed<<DP[N - 1]<<endl;
    return 0;
}
