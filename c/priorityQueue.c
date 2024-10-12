#include <stdio.h>

int main() {
    int n, i, j, pos, temp;
    int bt[20], p[20], wt[20], tat[20], pr[20]; // burst time, process ID, waiting time, turnaround time, priority
    float avg_wt = 0, avg_tat = 0;

    printf("Enter the number of processes: ");
    scanf("%d", &n);

    printf("Enter Burst Time and Priority for each process:\n");
    for (i = 0; i < n; i++) {
        printf("Process[%d] Burst Time: ", i + 1);
        scanf("%d", &bt[i]);
        printf("Process[%d] Priority: ", i + 1);
        scanf("%d", &pr[i]);
        p[i] = i + 1; // storing process ID
    }

    // Sorting burst time, priority, and process ID based on priority using selection sort
    for (i = 0; i < n - 1; i++) {
        pos = i;
        for (j = i + 1; j < n; j++) {
            if (pr[j] < pr[pos]) { // priority-based sorting (lower number = higher priority)
                pos = j;
            }
        }

        // swapping priority
        temp = pr[i];
        pr[i] = pr[pos];
        pr[pos] = temp;

        // swapping burst time
        temp = bt[i];
        bt[i] = bt[pos];
        bt[pos] = temp;

        // swapping process ID
        temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;
    }

    wt[0] = 0; // waiting time for the first process is 0

    // calculating waiting time
    for (i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + bt[i - 1];
    }

    // calculating turnaround time and total waiting and turnaround time
    for (i = 0; i < n; i++) {
        tat[i] = wt[i] + bt[i];
        avg_wt += wt[i];
        avg_tat += tat[i];
    }

    avg_wt /= n;
    avg_tat /= n;

    printf("\nProcess\tPriority\tBurst Time\tWaiting Time\tTurnaround Time\n");
    for (i = 0; i < n; i++) {
        printf("P[%d]\t%d\t\t%d\t\t%d\t\t%d\n", p[i], pr[i], bt[i], wt[i], tat[i]);
    }

    printf("\nAverage Waiting Time: %.2f", avg_wt);
    printf("\nAverage Turnaround Time: %.2f\n", avg_tat);

    return 0;
}
