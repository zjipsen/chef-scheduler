# chef-scheduler

My friends and I cook dinner almost every night. One of us cooks a main dish, and someone else cooks a side. 

A dynamic scheduling algorithm that takes into account people's differing availability, days that no one is around, and weights to favor people that haven't cooked in a while, is preferrable to signing people up for a consistent day of the week.

Usage: 
python3 main.py

Current behavior:
Pick at random.

Future plans:
1. (DONE) Don't assign someone both a main and a side on the same day
2. (DONE) Assign weights 
3. Obey limited schedules
4. Obey constraints: 4 day cooking buffer, but must cook twice in a 2 week period
5. Maintain history and refer back
6. Add tests for fairness