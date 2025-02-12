import psycopg2

import ProductionCode.psqlConfig as config

class DataSource:

    def __init__(self):
        '''Constructor that initiates connection to database'''
        self.connection = self.connect()

    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.'''

        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def getExerciseByMuscle(self, muscle):
        '''Returns all exercises in the database that fit the users input for muscle group'''
        try:
            if muscle=="":

                # set up a cursor
                cursor = self.connection.cursor()

                query = "SELECT exercise_name FROM exercise_table;"

                # executing the query and saying that the type variable 
                # should be placed where %s was, the trailing comma is important!
                cursor.execute(query)
                return cursor.fetchall()

            else:
                # set up a cursor
                cursor = self.connection.cursor()

                # make the query using %s as a placeholder for the variable
                query = "SELECT exercise_name FROM exercise_table WHERE muscle_group = %s;"

                # executing the query and saying that the type variable 
                # should be placed where %s was, the trailing comma is important!
                cursor.execute(query, (muscle,))
                return cursor.fetchall()

        except Exception as e:
            return "Something went wrong when executing the by muscle query: ", e


    def getExerciseByEquipment(self, equipment):
        '''Returns all exercises in the database that fit the users input for muscle group'''
        try:
            if equipment=="":

                # set up a cursor
                cursor = self.connection.cursor()

                query = "SELECT exercise_name FROM exercise_table;"

                # executing the query and saying that the type variable 
                # should be placed where %s was, the trailing comma is important!
                cursor.execute(query)
                return cursor.fetchall()

            else:
                # set up a cursor
                cursor = self.connection.cursor()

                # make the query using %s as a placeholder for the variable
                query = "SELECT exercise_name FROM exercise_table WHERE equipment = %s;"

                # executing the query and saying that the type variable 
                # should be placed where %s was, the trailing comma is important!
                cursor.execute(query, (equipment,))
                return cursor.fetchall()

        except Exception as e:
            return "Something went wrong when executing the by equipment query: ", e

    
    def getURLByName(self, name):
        '''Returns the description_URL for the exercise called name'''

        cursor = self.connection.cursor()

        query = "SELECT description_URL FROM exercise_table WHERE exercise_name = %s;"
        cursor.execute(query, (name,))
        return cursor.fetchall()
