valid_ids = [1234, 1235, 1237, 2468]


def validate_id(func):
    def wrapper(*args, **kwargs):
        if 'id' not in kwargs.keys():
            print("Parameter id unknown")
        elif kwargs['id'] not in valid_ids:
            print("Invalid id {}".format(kwargs['id']))
        else:
            data = func(*args, **kwargs)
            return data
    return wrapper


@validate_id
def read_record(id=0):
    return "Read data for customer with id {}".format(id)


@validate_id
def update_record(id=0):
    return "Updated data for customer with id {}".format(id)


@validate_id
def delete_record(id=0):
    return "Deleted data for customer with id {}".format(id)


print("read_record()", read_record())
print("read_record(1234)", read_record(1234))
print("read_record(id=1234)", read_record(id=1234))
print("read_record(id=1230)",read_record(id=1230))

print("update_record(id=1234)", update_record(id=1234))
print("update_record(id=1235)",update_record(id=1235))

print("delete_record(id=2468)", delete_record(id=2468))
print("delete_record(id=1230)",delete_record(id=1230))


