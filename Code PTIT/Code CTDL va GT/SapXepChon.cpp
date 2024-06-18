#include<bits/stdc++.h>
using namespace std;
int n,a[101];
void out(){
     for(int i=0;i<n;i++) cout<<a[i]<<' ';
}
int main(){
     cin>>n;
     for(int i=0;i<n;i++) cin>>a[i];
     for(int i=0;i<n-1;i++){
       int k=i,temp=a[i];
      for(int j=i+1;j<n;j++){
          if(a[j]<temp){
              k=j;temp=a[j];
        	}
    	}
       swap(a[i],a[k]);
       cout<<"Buoc "<<i+1<<": ";
       out();
       cout<<endl;
	}
     return 0;
}
