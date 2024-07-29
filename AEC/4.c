#include<stdio.h>
#include<string.h>
int main ()
{
  char buff[15];
  int pass=0;
  printf("enter the password\n");
  scanf("%s",&buff);
  if (strcmp(buff,"Thegeek")){
      printf("the password is correct\n");
      pass=1;
  }else{
      printf("The password is wrong\n");
      pass=0;}
  if(pass==1)
      printf("root acess granted");
  return 0;
}
