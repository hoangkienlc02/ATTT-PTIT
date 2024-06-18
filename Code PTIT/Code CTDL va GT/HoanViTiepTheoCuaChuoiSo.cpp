#include<bits/stdc++.h>
using namespace std;
void HoanViTiepTheoCuaChuoiSo(){
     int n;cin>>n;
     string s;cin>>s;
     int i=s.length()-1 , j=s.length()-1;
     while(s[i]<=s[i-1]&&i>0) i--;i-- ;
	if(i<0) {
          cout<<n<<" BIGGEST\n"; return;
	}
     else{
          while(s[j]<=s[i]) j--;
          swap(s[i],s[j]);
          sort(s.begin()+i+1,s.end());
          cout<<n<<' ';
          for(int i=0;i<s.length();i++) cout<<s[i]; cout<<endl ;
     }
}
int main(){
     int t;cin>>t;
     while(t--) HoanViTiepTheoCuaChuoiSo();
      return 0;
}
