#include<bits/stdc++.h>
using namespace std;
void HangDoiHaiDau(){
   int n;cin>>n;
   cin.ignore();
   deque<int> d;
   while(n--){
       string s;cin>>s;
       if(s=="PUSHFRONT"){int temp;cin>>temp;d.push_front(temp);}
       else if(s=="PUSHBACK"){int temp;cin>>temp;d.push_back(temp);}
       else if(s=="PRINTFRONT"){
              if(d.size())cout<<d.front()<<endl; else cout<<"NONE"<<endl;
        	}
       else if(s=="PRINTBACK"){
              if(d.size())cout<<d.back()<<endl; else cout<<"NONE"<<endl;
        }
       else if(s=="POPFRONT"&&d.size()) d.pop_front();
       else if(s=="POPBACK"&&d.size()) d.pop_back();
   }
}
int main(){
   HangDoiHaiDau();
     return 0;
}
