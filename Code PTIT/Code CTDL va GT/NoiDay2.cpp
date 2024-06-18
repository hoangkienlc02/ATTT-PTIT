#include <bits/stdc++.h>//
using namespace std;
const long long mod=1e9+7;
void NoiDay2(){
   long long n;cin>>n;
     priority_queue<long long,vector<long long>,greater<long long> > pq;//1
   long long a[n];
     for(long long i=0; i<n; i++){
          cin>>a[i];
          pq.push(a[i]);
     }
     long long p, q, sum=0, sum1=0;
     while(pq.size()){
          p = pq.top(); pq.pop();
          q = pq.top(); pq.pop();//2
          sum = (p+q)%mod;
         sum1=(sum1+sum)%mod;
		if(pq.size()==0) break;//4
		pq.push(sum);//3
	}
	cout<<sum1<<endl;
}
int main(){
	int t;cin>>t;
	while(t--)NoiDay2();
	return 0;
}
