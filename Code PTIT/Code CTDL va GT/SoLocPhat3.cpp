#include <bits/stdc++.h>
using namespace std;
void SoLocPhat3(){
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
   for(int i=res.size()-1;i>=0;i--)
       cout<<res[i]<<' ';
   cout<<endl;
}
int main(){
  int t;cin>>t;
   while(t--) SoLocPhat3();
  return 0;
}
