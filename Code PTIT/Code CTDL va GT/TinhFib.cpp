#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
using namespace std ;
int Fib(int n){
	int fib1=1 , fib0=0 , fibn ,i ;
	if(n<=1)
		return n ;
	else{
		for(i=2 ; i<=n ; i++){
			fibn=fib1 + fib0 ;
			fib0=fib1 ;
			fib1=fibn ;
		}	
		return fibn ;
	}
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
    printf("thuat toan mat %f", duration);
	return 0;
}
