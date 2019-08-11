from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dish(db.Model):
 #   __tablename__ = 'dishes'
# table name is automatically set for you unless overridden. It’s derived from the class name converted to lowercase and with “CamelCase” converted to “camel_case”. 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False) #  string is for short texts (when storing single list boards) & text used for large blocks of text (matrix boards)
    description = db.Column(db.Text)
  #  picture = db.Column(db.String(15))
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(15), nullable=False)


#Defining how our data will be represented
 #   def __repr__(self):
  #      return "<Solution(id='%d', board='%s', n='%d', total='%d')>"\
   #         .format(self.id, self.board, self.n, self.total)
