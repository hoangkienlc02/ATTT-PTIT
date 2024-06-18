#include <bits/stdc++.h>
using namespace std;
void initwsolve(){
     int n;cin>>n;
     string s="",temp="";
     for(int i=0;i<n;i++){
          cin>>temp;
		  s+=temp;
     }
     sort(s.begin(),s.end());
     for(int i=0;i<s.length();i++)
          if(s[i]!=s[i+1]) cout<<s[i]<<' ';
     cout<<endl;
}
int main() {
     int t;cin>>t;
     while(t--) initwsolve();
     return 0;
}
