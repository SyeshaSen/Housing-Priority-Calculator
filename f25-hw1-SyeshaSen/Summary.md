# SUMMARY TEMPLATE
Answer all the questions. Please put your answers *after* the italicized instructions.

## Scoring System Rationale  
*Explain how you decided on the point values for each criterion in your `HousingPriorityCalculator` class. Why these weights? How do they reflect the goals of fairness, simplicity, or rewarding effort? Be specific about your point values for:*
- *Class year (1=Freshman, 2=Sophomore, 3=Junior, 4=Senior) - how many points each?* I decided to give 10 points to freshman, 20 to sophomores, 30 to juniors, and 40 to seniors
- *Graduation status (True/False) - how many points?*   20 to those who are graduating this semester, and 10 to those who are not
- *Credits earned - points per credit or brackets?* points per credit (1 credit means 1 point)
- *Additional questions - what questions did you choose and how many points each?*

1. Are you older than 23 (y/n)? 
30 points for those who say yes, 10 for those who say no
2. Are you in the honors program? (y/n)
30 points for those who say yes, 10 for those who say no

*Also include your complete scoring breakdown here so TAs can verify your test calculations.*


[10 points]  
*Answer:*

10 points per year in college (freshman are 10, seniors are 40)
20 points to those graduating this semester, 10 to those who are not
1 point per credit
30 points to those who are older than 23, 10 to those who do not
30 points to those in honors, 10 to those who are not

---

## Citations 

### Who did you work with and how?   
*Discussing the assignment with people not on your team is fine as long as you don't share code.*   
*Please include any people or other sources who helped you, and any students whom you helped.*   
*For each source, make sure to include how they helped you (or how you helped them).*    

[1 point] 
* *"I had no idea how to approach Question 3 until classmate Alice Smith explained how I could break it down into separate functions."*   
* *"I showed Bob Lee my test-mocking approach for calculate_score; he gave me feedback on ordering the decorators."*   
* *If you did not talk to anybody about the assignment, please state that.*  

I was confused on github, and commands for checking status, and commiting and ensuring everything saves, and I asked Tiffany Uong for assistance on that. She taught me some new commands like git log, which helped me be positive that my commits were working
---  

### What resources did you use?   
*Please give specific URLs (not "Stack Overflow" or "Google") and state which ones were particularly helpful.*    

[1 point] 
* *https://docs.python.org/3/library/unittest.html – for learning about `unittest.mock.patch`.*   
* *https://realpython.com/python-mock-library/ – example patterns for mocking user input.*  

https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python - I used this to learn about While True loops, which helped me ask the user for input until they give a valid response

https://www.w3schools.com/python/python_dictionaries.asp - I used this to learn what dictionaries are in python. I implemented these in the additional questions function, and this really helped, as I had not used dictionaries before

---  

## Logistics 

### Did you successfully implement everything that was requested?   
*Answer "Yes", or state here which parts did not work or which tests did not pass. Be specific about any methods or test cases that are incomplete.*    

yes

These were the tests that were unable to pass, I am assuming this is due to the HousingQuestionAsker class not working. I did however implement this class and believe it is correct.

[1 point]   
*Answer:*  

### How long did the assignment take?   
*Rather than giving a range, if you are unsure, give the average of the range. Break down time spent on different parts (writing tests, implementation, debugging, documentation).*    

I took around 8 hours on this assignment.
It took me 1.5 hours to write the tests
3 hours to implement the functions
2.5 hours to debug
1 hour for documentation

[1 point]   
*Answer:*  

---  

## Reflections   
*Give **one or more paragraphs** reflecting on your experience with the assignment, including answers to all of these questions:*   
* What was the most difficult part of the assignment?   
* What was the most rewarding part of the assignment?   
* What did you learn from this assignment?
* Constructive and actionable suggestions for improving assignments, office hours, and lecture are always welcome.    

[8 points]   
*Answer:*  

I think that this assignment was difficult for me overall. Although I did think that I was able to come up with most of the logic, I struggled in navigating git hub, vs code, and pawtograder. I also did not know how to implement the functions using the correct syntax for various functions, and therefore had to try to learn it online. I think the most difficlut part was implementing tests, because I was able to do basic tests, but I felt really challenged by the type of tests in this program. I was confused what exactly to include in the parameters for assert.Equal. I also found the method with the dictionary really difficult, because I have never worked with dictionaries so I had to spend a lot of time trying to learn what it is, and how to used it in this case. The most rewarding part was learning more about git, and finally starting to be aquainted to the git commands and troubleshooting. I learnt about dictionaries a little bit because of this assignment, but I would love to go more in depth about them in class. I feel that it was difficult for me to go to office hours, because I had classes during that time, so having more drop in hours would definetly help. Also, I think that this homework was a great amount of workload, and it was quite advanced. I wish we would complete exercises in classes which are similar to this program, so I feel more prepared to tackle advanced homeworks.

---
