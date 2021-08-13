// 文件 distance.c
#include <math.h>

typedef struct Point {
    double x;
    double y;
} Point;

double distance(Point *p1, Point *p2) {
    return hypot(p1->x - p2->x, p1->y - p2->y);
}