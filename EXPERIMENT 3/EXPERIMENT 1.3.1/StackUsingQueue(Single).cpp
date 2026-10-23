#include<iostream>
#include<queue>

using namespace std;

class Stack{
    
    queue<int> q;


    public:
        void push(int x){
            q.push(x);
            int n = q.size();

            while(n>1){
                q.push(q.front());
                q.pop();
                n--;
            }
        }

        void pop(){
            if(q.empty()){
                cout<<"Stack Underflow\n";
                return;
            }
            cout<<"Popped: "<<q.front()<<endl;
            q.pop();
        }

        void top(){
            if(q.empty()){
                cout<<"Stack is Empty\n";
                return;
            }
            cout<<"Top: "<<q.front()<<endl;
        }

        bool isEmpty(){
            return q.empty();
        }

        void display(){
            if (q.empty()) {
            cout << "Stack is Empty\n";
            return;
        }

        queue<int> temp = q;

        while (!temp.empty()) {
            cout << temp.front() << " ";
            temp.pop();
        }
        cout << endl;
        }

};

int main(){
        
    Stack s;

    s.push(10);
    s.push(20);
    s.push(30);


    s.display();

    s.top();

    s.pop();

    s.display();

    s.push(40);

    s.display();

    return 0;
}

/*
Output:
30 20 10
Top: 30
Popped: 30
20 10
40 20 10
*/