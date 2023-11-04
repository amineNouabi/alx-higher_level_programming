#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: pointer to the head of the list
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev;
	listint_t *next;

	prev = 0;
	next = 0;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (prev);
}

/**
 * is_palindrome - checks if linkedlist is palindrome
 * @head: head of linked list
 *
 * Return: 1 if palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *cursor, *fast, *reversed_list;
	int is_palindrome = 1;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	cursor = slow = fast = *head;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast)
		slow = slow->next;

	reversed_list = reverse_listint(&slow);
	while (slow)
	{
		if (slow->n != cursor->n)
		{
			is_palindrome = 0;
			break;
		}
		slow = slow->next;
		cursor = cursor->next;
	}
	reverse_listint(&reversed_list);
	return (is_palindrome);
}
