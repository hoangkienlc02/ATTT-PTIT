#include<bits/stdc++.h>
using namespace std;
long long convert(string a){
   long long res=0;
   for(int i=0;i<a.length();i++)
       res=res*2+a[i]-'0';
   return res;
}
void TichHaiSoNhiPhan(){
   string a,b;
   cin>>a>>b;
   cout<<convert(a)*convert(b)<<endl ;
}
int main(){
     int t;cin>>t;
     while(t--) TichHaiSoNhiPhan();
  return 0;
}
