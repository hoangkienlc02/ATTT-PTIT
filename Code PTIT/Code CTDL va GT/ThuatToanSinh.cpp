#include<iostream>
using namespace std ;
void taoCauHinhDau(int cauHinh[] , int a){
	for(int i=1 ; i<=a ; i++){
		cauHinh[i] = 0 ;
	}
}
int kiemTraCauHinhCuoi(int cauHinh[] , int a){
	int flag=0 ;
	for(int i=1 ; i<=a ; i++){
		if(cauHinh[i] == 0){
			flag++ ;
		}
	}
	if(flag==0){
		return 1;
	}else{
		return 0 ;
	}
}
void sinh(int cauHinh[] , int a){
	
	for(int i=a ; i>=1 ; i--){
		if(cauHinh[i] == 0){
			cauHinh[i] = 1;
			break ;
		}if(cauHinh[i] == 1){
			cauHinh[i] = 0 ;
		}
	}
}
void in(int cauHinh[] ,int a){
	for(int i=1 ; i<=a ; i++){
		cout<<cauHinh[i]<<"                   " ;
	}
	
}
void saoChepCauHinh(int cauHinh[] , int cauHinhDao[] , int n){
	for (int i = 1; i <= n ; i++) {
        cauHinhDao[i] = cauHinh[i] ;
    }
}
void dao(int cauHinhDao[], int a){
    for (int i = 1; i <= a/2; i++) {
        swap(cauHinhDao[i], cauHinhDao[a - i + 1]);
    }
}
int soSanhCauHinh(int cauHinh[] , int cauHinhDao[] , int n) {
	int flag=0 ;
	for (int i = 1; i <= n ; i++) {
		if(cauHinhDao[i] == cauHinh[i]){
			flag++ ;
		}
    }
    if(flag==n){
    	return 1;
	}else{
		return 0 ;
	}
}
int main(){
	int n ;
	scanf("%d" , &n) ;
	int cauHinh[n+1] ;
	taoCauHinhDau(cauHinh , n) ;
	in(cauHinh , n) ;
	cout<<"\n" ;
	while(kiemTraCauHinhCuoi(cauHinh , n) == 0){
		sinh(cauHinh , n) ;
		int cauHinhDao[n+1] ;
		saoChepCauHinh(cauHinh ,cauHinhDao , n) ;
		dao(cauHinhDao , n) ;
		if(soSanhCauHinh(cauHinh , cauHinhDao , n)==1){
			in(cauHinh , n) ;
			cout<<"\n" ;
		}
	}
	return 0 ;
}
