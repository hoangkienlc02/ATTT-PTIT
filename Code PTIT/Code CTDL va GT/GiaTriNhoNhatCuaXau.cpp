#include<bits/stdc++.h>
using namespace std;
void GiaTriNhoNhatCuaXau(){
   int k;string s; cin>>k>>s;
   if(k>s.length())return;
   int f[26];memset(f,0,sizeof(f));
   for(int i=0;i<s.length();i++) f[s[i]-'A']++;//1
   priority_queue <int> pq;
   for(int i=0;i<26;i++)//2
       if(f[i]!=0) pq.push(f[i]);
   while(k>0){
       int temp=pq.top();
       pq.pop();
       temp--;
       pq.push(temp);
       k--;
   }
   long long res=0;
   while(pq.size()){
       long long temp=pq.top();
       res+=temp*temp;
       pq.pop();
   }
   cout<<res<<endl;
}
int main(){
    int t;cin>>t;
    while(t--)GiaTriNhoNhatCuaXau();
    return 0;
}
