#include<bits/stdc++.h>
using namespace std;
void ToHopTiepTheo(){
	int n ;
	int k ;
	scanf("%d %d" , &n , &k) ;
	int arr[k+1] ;
	int arr2[k+1] ;
	for(int i=1 ; i<=k ; i++){
		cin>>arr[i] ;
	}
	for(int i=1 ; i<=k ; i++){
		arr2[i] = arr[i] ;
	}
	int i2=k ;
	while(arr[i2]==n-k+i2 && i2>0) i2-- ;
	if(i2==0){
		cout<<k<<endl ;
	}else{
		int dem = 0 ;
		arr[i2] = arr[i2]+1 ;
		for(int i3=i2 ; i3<=k ; i3++) arr[i3+1] = arr[i3]+1 ;
		for(int i=1 ; i<=k ; i++){
			int dem2 = 0 ;
			for(int j=1 ; j<=k ; j++){
				if(arr2[j] == arr[i]){
					dem2++ ;
				}
			}
			if(dem2==0){
				dem++ ;
			}
		}
		cout<<dem<<endl ;
	}
	 
}
int main(){
	int t ;
	scanf("%d" ,&t) ;
	while(t--) ToHopTiepTheo() ;
	return 0 ;	
}
