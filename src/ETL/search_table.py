def search_person(search_term, search_list):
    search_results = []
    try:
        for i in range(len(search_list)):
            if search_list[i].id == search_term\
                    or search_list[i].first_name == search_term \
                    or search_list[i].last_name == search_term:
                search_results.append(search_list[i])
        return search_results
    except Exception as error:
        print(error)
