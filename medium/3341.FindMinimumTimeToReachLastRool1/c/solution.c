#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct heap Heap;
struct heap {
	uint8_t capacity;
	uint8_t size;
	uint32_t *arr;

	// methods
	void (*heapify)(Heap *self, uint8_t i, uint8_t size);
	void (*heappush)(Heap *self, uint32_t value);
	uint32_t (*heappop)(Heap *self);
};

void heapify(Heap *self, uint8_t i, uint8_t size)
{
	uint8_t largest = i;
	uint8_t left = 2 * i + 1;
	uint8_t right = 2 * i + 2;
	if (left < size && self->arr[left] > self->arr[largest]) {
		largest = left;
	}
	if (right < size && self->arr[right] > self->arr[largest]) {
		largest = right;
	}
	if (largest != i) {
		uint32_t temp = self->arr[i];
		self->arr[i] = self->arr[largest];
		self->arr[largest] = temp;
		heapify(self, largest, size);
	}
}

// Implementation of all the methods in Heap
void heappush(Heap *self, uint32_t value)
{
}
uint32_t heappop(Heap *self)
{
	uint32_t value = self->arr[0];
	self->arr[0] = self->arr[self->size - 1];
	self->size--;
	heapify(self->arr, 0, self->size);
	return value;
}
static int create_Heap(Heap **self, uint8_t capacity)
{
	*self = (Heap *)malloc(sizeof(Heap));
	if (*self == NULL) {
		return -1;
	}
	(*self)->capacity = capacity;
	(*self)->size = 0;
	(*self)->arr = (uint32_t *)malloc(capacity * sizeof(uint32_t));
	if ((*self)->arr == NULL) {
		free(*self);
		return -1;
	}
	(*self)->heapify = heapify;
	(*self)->heappush = heappush;
	(*self)->heappop = heappop;
	return 0;
}
