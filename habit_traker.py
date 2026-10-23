habit={}

print('''welcome to habit traker
What do you want to do
1.Add a habit
2.View all habits
3.Mark a habit as completed
4.See your progress
5.Exit the program''')

def add_habit():
    habit_name = input("Enter the name of the habit: ").lower()
    habit[habit_name] = False
    print(f"Habit '{habit_name}' added successfully!")
    return

def view_habits():
 if habit=={}:
    print("No habits found.")
    return
 else:
    num=1
    for habit_name in habit:
       print(f"your habits are-->".title())
       print(f"{num}.{habit_name}")
       num+=1
    return

def mark_habit():
   user_1=input("enter the name of the habit you want to mark ac completed->\n".title()).lower()
   if habit=={}:
       print("No habits found.")
       return
   else:    
       if user_1 not in habit:
         print("no such habit found!".title())
         return
       else:
          habit[user_1]=True
          print("your habit has been marked as completed!".title())
          return

def progress():
    if habit=={}:
          print("No habits found.")
          return
    else:
       completed_habit=0
       for key in habit.values():
          if key==True:
             completed_habit+=1
    progress1=(completed_habit/len(habit))*100
    print(f"your progress is:{progress1}%")
    return

#logic


def main():
   while True:
      user_2=input("what do you want to do-->\n")

      if user_2=="1":
         add_habit()
      elif user_2=="2":
         view_habits()
      elif user_2=="3":
         mark_habit()
      elif user_2=="4":
         progress()
      elif user_2=="5":
         break
      else:
         continue

main()