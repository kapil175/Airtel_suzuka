import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock - Multiple Time Zones")
        self.root.geometry("600x400")
        self.root.configure(bg='#1a1a1a')
        
        # Define time zones to display
        self.time_zones = {
            'UTC': 'UTC',
            'IST (India)': 'Asia/Kolkata',
            'EST (US)': 'US/Eastern',
            'PST (US)': 'US/Pacific',
            'GMT (UK)': 'Europe/London',
            'JST (Japan)': 'Asia/Tokyo',
            'AEST (Australia)': 'Australia/Sydney'
        }
        
        self.clock_labels = {}
        self.setup_ui()
        self.update_time()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Title
        title_font = font.Font(family="Helvetica", size=20, weight="bold")
        title_label = tk.Label(
            self.root, 
            text="World Clock", 
            font=title_font, 
            bg='#1a1a1a', 
            fg='#00ff00'
        )
        title_label.pack(pady=20)
        
        # Create a frame to hold all clocks
        clock_frame = tk.Frame(self.root, bg='#1a1a1a')
        clock_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Create clock display for each timezone
        time_font = font.Font(family="Courier", size=14, weight="bold")
        label_font = font.Font(family="Helvetica", size=10)
        
        for tz_name, tz_code in self.time_zones.items():
            # Container frame for each timezone
            container = tk.Frame(clock_frame, bg='#2a2a2a', relief=tk.RAISED, bd=2)
            container.pack(fill=tk.X, pady=5, padx=5)
            
            # Timezone label
            tz_label = tk.Label(
                container, 
                text=tz_name, 
                font=label_font, 
                bg='#2a2a2a', 
                fg='#ffff00',
                width=20,
                anchor='w'
            )
            tz_label.pack(side=tk.LEFT, padx=10, pady=8)
            
            # Time display label
            time_label = tk.Label(
                container, 
                text="00:00:00", 
                font=time_font, 
                bg='#2a2a2a', 
                fg='#00ff00'
            )
            time_label.pack(side=tk.RIGHT, padx=10, pady=8)
            
            self.clock_labels[tz_code] = time_label
    
    def update_time(self):
        """Update the time display for all timezones"""
        for tz_code, label in self.clock_labels.items():
            try:
                # Get current time in the specified timezone
                tz = pytz.timezone(tz_code)
                current_time = datetime.now(tz)
                time_string = current_time.strftime("%H:%M:%S")
                label.config(text=time_string)
            except Exception as e:
                label.config(text=f"Error: {str(e)}")
        
        # Schedule the next update after 1000ms (1 second)
        self.root.after(1000, self.update_time)

def main():
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
