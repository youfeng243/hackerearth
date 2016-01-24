#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N = 0;
    string str = "";
    
    cin>>N;
    for( int i = 0; i < N; i++ )
    {        
        
        cin>>str;
        vector<int> DP(str.length() + 1, 0);
        if( str.length() <= 2 )
        {
            cout<<str.length()<<endl;
            continue;
        }
        
        if( str.length() <= 3 )
        {
            if( str[0] == str[1] && str[0] == str[2] )
            {
                cout<<str.length()<<endl;
                continue;
            }
            cout<<0<<endl;
            continue;
        }
        
        int Max = 0;
        for( int j = 3; j < str.length() + 1; j++ )
        {
            if( str[j - 1] == str[j - 2] && str[j - 1] == str[j - 3] )
            {
                DP[j] = 0;
            }
            else
            {
                DP[j] = DP[j - 3] + 3;
            }
            Max = max(DP[j], Max);
        }
        
        cout<<str.length() - Max<<endl;
    }
    
}
