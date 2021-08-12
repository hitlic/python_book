// 文件 average.c
double average(double * data, int n) {
    double sum = 0;
    for(int i=0; i < n; i++) {
        sum += data[i];
    }
    return sum / n;
}