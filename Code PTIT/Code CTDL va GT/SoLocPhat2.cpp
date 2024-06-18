#include <bits/stdc++.h>
using namespace std ;
void SoLocPhat2(){
   int n;cin>>n;
   queue<string> q;
   q.push("6"); q.push("8");
   vector <string> res;
   while( q.front().size()<=n ){
       string temp=q.front();
       res.push_back(temp);
       q.pop();
        q.push(temp+"6");
       q.push(temp+"8");
	}
   cout<<res.size()<<endl;
   for(int i=0;i<res.size();i++)
       cout<<res[i]<<' ';
   cout<<endl;
}
int main(){
  int t;cin>>t;
   while(t--) SoLocPhat2();
  return 0;
}
