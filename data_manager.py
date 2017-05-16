import psycopg2


def run_query(query):
    try:
        # setup connection string
        connect_str = "dbname='birop' user='birop' host='localhost' password='postgreSQL_birop'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # run a query
        cursor.execute("""{}""".format(query))
        # Fetch and print the result of the last execution
        if query.upper().startswith("SELECT"):
            rows = cursor.fetchall()
        else:
            rows = "Done"
        return rows
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def main():
    pass

if __name__ == '__main__':
    main()