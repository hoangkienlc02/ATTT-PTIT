#include<bits/stdc++.h>
using namespace std;
void HeCoSoK(){
   int k;string a,b;
   cin>>k>>a>>b;
   while(a.length()<b.length())a='0'+a;
   while(b.length()<a.length())b='0'+b;
   int carry=0,temp=0;
   string res;
	for(int i=a.length()-1;i>=0;i--){
       int temp=a[i]-'0'+b[i]-'0'+carry;
       res= char(temp%k+'0')+res;
       carry=temp/k;
	}
   if(carry>0)res='1'+res;
   cout<<res<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)HeCoSoK();
   return 0;
}
