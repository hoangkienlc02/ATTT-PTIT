#include<bits/stdc++.h>
using namespace std;
stack <int> s;
void show(){
   if(s.size()==0)cout<<"NONE"<<endl;
       else cout<<s.top()<<endl;
}
int main(){
   int t;cin>>t;
   while (t--){
       string str;cin>>str;
    if(str=="PUSH"){int n;cin>>n;s.push(n);}
       else if(str=="POP"){if(s.size()!=0)s.pop();}
       else show();
    }
   return 0;
}
