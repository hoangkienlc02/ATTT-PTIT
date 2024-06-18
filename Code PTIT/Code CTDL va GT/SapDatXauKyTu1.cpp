#include<bits/stdc++.h>
using namespace std;
void SapDatXauKyTu1(){
   string s;cin>>s;
   int f[26],sum=0;
   memset(f,0,sizeof(f));
   for(int i=0;i<s.length();i++) f[s[i]-'a']++;
   sort(f,f+26,greater<int>());
   for(int i=1;i<26;i++)sum+=f[i];
   if(sum+1>=f[0])cout<<1<<endl;
   else cout<<-1<<endl;
}
int main(){
   int t;cin>>t;
   cin.ignore();
   while(t--) SapDatXauKyTu1();
}
