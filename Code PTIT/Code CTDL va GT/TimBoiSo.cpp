#include<bits/stdc++.h>
using namespace std;
void TimBoiSo(){
  int n;cin>>n;
  queue <long long> q;
  q.push(9);
  while(1){
	    long long x=q.front();
	    if(x%n==0) {
	       cout<<x<<endl; break;
		}
	    q.pop();
	    q.push(x*10);
	    q.push(x*10+9);
	}
}
int main(){
          int t;cin>>t;
          while(t--) TimBoiSo();
     return 0;
}

