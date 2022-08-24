#include "lists.h"

/**
 * insert_node - entry point
 * @head: num1
 * @number: integer
 *
 * Return: head.
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (*head == NULL)
	{
		return (NULL);
	}
	
