def create_sql_list(params):
    tmplist = []
    for key,value in params.items():
        tmplist.append("'" + str(value) + "'")

    return "("+ (",".join(tmplist)) + ")"
        
def create_sql_select_list(params):
    pass
