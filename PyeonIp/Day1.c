/* 자료형 / 입출력 / 연산자 */
#include <stdio.h>

int main(){
    // 자료형 
    short a=-32768;
    int b=-5;
    long c=-1000000000;
    long long d=10000000000;
    unsigned int e=4294967295;
    char f='a';
    float g=3.14;
    double h=3.14;
    long double i=1.2345678;

    printf("short %d \n", a);
    printf("int %d \n", b);
    printf("long %ld \n", c);
    printf("long long %lld \n", d);
    printf("unsinged int %u \n", e);
    printf("char %c \n", f);
    printf("float %f \n", g);
    printf("double %lf \n", h);
    printf("long double %lld \n", i);

    // 연산자
    // 단항 !++--&sizeof()(type)
    int num = 10;
    // 산술 */%
    num = num + num;
    // 증감

    // 관계 논리
    num != 4;
    // 비트 & ^ | << >>

    // 삼항 
    num = num == 10 ? 100 : 200;
    return 0;
}