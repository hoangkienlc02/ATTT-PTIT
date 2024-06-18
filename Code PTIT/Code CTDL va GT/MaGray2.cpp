#include<bits/stdc++.h>
using namespace std;
void MaGray2(){
  string s; cin>>s;
  cout<<s[0];
     for(int i=1;i<s.length();i++){
    int res=(s[i]-'0')^(s[i-1]-'0'); cout<<res;
	}
  cout<<endl;
}
int main(){
     int t;cin>>t;
     while(t--) MaGray2();
     return 0;
}
