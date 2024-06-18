#include<bits/stdc++.h>
using namespace std;
void SoLocPhat1(){
   int n;cin>>n;
   queue <string> q;
   q.push("6");q.push("8");
   vector<string> res;
   while(1){
       string temp=q.front();
       res.push_back(temp);
       q.pop();
   if(temp.length()<=n-1){
          q.push(temp+'6');
          q.push(temp+'8');
	}
	else break;
   }
	while(q.size()){
       res.push_back(q.front());
       q.pop();
   }
   for(int i=res.size()-1;i>=0;i--) cout<<res[i]<<' ';
   cout<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)SoLocPhat1();
   return 0;
}
