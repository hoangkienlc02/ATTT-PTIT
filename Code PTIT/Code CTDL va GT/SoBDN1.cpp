#include<bits/stdc++.h>
using namespace std;
void soBDN1(){
   long long n;cin>>n;//note :1l
   queue<long long> q;
   q.push(1);
   int res=0;
   while(1){
       long long temp=q.front();
       if (temp<=n)res++; else break;
       q.pop();
       q.push(temp*10);
       q.push(temp*10+1);
   }cout<<res<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)soBDN1();
     return 0;
}
