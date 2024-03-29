#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked lists
 * @n: interger
 * @next: point to the next node.
 *
 * description: singly linked list node structures
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
}
listint_t;

site_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
#endif
