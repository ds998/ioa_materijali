

#include <iostream>

using namespace std;

int main()
{
    int num_c=0;
    
    for(int a=0;a<=711;a++){
        for(int b=a;b<=711;b++){
            for(int c=b;c<=711;c++){
                for(int d=c;d<=711;d++){
                    num_c++;
                    if(a+b+c+d==711 && a*b*c*d==711000000){
                        cout<<(double)(a)/100<<" "<<(double)(b)/100<<" "<<(double)(c)/100<<" "<<(double)(d)/100<<endl;
                        cout<<"Number of calls: "<<num_c<<endl;
                        return 0;
                    }
            
                }
            }
            
        }
    }

    return 0;
}
