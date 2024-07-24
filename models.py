# Description: This file contains the database models for the application.
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from config import load_config

# Import configurations
config = load_config()

# Create the engine
connection_str = f"postgresql://{config['user']}@{config['host']}:{config['port']}/{config['database']}"
engine = create_engine(connection_str)

# Check if the connection is successful
try:
    with engine.connect() as connection:
        print("Connection successful")
except Exception as error:
    print(f"Connection failed: {error}")

# Create the session and base
Session = sessionmaker(bind=engine)
base = declarative_base()


# Create the models
class Plant(base):
    __tablename__ = "plants"
    plant_id = Column(Integer, primary_key=True)
    plant_name = Column(String)
    plant_variety = Column(String)
    planting_date = Column(String)  # Change this to date format
    field_planted = Column(Integer, foreign_key="fields.field_id")
    plant_yield = Column(Integer)
    comments = Column(String)

    def __repr__(self):
        return f"""<Plant(plant_id={self.plant_id}, plant_name={self.plant_name}, 
        plant_variety={self.plant_variety}, planting_date={self.planting_date}, 
        plant_yield={self.plant_yield}, comments={self.comments})>"""


class Field(base):
    __tablename__ = "fields"
    field_id = Column(Integer, primary_key=True)
    field_name = Column(String)
    field_size = Column(Integer)
    field_owner = Column(String)
    field_plants = Column(Integer)
    field_comments = Column(String)

    def __repr__(self):
        return f"""<Field(field_id={self.field_id}, field_name={self.field_name},
        field_size={self.field_size}, field_owner={self.field_owner},
        field_plants={self.field_plants}, field_comments={self.field_comments})>"""

    field_plants = relationship(
        "Plant", backref="field"
    )  # Many plants can belong to one field


class Inventory(base):
    __tablename__ = "inventory"
    inventory_id = Column(Integer, primary_key=True)
    item_name = Column(String)
    item_quantity = Column(Integer)
    item_price = Column(Integer)
    item_comments = Column(String)

    def __repr__(self):
        return f"""<Inventory(inventory_id={self.inventory_id}, item_name={self.item_name},
        item_quantity={self.item_quantity}, item_price={self.item_price},
        item_comments={self.item_comments})>"""


class Sales(base):
    __tablename__ = "sales"
    sale_id = Column(Integer, primary_key=True)
    customer_name = Column(String, foreign_key="customers.customer_name")
    sale_date = Column(String)  # Change this to date format
    sale_item = Column(String)
    sale_quantity = Column(Integer)
    sale_price = Column(Integer)
    sale_comments = Column(String)

    def __repr__(self):
        return f"""<Sales(sale_id={self.sale_id}, customer_name={self.customer_name},
        sale_date={self.sale_date}, sale_item={self.sale_item}, 
        sale_quantity={self.sale_quantity},sale_price={self.sale_price}, 
        sale_comments={self.sale_comments})>"""


class Customers(base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    customer_address = Column(String)
    customer_phone = Column(String)
    customer_email = Column(String)

    def __repr__(self):
        return f"""<Customers(customer_id={self.customer_id}, customer_name={self.customer_name},
        customer_address={self.customer_address}, customer_phone={self.customer_phone},
        customer_email={self.customer_email})>"""


class Employees(base):
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    employee_address = Column(String)
    employee_phone = Column(String)
    employee_email = Column(String)

    def __repr__(self):
        return f"""<Employees(employee_id={self.employee_id}, employee_name={self.employee_name},
        employee_address={self.employee_address}, employee_phone={self.employee_phone},
        employee_email={self.employee_email})>"""


# Create tables
base.metadata.create_all(engine)
