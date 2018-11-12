#include<bits/stdc++.h>
using namespace std;
double matrix[20][20];
char variable_type;
int variable_count=-1;
void matrix_print(double matrixx[][20],int N,int flag);
void parser()
{
    int variable_pos,sign=1;
    double val;
    string line;


    memset(matrix,0,sizeof matrix);
    ifstream file ("file.txt");
    vector<double> rhs;
    if (file.is_open())
    {
        int i=0;

        while ( getline (file,line) )
        {

            stringstream tokenizer(line);
            sign=1;
            bool equ=false;
            while(tokenizer>>line)
            {
                if(line=="=")
                    equ=true;
                else if(line.size()==1 && line=="+")
                    sign=1;
                else if(line.size()==1 && line=="-")
                    sign=-1;
                else if((line[0]>=48 && line[0]<=57) || line[0]=='.' || line[0]=='-')
                {
                    stringstream token(line);
                    token>>val;
                    if(equ==true)
                    {
                        rhs.push_back(val);
                        continue;
                    }
                    token>>variable_type;
                    if(variable_type>=65 && variable_type<=90)
                    {
                        matrix[i][variable_type-65]=val*sign;
                        variable_count=max(variable_count,variable_type-64);
                    }
                    else
                    {
                        token>>variable_pos;
                        matrix[i][variable_pos-1]=val*sign;
                        variable_count=max(variable_count,variable_pos);
                    }
                }
                else
                {
                    stringstream token(line);
                    token>>variable_type;
                    if(variable_type>=65 && variable_type<=90)
                    {
                        matrix[i][variable_type-65]=1*sign;
                        variable_count=max(variable_count,variable_type-64);
                    }
                    else
                    {
                        token>>variable_pos;
                        matrix[i][variable_pos-1]=1*sign;
                        variable_count=max(variable_count,variable_pos);
                    }
                }

            }
            i++;
        }
        for(int i=0; i<rhs.size(); i++)
            matrix[i][variable_count]=rhs[i];
        printf("Given augmanted matrix:\n");
        matrix_print(matrix,variable_count,1);
        file.close();
    }
}
void matrix_print(double matrixx[][20],int N,int flag)
{
    for (int i=0; i<N; i++, printf("\n"))
    {
        if(flag){
        for (int j=0; j<=N; j++)
            printf("%10.4lf ", matrixx[i][j]);
        }else{
          for (int j=0; j<N; j++)
            printf("%10.4lf ", matrixx[i][j]);
        }

    }

    printf("\n");
}
void LU_decomposer(double matrix[][20],int n,char variable_type)
{
    double A[20][20]= {0};
    double L[20][20]= {0}, U[20][20];
    double B[20]= {0}, X[20]= {0},Y[20]= {0};
    int i,j,k;
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            A[i][j]=matrix[i][j];
        }
    }
    for(i=0; i<n; i++)
    {

        B[i]=matrix[i][n];
    }

    printf("Matrix A: \n");

    matrix_print(A,n,0);
    printf("Vector B: \n");
    for(i = 0 ; i<n ; i++)
    {

        printf("%10.4lf\n",B[i]);
    }

    for(j=0; j<n; j++)
    {
        for(i=0; i<n; i++)
        {
            if(i<=j)
            {
                U[i][j]=A[i][j];
                for(k=0; k<=i-1; k++)
                    U[i][j]-=L[i][k]*U[k][j];
                if(i==j)
                    L[i][j]=1;
                else
                    L[i][j]=0;
            }
            else
            {
                L[i][j]=A[i][j];
                for(k=0; k<=j-1; k++)
                    L[i][j]-=L[i][k]*U[k][j];
                L[i][j]/=U[j][j];
                U[i][j]=0;
            }
        }
    }
    printf("Lower trianglar L: \n");
    matrix_print(L,n,0);
    printf("Upper triangular U: \n");
    matrix_print(U,n,0);
    for(i=0; i<n; i++)
    {
        Y[i]=B[i];
        for(j=0; j<i; j++)
        {
            Y[i]-=L[i][j]*Y[j];
        }
    }
    printf("Vector Z: \n");
    for(i=0; i<n; i++)
    {
        printf("%10.4lf\n",Y[i]);
    }



    for(i=n-1; i>=0; i--)
    {
        X[i]= Y[i];
        for(j=i+1; j<n; j++)
        {
            X[i]-=U[i][j]*X[j];
        }
        X[i]/=U[i][i];
    }


    printf("\nSolution:\n");
    ofstream of("output_file.txt");
    of<<"\nSolution:\n";
    for (int i=0; i<n; i++)
        if(variable_type>=65 && variable_type<=90)
        {
            string unknown="";
            unknown+=('A'+i);
            cout<<unknown<<" = "<<X[i]<<endl;
            of<<unknown<<" = "<<X[i]<<endl;
        }
        else
        {
            string unknown="";
            unknown+=variable_type;
            stringstream tokenizer;
            tokenizer << (i+1);
            unknown+=tokenizer.str();
            cout<<unknown<<" = "<<X[i]<<endl;
            of<<unknown<<" = "<<X[i]<<endl;
        }


}
int main()
{
    parser();
    LU_decomposer(matrix,variable_count,variable_type);
}
