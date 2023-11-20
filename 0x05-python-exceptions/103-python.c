#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *elem;

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		elem = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, elem->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python Bytes = %ld\n", size);
	printf("[*] First 10 bytes: ");

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx ", ((PyBytesObject *)p)->ob_sval[i]);
	}
	printf("\n");
}

/**
 * print_python_float - prints some basic info about Python float
 * @p: PyObject
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("[*] Python float = %f\n", ((PyFloatObject *)p)->ob_fval);
}
