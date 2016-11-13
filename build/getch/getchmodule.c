#include <Python.h>
#include <termios.h>
#include <unistd.h>
#include <stdio.h>

// THIS IS PYTHON 2

/* reads from keypress, doesn't echo */
int getch(void)
{
    struct termios oldattr, newattr;
    int ch;
    tcgetattr( STDIN_FILENO, &oldattr );
    newattr = oldattr;
    newattr.c_lflag &= ~( ICANON | ECHO );
    tcsetattr( STDIN_FILENO, TCSANOW, &newattr );
    ch = getchar();
    tcsetattr( STDIN_FILENO, TCSANOW, &oldattr );
    return ch;
}

/* reads from keypress, echoes */
int getche(void)
{
    struct termios oldattr, newattr;
    int ch;
    tcgetattr( STDIN_FILENO, &oldattr );
    newattr = oldattr;
    newattr.c_lflag &= ~( ICANON );
    tcsetattr( STDIN_FILENO, TCSANOW, &newattr );
    ch = getchar();
    tcsetattr( STDIN_FILENO, TCSANOW, &oldattr );
    return ch;
}

static PyObject *getch_getche(PyObject *self, PyObject *args)
{
	int ok = PyArg_ParseTuple(args, "");
	char c = getche();
	return PyUnicode_FromFormat("%c", c);
}

static PyObject *getch_getch(PyObject *self, PyObject *args)
{
	int ok = PyArg_ParseTuple(args, "");
	char c = getch();
	return PyUnicode_FromFormat("%c", c);
}

static PyMethodDef GetchMethods[] = {
	{"getch",  getch_getch, METH_VARARGS, "Reads a character from standard input, not echoing it."},
	{"getche", getch_getche, METH_VARARGS, "Reads a character from standard input, displaying it on the screen"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initgetch(void)
{
	(void) Py_InitModule("getch", GetchMethods);
}
