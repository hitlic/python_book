// 文件testlib_ext.c
#include "Python.h"
#include "testlib.h"

static PyObject *ext_add(PyObject *self, PyObject *args){
    double x, y, result;

    // 参数解析
    if (!PyArg_ParseTuple(args, "dd", &x, &y))
        return NULL;

    result = add(x, y);
    return Py_BuildValue("d", result);
}

static PyObject *ext_average(PyObject *self, PyObject *args)
{
    PyObject *value_list;
    double *value_array, result;
    int list_len;
    
    // 参数解析
    if (!PyArg_ParseTuple(args, "O", &value_list))
        return 0;

    // 将Python序列复制至double数组
    list_len = PySequence_Length(value_list);
    value_array = malloc(list_len * sizeof(double)); // 为数组分配存储空间
    for (int i = 0; i < list_len; i++) {
        PyObject *value = PyList_GetItem(value_list, i); // 获取列表元素
        // 将Python float类型转为C double类型
        value_array[i] = PyFloat_AsDouble(value);
    }

    Py_DECREF(value_list);  // 释放Python列表
    result = average(value_array, list_len);  // 调用average函数
    free(value_array);//释放数组
    return Py_BuildValue("d", result);
}

// Point 对象的析构函数
static void point_destructor(PyObject *obj) {
    free(PyCapsule_GetPointer(obj, "Point"));
}

static PyObject *ext_Point(PyObject *self, PyObject *args) {
    Point *point;
    double x, y;
    if (!PyArg_ParseTuple(args, "dd", &x, &y))
        return NULL;

    // 定义结构体
    point = (Point *)malloc(sizeof(Point));
    point->x = x;
    point->y = y;

    // 将结构体转换为PyCapsule类型，并指定PyCapsule的析构函数
    return PyCapsule_New(point, "Point", point_destructor);
}

static PyObject *ext_distance(PyObject *self, PyObject *args){
    Point *p1, *p2;
    PyObject *py_p1, *py_p2;
    double result;
    if (!PyArg_ParseTuple(args, "OO", &py_p1, &py_p2))
        return NULL;

    // 提取capsule中的指针
    p1 = (Point *)PyCapsule_GetPointer(py_p1, "Point");
    p2 = (Point *)PyCapsule_GetPointer(py_p2, "Point");

    result = distance(p1, p2);
    return Py_BuildValue("d", result);
}

// 模块函数列表
static PyMethodDef methods[] = {
    {"add", ext_add, METH_VARARGS, "add two values"},
    {"average", ext_average, METH_VARARGS, "average a list of values"},
    {"distance", ext_distance, METH_VARARGS, "distance between points"},
    {"Point", ext_Point, METH_VARARGS, "create a point"},
    {NULL, NULL, 0, NULL}};

// 模块配置信息
static struct PyModuleDef module_config = {
    PyModuleDef_HEAD_INIT,
    "testlib",        // 模块名
    "A lib for test", // 模块文档字符串
    -1,               // 解释器状态大小，-1表示用全局变量保存状态
    methods           // 函数列表
};

// 模块初始化函数
PyMODINIT_FUNC PyInit_testlib(void){
    return PyModule_Create(&module_config);
}