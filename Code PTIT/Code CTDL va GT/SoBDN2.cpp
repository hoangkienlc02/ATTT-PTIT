#include<bits/stdc++.h>
using namespace std;
void soBDN2(){
   int n;cin>>n;
   queue <long long> q;
   q.push(1);
   while(1){
       long long temp=q.front();
       if(temp%n==0){cout<<temp<<endl;break;}
       q.pop();
       q.push(temp*10);
       q.push(temp*10+1);
   }
}
int main(){
   int t;cin>>t;
   while(t--)soBDN2();
   return 0;
}
