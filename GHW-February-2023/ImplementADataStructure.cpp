#include <bits/stdc++.h>

using namespace std;

class Stack
{
    int top;
    int arr[100];

public:
    Stack()
    {
        top = -1;
    }
    void push(int x)
    {
        arr[++top] = x;
    }
    int pop()
    {
        return arr[top--];
    }
    int peek()
    {
        return arr[top];
    }
    bool isEmpty()
    {
        return top == -1;
    }
};

int main(int argc, char const *argv[])
{
    Stack s;
    s.push(10);
    s.push(20);
    cout << s.pop() << endl;
    cout << s.peek() << endl;
    cout << s.isEmpty() << endl;
    return 0;
}
