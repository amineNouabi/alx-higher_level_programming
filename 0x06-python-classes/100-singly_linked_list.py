#!/usr/bin/python3
"""This module defines a class SinglyLinkedList"""


class Node:
    """class Node that defines a node of a singly linked list

    Attributes:
            data (int): data of the node.
            next_node (Node): next node of the list.

    """

    def __init__(self, data, next_node=None):
        """ Init a new node

        Args:
            data (int): value of the node
            next_node (Node or None): Next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/Set Node's data"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/Set Node's next"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class that defines defines a singly linked list

    Attributes:
        head (Node): head of the linked list.
    """

    def __init__(self):
        """Init a new SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """Returns string respresentation of LinkedList"""
        seperator = "\n"

        str_rep = ""
        cursor = self.__head
        while cursor:
            if cursor.next_node is None:
                seperator = ""
            str_rep = "{}{}{}".format(str_rep, cursor.data, seperator)
            cursor = cursor.next_node
        return str_rep

    def sorted_insert(self, value):
        """ Insert new node in right place ascending order

        Args:
            value (int): data of new node
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        cursor = self.__head
        if cursor.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        while cursor:
            if cursor.next_node is None:
                cursor.next_node = new_node
                break
            if cursor.next_node.data >= value:
                new_node.next_node = cursor.next_node
                cursor.next_node = new_node
                break
            cursor = cursor.next_node
