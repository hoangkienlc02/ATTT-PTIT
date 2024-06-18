#include<bits/stdc++.h>
using namespace std;
stack <int> s;
string str;
int n;
void show(){
   stack <int> s1=s;
   vector <int> a;
   while(!s1.empty()){
       a.push_back(s1.top());
       s1.pop();
	}
   for(int i=a.size()-1;i>=0;i--)cout<<a[i]<<' ';
   cout<<endl;
}
int main(){
   while (1){
       cin>>str;
       if(str=="push"){cin>>n;s.push(n);}
       else if(str=="pop")s.pop();
       else if(str=="show") show();
       if(s.size()==0){cout<<"empty";break;}
	}
  	return 0;
}
