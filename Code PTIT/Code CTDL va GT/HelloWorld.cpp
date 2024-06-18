#include<iostream>
using namespace std ;

void taoCauHinh1(int cauHinh[] , int n){
	for(int i=1 ; i<=n/2 ; i++){
		cauHinh[i] = 0 ;
	}
}
bool cauHinhCuoi(int cauHinh[] , int n){
	int flag=0 ;
	for(int i=1 ; i<=n ; i++){
		if(cauHinh[i] == 0){
			flag++ ;
		}
	}
	if(flag==0){
		return 1;
	}else{
		return 0;
	}
}
void sinhCauHinhKeTiep(int cauHinh[] , int n){
	for(int i=1 ; i<=n ; i++){
		
	}
}
int main(){
	int n ;
	cin>>n ;
	if(n%2==0){
		int cauHinh[n/2] ;
		taoCauHinh1(cauHinh , n) ; 
		
	}else{
		
	}
}
