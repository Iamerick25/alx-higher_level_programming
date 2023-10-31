#include "lists.h"
/**
 * insert_node - insert node in a sorted linked list
 * @head: the head of the linked list
 * @number: the int value to insert
 * Return: the new linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t **new;
	listint_t *tmp;

	tmp = malloc(sizeof(listint_t));
	new = malloc(sizeof(listint_t));
	if (tmp == NULL || new == NULL)
	{
		return (NULL);
	}
	tmp->n = number;
	tmp->next = NULL;
	if (*head == NULL)
	{
		*head = tmp;
	}
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
			{
				*new = current->next;
				tmp->next = current->next;
				(*new)->next = tmp;
				return (*head);
			}
			current = current->next;
		}
		current->next = tmp;
		return (*head);
	}
	return (NULL);
}
