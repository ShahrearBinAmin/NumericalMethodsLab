#include<bits/stdc++.h>
using namespace std;
#define e 2.718
double func(double x)
{
    return (x-4)*(x-4)*(x+2);
}

int main()
{
    FILE *fp=fopen("out1-1.txt","w");
    FILE *fpp=fopen("out1-2.txt","w");
    printf(" x   f(x)\n");
    printf("-----------------------\n");
    for(double x=1; x<=20; x+=1)
    {
        double y=func(x);
        printf("%lf %lf\n",x,y);
        fprintf(fp,"%lf %lf\n",x,y);
    }
    double lo,hi,xo,xm=0,a;
    int step=0;
    double low_y=0,high_y=0;
    printf("Give Input: ");
    scanf("%lf %lf %lf",&lo,&hi,&a);
    printf(" Itr Xmid Rel. Approx. Error\n");
    printf("-----------------------------------------\n");
    do
    {
        step++;
        low_y=func(lo);
        high_y=func(hi);
        //printf("%lf %lf\n",low_y,high_y);
        xo=xm;
        xm=hi-((high_y*(hi-lo))/(high_y-low_y));
        double y= func(xm);
        if(y>0) hi=xm;
        else lo=xm;
        printf(" %d %lf %lf\n",step,xm,fabs((xm-xo)/xm)*100);
        fprintf(fpp,"%d %lf\n",step,fabs((xm-xo)/xm)*100);
    }while(((xm-xo)/xm>a));
}
