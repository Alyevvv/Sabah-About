from datetime import datetime
from sabah import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    type = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"User('{self.email}')"



class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    type = db.Column(db.Integer, default=1)
      
    def  __repr__(self):
        return f"Blog('{self.title}', '{self.add_date}')"




class Slider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Slider('{self.image}', '{self.title}')"






#In the Future

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text= db.Column(db.Text, nullable=False)
    credit_count= db.Column(db.Integer, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('Faculty.id'), nullable=False)


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Sting(255), nullable=False)
    text = db.Column(db.Text, nullable=False)


class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    


class Teachers_courses(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     teacher_id = db.Column(db.Integer, db.ForeignKey('Faculty.id'), nullable=False)
     course_id =  db.Column(db.Integer, db.ForeignKey('Courses.id'), nullable=False)



class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('Faculty.id'))



