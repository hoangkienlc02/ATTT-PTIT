#include<bits/stdc++.h>
using namespace std;
int const N=1e6+5;
int prime[N];
void tongCapSoNguyento(){
   int n;cin>>n;
   for(int i=2;i<n;i++){
       if(prime[i]==0&&prime[n-i]==0){
          cout<<i<<' '<<n-i<<endl;
		  return;
		}
   }
   	cout<<-1<<endl;
}
int main(){
   int t; cin>>t;
   prime[0]=1 ;prime[1]=1;
   for(int i=2;i<=sqrt(N);i++){
       if(prime[i]==0)
          for(int j=i*i;j<N;j+=i)
              prime[j]=1;
	}
   while(t--) tongCapSoNguyento();
   return 0;
}
