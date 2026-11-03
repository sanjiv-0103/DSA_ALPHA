def rich_custom(accounts):
    richest=0
    for customer in accounts:
        total=sum(customer)
        if total>richest:
            richest=total
    return richest