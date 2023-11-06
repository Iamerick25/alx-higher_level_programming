#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: points to beginning of the linked list to be checked
 * Return: 0 if list is not a palindrome, 1 if list is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j;
	int *lst;

	current = *head;
	if ((head == NULL) || (current == NULL))
		return (1);
	for (i = 1; current->next; i++)
		current = current->next;
	lst = malloc(sizeof(int) * i);
	if (lst == NULL)
		return (1);
	current = *head;
	for (j = 0; j < i; j++)
	{
		lst[j] = current->n;
		current = current->next;
	}
	for (j = 0; j < i ; j++)
	{
		if (lst[i - 1] != lst[j])
			return (0);
		i--;
	}
	return (1);
}
