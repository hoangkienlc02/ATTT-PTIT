#include <bits/stdc++.h>
using namespace std;
void show(stack<string> s){
   while(s.size()){
       cout<<s.top()<<' ';
       s.pop();
    } cout<<endl;
}
int main(){
   string str;
   int t;cin>>t;
   //cin.ignore();
   while(t--){
       stack <string> s;
       while(1){
          cin>>str;
          s.push(str);
          if(getchar()=='\n')break;
       }show(s);
	}
}
