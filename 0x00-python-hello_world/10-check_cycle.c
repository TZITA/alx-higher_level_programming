#include "lists.h"

/**
 * check_list - checks if there is cycle or not
 * @list: list
 *
 * Return: Int.
 */

int check_cycle(listint_t *list)
{
	listint_t *a;
	listint_t *b;
	a = b = list;

	while(a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		
		if (a == b)
		{
			return (1);
		}
	}
	return (0);
}
