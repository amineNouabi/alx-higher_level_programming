#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to the head of the list
 * @n: integer to add to the list
 *
 * Return: the address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node = 0;

	if (!head)
		return (0);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (0);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * is_palindrome - checks if linkedlist is palindrome
 * @head: head of linked list
 *
 * Return: 1 if palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *cursor, *reversed_list, *cursor_rev;
	int is_palindrome = 1;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	reversed_list = 0;
	cursor = *head;
	while (cursor)
	{
		add_nodeint(&reversed_list, cursor->n);
		cursor = cursor->next;
	}
	cursor = *head;
	cursor_rev = reversed_list;
	while (cursor && cursor_rev)
	{
		if (cursor->n != cursor_rev->n)
		{
			is_palindrome = 0;
			break;
		}
		cursor = cursor->next;
		cursor_rev = cursor_rev->next;
	}
	free_listint(reversed_list);
	return (is_palindrome);
}
