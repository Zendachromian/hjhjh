from database import db 

class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'sponsor', 'influencer'
    profile = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return f"Category('{self.name}')"

class Sponsor(db.Model):
    """Sponsor model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(120))
    industry = db.Column(db.String(120))
    budget = db.Column(db.Integer)
    campaigns = db.relationship('Campaign', backref='sponsor', lazy=True)
    user = db.relationship('User', backref='sponsor', lazy=True)

    def __repr__(self):
        return f"Sponsor('{self.company_name}', '{self.industry}')"

class Influencer(db.Model):
    """Influencer model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120))
    category = db.Column(db.String(120))
    niche = db.Column(db.String(120))
    reach = db.Column(db.Integer)
    ad_requests = db.relationship('AdRequest', backref='influencer', lazy=True)
    user = db.relationship('User', backref='influencer', lazy=True)

    def __repr__(self):
        return f"Influencer('{self.name}', '{self.category}')"

class Campaign(db.Model):
    """Campaign model"""
    id = db.Column(db.Integer, primary_key=True)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.id'), nullable=False)
    name = db.Column(db.String(120))
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    budget = db.Column(db.Integer)
    visibility = db.Column(db.String(10))  # 'public' or 'private'
    goals = db.Column(db.Text)
    ad_requests = db.relationship('AdRequest', backref='campaign', lazy=True)

    def __repr__(self):
        return f"Campaign('{self.name}', '{self.sponsor_id}')"

class AdRequest(db.Model):
    """Ad request model"""
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.id'), nullable=False)
    messages = db.Column(db.Text)
    requirements = db.Column(db.Text)
    payment_amount = db.Column(db.Integer)
    status = db.Column(db.String(20))  # 'pending', 'accepted', 'ejected'

    def __repr__(self):
        return f"AdRequest('{self.campaign_id}', '{self.influencer_id}')"
    
