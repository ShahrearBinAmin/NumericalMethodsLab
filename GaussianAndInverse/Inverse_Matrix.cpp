#include<bits/stdc++.h>

//inverse of matrix using cofactors
using namespace std;
int N=50;

void getCofactor(double A[][50], double temp[][50], int p, int q, int n)
{
    int i = 0, j = 0;

    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < n; col++)
        {
            if (row != p && col != q)
            {
                temp[i][j++] = A[row][col];

                if (j == n - 1)
                {
                    j = 0;
                    i++;
                }
            }
        }
    }
}

double determinant(double A[50][50], int n)
{
    double D = 0;
    if (n == 1)
        return A[0][0];

    double temp[50][50];

    int sign = 1;
    for (int f = 0; f < n; f++)
    {

        getCofactor(A, temp, 0, f, n);
        D += sign * A[0][f] * determinant(temp, n - 1);

        sign = -sign;
    }

    return D;
}

// Function to get adjoint of A[N][N] in adj[N][N].
void adjoint(double A[50][50],double adj[50][50],double minors[50][50],double co_factors[50][50])
{
    if (N == 1)
    {
        adj[0][0] = 1;
        return;
    }

    double sign = 1, temp[50][50];

    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            getCofactor(A, temp, i, j, N);
            sign = ((i+j)%2==0)? 1: -1;

            minors[i][j]=(determinant(temp, N-1));
            co_factors[i][j] = (sign)*(determinant(temp, N-1));
            adj[j][i] = co_factors[i][j];
        }
    }
}

bool inverse(double A[50][50], double inverse[50][50],double minors[50][50],double co_factors[50][50])
{
    double det = determinant(A, N);
    if (det == 0)
    {
        cout << "Singular matrix, can't find its inverse";
        return false;
    }

    double adj[50][50];

    adjoint(A, adj, minors,co_factors);

    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            inverse[i][j] = adj[i][j]/float(det);

    return true;
}

template<class T>
void display(T A[50][50],FILE *fp)
{
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            printf("%10.3lf",A[i][j]);
            fprintf(fp,"%10.3lf",A[i][j]);
        }
        cout << endl;
        fprintf(fp,"\n");
    }
}

void solve(double inv[50][50],double B[50],double solutions[50])
{
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            solutions[i]+=inv[i][j]*B[j];
        }
    }
}
int main()
{

    double adj[50][50];  // To store adjoint of A[][]
    double inv[50][50]; // To store inverse of A[][]
    double minors[50][50],co_factors[50][50],B[50];
    FILE *fp=fopen("sol.txt","w");

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
        for(int i=0; i<rhs.size(); i++)
            B[i]=rhs[i];
        N=mx;
        myfile.close();
    }

    cout << "Input matrix is :\n";
    fprintf(fp,"Input matrix is :\n");
    display(mat,fp);

    adjoint(mat, adj,minors,co_factors);
    cout << "\nThe Minor matrix is :\n";
    fprintf(fp,"\nThe Minor matrix is :\n");
    display(minors,fp);

    cout << "\nThe Co-factor matrix is :\n";
    fprintf(fp,"\nThe Co-factor matrix is :\n");
    display(co_factors,fp);

    cout << "\nThe Adjoint matrix is :\n";
    fprintf(fp,"\nThe Adjoint matrix is :\n");
    display(adj,fp);

    cout << "\nThe Inverse matrix is :\n";
    fprintf(fp,"\nThe Inverse matrix is :\n");
    if (inverse(mat, inv,minors,co_factors))
        display(inv,fp);
    else fprintf(fp,"The Inverse doesn't exist\n");

    double solutions[50];
    solve(inv,B,solutions);

    cout << "\nThe set of solution is :\n";
    fprintf(fp,"\nThe set of solution is :\n");

    for (int i=0; i<N; i++)
        if(var_name>=65 && var_name<=90)
        {
            string unknown="";
            unknown+=('A'+i);
            cout<<unknown<<" = "<<solutions[i]<<endl;
            fprintf(fp,"%s = %lf\n",unknown.c_str(),solutions[i]);
        }
        else
        {
            string unknown="";
            unknown+=var_name;
            stringstream ss;
            ss << (i+1);
            unknown+=ss.str();
            cout<<unknown<<" = "<<solutions[i]<<endl;
            fprintf(fp,"%s = %lf\n",unknown.c_str(),solutions[i]);
        }

    return 0;
}
