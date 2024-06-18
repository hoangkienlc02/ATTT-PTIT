#include<bits/stdc++.h>
using namespace std;
void CauTrucDuLieuHangDoi1(){
   int n;cin>>n;
   queue<int> q;
   while (n--){
       int ask;cin>>ask;
       switch(ask){
          case 1: cout<<q.size()<<endl;break;
          case 2: if(q.size()==0)cout<<"YES"<<endl;
                     else cout<<"NO"<<endl;break;
          case 3: int temp;cin>>temp;q.push(temp);break;
          case 4: if(q.size())q.pop();break;
          case 5:if(q.size()) cout<<q.front()<<endl;
              else cout<<-1<<endl;break;
          case 6:if(q.size()) cout<<q.back()<<endl;
              else cout<<-1<<endl;break;
   		}
   }
}
int main(){
   int t;cin>>t;
   while (t--)CauTrucDuLieuHangDoi1();
   return 0;
}
