#include "lists.h"

/**
 * insert_node - insert a node in a sorted single linked list
 * @head: Head of Linked list
 * @number: number in new node.
 *
 * Return: List's new head or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = 0, *next = 0, *cursor = 0;

	if (!head)
		return (0);

	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = 0;


	if (!*head)
		return (*head = new_node);
	if ((*head)->n > new_node->n)
	{
		new_node->next = *head;
		return (*head = new_node);
	}

	cursor = *head;

	while (cursor)
	{
		if (!cursor->next)
		{
			cursor->next = new_node;
			break;
		}
		else if (cursor->next->n > new_node->n)
		{
			next = cursor->next;

			cursor->next = new_node;
			new_node->next = next;
			break;
		}
		cursor = cursor->next;
	}
	return (*head);
}
