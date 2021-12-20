#include <stdio.h>

typedef struct grade {
        char ID[10];
        char name[10];
        int mtg;
        int prgg;
        int elg;
        float avr;
    }grade;

int main(void){
    grade input[100]={-1};
    grade change;
    int n;
    char f[10],check,choice;
    float p[100];
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        scanf("%s",input[i].ID);
        scanf("%s",input[i].name);
        scanf("%d",&input[i].mtg);
        scanf("%d",&input[i].prgg);
        scanf("%d",&input[i].elg);
        input[i].avr=(float)(input[i].mtg+input[i].prgg+input[i].elg)/3;
        getchar();
    }
    for (int i=0;i<n;i++){
        for (int j=0;j<n-1;j++){
            if (input[j].avr<input[j+1].avr){
                change=input[j];
                input[j]=input[j+1];
                input[j+1]=change;
            }
        }
    }
    for (;;){
        puts("===== menu =====");
        puts("f: find specific students' data");
        puts("s: show all students' data");
        puts("d: show the sorted students' data (high to low)");
        puts("a: show the sorted students' data (low to high)");
        puts("b: show the average score value");
        puts("q: quit");
        printf("function choice: ");
        scanf(" %c",&choice);
        switch (choice)
        {
        case 'f':
            scanf("%s",f);
            for (int i=0;i<n;i++){
                for (int j=0,check=0;j<10 && input[i].ID[j]!=EOF;j++){
                    if (f[j] != input[i].ID[j])
                    check=1;
                }
                if (check==0){
                    printf("%s\t",input[i].ID);
                    printf("%s\t",input[i].name);
                    printf("%d\t",input[i].mtg);
                    printf("%d\t",input[i].prgg);
                    printf("%d\n",input[i].elg);
                    break;
                }
                if (i=n-1){
                    printf("No such student");
                }
            }
            break;
        case 's':
            for (int i=0;i<n;i++){
                printf("%s\t",input[i].ID);
                printf("%s\t",input[i].name);
                printf("%d\t",input[i].mtg);
                printf("%d\t",input[i].prgg);
                printf("%d\n",input[i].elg);
            }
            break;
        case 'd':
            for (int i=0;i<n;i++){
                printf("%s\t",input[i].ID);
                printf("%s\t",input[i].name);
                printf("%d\t",input[i].mtg);
                printf("%d\t",input[i].prgg);
                printf("%d\n",input[i].elg);
            }
            break;
        case 'a':
            for (int i=n-1;i>=0;i--){
                printf("%s\t",input[i].ID);
                printf("%s\t",input[i].name);
                printf("%d\t",input[i].mtg);
                printf("%d\t",input[i].prgg);
                printf("%d\n",input[i].elg);
            }
            break;
        case 'b':
            for (int i=0;i<n;i++){
                printf("%s\t",input[i].ID);
                printf("%f\n",input[i].avr);
            }
            break;
        case 'q':
            return 0;
        default:
        puts("Error");
            break;
        }
    }
}
