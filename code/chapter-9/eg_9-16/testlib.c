// 文件testlib.c
#include <math.h>
#include <testlib.h>

double add(double x, double y) {
    return x + y;
}

double average(double * data, int n) {
    double sum = 0;
    for(int i=0; i < n; i++) {
        sum += data[i];
    }
    return sum / n;
}

double distance(Point *p1, Point *p2) {
    return hypot(p1->x - p2->x, p1->y - p2->y);
}