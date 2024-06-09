#include <stdbool.h>
#include <stdio.h>

void rotor_sim(
    int *p_starter,
    int len_starter,
    int rotor_size,
    int rotors_max_num,
    void (*p_turn_func)(int *, int, char),
    void (*p_append_func)(int *, int, char),
    void (*p_completion_func)(int *, int, char))
{
    // Initialize and populate ROTORS with the starter values if present
    int ROTORS[rotors_max_num];
    ROTORS[0] = 0;
    int LEN_ROTORS = 1;

    if (len_starter > 0)
    {
        LEN_ROTORS = 0;
        for (int i = 0; i < len_starter; i++)
        {
            ROTORS[i] = *(p_starter + i);
            LEN_ROTORS++;
        }
    }

    // Where the magic happens
    while (LEN_ROTORS <= rotors_max_num)
    {
        (*p_turn_func)(ROTORS, LEN_ROTORS, '\r');

        // Turn base rotor
        ROTORS[0]++;
        ROTORS[0] %= rotor_size;

        // Turn other rotors up the chain
        bool add_rotor_flag = false;
        for (int i = 0; i < LEN_ROTORS; i++)
        {
            if (ROTORS[i] != 0)
            {
                add_rotor_flag = false;
                break;
            }

            if (LEN_ROTORS > 1 && (i < LEN_ROTORS - 1))
            {
                ROTORS[i + 1]++;
                ROTORS[i + 1] %= rotor_size;
            }

            if (i == LEN_ROTORS - 1)
                if (ROTORS[i] == 0)
                    add_rotor_flag = true;
        }

        // Append rotor
        if (add_rotor_flag)
        {
            ROTORS[LEN_ROTORS] = 0;
            LEN_ROTORS++;
            (*p_append_func)(ROTORS, LEN_ROTORS, '\n');
        }
    }

    (*p_completion_func)(ROTORS, LEN_ROTORS, '\n');
}

void print_breaker_array(
    int *p_breaker_array,
    int len_breaker_array,
    char next_line)
{
}

void print_after_completion(
    int *p_breaker_array,
    int len_breaker_array,
    char next_line)
{
    printf("C ROTOR SIMULATOR \n");
    printf("rotors: ");
    for (int i = 0; i < len_breaker_array; i++)
    {
        printf("%d ", *(p_breaker_array + i));
        if (i == len_breaker_array - 1)
            printf("%c", next_line);
    }
}

int main()
{
    int starter[3] = {0};
    int starter_len = sizeof(starter) / sizeof(starter[0]);

    rotor_sim(
        starter,
        starter_len,
        10,
        7,
        &print_breaker_array,
        &print_breaker_array,
        &print_after_completion);
    return 0;
}
