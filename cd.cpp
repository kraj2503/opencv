#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t;
    while (t--)
    {
        string str;
        cin >> str;
        int d = 0, c = 0;
        for (int i = 0; i < str.length(); i++)
        {
            if (str[i] == 'c')
                c++;
            if (str[i] == 'd')
                d++;
        }
        if (c - d == 0)
            cout << "dogs" << endl;
        else if (c - d ==1)
            cout << "cats" << endl;
        else if (d - c == 1)
            cout << "dogs" << endl;
        else if(c-d>1)cout<<"cats"<<endl;
        else if(d-c>1)cout<<"dogs"<<endl;
    }
    return 0;
}