#include <Python.h>

/**
 * print_python_list - prints python list info
 * @p: PyObject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	PyObject *element;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Not a Python list\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("Size of the Python List = %ld\n", size);
	printf("Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

/**
 * print_python_bytes - prints python list info
 * @p: PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Not a Python bytes object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	printf("[.] bytes object info\n");
	printf("Size: %ld\n", size);
	printf("trying string: %s\n", PyUnicode_1BYTE_DATA(p));

	printf("first %ld bytes: ", size > 10 ? 10 : size);
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02hhx", ((char *)PyBytes_AS_STRING(p))[i]);
		if (i < (size > 10 ? 9 : size - 1))
			printf(" ");
	}
	printf("\n");
}
