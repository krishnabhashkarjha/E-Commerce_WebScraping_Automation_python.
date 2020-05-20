'''
@ Author - Karan Pandya
@ Creation date - 12/10/2018
@ Description - Utility for all database operations
'''

import psycopg2
from Utilites import AppConstants
class DatabaseUtility:

    def __init__(self, task_type, log_file_object):
        self.task_type = task_type
        self.log_file_object = log_file_object
        self.conn = None

    def connection(self):
        connection_flag = 0
        for v_host in AppConstants.db_host_list:
            try:
                self.conn = psycopg2.connect(host= v_host, database=AppConstants.db_name, user=AppConstants.db_username, password=AppConstants.db_password)
                #self.log_file_object.log_to_file('INFO', 'Successfully connected to database')
                connection_flag = 1
            except (Exception, psycopg2.DatabaseError) as error:
                connection_flag = 0
                self.log_file_object.log_to_file('ERROR', error)
            if connection_flag == 1:
                break
        if connection_flag == 1:
            return True
        else:
            return False

    def get_data_query(self, sql, data):
         cursor = self.conn.cursor()
         try:
            cursor.execute(sql, data)
            return cursor.fetchall()
         except (Exception, psycopg2.DatabaseError) as error:
              self.log_file_object.log_to_file('ERROR', error)
              rollback = 'rollback;'
              cursor.execute(rollback)
              return False

    def insert_and_update_data_query(self, sql, data):
         cursor = self.conn.cursor()
         try:
            cursor.execute(sql, data)
            self.conn.commit()
         except (Exception, psycopg2.DatabaseError) as error:
              self.log_file_object.log_to_file('ERROR', error)
              rollback = 'rollback;'
              cursor.execute(rollback)
