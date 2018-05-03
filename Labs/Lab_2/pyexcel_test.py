import pyexcel

data = [
    {
        "Name": "Huyen",
        "Age": 23
    },
    {
        "Name": "Huye",
        "Age": 24
    },
    {
        "Name": "Don",
        "Age": 21
    }
]
pyexcel.save_as(records = data, dest_file_name = "test.xlsx")