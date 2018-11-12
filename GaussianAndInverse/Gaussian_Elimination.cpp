#include<bits/stdc++.h>
using namespace std;

int forwardElim(double mat[][50],int N);

void backSub(double mat[][50],int N,char var_name);

void gaussianElimination(double mat[][50],int N,char var_name)
{
    int singular_flag = forwardElim(mat,N);

    if (singular_flag != -1)
    {
        printf("Singular Matrix.\n");


        if (mat[singular_flag][N])
            printf("Inconsistent System.");
        else
            printf("May have infinitely many "
                   "solutions.");

        return;
    }

    backSub(mat,N,var_name);
}

void swap_row(double mat[][50], int i, int j,int N)
{

    for (int k=0; k<=N; k++)
    {
        double temp = mat[i][k];
        mat[i][k] = mat[j][k];
        mat[j][k] = temp;
    }
}

void print(double mat[][50],int N)
{
    for (int i=0; i<N; i++, printf("\n"))
        for (int j=0; j<=N; j++)
            printf("%lf ", mat[i][j]);

    printf("\n");
}

int forwardElim(double mat[][50],int N)
{
    for (int k=0; k<N; k++)
    {
        int i_max = k;
        int v_max = mat[i_max][k];

        for (int i = k+1; i < N; i++)
            if (abs(mat[i][k]) > v_max)
                v_max = mat[i][k], i_max = i;

        if (!mat[k][i_max])
            return k;

        if (i_max != k)
            swap_row(mat, k, i_max,N);


        for (int i=k+1; i<N; i++)
        {

            double f = mat[i][k]/mat[k][k];

            for (int j=k+1; j<=N; j++)
                mat[i][j] -= mat[k][j]*f;

            mat[i][k] = 0;
        }

    }
    return -1;
}

void backSub(double mat[][50],int N,char var_name)
{
    double x[N];

    for (int i = N-1; i >= 0; i--)
    {
        x[i] = mat[i][N];


        for (int j=i+1; j<N; j++)
        {

            x[i] -= mat[i][j]*x[j];
        }


        x[i] = x[i]/mat[i][i];
    }

    printf("\nSolution for the system:\n");
    ofstream of("ans.txt");
    of<<"\nSolution for the system:\n";
    for (int i=0; i<N; i++)
        if(var_name>=65 && var_name<=90)
        {
            string unknown="";
            unknown+=('A'+i);
            cout<<unknown<<" = "<<x[i]<<endl;
            of<<unknown<<" = "<<x[i]<<endl;
        }
    else
    {
        string unknown="";
        unknown+=var_name;
        stringstream ss;
        ss << (i+1);
        unknown+=ss.str();
        cout<<unknown<<" = "<<x[i]<<endl;
        of<<unknown<<" = "<<x[i]<<endl;
    }
}
int main()
{

  string line;
  double val;
  char var_name;
  int var_pos,sign=1,mx=-1;
  double mat[50][50];
  memset(mat,0,sizeof mat);
  ifstream myfile ("example.txt");
  vector<double> rhs;
  if (myfile.is_open())
  {
      int i=0;

    while ( getline (myfile,line) )
    {
        bool equal_sign=false;
        stringstream ss(line);
        sign=1;
        while(ss>>line)
        {
            if(line=="=")
                equal_sign=true;
            else if(line.size()==1 && line=="+")
                sign=1;
            else if(line.size()==1 && line=="-")
                sign=-1;
            else if((line[0]>=48 && line[0]<=57) || line[0]=='.' || line[0]=='-')
            {
                stringstream sss(line);
                sss>>val;
                if(equal_sign==true)
                {
                    rhs.push_back(val);
                    continue;
                }
                sss>>var_name;
                if(var_name>=65 && var_name<=90)
                {
                    mat[i][var_name-65]=val*sign;
                    mx=max(mx,var_name-64);
                }
                else
                {
                    sss>>var_pos;
                    mat[i][var_pos-1]=val*sign;
                    mx=max(mx,var_pos);
                }
            }
            else
            {
                stringstream sss(line);
                sss>>var_name;
                if(var_name>=65 && var_name<=90)
                {
                    mat[i][var_name-65]=1*sign;
                    mx=max(mx,var_name-64);
                }
                else
                {
                    sss>>var_pos;
                    mat[i][var_pos-1]=1*sign;
                    mx=max(mx,var_pos);
                }
            }

        }
        i++;
    }
    for(int i=0;i<rhs.size();i++)
        mat[i][mx]=rhs[i];
    print(mat,mx);
    myfile.close();
  }
  gaussianElimination(mat,mx,var_name);
}
