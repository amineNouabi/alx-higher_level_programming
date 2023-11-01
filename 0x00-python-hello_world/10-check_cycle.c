#include "lists.h"

/**
 * check_cycle - Checks if linked list has cycle
 * @list: list's head
 * 
 * Return: 0 if has no cycle, 1 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *speed, *slow;

	if (!list || !list->next)
		return (0);

	speed = slow = list;

	while (speed && speed->next)
	{
		slow = slow->next;
		speed = speed->next->next;
		if (slow && slow == speed)
			return (1);
	}
	return (0);
}
