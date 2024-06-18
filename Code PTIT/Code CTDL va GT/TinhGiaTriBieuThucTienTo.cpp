#include<bits/stdc++.h>
using namespace std;
bool oprt(char x){
   if(x=='+'||x=='-'||x=='*'||x=='/')
       return 1; return 0;
}
int cal(int a,int b,char x){
   if(x=='+')return a+b; if(x=='-')return a-b;
   if(x=='*')return a*b; if(x=='/')return a/b;
}
void TinhGiaTriBieuThucTienTo(){
   string str;cin>>str;
   stack <int> s;
   for(int i=str.length()-1;i>=0;i--){
       if(oprt(str[i])==0) s.push(str[i]-'0');
       else{
          int str1=s.top();s.pop() ;
          int str2=s.top();s.pop() ;
          int temp=cal(str1,str2,str[i]) ;
          s.push(temp) ;
    	}
   }cout<<s.top()<<endl;
}
int main(){
   int t; cin>>t;
   while(t--) TinhGiaTriBieuThucTienTo() ;
}

