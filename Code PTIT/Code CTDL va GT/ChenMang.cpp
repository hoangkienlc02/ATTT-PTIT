#include <iostream>
using namespace std ;

int main(){
	//Khai bao thanh phan............
	int n ;
	int k ;
	cin>> n ;
	int arr[n+1] ;
	
	//Nhap Mang , Nhap k............
	for(int i=1 ; i<=n ; i++){
		cin>>arr[i] ;
		arr[n+1] = 100 ;
	}
	cin>>k;
	
	//Thuat toan chen mang..............................
	int kLonNhat = 1 ;
	for(int i=1 ; i<=n ; i++){
		if(k<=arr[i]){
			for(int j=n+1 ; j>=i ; j--){
				arr[j] = arr[j-1] ;  
			}
			arr[i] = k ;
			kLonNhat = 0 ;
			break ;
		}
	}
	if(kLonNhat == 1){
		arr[n+1] = k ;
	}
	for(int i=1 ; i<=n+1 ; i++){
		cout<<arr[i]<<"  " ;
	}
	return 0;
}
 
