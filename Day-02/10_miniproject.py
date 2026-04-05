print("🎓 Welcome to Smart Student Assistant")

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
mood = input("Enter your mood (happy/sad/tired): ").lower()
time = input("Enter time of day (morning/afternoon/night): ").lower()

# -------------------------------
# 1. Grade Evaluation (if-elif-else)
# -------------------------------
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print(f"\n📊 Grade: {grade}")

# -------------------------------
# 2. Nested if (performance advice)
# -------------------------------
if grade == "A":
    if mood == "happy":
        print("🔥 Keep going! You are doing excellent!")
    else:
        print("🙂 You are doing great, take some rest also.")
else:
    if marks < 50:
        print("⚠️ You need serious improvement!")
    else:
        print("👍 You can improve with practice.")

# -------------------------------
# 3. Logical Operators
# -------------------------------
if marks > 80 and mood == "happy":
    print("🎉 Perfect combo: High marks + Good mood!")
elif marks < 50 or mood == "tired":
    print("💤 You need rest and revision.")

# -------------------------------
# 4. Membership Operator
# -------------------------------
if mood in ["sad", "tired"]:
    print("💡 Suggestion: Take a short break or listen to music.")

# -------------------------------
# 5. Match Case (Main Decision System)
# -------------------------------
print("\n📌 Recommendation System:")

match time:
    case "morning":
        print("🌅 Best time to study tough subjects!")
        
        if marks < 60:
            print("📚 Focus on basics today.")
    
    case "afternoon":
        print("🌤️ Practice problems and revise.")
        
        if mood == "tired":
            print("😴 Take a power nap first.")
    
    case "night":
        print("🌙 Light study or revision recommended.")
        
        if marks > 80:
            print("✨ Try advanced problems!")
    
    case _:
        print("❓ Invalid time input")

# -------------------------------
# 6. Match Case with Multiple Conditions
# -------------------------------
print("\n🎯 Activity Suggestion:")

match mood:
    case "happy":
        print("🏃 Try learning something new!")
    
    case "sad":
        print("🎧 Listen to music + light study")
    
    case "tired":
        print("😴 Rest now, study later")
    
    case _:
        pass   # No actionn