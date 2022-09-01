#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>

#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string c;
        int cats = 0, dogs = 0;

        cin >> c;
        if (c[0] == 'd' && c[1] == 'c')
        {
            c[1] = 'r';
        }
        for (int i = 1; i < c.length(); i++)
        {
            if (c[i] == 'd')
            {
                if (c[i - 1] == 'c')
                {
                    c[i - 1] = 'r';
                }
                else if (c[i + 1] == 'c')
                {
                    c[i + 1] = 'r';
                }

                else
                {
                    ;
                }
            }
        }
        for (int i = 0; i < c.length(); i++)
        {
            if (c[i] == 'c')
            {
                cats++;
            }
            else if (c[i] == 'd')
            {
                dogs++;
            }
            else
            {
                ;
            }
        }
        if (cats > dogs)
        {
            cout << "cats" << endl;
        }
        else if (cats < dogs)
        {
            cout << "dogs" << endl;
        }
        else
        {
            cout << "tie" << endl;
        }
    }

    return 0;
}