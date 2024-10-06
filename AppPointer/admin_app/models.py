from django.db import models
import re

APP_CATEGORIES = [
    ('AC', 'App Category'),
    ('SN', 'Social Networking'),
    ('ENT', 'Entertainment'),
    ('PROD', 'Productivity'),
    ('GAME', 'Games'),
    ('HF', 'Health & Fitness'),
    ('EDU', 'Education'),
    ('LIFE', 'Lifestyle'),
    ('FIN', 'Finance'),
    ('TRV', 'Travel'),
    ('SHOP', 'Shopping'),
    ('FD', 'Food & Drink'),
    ('MA', 'Music & Audio'),
    ('PV', 'Photo & Video'),
    ('NM', 'News & Magazines'),
    ('BUS', 'Business'),
    ('COM', 'Communication'),
    ('BR', 'Books & Reference'),
    ('MN', 'Maps & Navigation'),
    ('WE', 'Weather'),
    ('MED', 'Medical'),
    ('SP', 'Sports'),
    ('TU', 'Tools & Utilities'),
    ('DAT', 'Dating'),
    ('PAR', 'Parenting'),
    ('BEA', 'Beauty'),
    ('AD', 'Art & Design'),
    ('HH', 'House & Home'),
    ('EVT', 'Events'),
    ('AV', 'Auto & Vehicles'),
    ('PER', 'Personalization'),
    ('COMIC', 'Comics'),
]

APP_SUBCATEGORIES = [
    ("ASC", "App  Sub Category"),
    ("ACT", "Action"),
    ("ADV", "Adventure"),
    ("PUZ", "Puzzle"),
    ("STR", "Strategy"),
    ("ARC", "Arcade"),
    ("SIM", "Simulation"),
    ("SPR", "Sports"),
    ("RPG", "Role Playing"),
    
    ("WKT", "Workout"),
    ("MED", "Meditation"),
    ("NUT", "Nutrition"),
    ("YOG", "Yoga"),
    ("RUN", "Running"),
    ("CYC", "Cycling"),
    
    ("LAN", "Language Learning"),
    ("KID", "Kids"),
    ("CRS", "Courses"),
    ("STT", "Study Tools"),
    ("MTH", "Math"),
    ("SCI", "Science"),
    
    ("MUS", "Music Streaming"),
    ("POD", "Podcasts"),
    ("PLY", "Music Player"),
    ("AUD", "Audio Books"),
    
    ("PED", "Photo Editing"),
    ("VED", "Video Editing"),
    ("CAM", "Camera"),
    ("GIF", "GIF Makers"),
    
    ("PFI", "Personal Finance"),
    ("INV", "Investing"),
    ("BAN", "Banking"),
    ("CRY", "Cryptocurrency"),
    
    ("SHO", "Shopping"),
    ("FDK", "Food & Drink"),
    ("DAT", "Dating"),
    ("BEA", "Beauty"),
    ("HOM", "Home Decor"),
    
    ("TCB", "Team Collaboration"),
    ("CRM", "CRM"),
    ("ACC", "Accounting"),
    ("PMT", "Project Management"),
    ("IMN", "Inventory Management"),
    
    ("MAP", "Maps"),
    ("TRA", "Transportation"),
    ("HOT", "Hotels"),
    ("FLI", "Flights"),
    ("LEX", "Local Experiences"),
    
    ("LVS", "Live Scores"),
    ("NEW", "News"),
    ("FAN", "Fantasy Sports"),
    ("SPS", "Sports Streaming")
]

def slugify(val):
    return re.sub(r'[\s\W-]+', '-', re.sub(r'&', '-and-', val.strip().lower()))


class Application(models.Model):
    app_name = models.CharField(max_length=100, unique=True)
    app_link = models.CharField(max_length=200)
    app_slug = models.CharField(max_length=300)
    app_logo = models.ImageField( default='app_logos/default.png')
    app_category = models.CharField(max_length=30,choices=APP_CATEGORIES, default='AC')
    app_subcategories  =models.CharField(max_length=30, choices=APP_SUBCATEGORIES, default='ASC')
    app_points = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.app_link.startswith('http'):
            self.app_link = "http://" + self.app_link
        if not self.app_slug:
            self.app_slug = slugify(self.app_name)
        super().save(*args, **kwargs)

