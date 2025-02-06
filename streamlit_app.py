# College Event Management System

class CollegeEventManagement:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name):
        if event_name not in self.events:
            self.events[event_name] = []

    def add_participant(self, event_name, name, contact, department, status="Not Attended"):
        if event_name in self.events:
            self.events[event_name].append((name, contact, department, status))
        else:
            print("Event not found.")

    def display_participants(self, event_name):
        if event_name in self.events:
            return self.events[event_name]
        return "Event not found."

    def search_participant(self, name):
        for event, participants in self.events.items():
            for participant in participants:
                if participant[0] == name:
                    return {"Event": event, "Details": participant}
        return "Participant not found."

    def mark_attendance(self, event_name, name, status):
        if event_name in self.events:
            for i, participant in enumerate(self.events[event_name]):
                if participant[0] == name:
                    self.events[event_name][i] = (participant[0], participant[1], participant[2], status)
                    return "Status updated."
        return "Event or participant not found."

    def generate_summary(self):
        summary = {}
        for event, participants in self.events.items():
            summary[event] = len(participants)
        return summary

# Suggested website for UI: 
# Consider using Django or Flask for a web-based UI. 
# Alternatively, you can use Streamlit for a simple, interactive UI: https://streamlit.io/
