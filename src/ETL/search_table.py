def search_person(search_term, search_list):
    search_results = []
    try:
        for i in range(len(search_list)):
            if search_term in str(search_list[i].id)\
                    or search_term in search_list[i].first_name.lower()\
                    or search_term in search_list[i].last_name.lower():
                search_results.append(search_list[i])
        return search_results
    except Exception as error:
        print(error)
