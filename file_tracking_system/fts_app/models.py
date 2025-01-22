from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Loan(models.Model):
    Loan_Choices = [
        ('Home Loan', 'Home Loan'),
        ('Pregnancy Loan', 'Pregnancy Loan'),
        ('Other Loan', 'Other Loan'),
    ]
    
    loan_type = models.CharField(max_length=255, choices=Loan_Choices)
    name = models.CharField(max_length=255)
    interest_rate = models.FloatField()
    max_amount = models.FloatField()
    min_amount = models.FloatField()
    max_tenure = models.IntegerField()
    min_tenure = models.IntegerField()

    def __str__(self):
        return self.name

class Office(models.Model):
    position_category_choices = [
        ('Darbandi', 'Darbandi'),
        ('Kaaj', 'Kaaj'),
    ]

    duration = models.DurationField()
    office_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    position_category = models.CharField(max_length=255, choices=position_category_choices)

    def __str__(self):
        return self.name
    
class Awards(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='awards/')

    def __str__(self):
        return self.name
    
class Punishments(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file= models.FileField(upload_to='punishments/')

    def __str__(self):
        return self.name    
    
class Education(models.Model):
    Education_Choices = [
        ('SLC', 'SLC'),
        ('+2', '+2'),
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('PhD', 'PhD'),
    ]
    
    education_level = models.CharField(max_length=255, choices=Education_Choices)
    institution = models.CharField(max_length=255)
    board = models.CharField(max_length=255)
    percentage = models.FloatField()
    year = models.IntegerField()
    certificate = models.FileField(upload_to='education/')
    marksheets = models.FileField(upload_to='education/' , null=True, blank=True)


    def __str__(self):
        return self.institution

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

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

    position_category_choices = [
        ('Darbandi', 'Darbandi'),
        ('Kaaj', 'Kaaj'),
    ]

    BANK_CHOICES = [
        ('Nepal Bank Ltd.', 'Nepal Bank Ltd.'),
        ('Agriculture Development Bank Ltd.', 'Agriculture Development Bank Ltd.'),
        ('Nabil Bank Ltd.', 'Nabil Bank Ltd.'),
        ('Nepal Investment Bank Ltd.', 'Nepal Investment Bank Ltd.'),
        ('Standard Chartered Bank Nepal Ltd.', 'Standard Chartered Bank Nepal Ltd.'),
        ('Himalayan Bank Ltd.', 'Himalayan Bank Ltd.'),
        ('Nepal SBI Bank Ltd.', 'Nepal SBI Bank Ltd.'),
        ('Everest Bank Ltd.', 'Everest Bank Ltd.'),
        ('NIC ASIA Bank Ltd.', 'NIC ASIA Bank Ltd.'),
        ('Machhapuchchhre Bank Ltd.', 'Machhapuchchhre Bank Ltd.'),
        ('Kumari Bank Ltd.', 'Kumari Bank Ltd.'),
        ('Laxmi Bank Ltd.', 'Laxmi Bank Ltd.'),
        ('Siddhartha Bank Ltd.', 'Siddhartha Bank Ltd.'),
        ('Global IME Bank Ltd.', 'Global IME Bank Ltd.'),
        ('Citizens Bank International Ltd.', 'Citizens Bank International Ltd.'),
        ('Prime Commercial Bank Ltd.', 'Prime Commercial Bank Ltd.'),
        ('NMB Bank Ltd.', 'NMB Bank Ltd.'),
        ('Prabhu Bank Ltd.', 'Prabhu Bank Ltd.'),
        ('Sanima Bank Ltd.', 'Sanima Bank Ltd.'),
        ('Mahalaxmi Bikas Bank Ltd.', 'Mahalaxmi Bikas Bank Ltd.'),
        ('Narayani Development Bank Ltd.', 'Narayani Development Bank Ltd.'),
        ('Karnali Development Bank Ltd.', 'Karnali Development Bank Ltd.'),
        ('Shangrila Development Bank Ltd.', 'Shangrila Development Bank Ltd.'),
        ('Excel Development Bank Ltd.', 'Excel Development Bank Ltd.'),
        ('Miteri Development Bank Ltd.', 'Miteri Development Bank Ltd.'),
        ('Muktinath Bikas Bank Ltd.', 'Muktinath Bikas Bank Ltd.'),
        ('Garima Bikas Bank Ltd.', 'Garima Bikas Bank Ltd.'),
        ('Kamana Sewa Bikas Bank Ltd.', 'Kamana Sewa Bikas Bank Ltd.'),
        ('Corporate Development Bank Ltd.', 'Corporate Development Bank Ltd.'),
        ('Jyoti Bikas Bank Ltd.', 'Jyoti Bikas Bank Ltd.'),
        ('Shine Resunga Development Bank Ltd.', 'Shine Resunga Development Bank Ltd.'),
        ('Lumbini Bikas Bank Ltd.', 'Lumbini Bikas Bank Ltd.'),
        ('Sindhu Bikas Bank Ltd.', 'Sindhu Bikas Bank Ltd.'),
        ('Salapa Bikas Bank Ltd.', 'Salapa Bikas Bank Ltd.'),
        ('Saptakoshi Development Bank Ltd.', 'Saptakoshi Development Bank Ltd.'),
        ('Green Development Bank Ltd.', 'Green Development Bank Ltd.'),
        ('Nepal Finance Ltd.', 'Nepal Finance Ltd.'),
        ('Nepal Share Markets and Finance Ltd.', 'Nepal Share Markets and Finance Ltd.'),
        ('Gurkhas Finance Ltd.', 'Gurkhas Finance Ltd.'),
        ('Goodwill Finance Ltd.', 'Goodwill Finance Ltd.'),
        ('Shree Investment & Finance Co.', 'Shree Investment & Finance Co.'),
        ('Best Finance Ltd.', 'Best Finance Ltd.'),
        ('Capital Merchant Banking & Finance Ltd.', 'Capital Merchant Banking & Finance Ltd.'),
        ('Central Finance Ltd.', 'Central Finance Ltd.'),
        ('Gorkhas Finance Ltd.', 'Gorkhas Finance Ltd.'),
        ('Guheshwori Merchant Banking & Finance Ltd.', 'Guheshwori Merchant Banking & Finance Ltd.'),
        ('ICFC Finance Ltd.', 'ICFC Finance Ltd.'),
        ('Janaki Finance Co. Ltd.', 'Janaki Finance Co. Ltd.'),
        ('Manjushree Finance Ltd.', 'Manjushree Finance Ltd.'),
        ('Multipurpose Finance Co. Ltd.', 'Multipurpose Finance Co. Ltd.'),
        ('Pokhara Finance Ltd.', 'Pokhara Finance Ltd.'),
        ('Progressive Finance Ltd.', 'Progressive Finance Ltd.'),
        ('Reliance Finance Ltd.', 'Reliance Finance Ltd.'),
        ('Samridhhi Finance Co. Ltd.', 'Samridhhi Finance Co. Ltd.'),
        ('Shree Investment & Finance Co.', 'Shree Investment & Finance Co.'),
        ('Nepal Bangladesh Bank Ltd.', 'Nepal Bangladesh Bank Ltd.'),
        ('Nepal Bank Ltd.', 'Nepal Bank Ltd.'),
        ('Nepal Credit and Commerce Bank Ltd.', 'Nepal Credit and Commerce Bank Ltd.'),
        ('Nepal Finance Ltd.', 'Nepal Finance Ltd.'),
        ('Nepal Investment Bank Ltd.', 'Nepal Investment Bank Ltd.'),
        ('Nepal Rastra Bank', 'Nepal Rastra Bank'),
        ('Nepal SBI Bank Ltd.', 'Nepal SBI Bank Ltd.'),
        ('Nepal Grameen Bikas Bank Ltd.', 'Nepal Grameen Bikas Bank Ltd.'),
        ('Nepal Infrastructure Bank Ltd. (NIFRA)', 'Nepal Infrastructure Bank Ltd. (NIFRA)'),
        ('Nepal Rastra Bank', 'Nepal Rastra Bank'),
        ('Nepal SBI Bank Ltd.', 'Nepal SBI Bank Ltd.'),
        ('Nepal Grameen Bikas Bank Ltd.', 'Nepal Grameen Bikas Bank Ltd.'),
        ('Nepal Infrastructure Bank Ltd. (NIFRA)', 'Nepal Infrastructure Bank Ltd. (NIFRA)'),
        ('Nepal Rastra Bank', 'Nepal Rastra Bank'),
        ('Nepal SBI Bank Ltd.', 'Nepal SBI Bank Ltd.'),
        ('Nepal Grameen Bikas Bank Ltd.', 'Nepal Grameen Bikas Bank Ltd.'),
        ('Nepal Infrastructure Bank Ltd. (NIFRA)', 'Nepal Infrastructure Bank Ltd. (NIFRA)'),
    ]

    # These will be the dynamically filled fields based on selected province
    #Permanent Address
    perm_state = models.CharField(max_length=255, choices=PROVINCE_CHOICES)
    perm_district = models.CharField(max_length=255)
    perm_municipality = models.CharField(max_length=255)
    perm_ward_no = models.CharField(max_length=255)

    # Temporary Address
    temp_state = models.CharField(max_length=255, choices=PROVINCE_CHOICES)
    temp_district = models.CharField(max_length=255)
    temp_municipality = models.CharField(max_length=255)
    temp_ward_no = models.CharField(max_length=255)

    # Citizenship details
    citizenship_id = models.CharField(max_length=255, unique=True)
    citizenship_date_of_issue = models.DateField()
    citizenship_district = models.CharField(max_length=255)
    citizenship_front_image = models.ImageField(upload_to='citizenship/')
    citizenship_back_image = models.ImageField(upload_to='citizenship/')

   # Personal details 
    home_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    date_joined = models.DateTimeField()
    recess_date = models.DateTimeField()
    position = models.CharField(max_length=255)
    position_category = models.CharField(max_length=255, choices=position_category_choices)

    
    # Employee details
    empolyee_id = models.CharField(max_length=255)
    na_la_kos_no = models.CharField(max_length=255)
    accumulation_fund_no = models.CharField(max_length=255)
    bank_account_no = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255, choices=BANK_CHOICES)

    # Rewards and Punishments
    awards = models.ForeignKey(Awards, on_delete=models.CASCADE, null=True, blank=True)
    punishments = models.ForeignKey(Punishments, on_delete=models.CASCADE, null=True, blank=True)

    # Loan details
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True)

    # Eduction Details
    education = models.ForeignKey(Education, on_delete=models.CASCADE, null=True, blank=True)

    #Office Details


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


