#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Checks if list is palindrome
 * @head: Linked list
 *
 * Return: 1 if true or 0 if false.
 */
int is_palindrome(listint_t **head)
{
	if (*head != NULL)
	{
		return (1);
	}
	else
	{
		return (0);
	}	
}
