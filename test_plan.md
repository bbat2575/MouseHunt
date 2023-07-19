Author: Bassam Batch
SID: 310229251
Unikey: bbat2575



**Test Cases**
Table 1. Summary of test cases for `buy_cheese` function in `shop.py`. 
| Test ID | Description                   | Inputs     | Expected Output                    | Status  |
| ------- | ----------------------------- | ---------- | ---------------------------------- | ------- |
| 01      | buy cheddar - Positive Case.  | cheddar 2  | Successfully purchase 2 cheddar.   | Pass    |
| 02      | buy swiss - Positive Case.    | swiss 1    | Successfully purchase 1 swiss.     | Pass    |
| 03      | buy heaps - Negative Case.    | cheddar 99 | Insufficient gold.                 | Pass    |
| 04      | buy brie - Negative Case.     | brie 3     | We don't sell brie!                | Pass    |
| 05      | empty strings - Edge Case.    | [] []      | We don't sell []!                  | Pass    |
| 06      | weird quantity - Edge Case.   | cheddar 0A | Invalid quantity.                  | Pass    |


Table 2. Summary of test cases for `change_cheese` function in `game.py`.
| Test ID | Description                   | Inputs     | Expected Output                    | Status  |
| ------- | ----------------------------- | ---------- | ---------------------------------- | ------- |
| 01      | marble - Positive Case.       | marble     | Out of cheese!                     | Pass    |
| 02      | back - Positive Case.         | back       | What do ye want to do now, Hunter Bob?| Pass    |
| 03      | parmesan - Negative Case.     | parmesan   | No such cheese!                    | Pass    |
| 04      | shout marble - Negative Case. | MARBLE     | Out of cheese!                     | Pass    |
| 05      | tab escape - Edge Case.       | cheddar\t  | No such cheese!                    | Pass    |
| 06      | open/close str - Edge Case.   | "cheddar"  | No such cheese!                    | Pass    |

