// 本实例仅用于解释，不可直接编译执行

// (1) Python参数列表包含两个整数
int x, y;
PyArg_ParseTuple(args, "ii", &x, &y);

// (2) Python参数列表包含三个参数，分别为字符串、整数和浮点数
const char* x;
int y;
double z;
PyArg_ParseTuple(args, "sid", &x, &y, &z)

// (2) Python参数为列表
PyObject *seq;
PyArg_ParseTuple(args, "O", &seq);
seq = PySequence_List(seq);
int seqlen = PySequence_Length(seq);