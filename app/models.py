from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, photos
# ...
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(48), unique = True, index=True)
    email = db.Column(db.String(48),unique=True, index = True)
    hash_pass = db.Column(db.String(255)) 
    

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    blog_content = db.Column(db.String())
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    blog_pic = db.Column(db.String(255))
    photo_url = db.Column(db.String(500))

    comment = db.relationship('Comment', backref='blogs', lazy='dynamic')
    photo = db.relationship('Photo', backref='blog',lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.all()
        return blogs

    @classmethod
    def get_single_blog(cls, id):
        blog = Blog.query.filter_by(id=id).first()
        return blog


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    comment_content = db.Column(db.String())
    date_comment = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog_comments(cls, id):
        comments = Comment.query.filter_by(blog_id=id).order_by('-id').all()
        return comments

    @classmethod
    def get_single_comment(cls, id_blog, id):
        comment = Comment.query.filter_by(blog_id=id_blog, id=id).first()
        return comment


class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email_data = db.Column(db.String(255))

    def save_email(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def send_single_email(cls, id):
        email = Email.query.filter_by(id=id).first()
        return email


class Photo(db.Model):
    __tablename__='photos'
    id = db.Column(db.Integer,primary_key=True)
    photo_data = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
