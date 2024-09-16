#include <stdio.h>

/*1*/
// int main() {
//     int sum = 0;
//     for (int i = 10; --i > 0;)
//         sum += i--;
//     printf("%d", sum);
// }


/*2*/
// void f0(int a);
// void f1(int a);
// void f2(int a);

// int main() {
//     int i;
    
//     //(A)
//     void (*f[3])(int) = {f0,f1,f2};

//     printf("Enter number 0, 1 or 2: ");
//     scanf("%d", &i);
//     if (i >= 0 && i <= 2) 
//         (*f[i])(i);
//     else 
//         printf("Wrong number");
// }

// void f0(int a) {
//     printf("You entered %d, so f0 is called", a);}
    
// void f1(int a) {
//     printf("You entered %d, so f1 is called", a);}
    
// void f2(int a) {
//     printf("You entered %d, so f2 is called", a);
// }

#define MAX 128

// void reverse_string_print(char* a) {
//         int SIZE = sizeof(a)/sizeof(char);
//         char stack[SIZE];
//         // assign stack
//         for (int i=0;;i++){
//             if(a[i] == '\0')
//                 break;
//             else
//                 stack[i] = a[i];
//                 printf("Stack[%d]: %c\n",i,a[i]);
//         }
//         int len = sizeof(stack)/sizeof(char);
//         printf("len: %d\n",len);
//         for(int x=0;x<len;x++){
//             printf("%c",stack[len-x-1]);
//         }
//     }
void reverse_string_print(char* a){
    if (*a == '\0') {
        return;
    } else {
        reverse_string_print(a + 1);
        printf("%c", *a);
    }
}

int main() {
    char a[MAX] = { 0, };
    printf("Write down a sentence: ");
    scanf("%s", a);
    reverse_string_print(a);
}