#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

int main(void) {
   int t,i,j,x;
    scanf("%d",&t);
    long int a[t],temp;
    for(i=0;i<t;i++)
        scanf("%ld",&a[i]);
    for(i=0;i<t;i++)
        {
         temp=a[i];
         j=i-1;
      while((temp<a[j])&&(j>=0)){
          a[j+1]=a[j];
            j=j-1;
            for(x=0;x<t;x++)
            printf("%ld ",a[x]);
            printf("\n");
      }
      
      a[j+1]=temp;
        
    }
            for(x=0;x<t;x++)
            printf("%ld ",a[x]);
            printf("\n");
   return 0;
}
