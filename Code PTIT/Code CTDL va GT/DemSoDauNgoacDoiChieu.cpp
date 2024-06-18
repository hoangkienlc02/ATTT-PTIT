#include<bits/stdc++.h>
using namespace std;
void DemSoDauNgoacDoiChieu(){
   string str;
   cin>>str;
   stack <char> s;
   int count=0;
   for(int i=0;i<str.length();i++){
       if(str[i]!=')') s.push(str[i]);
       else {
          if(s.size()==0) {s.push('('); count++;}
          else s.pop();
   		}
   }
   cout<<count+s.size()/2<<endl ;
}
int main(){
   int t;cin>>t;
   cin.ignore();
   while (t--)DemSoDauNgoacDoiChieu();
   return 0;
}
