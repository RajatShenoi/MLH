#include <bits/stdc++.h>

using namespace std;

int main()
{
    cout << "Enter the number of elements: ";
    int n;
    cin >> n;

    vector<int> v(n);
    cout << "Enter the numbers seperated by space or new lines" << endl;
    for (int i = 0; i < n; i++)
        cin >> v[i];

    sort(v.begin(), v.end());

    for (auto el : v)
        cout << el << " ";

    cout << endl;
    return 0;
}