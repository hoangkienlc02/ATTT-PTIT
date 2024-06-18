#include<bits/stdc++.h>
using namespace std;
int n,p,sum;
vector <int> prime,v;
vector <vector <int> > res;
int /*2*/ snt(int n){
   if(n<2) return 0;
   for(int i=2;i<=sqrt(n);i++)
       if(n%i==0) return 0; return 1;
}
void Try(int i,int s,int count){//3
/*5*/ if(s==sum&&count==n){
       res.push_back(v);return;
   }
   if(s>sum|count>n) return;
/*4*/for(int j=i;j<prime.size();j++){
       v.push_back(prime[j]);
       Try(j+1,s+prime[j],count+1);//j+1
       v.pop_back();
   }
}
void SoNguyenTo(){
   cin>>n>>p>>sum;
   res.clear(),prime.clear();
	for(int i=p+1;i<=sum;i++){
       if(snt(i)==1) prime.push_back(i);
	}
	Try(0,0,0);
   cout<<res.size()<<endl;
	for(int i=0;i<res.size();i++){
       for(int j=0;j<res[i].size();j++){
           cout<<res[i][j]<<' ';
       }cout<<endl;
	}
}
int main(){
  int t;cin>>t;while(t--) SoNguyenTo();
return 0;
}
