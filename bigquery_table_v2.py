import pandas_gbq


def query_bq():
    project_id = PROJECT_ID
    table_id = TABLE_ID
    # Can query for time range
    sql = """
            SELECT *
            FROM `project.table_name`
          """

    df = pandas_gbq.read_gbq(sql, project_id = project_id)
    pandas_gbq.to_gbq(df, table_id, project_id = project_id, if_exists = "append")