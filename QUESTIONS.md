The following values were given in the example as expected inputs and output:

Input:
- 5 small dogs (`num_small`)
- 3 medium dogs (`num_medium`)
- 7 large dogs (`num_large`)
- 17 lbs of leftover food (`lbs_surplus`)

Output:
- 363.6 lbs of food to order (`food_amount`)

Based on this example, the calculation that returns this expected output is as follows:

`food_amount = (((num_small * 10) + (num_medium * 20) + (num_large * 30)) - lbs_surplus) * 1.2`

This is the calculation that I am using in my code so that it satisfies the example given. However, I don't think this is the best way to calculate how much food the shelter should order for the next month. With the above calculation, it may not always produce a 20% buffer that the problem calls out.

For example, if the shelter has only 10 small dogs, we assume that they will require 100 lbs of food (10 * 10). If we also say that the shelter had 100 lbs of leftover food from the previous month, then the calculation above would tell you not to order any food becuase (100 - 100) * 1.2 = 0. If you don't order any dog food, you will only have the minimum amount of food required for 10 small dogs, and you may run out of food in the next month. You won't end up with the 20% extra food in this case.

The calculation that I believe solves this problem better is as follows:

`food_amount = (((num_small * 10) + (num_medium * 20) + (num_large * 30)) * 1.2) - lbs_surplus`

By subtracting the leftover food amount after you account for the 20% extra food, you have a better chance of not running out of food for the next month.