/* This program uses the selection sort algorithm to demonstrate
   many features of the CS language.
   You should get these output values (on separate lines):
      9  1480  16  17  20  20  32  55  57
*/


int i, I, largestIndex;
int listLength=9, list[50] = {'x', 'X', 20, 020, 0x20, 54, 17,
        87, 20, 1000};
int negOne, value;

void sortList()
{
    int largest;
    I = listLength - 1;
    while (0 < I) {
        largest = list[0];
        largestIndex = 0;
        i = 1;
        while (i <= I) {
            if(largest < list[i]) {
                largest = list[i];
                largestIndex = i;
            }
            i = i + 1;
        }
        if (largestIndex < I) {
            swap();
        }
        I = I + negOne;
    }
}

void swap()
{
    int temp;
    value = list[largestIndex] - list[I] / 2 + value;
    temp = list[I];
    list[I] = list[largestIndex];
    list[largestIndex] = temp;
}

void Main()
{
    value = 1234;
    negOne = (0xf423D - 03641077) / 2;  // (999997 - 999999) / 2
    sortList();
    write(listLength);
    write(value);
    i = 0;
    while (listLength > i) {
        if (list[i] < 50) {
           write(list[i]);
        }
        else {
           write(i + list.length);
           i = i + 1;
        }
        i = i - negOne;
    }
}

                                             