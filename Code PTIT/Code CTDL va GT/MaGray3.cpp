#include<bits/stdc++.h>
using namespace std;
void MaGray3(){
  string s; cin>>s;
  string res=s;
     for(int i=1;i<s.length();i++){
    if((res[i-1]-'0')^0==(s[i]-'0')) res[i]='0';
    else res[i]='1';
     }
  cout<<res<<endl;
}
int main(){
     int t;cin>>t;
     while(t--) MaGray3();
     return 0;
}
