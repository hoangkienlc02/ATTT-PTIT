#include<bits/stdc++.h>
using namespace std;
int main(){
   int t;cin>>t;
   while (t--){
       string str;cin>>str;
       stack <int> s;
       s.push(-1);
       int res=0;
       for(int i=0;i<str.length();i++){
          if(str[i]=='(') s.push(i);
          else{
              s.pop();
              if(s.size()!=0)res=max(res,i-s.top());
              else s.push(i);
        	}
       }cout<<res<<endl;
	}
   return 0;
}
