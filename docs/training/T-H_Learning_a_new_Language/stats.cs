public class Stats {
    public static double Average(List<int> numbers) {
        double total = 0;
        foreach (var number in numbers) {
            total += number;
        }
        var avg = total / numbers.Count;
        return avg;
    }

    public static void Main()
    {
        var my_numbers = new List<int> {3,1,6,3,5,4,6,2};
        var my_avg = Stats.Average(my_numbers);
        Console.WriteLine($"Average = {my_avg}");
    }
}