import streamlit as st

from models import Field, Inventory, Plant, Sales, Session


def main():
    st.title("Welcome to the Farm Management App")
    st.sidebar.title("Menu")

    session = Session()
    plants = session.query(Plant).all()
    field = session.query(Field).all()
    inventory = session.query(Inventory).all()
    sales = session.query(Sales).all()

    st.table(plants)
    st.table(field)
    st.table(inventory)
    st.table(sales)
    session.close()


if __name__ == "__main__":
    main()
