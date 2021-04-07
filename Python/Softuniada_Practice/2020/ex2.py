size = int(input())

width = size
height = size + size // 2

for i in range(height):
    result = ''
    for j in range(width):
        isStripe = (i + j) % 4 == 0

        if isStripe:
            result += '#'

        else:
            result += '.'

    print(result)


# int size = int.Parse(Console.ReadLine());
#
#             int width = size;
#             int height = size + size / 2;
#
#             for (int i = 0; i < height; i++)
#             {
#                 for (int j = 0; j < width; j++)
#                 {
#                     bool isStripe = (j + i) % 4 == 0;
#
#                     if (isStripe)
#                     {
#                         Console.Write("#");
#                     }
#                     else
#                     {
#                         Console.Write(".");
#                     }
#                 }
#                 Console.WriteLine();
#             }