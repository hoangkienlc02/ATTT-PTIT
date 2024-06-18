#include <bits/stdc++.h>
using namespace std ;
int Fib(int i){
	if(i==0) return 0 ;
	if(i==1) return 1 ;
	return Fib(i-1)+Fib(i-2);
}
int main(){
	clock_t start, end;	
	double duration;
	start = clock();
	int n;
	cin>>n ;
	cout<<Fib(n) ;
    end = clock();
    cout<<endl ;
    duration = (double)(end - start) / CLOCKS_PER_SEC;
    printf("interchangeSort take %f", duration);
	return 0;
}
