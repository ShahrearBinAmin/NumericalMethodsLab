#include<bits/stdc++.h>
using namespace std;
#define e 2.718
double func(double x)
{
    return -.016+((42+x)/(28-2*x)*(28-2*x)*(4-x));
}

int main()
{
    FILE *fp1=fopen("out2-1.csv","w");
    FILE *fp2=fopen("out2-2.csv","w");
    FILE *fp3=fopen("out2-3.csv","w");

    printf(" x   f(x)\n");
    printf("-----------------------\n");
    for(double x=0; x<=20; x++)
    {
        double y=func(x);
        printf("%lf %lf\n",x,y);
        fprintf(fp1,"%lf %lf\n",x,y);
    }

    double lo,lo1,hi,hi1,xo,xm=0,a;
    int step=0;
    double low_y=0,high_y=0;
    printf("Give Input: ");
    scanf("%lf %lf %lf",&lo,&hi,&a);
    lo1=lo;
    hi1=hi;
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
        fprintf(fp2,"%d %lf\n",step,fabs((xm-xo)/xm)*100);
    }while(fabs((xm-xo)/xm)>a);

    printf("---------------Bisection-----------");

    step=0;
    xm=0;

    printf(" Itr Xmid Rel. Approx. Error\n");
    printf("-----------------------------------------\n");
    while(fabs(lo1-hi1)>a)
    {
        step++;
        xo=xm;
        xm=(hi1+lo1)/2;
        double y= func(xm);
        if(y>0) lo1=xm;
        else hi1=xm;
        printf(" %d %lf %lf\n",step,xm,fabs((xm-xo)/xm)*100);
        fprintf(fp3,"%d %lf\n",step,fabs((xm-xo)/xm)*100);
    }


}

