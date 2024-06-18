#include <bits/stdc++.h>
using namespace std;
void NoiDay1(){
    int n;cin>>n;
    priority_queue<int,vector<int>,greater<int> > pq;
    int a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
        pq.push(a[i]);
    }
    long long p, q, sum=0, suml=0;
    while(pq.size()){
        p = pq.top(); pq.pop();
        q = pq.top(); pq.pop();
        sum = p+q;
        suml+=sum;
		if(pq.size()==0) break;
        pq.push(sum);
	}
    cout<<suml<<endl;
}
int main(){
    int t;cin>>t;
    while(t--)NoiDay1() ;
    return 0;
}
