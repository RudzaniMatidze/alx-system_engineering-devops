#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

/**
 * infinate_while - creates an infinate loop that makes pragram hang
 * Return: 0 (always)
 */
int infinate_while(void)
{
	while (1)
	{
		sleep(10);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: 0 (always)
 */
int main(void)
{
	int a;
	pid_t zombie;

	for (a = 0; a < 5; a++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinate_while();
	return (0);
}
