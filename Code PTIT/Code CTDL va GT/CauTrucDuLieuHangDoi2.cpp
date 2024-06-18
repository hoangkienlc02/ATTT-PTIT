#include<bits/stdc++.h>
using namespace std;
void CauTrucDuLieuHangDoi2(){
   int n;cin>>n;
   cin.ignore();
   queue<int> q;
   while(n--){
       string s;cin>>s;
       if(s=="PUSH"){int temp;cin>>temp;q.push(temp);}
       else if(s=="PRINTFRONT"){
              if(q.size())cout<<q.front()<<endl;
              else cout<<"NONE"<<endl;
        }
       else{
          if(q.size()) q.pop();
    	}
	}
}
int main(){
   CauTrucDuLieuHangDoi2();

    return 0;
}
