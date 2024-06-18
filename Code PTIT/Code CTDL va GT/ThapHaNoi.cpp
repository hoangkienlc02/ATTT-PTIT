#include <bits/stdc++.h>
using namespace std ;
int chuyen(int n , char a , char b){
	cout<<"Chuyen dia thu "<<n<<" tu coc "<<a<<" sang coc "<<b ;
	cout<<endl ;
}
void thapHaNoi(int n , char a , char b , char c){
	if(n==1){
		chuyen(1 , a , c) ;
	}else{
		thapHaNoi(n-1 ,a , c , b) ;
		chuyen(n , a , c) ;
		thapHaNoi(n-1 , b , a , c) ;
	}
}
int main(){
	int n ;
	char a='a' , b='b' , c='c' ;
	cin>>n;
	thapHaNoi(n , a , b , c) ;
}
