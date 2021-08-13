// 文件testlib.h
#include <math.h>
extern double add(double, double);
extern double average(double *, int);
typedef struct Point {
    double x,y;
} Point;
extern double distance(Point *, Point *);