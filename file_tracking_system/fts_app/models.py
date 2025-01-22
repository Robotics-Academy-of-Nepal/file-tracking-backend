from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Static choices for Provinces (States) - 7 Provinces of Nepal
    PROVINCE_CHOICES = [
        ('Province 1', 'Province 1'),
        ('Province 2', 'Province 2'),
        ('Province 3', 'Province 3'),
        ('Province 4', 'Province 4'),
        ('Province 5', 'Province 5'),
        ('Province 6', 'Province 6'),
        ('Province 7', 'Province 7'),
    ]
    
    # These will be the dynamically filled fields based on selected province
    perm_state = models.CharField(max_length=255, choices=PROVINCE_CHOICES)
    perm_district = models.CharField(max_length=255)
    perm_municipality = models.CharField(max_length=255)
    perm_ward_no = models.CharField(max_length=255)
    
    temp_state = models.CharField(max_length=255, choices=PROVINCE_CHOICES)
    temp_district = models.CharField(max_length=255)
    temp_municipality = models.CharField(max_length=255)
    temp_ward_no = models.CharField(max_length=255)

    citizenship_id = models.CharField(max_length=255, unique=True)
    citizenship_date_of_issue = models.DateField()
    citizenship_district = models.CharField(max_length=255)
    citizenship_front_image = models.ImageField(upload_to='citizenship/')
    citizenship_back_image = models.ImageField(upload_to='citizenship/')
    
    home_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    date_joined = models.DateTimeField()
    recess_date = models.DateTimeField()
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    # Dynamic district and municipality choices based on the state
    def get_district_choices(self, state):
        # Province data with respective districts
        province_data = {
            "Province 1": ["Jhapa", "Morang", "Sunsari", "Bhojpur", "Ilam", "Khotang", "Okhaldhunga", "Panchthar", "Sankhuwasabha", "Solukhumbu", "Taplejung", "Terhathum", "Udayapur"],
            "Province 2": ["Saptari", "Dhanusha", "Mahottari", "Sarlahi", "Siraha", "Bara", "Parsa", "Rautahat", "Chhathapol"],
            "Province 3": ["Kathmandu", "Bhaktapur", "Lalitpur", "Kavrepalanchok", "Nuwakot", "Rasuwa", "Sindhuli", "Sindhupalchok", "Chitwan", "Makawanpur", "Bhaktapur", "Nawalparasi", "Tanahu"],
            "Province 4": ["Kaski", "Parbat", "Tanahun", "Gorkha", "Lamjung", "Manang", "Mustang", "Syangja", "Nawalparasi", "Syangja"],
            "Province 5": ["Rupandehi", "Kapilvastu", "Palpa", "Nawalparasi", "Arghakhanchi", "Rukum", "Salyan", "Dang", "Banke", "Bardiya"],
            "Province 6": ["Surkhet", "Dailekh", "Jajarkot", "Jumla", "Kalikot", "Mugu", "Humla", "Dolpa", "Rukum", "Salyan"],
            "Province 7": ["Kanchanpur", "Baitadi", "Darchula", "Achham", "Kailali", "Bajura", "Bajhang", "Dadeldhura", "Doti", "Dadeldhura"]
        }
        return province_data.get(state, [])

    def get_municipality_choices(self, state, district):
        # Expanded data for municipalities (to be filled with your data)
        district_municipality_data = {
            # Province 1
            "Jhapa": ["Birtamod", "Mechinagar", "Damak", "Kankai", "Shivasatakshi", "Sunsari", "Basantapur", "Arjundhara"],
            "Morang": ["Biratnagar", "Inaruwa", "Rangeli", "Madhyapur Thimi", "Pathari", "Katahari", "Dhanpalthana"],
            "Sunsari": ["Itahari", "Bharatpur", "Damak", "Bhanjanagar", "Sunsari", "Mahendranagar", "Kishannagar"],
            "Ilam": ["Ilam", "Pashupati", "Suryodaya", "Maihami", "Barshangia"],
            "Bhojpur": ["Bhojpur", "Aadhhar", "Aphun", "Tandi"],
            
            # Province 2
            "Saptari": ["Rajbiraj", "Kanchanpur", "Bardibas", "Saptakoshi", "Mahendra Nagar"],
            "Dhanusha": ["Janakpur", "Dhanushadham", "Chandrapur", "Aurahi"],
            "Mahottari": ["Jaleshwar", "Bhathabara", "Ramnagar", "Kanakpatti", "Hathura"],
            "Sarlahi": ["Madhavpur", "Sarlahi", "Hariharpur"],
            "Siraha": ["Lahan", "Dhangadhimai", "Karjanha", "Lohandigama"],
            "Bara": ["Parsa", "Birgunj", "Nawalpur", "Simraungadh"],
            "Parsa": ["Birgunj", "Bairgania", "Madhav Narayan", "Shivpur"],
            
            # Province 3
            "Kathmandu": ["Kathmandu", "Bhaktapur", "Lalitpur", "Chandragiri", "Kirtipur", "Boudha", "Patan"],
            "Bhaktapur": ["Bhaktapur", "Suryabinayak", "Madhyapur Thimi"],
            "Lalitpur": ["Lalitpur", "Godawari", "Mahankal", "Imadol"],
            "Kavrepalanchok": ["Dhulikhel", "Panauti", "Banepa", "Kavre"],
            "Nuwakot": ["Trisuli", "Bidur", "Taruka", "Ishwarpur"],
            "Rasuwa": ["Dhunche", "Kalika", "Ramche", "Kailash"],
            
            # Province 4
            "Kaski": ["Pokhara", "Lekhnath", "Machhapuchhre", "Syangja", "Ghorepani"],
            "Parbat": ["Jomsom", "Baglung", "Kahwang"],
            "Tanahun": ["Damauli", "Puranchaur", "Bhanu", "Besisahar"],
            "Gorkha": ["Gorkha", "Arughat", "Chhetrapati"],
            "Lamjung": ["Besisahar", "Bhanu", "Syangja"],
            
            # Province 5
            "Rupandehi": ["Butwal", "Bhanu", "Siddharthanagar", "Taulihawa"],
            "Kapilvastu": ["Taulihawa", "Parasi", "Khalwat"],
            "Palpa": ["Tansen", "Rani", "Lumbini"],
            "Nawalparasi": ["Ramgram", "Siddhartha", "Chandranigahapur"],
            "Arghakhanchi": ["Sandhikharka", "Panchanewan", "Bashidharam"],
            "Rukum": ["Rukumkot", "Rukum", "Ghorahi"],
            "Salyan": ["Salyan", "Tulasipur"],
            "Dang": ["Tulsipur", "Ghorahi", "Dangbhuli"],
            "Banke": ["Nepalgunj", "Kohalpur"],
            "Bardiya": ["Gulariya", "Rajapur", "Bardiya"],
            
            # Province 6
            "Surkhet": ["Birendranagar", "Karnali", "Manma"],
            "Dailekh": ["Dailekh", "Chaugan"],
            "Jajarkot": ["Jajarkot", "Chhidrapur"],
            "Jumla": ["Jumla", "Chandannath"],
            "Kalikot": ["Kalikot", "Khandachakra"],
            "Mugu": ["Mugu", "Gamgadhi"],
            "Humla": ["Simkot", "Humla"],
            "Dolpa": ["Dolpa", "Jajarkot"],
            "Rukum": ["Rukumkot", "Salyan"],
            
            # Province 7
            "Kanchanpur": ["Mahendranagar", "Bhimdutta", "Kanchanpur", "Gulariya"],
            "Baitadi": ["Baitadi", "Darchula"],
            "Darchula": ["Darchula", "Dugdiligad"],
            "Achham": ["Achham", "Mugu", "Khaptad"],
            "Kailali": ["Dhangadhi", "Tikapur", "Lamki", "Bajhang"],
            "Bajura": ["Bajura", "Sanphebagar"],
            "Bajhang": ["Bajhang", "Baitadi", "Chhetrapur"],
            "Dadeldhura": ["Dadeldhura", "Doti"],
            "Doti": ["Doti", "Dipayal"]
        }
        
        # Return the relevant municipalities based on district selection
        return district_municipality_data.get(district, [])


