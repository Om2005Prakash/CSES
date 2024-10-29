#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

int main(){
    int n;
    scanf("%d", &n);
    char *data = (char *) malloc(n*sizeof(char));
    scanf("%s", data);
    int* nums = (int *) malloc(n*sizeof(int));

    int i = 0;
    int res = 0;
    char *token;

    while ((token = strsep(data, " ")) != NULL)
    {
        nums[i] = atoi(token);
        i++;
    }
    for (i = 0; i<n; i++){
        if ((nums[i] != -1) && (nums[i] != i+1)){
            if (nums[nums[i] - 1] == i+1){
                nums[nums[i] - 1] = -1;
            }
            else{
                
            }
        }
    }
}