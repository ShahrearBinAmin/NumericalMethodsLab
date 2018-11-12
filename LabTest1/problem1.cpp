#include<bits/stdc++.h>
using namespace std;

double fact(double n)
{
    if(n==1 || n==0)
    return 1;
    else return fact(n-1)*n;
}
double func(double x,double n)
{

    double immediate = pow((x/2),n);
    double total_sum;
    double s=0;
    for(int k=1; k<=10; k++)
    {
        total_sum = (pow(-1,k)*pow((pow(x,2)/4),k))/ (fact(k)*fact(n+k));
        total_sum=total_sum+s;
        s=total_sum;

    }
    return immediate*total_sum;
}
double func1(double x){
    return pow(x,3)-pow(x,2)-11*x+12;
}


int main()
{
    FILE *fp1=fopen("out1-1.1.csv","w");
    FILE *fp2=fopen("out1-1.2.csv","w");
    FILE *fp3=fopen("out1-1.3.csv","w");
    FILE *fpp4=fopen("out1-2.csv","w");
    FILE *fpp5=fopen("out1-3.csv","w");


    for(int i=0; i<3; i++)
    {
    printf(" x     f(x)\n\n");
    printf("---------- n= %d  -------------\n\n",i);
    double y;
        for(double x=0; x<10; x+=.1)
        {
            if(i==0)
            {
                y=func(x,0);
                printf("%lf %lf\n",x,y);
                fprintf(fp1,"%lf %lf\n",x,y);
            }
            else if(i==1)
            {
                y=func(x,1);
                printf("%lf %lf\n",x,y);
                fprintf(fp2,"%lf %lf\n",x,y);
            }
            else if(i==2)
            {
                y=func(x,2);
                printf("%lf %lf\n",x,y);
                fprintf(fp3,"%lf %lf\n",x,y);
            }




        }
        printf("\n");
    }
    printf("---------------x=1 to x=3 -----------\n");
    printf("x                J(x)\n");
    for(double x=1; x<=3; x+=.1)
    {
        printf("%lf          %lf\n",x,func(x,0));
    }

    printf("----------------Bisection------------------\n");

    double lo,hi,xo,xm,a,lor,hir;
    int step=0;
    printf("Give Input: ");
    scanf("%lf %lf %lf",&lo,&hi,&a);

    if((func1(lo)*func1(hi))>=0)
        cout<<"Root does not exists"<<endl;
    else
    {

        printf("Iteration    Upper    Lower    Xm     f(Xm)    Relative Approx\n");
        printf("-----------------------------------------\n");
        while(fabs(lo-hi)>a)
        {
            step++;
            xo=xm;
            xm=(hi+lo)/2;
            lor=lo;
            hir=hi;
            double y= func1(xm);
            if(y>0) lo=xm;
            else hi=xm;
            printf(" %d   %lf    %lf   %lf   %lf  %lf\n",step,hir,lor,xm,y,fabs((xm-xo)/xm)*100);

            fprintf(fpp4,"%lf %lf\n",xm,fabs((xm-xo)/xm)*100);

            fprintf(fpp5,"%d %lf\n",step,fabs((xm-xo)/xm)*100);
        }
    }
}

