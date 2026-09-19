#include<stdio.h>
#include<string.h>
struct student
{
    char Name[10];
    char Number[30];
    char Sex;
};

int main()
{
    struct student b;//定义一个student类型的变量b
    strcpy(b.Name,"宋琪");//字符串赋值方式
    strcpy(b.Number,"204521480031");
    b.Sex='1';
    printf("%s %s %c",b.Name,b.Number,b.Sex);
    return 0;
}

//typedef可以解决每次使用结构体时都要写struct关键字的问题：

// typedef struct 
// {
//     char Name[10];
//     char Number[30];
//     char Sex;
// }student;

// 这样就直接可以声明变量