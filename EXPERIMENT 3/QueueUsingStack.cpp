#include <iostream>
#include <stack>
using namespace std;

class Queue {
    stack<int> s1, s2;

public:
    void enqueue(int x) {
        s1.push(x);
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow\n";
            return;
        }

        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }

        cout << "Dequeued: " << s2.top() << endl;
        s2.pop();
    }

    void front() {
        if (isEmpty()) {
            cout << "Queue is Empty\n";
            return;
        }

        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }

        cout << "Front: " << s2.top() << endl;
    }

    bool isEmpty() {
        return s1.empty() && s2.empty();
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is Empty\n";
            return;
        }

        stack<int> temp1 = s1;
        stack<int> temp2 = s2;
        stack<int> rev;

        while (!temp2.empty()) {
            cout << temp2.top() << " ";
            temp2.pop();
        }

        while (!temp1.empty()) {
            rev.push(temp1.top());
            temp1.pop();
        }

        while (!rev.empty()) {
            cout << rev.top() << " ";
            rev.pop();
        }

        cout << endl;
    }
};

int main() {
    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    q.display();

    q.front();

    q.dequeue();

    q.display();

    q.enqueue(40);

    q.display();

    return 0;
}

/*
Output:
10 20 30
Front: 10
Dequeued: 10
20 30
20 30 40
*/
