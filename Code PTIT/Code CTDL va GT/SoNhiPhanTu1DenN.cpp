#include<bits/stdc++.h>
using namespace std;
void soNhiPhanTu1DenN(){
   int n;cin>>n;
   queue<long long> q;
   q.push(1);
   for(int i=1;i<=n;i++){
       long long temp=q.front();
       cout<<temp<<' ';
       q.pop();
       q.push(temp*10);
       q.push(temp*10+1);
   }cout<<endl;
}
int main(){
   int t;cin>>t;
    while(t--)soNhiPhanTu1DenN();
    return 0;
}
