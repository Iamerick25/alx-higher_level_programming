#include "lists.h"
/**
 * check_cycle - Check if a singly linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp1 = list;
	listint_t *tmp2 = list;

	if (list == NULL)
	{
		return (0);
	}

	while (tmp2 != NULL && tmp2->next != NULL)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;

		if (tmp1 == tmp2)
		{
			return (1);
		}
	}

	return (0);
}
