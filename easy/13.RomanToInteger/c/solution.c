int romanToInt(char *s)
{
    int val = 0, idx = 0, sum = 0, prev = 0;
    do
    {
        switch (*s)
        {
        case 'I':
            val = 1;
            break;
        case 'V':
            val = 5;
            break;
        case 'X':
            val = 10;
            break;
        case 'L':
            val = 50;
            break;
        case 'C':
            val = 100;
            break;
        case 'D':
            val = 500;
            break;
        case 'M':
            val = 1000;
            break;
        default:
            break;
        }
        if (idx++ > 0 && val > prev)
        {
            sum += val - 2 * prev;
        }
        else
        {
            sum += val;
        }
        prev = val;

    } while (*(++s));
    return sum;
}