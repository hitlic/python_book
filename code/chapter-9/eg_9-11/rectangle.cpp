// 文件 rectangle.cpp
class Rectangle {
public:
    Rectangle(float, float);
    double area();
    double perimeter();
private:
    float w;
    float h;
};

Rectangle::Rectangle(float width, float height) {
    w = width;
    h = height;
}

double Rectangle::area() {
    return w * h;
}

double Rectangle::perimeter() {
    return 2 * w + 2 * h;
}

// 以C的方式编译如下函数
extern "C" {
    Rectangle *create(double width, double height) {
        return new Rectangle(width, height);
    }
    double area(Rectangle *rect) {
        return rect->area();
    }
    double perimeter(Rectangle *rect) {
        return rect->perimeter();
    }
}