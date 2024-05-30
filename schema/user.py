# Normal way
def SerializeDict(item) -> dict:
    return {**{i:str(item[i]) for i in item if i=="_id"},**{i:str(item[i]) for i in item if i!="_id"}}

def SerializeList(items) -> list:
    return [SerializeDict(item) for item in items]
    