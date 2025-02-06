import streamlit as st

# College Event Management System
events = {}

def add_event(event_name):
    if event_name not in events:
        events[event_name] = []

def add_participant(event_name, name, contact, department, status="Not Attended"):
    if event_name in events:
        events[event_name].append((name, contact, department, status))

def display_participants(event_name):
    return events.get(event_name, "Event not found.")

def search_participant(name):
    for event, participants in events.items():
        for participant in participants:
            if participant[0] == name:
                return {"Event": event, "Details": participant}
    return "Participant not found."

def mark_attendance(event_name, name, status):
    if event_name in events:
        for i, participant in enumerate(events[event_name]):
            if participant[0] == name:
                events[event_name][i] = (participant[0], participant[1], participant[2], status)
                return "Status updated."
    return "Event or participant not found."

def generate_summary():
    return {event: len(participants) for event, participants in events.items()}

# Streamlit UI
st.title("College Event Management System")

menu = ["Add Event", "Add Participant", "View Participants", "Search Participant", "Mark Attendance", "Event Summary"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Event":
    event_name = st.text_input("Enter Event Name")
    if st.button("Add Event"):
        add_event(event_name)
        st.success(f"Event '{event_name}' added successfully.")

elif choice == "Add Participant":
    event_name = st.selectbox("Select Event", list(events.keys()))
    name = st.text_input("Participant Name")
    contact = st.text_input("Contact Number")
    department = st.text_input("Department")
    if st.button("Add Participant"):
        add_participant(event_name, name, contact, department)
        st.success(f"Participant '{name}' added to '{event_name}'.")

elif choice == "View Participants":
    event_name = st.selectbox("Select Event", list(events.keys()))
    if st.button("Show Participants"):
        participants = display_participants(event_name)
        st.write(participants)

elif choice == "Search Participant":
    name = st.text_input("Enter Participant Name")
    if st.button("Search"):
        result = search_participant(name)
        st.write(result)

elif choice == "Mark Attendance":
    event_name = st.selectbox("Select Event", list(events.keys()))
    name = st.text_input("Enter Participant Name")
    status = st.selectbox("Select Status", ["Attended", "Not Attended"])
    if st.button("Update Attendance"):
        result = mark_attendance(event_name, name, status)
        st.success(result)

elif choice == "Event Summary":
    if st.button("Show Summary"):
        summary = generate_summary()
        st.write(summary)
