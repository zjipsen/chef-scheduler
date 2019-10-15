# chef-scheduler

My friends and I cook dinner almost every night. One of us cooks a main dish, and someone else cooks a side. 

A dynamic scheduling algorithm that takes into account people's differing availability, days that no one is around, and weights to favor people that haven't cooked in a while, is preferrable to signing people up for a consistent day of the week.

Pre-requisites:
pip install nexmo

Usage:
python main.py

Current behavior:
- Assign nights based on rudimentary weights system. The person who cooked the longest ago is preferred; if unavailable, the next least-recent chef is selected, and so on.
- The method "find_fair" introduces randomization of the order of chefs in the schedule as presented to the scheduling algorithm. It randomizes the input order, then attempts to find a fair schedule by running the algorithm. If it fails, it tries again.
- Filters:
	1. The same person cannot cook twice in one day.
	2. Roommates are not assigned the same day.
	3. No chef is assigned to cook two days in a row.
By uncommenting the other versions of the `roommates` and `yesterday` schedules, conditions 2. and 3. will be allowed, but not unless they are necessary to generate a viable schedule.

Future plans:
1. (DONE) Don't assign someone both a main and a side on the same day
2. (DONE) Assign weights 
3. (DONE) Obey limited schedules
4. (DONE) Test for constraints: no more than 1x per week, no less than 2x in a 3 week period
5. (DONE) Manually set 'since' variable to add data from previous weeks
6. (DONE) Add tests for fairness
7. (DONE) Send SMS via Nexmo API
8. (DONE) Allow starting algorithm on a Thursday (or any other day)
9. (DONE) Two cooks that live in the same apartment shouldn’t cook on the same day
10. Support people being gone on vacation
11. Send updates to one shared google calendar that everyone can see?
12. (DONE) Attempt to find a fair schedule by randomly shuffling chef entry order until one is found.
13. Use curl instead of nexmo python package in order to use python3
14. Clean up and separate logic
