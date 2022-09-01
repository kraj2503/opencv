#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{

    ll t;
    while (t--)
    {
        int n;
        cin >> n;

        vector<int> m1;
        for (int i = 0; i < n; i++)
        {
            int temp;
            cin >> temp;
            m1.push_back(temp);
        }
        int cmp = 1000;

        string tep;
        cin >> tep;
        // cin.getline(tep)
        for (int i = 0; i < n; i++)
        {
            if (tep[i] == '0')
            {
                cmp = min(cmp, m1[i]);
            }
        }
        cout << cmp << endl;
    }
    return 0;
}