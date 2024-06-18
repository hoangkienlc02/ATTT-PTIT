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
       for(int j=i+1;j<n;j++){
          if(a[j]<a[i])swap(a[i],a[j]);
    	}
       cout<<"Buoc "<<i+1<<": ";
       out();
       cout<<endl;
	}
	return 0;
}
