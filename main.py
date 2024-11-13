import streamlit as st

# App title and introduction
st.title("Supporting Your Health with Screen and Light Use")
st.write("""
This tool helps you understand your daily screen use habits, assesses your readiness to manage potential health impacts, and provides tailored resources and strategies to support you in a positive, non-judgmental way.
""")

# Section 1: Screen Use Habits Assessment
st.header("Step 1: Understand Your Screen Use Habits")

# Expanded questions in Step 1
# Question 1: Estimated hours of daily screen time
screen_time = st.selectbox("How many hours a day do you estimate you spend with screens?", 
                           options=["Less than 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "More than 8 hours"])

# Question 2: Devices frequently used
devices = st.multiselect("Which of these devices do you interact with daily? Select all that apply.",
                         options=["Smartphone", "Tablet", "Laptop", "Desktop Computer", "Television", "Smart Watch", "E-Reader", "Gaming Console", "Other"])

# Question 3: Awareness of potential health effects
awareness = st.radio("Are you aware of any potential health impacts from frequent screen use?",
                     options=["Yes, I am aware", "No, I am not aware", "I've heard some information"])

# Question 4: Experiencing any health effects
health_effects = st.multiselect("Do you experience any of the following? Select all that apply.",
                                options=["Difficulty sleeping", "Headaches", "Eye strain", "Neck or shoulder pain", "Anxiety", "Irritability", "None of these"])

# Question 5: Frequency of device use throughout the day
device_frequency = st.selectbox("How often do you check or use your devices throughout the day?",
                                options=["Rarely", "A few times a day", "Every hour", "Frequently (every 30 minutes)", "Constantly"])

# Question 6: Location of device use
location_use = st.multiselect("Where do you primarily use screens? Select all that apply.",
                              options=["Home", "Workplace", "School", "Public transit", "Outdoors", "Other"])

# Question 7: Frequency of device use in bed
device_in_bed = st.radio("Do you use your devices in bed?",
                         options=["Never", "Occasionally", "Frequently", "Constantly"])

# Question 8: Adjustments to minimize strain
adjustments = st.radio("Do you take any steps to reduce strain (e.g., adjusting brightness, taking breaks)?",
                       options=["Yes, regularly", "Sometimes", "No"])

# Calculate the initial Screen Use Score
score = 0
if screen_time == "Less than 2 hours":
    score += 10
elif screen_time == "2-4 hours":
    score += 20
elif screen_time == "4-6 hours":
    score += 40
elif screen_time == "6-8 hours":
    score += 60
else:
    score += 80
score += len(devices) * 5
if awareness != "No, I am not aware":
    score += 10
score += len(health_effects) * 5
if device_frequency == "Frequently (every 30 minutes)" or device_frequency == "Constantly":
    score += 20
if device_in_bed in ["Frequently", "Constantly"]:
    score += 15
if adjustments == "Yes, regularly":
    score -= 10
score = min(score, 100)

# Display score and provide initial feedback
st.write("### Your Screen Use Score: ", score, "%")
if score > 50:
    st.write("Your screen use is above average. Below, we’ll provide personalized tips to help balance screen habits in a supportive way.")

# Section 2: Readiness Assessment
st.header("Step 2: Assess Your Readiness to Make Changes")

# Additional Readiness Questions
# Question 1: Familiarity with potential health impacts
readiness_awareness = st.radio("How familiar are you with potential health impacts of prolonged screen and light use?",
                               options=["Not familiar", "Somewhat familiar", "Quite familiar"])

# Question 2: Desire to learn more or make changes
readiness_desire = st.radio("How interested are you in learning more or taking steps to mitigate any health impacts?",
                            options=["Not interested", "Considering it", "Would like to but unsure how", "Actively taking steps"])

# Question 3: Actions taken to reduce health impacts
readiness_actions_taken = st.radio("Have you already taken any steps to reduce potential health impacts of screen and light use?",
                                   options=["None", "Thinking about it", "Some steps", "Consistent changes"])

# Question 4: Barriers to reducing screen time
barriers = st.multiselect("What barriers prevent you from reducing screen time? Select all that apply.",
                          options=["Work or study requirements", "Entertainment", "Communication needs", "Habits or routines", "Lack of awareness", "Cost of alternatives", "Other"])

# Determine readiness stage based on responses
if readiness_awareness == "Not familiar" and readiness_desire == "Not interested":
    stage = "New to the Topic"
elif readiness_awareness == "Somewhat familiar" and readiness_desire in ["Considering it", "Would like to but unsure how"]:
    stage = "Curious but Unsure"
elif readiness_awareness == "Quite familiar" and readiness_desire == "Would like to but unsure how":
    stage = "Aware but Seeking Guidance"
elif readiness_awareness == "Quite familiar" and readiness_desire == "Actively taking steps" and readiness_actions_taken in ["Some steps", "Consistent changes"]:
    stage = "Taking Positive Steps"
else:
    stage = "Balanced and Knowledgeable"

# Section 3: Personalized Support Based on Readiness Stage
st.header("Step 3: Your Personalized Support and Recommendations")
st.write(f"Based on your responses, you are in the **{stage}** stage.")

# Expanded support and resources based on stage
if stage == "New to the Topic":
    st.write("""
    **You’re just starting to learn about screen-related health impacts.** Here’s some helpful information to get started:
    - **Potential Effects**: Extended screen use can affect sleep, cause eye strain, headaches, and contribute to stress or irritability.
    - **Simple Tips**:
        - Try the 20-20-20 rule: Look 20 feet away for 20 seconds every 20 minutes.
        - Take short breaks every hour to move around and refresh your mind.
        - Adjust screen brightness to match the lighting around you.
    - **Resources**:
        - [National Sleep Foundation](https://www.sleepfoundation.org)
        - [American Optometric Association](https://www.aoa.org)
        - [Calm Meditation App](https://www.calm.com) - for short, stress-reducing breaks
    """)

elif stage == "Curious but Unsure":
    st.write("""
    **You’re interested in making changes but may need guidance on where to start.** Here are some strategies to help:
    - **Night Mode or Blue Light Filters**: Enable these on devices to reduce eye strain.
    - **Limit Evening Screen Use**: Reducing screen time before bed can help improve sleep.
    - **Take Breaks**: Stand up, stretch, or do eye exercises to alleviate strain.
    - **Mindful Routines**: Try setting a limit on evening screen use with a relaxing pre-sleep routine.
    - **Resources**:
        - [Flux (Blue Light Filter)](https://justgetflux.com)
        - [Eye Exercises](https://www.allaboutvision.com/conditions/eye-exercises/)
    """)

elif stage == "Aware but Seeking Guidance":
    st.write("""
    **You’re aware of screen-related health impacts and want to make changes.** Here are ways to start:
    - **Invest in Blue Light Glasses**: These glasses can help reduce eye strain if you work late.
    - **Adjust Room Lighting**: Use warmer lights in the evening and maximize daylight exposure during the day.
    - **Screen-Free Breaks**: Practice screen-free activities like stretching, deep breathing, or walking to reduce tension.
    - **Resources and Suggestions**:
        - [Zenni Blue Light Glasses](https://www.zennioptical.com/b/blue-light-glasses)
        - [Sleep Foundation Tips for Healthy Sleep](https://www.sleepfoundation.org)
    """)

elif stage == "Taking Positive Steps":
    st.write("""
    **You’re already taking positive steps!** Here’s some additional guidance:
    - **Add Eye and Neck Exercises**: Simple stretches can help alleviate neck and eye strain.
    - **Control Ambient Lighting**: Use adjustable lighting that simulates natural light cycles.
    - **Mindful Tech Use**: Schedule tech-free time for relaxation or hobbies.
    - **Resources**:
        - [American Academy of Ophthalmology Exercises](https://www.aao.org/eye-health/tips-prevention/computer-usage)
        - [Philips Hue Adjustable Lighting](https://www.philips-hue.com)
    """)

elif stage == "Balanced and Knowledgeable":
    st.write("""
    **You’re well-informed and have created a balanced routine.** Here are a few advanced tips:
    - **Mindfulness Breaks**: Incorporate deep breathing or mindfulness

 exercises to maintain focus.
    - **Monitor Screen Settings**: Regularly check device settings to ensure minimal strain.
    - **Ongoing Support**: Keep tracking your habits and adjust as needed to maintain a balanced approach.
    - **Resources**:
        - [Headspace](https://www.headspace.com) for mindfulness practices.
        - [Sleepio](https://www.sleepio.com) for sleep tracking and improvement.
    """)

st.write("Thank you for using this app! We hope it provides a supportive way to enhance your screen habits without stress.")
