#include<bits/stdc++.h>
using namespace std;
int n,check[1005],kq[1005];
struct data{
   int j,d,p;
}; data a[1005];
bool cmp(data a,data b){
     return a.p>b.p;
}
void SapXepCongViec2(){
   cin>>n;
   memset(check,0,sizeof(check));
   for(int i=0;i<n;i++)
       cin>>a[i].j>>a[i].d>>a[i].p;
   sort(a,a+n,cmp);
   for(int i=0;i<n;i++){
       for(int j=min(n,a[i].d )-1;j>=0;j--){
          if(check[j]==0){
              kq[j]=i;
              check[j]=1;break;
             }
    		}
    	}
		int res=0,count=0;
		for(int i=0;i<n;i++)
		       if(check[i]==1)count++,res+=a[kq[i]].p;
		cout<<count<<' '<<res<<endl;
}
int main(){
		int t;cin>>t;
		while(t--)SapXepCongViec2();
		return 0;
}
